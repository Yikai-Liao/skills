---
name: google-rust-style
description: Apply Google's Rust Style Guide when writing, refactoring, or reviewing Rust under Google-style conventions, including API design, ownership, imports, and documentation for general Rust/Cargo projects. Use when the user requests this guide or the project adopts it; not as a blanket policy for all Rust projects.
---

# Google Rust Style

Apply the guide to the code being changed. Identify whether the code is a reusable library or a single application before selecting rules.

## Shared judgments

- For library code, API-design rules are binding under this guide. For application code, they are strong recommendations: favor simplicity and directness over premature generalization.
- Keep each retained rule's strength and exceptions. A preference is not a prohibition. This edition omits codebase-specific policies; use the project's own Cargo layout, runtime, and test framework rather than inferring restrictions from the upstream guide.
- Follow the public Rust Style Guide and Rust API Guidelines where they do not conflict with this guide. The project's adoption policy determines how strictly this guide applies. For authority, rationale, or conflicts, read [scope and priorities](references/scope-and-priorities.md).

## Read by decision

Read only the references relevant to the changed code or requested review. Follow a cross-reference when its linked condition affects the decision; do not load every file for a local edit.

| Decision in the task | Read |
|---|---|
| Module organization, re-exports, globs, function/type/trait imports | [Organization and imports](references/organization-and-imports.md) |
| Formatter settings, invisible characters, or rustfmt skip | [Formatting](references/formatting.md) |
| Borrowing versus deep copies or shared ownership (`Rc` / `Arc`) | [Ownership](references/ownership.md) |
| Borrowed input types, iterators versus collections, `Into`, bool flags, `Option` / `Result` / panic contracts | [Function contracts](references/function-contracts.md) |
| Newtypes, named fields, trait design, generics versus dyn, derives, standard traits, constructors | [Types and traits](references/types-and-traits.md) |
| Handling poisoned locks | [Concurrency](references/concurrency.md) |
| Macros versus ordinary Rust or code generation | [Macros](references/macros.md) |
| Method, lifetime, generic, constructor, extension-trait names, abbreviations | [Naming](references/naming.md) |
| Public API docs, panic/safety contracts, doc syntax, or implementation comments | [Documentation](references/documentation.md) |
| Unsafe implementation, safety justification, benchmarks, or unstable features | [Safety and stability](references/safety-and-stability.md) |
| Accessors, closure access, expected API sets, hidden items, const, operators, non_exhaustive, must_use, pre-main code | [API evolution](references/api-evolution.md) |
| Inference, matching, expect/unwrap, assertions, iterator chains, catch_unwind, string formatting | [Implementation](references/implementation.md) |

## Apply and review

For a proposed change or finding, connect the applicable rule to the actual code and check its exceptions before recommending a fix. When requirements overlap, read both topics: for example, an unsafe public API needs safety and documentation guidance; a public enum and its callers need API-evolution and implementation guidance; panic contracts and recovery need function-contracts and implementation guidance.

The references retain upstream examples, including illustrative fragments and bad examples. Treat them as explanations of style, not tested drop-in code. Do not silently repair the source examples or infer broader permissions from them.

For source revision and licensing, see [NOTICE.md](NOTICE.md). This is an unofficial adaptation, not a Google-published skill.
