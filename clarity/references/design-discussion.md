# Design Discussion and Records

For expressing design trade-offs, recording decisions, and handing off. For structural explanations, choose a [view](software-documentation.md#choosing-a-view-by-question) by question and reuse existing content.

## Recording and discussing

When a design is under ongoing review, handed to implementation, or continued across sessions, write it back promptly into the existing architecture notes, RFC, ADR, or plan, separating current state, proposals, and decisions in force. Keep grounded reasons, costs, scope, conditions, and sources; sections in one document are fine.

Explain changes from the current scenario. For important choices, give the recommendation, viable alternatives, and costs. When the user says they cannot follow, first explain the relevant relations.

## Inheriting decisions

When continuing a discussion, foreground new facts and their local impact; carry over decisions in force with their important reasons. When a contract or assumption changes, re-examine the affected parts. Whether to revisit depends on semantic impact, not on commit count or file conflicts.

A partial decision keeps its scope. "Proceed once the condition is met" and "a person decides after the result is in" are recorded as different decisions and followed as such when continuing.

## Implementation feedback and handoff

A handoff keeps the version, original goal, decisions in force, progress, and blockers, and states the next step's capabilities, dependencies, and completion criteria, with transition and rollback when needed.

When implementation and design disagree, distinguish: implementation freedom within the agreement stays; an outdated description gets the document updated; a violation gets the implementation fixed or a design revision proposed. When new facts undermine a decision's basis, return to the trade-off discussion; do not edit the document to hide an actual violation.

Update the current state as work lands, including default behavior and transitional states, and use evidence to separate implemented, verified, and released. When continuing, scaling back, or ending, record the completed scope and where open, deferred, or cancelled items went.
