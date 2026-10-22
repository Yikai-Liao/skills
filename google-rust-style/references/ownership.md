# Ownership, borrowing, and cloning

Source: [Google Rust Style Guide](https://github.com/google/styleguide/blob/2ac1584cd3c9854760f02418ec24687ec1698fb8/rustguide.md#L486-L530); adapted under [CC BY 3.0](../LICENSE).

<a id="ownership-borrowing"></a>

## Ownership and borrowing

<a id="avoid-rc-arc"></a>

### Avoid `Rc` and `Arc`

Prefer unique ownership and borrowing over `Rc` and `Arc` for managing memory.

Exception:

*   Use `Rc` and `Arc` when the alternative ownership and borrowing structure
    would be unreasonably complex to write, understand, or maintain. This is a
    judgment call to be discussed during code review.

Rationale

Generally, Rust allows representing object graphs without using shared ownership
smart pointers. These pointers add runtime overhead and their own unique
complexity. Engineers coming from other languages might tend to use `Rc` and
`Arc` too quickly.

<a id="prefer-borrows"></a>

### Prefer borrows over deep copies

Use `.clone()` when you genuinely need a deep copy of an object.

Avoid using `.clone()` as a substitute for borrowing. Design code that works
naturally with Rust's ownership and borrowing rules. However, if the borrowing
relationships become excessively complex, `.clone()` can be a pragmatic choice.

Consider the performance needs of the code while choosing between cloning and
borrowing.

Note: This advice does not apply to cloning `Rc` or `Arc` pointers. Cloning
reference-counted pointers does not create a deep copy, and is an expected way
to use them.

Rationale

Deep copies can be expensive to make due to memory allocation and data copying.
