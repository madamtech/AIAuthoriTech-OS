# SaaS Architecture Standard

## Isolation models

| Model | Description | Strength | Cost and complexity |
|---|---|---|---|
| Pooled | Tenants share infrastructure and logical stores | Efficient and elastic | Requires rigorous contextual isolation |
| Bridge | Shared services with tenant-scoped partitions or databases | Stronger data boundary | More routing and lifecycle work |
| Siloed | Dedicated stack or resources per tenant | Strong isolation and customization | Highest operating burden |
| Hybrid | Isolation varies by component or tenant tier | Matches diverse requirements | Complex policy and support model |

Choose separately for compute, database, object storage, search, queues, caches,
analytics, keys, logs, and backups. Document enforcement and tests for each.

## Tenant context

Resolve tenant context from authenticated membership, trusted routing, or service
credentials. Bind it to authorization, queries, cache keys, storage paths, queue
messages, logs, metrics, audit events, jobs, exports, and integrations. Reject
missing, conflicting, or unauthorized context.

## Entitlements and commerce

Treat these as distinct concepts:

- catalog: sellable product and add-on definitions;
- price: amount, currency, interval, usage rate, and effective dates;
- plan: packaged commercial offer;
- entitlement: effective capability granted to a tenant;
- limit: allowed quantity or concurrency;
- meter: measured consumption;
- billing record: financially relevant, reconcilable usage or charge;
- payment state: external commercial status informing a controlled access policy.

Keep a versioned entitlement decision with source and effective time. Design for
billing-provider outage, webhook delay, dispute, refund, and manual correction.

## Meter integrity

Every usage event needs tenant, event ID, meter, quantity, unit, event time, source,
schema version, idempotency, and provenance. Preserve raw immutable events when
appropriate, aggregate deterministically, reconcile with the source, and maintain
corrections without erasing financial history.

## Noisy-neighbor controls

Define per-tenant quotas, rate limits, concurrency, queue partitions, timeouts,
payload limits, job budgets, storage limits, cache isolation, circuit breakers,
and load shedding. Segment high-risk or high-volume tenants when pooled controls
cannot meet objectives.

## Tenant lifecycle

Make provisioning and deprovisioning stateful, idempotent, observable, and
reconcilable. Never treat a payment webhook as proof that every internal
entitlement, resource, or deletion action completed. Maintain exception queues and
named support ownership.

## Evidence

Test tenant isolation, resource authorization, cache and search boundaries,
support access, metering duplicates and corrections, entitlement timing, quota
enforcement, lifecycle retries, deletion, export, restore limitations, noisy
neighbors, regional failure, billing-provider outage, and cross-version rollout.
