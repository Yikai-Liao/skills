# Function parameters, returns, and errors

## Contents

- [Function inputs and outputs](#inputs-and-outputs)
- [Accept flexible references for immutable data](#flexible-references)
- [Iterators vs. owned collections in return types](#return-iterators)
- [Iterators vs. slices in function parameters](#accept-iterators)
- [Accepting `Into`](#accepting-into)
- [Prefer `enum` over `bool` in APIs](#enum-vs-bool)
- [Reporting errors](#reporting-errors)

<a id="inputs-and-outputs"></a>

## Function inputs and outputs

<a id="flexible-references"></a>

### Accept flexible references for immutable data

When functions accept borrowed, immutable data, use a reference type that
affords the most flexibility. Pass references to the data itself instead of
references to smart pointers, containers, or wrappers.

<!-- mdformat off(keep table rows on single lines for Kramdown compatibility in the public style guide) -->

| Use          | Instead of   | Why?                                                         |
| ------------ | ------------ | ------------------------------------------------------------ |
| `&T`         | `&Box<T>`    | Borrow the data inside the box                               |
| `&[T]`       | `&Vec<T>`    | Accept any slice instead of specific containers              |
| `&str`       | `&String`    | Accept a string slice instead of references to owned strings |
| `Option<&T>` | `&Option<T>` | Borrow the data inside the Option                            |

<!-- mdformat on -->

Exceptions:

*   When expecting non-linear character data such as Rope/Cord.

For context, see Clippy lints
[`borrowed_box`](https://rust-lang.github.io/rust-clippy/master/index.html#borrowed_box)
and
[ptr_arg](https://rust-lang.github.io/rust-clippy/master/index.html#ptr_arg).

Rationale

Accepting reference types that don't mention specific smart pointers,
containers, or wrappers makes functions more versatile and performant: callers
can pass data held in a variety of ways without copying it first.

<a id="return-iterators"></a>

### Iterators vs. owned collections in return types

Prefer returning iterators (either concrete types or `impl Iterator`) where
possible over returning `Vec<T>`.

Note: In application code, returning a `Vec<T>` is fine if it simplifies the
code and if flexibility and performance advantages of iterators are not clearly
needed.

Exceptions:

*   Most callers will need to construct an owned vector.
*   The function's implementation naturally constructs a vector.
*   The returned value will likely need to be randomly indexed.
*   The algorithm works better as a `for` loop and the forced allocation doesn't
    matter too much.
*   The function's intended purpose is creating a new owned collection.
*   The function is returning a pre-existing vector.

Rationale

Highly reusable library code generally should strive to provide more flexible
and performant APIs. Returning an iterator allows callers to choose how to
consume the data: collect it into a vector, process it in a loop, or chain
further iterator adapters. Some of these options allow users to avoid
unnecessary allocations.

In application code, the usage patterns for a function are often easier to
predict. If it is clear that performance is not a concern, or that data would be
collected into a vector anyway, returning a vector makes for a simpler API.

<a id="accept-iterators"></a>

### Iterators vs. slices in function parameters

Highly reusable library code should accept iterators or `impl IntoIterator` if
it only needs to iterate over the input.

Note: In application code, accepting a slice `&[T]` is fine if it simplifies the
code and if flexibility and performance advantages of iterators are not clearly
needed.

Rationale

Highly reusable library code generally should strive to provide more flexible
and performant APIs. Functions that accept iterators offer callers:

*   More flexibility (data can be supplied from any collection)
*   Efficiency (data does not need to be copied into a contiguous piece of
    memory)
*   Composability (the function works better with iterator chains)

In application code, the usage patterns for a function are often easier to
predict. If it is clear that performance is not a concern, or that callers would
always have a vector anyway, accepting a slice makes for a simpler API.

<a id="accepting-into"></a>

### Accepting `Into`

When designing library APIs that accept a `T` but users are likely to have
various types, consider accepting `impl Into<T>` instead of `T` if **call-site
ergonomics are paramount**.

Tip: This should be balanced against code bloat concerns; it is not a
requirement to use lots of `Into<T>` in your code.

Note: Application code should almost never use `impl Into<T>` parameters.

Rationale

Using `impl Into<T>` allows a function to directly accept various arguments of
various compatible types. For example, a function accepting `impl Into<String>`
could be called with a `String` or a `&str` literal directly.

The tradeoff here is balancing the convenience of avoiding a `.into()` at the
callsite against the cost of generics (more complex API signature, increased
code size, sometimes even type inference difficulties).

<a id="enum-vs-bool"></a>

### Prefer `enum` over `bool` in APIs

Use `enum` function parameters instead of `bool` in cases where the purpose of
the parameter is not obvious.

If you do use `bool`, consider using an inline comment to document the purpose
of the `bool` in an argument list.

<a id="reporting-errors"></a>

### Reporting errors

Choose the error reporting mechanism that fits your API contract: `Option`,
`Result`, or `panic!`.

**Use `Option` for simple failures** where the cause is obvious and the caller
would not benefit from further details. This is best for standard, anticipated
outcomes like a missing value or a parsing mismatch.

**Good:**

```rust
// Good: The cause of the failure is obvious (integer overflow). No further
// details could be reasonably provided.
fn checked_add(a: u32, b: u32) -> Option<u32> { ... }
```

**Use `Result` for recoverable failures where the caller needs context** to
handle the error. These are often "unavoidable" errors caused by external
factors (like I/O or network) that even correctly implemented code cannot
prevent with checks ahead of time. Nevertheless, the caller can reasonably
anticipate the kinds of errors (a file-related function can fail with an I/O
error). The error details allow the caller to distinguish failure modes and
recover appropriately.

**Good:**

```rust
// Good: The caller needs to know *why* it failed (NotFound vs PermissionDenied).
fn open_file(path: &Path) -> Result<File, io::Error> { ... }
```

**Use `panic!` to report bugs and violated invariants.** These errors are
avoidable: the program is missing a check, and is calling an operation without
fulfilling a precondition. These defects must be fixed in the code, not handled
at runtime, although coarse-grained recovery might be possible with
`catch_unwind`.

**Good:**

```rust
// Good: Panics if the invariant (index must be in bounds) is violated.
// This indicates a bug in the caller's logic.
impl<T> MyVec<T> {
    pub fn remove(&mut self, index: usize) -> T {
        if index >= self.len() {
            panic!("index out of bounds");
        }
        // ...
    }
}
```

Note: Some codebases may choose to avoid panics entirely, and require even
broken invariants to be reported via `Result`.

Exceptions:

*   Developer-facing binaries may use panics for non-fatal errors.
*   Tests may use panics for assertions.
