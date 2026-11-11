# Sources and decisions

Maintenance record; not installed with the skill and not a runtime step. Runtime rules live only in [SKILL.md](../../software-design-philosophy/SKILL.md) and its references; this page records where they came from and why. Older book notes, Q&A transcripts, full research write-ups, and earlier test reports are in Git history (the pre-refactor source decisions are at `1f3d992`).

## Source roles

- John Ousterhout, *A Philosophy of Software Design* (2nd ed.): the main lens for complexity, information hiding, deep modules, comparing candidates, and performance judgment.
- Robert C. Martin, *Clean Architecture* and related work: axes of change, dependency direction, system boundaries, lifecycle responsibility. Layers, use cases, or technology labels are not boundary conclusions by themselves.
- A user-provided discussion of Linux filesystem design: shared resource invariants, complete workflows, advanced capabilities that return to shared governance.
- `ByteByteGoHq/system-design-101` at `b28380a4`: only judgments about boundaries, state, and failure semantics were kept; no company cases, product catalogs, capacity numbers, or upstream figures.

Sources do not override explicit user requirements.

## User decisions

These come from the user directly and take precedence over earlier summaries or the maintainer's own inferences. Do not remove them merely because a model might infer them.

- Simple tools and small programs do not get a dedicated test / agent debugging surface; once complexity rises, ask the user. Asking is not authorization to build one.
- Judge reference reads by relevance and cost; reading an extra file is not a failure. Explicit delivery scope still applies.
- "How do I fix and migrate this?" is a consultation: a full recommendation is a valid delivery; do not escalate to implementation.
- Derive constraints from the user's stated goals first. When still unsure, give conditional conclusions for a few key scenarios and ask only about information that changes the decision and cannot be derived.
- Performance-relevant structure is in scope for an architecture audit of a high-performance library, including measurement, baseline, and optimization recommendations; recommendations do not authorize implementation.
- Not every project needs mutation testing; choose by risk, tool fit, and runtime cost.
- No defensive additions in the skill: no reverse inferences, imagined rebuttals, exception lectures, extra proof or reporting duties, or repeated acceptance steps.
- `software-design-philosophy` and `clarity` may be installed independently; neither references the other at runtime.
- Cyclomatic complexity > 10 triggers this skill's review, combined with coverage and other design principles; it is a review condition, not a mandate to split or rewrite. It lives in the body, not the description: a model that has not loaded the skill does not measure CC, so it cannot trigger loading.
- During ordinary coding, strategic modification compares the from-the-start structure; when that comparison reveals a meaningful gap, register it as cumulative debt and propose the refactor. Refactoring existing structure happens in-task only when requested; new designs still use the comment-first and alternative-design rules.

## Personal preferences and where they live

| Old record | Kept intent | Current location |
|---|---|---|
| C01 tests and design | Do not generate architecture by TDD by default; verify by risk | [Test protection](../../software-design-philosophy/references/design-behavioral-tests.md) |
| C02 limited interfaces | Shared invariants, complete workflows, long-tail ownership, escape hatches that return to shared governance | [Deep modules](../../software-design-philosophy/references/design-deep-modules.md) |
| C03 future options | Current simplicity; narrow seams only for evidenced, hard-to-reverse change | [SKILL.md](../../software-design-philosophy/SKILL.md) |
| C04/C06 use cases and metrics | Knowledge and change evidence; no automatic refactoring by use-case count, class count, or local dependency metrics | [Module boundaries](../../software-design-philosophy/references/design-module-boundaries.md) |
| C05 importance and performance | Check interface gaps first; necessary performance entry points; main flow first in v1; performance context does not widen the user's goal | [Performance](../../software-design-philosophy/references/design-measured-critical-paths.md) |
| C07 implementation inheritance | The user rejects multiple-base implementation inheritance; a preference, not a language fact | [Module boundaries](../../software-design-philosophy/references/design-module-boundaries.md) |
| C08 debugging surface | Agent-friendly, production-isolated; ask only once complexity rises (see user decisions) | [Test protection](../../software-design-philosophy/references/design-behavioral-tests.md) |
| C09 architecture classification | Relative scope; structural mechanism versus local fix; no forced dual severity scale or report template | [Architecture audit](../../software-design-philosophy/references/audit-software-architecture.md) |
| C10–C12 pattern additions | Pressure, authority, failure, and cost as conditional system contracts; no full-catalog loading | [System boundaries](../../software-design-philosophy/references/design-system-boundaries.md) |

