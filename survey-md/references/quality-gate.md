# Survey Markdown Quality Gate

Run this gate before declaring a survey manuscript or audit complete. Treat failures as remediation triggers, not reasons to lower the standard or delete required content.

## Contents

1. Evidence integrity
1. Coverage and source use
1. Thesis and architecture
1. Concepts and explanation
1. Synthesis and judgment
1. Cross-section discipline
1. Markdown and visual integrity
1. Final report

## 1. Evidence Integrity

Require all of the following:

- every cited source resolves to a verified ledger entry or supplied reference;
- every successful retrieval claimed in the source manifest resolves to a present, type-valid local artifact and its acquisition record;
- author, title, year, venue, identifier, quotation, and numerical facts are not invented;
- claims that depend on methods or results are based on sufficient source depth;
- quantitative statements and data-bearing visuals have recorded provenance;
- illustrative values are labeled and do not support empirical conclusions;
- claim strength matches evidence strength;
- systematic-review language appears only with a documented protocol.

Block on unresolved or fabricated citation details. If verification is impossible, mark the gap and narrow or remove only the unsupported claim.

## 2. Coverage And Source Use

Compare the declared search posture and scope with the corpus:

- recency-led reviews contain real evidence from the named window;
- timeline-spanning reviews cover decisive foundations, turning points, and the current frontier;
- balanced reviews include foundations, representative families, critiques, and recent work;
- major taxonomy categories, controversies, benchmarks, and claims have source support;
- relevant prior reviews are acknowledged and the present scope is distinguished;
- opposing or negative evidence is not excluded without reason.

Audit source disposition. Do not keep included sources that play no evidence or context role merely to inflate coverage. Do not omit on-scope sources solely because they complicate the thesis.

## 3. Thesis And Architecture

Require:

- an explicit, contestable review thesis;
- a clear reader payoff;
- a section sequence that advances the thesis;
- a frozen organization unit for every main-synthesis block;
- a successful sibling-heading test in which every parallel synthesis section represents one precise unit with stable membership criteria;
- one field-level claim per major section;
- body support for the conclusion and future directions;
- no abandoned early setups or unsupported late payoffs.

Fail an architecture that remains a chronology or method-name inventory without field-level movement. Also fail one that mixes field-level design axes, concrete methods or papers, method-specific explanatory questions, evaluation dimensions, and deployment settings as peer synthesis sections. Treat a representative method as a member of its field-level unit unless the review question and the complete synthesis architecture are explicitly method-specific. Do not use `topic`, `aspect`, `section`, or `part of the field` to force a false sibling match.

Apply this unit test within parallel synthesis blocks, not as a claim that introduction, review method, synthesis, discussion, and conclusion share one taxonomy unit. Require the visible heading hierarchy to expose each block boundary. Repair organization before using coverage or word-count balancing as the primary intervention.

## 4. Concepts And Explanation

Require:

- central terms defined before or at first conceptual use;
- stable distinctions among entities, representations, processes, claims, and metrics;
- shared frames before approach differences;
- complete explanations from distinguishing move to broader significance;
- taxonomy axes with a question, unit, criteria, overlap rule, and explanatory consequence;
- successful reader reconstruction for every major family and axis.
- paper-specific shorthand expanded at first use into the relevant objects, operations, held-fixed conditions, changed variables, measured outcomes, and inferential consequence.

Block when a reader must open a cited source merely to understand what an approach does or why the category matters.

Search for compression labels such as `unified protocol`, `controlled comparison`, `isolate`, `ablation`, `alignment`, `end-to-end`, `robustness`, and `framework`. Inspect each hit rather than banning the word: retain it only when the surrounding sentence makes its concrete meaning reconstructable for the declared reader.

## 5. Synthesis And Judgment

Require:

- paragraphs organized by claims and evidence relationships rather than author order;
- explicit roles for cited evidence;
- critique integrated into the comparison that exposes it;
- author-stated and survey-inferred limitations distinguished for major work;
- consensus, controversy, missing evidence, and field drift separated;
- an evidence-bound authorial position maintained throughout;
- future directions tied to demonstrated gaps and required evidence.
- each parallel synthesis unit covers the question and assumptions, core objects or mechanisms, representative relationships, evidence, failure conditions, and practical significance needed by the review; thin units are completed before strong units are cut merely for symmetry.

Fail citation piles, inert source lists, generic criticism, and conclusions stronger than the corpus.

## 6. Cross-Section Discipline

Check manuscript promises in both directions:

- the introduction's review question, organizing lens, and promised contributions appear in the body;
- definitions and notation remain consistent;
- each figure and table is introduced, interpreted, and used later when promised;
- datasets, metrics, or controversies named as important recur in analysis;
- the discussion synthesizes the main sections rather than introducing a new literature base;
- the conclusion does not repeat the abstract verbatim or introduce new claims.

## 7. Markdown And Visual Integrity

Check mechanically and visually:

- heading hierarchy is valid and contains no empty or duplicated sections;
- internal links, anchors, footnotes, citations, and relative file links resolve in the target renderer;
- tables render legibly and are discussed in prose;
- figures exist, match their captions, remain readable at normal scale, and cite their data or source;
- no absolute local paths, audit statuses, template fields, TODOs, or hidden drafting notes leak into the manuscript;
- terminology, names, citation keys, and numerical values are consistent;
- no defensive opening, meta-taxonomy heading, author-list rhythm, or generic AI scaffolding remains.
- negation and binary-reversal phrases are not used as recurring rhetorical scaffolding. Search headings, abstract openings, topic sentences, and conclusion claims for patterns equivalent to `not X but Y`, `X is not equal to Y`, `not only X`, and `X cannot represent Y`; inspect every hit and retain only evidence-bearing contradiction or necessary scope limitation.
- every cited work's first substantive mention uses verified leading-institution/team attribution and one Markdown link over the complete `Work(Year)` label when that metadata is available; the year uses ASCII English parentheses `(` and `)`, never full-width Chinese parentheses `（` and `）`; later mentions avoid repetitive affiliation bookkeeping. An unresolved label is blocking unless the workspace records the authoritative byline, PDF first page, proceedings or repository record, and authoritative project page checked as applicable, with the exact access failure or ambiguity for each. A missing field in a cache, parser, Markdown conversion, or secondary index never satisfies this condition.
- preprint version changes are not hidden behind combined aliases: title, method name, author-list, or substantive changes are represented with the exact supporting version and documented in the workspace.

Use available repository checks or renderers when present. A syntax pass does not replace reading the rendered manuscript.

## 8. Final Report

Report:

- manuscript path and workspace path;
- mode: build, revise, audit, or continue;
- scope and search posture;
- source and citation verification performed;
- structural, conceptual, explanatory, and prose checks performed;
- resolved blockers;
- accepted boundaries and exact remaining evidence gaps;
- files changed and any validation limitations.

Declare readiness only when all blocking gates pass. If a hard evidence limit remains, deliver the best bounded manuscript and state why it is not fully ready; do not pad, fabricate, or soften the gate.

Do not pass this gate by searching only for institution-shaped wording in the manuscript. Reconcile every first-mention attribution and every unresolved label against the corresponding paper note and persisted source evidence. Fail the audit when a note says unresolved while an acquired authoritative artifact contains a clear affiliation, or when the manifest claims a fallback artifact that is absent from disk.
