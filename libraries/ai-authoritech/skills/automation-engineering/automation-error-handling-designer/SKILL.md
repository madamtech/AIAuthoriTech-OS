---
name: automation-error-handling-designer
description: Design failure classification, detection, bounded retries, backoff, timeouts, circuit breaking, compensation, dead-letter handling, replay, reconciliation, escalation, user communication, and incident recovery for automations. Use to make workflow failures safe, observable, and recoverable. Do not use generic retry-all behavior or conceal partial completion. Use when asked to (1) design automation error handling, (2) revise automation error handling, (3) compare options for automation error handling, or (4) document specifications for automation error handling.
---

# Automation Error Handling Designer

Use the [error handling standard](references/error-handling-standard.md) and record the design in the [failure handling plan template](assets/failure-handling-plan-template.md).

## Procedure

1. Inventory steps, side effects, dependencies, state, criticality, recovery objectives, owners, and user impact.
2. Classify validation, authorization, conflict, duplicate, timeout, rate-limit, dependency, partial, and terminal failures.
3. Define detection, error codes, safe context, correlation, severity, retryability, and authoritative status.
4. Set bounded retries with backoff, jitter, budgets, idempotency, and circuit breakers where appropriate.
5. Design compensation, checkpoints, dead letters, replay, reconciliation, quarantine, and manual correction.
6. Prevent sensitive data leakage in errors, logs, notifications, tickets, and dashboards.
7. Define escalation, user messages, ownership, service levels, incident response, and post-incident learning.
8. Test injected failures, recovery, duplicate effects, lost acknowledgments, stale state, and rollback.
9. Deliver failure matrix, state transitions, policies, runbooks, tests, monitoring, and residual risks.

## Guardrails

- Do not report failure as success or discard failed records silently.
- Do not retry authentication, validation, or permanent errors without a changed condition.
- Do not compensate unless the reversal is authorized and independently verifiable.
- Do not allow replay to duplicate irreversible side effects.

## Recovery

If authoritative state, side effects, retry safety, or compensation cannot be verified, stop automated recovery and quarantine the affected execution. Preserve correlation and sanitized evidence, reconcile against systems of record, and require an authorized owner to select correction, compensation, or closure.

## Output Contract

Deliver a failure matrix, state transitions, detection and retry policies, compensation and reconciliation, escalation, user communication, runbooks, tests, monitoring, owners, residual risks, and approval status.
