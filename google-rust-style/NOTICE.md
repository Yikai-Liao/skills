# Source and attribution

Adapted from **Rust Style Guide**, Google / google/styleguide contributors, under Creative Commons Attribution 3.0 Unported ([license](LICENSE), [license URL](https://creativecommons.org/licenses/by/3.0/)).

- [Original published guide](https://google.github.io/styleguide/rustguide.html)
- [Pinned Markdown source](https://github.com/google/styleguide/blob/2ac1584cd3c9854760f02418ec24687ec1698fb8/rustguide.md)
- Commit: `2ac1584cd3c9854760f02418ec24687ec1698fb8` (2026-10-21); retrieved 2026-10-22.
- Original file Git blob: `5d8e48b84afc157ca2a1433016207c5f336a0ff2`.
- Original Markdown SHA-256: `059c6cdee4e7e5a8b756135200b2ca360de146ddaf7ca6f720f839b5dd7edfe6`.
- [Pinned upstream license](https://github.com/google/styleguide/blob/2ac1584cd3c9854760f02418ec24687ec1698fb8/LICENSE); reproduced unchanged in LICENSE.

Changes: split the source into task-specific references; added a skill entrypoint and conditional routing; removed the website's CSS/table-of-contents boilerplate; changed CSS-only good/bad example markers to explicit labels; preserved codebase badge text; repaired cross-file fragment links; added local contents and provenance links. Retained general rules, examples, rationales, exceptions, and external references remain in the topic files. At the user's request, this edition omits Chrome/Chromium, Android, and Fuchsia policies: crate size and flat layout, codebase-specific import and formatting mechanisms, async/thread/mutex restrictions, unstable-feature exceptions, and test frameworks. It also removes their scope text, function-import exception, and panic-abort examples. The general catch_unwind exception still requires possible panic=unwind execution. Removed codebase-specific rules are not converted into universal Rust restrictions. Examples were not corrected or compiled. No affiliation with or endorsement by Google is implied.

The organization was informed by [Clarity instruction-writing](https://github.com/Yikai-Liao/skills/blob/a92f73adca162915fa117872482f76b405738df4/clarity/references/instruction-writing.md) and [long-form-writing](https://github.com/Yikai-Liao/skills/blob/a92f73adca162915fa117872482f76b405738df4/clarity/references/long-form-writing.md), read at commit `a92f73adca162915fa117872482f76b405738df4`. Clarity's text is not bundled, and Clarity is not a runtime dependency.
