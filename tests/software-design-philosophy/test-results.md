# software-design-philosophy: validation records

One section per revision, newest first. Each records what changed in the runtime, how the test set changed, and what was actually verified. Raw outputs, workflow IDs, file hashes, byte tables, and the earlier standalone pages (`luna-simplification-validation.md`, `research-validation-2026-09-08.md`) are in Git history. Sources and decisions are in [source decisions](../../docs/software-design-philosophy/source-decisions.md).

"Not verified" means not verified: a test case's prompt and expected behavior existing is not a pass, and static checks are not evidence of behavior.

## Current revision: translation follow-up (0.17.1)

Runtime: separated retained copies from cumulative debt; preserved the performance-copy merge-evidence requirement; made a meaningful structural gap the condition for debt registration. Scoped complete structural implementation to new designs and requested refactors. Restored internal design decisions to the trigger and added a deep-module route to the debugging-surface preference. Restored confirmed-success / confirmed-non-execution / unknown outcomes separately from error classification. Fixed the migration-seam lifecycle and the automatic pipeline-stage merge recommendation; clarified joining writers before the operation returns.

Tests: 98 → 103. Added adjacent cases for necessary boundary copies, external outcome versus retry classification, migration-seam lifetime, pipeline isolation, and a flag with no structural gap. The existing private-stage case now also tests triggering. The dry-run consultation expectation explicitly stays a consultation and distinguishes structural debt from copy checks. Existing performance-copy, external-adapter, debugging-surface, local-readability, and explicit-refactor cases remain as controls.

Verified: JSON parsing and unique test IDs, local Markdown links and anchors, runtime reference reachability, English-only runtime text, `git diff --check`, and manual comparison of the affected rules and adjacent expectations. Not run: independent model answers or natural-trigger behavior. The five new cases are evaluation material, not passing behavior results.

## 2026-11-11 English translation and consolidation (0.17.0)

Runtime changes:

- `SKILL.md`, `agents/openai.yaml`, and all 9 references translated to English.
- The retained-copies rule now lives in one place, `design-module-boundaries.md#retained-copies`. `SKILL.md`, the audit, and the performance reference link to it. The performance copy had dropped the requirement that the check catch mismatches between copies.
- Ownership of advanced entry points is defined in `design-deep-modules.md`; the performance reference keeps only view/span ownership and lifetime.
- The debugging-surface preference moved from `design-deep-modules.md` to `design-behavioral-tests.md`, with a routing row in `SKILL.md`.
- The metrics routing row merged into the audit row.
- In the tests reference, the trim and stop sections merged; trimming applies only when this round added or rewrote tests.
- In `search-global-simplification.md`, the last two sections merged and now link to the retire-old-mechanisms section of the evolution reference.
- The unknown-outcome classification is owned by `reduce-exception-surface.md`; system boundaries keeps the unknown-outcome protocol.
- The description now triggers on structural decisions rather than any module edit; edits inside an existing structure still trigger when they add a special case, flag parameter, parallel entry point, or second copy of a rule. `CC > 10` stays in the body only (a model that has not loaded the skill does not measure CC), and the entry states it triggers a review, not a required change. Existing trigger cases (error contracts in case 6, cross-module understanding cost in case 46) were checked against the new wording by reading only; natural-trigger behavior was not run.
- Strategic modification during ordinary coding now registers the gap as cumulative debt and proposes the refactor; structural adjustment happens in-task only when the user asked for a refactor.

Tests: 97 → 98, version 0.17.0. Case 96 (`edge-tactical-flag`) expectation updated to recommend rather than perform the refactor; new case 98 (`edge-tactical-refactor-requested`) covers an explicit refactor request. Other cases unchanged.

The test prompts stay in Chinese; they now act as Chinese user requests against English instructions.

Verified: skill-creator `quick_validate.py`, local links and anchors, `git diff --check`, no CJK left in runtime files. Not run: model behavior regression, so translation fidelity and the consolidations are not behavior-tested.

## 2026-11-09 coding-time design steps (0.16.0)

