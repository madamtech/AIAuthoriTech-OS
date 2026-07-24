# Automation Blueprint Standard

## Entry criteria

Begin only after the current-state workflow, business outcome, opportunity, accountable owner, and automation boundary are validated. Separate deterministic rules from human judgment. Document systems of record, data rights, external effects, approvals, exceptions, and non-goals before choosing implementation details.

## Required design controls

- Define trigger, completion, state, inputs, outputs, decisions, and handoffs.
- Make duplicate handling, idempotency, timeouts, retries, compensation, reconciliation, cancellation, and manual recovery explicit.
- Apply least privilege, data minimization, audit events, and human authorization for consequential actions.
- Create acceptance tests for normal, missing, duplicate, conflicting, unauthorized, partial-failure, recovery, and rollback cases.
- Identify owners for operation, incidents, changes, and risk acceptance.

A blueprint is a design contract, not proof of implementation. Mark unresolved decisions as blockers rather than silently filling them in.
