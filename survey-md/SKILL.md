---
name: survey-md
description: >-
  Create, revise, or audit source-grounded scholarly survey articles and literature reviews in Markdown. Use for survey papers, literature-review manuscripts, related-work syntheses, field maps, technical taxonomies, research-gap analyses, consensus or controversy reviews, and manuscript-wide survey revision. Accept a topic, bibliography, literature map, paper notes, source files, or an existing draft. Do not use for questionnaire design, response-rate analysis, or survey-methodology studies unless they are themselves the literature being reviewed.
---

# Survey MD

Produce a coherent scholarly survey in Markdown. Organize the literature around a review question, make an evidence-bound authorial argument, explain the field well enough that a reader can reconstruct its major approaches, and preserve traceable source support.

Remain self-contained. Use the sources and tools available in the current environment without external workflow dependencies. When evidence is insufficient, retrieve and verify it directly when permitted; otherwise mark the exact gap and narrow the claim.

## Choose The Work Mode

Choose one mode from the request and existing artifacts:

- **Build**: create a survey from a topic, bibliography, literature map, or paper set.
- **Revise**: repair an existing manuscript. Unless the user explicitly requests a local edit, audit the whole manuscript before changing prose.
- **Audit**: diagnose readiness and produce an actionable audit without editing the manuscript unless requested.
- **Continue**: resume a persisted survey workspace instead of reconstructing decisions from chat history.

For a narrowly scoped edit, inspect the surrounding definitions, section claim, cross-references, and downstream conclusions. Do not silently expand the edit, but report manuscript-wide blockers that the local change cannot resolve.

## Load Only The Needed References

Read each selected reference completely **before** performing the covered work. All references are one level below this file.

| Situation | Read first |
|---|---|
| Any full build, broad revision, or resumed project | [workflow-and-state.md](references/workflow-and-state.md) |
| Discovering, resolving, verifying, or downloading papers, metadata, PDFs, or supplements | [source-retrieval.md](references/source-retrieval.md) |
| Building a source base, notes, evidence matrix, critique, or synthesis | [evidence-and-synthesis.md](references/evidence-and-synthesis.md) |
| Defining terms, explaining technical routes, or designing a taxonomy | [concepts-taxonomy-explanation.md](references/concepts-taxonomy-explanation.md) |
| Designing sections, headings, paragraphs, tables, figures, or scholarly style | [manuscript-design.md](references/manuscript-design.md) |
| Revising or auditing an existing draft | [revision-gates.md](references/revision-gates.md) |
| Using subagents for a large corpus or independent validation | [collaboration.md](references/collaboration.md) |
| Declaring a manuscript or audit complete | [quality-gate.md](references/quality-gate.md) |

Do not load every reference automatically. A local prose edit may need only the manuscript and revision references; a new technical survey usually needs the workflow, evidence, concepts, manuscript, and quality references.

## Core Workflow

### 1. Frame The Review

Write a one-sentence review question naming the field, central problem, and angle. Record the intended reader, scope, exclusions, coverage limits, and a provisional answer or thesis. Reject scopes that amount to `all papers about X`.

Treat the thesis as a revisable, contestable proposition about the literature—not a promise to list papers or introduce a taxonomy.

### 2. Establish Durable State

Create or reuse a project-local `survey-workspace/` and a target manuscript such as `survey.md`. Persist source coverage, paper-level notes, cross-paper evidence, concepts, structural decisions, and citation status. Follow the artifact contract in the workflow reference; adapt filenames only when the repository already has a convention.

Use the filesystem as the source of truth. Resume from persisted artifacts, and checkpoint after each meaningful search, reading, restructuring, drafting, or audit batch.

### 3. Build A Defensible Evidence Base

Map the field broadly, then read important sources selectively in depth. Verify bibliographic facts and every claim that depends on a paper's method, result, limitation, dataset, or evaluation. Distinguish author-stated limitations from limitations inferred through cross-paper comparison.

When source acquisition is needed, resolve identifiers to authoritative records, persist every attempted and successful retrieval, and validate downloaded content before treating it as a paper or supplement. For arXiv full text, prefer a cleaned Markdown reading copy derived from cached official HTML; do not read raw HTML by default. Retain the HTML for provenance and structural checks, and fall back without repeated probing when HTML is unavailable.

Convert sources into evidence units that can establish, change, contradict, narrow, transfer, or bound a field-level claim. Do not draft the body from titles and abstracts alone when the argument depends on methods or results.

### 4. Reconstruct The Explanation Before Classifying

Define central terms before or at first conceptual use. Establish the shared problem, relevant objects and conditions, mechanism or reasoning, immediate result or claim, connection to the broader phenomenon, supporting evidence, and scope boundary.

