"""Self-authored starting implementation; not a recommended refactoring."""

import csv
import io


def import_catalog(text, store):
    rows = csv.DictReader(io.StringIO(text))
    items = []
    seen = set()
    for row in rows:
        sku = row["sku"].strip()
        if not sku:
            raise ValueError("empty sku")
        if sku in seen:
            raise ValueError("duplicate sku")
        price_cents = int(row["price_cents"])
        if price_cents < 0:
            raise ValueError("negative price")
        seen.add(sku)
        items.append((sku, price_cents))
    store.replace(items)
    return len(items)
