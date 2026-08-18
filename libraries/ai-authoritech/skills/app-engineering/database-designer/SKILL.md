---
name: database-designer
description: Convert approved application requirements into a secure, governed, migration-ready database design covering entities, relationships, keys, constraints, tenancy, row-level authorization, transactions, concurrency, indexes, query patterns, audit history, retention, deletion, migrations, backups, recovery, performance, observability, testing, and provider-neutral implementation contracts. Use for new application schemas, SaaS multitenancy, database redesigns, migration planning, or AI-generated app backends - not executing production migrations, replacing data governance, or selecting a database without workload evidence. Use when asked to (1) design database, (2) revise database, (3) compare options for database, or (4) document specifications for database.
---

# Database Designer

Model business truth and authorization before optimizing storage.

## Procedure

1. Confirm requirement IDs, business rules, users and roles, source systems,
   workloads, data volume and growth, sensitivity, tenancy, retention, recovery,
   latency, reporting, search, and integration needs.
2. Identify each entity, aggregate, event, reference value, file, derived value,
   and external identifier. Assign a source of truth and accountable owner.
3. Define stable primary keys, natural uniqueness, foreign keys, cardinality,
   optionality, lifecycle, effective dates, and deletion behavior using
   [references/database-design-standard.md](references/database-design-standard.md).
4. Normalize transactional facts until every remaining duplication has a justified
   consistency or performance purpose. Separate authoritative facts from caches,
   projections, analytics, search indexes, and model-derived content.
5. Encode invariant business rules with types, nullability, defaults, checks,
   uniqueness, references, and transactions. Keep rules that span systems explicit.
6. Define tenant, organization, user, resource, and ownership boundaries. Enforce
   authorization at the database or trusted server layer, including service,
   administrator, anonymous, and background-job access.
7. Define create, read, update, delete, restore, archive, import, export, and audit
   behavior. Specify soft deletion only when recovery or history justifies its
   privacy, uniqueness, and query complexity.
8. Map critical queries, filters, joins, sorts, pagination, reports, and write paths.
   Design indexes from observed access patterns and verify their write and storage
   cost.
9. Define transaction boundaries, isolation, optimistic or pessimistic concurrency,
   idempotency, duplicate suppression, ordering, retries, outbox or inbox patterns,
   and reconciliation for external effects.
10. Define classification, encryption, masking, secrets separation, audit events,
    retention, legal holds, correction, export, deletion propagation, and access
    review.
11. Plan additive migrations, backfills, compatibility windows, validation,
    cutover, rollback or forward-fix, backups, restore testing, recovery objectives,
    seed data, and environment isolation.
12. Test constraints, authorization, tenant isolation, concurrency, idempotency,
    migrations, deletion, recovery, representative queries, worst-case data,
    performance, and observability before production use.
13. Deliver with [assets/database-design-template.md](assets/database-design-template.md).

## Guardrails

- Do not rely on client-side filtering or hidden UI for data authorization.
- Do not use generic JSON storage to avoid modeling stable, queryable business data.
- Do not add indexes without a query and selectivity rationale.
- Do not treat soft deletion as verified erasure.
- Do not apply destructive or irreversible migrations without backups, validation,
  compatibility analysis, and an approved recovery path.
- Do not expose sequential identifiers as authorization controls.
- Do not put secrets in database schemas, fixtures, migrations, or documentation.
- Keep provider-specific SQL, policies, and tuning in adapters.

## Output Contract

Provide the conceptual and logical model, entity dictionary, constraints,
authorization and tenancy matrix, query and index plan, transaction and concurrency
contracts, audit and lifecycle controls, migration and recovery plan, test plan,
provider-adapter requirements, risks, assumptions, and open decisions.

## Recovery

If ownership, tenancy, retention, or authorization is unresolved, block the affected
schema and expose the decision. If a migration validation fails, stop cutover and
use the approved rollback or forward-fix path. Never repair production data through
an unreviewed generated migration.
