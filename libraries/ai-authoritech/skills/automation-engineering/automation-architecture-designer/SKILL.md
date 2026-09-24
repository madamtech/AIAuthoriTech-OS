---
name: automation-architecture-designer
description: Design reliable, secure, observable automation architecture across orchestrators, queues, APIs, events, workers, data stores, identity, secrets, approvals, and recovery. Use when an automation blueprint requires technical component, deployment, scaling, availability, or integration decisions. Do not select technology without requirements or confuse architecture with deployed implementation. Use when asked to (1) design automation architecture, (2) revise automation architecture, (3) compare options for automation architecture, or (4) document specifications for automation architecture.
---

# Automation Architecture Designer

Use the [automation architecture standard](references/automation-architecture-standard.md) to select and validate technical patterns. Record components, decisions, controls, and recovery in the [automation architecture template](assets/automation-architecture-template.md).

## Procedure

1. Confirm blueprint, workloads, criticality, latency, throughput, residency, security, availability, and cost constraints.
2. Choose synchronous, asynchronous, scheduled, event-driven, batch, or hybrid patterns from evidence.
3. Define components, boundaries, state, queues, events, schemas, identities, secrets, and network paths.
4. Design idempotency, ordering, concurrency, backpressure, retries, dead letters, compensation, and reconciliation.
5. Enforce least privilege, tenant separation, encryption, approvals, auditability, and data minimization.
6. Design health, metrics, traces, alerts, runbooks, scaling, continuity, deployment, rollback, and change control.
7. Test failure domains, dependency loss, partial writes, duplicates, stale events, overload, and recovery objectives.
8. Deliver diagrams, decisions, interfaces, threat model, capacity, operations, tests, risks, and alternatives.

## Guardrails

- Do not use retries without idempotency and bounded retry policy.
- Do not rely on logs as the only source of workflow state or audit evidence.
- Do not create single points of failure that violate recovery requirements.
- Do not put credentials or sensitive payloads in diagrams, examples, or logs.

## Recovery

If state ownership, idempotency, credentials, failure domains, or recovery behavior cannot be demonstrated, block implementation approval. Preserve source-system state, isolate incomplete effects, document the architecture gap, and require successful failure and recovery tests before promotion.

## Output Contract

Deliver a completed architecture package containing context and component diagrams, state and data flows, interface contracts, identity and secret controls, reliability patterns, threat considerations, capacity assumptions, observability, deployment, recovery, alternatives, risks, tests, and decision records.
