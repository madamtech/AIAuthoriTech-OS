# API Integration Standard

## Contract

For each operation or event define:

- Stable name, version, owner, purpose, and direction
- Endpoint, method, topic, schedule, or file boundary
- Authentication, token audience, authorization, tenant, and delegation
- Request or event schema, validation, limits, and examples
- Response, acknowledgment, receipt, and error schema
- Side effects and authoritative completion verification
- Idempotency, ordering, concurrency, pagination, and replay
- Timeout, retry, quota, rate, and spend controls
- Compatibility, deprecation, monitoring, support, and retirement

## Delivery semantics

Assume at-least-once delivery unless a provider contract and end-to-end evidence
prove otherwise. Design consumers to handle duplicates. Record event and
idempotency identities independently from business identifiers.

For unknown write outcomes, reconcile before retrying. Preserve ordered processing
only where the business rule requires it; otherwise avoid unnecessary global
serialization.

## Webhook controls

Verify signature over the raw body, expected algorithm and secret, timestamp
tolerance, event identity, destination, and environment. Acknowledge according to
provider timing, persist durable work before returning success, and process
asynchronously when appropriate.

## Reconciliation

Define:

- Authoritative comparison source
- Frequency and freshness objective
- Selection window and pagination
- Count, checksum, field, or state comparisons
- Missing, extra, duplicate, stale, and conflicting records
- Automated repair boundaries
- Exception queue, manual owner, evidence, and closure

## Required tests

Test schema evolution, invalid and extreme values, authentication and scope,
cross-tenant attempts, field transformations, time zones, pagination, duplicate,
late and reordered events, signature failure, replay, provider throttling, timeout
after effect, partial response, outage, dead-letter recovery, reconciliation,
backfill, version compatibility, and credential rotation.
