# Implementation, matching, assertions, and iteration

## Contents

- [Don't overuse type inference](#type-inference)
- [Prefer pattern matching over check-then-unwrap](#dont-check-then-unwrap)
- [Prefer `expect` over `unwrap`](#expect-over-unwrap)
- [Don't omit patterns on `non_exhaustive` enums when matching](#non-exhaustive-enum-matching)
- [Use context strings to clarify assertions](#assertion-context)
- [Don't use iterator combinator chains when direct iteration is clearer](#combinator-chains)
- [Don't call `panic::catch_unwind`](#catch-unwind)
- [Prefer `format!` / `write!` for concatenation and substitution](#prefer-format-or-write)

## Implementation concerns

<a id="type-inference"></a>

### Don't overuse type inference

Add enough explicit types so that someone familiar with the codebase can figure
out what the inferred types are.

Prefer to add the types to variable declarations, rather than as
[turbofishes](https://doc.rust-lang.org/reference/glossary.html#turbofish). If
the compiler forces you to add a turbofish, it is generally fine to add a `_`
inference marker.

Specific situations in which you should probably add types:

*   When calling methods with a generic return type, such as `.into()` or
    `.parse()`.
*   For the result of complex iterator chains.

<a id="dont-check-then-unwrap"></a>

### Prefer pattern matching over check-then-unwrap

Avoid potentially panicking operations when the input data guarantees they
cannot panic. For example, instead of using `Option::unwrap` on a value known to
be valid, use pattern matching to prove correctness to the compiler.

**Good:**

```rust
// Good: The match arm proves to the compiler that `x` is `Some`.
// A panic is obviously not possible.
if let Some(value) = option {
    use_value(value);
}
```

**Bad:**

```rust
// Bad: Correctness of `unwrap` relies on a runtime check that `option` is `Some`.
if option.is_some() {
    use_value(option.unwrap());
}
```

<a id="expect-over-unwrap"></a>

### Prefer `expect` over `unwrap`

If a panic is necessary because an invariant cannot be expressed in the type
system, prefer `expect` over `unwrap` to document the reason.

<a id="non-exhaustive-enum-matching"></a>

### Don't omit patterns on `non_exhaustive` enums when matching

Prefer to list all enum variants in `match` statements over `non_exhaustive`
enums.

If you don't care about specific variants, place them in the wildcard arm. If
you *only* care about specific variants, use an `if let` or a `let … else {}`.

Examples:

```rust
#[non_exhaustive]
pub enum Shape {
    Circle,
    Square,
    Triangle,
}
```

**Good:**

```rust
fn process_shape(shape: Shape) {
  match shape {
    Shape::Circle => println!("It's a circle"),
    Shape::Square => println!("It's a square"),
    // Triangle and any future variants don't require any actions.
    Shape::Triangle | _ => {}
  }
}
```

**Good:**

```rust
fn process_shape(shape: Shape) {
  if let Shape::Circle = shape {
    println!("It's a circle"),
  }
}
```

**Bad:**

```rust
fn process_shape(shape: Shape) {
  match shape {
    Shape::Circle => println!("It's a circle"),
    _ => {}
  }
}
```

Exceptions:

*   You only care about specific variants *and* `match` is cleaner than `if
    let`.

This is covered by the built-in lint `non_exhaustive_omitted_patterns` which you
can enable on your code.

<a id="assertion-context"></a>

### Use context strings to clarify assertions

While some assertions are self-explanatory, many benefit from additional context
that clarifies why an assertion is expected to hold, or what caused it to be
violated. Use the optional format string argument for `assert!` to convey this
context.

You should always consider adding context, but particularly in the following
situations:

*   If you're thinking of adding a comment to the assertion. Use a format string
    instead: It has the benefit that it will appear in logs.
*   If you expect failing assertions to be seen by users. In this case, a
    human-readable explanation is more helpful than a Rust expression.
*   If logging a value helps in understanding why the assertion failed.
*   To clarify whether a failing assertion means that
    *   The client misused an API (i.e., they should change their use of the
        API), or
    *   The implementation contains a bug (i.e., the client should file a bug
        report).

Examples

**Explaining why an assertion should hold**

**Good:**

```rust
    assert!(
        values.is_sorted(),
        "`values` is populated from a `PriorityQueue`, so we expect it to be sorted"
    );
```

**Logging a value to clarify why the assertion failed**

**Good:**

```rust
assert!(refund > 0, "Refund must be positive, got {refund:?});
```

**Flagging misuse of an API**

**Good:**

```rust
impl Database {
    ...

    fn execute_query(&self, query: &str) {
        assert!(self.stream.is_some(), "Call connect() before executing queries");
    }

    ...
}
```

**Don't use the context string merely to repeat the condition**

**Bad:**

```rust
assert(!values.is_sorted(), "values should always be sorted");
```

<a id="combinator-chains"></a>

### Don't use iterator combinator chains when direct iteration is clearer

Avoid using combinator chains in ways that hurt readability. Specifically:

*   Avoid long and complex combinator chains.
*   Don't construct combinator chains in the header of a `for` loop. Instead,
    assign the combinator chain to a variable, then consume that variable in the
    `for` loop.
*   Avoid `Iterator::for_each` unless you're convinced you have a good reason. A
    `for` loop is usually easier to read.

Combinators *are* preferable for shorter chains and for cases where the
combinator itself provides a lot of logic that would otherwise have to be
written out in the corresponding `for` loop.

Examples

**Complex combinator chains**

Here's an example of a combinator chain that is hard to read because it involves
conditionals and mutates external state:

**Bad:**

```rust
let mut error_count = 0;
let _processed_items: Vec<_> = items
    .into_iter()
    .map(transformation_that_may_fail)
    .map(|result| {
        if result.is_err() {
            error_count += 1;
        }
        result
    })
    .filter_map(Result::ok)
    .collect();
```

The corresponding `for` loop is easier to read:

**Good:**

```rust
let mut error_count = 0;
let mut processed_items = Vec::with_capacity(items.len());

for item in items {
    match transformation_that_may_fail(item) {
        Ok(val) => processed_items.push(val),
        Err(_) => error_count += 1,
    }
}
```

**Combinator chains in for loops**

Avoid constructing a combinator chain in the header of a `for` loop:

**Bad:**

```rust
for bug in bug_descriptions
    .iter()
    .filter_map(|description| parse_bug_description(description).ok())
    .filter(|bug| bug.priority <= Priority::P1)
{
    assign_bug(bug);
}
```

Instead, assign the combinator chain to a variable. This reduces clutter, and
the variable name documents what the combinator chain does:

**Good:**

```rust
let urgent_bugs = bug_descriptions
    .iter()
    .filter_map(|description| parse_bug_description(description).ok())
    .filter(|bug| bug.priority <= Priority::P1);

for bug in urgent_bugs {
    assign_bug(bug);
}
```

**When to prefer a combinator chain**

Here's an example where a combinator chain is preferable:

**Good:**

```rust
let threshold_exceeded = values.iter().any(|&v| v > threshold);
```

The corresponding for loop is harder to read and reinvents the logic contained
in `any()`:

**Bad:**

```rust
let mut threshold_exceeded = false;
for v in values {
  if v > threshold {
    threshold_exceeded = true;
    break;
  }
}
```

<a id="catch-unwind"></a>

### Don't call `panic::catch_unwind`

Use of `panic::catch_unwind` is prohibited in first-party Rust code.

Exceptions:

*   It is acceptable as a defense in depth mechanism as long as it is never
    *relied* upon for any properties. A codebase that is already attempting to
    avoid panics may choose to wrap critical entry points with a `catch_unwind`
    recovery mechanism just in case a panic slips through. Code authors must
    convince the reviewer that the codebase is doing most of what it can to
    avoid panics. This exception only applies to code that has the possibility
    of being run with `panic=unwind`.

Rationale

Rust code may be used in many environments, and `panic::catch_unwind` will only
function correctly in environments with `panic=unwind`.

<a id="prefer-format-or-write"></a>

### Prefer `format!` / `write!` for concatenation and substitution

Prefer `format!()` and `write!()` to other alternatives in the following
situations:

*   To concatenate more than two strings. For example, use
    `format!("{a}{b}{c}")` instead of `a + b + c`.
*   To perform substitutions on a literal string (instead of using
    `str::replace`).

Rationale

*   `format!` / `write!` require fewer allocations than concatenating strings
    using `+`.
*   Prefer standard format strings to inventing your own templating syntax.
