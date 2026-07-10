# Concepts, Taxonomy, And Explanatory Closure

Use this reference when a survey defines technical concepts, compares approaches, or uses a taxonomy.

## Contents

1. Explanatory contract
1. Term definitions
1. Approach explanations
1. Taxonomy validity
1. Architecture unit freeze
1. Multi-axis taxonomies
1. Reader reconstruction
1. Repair patterns

## 1. Explanatory Contract

Reconstruct the explanation the literature supports before selecting labels or categories. Use this generic dependency chain:

`shared question and conditions -> distinguishing mechanism or reasoning -> immediate result or claim -> connection to the broader phenomenon -> supporting evidence and inference -> scope boundary`

Adapt the nouns to the field. The chain may describe a technical process, theoretical argument, empirical measurement, historical change, clinical association, policy mechanism, or interpretive framework. Do not impose an operational pipeline on a field that does not have one.

Separate what compared approaches share from what they change. Record shared problem definitions, objects, observations, assumptions, and evidence conventions. Then state the specific intervention, relation, or claim that distinguishes each line.

Do not stop at an intermediate artifact such as a representation, score, measurement, theorem, generated object, category, explanation, or latent state. Explain what it permits the study to establish or do, how it connects to the broader phenomenon motivating the section, and what evidence supports that connection.

## 2. Term Definitions

Define a central term before or at first conceptual use. Give enough information to interpret the first claim containing it.

For each structure-controlling term, specify:

- **kind**: entity, representation, process, operation, relation, condition, constraint, claim, metric, or another field-appropriate kind;
- **referent**: what the term names in this review;
- **role**: why it matters in the explanation or argument;
- **applicability**: conditions under which the term applies;
- **boundary**: the nearest term or level from which it differs;
- **evidence anchor**: a source, mechanism, measurement, or consequence that makes the definition operationally meaningful.

A translation, synonym, example, motivation, metaphor, or list of instances is not a definition. Do not let one term silently change kind or referent across sections.

For capability or property terms, name the object that has the property, the operation or condition that gives it meaning, the observable consequence, and the evidence or test used to assess it.

## 3. Approach Explanations

For each major approach, family, theory, or empirical line, answer in prose:

1. What problem and conditions are shared with adjacent approaches?
1. Which object, relation, assumption, mechanism, or inferential step is focal?
1. How does the distinguishing move work at the depth required by the section claim?
1. What immediate result, artifact, observation, or proposition follows?
1. How does that result affect, explain, or support the broader phenomenon or outcome?
1. What evidence supports the interpretation?
1. What does the evidence not establish, and under which conditions does it hold?
1. How does the line relate to adjacent lines?

Write a compact working card if useful:

`shared frame -> focal change -> distinguishing move -> immediate result -> broader significance -> evidence -> boundary`

Keep the card in working notes. Convert it into coherent scholarly prose, a substantive table, or an explanatory figure before placing it in the manuscript.

## 4. Taxonomy Validity

Treat a taxonomy as a claim about the field. For every axis or grouping, record:

- the classification question;
- the unit being classified;
- membership criteria for each category;
- permitted overlap and multi-membership;
- the explanatory consequence of changing categories;
- the relation of the axis to the review thesis.

Reject or repair an axis when:

- labels name surface nouns without a stable analytical distinction;
- categories classify different units or mix conceptual levels;
- works routinely fit multiple categories but the display implies exclusivity;
- category membership requires repeated exceptions;
- a change of category changes no object, mechanism, assumption, evidence, or scope;
- the axis inventories implementation choices without helping answer the review question.

If an axis names something generated, predicted, estimated, measured, represented, or explained, classify the **focal object, relation, process, or claim on which the approach intervenes**. Do not imply that other necessary objects are absent merely because they are not focal.

Prefer labels that state analytical role or distinguishing relation over loose nouns that readers could mistake for the entire task.

## 5. Architecture Unit Freeze

Do not treat a valid taxonomy as sufficient proof of a valid article hierarchy. Before assigning or preserving main-synthesis sections, write one sentence that names their organization unit. Valid units include field-level design problems, mechanism families, historical turning points, controversies, evidence levels, or another unit justified by the review question.

For every group of parallel synthesis headings, complete:

`These sections are parallel because each represents a ____.`

