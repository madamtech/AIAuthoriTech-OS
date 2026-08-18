---
name: exception-flow-designer
description: Design complete exception paths for business and technical workflows, covering detection, classification, ownership, containment, correction, compensation, escalation, communication, reconciliation, closure, and learning. Use when happy-path maps omit recoverable, disputed, unusual, or failed cases. Do not label foreseeable recurring work as an undocumented exception. Use when asked to (1) design exception flow, (2) revise exception flow, (3) compare options for exception flow, or (4) document specifications for exception flow.
---

# Exception Flow Designer

Use the [exception flow standard](references/exception-flow-standard.md) and record cases in the [exception flow register template](assets/exception-flow-register-template.md).

## Procedure

1. Inventory exceptions from evidence, incidents, staff experience, controls, and boundary analysis.
2. Classify business, data, authorization, dependency, timing, duplicate, dispute, safety, and terminal cases.
3. Define detection, severity, required evidence, owner, queue, service level, and containment.
4. Design correction, retry, compensation, alternate path, approval, appeal, escalation, and closure.
5. Preserve state, correlation, audit, user communication, and authoritative reconciliation.
6. Prevent exception paths from broadening permissions or bypassing mandatory controls.
7. Test recurrence, overload, missing owner, stale case, partial completion, and failed recovery.
8. Deliver exception register, flows, state transitions, responsibilities, tests, metrics, and improvement loop.

## Guardrails
- Do not create an exception queue without ownership and capacity.
- Do not silently discard or indefinitely park unresolved cases.
- Do not retry irreversible actions without idempotency or reconciliation.
- Do not expose sensitive error details to unauthorized users.

## Recovery

If an exception lacks ownership, capacity, authoritative state, safe correction, or closure criteria, contain and quarantine the case rather than retrying or parking it silently. Escalate with preserved evidence and reconcile all partial effects before closure.

## Output Contract

Deliver an exception register, detection and severity, state transitions, owners and queues, service levels, containment, correction, compensation, escalation, communication, reconciliation, closure evidence, tests, metrics, and improvement triggers.
