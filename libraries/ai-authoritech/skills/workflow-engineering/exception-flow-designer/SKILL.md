---
name: exception-flow-designer
description: Design complete exception paths for business and technical workflows, covering detection, classification, ownership, containment, correction, compensation, escalation, communication, reconciliation, closure, and learning. Use when happy-path maps omit recoverable, disputed, unusual, or failed cases. Do not label foreseeable recurring work as an undocumented exception.
---

# Exception Flow Designer

1. Inventory exceptions from evidence, incidents, staff experience, controls, and boundary analysis.
2. Classify business, data, authorization, dependency, timing, duplicate, dispute, safety, and terminal cases.
3. Define detection, severity, required evidence, owner, queue, service level, and containment.
4. Design correction, retry, compensation, alternate path, approval, appeal, escalation, and closure.
5. Preserve state, correlation, audit, user communication, and authoritative reconciliation.
6. Prevent exception paths from broadening permissions or bypassing mandatory controls.
7. Test recurrence, overload, missing owner, stale case, partial completion, and failed recovery.
8. Deliver exception register, flows, state transitions, responsibilities, tests, metrics, and improvement loop.

## Rules
- Do not create an exception queue without ownership and capacity.
- Do not silently discard or indefinitely park unresolved cases.
- Do not retry irreversible actions without idempotency or reconciliation.
- Do not expose sensitive error details to unauthorized users.
