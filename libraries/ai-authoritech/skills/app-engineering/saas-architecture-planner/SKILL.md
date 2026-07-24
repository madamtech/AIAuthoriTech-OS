---
name: saas-architecture-planner
description: Design provider-neutral SaaS architectures covering tenant and identity boundaries, isolation, provisioning, entitlements, plans, metering, billing interfaces, quotas, data lifecycle, integrations, extensibility, reliability, scaling, observability, support, compliance, unit economics, portability, and tenant retirement. Use for new multi-tenant products, SaaS migrations, enterprise-ready redesigns, platform reviews, or vibe-coded SaaS foundations - not detailed implementation, production provisioning, tax or accounting advice, or assuming shared infrastructure is safe without enforced isolation.
---

# SaaS Architecture Planner

Design the tenant lifecycle, control plane, and economic boundaries before choosing
providers.

## Procedure

1. Confirm the product outcome, customer types, tenant model, users and
   administrators, regulated or enterprise needs, regions, scale assumptions,
   availability and recovery objectives, pricing intent, budget, and owners.
2. Define tenant, organization, workspace, environment, user, service identity,
   resource, ownership, and delegation boundaries. State whether hierarchy,
   cross-tenant collaboration, or reseller administration is permitted.
3. Choose pooled, bridge, siloed, or hybrid isolation independently for compute,
   data, storage, encryption keys, queues, caches, search, analytics, logs, and
   backups using
   [references/saas-architecture-standard.md](references/saas-architecture-standard.md).
4. Enforce tenant context and resource authorization in trusted services and the
   data layer. Define provisioning, invitation, federation, role administration,
   impersonation, support access, break-glass use, access review, and audit.
5. Model the tenant lifecycle: trial, signup, verification, provisioning,
   configuration, import, activation, upgrade, downgrade, suspension, restoration,
   export, cancellation, retention, deletion, and final evidence. Make each step
   idempotent and recoverable.
6. Separate product catalog, plan, price, entitlement, limit, consumption,
   invoice, payment status, and access state. Define effective dates, grandfathering,
   trials, credits, promotions, proration, grace periods, and manual adjustments.
7. Define metering units, event identity, source of truth, event time, ingestion,
   deduplication, corrections, aggregation, late events, reconciliation, retention,
   audit, and customer-visible usage. Do not derive financial records from
   mutable operational counters.
8. Define quotas and fair-use controls with measurement window, enforcement point,
   warning, hard or soft behavior, concurrency, burst, tenant overrides, and
   administrative approval.
9. Separate control-plane operations from tenant workloads. Define asynchronous
   jobs, queues, schedulers, workflow state, retries, idempotency, dead letters,
   reconciliation, and protection against one tenant exhausting shared resources.
10. Define data residency, encryption, tenant keys where required, backup and
    restore, point-in-time recovery, export, portability, retention, legal hold,
    deletion propagation, audit, and per-tenant recovery limitations.
11. Define public and internal APIs, webhooks, events, integrations, app or
    extension boundaries, tenant credentials, consent, scopes, versioning, rate
    limits, idempotency, signatures, replay, and revocation.
12. Design for demand with tenant and workload segmentation, noisy-neighbor
    controls, sharding keys, routing, caching, queue isolation, capacity headroom,
    regional topology, failure domains, load shedding, and degraded modes.
13. Define service-level indicators and objectives for critical journeys,
    provisioning, authorization, metering, billing handoffs, integrations, jobs,
    data freshness, recovery, support, and tenant-level health.
14. Model cost per tenant, active user, transaction, storage unit, model call, or
    other causal driver. Attribute shared and third-party costs, set budget and
    margin guardrails, and expose anomalous consumption without weakening service
    or control requirements.
15. Define environment isolation, immutable releases, schema and contract
    compatibility, tenant-safe migrations, staged rollout, feature flags,
    rollback or forward-fix, support tooling, runbooks, and incident boundaries.
16. Keep provider services behind explicit adapters for identity, data, storage,
    payments, messaging, analytics, observability, AI, and hosting. Record lock-in,
    export, substitute, and exit costs.
17. Deliver with
    [assets/saas-architecture-template.md](assets/saas-architecture-template.md).

## Guardrails

- Do not trust a client-supplied tenant identifier without authorized server-side
  resolution.
- Do not rely on application filters alone when stronger data-layer isolation is
  feasible.
- Do not make billing status the only authorization check; resolve effective
  entitlements explicitly.
- Do not count retries, duplicates, or corrected events as billable usage without
  defined reconciliation.
- Do not expose cross-tenant data in logs, caches, analytics, search, exports,
  backups, support tools, or error messages.
- Do not let one tenant consume unbounded shared resources.
- Do not promise per-tenant restore, residency, deletion, or isolation the
  architecture cannot verify.
- Do not couple core product contracts to one provider without documenting the
  business reason and exit path.

## Recovery

If tenant identity, authorization, isolation, billing state, or data lifecycle
cannot be verified, mark the affected architecture provisional and block that
capability from production design approval. Default to stronger isolation and
least privilege, preserve unresolved decisions, and require specialist review
where legal, financial, privacy, or security obligations control the answer.

## Output Contract

Provide the context and tenant model, isolation matrix, identity and authorization,
tenant lifecycle, entitlements and billing boundary, metering and quotas, control
plane, data lifecycle, integration and extension contracts, scaling and failure
domains, observability and SLOs, cost model, deployment and operations, provider
adapters, risks, assumptions, and open decisions.
