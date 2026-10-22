# Accessors and API evolution

## Contents

- [Getters and setters](#getters-and-setters)
- [More on accessors that accept closures](#closure-accessors)
- [Implement expected API sets together](#expected-api-sets)
- [Do not access items marked `#[doc(hidden)]` that you don't own](#doc-hidden)
- [Use `const` functions responsibly](#const-functions)
- [Avoid overloading for non-mathematical purposes](#operator-overloads)
- [Apply `#[non_exhaustive]` to publicly-exposed enums](#non-exhaustive-enums)
- [Apply `#[non_exhaustive]` to public structs with public fields](#non-exhaustive-structs)
- [`#[must_use]` on functions](#must-use-on-functions)
- [`#[must_use]` on types](#must-use-on-types)
- [Do not run code before `main()`](#global-initialization)

<a id="getters-and-setters"></a>

### Getters and setters

Writing and naming getters and setters should follow these guidelines:

*   `foo()` for a getter that returns a `T` by value.
*   `foo_mut()` for a getter that returns a `&mut T`.
*   `take_foo()` for a getter that "clears" the value (by setting it to `None`
    or some other default state) and returns the old value.
*   `set_foo()` for a setter that takes a `T` by value.
*   `with_foo()` / `with_mut_foo()` for an accessor that operates via a closure
    (see details [below](#closure-accessors)). Such an accessor is invoked as
    `object.with_foo(|foo| frob(foo))`.
*   `replace_foo()` for a setter that returns the old value.

Examples

```rs
impl Stuff {
   fn foo(&self) -> &Foo { ...  }
   fn foo_mut(&mut self) -> &mut Foo { ... }

   /// Sets "baz" property to `None` and returns the old value.
   fn take_baz(&mut self) -> Option<Baz> { ... }

   fn set_foo(&mut self, foo: Foo) { ... }

   /// Calls `f` with a borrow of the "bar" property.
   /// Returns the return value of `f`.
   fn with_bar<R>(&self, f: impl FnOnce(&Bar) -> R) -> R { ... }

   /// Calls `f` with a mutable borrow of the "bar" property.
   /// Returns the return value of `f`.
   fn with_mut_bar<R>(&self, f: impl FnOnce(&mut i32) -> R) -> R { ... }

   /// Sets "foo" property to `foo` and returns the old value.
   fn replace_foo(&mut self, foo: Foo) -> Foo  { ... }
}
```

<a id="closure-accessors"></a>

#### More on accessors that accept closures

Accessors that accept a closure (`.with_foo()`) are typically invoked as
`object.with_foo(|foo| do_something_with(foo))`. They can be a good choice in
the following situations:

*   When the property is contained in an interior mutability wrapper (e.g.
    `Mutex` or `RefCell`). These mechanisms need to constrain access to the
    property to a scope, and the closure provides this scope. This is usually
    preferable to directly returning the RAII object that implements the scope
    (e.g. `MutexGuard<T>`) because the latter would leak an implementation
    detail.

*   When follow-up work or validation is needed after a property is changed and
    a `set_foo()` accessor cannot be used (for example because the property's
    type is expensive to clone or cannot be cloned at all).

A `with_foo()` accessor will often allow the closure to return a value and
forward it by returning it from `with_foo()`.

If you need to provide two closure-accepting accessors, one for read-only access
and one for mutable access, it is common to name them `with_foo()` and
`with_mut_foo()`. Otherwise, `with_foo()` is often also used for mutating
accessors.

<a id="expected-api-sets"></a>

### Implement expected API sets together

If you implement `len()`, also implement `is_empty()`. For context, see Clippy
lint
[`len_without_is_empty`](https://rust-lang.github.io/rust-clippy/master/index.html#len_without_is_empty).

<a id="doc-hidden"></a>

### Do not access items marked `#[doc(hidden)]` that you don't own

Treat items marked `#[doc(hidden)]` as private. Don't access them unless you own
the code.

<a id="const-functions"></a>

### Use `const` functions responsibly

Mark a public function as `const` only if you expect it to remain `const` in the
future (or can commit to helping clients migrate when it changes).

Rationale

It’s a breaking change to turn a `const` function into a regular function.

<a id="operator-overloads"></a>

### Avoid overloading for non-mathematical purposes

Use operator overloads for their original mathematical/logical purpose, not just
to make the code more concise (as "syntax sugar").

<a id="non-exhaustive-enums"></a>

### Apply `#[non_exhaustive]` to publicly-exposed enums

If an enum is part of a public API used by other teams, mark it
`#[non_exhaustive]`.

Exceptions:

*   The enum will never change. For example:
    *   Enums describing an existing ontology (e.g., `enum Color { Red, Green,
        Blue }`).
    *   Enums with two states that could be Booleans (e.g., `enum Visibility {
        Visible, Hidden }`)
*   The enum *may* change in the future, but you are committed to fixing
    resulting breakages via an LSC.

For context, see Clippy lint
[`exhaustive_enums`](https://rust-lang.github.io/rust-clippy/master/index.html#exhaustive_enums).

Rationale

Marking an enum `#[non_exhaustive]` forces users to include a wildcard arm (`_
=> ...`) in `match` statements. This ensures code continues to compile when new
variants are added to the enum later.

This rule is primarily important for enums used across team boundaries, because
the scope of the breakage could be significant. Enums used only a small number
of times can't create a large breakage and thus may ignore this rule.

<a id="non-exhaustive-structs"></a>

### Apply `#[non_exhaustive]` to public structs with public fields

Structs with public fields that are part of a public API used by other teams
should be marked `#[non_exhaustive]`.

Exceptions:

*   The struct fields are unlikely to change, e.g., because they describe an
    existing ontology (e.g., a Rectangle type) or the reviewer can otherwise be
    confident that they will not change.
*   The struct fields *may* change in the future, but you are committed to
    fixing resulting breakages via an LSC.
*   You want to enable your users to use functional record update (FRU) struct
    initialization syntax (`Person { name: "foo", ..Default::default() }`).

Rationale

Adding a new field (even a private one) to a struct with all public fields is a
breaking change, because callers can no longer name all fields in a struct
literal.

A `#[non_exhaustive]` struct can't be constructed with the struct literal
syntax, except for the code in the same crate. This allows new private fields to
be added without breaking users.

This rule is primarily important for structs used across team boundaries,
because the scope of the breakage could be significant. Structs used only a
small number of times can't create a large breakage and thus may ignore this
rule.

<a id="must-use-on-functions"></a>

### `#[must_use]` on functions

Use `#[must_use]` on functions in these cases:

*   The caller cannot use the function correctly if they ignore the return
    value. This includes pure functions (functions without side effects), such
    as `HashMap::get()`.

*   Any function whose return value represents an error or otherwise critical
    information about the function's behavior. If the return type is already
    annotated `#[must_use]` (which is true of `Result`, for example), the
    function does not need to be annotated `#[must_use]`.

<a id="must-use-on-types"></a>

### `#[must_use]` on types

Use `#[must_use]` on types intended to be returned by functions that would
otherwise be annotated `#[must_use]` according to the
[rules above](#must-use-on-functions).

Examples:

*   The type is an error type (similar to `Result` or `StatusOr`).

*   The type represents a lazily evaluated computation. In other words, the
    function call doesn't do anything by itself, and the return value needs to
    be accessed to cause some desired side effect.

<a id="global-initialization"></a>

### Do not run code before `main()`

Do not cause code to run before `main()`, for example by using techniques such
as the [ctor crate](https://docs.rs/ctor/latest/ctor/).
