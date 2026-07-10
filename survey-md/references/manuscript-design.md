# Manuscript Design And Scholarly Prose

Use this reference when designing or repairing the article architecture, sections, headings, paragraphs, figures, tables, and prose surface.

## Contents

1. Authorial position
1. Article architecture
1. Section contracts
1. Section roles
1. Setup and payoff
1. Paragraph design
1. Headings and scope language
1. Figures and tables
1. Style discipline

## 1. Authorial Position

State an evidence-bound, contestable view of how the field is structured, what its evidence establishes, which conditions change the interpretation, or what should follow from the comparison.

Do not confuse authorial position with unsupported opinion, promotional language, or a claim that the manuscript is better than a paper list. Let the position control scope, organization, evidence selection, comparison, criticism, and conclusion. Revise it when the corpus contradicts it.

## 2. Article Architecture

Choose an organization that answers the review question. Options include:

- taxonomy or problem decomposition;
- chronology organized around turning points;
- controversy or assumption map;
- evidence ladder from feasibility to external validity;
- process or system anatomy when the field has meaningful stages;
- cross-domain transfer and failure;
- order of explanatory importance.

Write an architecture contract before drafting:

- central thesis;
- reader starting point and intended payoff;
- section sequence and its rationale;
- field-level claim for every major section;
- role of foundational, representative, contradictory, and boundary sources;
- cross-cutting threads that must recur;
- early setups and later payoffs;
- how the discussion, future directions, and conclusion follow from the body.

Use this default arc only when it fits:

1. Abstract
1. Introduction
1. Review method or scope
1. Conceptual background and explanatory frame
1. Field map or organizing lens
1. Main synthesis sections
1. Cross-cutting analysis
1. Consensus, controversies, and open problems
1. Evidence-grounded future directions
1. Conclusion

Combine, rename, or reorder sections when another path better serves the argument.

## 3. Section Contracts

Give each major section:

- one field-level claim;
- the concepts and prior sections it depends on;
- the evidence relationships that establish or qualify the claim;
- integrated strengths, limitations, and boundary conditions;
- a transition that changes what the reader can now understand;
- a payoff in a later section, conclusion, or future direction.

Do not use a method name or time period as a section merely because papers can be filed beneath it. State what that family or period changed and failed to settle.

Write the abstract after the body stabilizes. Make it state the problem, scope, thesis, organizing lens, principal synthesis, and consequential gaps. Make the conclusion return to the thesis and explain what the literature should now be understood to show.

## 4. Section Roles

Use each section for a distinct scholarly function:

- **Abstract**: state the problem, actual scope, thesis, organizing lens, central synthesis, and consequential gaps. Do not include drafting defenses or promises the body does not fulfill.
- **Introduction**: explain why the literature is difficult or important to integrate, pose the review question, state the authorial position, delimit coverage, and establish the reader path.
- **Review method or scope**: report search posture, sources, dates, screening logic, inclusion and exclusion, access gaps, and protocol limits. Do not use systematic-review vocabulary without the corresponding record.
- **Conceptual background**: define only the concepts, distinctions, mechanisms, and evidence conventions required by later synthesis. Do not turn background into an uncited textbook chapter.
- **Field map or taxonomy**: introduce a tested organizing lens and its criteria after the shared explanatory frame is clear.
- **Main synthesis sections**: advance one field-level claim, compare evidence, integrate critique, and end with the unresolved boundary that motivates the next section or discussion.
- **Cross-cutting discussion**: synthesize patterns across earlier families, evidence regimes, or debates. Do not introduce an unrelated literature base merely to make the discussion appear broader.
- **Open problems and future directions**: derive each direction from an established gap and state the evidence needed to resolve it.
- **Conclusion**: answer the review question at the strength permitted by the corpus. Do not add new sources, categories, or claims.

Ensure that prior reviews are not merely counted. Contrast their questions, periods, evidence bases, and organizing lenses with the present review when that distinction matters to scope or contribution.

## 5. Setup And Payoff

Audit both directions:

- Every concept, source, dataset, metric, controversy, example, metaphor, table, or figure introduced early must support a later comparison or conclusion; otherwise remove or demote it.
- Every late conclusion, criticism, taxonomy distinction, or future direction must have evidence and conceptual setup earlier in the manuscript.

Do not leave decorative examples, abandoned terminology, one-off benchmark names, or future directions introduced only because they sound plausible.

## 6. Paragraph Design

Prefer this movement:

`field-level claim -> comparative evidence -> relationship among sources -> survey inference -> boundary or consequence`

Vary the form when the argument requires it, but preserve movement. Introduce a paper by author when it is a foundation, turning point, contradiction, or representative case; avoid making most paragraphs a sequence of author-led summaries.

