# Backend Architecture Standard

## Topology decision

Start with the simplest deployable topology that meets verified requirements.
Compare options using:

- cohesive domain responsibility and team ownership;
- release cadence and independent deployment need;
- data authority, transaction, and consistency boundaries;
- scale profile and bottlenecks;
- failure isolation and blast radius;
- latency and synchronous dependency depth;
- testing, debugging, observability, security, and incident complexity;
- infrastructure, platform, staffing, and support cost;
- migration reversibility and exit path.

A modular monolith is often appropriate when boundaries are evolving or one team
owns the system. Services are justified when independent ownership, deployment,
failure containment, or materially different scaling outweigh distributed-system
cost.

## Boundary contract

For every module or service define responsibility, owner, authoritative data,
allowed writers, commands, queries, events, invariants, dependencies, identities,
authorization, SLO, deployment, on-call, and retirement.

Communicate through versioned contracts. Do not expose internal database models.
Avoid distributed call chains on critical paths; record timeouts and end-to-end
latency budgets.

## Consistency and effects

Identify transaction boundaries and required consistency for every invariant.
Use an outbox or equivalent atomic publication when state and events must agree.
For distributed workflows, define state machine, step identity, idempotency,
timeouts, retries, compensation, checkpoints, reconciliation, and manual recovery.

Design for duplicates, missing and late messages, reorder, consumer restart,
poison messages, timeout after effect, partial success, and replay. Preserve the
authoritative result independently from transient transport state.

## Resilience

Set timeouts from end-to-end budgets. Bound retries with jitter and a retry budget.
Use backpressure and admission control before saturation. Define circuit behavior,
bulkheads, load shedding, degraded modes, queue limits, dead-letter ownership,
dependency substitution, and operator actions.

Recovery must specify authoritative state inspection, replay safety,
reconciliation, rollback or forward-fix, customer impact, and evidence.

## Security and data

Authenticate workload identities and scope service authority. Authorize resources
in trusted context. Validate at ingress and at invariant boundaries. Protect
secrets, keys, certificates, sensitive data, logs, traces, events, backups,
exports, support tools, and nonproduction environments.

Define retention, deletion propagation, legal hold where applicable, audit,
access review, vulnerability response, provenance, incident containment, and
credential revocation.

## Operations and evolution

Each critical workflow needs business and technical signals, correlation, SLOs,
alerts, dashboards, runbooks, support and on-call owners, capacity thresholds,
cost attribution, backup and restore evidence, and incident exercises.

Evolve schemas and contracts through expand, migrate, switch, verify, and
contract. Keep old and new participants compatible during the rollout window.
Remove adapters and old state only after consumers and authoritative data are
verified.
