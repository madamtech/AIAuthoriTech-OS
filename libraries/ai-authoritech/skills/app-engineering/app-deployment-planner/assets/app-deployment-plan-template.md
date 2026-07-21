# Application Deployment Plan

## Release control

- Product and release:
- Source revision:
- Artifact identifier and digest:
- Change owner:
- Release approver:
- Incident commander:
- Planned window:
- Status:

## Scope and constraints

- Business outcome:
- Included changes:
- Excluded changes:
- Users and regions affected:
- Criticality and data classification:
- Recovery objectives:
- Assumptions and open decisions:

## Dependency inventory

| Component | Current | Target | Owner | Compatibility | Evidence |
|---|---|---|---|---|---|

## Environments, configuration, and secrets

| Item | Development | Test | Staging | Production | Owner |
|---|---|---|---|---|---|

Record parity exceptions, secret locations without values, rotation needs, domains,
certificates, feature flags, quotas, and external dependencies.

## Rollout strategy

- Selected pattern:
- Selection rationale:
- Cohorts or traffic stages:
- Observation window per stage:
- Concurrency and locking:
- Automatic abort conditions:
- Manual decision owner:

## Change sequence

| Step | Change | Preconditions | Method | Expected result | Evidence | Owner | Abort action |
|---|---|---|---|---|---|---|---|

## Data and contract compatibility

| Change | Expand | Migrate or backfill | Switch | Verify | Contract | Recovery constraint |
|---|---|---|---|---|---|---|

## Preflight gates

| Gate | Required evidence | Status | Approver | Blocker or waiver |
|---|---|---|---|---|

## Verification matrix

| Check | Timing | Method | Authoritative oracle | Threshold | Evidence | Owner | Failure action |
|---|---|---|---|---|---|---|---|

## Observability

| Signal | Baseline | Warning | Abort or rollback | Dashboard or alert | Owner |
|---|---|---|---|---|---|

## Recovery runbook

- Rollback triggers:
- Forward-fix triggers:
- Decision authority:
- Previous artifact:
- Configuration restore:
- Feature-flag actions:
- Database and data implications:
- Traffic, queue, and job containment:
- Credential revocation:
- Recovery verification:

## Communications

| Audience | Before | During | Success | Degradation or rollback | Owner |
|---|---|---|---|---|---|

## Execution record

| Planned or actual time | Actor | Action | Result | Evidence | Deviation |
|---|---|---|---|---|---|

## Closure

- Final release state:
- Residual risk:
- Incidents or defects:
- Follow-up owners and dates:
- Evidence location:
- Final approval:
