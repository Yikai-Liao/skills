# Catalog import contract

Implement `import_catalog(text, store)` using Python's standard library. `text` is CSV with `sku` and `price_cents` columns. Read it with `csv.DictReader(io.StringIO(text))`; preserve that reader's field and quoting behavior. For each row, in input order:

1. Read `row["sku"]` and strip its ends. Reject an empty SKU with `ValueError("empty sku")`.
2. Reject a SKU already encountered after stripping with `ValueError("duplicate sku")`.
3. Convert `row["price_cents"]` with `int()`. Propagate its exception type and arguments unchanged. Reject a negative price with `ValueError("negative price")`.
4. Keep the `(sku, price_cents)` pair, in input order.

Missing keys retain `KeyError`; a missing cell retains the exception produced by the specified operation. Do not add defaults, convert error types, or catch errors to return a partial result. If more than one condition fails, the first failure in the order above wins.

Only after every row succeeds, call `store.replace(items)` exactly once and return the count. Empty input and a header with no data both replace with `[]` and return `0`. If `replace` fails, propagate that same failure and do not return success. There is no retry, partial commit, or new public API. The store owns how replacement is persisted.
