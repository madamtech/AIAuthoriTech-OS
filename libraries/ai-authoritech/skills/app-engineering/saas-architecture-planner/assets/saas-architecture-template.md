# SaaS Architecture Plan

## Product context

- Product outcome and customer types:
- Tenant definition and hierarchy:
- Users and administrators:
- Scale and region assumptions:
- Data classification and obligations:
- Availability and recovery objectives:
- Pricing intent and economic constraints:
- Owners and decision rights:

## Tenant and identity model

| Actor or identity | Tenant relationship | Allowed resources | Delegation | Administration | Audit |
|---|---|---|---|---|---|

## Isolation matrix

| Component | Pooled, bridge, siloed, or hybrid | Tenant enforcement | Failure boundary | Test evidence | Owner |
|---|---|---|---|---|---|

## Tenant lifecycle

| State or transition | Trigger | Preconditions | Idempotency | Effects | Verification | Recovery | Owner |
|---|---|---|---|---|---|---|---|

## Product, entitlement, and commerce model

| Concept | Source of truth | Versioning or effective date | Failure behavior | Owner |
|---|---|---|---|---|

## Metering and quotas

| Meter or limit | Unit and window | Event source | Deduplication | Reconciliation | Enforcement | Customer visibility |
|---|---|---|---|---|---|---|

## Control plane and workloads

| Capability | Control or data plane | State | Queue or workflow | Retry and recovery | Isolation |
|---|---|---|---|---|---|

## Data lifecycle

| Data class | Residency | Encryption and keys | Backup and restore | Export | Retention | Deletion evidence |
|---|---|---|---|---|---|---|

## APIs, integrations, and extensions

| Contract | Identity and scope | Tenant context | Versioning | Limits | Failure and replay | Owner |
|---|---|---|---|---|---|---|

## Scaling and failure domains

| Demand driver | Segmentation or shard | Capacity signal | Tenant protection | Degraded mode | Recovery |
|---|---|---|---|---|---|

## Reliability and observability

| Journey or service | SLI | Objective | Tenant dimension | Alert | Runbook | Owner |
|---|---|---|---|---|---|---|

## Unit economics

| Cost driver | Attribution unit | Baseline | Budget or margin guardrail | Anomaly action | Owner |
|---|---|---|---|---|---|

## Deployment and operations

- Environment isolation:
- Migration and compatibility:
- Feature rollout:
- Rollback or forward-fix:
- Support and impersonation controls:
- Incident boundaries:

## Provider adapters and portability

| Capability | Contract | Current provider | Lock-in | Export or substitute | Exit trigger |
|---|---|---|---|---|---|

## Decisions and risks

| Item | Decision or risk | Evidence | Owner | Due or review trigger |
|---|---|---|---|---|