## Failures the structure protects against

Earlier test records found three behavioral errors: using severity in place of architectural category, letting performance context take over the delivery, and mutually exclusive methods causing omissions. They are covered by the audit admission criterion, the entry's scope rules, and on-demand combined reading. An older "load all 11 methods and four pattern families" fix for a recall blind spot was replaced by putting discovery criteria into the compact audit reference; the recall of that structure still needs behavioral evaluation.

## Revision log

### Core compression (baseline `0037221`)

Removed duplicate definitions, teaching steps, example padding, and duplicate routing; kept personal preferences, easily misused boundaries, and necessary counterexamples. No new research or policy. Review restored distinguishable error results and the check that evolution reduces caller knowledge.

### 2026-09-08 research additions

See [research summary](research-2026-09-08.md). Added implicit consumer dependencies and test-double fidelity (evolution), reachability of authoritative knowledge (module boundaries, audit), independent acceptance evidence and starting scenarios versus real operations (interfaces), and collaborative write ownership with composition checks (evolution). Kept task-oriented references with no AI-specific branch; did not adopt whole-repo regeneration, fixed role counts, or an optimal instruction length.

### 2026-10-10 deep modules and internal stages

Module depth describes public capability versus interface burden; it does not require one long function. Internal stages may hide detail but must not cut through a state, transaction, lock, or resource-recovery invariant. Qwik and Ferret agent guides (pinned commits) supported judging extraction from call sites and reading the full implementation scope; only the boundary judgment was adopted.

### 2026-10-30 ub-mode integration

