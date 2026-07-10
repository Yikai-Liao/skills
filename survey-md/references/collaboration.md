# Collaboration For Large Survey Tasks

Use this reference only when subagents are available and the corpus, verification load, or validation task benefits from delegation.

## Contents

1. Lead responsibility
2. Safe assignment units
3. Worker contract
4. Merge and adjudication
5. Independent validation

## 1. Lead Responsibility

Keep the lead agent responsible for:

- review question, scope, thesis, and search posture;
- corpus coverage and assignment map;
- shared terminology and explanatory frame;
- taxonomy and article architecture;
- cross-paper synthesis and authorial judgment;
- conflict resolution, citation audit, and final manuscript.

Use the lead context for coordination and synthesis, not indiscriminate paper-by-paper reading. Let workers persist bounded evidence, but do not outsource the argument.

## 2. Safe Assignment Units

Assign work by non-overlapping files or evidence units:

- a named batch of papers with one note file per paper;
- metadata or citation verification for a bounded list;
- one benchmark, dataset, controversy, or method family evidence packet;
- an independent read-only audit of a completed manuscript;
- targeted adjudication of a contradiction.

Avoid assigning several workers to the same synthesis file. Do not let workers independently redesign the global taxonomy or thesis in shared manuscript files.

## 3. Worker Contract

Tell every worker explicitly that it is a subagent in a larger survey project. Include:

- the review question, scope, and inclusion rule;
- exact papers, URLs, identifiers, or file paths it owns;
- files it may edit and files it must not edit;
- the required paper-note or evidence-unit schema;
- the evidence standard and metadata verification requirement;
- the distinction between author-stated and survey-inferred limitations;
- how to report missing sources, uncertainty, contradictions, and suggested links;
- a prohibition on inventing bibliographic or empirical details.

Require workers to write durable artifacts, not only return a chat summary.

## 4. Merge And Adjudication

Inspect returned work for completeness, evidence support, duplicate sources, taxonomy assumptions, unsupported criticism, and inconsistent terminology. Return incomplete assignments for repair before merging them into cross-paper artifacts.

Resolve disagreements by consulting primary evidence or assigning a narrow adjudication pass. Record decisions that change inclusion, terminology, taxonomy, or interpretation.

Merge verified notes into the evidence matrix, then synthesize them from the review question. Do not concatenate worker summaries into the manuscript.

## 5. Independent Validation

Use a fresh, read-only worker to test a substantial revision when feasible. Pass only:

- the `survey-md` skill path;
- the raw manuscript and source workspace;
- a realistic user-style request.

Do not pass the suspected defects, intended answers, prior diagnosis, or expected taxonomy. Ask the worker to produce an audit or revision plan, not to confirm the lead's changes.

Judge the skill by whether the worker independently identifies missing definitions, invalid categories, incomplete explanations, weak synthesis, unsupported claims, and manuscript-process residue—and proposes content-preserving repairs. Clean up test artifacts or keep the test read-only so later runs cannot discover expected answers on disk.
