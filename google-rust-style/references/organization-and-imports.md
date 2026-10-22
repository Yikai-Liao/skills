# Crates, modules, and imports

## Contents

- [Code organization](#code-organization)
- [Name source files and leaf modules after the primary user-defined item](#userdefined-item)
- [Don’t implement APIs in non-leaf modules](#non-leaf-modules)
- [Don’t use glob imports](#glob-imports)
- [A `use` statement should import items from one module](#use-statement)
- [Prefer locally-scoped trait imports](#prefer-local-trait-imports)
- [Qualify calls to top-level functions with a module name](#toplevel-functions)
- [Type names should be imported and used unqualified](#type-names)

<a id="code-organization"></a>

## Code organization

*Terminology:*

*   A *crate* is a unit of compilation. A crate always contains a nameless Rust
    module, the "root module".

*   A Rust *module* is a unit of code organization within a crate. Rust modules
    are used to control visibility of names. Modules can be nested. They can
    also be used to split code across files and directories.

<a id="userdefined-item"></a>

### Name source files and leaf modules after the primary user-defined item

When a `leaf module` has a primary user-defined item (e.g., `Foo`), the module
should be named after that item (e.g., `mod foo` and `foo.rs`).

Leaf modules that are not primarily about any particular abstraction can be
named as desired.

Rationale

This makes it easy to identify the content/purpose of a source file or leaf
module at a glance.

<a id="non-leaf-modules"></a>

### Don’t implement APIs in non-leaf modules

The only items in non-leaf modules should be module declarations (not
definitions) and `re-exports`.

Note that the definition of `leaf modules` allows the following sub-modules:
`mod test` and cross-language binding modules like `#[cxx::bridge]`.

Exceptions:

*   Having a small amount of core “ties things together” implementation code in
    a non-leaf module may be fine. The goal is to not have a lot of code in
    these modules.

Rationale

This makes it easier to find things, and avoids mixing structure and contents.

<a id="glob-imports"></a>

### Don’t use glob imports

Don't use glob imports, except in the following situations where you may
optionally do so at your own discretion:

*   `use super::*` for inline modules
*   `use enum::*` in method bodies of enums, and functions that are primarily
    dealing with that enum
*   `pub use submodule::*` for non-leaf modules
*   C++ interop: Since the same namespace (in C++) is a submodule in different
    Rust crates (in Rust), you may merge the namespaces into a private copy
    using glob imports. For example:

    ```rust
    mod absl {
        pub use status::absl::*;
        pub use strings::absl::*;
    }
    ```

    In this hypothetical example, you can use `absl::Status` and `absl::StrCat`
    from Rust, the same way you would from C++, instead of spelling them as
    `status::absl::Status` and `strings::absl::StrCat`.

    This must only be used for merging C++ namespaces, and the resulting merged
    module must not be public.

If using third-party crates that encourage a prelude, it is up to the reviewer’s
discretion to allow it.

This also means that defining preludes should be avoided.

Rationale

Glob imports increase toil for code janitors running LSCs, and make it harder to
know where a type comes from in contexts without xrefs.

<a id="use-statement"></a>

### A `use` statement should import items from one module

This rule corresponds to the rustfmt setting `imports_granularity = Module`.

Basically, there should not be any `::`'s inside the `{..}` block of a `use`
statement. For example:

**Good:**

```rust
use foo::Foo;
use foo::bar::Bar;
use foo::bar::Baz;
```

**Good:**

```rust
use foo::Foo;
use foo::bar::{Bar, Baz};
```

**Bad:**

```rust
use foo::{Foo, bar::Bar};
```

<a id="prefer-local-trait-imports"></a>

### Prefer locally-scoped trait imports

Import traits within function bodies, unless the trait's methods are used
extensively throughout the file.

**Good:**

```rust
fn foo(x: u8) {
    // Import the trait within a function, not at the module scope.
    use std::str::FromStr;

    let string: String = x.parse();
}
```

<a id="toplevel-functions"></a>

### Qualify calls to top-level functions with a module name

To use top-level functions defined in other modules or crates, import their
module and call them with `modulename::functionname()`. For example:

**Good:**

```rust
use std::mem;

let x = mem::transmute(y);
```

**Bad:**

```rust
use std::mem::transmute;

let x = transmute(y);
```

Exceptions:

*   When importing functions with sufficiently disambiguated names, e.g.,
    functions from C++ (where it is typical to call top-level (free) functions
    directly).

*   When the module name itself is prone to collisions. For example, when the
    module name is a C++ namespace name, and multiple crates define the same
    submodules.

Rationale

Many Rust codebases consistently keep a style such that unqualified lowercase
names are assumed local, so `foo()` can be assumed to be from the same module.
This rule largely exists to avoid reviewer disagreements, the benefit is mostly
consistency and a minor edge on reading code without xrefs.

<a id="type-names"></a>

### Type names should be imported and used unqualified

By default, types and traits should be referenced in code without using their
module path, e.g., code should use `Regex`, not `regex::Regex`, with a `use
regex::Regex` at the top of the file or potentially in the relevant function.

Exceptions:

*   In cases where there are ambiguities, it is acceptable to directly reference
    types with common names like `io::Error`. It is also acceptable to rename
    (`use std::io::Error as IoError`).
*   In cases where you have a large “group” of types, e.g. the
    [`hir module in rustc`](https://doc.rust-lang.org/nightly/nightly-rustc/rustc_hir/hir/index.html)
    which contains a large number of HIR types.
*   In macros and generated code; where requiring a `use` is counterproductive.
*   In code with lots of dependencies, where importing everything would lead to
    a very large import block with little benefit.

Rationale

This rule largely exists to avoid reviewer disagreements.