Source: [`ub-mode` at 57a8bdd](https://github.com/unclebob/ub-mode/blob/57a8bdd28e45ed41900ace0bafa2ff76dd9ed70f/SKILL.md), with [`crapper`](https://github.com/unclebob/crapper/blob/6fd92c4c9bcc56efb64a2f8743d5a2993bcfd42d/README.md), [`dryer`](https://github.com/unclebob/dryer/blob/66ff6d21a42c04afcad89c78a80066176d1294b0/README.md), [`mutator`](https://github.com/unclebob/mutator/blob/a5a0cb803b66e0cdb8bf471b3b08af701d424a41/README.md), and [PIT concepts](https://pitest.org/quickstart/basic_concepts/).

| Adopted | Runtime location and trade-off |
|---|---|
| CC, coverage, CRAP | Entry triggers review at `CC > 10`; audit explains the formula and counting rules. `crapper` records missing coverage as 0%, so the runtime requires separating failed measurement from real coverage. At 100% coverage `CRAP = CC`, so no uniform `CRAP < 10` cutoff |
| Structural duplication, verification effectiveness | Audit uses similarity to find shared knowledge; targeted mutation by risk, separating equivalent mutants and execution errors |
| Valid representation, domain vocabulary, type constraints | Module boundaries connect boundary validation with internal constraints |
| Shared state, shared premises | Check whether sharing is needed; re-examine premises when successive patches fail |
| Separating decisions from effects | Deep-module stages may separate deterministic computation from effects while keeping required atomicity |
| Sample-first bulk automation | Verify one complete slice before scaling an automated transformation |

Upstream single-writer, pure-function, and auto-tooling requirements became conditional judgments.

### 2026-10-30 test protection and maintenance cost

Added an on-demand test reference covering admission of new permanent tests, support-code cost review, and stopping. Sources, each adopted narrowly:

| Source | Adopted |
|---|---|
| [Hypothesis agent command, 3fc38f1](https://github.com/HypothesisWorks/hypothesis/blob/3fc38f1d6a6b1752bf5fad61d44ee79d31d35406/.claude/commands/hypothesis.md) | Few evidence-backed properties; stopping is fine when none is worth testing; reference models must not copy the logic under test |
| [Google, Practical Mutation Testing at Scale (2021)](https://homes.cs.washington.edu/~rjust/publ/practical_mutation_testing_tse_2021.pdf) | Incremental analysis, filtering low-value mutants; a killable mutant is not automatically worth a permanent test |
| [Kent Beck, Composable Tests (2025)](https://newsletter.kentbeck.com/p/composable-tests) | Compose tests over dimensions shown to be independent; keep failure localization when removing duplicate protection |
| [Meta, Just-in-Time Catching Test Generation (2601.22832v1)](https://arxiv.org/html/2601.22832v1) | Separate finding bugs in this change from long-term regression protection |

No fixed test/code ratio, mutation budget, or reduction target. These are engineering judgments, not empirical results for this skill.

### 2026-11-09 cumulative knowledge duplication

The Tessera audit (PR #68) found duplication accumulated across PRs even though every PR was developed and reviewed with this skill: two case-ID formats parsed by position in several places, Rust and C++ indexing the same records with separate type numbering, a parallel engine copying the probe flow and counting window to protect serial codegen, and stale module names in docs. Each was locally reasonable and below the architectural criterion. The rules allowed retained copies but never required a trackable record. Added: find the existing authority before adding a consumer of shared knowledge; drift detection for retained copies that catches mismatches between copies (from a Tessera bug where a null-pattern check missed swapped columns with identical null patterns); recording the measurement behind performance duplication; registering sub-threshold duplication as cumulative debt. Evidence is one audit; not claimed as a general law.

### 2026-11-09 maintainers without session context

Another agent's maintainability analysis proposed a new cost vocabulary; most of it already existed. The one uncovered point: whose cognitive load counts. The authoring agent knows its session's conventions and underrates them. Cognitive load and unknown dependencies are now measured for a maintainer who has only the repository; a paired counterexample prevents flagging conventions that are already in a checked contract.

### 2026-11-09 coding-time design steps

Agent development proceeds by minimal changes per task, which is the book's tactical programming. Added three of the book's practices: write the interface comment first; design it twice (limited to new modules and public interfaces); strategic modification, triggered only when the minimal change would add a special case, flag, parallel entry point, or second interpretation, with external protocol differences excluded. Not yet behavior-tested.

### 2026-11-11 English translation and consolidation

Runtime files translated to English; maintenance docs translated and condensed. A `/simplify` review with four angles found that the four 2026-11-09 additions were versions of one missing rule filed in four places, and three copies had already drifted (the performance copy dropped mismatch detection; SKILL.md's two triggers disagreed on registering debt). Consolidated:

- Retained copies and cumulative debt: one rule in [module boundaries](../../software-design-philosophy/references/design-module-boundaries.md#retained-copies); SKILL.md, audit, and performance link to it.
- Advanced entry point ownership: owned by deep modules; performance keeps only view/span semantics.
- Debugging surface (C08): moved to the test reference, with a routing row.
- Unknown-outcome classification: owned by error handling; system boundaries keeps the protocol.
- Smaller merges: metrics routing row into the audit row; test trim/stop sections (trimming applies only when tests were added or rewritten); the last two sections of global simplification.

The user then approved narrowing the description from "touching modules" to "deciding structure", with an explicit exception that keeps strategic modification in scope: edits inside an existing structure trigger the skill when they add a special case, flag parameter, parallel entry point, or second copy of a rule. The entry now says `CC > 10` triggers a review, not a required change; it stays out of the description (see user decisions). The user also adopted "record and propose" for coding-time structural gaps, with in-task refactoring only on request.

Considered but not applied, because they reverse earlier user decisions: removing `CC > 10` from the entry and limiting design-it-twice to hard-to-reverse decisions. Test prompts remain in Chinese, now exercising Chinese requests against English instructions.

### Translation follow-up: conditional rules and reachability (0.17.1)

The user requested a clarity-based correction after a static review found that some consolidations joined rules with different conditions. Retained copies and cumulative debt now have separate sections: necessary boundary copies can be part of the intended design, while deferred structural improvements need not involve copies. Performance-motivated implementation duplication still records the evidence needed for merging. A special case or flag triggers comparison, not automatic debt; a meaningful gap is required. The coding introduction now scopes complete structural changes to new designs and requested refactors.

Restored the external-operation outcome distinction (confirmed success, confirmed rejection/non-execution, unknown), which is separate from error retry classification. Fixed migration wording that retired necessary seams, and removed the automatic merge recommendation for pipeline stages lacking transformations. The description includes internal structural decisions; deep modules links to the debugging-surface preference for complex or hard-to-reproduce workflows. These are static corrections, not observed behavior improvements; verification is recorded in the test results.
