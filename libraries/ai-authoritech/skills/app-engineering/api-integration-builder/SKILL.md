---
name: api-integration-builder
description: Design secure, reliable application-to-application integrations with explicit source-of-truth ownership, API and event contracts, authentication, authorization, field mapping, validation, idempotency, pagination, webhooks, ordering, rate limits, retries, partial success, reconciliation, observability, testing, versioning, migration, and recovery. Use for REST, GraphQL, webhooks, event streams, SaaS connectors, internal APIs, and data synchronization - not undocumented screen scraping, credential provisioning, production execution, or assuming third-party behavior without current documentation and tests.
---

# API Integration Builder

Design for duplicate, delayed, missing, reordered, and partially successful work.

## Procedure

1. Confirm the business outcome, systems, owners, environments, data classes,
   volumes, latency, consistency, recovery, audit, and support requirements.
2. Define the system of record and allowed writers for every shared entity and
   field. Specify conflict authority and synchronization direction.
3. Choose request-response, scheduled pull, webhook, event stream, batch file, or
   hybrid patterns based on timeliness, volume, ordering, provider capability,
   coupling, and recovery needs.
4. Define operations and messages with
   [references/api-integration-standard.md](references/api-integration-standard.md):
   purpose, endpoint or topic, version, schema, identity, authorization, effects,
   limits, errors, and owner.
5. Define field mapping, types, identifiers, enumerations, time zones, units,
   normalization, defaults, nulls, validation, transformation, and rejected-record
   handling. Preserve source identifiers and provenance.
6. Define service authentication, token audience and scope, tenant and user
   delegation, secret storage, rotation, revocation, network controls, and
   environment isolation.
7. Define idempotency keys, deduplication, concurrency, ordering, replay,
   pagination, checkpoints, cursors, watermarking, and late or stale data behavior.
8. Verify webhook signatures, timestamp tolerance, replay protection, event IDs,
   subscription lifecycle, acknowledgments, retry behavior, and recovery polling.
9. Define timeouts, transient and permanent errors, bounded backoff, provider rate
   guidance, quotas, circuit breaking, dead-letter handling, partial success,
   compensation, and manual escalation.
10. Reconcile intended and actual state using authoritative reads, receipts,
    counts, checksums, exception queues, and scheduled repair. Never equate an
    accepted request with completed synchronization.
11. Define correlation IDs, sanitized logs, metrics, traces, alerts, dashboards,
    audit events, freshness and backlog objectives, incident response, and owner.
12. Test schemas, authentication, authorization, mappings, invalid data,
    pagination, duplicate and reordered events, timeouts after effects, rate
    limits, provider outages, partial success, replay, reconciliation, version
    compatibility, and recovery using sandbox or controlled fixtures.
13. Plan versioning, contract testing, deprecation, migration, backfill, cutover,
    rollback or forward-fix, credential rotation, support, and retirement.
14. Deliver with [assets/api-integration-design-template.md](assets/api-integration-design-template.md).

## Guardrails

- Do not integrate a field without an agreed source of truth and conflict rule.
- Do not place secrets or sensitive payloads in URLs, prompts, logs, fixtures, or
  documentation.
- Do not retry non-idempotent writes without deduplication or compensation.
- Do not trust webhook origin without cryptographic verification when supported.
- Do not fetch an unbounded collection without pagination and checkpoint behavior.
- Do not silently discard invalid, unauthorized, duplicate, or unmapped records.
- Do not claim synchronization until authoritative state is reconciled.
- Keep provider-specific endpoints and credentials in adapters.

## Output Contract

Provide the context and ownership map, integration pattern, contracts and schemas,
mapping rules, identity and security model, delivery and idempotency semantics,
failure and reconciliation design, observability, test plan, lifecycle and
migration plan, provider adapters, risks, and open decisions.

## Recovery

If source-of-truth ownership or mapping is disputed, hold affected synchronization
and route the conflict to its owner. If an effect times out or partially succeeds,
reconcile authoritative state before retrying. Quarantine invalid or unmapped data
with provenance instead of silently discarding or coercing it.
