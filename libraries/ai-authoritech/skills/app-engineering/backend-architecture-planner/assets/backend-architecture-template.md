# Backend Architecture Plan

## 1. Context and Constraints

- Product outcome and critical journeys:
- Workloads, scale, latency, consistency, availability, and recovery:
- Users, tenants, data classes, regions, and obligations:
- Team, budget, timeline, and owners:
- Confirmed constraints, assumptions, and open decisions:

## 2. Domain and Ownership Map

| Capability/aggregate | Responsibility/invariants | Business owner | Technical owner | Authoritative state | External systems |
|---|---|---|---|---|---|

## 3. Topology Decision

| Option | Ownership fit | Data/consistency | Scale/failure | Operability/cost | Exit path | Decision |
|---|---|---|---|---|---|---|

## 4. Module and Service Boundaries

| Boundary | Responsibility | Data authority | Contracts | Dependencies | Identity/access | SLO/owner |
|---|---|---|---|---|---|---|

## 5. Contract Inventory

| Contract | Type/version | Caller/consumer | Identity/authorization | Schema/effects | Errors/idempotency | Compatibility |
|---|---|---|---|---|---|---|

## 6. Data and Consistency

- Entity, tenancy, constraint, transaction, and concurrency model:
- Read models, cache, search, analytics, and derived data:
- Audit, retention, deletion, backup, restore, and migration:
- Completion states and authoritative reconciliation:

## 7. Asynchronous Workflows

| Workflow | State/steps | Message identity/order | Retry/idempotency | Compensation/reconcile | Operator recovery |
|---|---|---|---|---|---|

## 8. Failure and Resilience Model

| Failure | Impact/blast radius | Detection | Containment/degradation | Recovery | Owner |
|---|---|---|---|---|---|

## 9. Capacity, Performance, and Cost

| Resource/path | Workload/budget | Scaling trigger | Limit/quota | Cost driver | Action |
|---|---|---|---|---|---|

## 10. Security and Privacy

- Human, service, workload, job, and integration identities:
- Resource authorization and tenant isolation:
- Secrets, encryption, network, validation, and abuse controls:
- Data lifecycle, audit, vulnerabilities, provenance, and incident actions:

## 11. Observability and Operations

| Journey/service | Business/technical signals | SLO/threshold | Alert/runbook | Support/on-call owner |
|---|---|---|---|---|

## 12. Testing and Verification

| Risk/contract | Test level | Scenario | Environment/data | Evidence/gate |
|---|---|---|---|---|

## 13. Deployment and Evolution

- Repositories, builds, environments, configuration, and flags:
- Schema and contract compatibility:
- Rollout, observation, rollback or forward-fix, and reconciliation:
- Provider adapters, lock-in, export, substitute, and exit path:
- Retirement and cleanup:

## 14. Delivery

- Decisions and rationale:
- Risks and mitigations:
- Dependencies and milestones:
- Open decisions and owners:
