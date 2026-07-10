# Scholarly Source Discovery And Retrieval

Use this reference when discovering papers, resolving a DOI or arXiv ID, verifying metadata, generating citation records, or acquiring full text and supplementary materials.

## Contents

1. Retrieval contract
2. Search, triage, fetch, and persist
3. Site routes
4. arXiv HTML-first full-text cache
5. Recency-led arXiv retrieval
6. Metadata and citation records
7. PDF and supplement acquisition
8. Validation and deduplication
9. Source manifest
10. Failure handling

## 1. Retrieval Contract

Separate three operations:

- **discovery** finds candidate papers;
- **resolution** maps a title or identifier to a stable landing page;
- **acquisition** obtains the metadata, full text, figures, data, or supplements actually used.

Do not create a citation from model memory or a search-result snippet. Fetch a stable paper, proceedings, repository, review-platform, DOI, or publisher page first. Record the exact source URL and retrieval date. Use full text when a claim depends on methods, results, limitations, evaluation protocols, or numerical values.

Respect access controls and rate limits. Follow openly exposed links; do not bypass authentication or guess private download URLs.

When the `huggingface-papers` skill is available in the current environment, read that skill and use it as the first route for two operations: discovering candidate papers and obtaining a specified paper's readable Markdown. This priority applies even to arXiv papers: do not start with an arXiv search, Atom query, HTML request, or local arXiv conversion while `huggingface-papers` can perform the requested discovery or Markdown-acquisition operation. Fall back to the arXiv workflow only when `huggingface-papers` is unavailable, fails to complete that operation, or does not cover the paper. Record the fallback reason in the source manifest. This routing preference does not replace the requirement to confirm manuscript-critical metadata against a primary paper, proceedings, repository, DOI, or publisher record.

## 2. Search, Triage, Fetch, And Persist

For each query family:

1. **Discover** candidates with `huggingface-papers` when it is available. Otherwise, **WebSearch** the review's problem, mechanism, evidence type, application, controversy, or time window.
2. **Triage** the results. Keep peer-reviewed venue pages, authoritative preprints, prior surveys, benchmarks, datasets, and relevant critiques. Reject duplicate, off-scope, marketing, blog, slide, and unsupported pages.
3. **WebFetch** or open the most authoritative landing page for each retained candidate.
4. Extract title, ordered authors, year, venue, work type, DOI or repository ID, abstract, canonical URL, and available artifact links.
5. Append the paper ledger, citation record, and source manifest immediately rather than waiting for the whole query batch.
6. Fetch the full text or supplements only when deeper evidence is needed. For a requested readable Markdown version, try `huggingface-papers` first when available, then use the source-specific fallback below.

For known DOI or arXiv inputs, resolve the identifier directly instead of searching by title. For recency-led work, use date-sorted feeds rather than relevance search alone.

Treat search engines and scholarly aggregators as discovery surfaces. Prefer the paper's repository, proceedings, review-platform, DOI-resolved publisher, or journal page for final metadata.

## 3. Site Routes

### arXiv

```text
Abstract page: https://arxiv.org/abs/<id>
HTML:         https://arxiv.org/html/<id>
PDF:          follow the PDF link from the abstract or Atom record
Batch API:    https://export.arxiv.org/api/query?search_query=<encoded-query>&max_results=<n>
Known IDs:    https://export.arxiv.org/api/query?id_list=<comma-separated-ids>
```

Parse the Atom record for title, ordered authors, abstract, `published`, `updated`, categories, DOI, journal reference, abstract URL, and PDF URL. Store the base arXiv ID separately from an optional version such as `v2`.

Treat the abstract or Atom record as the metadata authority and HTML as a full-text representation. HTML availability is incomplete, especially for older or conversion-resistant submissions, so a valid arXiv ID does not imply a valid `/html/` page.

### Semantic Scholar

```text
Paper page: https://www.semanticscholar.org/paper/<slug>/<id>
Graph API:  https://api.semanticscholar.org/graph/v1/paper/<paper-id>
```

Use Semantic Scholar to discover papers, recover cross-identifiers, and inspect citation relations. Request only needed fields when the API permits field selection. Confirm final author, year, venue, DOI, and publication status against a primary paper or venue record when they control a manuscript claim.

### OpenReview

```text
Forum page: https://openreview.net/forum?id=<id>
```

Use the forum page to retrieve the submission title, authors, abstract, PDF link, revision state, and public venue or decision information. Do not present a submission as accepted without public evidence of acceptance or proceedings publication.

### NeurIPS

```text
Proceedings path: https://papers.nips.cc/paper_files/paper/<year>/...
```

Open the proceedings landing page and follow its paper, BibTeX, and supplementary links. Do not invent a hash or PDF path from the title; use the links exposed by the actual page because formats vary by year.

