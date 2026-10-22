# Codebase-specific test frameworks

Source: [Google Rust Style Guide](https://github.com/google/styleguide/blob/2ac1584cd3c9854760f02418ec24687ec1698fb8/rustguide.md#L1791-L1804); adapted under [CC BY 3.0](../LICENSE).

<a id="test-framework"></a>

## Use the right per-codebase test framework

Most codebases use their own specific test framework rather than `#[test]`.

*   Chrome Use
    [rust_gtest_interop](https://source.chromium.org/chromium/chromium/src/+/main:testing/rust_gtest_interop/).
    This makes it possible to integrate Rust tests into C++ test binaries.

*   Fuchsia Use `#[fuchsia::test]`. See
    [here](https://fuchsia.dev/fuchsia-src/development/languages/rust/testing.md)
    for more details.
