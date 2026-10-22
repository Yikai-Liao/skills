# Crates, modules, and imports

Source: [Google Rust Style Guide](https://github.com/google/styleguide/blob/2ac1584cd3c9854760f02418ec24687ec1698fb8/rustguide.md#L168-L443); adapted under [CC BY 3.0](../LICENSE).

## Contents

- [Code organization](#code-organization)
- [Prefer small crates [chrome]](#small-crates)
- [Use flat file layout for `rust_library` sources [chrome]](#structure)
- [Name source files and leaf modules after the primary user-defined item](#userdefined-item)
- [Don’t implement APIs in non-leaf modules](#non-leaf-modules)
- [Don’t use glob imports](#glob-imports)
- [A `use` statement should import items from one module](#use-statement)
- [Prefer locally-scoped trait imports](#prefer-local-trait-imports)
- [Qualify calls to top-level functions with a module name](#toplevel-functions)
- [Type names should be imported and used unqualified](#type-names)
- [Use the appropriate import mechanism [chrome]](#import-macro)

<a id="code-organization"></a>

## Code organization

*Terminology:*

*   A *crate* is a unit of compilation. A crate always contains a nameless Rust
    module, the "root module".

*   A Rust *module* is a unit of code organization within a crate. Rust modules
    are used to control visibility of names. Modules can be nested. They can
    also be used to split code across files and directories.

The following sections convey that in Chromium, it is preferable to **not** make
use of all possibilities of splitting modules across files.

<a id="small-crates"></a>

### Prefer small crates [chrome]

Prefer small crates in Chromium; ideally, but not necessarily, a single file
(focusing on one abstraction). If your code can be split up into small crates,
do so.

A crate corresponds to a single `rust_static_library` (chrome) rule, which may
contain one or more `.rs` files.

Additional considerations:

*   The root module is allowed to `re-export` public APIs from `leaf
    submodules`, making submodules an implementation detail of the crate (as
    users don't need to know about these submodules).

*   This rule about small crates applies equally to crates with and without
    submodules. First, evaluate whether the APIs need to be in the same crate,
    and only then consider whether submodules could help organize the APIs.

*   If you decide to use submodules, follow the
    [expected file structure](#structure).

Larger crates are allowed when
[trait impl coherence rules](https://smallcultfollowing.com/babysteps/blog/2015/01/14/little-orphan-impls/)
force multiple types and traits to be included in one library, or if you're
building a large foundational library.

Rationale

Fine-grained library targets are recommended in Chromium due to the massive size
of our codebase, non-local effects of adding dependencies in the build graph,
and to improve performance of parallel compilation and build caching.

<a id="structure"></a>

### Use flat file layout for `rust_library` sources [chrome]

In Chromium `.rs` source files belonging to one `rust_library` (one Rust crate)
must reside in a single directory.

Don't use subdirectories to organize files that belong to a single crate. If
organizing one crate's files into subdirectories feels necessary, this is a
strong indication that the crate has grown [too large](#small-crates) and should
be split.

This crate layout is intentionally different from the conventional Cargo
directory structure typically used in open-source repositories.

Exception: Rust code in `//third_party` that is also built with
[Cargo](https://doc.rust-lang.org/cargo/) should follow the conventional Cargo
directory structure.

Rationale

The approach in Chromium is driven by the following factors:

*   Based on the preference for [small crates](#small-crates), most
    `rust_library` targets will only contain one source file.
*   Because of the above point, creating a directory for each `rust_library`
    target would result in most directories containing only one source file.
*   Multi-file `rust_library` targets should not create dedicated directories
    for submodules either; this ensures a consistent approach.

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
*   In Chromium, when importing functions from
    [small, single-purpose first-party crates](#small-crates).

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

<a id="import-macro"></a>

### Use the appropriate import mechanism [chrome]

*   Chrome Use `chromium::import!()`.