The completion must be one precise noun phrase with stable membership criteria. Reject generic completions such as `topic`, `aspect`, `section`, or `part of the field`, because they conceal rather than test the classification.

Block the outline when siblings mix units such as:

- a field-level design axis;
- a concrete method, system, or paper;
- an explanatory question about one method;
- an evaluation dimension;
- an application or deployment setting.

A concrete method belongs beneath the field-level axis, family, controversy, or turning point it exemplifies unless the review question is explicitly method-specific and every sibling uses the same method-centered unit. Move a genuinely cross-cutting explanation into a cross-cutting analysis section; do not promote it into a peer category merely because it is evidence-rich.

Apply the test within each intended synthesis block. The outer article sequence may contain different functional roles such as introduction, review method, main synthesis, cross-cutting discussion, and conclusion; record those as article roles rather than pretending they are taxonomy categories. If the hierarchy does not visually reveal where the parallel synthesis block begins and ends, add or rename a parent heading instead of relying on hidden author intent.

Persist in `06-taxonomy-and-outline.md`:

- the organization unit sentence;
- the headings governed by it;
- the completed sibling sentence;
- membership criteria and any permitted overlap;
- the disposition of methods or questions moved to a lower or cross-cutting level.

Do not begin synthesis prose until every parallel group passes. After the hierarchy passes, audit coverage depth across its units: core question and assumptions, mathematical or conceptual objects, representative relationships, evidence, failure conditions, and system or practical significance where relevant. Repair thin units before trimming a well-supported unit merely for visual symmetry.

## 6. Multi-Axis Taxonomies

Make each axis answer one distinct explanatory question. Treat axes as coordinates unless the evidence justifies exclusive families: one work may take a value on several axes.

Order axes by conceptual dependency, not by the order in which the writer discovered them. Explain shared objects and conditions before the dimensions on which approaches diverge.

Test each axis against representative, boundary, and hybrid cases. A useful axis should help a reader predict at least one difference in mechanism, assumption, evidence, interpretability, applicability, or failure mode.

Do not turn the number of axes or rejection of an older label into a manuscript heading. Name the scholarly subject or distinction that the classification illuminates.

## 7. Reader Reconstruction

Test each major family and taxonomy axis without consulting internal notes. Reconstruct it in two to four sentences containing:

- the shared problem;
- the focal distinction;
- how the distinguishing move works;
- how any intermediate result connects to the larger question;
- the evidence and boundary.

Fail the passage if reconstruction requires guessing, importing unstated domain knowledge, or repeating labels without relationships. A citation does not repair missing explanation; the manuscript must remain intelligible while the citation supplies support and detail.

Run a paper-shorthand expansion check. Highlight phrases inherited from abstracts or method sections, including `unified protocol`, `controlled setting`, `isolate factors`, `ablation`, `alignment`, `end-to-end`, `robustness`, `framework`, and named intermediate modules. For each phrase, ask whether the intended reader can state:

- what concrete objects, data partitions, or system components are involved;
- what was held fixed and what was varied;
- what operation connects the input to the reported output;
- what observable comparison licenses the survey's interpretation.

If any answer is absent, replace or immediately unpack the shorthand. Keep the field's useful vocabulary after explaining it; do not flatten technical content into generic prose.

## 8. Repair Patterns

Repair the smallest broken dependency that restores understanding:

- add or move a first-use definition;
- identify the shared frame before differences;
- explain the missing mechanism or inferential step;
- expand experimental shorthand into held-fixed conditions, changed variables, measured outcomes, and the resulting inference;
- connect an intermediate artifact to the broader phenomenon;
- distinguish a focal object from supporting objects;
- rename a category by analytical role;
- clarify overlap or represent a work on multiple axes;
- merge categories with no explanatory consequence;
- split an axis that mixes classification questions;
- demote a representative method beneath the field-level unit it exemplifies;
- move a method-specific explanatory question into the method subsection or a justified cross-cutting analysis;
- add a parent heading that makes the boundary of a parallel synthesis block explicit;
- replace a weak taxonomy with another organizing logic;
- narrow a claim when evidence cannot support the full explanation.

When restructuring, redistribute valid sources, concepts, and unresolved questions. Delete only material shown to be redundant, out of scope, unsupported, or unnecessary to the review argument.
