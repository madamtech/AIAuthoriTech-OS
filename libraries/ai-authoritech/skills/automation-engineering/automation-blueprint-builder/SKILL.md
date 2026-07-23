---
name: automation-blueprint-builder
description: Convert an approved current-state workflow and automation opportunity into an implementation-ready blueprint covering scope, triggers, steps, decisions, data, systems, controls, exceptions, human approvals, testing, operations, and acceptance. Use after workflow discovery and prioritization, before platform-specific implementation. Do not automate an unvalidated process or authorize external actions.
---

# Automation Blueprint Builder

Use the [automation blueprint standard](references/automation-blueprint-standard.md) to convert an approved opportunity into a governed implementation contract. Record the design in the [automation blueprint template](assets/automation-blueprint-template.md).

## Procedure

1. Confirm validated current state, target outcome, owners, users, volumes, service levels, risk, and boundaries.
2. Define trigger, inputs, outputs, completion, non-goals, systems, data classes, and source-of-truth rules.
3. Map deterministic steps, decisions, branches, approvals, handoffs, exceptions, and human judgment.
4. Specify integrations, field mappings, identities, permissions, idempotency, state, and audit events.
5. Define retries, compensation, reconciliation, timeouts, cancellation, escalation, and manual recovery.
6. Separate business rules from platform implementation and preserve an executable acceptance contract.
7. Design tests for normal, duplicate, missing, conflicting, unauthorized, failure, recovery, and rollback cases.
8. Estimate dependencies, implementation phases, ownership, monitoring, support, and change management.
9. Deliver the blueprint, diagrams, contracts, control matrix, tests, rollout, rollback, assumptions, and decisions.

## Guardrails

- Do not automate unstable, unlawful, unsafe, or undefined decisions.
- Do not embed secrets or use service accounts with broader access than required.
- Do not claim implementation or integration success from a design artifact.
- Do not remove required human approval merely to increase straight-through processing.

## Recovery

If the workflow, decision authority, external effects, data ownership, or exception paths remain unresolved, mark the blueprint provisional and block implementation or deployment. Preserve the validated current state and route each open decision to a named owner before revising the acceptance contract.

## Output Contract

Deliver a completed automation blueprint containing scope, trigger, state model, process flow, decisions, integrations, field mappings, controls, human approvals, exceptions, recovery, test cases, monitoring, rollout, rollback, assumptions, owners, and acceptance status. Separate verified requirements from proposals.