Runtime: three additions to "Coding and simplification". Write the interface comment first for new modules or public interfaces, and adjust the design if it cannot be written briefly or needs internal steps. Sketch at least one structurally different alternative for new modules or public interfaces. When a minimal change would add a special case, flag, parallel entry point, or second interpretation, compare against the structure the requirement would have produced from the start; register deferrals as cumulative debt.

Tests: 93 → 97. Four boundary cases, a positive and negative case per rule: an interface comment that leaks protocol, alternatives required only for public interfaces, a flag-parameter change, and external-protocol special cases that are not debt.

Verified: `quick_validate.py`, JSON parsing, local links and anchors, `git diff --check`. Not run: independent model answers or behavior regression.

## 2026-11-09 maintainers without session context (0.15.0)

Runtime: the first shared judgment now measures cognitive load and unknown dependencies for a maintainer who works only from what the repository contains; conventions that exist only in the author's session or memory count as unknown dependencies.

Tests: 91 → 93. A pair: a convention that exists only in the author's context is an unknown dependency; the same convention written into a contract and checked by assertions and tests is not, and needs no new abstraction.

Verified: same static checks as above. Not run: model answers or regression.

## 2026-11-09 cumulative knowledge duplication (0.14.0)

Runtime: four rules. Find existing interpreters before adding a consumer and list new consumers in review; detect drift when keeping multiple interpretations; record the measurement and register merge evidence for implementations duplicated for code generation; list sub-threshold duplication as cumulative debt. (Consolidated into one rule in the 2026-11-11 revision.)

Tests: 87 → 91, one case per rule, taken from real situations in the Tessera audit: positional ID parsing, C++/Rust type numbering, a parallel entry point copying a probe flow, and small sub-threshold duplicates.

Verified: same static checks. Not run: model answers or regression; not shown to reduce duplication in real projects.

## 2026-10-30 test protection and maintenance cost (0.13.0)

Runtime: a new on-demand tests reference, linked from the entry, the audit, and evolution. It covers test admission, reuse order, cost review, filtering exploratory tests, optional mutation checks, and when to stop.

Tests: 79 → 87. Eight cases: stopping once protection is sufficient, strengthening an existing parameter table, the budget exception for minimal regressions, coverage/mutation signatures not being enough to delete a test, independent dimensions versus interactions, low-value or unknown mutants, exploration versus permanent admission, and choosing mutation by project payoff and cost.

User corrections: mutation testing is not needed in every project, so tool fit and runtime cost became selection conditions. The user then asked for defensive additions to be removed across the runtime: reverse inferences, imagined objections, exception walkthroughs, extra proof or reporting duties, and repeated acceptance steps. Runtime Markdown went from 12,236 to 8,534 characters. Independent subagent reviews found nothing that had to be fixed.

Verified: `quick_validate.py`, YAML/JSON parsing, local links and anchors, runtime reference reachability, preservation of the original cases and execution protocol, `git diff --check`. Not run: model answers or full regression; no claim that it reduces real test cost.

## 2026-10-30 ub-mode integration (0.12.0)

Runtime: a soft cyclomatic-complexity review trigger in the entry; CRAP and coverage counting rules in the audit; valid representations and state ownership in module boundaries; separating decisions from effects in deep modules; sample-first automation and targeted mutation in evolution.

Tests: 66 → 79, with 13 cases covering metrics, trust boundaries, shared state, mutation results, and migration boundaries. One mutation case's expected behavior assumed an assertion gap the prompt had not established. The prompt now states the observable error on legal input.

Verified: static checks. A fresh independent executor answered 9 targeted consultation tasks (not the 13 new JSON cases) using only the skill and the raw prompts. Its answers matched the intended judgments:

- It computed CRAP and prioritized the thinly covered permission boundary.
- It treated a failed coverage run reporting 0% as unknown.
- It reused a protected valid representation while checking revocable permissions where they are used.
- It accounted residency by active tasks.
- It kept an existing transaction instead of adding an actor.
- It separated equivalent mutants and compile errors from behavior gaps.
- It traced repeated charges to a fresh business ID on each retry.
- It verified one complete slice before automating an adapter migration.
- It kept the atomicity needed when moving an inventory check.

