# Workflow And Persistent State

Use this reference for a full build, broad revision, or resumed survey project.

## Contents

1. Inputs and mode
2. Workspace contract
3. Incremental execution
4. Source coverage
5. Build sequence
6. Resume and handoff

## 1. Inputs And Mode

Collect what exists before asking for more:

- topic, review question, or draft manuscript;
- intended reader, venue, length, language, and citation format;
- scope boundaries and exclusions;
- bibliography, source links, PDFs, notes, or literature map;
- repository conventions and existing workspace artifacts.

Infer low-risk defaults and record them. Ask only when a missing choice would materially change the review question, evidence standard, or deliverable.

When the topic is broad or exploratory, run a short landscape pass before freezing the question. Map major subfields, active debates, prior reviews, benchmark or evidence traditions, applications, adjacent fields, and recent breakthroughs. Propose a small set of reviewable focal questions with their likely evidence density and scope risk. Select the question that produces a coherent scholarly argument, not merely the largest source count.

Choose the work mode:

- **Build**: create the evidence base, explanatory frame, architecture, and manuscript.
- **Revise**: audit the complete manuscript, rebuild weak structures, then edit prose.
- **Audit**: persist findings and repair obligations without changing the manuscript.
- **Continue**: inspect persisted state and resume from the first incomplete dependency.

## 2. Workspace Contract

Use a project-local `survey-workspace/` unless the repository already defines a location. Keep the final Markdown manuscript outside or alongside it, for example `survey.md`.

Create artifacts only when relevant, but never keep an expensive decision solely in hidden reasoning or chat history:

| Artifact | Purpose |
|---|---|
| `00-review-brief.md` | question, thesis, reader, scope, exclusions, deliverable, status |
| `01-search-coverage.md` | sources searched, queries, dates, screening rules, access gaps |
| `01a-source-manifest.md` | attempted and successful metadata, full-text, and supplement retrievals |
| `02-paper-ledger.csv` | candidate and included sources with status and rationale |
| `03-paper-notes/KEY.md` | one structured note per important source |
| `04-evidence-matrix.md` | cross-source comparison and evidence units |
| `05-concepts-and-explanations.md` | definitions, shared frames, mechanism or reasoning maps |
| `06-taxonomy-and-outline.md` | taxonomy tests, frozen organization unit, sibling-heading tests, article architecture, section claims |
| `07-consensus-controversies-gaps.md` | synthesis, disagreements, weak evidence, authorial position |
| `08-figures-and-tables.md` | each visual artifact and the claim it supports |
| `09-decision-log.md` | dated changes to scope, terms, inclusion, structure, interpretation |
| `10-citation-audit.md` | cited keys, missing metadata, unresolved support, access limits |
| `11-revision-audit.md` | manuscript-wide gate failures and repair dispositions |

For a small, explicitly local edit, reuse existing artifacts and write only the minimum audit needed to make the change traceable. Do not manufacture an empty bureaucracy. For a broad revision, create the revision audit even if the earlier workspace is incomplete.

Give every important paper its own note. Use the matrix for comparison, not as the only home for paper-level interpretation. Record why excluded sources were excluded.

## 3. Incremental Execution

Treat the filesystem as the source of truth.

Work in bounded, recoverable batches:

- search or screen one coherent query family at a time;
- read a small batch of related papers and write their notes immediately;
- update the evidence matrix after each batch, not at the end;
- revise one structural dependency or section claim at a time;
- checkpoint citation status and unresolved questions before stopping.

Make each batch atomic enough to retry. Do not accumulate large unwritten conclusions in context. When a batch changes the thesis, taxonomy, terminology, or scope, update the review brief and decision log before continuing.

Draft the abstract last for a new manuscript. For a revision, revisit the abstract after the body and conclusion stabilize.

## 4. Source Coverage

Build coverage around the review question rather than a fixed citation quota.

Choose and record a search posture before planning queries:

- **recency-led** when the request names a recent window or asks for emerging work; concentrate discovery in that window and use older work as lineage;
- **timeline-spanning** when the question concerns history, evolution, or foundations; cover turning points from origin to the current frontier;
- **balanced** when no temporal emphasis dominates; combine foundations, representative developments, contradictions, and the most recent credible work.

Treat a named date window as an evidence constraint, not decoration. Use date-sorted or date-filtered discovery when recency matters, because relevance ranking and model familiarity favor older, famous work. Record the posture, parsed window, and search date in `01-search-coverage.md`.

Search across relevant dimensions such as:

- canonical foundations and vocabulary-setting work;
- recent advances within the requested time window;
- competing problem formulations or theoretical traditions;
- representative method or evidence families;
- benchmarks, datasets, measurement practices, and replications;
- contradictory, negative, or boundary-setting results;
- prior reviews used to inspect coverage and framing;
- adjacent fields when transfer is part of the question.

Plan queries across several of these dimensions instead of repeating one keyword. Track each completed query family and its useful yield so a resumed run does not repeat it.

Record query strings, databases or sites, search dates, filters, inclusion decisions, and inaccessible sources. Verify canonical metadata from primary or authoritative records. Use full text when a claim depends on method details, results, assumptions, or limitations.

Do not equate a high paper count with coverage. Test whether each major claim, family, disagreement, and time period has evidence. State incomplete coverage affirmatively in the method or scope section and narrow exhaustive language.

Audit unused included sources before delivery. Either integrate an on-scope source with a distinct argumentative role, reclassify it as background-only, or remove it from the included corpus. Never pad the bibliography to reach an arbitrary count.

## 5. Build Sequence

Follow dependency order rather than sentence order:

1. Freeze the review question, scope, and provisional thesis.
2. Map and verify the source base.
3. Write paper notes and cross-paper evidence units.
4. Define central concepts and reconstruct explanations.
5. Test alternative taxonomies or organizing logics.
6. Freeze the organization unit for each main-synthesis block and run the sibling-heading test.
7. Assign a field-level claim and evidence role to each section.
8. Draft synthesis sections before abstract and conclusion.
9. Integrate critique, boundaries, consensus, controversy, and gaps.
10. Design only figures and tables that make an argument inspectable.
11. Audit citations, cross-section setup/payoff, and manuscript quality.

For revision, replace steps 1–2 with an initial whole-manuscript audit, then repair in dependency order:

`thesis and scope -> concepts -> explanations -> taxonomy -> organization unit and sibling hierarchy -> section claims -> evidence synthesis -> prose surface -> abstract and conclusion`

Do not start with sentence polishing when a higher dependency is broken.

## 6. Resume And Handoff

At the start of a resumed run, inspect:

- `00-review-brief.md` for the active question and status;
- `02-paper-ledger.*` for coverage and pending reads;
- `05-concepts-and-explanations.md` for terminology and explanatory gaps;
- `06-taxonomy-and-outline.md` for the current structure;
- `07-consensus-controversies-gaps.md` for the active synthesis;
- `09-decision-log.md` for decisions that must not be silently reversed;
- `11-revision-audit.md` for unresolved blockers.

Before stopping, update status, next action, unresolved evidence gaps, and any changed decisions. Leave the workspace understandable without access to the prior conversation.
