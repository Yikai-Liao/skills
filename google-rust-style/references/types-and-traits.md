# Types and traits

Source: [Google Rust Style Guide](https://github.com/google/styleguide/blob/2ac1584cd3c9854760f02418ec24687ec1698fb8/rustguide.md#L722-L957); adapted under [CC BY 3.0](../LICENSE).

## Contents

- [Types](#types)
- [Newtypes versus type aliases](#newtypes-vs-type-aliases)
- [Prefer named fields over tuples and non-newtype tuple structs](#prefer-named-fields)
- [Traits](#traits)
- [Add trait implementations when they become necessary](#traits-yagni)
- [Implement known standard library traits instead of custom methods](#known-traits)
- [Use `#[derive()]` if possible](#derive)
- [Generics versus `dyn Trait`](#generics-vs-dyn-trait)
- [When to define a trait versus an inherent implementation](#trait-vs-inherent-impl)
- [Extension traits](#extension-traits)
- [Specific guidance for important traits](#important-traits)
- [Pair important `From` impls with explicit constructor methods](#from-impls)
- [Options structs should implement Default](#options-should-implement-default)

<a id="types"></a>

## Types

<a id="newtypes-vs-type-aliases"></a>

### Newtypes versus type aliases

Use a
[newtype](https://doc.rust-lang.org/rust-by-example/generics/new_types.html)
instead of a type alias in the following cases:

*   If the type you are defining has notable semantic differences.
*   For types that warrant an API of their own.
*   If you want the flexibility to change the underlying type later, especially
    if you don't control all usages of your type.
*   For type safety, if it’s easy for the types to get mixed up. For example, a
    `Date` type may use newtypes to distinguish `Day`, `Month`, and `Year`
    numbers in its internal calculations.

<a id="prefer-named-fields"></a>

### Prefer named fields over tuples and non-newtype tuple structs

Prefer types with named fields over tuples, as tuple indexes (`.0`, `.1`, ...)
quickly become confusing.

Exceptions:

*   Newtype tuple structs (tuple structs with only one field).
*   In very local contexts where there is unlikely to be any confusion.

<a id="traits"></a>

## Traits

<a id="traits-yagni"></a>

### Add trait implementations when they become necessary

As a general rule, low-level library code should anticipate users' needs
proactively, while application code should add trait impls as needed.

<a id="known-traits"></a>

### Implement known standard library traits instead of custom methods

If a method matches the purpose and behavior of a standard library trait,
implement that trait. For example, instead of writing `fn from_str(&str) ->
Self` on `Foo`, you should `impl FromStr for Foo`.

It is acceptable to have both the method and the trait impl for discoverability
reasons.

For context, see Clippy lint
[`should_implement_trait`](https://rust-lang.github.io/rust-clippy/master/index.html#should_implement_trait)
([list of traits](https://github.com/rust-lang/rust-clippy/blob/928349795f9f28f54e69bd0f0ffeed33de5e272a/clippy_lints/src/methods/mod.rs#L3940-L3971)).

<a id="derive"></a>

### Use `#[derive()]` if possible

Manual implementations should be avoided if they can be expressed as a
`#[derive()]`.

<a id="generics-vs-dyn-trait"></a>

### Generics versus `dyn Trait`

In libraries, prefer accepting generics (`T: Trait` or `impl Trait`) in function
parameters over `dyn Trait`.

Exceptions:

*   Cases where code size matters.

Rationale

-   Efficiency

    -   Additional indirection: Creating a `dyn Trait` requires setting up a fat
        pointer, and a vtable lookup is required for every call of a function on
        the trait.
    -   If a function takes a `dyn Trait`, the compiler can't perform certain
        optimizations that it could if the function was generic, such as
        inlining calls to functions of the trait.

-   Some traits are not
    [`dyn` compatible](https://doc.rust-lang.org/reference/items/traits.html#dyn-compatibility).
    For example, a trait is not `dyn` compatible if it has generic functions,
    associated functions without a `self` parameter, or functions that return
    `Self`.

<a id="trait-vs-inherent-impl"></a>

### When to define a trait versus an inherent implementation

Define a trait only for the following purposes:

*   To enable generic programming (to use `T: Trait` in constraints of generic
    functions and types).

*   To accept or return an `impl Trait` or `dyn Trait`.

*   To define an [extension trait](#extension-traits) (but see also the caveats
    in the section on extension traits).

In all other cases where you want to implement functionality for a type, use an
[inherent implementation](https://doc.rust-lang.org/std/keyword.impl.html#inherent-implementations).

Don't use traits merely to organize code.

<a id="extension-traits"></a>

### Extension traits

An
[extension trait](https://rust-lang.github.io/rfcs/0445-extension-trait-conventions.html)
is a trait that adds methods to a type from a different crate.

What differentiates an extension trait from other traits is that its sole
purpose is to add methods to the type; it is not intended for use in generics
(`T: Trait`, `impl Trait`) or dynamic dispatch (`dyn Trait`). To indicate this,
the name of an extension trait should carry the suffix `~Ext` (for example,
`ForeignTypeExt`).

In general, the team that owns the original type should also own the extension
trait.

Exceptions:

*   Extension methods that are expected to become well known and provide
    significant value, for example, in foundational libraries / frameworks.

Note: This rule is specifically about extension traits. It is relatively common
to define a trait as an input trait (e.g., `DateLike`) and implement it on a
bunch of foreign types.

Examples

```rust
extern crate foreign_crate;
use foreign_crate::ForeignType;

trait ForeignTypeExt {
  fn additional_method(&self);
}

impl ForeignTypeExt for ForeignType {
  fn additional_method(&self) { ... }
}
```

It is also possible to define an extension trait for every type that implements
some foreign trait. Effectively, this is equivalent to adding default methods to
the foreign trait:

```rust
extern crate foreign_crate;
use foreign_crate::ForeignTrait;

trait ForeignTraitExt {
  fn additional_method(&self);
}

impl<T: ForeignTrait> ForeignTraitExt for T {
  fn additional_method(&self) { ... }
}
```

Rationale

When the same team owns the extension trait and the type being extended, this
helps avoid method name conflicts between the base type and the extension trait
or between two extension traits.

<a id="important-traits"></a>

### Specific guidance for important traits

*   **Types with public fields**: Consider implementing traits implemented by
    all subfields.

*   **Error types**: Implement the `Copy` trait whenever possible. `Copy` types
    are simpler to manage and propagate because they can be passed by value
    without moving ownership. An example of a case where this is not possible is
    if the error must contain non-`Copy` fields like a `String`.

*   **`Copy`**: Implement whenever it is reasonably clear that the type will
    continue to be `Copy` in the future.

*   **`Clone`**: Most types should implement `Clone` unless they represent some
    external resource.

*   **`Default`**: Implement if the type implements `new()` or otherwise has a
    default state. For context, see Clippy lint
    [`new_without_default`](https://rust-lang.github.io/rust-clippy/master/index.html#new_without_default).

*   **`PartialEq`** / **`Eq`**: If you want users to use the `==` operator,
    prefer implementing `PartialEq` over `Eq`. When you do implement `Eq`, be
    aware of the additionally required reflexivity (details:
    https://doc.rust-lang.org/std/cmp/trait.Eq.html).

*   **`PartialOrd`** / **`Ord`**: If you want users to use the `<` or `>`
    operators, prefer implementing `PartialOrd` over `Ord`. When you do
    implement `Ord`, be aware that it requires total ordering (details:
    https://doc.rust-lang.org/std/cmp/trait.Ord.html).

*   **Map keys**

    *   If you think it is likely that a type will be used as a map key or
        otherwise cached, implement `Hash` and `Eq`.
    *   If, in addition, the type has a clear total ordering, implement `Ord`
        (and any traits it needs).

<a id="from-impls"></a>

### Pair important `From` impls with explicit constructor methods

If a type has an important `From` impl that is expected to be one of the primary
ways of constructing it, add an inherent `::new()`, `::new_from_foo()`¸ or
`::from_foo()` method.

<a id="options-should-implement-default"></a>

### Options structs should implement Default

Structs with all-public fields that are primarily used as a “bag of options” for
a function should implement `Default`.

Rationale

This enables convenient use of struct update syntax (`Struct { a: 0,
..Default::default()}` ).
