# Application Deployment Standard

## Artifact and provenance

Record the source revision, build identity, dependency lock state, build runtime,
tests, security scans, software bill of materials, checksum or signature, storage
location, retention, and promotion history. Promote the same immutable artifact
through environments.

## Rollout selection

| Strategy | Prefer when | Key control |
|---|---|---|
| Recreate | Downtime is acceptable and state is simple | Verified maintenance window |
| Rolling | Instances are compatible during transition | Readiness and surge capacity |
| Blue-green | Fast traffic reversal justifies duplicate capacity | State and schema compatibility |
| Canary | Production signals can bound risk | Cohort control and automatic abort |
| Feature flag | Code release and feature exposure must be separated | Flag ownership and cleanup |
| Phased or regional | Users or regions can be isolated | Cohort parity and dependency awareness |

Choose a strategy based on measurable recovery and blast-radius needs, not trend.

## Compatibility sequencing

For stateful or distributed changes:

1. Expand: add compatible schema, contract, or capability.
2. Deploy compatible readers and writers.
3. Migrate or backfill with bounds, checkpoints, and reconciliation.
4. Switch traffic or behavior gradually.
5. Verify authoritative state and operational signals.
6. Contract only after old consumers and rollback windows expire.

Version APIs and events when coexistence cannot be preserved. Account for delayed
mobile clients, queued messages, retries, caches, replicas, and scheduled jobs.

## Preflight and gates

Require evidence appropriate to risk:

- approved change scope and named decision owner;
- passing required test suites and reviewed unresolved defects;
- artifact provenance and vulnerability findings;
- infrastructure plan and drift review;
- configuration, feature-flag, secret, certificate, and domain readiness;
- database backup and recent restore evidence;
- capacity and quota headroom;
- third-party and dependency status;
- monitoring, alerts, dashboards, and incident staffing;
- communications and customer-support readiness;
- verified rollback or forward-fix procedure.

## Verification matrix

Each check must define timing, command or method, expected result, authoritative
oracle, threshold, evidence, owner, and failure action. Cover:

- infrastructure readiness and application health;
- critical user journeys and permission boundaries;
- durable writes followed by authoritative reads;
- integrations, events, queues, scheduled jobs, and reconciliation;
- latency, errors, saturation, backlog, and data freshness;
- logging, tracing, alert delivery, audit events, and notifications.

Use business outcomes as the oracle. A container being ready or an endpoint
returning success is necessary but may not prove the release works.

## Rollback and forward-fix

Define objective triggers and a named authority. Preserve the previous artifact,
configuration, infrastructure state, and feature-flag values. State whether data
changes are backward compatible. If rollback would corrupt or discard data, use a
forward-fix or containment plan instead. Verify recovery using the same critical
checks used for release.

## Evidence and closure

Capture planned and actual scope, approvals, actors, times, artifacts, configuration
versions, commands or pipeline runs, results, metrics, deviations, waivers,
incidents, rollback actions, and final approval. Redact sensitive material and
retain evidence according to policy.