### DOI, Journal, And Conference Pages

```text
DOI landing page: https://doi.org/<doi>
```

Normalize the DOI by removing `doi:` or a `doi.org` prefix and trailing citation punctuation. Resolve it to the publisher landing page, then extract canonical metadata, correction or retraction status, license, PDF, and supplementary links. For venues without a DOI, use the official journal, conference, proceedings, or discipline-repository page.

## 4. arXiv HTML-First Full-Text Cache (Fallback)

If `huggingface-papers` is available, use it first to obtain a readable Markdown version of an arXiv paper. Use this arXiv route only after the conditional fallback rule above is met.

For the arXiv fallback route, use this order:

1. an already cached Markdown reading copy and its raw HTML;
2. official `https://arxiv.org/html/<id-or-version>`;
3. the openly available PDF and local PDF text extraction;
4. the abstract alone, with access depth marked accordingly.

HTML-first reduces repeated PDF parsing and usually preserves headings, paragraphs, citations, captions, tables, and TeX annotations. It is an optimization, not a change in evidence standards. Keep the raw HTML as the acquired artifact and the Markdown as a derived reading copy. Agents should read the `.md` by default, not inject raw HTML into context. For exact equations, complex tables, figure details, footnotes, or claims whose wording matters, inspect the cached HTML and use the PDF as a cross-check when necessary.

Once close reading begins, pin the exact version exposed by the HTML document's `<base>` URL or a versioned final URL, such as `2312.02445v4`. Do not silently replace a version-specific reading copy with the latest version. Relate base and versioned IDs in the source manifest.

### Cache And Convert

Use the bundled converter when its dependencies can be supplied by `uv`:

```bash
uv run /path/to/survey-md/scripts/cache_arxiv_html.py \
  2312.02445 \
  --output survey-workspace/sources/arxiv-html
```

The cache contains, per identifier:

- `.html`: untouched official response;
- `.md`: local reading copy;
- `.json`: requested and final URL, retrieval time, status, type, size, checksum, validators, and failure state.

The converter extracts only `article.ltx_document`, reconstructs mathematics from LaTeXML's `application/x-tex` annotations, removes conversion-only front matter, and resolves relative links against the document's `<base>` URL. It deliberately leaves figure URLs remote instead of downloading every image. Download only figures needed for an evidence claim, observing the same request pacing.

Do not use a generic HTML-to-Markdown conversion without checking the result. Naive conversion can concatenate visible MathML, TeX annotations, and accessibility text into corrupt expressions; it can also leave relative figure links unusable. Direct MarkItDown conversion showed this failure mode in an arXiv LaTeXML sample, so MarkItDown is acceptable only after arXiv-specific pre-cleaning or after representative formula checks pass. The bundled path pre-cleans LaTeXML and then uses a smaller Markdown converter. At minimum, verify the title, abstract, section headings, equations, tables, references, and absence of artifacts such as `start_POSTSUBSCRIPT`.

### Rate And Cache Discipline

- Check the local cache before every request. Do not re-fetch a successful entry unless freshness matters.
- Make at most one HTML availability request per uncached paper in a pass. Serialize requests and leave at least three seconds between them; the bundled tool defaults to five seconds.
- Use Atom `id_list` or a query response for metadata rather than opening one abstract page per paper solely to recover metadata.
- Negative-cache a 404 or structurally invalid HTML response. Fall back to PDF immediately and do not probe the same HTML URL again in the current run; the bundled tool defaults to a 30-day negative cache.
- Refresh only deliberately, using `ETag` or `Last-Modified` validators when present. A conditional request is still a request and must be paced.
- On `429` or a server-unavailable response, honor `Retry-After` when present, stop the batch, and resume later. Do not add parallel workers or aggressive automatic retries.
- Use an identifiable user agent for scripted retrieval. If the workflow will run repeatedly or at scale, include a real contact route supplied by the operator.

Record HTML success as `html-fulltext`, a derived Markdown copy as `html-derived-markdown`, and a negative probe as `html-unavailable` in the source manifest. A cached Markdown file never upgrades the evidence depth beyond what the underlying HTML actually contains.

## 5. Recency-Led arXiv Retrieval

Use the Atom API with explicit submission-date ordering when the request asks for the latest work:

```text
https://export.arxiv.org/api/query?search_query=<encoded-query>&sortBy=submittedDate&sortOrder=descending&max_results=<n>
```

Repeat the query for each major subtopic rather than relying on one broad feed. Inspect the returned `published` field against the requested window. Record which queries were date-sorted in `01-search-coverage.md`.

Do not assume familiar model or method names represent the current frontier. A recent-work claim must be backed by a source retrieved from the requested window.