Translate paper-internal compression into reader-facing explanation. Labels such as `unified protocol`, `controlled comparison`, `factor isolation`, `ablation`, `alignment`, `end-to-end`, `robustness`, or `framework` do not explain an experiment or method by themselves. State in concrete terms what data or condition was held fixed, what component was changed, what output was compared, and why that comparison supports the survey claim. Introduce necessary technical terms by naming their referent, operation, and observable consequence before reusing the shorthand.

Treat a taxonomy as a substantive claim. For every axis, specify the classification question, unit, membership criteria, overlap, and explanatory consequence. Do not confuse the focal object of an approach with every object or representation the approach requires. Do not preserve an axis merely because it already structures the draft.

### 5. Design The Argument

Choose an organizing logic that answers the review question: taxonomy, turning-point chronology, controversy map, evidence ladder, problem decomposition, process anatomy, cross-domain transfer, or another justified structure.

Give every major section a field-level claim. Make early concepts and examples pay off later; prepare every late conclusion and future direction in the body. State the survey's evidence-bound position early and carry it through selection, comparison, critique, and conclusion.

### 6. Draft Or Repair Scholarly Prose

Write from relationships among sources, not from a paper ledger. Build paragraphs around a claim, comparative evidence, interpretation, and boundary. Explain major approaches completely enough that a field-aware reader does not need to open the cited paper merely to understand what the approach does or why it matters.

Write for the declared survey reader, not for a reader who has already read every cited paper. Preserve useful domain vocabulary, but unpack paper-specific experimental shorthand and method labels at first use. A citation supplies evidence and further detail; it must not carry a missing subject, operation, comparison, causal link, or definition.

State the scholarly object and relationship directly. Do not use recurring correction templates such as `not X but Y`, `X is not equal to Y`, `not only X`, or `X cannot represent Y` as the default structure of headings, topic sentences, abstracts, or conclusions. Reserve explicit negation for a genuine disputed proposition supported by evidence; otherwise rewrite the sentence positively in terms of distinct constructs, conditions, mechanisms, scopes, or evidence levels.

On the first substantive mention of a work, identify its verified leading institution or research team and make the combined `work name + parenthesized year` phrase the Markdown link, for example `Alibaba's [RecGPT(2025)](...)`. Follow it immediately with the work's evidence role in the paragraph. Use the short work name on later mentions. Verify the institution and year from the paper, official proceedings, repository, or authoritative landing page; if the leading institution is unresolved, write `the research team behind [Work(Year)]` and keep the uncertainty in the workspace rather than guessing.

Keep critique inside the relevant comparison. Use headings that name scholarly objects, relations, processes, evidence boundaries, or claims. Remove defensive self-description, drafting commentary, audit labels, author-by-author rhythm, and unsupported future-work slogans.

When revising, restore missing scholarly content before polishing sentences. Do not pass a quality gate by deleting material that the question, scope, or thesis still requires.

### 7. Verify And Deliver

Run the quality gate over the complete Markdown manuscript and its citations. Resolve all blocking failures or mark an explicit accepted boundary with appropriately narrowed wording.

Deliver:

- the final or revised Markdown manuscript;
- the persisted survey workspace, or a concise explanation of unavailable artifacts for a limited task;
- an honest summary of coverage, unresolved evidence gaps, accepted boundaries, and validation performed.

Do not claim publication readiness solely because formatting or citation syntax passes. Readiness requires conceptual clarity, explanatory closure, valid organization, synthesis, evidence-calibrated judgment, and a clean scholarly surface.

## Runtime And Dependencies

Reuse an existing project environment when it is valid. If a required Python interpreter is unavailable, prefer letting `uv` provide or install the requested Python version. For a one-off Python CLI, prefer `uvx <tool>`; for temporary library requirements, prefer `uv run --with <package> ...`. Avoid modifying the global Python environment or project dependency files unless the deliverable requires a persistent dependency or the user explicitly requests it.

## Non-Negotiable Rules

- Do not invent papers, authors, years, venues, identifiers, quotations, results, or citation counts.
- Do not call a review systematic unless its protocol supports that term.
- Do not use a paper's claimed contribution or limitations section as the final survey judgment.
- Do not let tables, taxonomies, or internal note fields dictate the prose without an explanatory argument.
- Do not present working notes, checklists, audit statuses, or organizational decisions as manuscript content.
- Do not replace missing explanation with names, labels, equations, performance numbers, or citation piles.
- Do not export a paper's compressed labels as explanation. Expand phrases such as `under a unified protocol`, `we isolate factors`, `through alignment`, or `the ablation shows` into the concrete held-fixed conditions, changed variables, compared outcomes, and inferential consequence needed by the intended reader.
- Do not erase required but difficult material merely to clear a gate; repair, narrow, relocate, or explicitly bound it.
- Do not manufacture authorial force through repeated binary reversals. A survey should establish relations and boundaries directly, not repeatedly correct an imagined reader with `not X but Y` phrasing.
