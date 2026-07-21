# Database Design Standard

## Entity contract

For each entity define:

- Business meaning, owner, source of truth, and requirement IDs
- Primary key and external identifiers
- Fields, types, nullability, defaults, validation, and sensitivity
- Natural uniqueness and invariant constraints
- Relationships, cardinality, optionality, and delete behavior
- Tenant and resource ownership
- Created, effective, updated, archived, and deleted times
- Audit, retention, correction, export, and deletion behavior

## Authorization model

Test permissions as actor-resource-action-condition decisions. Include owner,
member, invited user, administrator, support, service identity, background job,
anonymous user, suspended user, and cross-tenant attempts as applicable.

Use deny by default. Derive tenant and user identity from trusted authentication
context, not request-supplied fields.

## Query and index contract

For every critical access pattern record filters, joins, ordering, expected rows,
frequency, latency target, pagination, consistency, and candidate index. Validate
with representative data and query plans. Review unused, overlapping, and
write-expensive indexes.

## Transaction and integration contract

Define atomic boundaries and what can fail independently. Use idempotency keys for
repeatable requests, explicit concurrency controls for contested updates, and an
outbox or equivalent reliable publication pattern when database state and external
events must remain consistent.

## Migration safety

Prefer expand-migrate-contract:

1. Add backward-compatible structure.
2. Deploy compatible readers and writers.
3. Backfill in bounded batches with validation.
4. Switch traffic or reads with observability.
5. Remove old structure only after the compatibility window.

Record backup, restore test, migration duration, lock risk, rollback or forward-fix,
data reconciliation, and owner. Never assume a down migration can restore deleted
or transformed data.

## Required tests

Test referential and business constraints, authorization and tenant isolation,
concurrent writes, duplicate requests, transactions, backfills, version
compatibility, deletion and retention, backup restoration, high-cardinality and
large-result queries, pagination stability, failure recovery, and audit evidence.
