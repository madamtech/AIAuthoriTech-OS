# Integration Planning Standard

## Contract first

Define the business event, permitted data use, systems, accountable owners, source of truth, identifiers, direction, frequency, service levels, and supported interface before designing transport. Use documented APIs, events, files, database access, or approved connectors. Record limitations and never invent undocumented behavior.

## Required controls

- Version contracts, mappings, transformations, validation, pagination, rate limits, and compatibility.
- Apply scoped authentication, authorization, tenant isolation, encryption, secret rotation, and audit evidence.
- Define ordering, deduplication, idempotency, retries, dead letters, replay, compensation, and manual correction.
- Reconcile source and target with explicit ownership and measurable discrepancy thresholds.
- Test duplicates, out-of-order messages, partial failures, malformed data, unauthorized requests, throttling, outages, and rollback.

Quarantine uncertain records instead of propagating ambiguity. Exactly-once behavior requires enforceable end-to-end proof.