## 6. Metadata And Citation Records

For every retained paper, record:

- exact title from the fetched record;
- full ordered author list;
- publication or preprint year and the meaning of that year;
- venue or repository status;
- DOI, arXiv ID, OpenReview ID, or another stable identifier;
- canonical landing URL;
- discovery query or source;
- retrieval date and access depth: metadata, abstract, full text, or supplement.

When BibTeX is requested or already used by the project, generate it from fetched metadata:

```bibtex
@inproceedings{key,
  title={Exact title from the source page},
  author={Ordered author list},
  booktitle={Venue},
  year={YYYY},
  doi={DOI when available},
  url={Fetched canonical URL},
}
```

Use `@article` and `journal` for journal articles. Represent an unpublished arXiv item as an arXiv preprint and preserve its arXiv ID. Escape format-sensitive characters and protect acronym capitalization when the citation toolchain requires it.

Do not let a fixed bibliography count override relevance. Every citation must trace to a fetched record and serve the review's evidence or context.

## 7. PDF And Supplement Acquisition

For non-arXiv sources, or after the arXiv HTML-first route is unavailable or insufficient, acquire materials in this order:

1. Fetch the article, preprint, proceedings, or DOI-resolved landing HTML.
2. Record metadata, abstract, captions, and every openly exposed PDF, supplement, source-data, code, correction, and high-resolution figure link.
3. Download only the artifacts needed by the review, preserving original filenames or a reversible mapping.
4. Fetch a correction's landing page and supplements separately when they affect the evidence being discussed.
5. Try the main PDF when openly available. If gated, continue with usable landing-page and supplementary material.

Inspect page links for terms such as `supp`, `supplement`, `source data`, `additional file`, `MEDIA`, `MOESM`, `mmc`, `pdf`, `xlsx`, and high-resolution figure variants. Publisher landing pages may expose supplement or figure files on separate CDN domains even when the main PDF is unavailable. Follow only URLs present in the page.

Do not claim full-text verification when only an abstract, caption, or metadata page was available. Conversely, do not mark the whole paper unavailable when its authoritative metadata or openly linked supplements remain accessible.

## 8. Validation And Deduplication

Validate every acquired artifact before using it:

- record the requested and final redirected URL;
- record retrieval time, status, content type, filename, and byte size;
- verify a PDF is a real PDF rather than an HTML login or error page;
- verify cached arXiv HTML contains the paper body rather than an error shell, and validate the derived Markdown against representative equations, tables, captions, and references;
- verify archives, spreadsheets, images, and documents open with the expected parser;
- compute a checksum when an artifact supports a central claim or must be reproduced.

Deduplicate in this order:

1. normalized DOI;
2. arXiv base ID and version relation;
3. OpenReview or proceedings identifier;
4. cross-identifiers from Semantic Scholar;
5. normalized title, first author, and year as a candidate match requiring confirmation.

Treat a preprint and published paper as related manifestations rather than automatically counting both as independent works. Preserve version-specific evidence when their methods, results, or claims differ.

For a preprint whose later versions change the title, method name, author list, or substantive content, do not collapse the old and current method names into a slash-separated alias. Cite the exact version supporting the manuscript claim, use that version's verified short work name on first mention, and record the version transition in the source manifest and paper note. A stable arXiv base ID does not imply stable content across versions.

## 9. Source Manifest

Maintain `01a-source-manifest.md` with one row per successful or failed retrieval:

| Work key | Artifact | Identifier | Requested URL | Final URL | Retrieved at | Status | Type/size | Checksum | Evidence use | Notes |
|---|---|---|---|---|---|---|---|---|---|---|

Keep failed attempts. They document access boundaries and prevent repeated dead ends. Link every included ledger row and paper note to its metadata record and deepest available evidence surface.

## 10. Failure Handling

- **No result**: vary the exact title, author, identifier, venue, and query vocabulary; record attempted variants.
- **Metadata conflict**: preserve both records, prefer the primary paper or venue record, and document the choice.
- **Rate limit**: reduce batch size, serialize requests, respect server guidance, and retry later.
- **arXiv HTML unavailable**: negative-cache the result, fall back to the PDF, and do not mistake HTML absence for paper absence.
- **arXiv Markdown corruption**: retain the raw HTML, repair the structural conversion or read the relevant HTML section directly, and cross-check exact equations or tables against the PDF.
- **Authentication or subscription gate**: record the gap and try openly linked repository, landing-page, correction, or supplement routes; do not bypass controls.
- **HTML saved as PDF**: reject it as full text, retain the landing HTML as a limited source, and mark the access depth honestly.
- **JavaScript-only page**: use an available browser renderer or another authoritative landing page.
- **Unavailable supplement**: name the missing artifact and avoid claims that require it.
