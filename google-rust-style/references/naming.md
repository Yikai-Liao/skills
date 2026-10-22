# Naming

Source: [Google Rust Style Guide](https://github.com/google/styleguide/blob/2ac1584cd3c9854760f02418ec24687ec1698fb8/rustguide.md#L1020-L1109); adapted under [CC BY 3.0](../LICENSE).

<a id="naming"></a>

## Naming

<a id="naming-methods"></a>

### Naming methods

Follow the Rust standard library style for naming methods. See also the guidance
on
[naming conventions](https://google.github.io/comprehensive-rust/idiomatic/foundations-api-design/predictable-api/naming-conventions.html)
in the Comprehensive Rust course.

Specific considerations:

*   Use prefixes such as `as_...()`, `to_...()`, or `into_...()` with the
    appropriate `self` convention. See also
    [this section](https://rust-lang.github.io/api-guidelines/naming.html#ad-hoc-conversions-follow-as_-to_-into_-conventions-c-conv)
    of the Rust API Guidelines and the Clippy lint
    [`wrong_self_convention`](https://rust-lang.github.io/rust-clippy/master/index.html#wrong_self_convention).

<a id="lifetimes"></a>

### Naming lifetimes

Lifetimes should have descriptive names, especially type lifetimes.

Exceptions:

*   Type lifetimes that are extremely generic abstractions like `Cow`.
*   It is fine to use anonymous lifetimes (`'_`) where they work.
*   Single-character lifetimes are okay when they are simply expressing the
    relationship between a method’s input and output, or needed for a local
    higher-ranked lifetime bounds (`for<'a>`). Up to two such local lifetimes
    are fine, if more are needed, we strongly advise you to use descriptive
    names.

<a id="generic-parameters"></a>

### Naming generic parameters

Use a short name for your generic parameters (either single or multi character),
related to the kind of thing they represent. Single-letter generics are okay,
but the letter chosen should be somewhat indicative of the object type, ideally
taken from the most important trait bound.

`T` or `U` are fine when the generics are in a relatively unbound context; i.e.
it is an API intended for use with most types, like `Vec<T>`.

<a id="naming-extension-traits"></a>

### Naming extension traits

When naming an [extension trait](types-and-traits.md#extension-traits), give the name an `~Ext`
suffix (for example, `ForeignTypeExt`).

<a id="naming-initialization-functions"></a>

### Naming initialization functions

Follow these guidelines when naming initialization functions:

*   Constructors: Use `new()`, or `new_with_foo()` if there is more than one. If
    the constructor returns a `Result`, use `try_new()`.

*   Value-to-value conversions: Use `from_foo()` with an associated `From` impl.
    See
    [here](https://doc.rust-lang.org/std/convert/trait.From.html#when-to-implement-from)
    for details on when an operation can be considered to be a value-to-value
    conversion.

<a id="avoid-abbreviations"></a>

### Avoid abbreviations

Don't use abbreviations (especially acronyms and initialisms) that someone
outside your project is unlikely to know. Don't abbreviate by deleting letters
within a word.

See also the
[Google C++ Style Guide](https://google.github.io/styleguide/cppguide.html#General_Naming_Rules).

Exceptions:

*   Common abbreviations found in Wikipedia.
*   Abbreviations that are unlikely to be confusing to people outside of your
    project, for example `IpAddr`. You and your reviewer should make this
    determination. In general, the preference should still be not to abbreviate.
