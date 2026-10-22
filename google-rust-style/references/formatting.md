# Formatting and formatter exceptions

<a id="code-formatting"></a>

## Code formatting and aesthetics

<a id="formatting-other"></a>

### Use the appropriate formatting tool

Use the appropriate formatting tool.

Configuration (for style guide authors)

A codebase may choose to not apply the following `rustfmt` options if they care
about building on stable and the option is unavailable on their stable Rust:

*   Maximum of 100 columns per line:
    [`max_width = 100`](https://rust-lang.github.io/rustfmt/?version=v1.6.0&search=#max_width)

*   Usage of lowercase alphabets in hex literals (`0xab123cdef` as opposed to
    `0xAB123CDEF`):
    [`hex_literal_case = Lower`](https://rust-lang.github.io/rustfmt/?version=v1.6.0&search=#hex_literal_case)

*   Macro matcher formatting:
    [`format_macro_matchers = true`](https://rust-lang.github.io/rustfmt/?version=v1.6.0&search=#format_macro_matchers)

*   Usage of escapes for invisible characters in literals. E.g., if you wish to
    have text containing a Zero-Width joiner, use `\u{200D}`.

<a id="formatting-optout"></a>

### Opting out of automatic formatting

You may opt out of automatic formatting using `#[rustfmt::skip]`, but only in
the following situations:

*   **Manual alignment** – If you have a situation-specific reason to have a
    snippet of code line up in a particular way (e.g., multiple similar lines of
    code that you want to remain aligned for readability, or a
    matrix-constructing function).
*   **Generated code** (ideally, use a genrule instead).

Important: Formatting should not be skipped for personal style choices.
