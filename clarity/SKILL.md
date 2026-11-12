---
name: clarity
description: >-
  Use when explaining, answering questions, or reporting, and when drafting, rewriting, translating, or reviewing text, including software documentation, design records, skills, and project instructions. Also use when adding or changing code with multi-step flows, branches, or state changes, to guide the main flow, naming, local structure, and comments. Not triggered by pure formatting fixes or mechanical implementation that needs no judgment about expression.
---

# Reader-Focused Clarity

Judge wording and local code organization by what it costs the reader to understand: less guessing, looking back, and piecing together. Choices about domain modeling, state ownership, data representation, and module contracts are design tasks.

## Keep the path of understanding and the concept structure

Start from objects or scenarios the reader already knows, and connect actions to their causes and results. For continuous prose, first organize how the whole piece advances, so each section's place and relations are recognizable. Explain with the material at hand, and supply project background the reader lacks.

Make necessary conditions, evidence, and conceptual distinctions available where they are used. The main reading path carries the relations; summaries, glossaries, and links assist. Show structure through grouping, names, and abstractions, so each concept is complete and its relations are readable nearby.

Choose expression by understanding cost. Keep useful terms, compact rules, necessary repetition, derivations, and literary rhythm. Fix local problems locally; clear original text can stay.

Look for template-driven filler that advances nothing: an opening that restates the task, paragraphs that each reassert significance, an ending that repeats the conclusion. Keep structure that explains, navigates, or emphasizes. Revise for a specific expression problem; style, word choice, and sentence length are not defects by themselves.

## Keep the claim; correct only with grounds

Respond to the actual claim and keep its **task, scope, and strength**. Aim rebuttals at the position the material takes; judge "some progress" and "fully delivered", or "partial evidence" and "conclusive", as different claims.

A correction or pre-emptive clarification needs the original claim or a concrete context for the misunderstanding; a teaching assumption states its purpose. Organize comparisons, contrasts, and qualifications by their actual relation, and keep explanations on topic.

**Directness applies to body text, reviews, delivery notes, and code comments:**

- State results, conditions, and concrete gaps directly. Keep exclusions of responsibility and safety prohibitions that do work.
- Delete softening, corrective asides, and reminders that contribute nothing. Base follow-up plans on established facts; once the content is complete, stop.
- Keep real limits, negative conclusions, unknown states, and existing plans as separate items. "Passed on a single machine; multi-node untested" keeps both halves.
- If a rewrite changed the original claim without authorization, restore its task, scope, and strength. Polishing and translation keep the substantive argument; reviews name concrete problems.

## Deliver from the material

Deliver the requested text, revision, or review directly, in the language the user asked for or the existing work uses, not the language of this skill.

Keep facts, numbers, conditions, attribution, strength of evidence, and the author's voice. Check which object each number belongs to, each claim's qualifications, and sequence, parallel, and ranking relations. Turning "the vendor says" into a direct assertion, or "may slightly improve" into "has improved", changes the claim. Describe any substantive change as what it is, based on the available material.

After removing empty phrasing, build sentences from the actions and relations the material already has. Concrete detail needs support in the material: polishing adds no data, sources, causes, experiences, or positions. Style follows the task and the original, with natural rhythm. Factual introductions add no personal attitude; first-person text expresses only experiences and judgments already present. Keep template variables and placeholders as they are.

Delete editing narration, writing strategy, self-assessment, and announcements of following guidelines. Keep the topic's own argument, research methods, necessary warnings, and citations. In code, put non-obvious reasons, bug history, optimization costs, and guards against mistaken edits in comments next to the code.

## Read references by problem

This page is enough for short ordinary replies; read references when the problem calls for them. For new or changed implementations with multi-step flows, branches, or state changes, read the code reference; for simple mechanical edits, read only the relevant part.

| Problem | Reference |
|---|---|
| Article throughline, heading hierarchy, follow-up questions, claim drift in rewrites, template prose, genre boundaries | [Text writing](references/text-writing.md) |
| Software contracts, current state versus proposals; architecture, state, and data views | [Software documentation](references/software-documentation.md) |
| Expressing, inheriting, and handing off design discussions and decisions | [Design discussion](references/design-discussion.md) |
| Cross-chapter dependencies, summaries, continuations | [Long-form writing](references/long-form-writing.md) |
| New or changed multi-step implementations; main flow, nesting, phase extraction, naming, comments, diagnostics | [Code expression](references/code-readability.md) |
| Semantic boundaries of translation and localization | [Language adaptation](references/language-adaptation.md) |
| Whether a readability finding holds | [Readability review](references/readability-review.md) |
| Preserving requirements in skills, project instructions, and prompts | [Instruction writing](references/instruction-writing.md) |
