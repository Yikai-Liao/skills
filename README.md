# Agent Skills

Reusable agent skills distributed through the [`skills`](https://skills.sh/) CLI.

## Install

Install the scholarly survey-writing skill with:

```bash
npx skills add Yikai-Liao/skills --skill survey-md
```

Install the software-design skill with:

```bash
npx skills add Yikai-Liao/skills --skill software-design-philosophy
```

Install all skills from this repository with:

```bash
npx skills add Yikai-Liao/skills --all
```

## Included skills

- `survey-md` — create, revise, or audit source-grounded scholarly survey articles and literature reviews in Markdown.
- `software-design-philosophy` — diagnose software complexity and design clearer modules, interfaces, boundaries, and evolution paths.

## Repository layout

Each top-level skill directory contains its installable files: `SKILL.md` and any runtime metadata, references, scripts, or assets. Keep development-only material outside these directories so it is not distributed with a skill.

- [`tests/software-design-philosophy/`](tests/software-design-philosophy/) — evaluation prompts and audit/validation results.
- [`docs/software-design-philosophy/`](docs/software-design-philosophy/) — source provenance and design decision history.
