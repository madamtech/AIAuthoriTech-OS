---
name: learning-integration-monitor
description: Monitor LMS integrations for availability, freshness, completeness, duplicates, ordering, mapping failures, retries, reconciliation, and business impact. Use for HR, CRM, SSO, content, reporting, or certification data flows after deployment.
---

# Learning Integration Monitor

Use the [operating standard](references/integration-monitoring-standard.md) and [working template](assets/integration-monitor-template.md).

Convert technical signals into prioritized operational incidents and preventive controls.

## Procedure

1. Define each flow's owner, source, target, schedule, expected volumes, service levels, critical fields, and downstream commitments.
2. Collect run status, timestamps, counts, latency, rejected records, retries, dead letters, alerts, and reconciliation results.
3. Compare actual behavior to baselines and distinguish no-data, delayed-data, partial failure, duplicate processing, and mapping defects.
4. Trace affected users, assignments, completions, credentials, reports, and communications.
5. Classify severity, contain impact, preserve evidence, route ownership, and define safe replay or correction.
6. Verify recovery through reconciliation and track recurring causes and control improvements.

## Output Contract

Provide an integration health summary, flow inventory, exception register, business impact, incident timeline, remediation, reconciliation evidence, and prevention actions.

## Guardrails

- Do not replay transactions without idempotency and impact checks.
- Protect credentials and personal data.
- Never mark recovery complete from a green job status alone.
- Separate source defects from transport and target defects.

## Recovery

If service expectations, source and target ownership, identity keys, event counts, latency, retries, reconciliation, alert threshold, or replay authority is unresolved, preserve failed payload evidence and prevent unsafe replay. Escalate by fault domain.
