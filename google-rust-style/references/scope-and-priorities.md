# Scope and rule priorities

Source: [Google Rust Style Guide](https://github.com/google/styleguide/blob/2ac1584cd3c9854760f02418ec24687ec1698fb8/rustguide.md#L45-L168); adapted under [CC BY 3.0](../LICENSE).

## Contents

- [Follow public Rust style rules](#public-rules)
- [Apply API design rules in context](#api-design-context)

This document is a *style guide* for the usage of the Rust programming language
at Google. In this context, “style” refers to more than just formatting; it
includes guidance on API and implementation design.

Rust is used in many places, including
[google3](https://opensource.google/documentation/reference/glossary#google3),
Android, ChromeOS, Fuchsia, and Chrome, and we'd like for Rust usage at Google
to be consistent both within and across codebases. In addition to bringing
consistency to our Rust code, style guidance also helps establish a standard of
quality.

## Background

### Scope

The current scope of authority of the rules outlined in this guide:

*   **In Android, Chromium, and other codebases**: This style guide has been
    developed in consultation with other codebases, and they intend to start
    applying it. These codebases may have their own rules about how strictly
    this is expected to be applied. Expect more information here as these
    codebases adopt this guide.

### Goals of the style guide

By and large, we have this document for
[the same reasons we have a C++ style guide](https://google.github.io/styleguide/cppguide.html#Goals).

Most style rules come from one or more of the goals listed below.

<dl>

<dt>Style rules should prioritize readability and maintainability over writeability</dt>
<dd>We expect our code to be around for long periods of time, and we
consider a little bit of extra effort applied during code writing to be
worth it in the long run if the style rule improves readability.
</dd>

<dt>Style rules should favor better automation</dt>
<dd>
Large-Scale Changes (LSCs)
are common at Google, and consistency helps
make LSCs easier to carry out.
</dd>


<dt>Style rules should be consistent with the wider Rust ecosystem where possible</dt>
<dd>The broader Rust ecosystem already has a pretty good amount of consistency
in style, and we should rely on that where possible to reduce surprise and make
it less work to learn Google's Rust style.
</dd>

<dt>Style rules should pull their weight</dt>
<dd>Every Rust developer and reviewer at Google has to keep these style rules
in mind: as such, we should be careful to include rules that have a tangible
benefit.
</dd>


<dt>Style rules may help avoid minor style disagreements</dt>
<dd>There are many cases where reasonable people may disagree about a style, and
we expect that disagreement to show up often on CLs. Having a style rule helps
avoid having to rehash this each time. Rules in this category that do not have other
benefits should be kept to a minimum.
</dd>

</dl>

<a id="public-rules"></a>

## Follow public Rust style rules

Follow the official public Rust style rules to the extent they don't conflict
with this style guide.

*   [Rust Style Guide](https://doc.rust-lang.org/nightly/style-guide/)

    *   Most code formatting conventions are enforced automatically by rustfmt.

*   [Rust API Guidelines](https://rust-lang.github.io/api-guidelines/)

A “conflict” would be a case where this style guide suggests a pattern that is
discouraged, or counter to the primary encouraged pattern in the Rust style
guide.

Why does the guidance in this style guide deviate from regular Rust style rules?

Most style guides have three goals: consistency, readability, and encouraging
good API design. Regardless of the specific choices made, it helps everyone to
have these choices made beforehand to limit bikeshedding.

This style guide shares those goals, but it also has an additional goal not seen
as often: smoothing the way for Large-Scale Changes (LSCs). Large codebases like
many of the ones at Google occasionally need to run codebase-spanning
refactorings that are assisted by tooling: for this to work well, the code
should be something tooling has an easy time working with. Consistency helps for
this, but so does having deliberate refactor-friendly patterns.

<a id="api-design-context"></a>

## Apply API design rules in context

When applying rules that relate to API design, you should distinguish two types
of code:

*   Library code

    *   Intended for use by other projects (applications or other libraries).
    *   Solves a relatively general problem.

*   Application code

    *   Intended for use in a single application.
    *   Solves a more specific problem.

For *library code*, style guide rules that concern API design are binding.

For *application code*, the rules on API design are a strong recommendation. As
you apply them, keep in mind that since application code is written to solve a
specific problem, it should generally favor simplicity and directness over broad
reusability. Avoid premature generalization and abstraction; focus on what is
required to meet the immediate need.
