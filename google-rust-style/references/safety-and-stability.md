# Unsafe code and unstable features

Source: [Google Rust Style Guide](https://github.com/google/styleguide/blob/2ac1584cd3c9854760f02418ec24687ec1698fb8/rustguide.md#L1205-L1248); adapted under [CC BY 3.0](../LICENSE).

<a id="other-features"></a>

## Other Rust features

<a id="unsafe"></a>

### Unsafe code

Don't write unsafe code unless there is no way to implement the same
functionality with safe code.

If you do have to write unsafe code:

*   Encapsulate unsafe code in a safe abstraction and isolate it from business
    logic as much as possible. Ideally, unsafe code should be in a separate
    crate with few dependencies beyond the standard library.
*   Add a safety comment starting with `SAFETY:` that explains why the code is
    correct.
*   Add a technical justification for unsafe code. Depending on context, this
    can be a justification for an individual unsafe block or a more general
    justification that covers an entire file or build target. The justification
    should answer these questions:
    *   Why is this code not written in an equivalent safe way?
    *   If the reason is performance, are there benchmarks?

<a id="unstable-features"></a>

### No unstable features

Don't use unstable features.
