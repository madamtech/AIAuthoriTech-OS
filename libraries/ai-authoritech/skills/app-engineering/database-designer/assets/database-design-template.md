# Database Design

## Design control

- Product and release:
- Requirement IDs:
- Data, security, and technical owners:
- Workload and growth assumptions:
- Recovery objectives:

## Conceptual model

Describe authoritative domains, entities, events, derived data, external systems,
tenancy, and major lifecycle relationships.

## Entity dictionary

| Entity | Meaning | Owner | Source of truth | Primary key | Tenant | Lifecycle |
|---|---|---|---|---|---|---|

## Fields and constraints

| Entity.field | Type | Required | Default | Validation | Unique or reference | Sensitivity |
|---|---|---|---|---|---|---|

## Relationships

| Parent | Child | Cardinality | Optional | Delete behavior | Constraint |
|---|---|---|---|---|---|

## Authorization and tenancy

| Actor or role | Resource | Read | Create | Update | Delete | Condition |
|---|---|---|---|---|---|---|

## Query and index plan

| Query or workload | Filters and ordering | Volume | Target | Index or strategy | Tradeoff |
|---|---|---:|---:|---|---|

## Transactions and concurrency

| Operation | Atomic boundary | Concurrency | Idempotency | External effect | Recovery |
|---|---|---|---|---|---|

## Audit and data lifecycle

| Data class | Audit | Retention | Archive | Export | Deletion propagation | Owner |
|---|---|---|---|---|---|---|

## Migration and recovery

| Phase | Change | Compatibility | Backfill or validation | Rollback or forward-fix | Owner |
|---|---|---|---|---|---|

Document backups, restore test, cutover, environment isolation, seed data, and
reconciliation.

## Verification

| Test | Requirement or risk | Data set | Expected | Evidence |
|---|---|---|---|---|

## Provider adapter, risks, and decisions

List provider-specific schema, policy, migration, observability, and tuning work
separately from the logical model, with assumptions and open decisions.
