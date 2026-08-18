---
name: integration-planner
description: Plan governed integrations between systems using explicit source ownership, data contracts, identifiers, mappings, transport, authentication, authorization, synchronization, errors, reconciliation, monitoring, and lifecycle controls. Use for API, webhook, event, file, database, and connector integrations. Do not invent undocumented interfaces or authorize data sharing. Use when asked to (1) plan integration, (2) revise integration, (3) evaluate options for integration, or (4) prepare implementation of integration.
---

# Integration Planner

Use the [integration planning standard](references/integration-planning-standard.md) to define supported interfaces, ownership, contracts, and failure controls. Record the result in the [integration plan template](assets/integration-plan-template.md).

## Procedure

1. Define business event, systems, owners, direction, frequency, volumes, service levels, and permitted data use.
2. Establish system of record, identity matching, canonical fields, mappings, transformations, and validation.
3. Select API, webhook, event, file, database, or connector pattern based on supported capabilities and risk.
4. Define authentication, authorization, scopes, secrets rotation, tenant boundaries, encryption, and audit.
5. Specify versioned contracts, ordering, deduplication, idempotency, pagination, rate limits, and compatibility.
6. Design errors, retries, dead letters, compensation, reconciliation, replay, and manual correction.
7. Test normal, duplicate, out-of-order, partial, unauthorized, malformed, rate-limited, and unavailable cases.
8. Deliver interface inventory, mappings, sequence, contracts, controls, tests, monitoring, rollout, and rollback.

## Guardrails

- Do not use screen scraping when an approved stable interface is required without documenting the risk.
- Do not sync more fields, records, or history than the purpose requires.
- Do not assume matching names or emails establish identity safely.
- Do not claim exactly-once delivery without enforceable end-to-end evidence.

## Recovery

If source-of-truth ownership, identity matching, contract compatibility, authorization, or side effects conflict, stop synchronization for affected records. Quarantine uncertain messages, reconcile both systems against an approved source, and avoid retrying until idempotency and correction behavior are verified.

## Output Contract

Deliver a completed integration plan containing business events, systems and owners, source-of-truth rules, identities, field mappings, versioned contracts, transport, security, synchronization, error handling, reconciliation, monitoring, rollout, rollback, tests, assumptions, and approval status.
