---
name: learning-integration-monitor
description: Monitor LMS integrations for availability, freshness, completeness, duplicates, ordering, mapping failures, retries, reconciliation, and business impact. Use for HR, CRM, SSO, content, reporting, or certification data flows after deployment.
---

# Learning Integration Monitor

Convert technical signals into prioritized operational incidents and preventive controls.

## Workflow

1. Define each flow's owner, source, target, schedule, expected volumes, service levels, critical fields, and downstream commitments.
2. Collect run status, timestamps, counts, latency, rejected records, retries, dead letters, alerts, and reconciliation results.
3. Compare actual behavior to baselines and distinguish no-data, delayed-data, partial failure, duplicate processing, and mapping defects.
4. Trace affected users, assignments, completions, credentials, reports, and communications.
5. Classify severity, contain impact, preserve evidence, route ownership, and define safe replay or correction.
6. Verify recovery through reconciliation and track recurring causes and control improvements.

## Output

Provide an integration health summary, flow inventory, exception register, business impact, incident timeline, remediation, reconciliation evidence, and prevention actions.

## Guardrails

- Do not replay transactions without idempotency and impact checks.
- Protect credentials and personal data.
- Never mark recovery complete from a green job status alone.
- Separate source defects from transport and target defects.

