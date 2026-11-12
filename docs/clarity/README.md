# clarity maintenance

`clarity/` holds the installable skill; this directory holds source records, and validation material is in `tests/clarity/`. Neither is installed or needed at runtime.

The skill covers conversational replies, persistent text, and code expression. Explaining, answering, reporting, and multi-step implementation trigger it without an explicit request to polish. Design discussion is an on-demand reference inside the same skill, covering proposals, decision records, and implementation feedback; it is not installed separately.

## Where to start

| Task | Entry |
|---|---|
| Scope, delivery boundaries, division of references | [Skill main file](../../clarity/SKILL.md) |
| Changing one kind of writing guidance | [Read references by problem](../../clarity/SKILL.md#read-references-by-problem) |
| Checking source text, versions, attribution, and adoption scope | [Sources and adoption boundaries](sources.md) |
| What has been verified and what limits remain | [Validation results](../../tests/clarity/test-results.md) |
| Choosing or adding reusable acceptance scenarios | [Test cases](../../tests/clarity/test-prompts.json) |
| Checking code outputs, isolated solvers, and judge inputs | [Code fixtures](../../tests/clarity/fixtures/README.md) |

## Document responsibilities

- `sources.md` records actual sources, case versions, and limits that affect use, by guidance topic; it does not copy runtime rules.
- `tests/clarity/test-results.md` summarizes coverage, findings, and results, and may keep actual answers to selected cases with the grounds for checking them. Case definitions live only in `test-prompts.json`.
- Raw agent replies, temporary downloads, round-by-round edit logs, and unused research drafts are not kept as maintenance documents.

## Admitting runtime content

Keep constraints that change the model's default behavior, boundaries that are easy to misapply, and the short examples needed to explain them. General writing knowledge, genre tutorials, and long case studies stay out; importance or a reliable source alone is not a reason to add something.

Over-compression, straw-man corrections, substantive semantic fidelity, code inlining, and maintenance comments keep explicit principles even though models have heard of them. For a new failure, first decide whether an existing rule was not followed or a rule is actually missing; do not turn every deviation into a patch instruction.

Runtime files are written in English. Deliverables follow the language the user asks for or the existing work uses.

## Self-consistency check after changes

Check the main file, references, positive and negative examples, and test expectations against each other. Read each positive example as a finished product: even when it follows the rules, it can still be redundant, preachy, or vague. When it is, fix the rule and the example together, and prepare adjacent should-change and should-keep scenarios to confirm the fix does not damage meaning.

Check responsibilities too. Shared rules apply to conversational replies and persistent text; the design discussion reference is used only when the task needs design discussion or record maintenance. Ordinary polishing adds no investigation, approval, or workspace, and design discussion does not widen tool or execution permissions. Process requirements already in a source text are content to keep; do not delete user requirements to make the skill shorter.

Acceptance checks both whether meaning is preserved and whether readers must supply relations themselves. Short sentences, tables, summaries, and fewer words are not evidence of improvement by themselves; check that examples build on established context and that follow-up questions get a direct answer. Real readers' understanding and impressions can only be judged from real feedback; the author's own review is not reported as a measured effect.

In test records, keep static checks, self-answered scenarios, and trial runs separate. Maintenance activities are not a required step each time someone uses clarity.

For code implementation regressions, check the actual output's behavior first, then judge the main line, state, and phase boundaries by reader task. Check together that complete single-use phases are kept, thin helpers are inlined by default, and cohesive state machines stay whole. Install the two skills in isolation from each other; at runtime neither may depend on the other's path, and using both does not turn ordinary local tidying into architecture design.
