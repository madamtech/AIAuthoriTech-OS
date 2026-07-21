---
name: integration-planner
description: Plan governed integrations between systems using explicit source ownership, data contracts, identifiers, mappings, transport, authentication, authorization, synchronization, errors, reconciliation, monitoring, and lifecycle controls. Use for API, webhook, event, file, database, and connector integrations. Do not invent undocumented interfaces or authorize data sharing.
---

# Integration Planner

1. Define business event, systems, owners, direction, frequency, volumes, service levels, and permitted data use.
2. Establish system of record, identity matching, canonical fields, mappings, transformations, and validation.
3. Select API, webhook, event, file, database, or connector pattern based on supported capabilities and risk.
4. Define authentication, authorization, scopes, secrets rotation, tenant boundaries, encryption, and audit.
5. Specify versioned contracts, ordering, deduplication, idempotency, pagination, rate limits, and compatibility.
6. Design errors, retries, dead letters, compensation, reconciliation, replay, and manual correction.
7. Test normal, duplicate, out-of-order, partial, unauthorized, malformed, rate-limited, and unavailable cases.
8. Deliver interface inventory, mappings, sequence, contracts, controls, tests, monitoring, rollout, and rollback.

## Rules

- Do not use screen scraping when an approved stable interface is required without documenting the risk.
- Do not sync more fields, records, or history than the purpose requires.
- Do not assume matching names or emails establish identity safely.
- Do not claim exactly-once delivery without enforceable end-to-end evidence.