Not run: the full 79-case set, implementation fixtures, or upstream metric tools. No measurement of old versus new.

## 2026-10-14 autonomous design and simplification (0.11.0)

Runtime: kept complete operations, information hiding, and internal stage organization; added state origin, lifecycle cost, and cleanup along the old concept; removed generic task discipline.

Tests: 61 → 66. Three new cases (first-time module design, derived cache vs. historical snapshot, per-task residency cost) were not run individually.

Verified: an independent executor given only the skill and an over-wrapped exported module with its public contract simplified the code directly. It retired the encoder, task records, state objects, and stage protocol, and kept the host `executor.map` and encoding options. The maintainer ran independent literal and contract checks before and after: encoding, order and duplicates, input preservation, single consumption, empty input, and original exceptions all passed. The executor's own 5 tests are recorded separately. Format and full-file review are in the [clarity results](../clarity/test-results.md#历史修订2026-10-14-职责边界与精简). No paired old/new or natural-trigger evaluation.

## 2026-10-10 internal stage boundaries (0.10.0)

Tests: 58 → 61. New cases: single-use internal stages of a deep module, a lock-held invariant counterexample, and local tidying that should not trigger architecture review. Independent installation of the two skills and compatibility of their rules were checked separately; an unchanged public API was not taken as proof of internal behavioral equivalence. Checks and the model smoke test are in [that round's validation](../clarity/readability-validation-2026-10-10.md).

## 0.9.1 prompt and answer-format adjustments

The user asked to commit without further skill changes based on that round's answers. Added execution-only answer instructions: judgment questions get a conclusion and key reasons; design questions get the necessary interface, contract, and trade-offs; only prompts that ask for a report or roadmap get one. Grading does not reward length or term coverage.

Prompt fixes:

- Case 2: "one-line bypass" became "temporary patch", so it is not read as a permission bypass.
- Case 8: asks for a short answer.
- Case 14: removed a leftover hint about the debugging surface.
- Case 48: risk and migration analysis only, no implementation without code.
- Case 28: says measurements will come later and only asks how to start.

Grading correction on case 28: the earlier run was failed for not meeting full-solution evidence standards on a prompt that gave no profile data. That penalty was withdrawn; the case tests the authorization switch, and cases 54/55 test solution choice with cost data. Only format, diff, and link checks were run; the 0.9.0 results below do not validate these prompt changes.

## 0.9.0 test-intent revision and partial Luna rerun (stopped)

Baseline `459cfe7`. After reviewing all 56 cases, the user confirmed four rules:

- Simple programs do not need a debugging surface; for complex systems, ask the user.
- Reference reading is judged by relevance and cost.
- A consultation does not authorize implementation.
- Infer constraints from goals and motives, and confirm only critical gaps that cannot be inferred.

Expected behavior was revised for cases 2/3/8/12/14/22/30/38/39, and cases 57 (simple program, no debugging surface) and 58 (infer a local copy from an offline goal) were added, for 58 in total. Executor and grader roles were separated.

The author ran all 58 cases in isolated contexts, at most 6 in parallel. This scope made the run unnecessarily slow, and it was stopped at the user's request: cases 1–48 completed, 49–54 were aborted, and 55–58 never started. There is no full-pass result.

Observed problems:

- Case 14 read the new ask-the-user rule but still did not ask about a debugging surface; the prompt had a distractor, fixed in 0.9.1.
- Case 27 correctly computed 33.4% remaining time but wrote a 2.2× speedup instead of about 3×.
- Case 42 ran 272 characters against a 200-character limit.

Cases 11/12/40 made the requested fixture changes, and the existing checks passed.

## 2026-09 Luna review of the compression (0.8.0, baseline 0037221, delivered at 459cfe7)

Runtime: compressed `SKILL.md` and all seven references by removing duplicated definitions, teaching steps, and duplicate routing, while keeping conditions, counterexamples, permissions, and personal choices. Runtime Markdown shrank about 33.5% by character count.

Tests: 53 → 56. Cases 26/28 had their expected behavior revised, and cases 54–56 were added as performance-evidence cases.

Luna (`gpt-5.6-luna:high`) ran blind on the frozen skill:

- Triggering: 18/18 trigger cases matched (12 positive, 6 negative).
- Boundary cases: 35 answered in batches; 31 were unflagged and 4 went to review. Because grading was later corrected, the 49/53 is not a stable success rate.
- Static review: two points accepted (restore stable, distinguishable error results; check that callers depend on fewer internal conventions after evolution). Two rejected, because existing rules already covered them.

User correction to grading (case 26): an architecture audit of a high-performance library should examine performance-relevant structure and may recommend measurements, baselines, and optimizations. Failing answers for proposing baselines was the evaluator's error, so the "no baseline-building recommendations" restriction added for it was withdrawn. What still counts is accurate evidence strength and not treating a recommendation as authorization to implement. Separate real issues were kept on record:

- A possible shared protocol was stated as confirmed (case 26).
- A "confirmed fine-grained boundary call" was not in the material (case 28).

Final targeted reruns, each in a fresh context, all passed under the corrected criteria:

- Case 26 audited with baselines and did not claim unmeasured regressions.
- Case 39 respected "no performance plan".
- Case 54 chose batching from the boundary-cost data.
- Case 55 chose consolidating copy responsibility once copying dominated.
- Case 56 refused to name a root cause from a total timing alone.

Not run: a full 56-case regression on the final version. No end-to-end business-system tests.

## 2026-09-08 research addendum (0.7.0, baseline 35f754a)

Runtime: practices from the [research report](../../docs/software-design-philosophy/research-2026-09-08.md) were folded into the entry and the module, interface, evolution, and audit references. The seven references were kept, with no AI-specific routing.

Tests: 46 → 53.

Verified: an independent evaluator got only the skill and three raw scenarios, read four relevant references, and did not load every file:

- Reservation and release built in separate worktrees, verified only with dicts and mocks: it flagged the composition gap and suggested idempotency and recovery checks on a real test database, without forcing whole-batch atomicity.
- A sort-order change that a consumer depends on, where the user wants a direct switch: it moved the consumer to an explicit fact and added no compatibility path.
- Stale PASS results and side effects still in flight after a mid-run requirement change: it re-evaluated them proportionately.

Final wording about checkable small examples and starting scenarios was checked textually only. `skills@1.5.24` local copy install produced 9 files, identical byte for byte to the skill, with no research or test material. Not measured: success rate, latency, token use, or cost versus the old version.

## 2026-09-08 refactor (0.6.0, baseline 1f3d992)

Runtime: `SKILL.md` went from 165 to 40 lines, and references from 20 to 7, cutting runtime text by about 89% in bytes. Several mandatory processes were removed:

- Full loading of 11 methods and four pattern families.
- Fixed multi-table outputs and completion criteria.
- Proactive questions about debugging surfaces.
- A forced second design candidate and repeated reader passes.
- A custom A0–A2/P0–P2 grading scheme.
- A glossary and pattern encyclopedias.

The 11 methods were merged by task into the current references. The audit reference keeps its own discovery criteria; the other references are read on demand. The description was narrowed and explicit user tasks take precedence. The test set was rewritten around behavioral outcomes (46 cases), dropping expectations that rewarded the removed processes.

Verified: `quick_validate.py`, links, YAML, and JSON. An independent agent with only the skill, raw tasks, and isolated fixtures completed three tasks without extra clarification or loading every reference: a record-library audit, an editor primitive design, and a resumable file-conversion job. This does not show all 46 cases pass or prove equivalence with the old version. No evaluation harness or CI was added.

Installation boundary: the [skills installer](https://github.com/vercel-labs/skills/blob/main/src/installer.ts) copies the skill directory recursively, and an installed copy did contain the test files. Tests therefore live in `tests/software-design-philosophy/` and sources in `docs/software-design-philosophy/`, outside the installable directory. A `skills@1.5.24` isolated install produced only the 9 runtime files.
