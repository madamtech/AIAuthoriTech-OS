---
name: workflow-automation-designer
description: Translate a validated automation blueprint into an executable platform-neutral workflow design with triggers, nodes, state, branches, loops, approvals, integrations, retries, compensation, observability, tests, deployment, and support. Use before implementation in n8n or another orchestrator. Do not redesign the business process silently or bypass human authority.
---

# Workflow Automation Designer

Use the [workflow automation design standard](references/workflow-automation-design-standard.md) to translate the approved blueprint without changing business authority. Record nodes, state, failure behavior, and operations in the [workflow automation specification template](assets/workflow-automation-specification-template.md).

## Procedure

1. Confirm blueprint, architecture, interfaces, business rules, approvals, controls, and acceptance tests.
2. Define typed trigger, correlation ID, state model, inputs, outputs, completion, cancellation, and time limits.
3. Map nodes, decisions, branches, parallel work, joins, loops, waits, handoffs, and human tasks.
4. Specify credentials, least privilege, data minimization, field mappings, transformations, and validation.
5. Design idempotency, locking, retries, backoff, dead letters, compensation, replay, and reconciliation.
6. Add logs, metrics, traces, audit events, alerts, dashboards, runbooks, and manual recovery.
7. Test normal, boundary, duplicate, concurrent, partial, timeout, unauthorized, dependency, and rollback cases.
8. Deliver workflow specification, contracts, diagrams, test suite, deployment, operations, risks, and open decisions.

## Guardrails

- Do not put secrets in workflow definitions or examples.
- Do not retry non-idempotent side effects blindly.
- Do not declare success before authoritative verification of required effects.
- Do not allow branches to terminate without explicit completion or failure state.

## Recovery

If a branch, side effect, state transition, approval, or authoritative completion check is undefined, mark the workflow non-executable and stop implementation. Preserve the approved blueprint, isolate the unresolved path, and require owner-approved rules plus passing failure and recovery tests before release.

## Output Contract

Deliver a completed workflow specification containing typed triggers, state model, node map, branches, loops, approvals, integrations, mappings, concurrency, idempotency, failures, compensation, reconciliation, observability, tests, deployment, rollback, operations, risks, and open decisions.
