# Collaboration For Large Survey Tasks

Use this reference only when subagents are available and the corpus, verification load, or validation task benefits from delegation.

## Contents

1. Lead responsibility
2. Safe assignment units
3. Artifact-first worker protocol
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

## 3. Artifact-First Worker Protocol

Before starting a worker, the lead must allocate one exact, project-local Markdown path for its assignment. Do not ask a worker to "report back" without a destination file. Use a non-overlapping path such as `survey-workspace/worker-reports/<assignment>.md`, a paper-note file, or an evidence-packet file.

Tell every worker explicitly that it is a subagent in a larger survey project and that its assigned Markdown file—not its chat reply—is its deliverable. Include:

- the review question, scope, and inclusion rule;
- exact papers, URLs, identifiers, or file paths it owns;
- the exact Markdown artifact path it must create or update, files it may edit, and files it must not edit;
- the required paper-note or evidence-unit schema;
- the evidence standard and metadata verification requirement;
- the distinction between author-stated and survey-inferred limitations;
- how to report missing sources, uncertainty, contradictions, and suggested links;
- a prohibition on inventing bibliographic or empirical details.

Require this sequence without exception:

1. Read and investigate the assigned unit.
2. Write the complete result to the assigned Markdown artifact. If evidence is unavailable, write the attempted retrievals, exact gap, uncertainty, and bounded conclusion there; an empty or absent artifact is not an acceptable outcome.
3. Re-open the artifact and verify that it is non-empty, readable, and contains the required schema.
4. Only then send a brief receipt: completion status, artifact path, and blockers or uncertainties. Do not put the research findings, a substitute summary, or the only copy of the result in the chat reply.

Workers must not create or edit the shared manuscript, evidence matrix, taxonomy, or another worker's artifact unless the lead explicitly assigns that file. They must not launch further subagents: the lead owns delegation, artifact allocation, and synthesis.

## 4. Merge And Adjudication

Wait for the worker receipt, then inspect the assigned file itself before accepting the assignment. Reject and return for repair any missing, empty, unreadable, schema-incomplete, or chat-only result. Do not recover research findings from a chat summary by copying them into a file; require the owning worker to persist and verify the artifact.

Inspect accepted work for completeness, evidence support, duplicate sources, taxonomy assumptions, unsupported criticism, and inconsistent terminology. Return incomplete assignments for repair before merging them into cross-paper artifacts.

Resolve disagreements by consulting primary evidence or assigning a narrow adjudication pass. Record decisions that change inclusion, terminology, taxonomy, or interpretation.

Merge verified notes into the evidence matrix, then synthesize them from the review question. Do not concatenate worker summaries into the manuscript.

## 5. Independent Validation

Use a fresh, read-only worker to test a substantial revision when feasible. Pass only:

- the `survey-md` skill path;
- the raw manuscript and source workspace;
- a realistic user-style request.

Do not pass the suspected defects, intended answers, prior diagnosis, or expected taxonomy. Ask the worker to produce an audit or revision plan, not to confirm the lead's changes.

Judge the skill by whether the worker independently identifies missing definitions, invalid categories, incomplete explanations, weak synthesis, unsupported claims, and manuscript-process residue—and proposes content-preserving repairs. Clean up test artifacts or keep the test read-only so later runs cannot discover expected answers on disk.
