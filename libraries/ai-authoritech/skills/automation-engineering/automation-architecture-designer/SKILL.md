---
name: automation-architecture-designer
description: Design reliable, secure, observable automation architecture across orchestrators, queues, APIs, events, workers, data stores, identity, secrets, approvals, and recovery. Use when an automation blueprint requires technical component, deployment, scaling, availability, or integration decisions. Do not select technology without requirements or confuse architecture with deployed implementation.
---

# Automation Architecture Designer

1. Confirm blueprint, workloads, criticality, latency, throughput, residency, security, availability, and cost constraints.
2. Choose synchronous, asynchronous, scheduled, event-driven, batch, or hybrid patterns from evidence.
3. Define components, boundaries, state, queues, events, schemas, identities, secrets, and network paths.
4. Design idempotency, ordering, concurrency, backpressure, retries, dead letters, compensation, and reconciliation.
5. Enforce least privilege, tenant separation, encryption, approvals, auditability, and data minimization.
6. Design health, metrics, traces, alerts, runbooks, scaling, continuity, deployment, rollback, and change control.
7. Test failure domains, dependency loss, partial writes, duplicates, stale events, overload, and recovery objectives.
8. Deliver diagrams, decisions, interfaces, threat model, capacity, operations, tests, risks, and alternatives.

## Rules

- Do not use retries without idempotency and bounded retry policy.
- Do not rely on logs as the only source of workflow state or audit evidence.
- Do not create single points of failure that violate recovery requirements.
- Do not put credentials or sensitive payloads in diagrams, examples, or logs.
