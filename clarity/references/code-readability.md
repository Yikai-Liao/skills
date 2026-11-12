# Code Expression

New and rewritten code both express the requirement and its effective contract through the main flow, names, and local organization. Behavior-preserving refactors keep the agreed behavior; feature changes and breaking iterations follow the target requirement.

## Main flow and local detail

Let the reader see operation phases, state changes, and external effects, and keep low-level detail local. Read together with its definition, type, and call context, a name states the object, granularity, unit, and tense accurately; when a responsibility changes, recheck the old name. Clear idiomatic names in short scopes can stay.

When the success path is buried in nested branches, phases interleave, or temporary state must be tracked across a long distance, pick early returns, local variables, or phase extraction to fit the specific obstacle. Preserve branch priority, short-circuiting, and cleanup relations.

**A complete phase can be extracted even if it is called once.** Its input, output, and effect boundaries must be clear, and the call site must read as the main flow from the name and contract. Keep related helpers nearby. If extraction adds much shared mutable state, a catch-all context, mode switches, or scattered invariants, choose another boundary so each phase owns a recognizable, complete responsibility.

A short function that expresses a stable concept, isolates a constraint, or hides an implementation choice can stay. Inline a helper that only renames, fetches, or forwards, adding a jump without reducing understanding; to name a single computation step, use a local variable. Decide by concept and reading cost, and keep meaningful intermediate values after inlining. A complete predicate, lookup, or idiom can stay compact.

Function length and indentation depth are only signals. Rule tables, coherent algorithms, and state transitions that must be audited together can stay whole. When renaming, check the contracts of public parameters, protocol keys, reflection, and dynamic references.

After the change, read the affected functions, helpers, and call sites together for one maintenance task, such as finding the first write or changing a failure condition. If the main path, state changes, and failure exits still have to be assembled layer by layer, adjust the local organization.

## Behavior boundaries when rewriting

Trace the relations the current reading problem depends on. Preserve effective evaluation count and order, short-circuiting, side effects, synchronous and asynchronous exceptions, numeric and Unicode semantics, resource cleanup, and lock scope. For example, an async wrapper may turn a synchronous throw into a Promise rejection; removing it changes the contract.

Make the relation between a current value, a snapshot, and an update clear. Keep or remove state, caches, and synchronization according to their design role; local tidying targets a specific reading problem.

When tidying tests, keep each test's regression purpose and the necessary coverage. Scaffolding that only re-verifies a dependency library, without checking this project's contract, can go.

## Comments and documentation tools

Next to non-obvious code, state why it holds and under what conditions, such as for fallbacks, sentinels, rollbacks, or skips. A bug fix keeps the trigger, the old problem, and what prevents regression; a performance trade-off states the work saved, where it applies, and its cost. If the reason is unclear, check the implementation, tests, or history, and write only facts that can be confirmed.

Keep history that carries technical information; delete chat logs and self-assessment. A long report can be linked, but the key reason that prevents a mistaken edit stays beside the code. Performance numbers come with their measurement conditions; when behavior changes, update the explanation.

API doc comments describe behavior and failure semantics, placed where documentation tools or `help()` can read them. Write private comments as actually needed.

## Error and diagnostic messages

Separate the operation outcome, known causes, candidate causes, and unknowns. A timeout means waiting stopped; describe the operation's final state only as far as it is actually guaranteed.

Keep the needed location, identifiers, and conditions. Human-facing wording can change; error codes, exception types, exit statuses, output channels, fields, and message text that machines depend on follow their compatibility agreements.
