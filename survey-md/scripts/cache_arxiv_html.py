#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.10"
# dependencies = [
#   "beautifulsoup4>=4.12,<5",
#   "markdownify>=1.2,<2",
# ]
# ///
"""Cache official arXiv HTML and make a cleaner Markdown reading copy."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import time
from dataclasses import asdict, dataclass
from datetime import datetime, timedelta, timezone
from html import unescape
from pathlib import Path
from typing import Iterable
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin, urlparse
from urllib.request import Request, urlopen

from bs4 import BeautifulSoup, NavigableString, Tag
from markdownify import markdownify


ARXIV_ID_RE = re.compile(
    r"^(?:[a-z-]+(?:\.[A-Z]{2})?/\d{7}|\d{4}\.\d{4,5})(?:v\d+)?$", re.I
)
DEFAULT_OUTPUT = Path("survey-workspace/sources/arxiv-html")
MINIMUM_INTERVAL_SECONDS = 3.0


@dataclass
class CacheRecord:
    arxiv_id: str
    requested_url: str
    final_url: str | None
    document_base: str | None
    resolved_arxiv_id: str | None
    checked_at: str
    status: str
    http_status: int | None = None
    content_type: str | None = None
    byte_size: int | None = None
    sha256: str | None = None
    etag: str | None = None
    last_modified: str | None = None
    retry_after: str | None = None
    note: str | None = None


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def iso_now() -> str:
    return utc_now().replace(microsecond=0).isoformat()


def normalize_arxiv_id(value: str) -> str:
    candidate = value.strip()
    if ":" in candidate and candidate.lower().startswith("arxiv:"):
        candidate = candidate.split(":", 1)[1]
    if "://" in candidate:
        parsed = urlparse(candidate)
        if parsed.netloc.lower() not in {"arxiv.org", "www.arxiv.org"}:
            raise ValueError(f"not an arXiv URL: {value}")
        parts = [part for part in parsed.path.split("/") if part]
        if len(parts) < 2 or parts[0] not in {"abs", "html", "pdf"}:
            raise ValueError(f"unsupported arXiv URL: {value}")
        candidate = "/".join(parts[1:])
    candidate = candidate.removesuffix(".pdf")
    if not ARXIV_ID_RE.fullmatch(candidate):
        raise ValueError(f"invalid arXiv identifier: {value}")
    return candidate


def safe_name(arxiv_id: str) -> str:
    return arxiv_id.replace("/", "_")


def read_json(path: Path) -> dict[str, object] | None:
    if not path.exists():
        return None
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None
    return value if isinstance(value, dict) else None


def write_record(path: Path, record: CacheRecord) -> None:
    path.write_text(
        json.dumps(asdict(record), ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def negative_cache_is_fresh(record: dict[str, object] | None, days: int) -> bool:
    if not record or record.get("status") != "html-unavailable":
        return False
    checked_at = record.get("checked_at")
    if not isinstance(checked_at, str):
        return False
    try:
        checked = datetime.fromisoformat(checked_at)
    except ValueError:
        return False
    if checked.tzinfo is None:
        checked = checked.replace(tzinfo=timezone.utc)
    return utc_now() - checked < timedelta(days=days)


def tex_from_math(math: Tag) -> str:
    annotation = math.find("annotation", attrs={"encoding": "application/x-tex"})
    raw = (
        annotation.get_text("", strip=False) if annotation else math.get("alttext", "")
    )
    return unescape(str(raw)).strip()


def document_base_from_html(html: str, source_url: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    base = soup.find("base", href=True)
    base_href = base.get("href") if isinstance(base, Tag) else None
    return (
        urljoin(source_url, str(base_href))
        if base_href
        else source_url.rstrip("/") + "/"
    )


def resolved_id_from_document_base(document_base: str) -> str | None:
    match = re.search(r"/html/([^/]+)/?$", urlparse(document_base).path)
    return match.group(1) if match else None


def stash_math(replacements: list[str], value: str) -> str:
    token = f"ARXIVMATHPLACEHOLDER{len(replacements):06d}TOKEN"
    replacements.append(value)
    return token


def replace_equations(soup: BeautifulSoup, root: Tag, replacements: list[str]) -> None:
    for table in list(root.select("table.ltx_equation")):
        math = table.find("math")
        if math is None:
            continue
        tex = tex_from_math(math)
        if not tex:
            continue
        number_node = table.select_one(".ltx_tag_equation")
        number = number_node.get_text(" ", strip=True) if number_node else ""
        block = soup.new_tag("div")
        block["class"] = ["arxiv-equation"]
        block.append(NavigableString(stash_math(replacements, f"\n$$\n{tex}\n$$\n")))
        if number:
            label = soup.new_tag("p")
            label.string = number
            block.append(label)
        table.replace_with(block)


def replace_remaining_math(root: Tag, replacements: list[str]) -> None:
    for math in list(root.find_all("math")):
        tex = tex_from_math(math)
        if not tex:
            math.replace_with(NavigableString(math.get_text("", strip=True)))
            continue
        if math.get("display") == "block":
            replacement = f"\n\n$$\n{tex}\n$$\n\n"
        else:
            replacement = f"${tex}$"
        math.replace_with(NavigableString(stash_math(replacements, replacement)))


def absolutize_links(root: Tag, document_base: str) -> None:
    for node, attribute in [(node, "href") for node in root.find_all(href=True)]:
        value = node.get(attribute)
        if isinstance(value, str) and not value.startswith(("#", "mailto:", "data:")):
            node[attribute] = urljoin(document_base, value)
    for node, attribute in [(node, "src") for node in root.find_all(src=True)]:
        value = node.get(attribute)
        if isinstance(value, str) and not value.startswith("data:"):
            node[attribute] = urljoin(document_base, value)


def convert_html_to_markdown(html: str, source_url: str, retrieved_at: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    root = soup.select_one("article.ltx_document")
    if root is None:
        raise ValueError("response does not contain article.ltx_document")

    document_base = document_base_from_html(html, source_url)

    for selector in [
        "script",
        "style",
        ".ltx_author_notes",
        ".ltx_note_frontmatter",
        ".ltx_tag_item",
    ]:
        for node in list(root.select(selector)):
            node.decompose()

    authors = root.select_one(".ltx_authors")
    if authors is not None:
        names = [
            node.get_text(" ", strip=True) for node in authors.select(".ltx_personname")
        ]
        names = [name for name in names if name]
        if names:
            authors.clear()
            authors.append(NavigableString("Authors: " + ", ".join(names)))

    keywords = root.select_one(".ltx_keywords")
    if keywords is not None:
        value = keywords.get_text(" ", strip=True)
        if value:
            keywords.clear()
            keywords.append(NavigableString("Keywords: " + value))

    abstract_title = root.select_one(".ltx_title_abstract")
    if abstract_title is not None:
        abstract_title.name = "h2"
        abstract_title.string = "Abstract"

    math_replacements: list[str] = []
    replace_equations(soup, root, math_replacements)
    replace_remaining_math(root, math_replacements)
    absolutize_links(root, document_base)

    body = markdownify(str(root), heading_style="ATX", bullets="-").strip()
    for index, value in enumerate(math_replacements):
        body = body.replace(f"ARXIVMATHPLACEHOLDER{index:06d}TOKEN", value)
    provenance = (
        f"<!-- Cached from {source_url} at {retrieved_at}. "
        "This Markdown is a derived reading copy; retain the HTML for exact structure. -->"
    )
    return provenance + "\n\n" + body + "\n"


def validate_html(payload: bytes, content_type: str | None) -> str:
    if content_type and "html" not in content_type.lower():
        raise ValueError(f"unexpected content type: {content_type}")
    text = payload.decode("utf-8")
    if "article" not in text or "ltx_document" not in text:
        raise ValueError("response is not an arXiv LaTeXML article")
    return text


def fetch_one(
    arxiv_id: str,
    output: Path,
    user_agent: str,
    refresh: bool,
    negative_cache_days: int,
) -> tuple[str, bool]:
    stem = safe_name(arxiv_id)
    html_path = output / f"{stem}.html"
    md_path = output / f"{stem}.md"
    record_path = output / f"{stem}.json"
    record = read_json(record_path)

    if html_path.exists() and md_path.exists() and not refresh:
        return f"cached {arxiv_id}: {md_path}", False
    if html_path.exists() and not refresh:
        checked_at = str(record.get("checked_at") or iso_now()) if record else iso_now()
        source_url = (
            str(
                record.get("document_base")
                or record.get("final_url")
                or f"https://arxiv.org/html/{arxiv_id}"
            )
            if record
            else f"https://arxiv.org/html/{arxiv_id}"
        )
        try:
            text = validate_html(html_path.read_bytes(), "text/html")
            md_path.write_text(
                convert_html_to_markdown(text, source_url.rstrip("/"), checked_at),
                encoding="utf-8",
            )
            return f"converted-cached-html {arxiv_id}: {md_path}", False
        except (OSError, ValueError, UnicodeDecodeError) as exc:
            result = CacheRecord(
                arxiv_id=arxiv_id,
                requested_url=f"https://arxiv.org/html/{arxiv_id}",
                final_url=None,
                document_base=None,
                resolved_arxiv_id=None,
                checked_at=iso_now(),
                status="html-unavailable",
                note=f"invalid local HTML cache: {exc}",
            )
            write_record(record_path, result)
            return f"html-unavailable {arxiv_id}: invalid local HTML cache", False
    if negative_cache_is_fresh(record, negative_cache_days) and not refresh:
        return f"negative-cache {arxiv_id}: HTML previously unavailable", False

    requested_url = f"https://arxiv.org/html/{arxiv_id}"
    headers = {"User-Agent": user_agent, "Accept": "text/html,application/xhtml+xml"}
    if refresh and record:
        if isinstance(record.get("etag"), str):
            headers["If-None-Match"] = str(record["etag"])
        if isinstance(record.get("last_modified"), str):
            headers["If-Modified-Since"] = str(record["last_modified"])

    request = Request(requested_url, headers=headers)
    checked_at = iso_now()
    try:
        with urlopen(request, timeout=45) as response:
            payload = response.read()
            content_type = response.headers.get("Content-Type")
            text = validate_html(payload, content_type)
            final_url = response.geturl()
            document_base = document_base_from_html(text, final_url)
            resolved_arxiv_id = resolved_id_from_document_base(document_base)
            html_path.write_bytes(payload)
            md_path.write_text(
                convert_html_to_markdown(text, document_base.rstrip("/"), checked_at),
                encoding="utf-8",
            )
            record_value = CacheRecord(
                arxiv_id=arxiv_id,
                requested_url=requested_url,
                final_url=final_url,
                document_base=document_base,
                resolved_arxiv_id=resolved_arxiv_id,
                checked_at=checked_at,
                status="html-cached",
                http_status=response.status,
                content_type=content_type,
                byte_size=len(payload),
                sha256=hashlib.sha256(payload).hexdigest(),
                etag=response.headers.get("ETag"),
                last_modified=response.headers.get("Last-Modified"),
            )
            write_record(record_path, record_value)
            return f"fetched {arxiv_id}: {md_path}", True
    except HTTPError as exc:
        if exc.code == 304 and html_path.exists():
            text = html_path.read_text(encoding="utf-8")
            source_url = (
                str(
                    record.get("document_base")
                    or record.get("final_url")
                    or requested_url
                )
                if record
                else requested_url
            )
            md_path.write_text(
                convert_html_to_markdown(text, source_url.rstrip("/"), checked_at),
                encoding="utf-8",
            )
            if record:
                record["checked_at"] = checked_at
                record["status"] = "html-cached"
                record_path.write_text(
                    json.dumps(record, ensure_ascii=False, indent=2) + "\n",
                    encoding="utf-8",
                )
            return f"not-modified {arxiv_id}: {md_path}", True
        status = "html-unavailable" if exc.code == 404 else "http-error"
        result = CacheRecord(
            arxiv_id=arxiv_id,
            requested_url=requested_url,
            final_url=exc.geturl(),
            document_base=None,
            resolved_arxiv_id=None,
            checked_at=checked_at,
            status=status,
            http_status=exc.code,
            content_type=exc.headers.get("Content-Type"),
            retry_after=exc.headers.get("Retry-After"),
            note=str(exc.reason),
        )
        write_record(record_path, result)
        return f"{status} {arxiv_id}: HTTP {exc.code}", True
    except (ValueError, UnicodeDecodeError) as exc:
        result = CacheRecord(
            arxiv_id=arxiv_id,
            requested_url=requested_url,
            final_url=None,
            document_base=None,
            resolved_arxiv_id=None,
            checked_at=checked_at,
            status="html-unavailable",
            note=str(exc),
        )
        write_record(record_path, result)
        return f"html-unavailable {arxiv_id}: {exc}", True
    except (URLError, TimeoutError) as exc:
        result = CacheRecord(
            arxiv_id=arxiv_id,
            requested_url=requested_url,
            final_url=None,
            document_base=None,
            resolved_arxiv_id=None,
            checked_at=checked_at,
            status="fetch-error",
            note=str(exc),
        )
        write_record(record_path, result)
        return f"fetch-error {arxiv_id}: {exc}", True


def run_selftest() -> None:
    fixture = """<!doctype html><html><head><base href="/html/2401.00001v2/"></head><body>
    <nav>outside</nav><article class="ltx_document"><h1>Fixture Paper</h1>
    <div class="ltx_authors"><span class="ltx_personname">A. Author</span><span class="ltx_author_notes">author-noise</span></div>
    <div class="ltx_abstract"><h6 class="ltx_title_abstract">Abstract.</h6><p>Body
    <math display="inline" alttext="x_i"><annotation encoding="application/x-tex">x_i</annotation></math>.</p></div>
    <span class="ltx_note_frontmatter">noise</span>
    <table class="ltx_equation"><tr><td><math display="block"><annotation encoding="application/x-tex">y=x^2</annotation></math></td><td><span class="ltx_tag_equation">(1)</span></td></tr></table>
    <img src="x1.png" alt="figure"><table><tr><th>A</th><th>B</th></tr><tr><td>1</td><td>2</td></tr></table>
    <section class="ltx_bibliography"><h2>References</h2></section></article></body></html>"""
    result = convert_html_to_markdown(
        fixture, "https://arxiv.org/html/2401.00001v2", "2026-01-01T00:00:00+00:00"
    )
    required = [
        "# Fixture Paper",
        "Authors: A. Author",
        "## Abstract",
        "$x_i$",
        "$$\ny=x^2\n$$",
        "https://arxiv.org/html/2401.00001v2/x1.png",
        "| A | B |",
        "## References",
    ]
    for value in required:
        assert value in result, value
    for forbidden in ["outside", "noise", "author-noise", "start_POSTSUBSCRIPT"]:
        assert forbidden not in result, forbidden
    print("selftest ok")


def parse_args(argv: Iterable[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("identifiers", nargs="*", help="arXiv IDs or arxiv.org URLs")
    parser.add_argument(
        "--output", type=Path, default=DEFAULT_OUTPUT, help="cache directory"
    )
    parser.add_argument(
        "--refresh", action="store_true", help="conditionally refresh cached HTML"
    )
    parser.add_argument("--negative-cache-days", type=int, default=30)
    parser.add_argument(
        "--min-interval",
        type=float,
        default=5.0,
        help="seconds between network requests; floor is 3",
    )
    parser.add_argument("--user-agent", default="survey-md-arxiv-cache/1.0")
    parser.add_argument("--selftest", action="store_true")
    return parser.parse_args(argv)


def main(argv: Iterable[str] | None = None) -> int:
    args = parse_args(argv)
    if args.selftest:
        run_selftest()
        return 0
    if not args.identifiers:
        print("at least one arXiv identifier is required", file=sys.stderr)
        return 2
    if args.negative_cache_days < 0:
        print("--negative-cache-days must be non-negative", file=sys.stderr)
        return 2

    try:
        identifiers = [normalize_arxiv_id(value) for value in args.identifiers]
    except ValueError as exc:
        print(exc, file=sys.stderr)
        return 2

    args.output.mkdir(parents=True, exist_ok=True)
    interval = max(MINIMUM_INTERVAL_SECONDS, args.min_interval)
    last_request_finished: float | None = None
    exit_code = 0
    for arxiv_id in dict.fromkeys(identifiers):
        if last_request_finished is not None:
            remaining = interval - (time.monotonic() - last_request_finished)
            if remaining > 0:
                time.sleep(remaining)
        message, used_network = fetch_one(
            arxiv_id=arxiv_id,
            output=args.output,
            user_agent=args.user_agent,
            refresh=args.refresh,
            negative_cache_days=args.negative_cache_days,
        )
        print(message)
        if used_network:
            last_request_finished = time.monotonic()
        if message.startswith(("http-error", "fetch-error")):
            exit_code = 1
        if "HTTP 429" in message or "HTTP 503" in message:
            print("server asked to slow down; stopping this batch", file=sys.stderr)
            break
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
