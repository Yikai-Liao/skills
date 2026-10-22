# Macros and code generation

Source: [Google Rust Style Guide](https://github.com/google/styleguide/blob/2ac1584cd3c9854760f02418ec24687ec1698fb8/rustguide.md#L986-L1020); adapted under [CC BY 3.0](../LICENSE).

<a id="macros"></a>

## Macros

When considering how to express an API, prefer in order:

-   Regular Rust functions, types, traits, objects, and modules. (Avoid macros,
    code generation, and metaprogramming where possible).

-   `macro_rules!`-style macros.

-   Other code generation strategies (e.g. `genrule`)

-   `proc_macro` macros.

When you decide to use a macro or code generation, please weigh the benefits
against the costs:

-   IDEs, Code Search and other developer tools will work less well on code that
    uses macros.
-   Macros can create dialects of the language that make it harder for engineers
    to work across the codebase.
-   Large scale changes are more difficult and expensive to apply.

Rationale

**Prefer non-macro facilities:** Macros can create dialects of the language that
make it harder for engineers to work across the codebase. When a reader sees a
usage of a macro, they can make fewer assumptions about that code than if it
didn't use a macro. Macros are harder to write correctly than regular Rust code.

**Use `macro_rules!` for simple code generation:** Since Rust macros operate on
the AST, they can be less fragile than textual code generation.