Anchor abstract terms near concrete evidence, mechanisms, measurements, or consequences. Explain why each cited source matters to the paragraph. Put criticism where the comparison exposes it rather than in a detached limitations dump.

Translate experimental and method labels into actions before drawing the field-level inference. For example, replace `the study isolates model scale, identifier design, and training strategy under a unified protocol` with a compact explanation that the authors reuse the same datasets, cold-start splits, metrics, and base pipeline, then change model size, identifier construction, and training objective one at a time. The intended reader should see what the comparison controls and why the result is attributable, even if they never open the cited paper.

At a work's first substantive appearance, prefer the compact pattern `verified leading institution/team + linked work name with parenthesized year + evidence role`, for example `Alibaba's [RecGPT(2025)](...) reframed intent extraction as a semantic middleware task`. Put the whole `Work(Year)` label inside one Markdown link. The year must use ASCII English parentheses, `(` and `)`, never full-width Chinese parentheses such as `（2025）`. Avoid detached citation introductions such as a bare linked title, author-year bookkeeping, or an institution list with no argumentative role. Later mentions may use the short work name without repeating the institution and year.

When prose feels artificial, repair hierarchy and evidence before editing style. Common structural causes include inert source lists, a forced thesis, missing explanatory links, misplaced abstraction, and unsupported payoff.

## 7. Headings And Scope Language

Make headings name a scholarly object, process, relation, evidence boundary, controversy, or field-level claim. A heading should tell the reader what will be understood, not how the writer organized notes.

Prefer positive nominal or relational headings such as `Alignment between content and collaborative objectives`, `Mapping quality across collision and prefix structure`, or `Evidence boundaries of industrial deployment`. Avoid correction-shaped headings such as `X is not Y`, `X cannot replace Y`, `not only X`, or `X rather than Y` unless the section analyzes an actual, sourced controversy whose competing propositions must be named.

Remove headings and prose that:

- advertise the number of taxonomy axes;
- argue against a discarded label;
- narrate classification or drafting decisions;
- expose audit prompts or template fields;
- announce only that a section will discuss a topic.

Describe scope affirmatively: state the question, evidence base, time window, inclusion logic, and coverage limits. Put protocol and access limitations in the method or scope discussion. Do not lead the abstract or introduction with what the manuscript is not.

Preserve a substantive authorial stance while removing defensive self-description.

## 8. Figures And Tables

Use a figure or table only when it makes a relationship materially easier to inspect. Strong artifacts include:

- a taxonomy with explicit criteria and overlap;
- a turning-point timeline rather than every paper by year;
- an evidence or benchmark map showing what each source can establish;
- a controversy map linking assumptions, evidence, and unresolved tests;
- a mechanism or reasoning diagram that closes an explanatory gap;
- a gap map stating why prior evidence is insufficient and what would close it.

Tie every artifact to a prose claim. Provide a standalone caption, define symbols and categories, cite source data, and discuss the artifact in the text. Do not make a table the outline of the prose or use it to hide weak explanation.

In Markdown, use stable headings, readable tables, relative links for project files, and citation syntax consistent with the user's toolchain. Preserve source or generation data for nontrivial figures.

## 9. Style Discipline

Write formal, direct scholarly prose. Use explicit subjects and synthesis verbs such as `distinguishes`, `extends`, `contradicts`, `constrains`, `reframes`, and `depends on`.

Remove:

- defensive claims about what the survey is not;
- repeated binary-reversal scaffolds such as `not X but Y`, `X is not equal to Y`, `not only X`, and `X cannot represent Y` when a direct statement of constructs, conditions, or scope would carry the argument;
- writer-process commentary and audit residue;
- oral phrasing, translationese, and inflated transitions;
- vague evaluations such as `important`, `effective`, or `promising` without criteria;
- citation piles and long noun lists without relationships;
- generic claims such as `many studies exist` or `future work is needed`;
- matrix field names copied into prose as if they were concepts;
- paper-internal compression such as `unified protocol`, `controlled experiment`, `factor isolation`, `alignment`, `end-to-end`, `robustness`, or `ablation` when the prose omits the concrete objects, operations, comparisons, or consequences behind the label;
- polished sentences that retain a paper-list structure;
- critique that only repeats authors' limitations;
- conclusions or future directions not earned by the body.

Keep necessary methodological limits and uncertainty, but express them as scholarly scope and evidence boundaries rather than apologies or drafting notes.

Negation is sometimes necessary for falsification, contradiction, and evidence limits. Audit its function: the sentence should identify a specific rejected proposition and nearby evidence. When negation merely creates rhetorical contrast, replace it with a direct relation, for example `A and B measure different properties`, `A supports condition C`, or `the evidence is limited to setting D`.
