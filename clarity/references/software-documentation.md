# Software Documentation

Reuse the project's layout. Separate **current behavior, approved goals, proposals under review, and unknowns**, and mark versions and differences between implementation and spec.

- A README separates user and contributor paths and organizes alternative installation methods as options; state preconditions such as demo/production isolation and permissions separately.
- Before an operation, state nearby the permissions, write-back or destructive effects, and backup and rollback requirements. Security reports use the project's private channel.
- APIs and specs keep failures, side effects, units, and strength of guarantees. Standalone references and source docstrings each live where their readers and tools find them.
- Plans keep dependencies, verification, rollback, and release requirements, plus actual progress, open items, and findings from execution.

## Choosing a view by question

For system boundaries, applications and storage, components, and deployment, prefer the matching C4 view and do not mix levels:

- **System context (C1)** places the system, its users, and the external systems it interacts with directly.
- **Container (C2)** opens up the applications and data stores inside the system. A logical container is not a Docker container, Pod, or deployment replica.
- **Component (C3) and code (C4)** drill down as far as explaining internal responsibilities or the implementation requires.
- **Dynamic views** explain the order of collaboration, kept distinct from static dependencies.
- **Deployment views** map to real environments, instances, and infrastructure. Replica counts, isolation, and failure guarantees come from actual deployment material.

A local algorithm can be explained with short prose, a data flow, or a state table covering phases, data lifecycle, and invariants; local discussion reuses the higher-level explanation that exists.

Objects and names correspond across views, with clear responsibilities and relations. When updating a contract description, check related examples and old terms. Pair diagrams with the reasons for the choice and its costs; for decision records see [design discussion](design-discussion.md).

For source naming, comments, and individual error messages, see [code expression](code-readability.md).
