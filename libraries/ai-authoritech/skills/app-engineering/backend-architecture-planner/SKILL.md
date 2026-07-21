---
name: backend-architecture-planner
description: Convert approved product requirements, business rules, data models, access policies, integrations, workloads, and service objectives into a provider-neutral backend architecture covering domain and service boundaries, APIs, events, jobs, data authority, transactions, identity, authorization, idempotency, consistency, resilience, scaling, security, privacy, observability, testing, deployment, migration, cost, and operations. Use before implementing or redesigning application backends, APIs, services, workers, or serverless systems—not to invent material requirements, provision production resources, or default to microservices without organizational and workload evidence.
---

# Backend Architecture Planner

Make ownership, authority, and failure behavior explicit before choosing runtime
topology.

1. Confirm requirements, actors, business rules, critical journeys, workloads,
   volumes, growth, latency, consistency, availability, recovery, data classes,
   regions, integrations, budget, team boundaries, and accountable owners.
2. Separate confirmed constraints from assumptions. Stop for decisions affecting
   sensitive data, authorization, irreversible state, external effects,
   contractual promises, or production authority.
3. Map domain capabilities, aggregates, workflows, invariants, commands, queries,
   events, external systems, and sources of truth. Assign business and technical
   ownership to every authoritative state and operation.
4. Choose a modular monolith, services, functions, workers, event-driven topology,
   or hybrid using
   [references/backend-architecture-standard.md](references/backend-architecture-standard.md).
   Record organizational fit, coupling, deployment independence, state,
   consistency, scale, failure isolation, operability, cost, and exit path.
5. Define module or service boundaries by cohesive responsibility and ownership.
   Prevent shared database tables, internal model leakage, and synchronous call
   chains from silently defeating the boundary.
6. Define contracts for commands, queries, APIs, events, webhooks, files, and jobs:
   schemas, versions, identity, authorization, validation, effects, errors,
   pagination, idempotency, timeouts, limits, compatibility, and ownership.
7. Define data placement, keys, constraints, tenancy, encryption, lifecycle,
   transactions, isolation, concurrency, read models, caches, search, analytics,
   audit, retention, deletion, backups, restore, migration, and reconciliation.
8. Authenticate each human, workload, service, job, and integration identity.
   Authorize actor, tenant, resource, action, and condition in trusted services and
   the data layer using deny by default and least privilege.
9. Design synchronous paths for bounded immediate outcomes and asynchronous paths
   for decoupled or long-running work. Define message identity, ordering,
   deduplication, idempotency, retries, backoff, dead letters, compensation,
   checkpoints, cancellation, and operator recovery.
10. Define consistency and completion semantics. Distinguish accepted, queued,
    processed, externally completed, reconciled, and failed states. Never equate a
    transport acknowledgment with the business outcome.
11. Model dependency failures, timeouts after effects, partial success, overload,
    hot keys, noisy tenants, queue growth, stale caches, regional loss, provider
    outage, corrupted data, and unavailable operators. Define containment,
    backpressure, circuit breaking, load shedding, degradation, and recovery.
12. Establish capacity and performance budgets for critical paths, concurrency,
    throughput, payloads, connections, database work, queues, storage, third-party
    quotas, and cost drivers. Scale measured bottlenecks, not hypothetical ones.
13. Define secrets, keys, certificates, network boundaries, input and output
    handling, software provenance, dependency policy, vulnerability response,
    privacy controls, audit evidence, abuse prevention, and incident actions.
14. Define logs, metrics, traces, correlation, audit events, business outcomes,
    SLOs, error budgets, dashboards, alerts, diagnostics, retention, redaction,
    support ownership, and runbooks for every critical workflow.
15. Define contract, unit, component, integration, migration, concurrency,
    authorization, resilience, load, recovery, and end-to-end tests using
    synthetic or approved de-identified data and controlled external effects.
16. Plan repositories, build provenance, environments, configuration, feature
    flags, schema and contract compatibility, staged rollout, observation,
    rollback or forward-fix, reconciliation, incident response, and retirement.
17. Keep provider-specific services behind adapters where portability has value.
    Record lock-in, operational benefits, cost, export, substitute, and exit path.
18. Deliver with
    [assets/backend-architecture-template.md](assets/backend-architecture-template.md).

## Rules

- Do not choose microservices merely for scale, fashion, or future possibility.
- Do not split a boundary without an owner, contract, failure model, deployment
  reason, and operational capacity.
- Do not share writable authoritative state across services without explicit
  transaction, ownership, and recovery semantics.
- Do not trust client-supplied user, tenant, role, ownership, or price context.
- Do not retry non-idempotent work when duplicate effects cannot be prevented,
  detected, reconciled, or compensated.
- Do not put secrets or sensitive payloads in source code, URLs, logs, events,
  fixtures, prompts, or architecture documents.
- Do not claim completion from HTTP success, message acknowledgment, or job exit
  status without authoritative business-state verification.
- Do not optimize availability, performance, or cost by weakening correctness,
  security, privacy, recovery, or required auditability.

## Handoff

Provide the scope and assumptions, domain and ownership map, topology decision,
module and service boundaries, contracts, data and consistency model, identity and
authorization, asynchronous workflow design, failure and resilience model,
capacity and cost budgets, security and privacy controls, observability and SLOs,
test strategy, deployment and evolution plan, provider adapters, risks, and open
decisions.
