# Refactoring Advice

## 1. Authority and Scope

- Advice, plan, or implementation authorized:
- Business objective:
- Systems and boundaries in scope:
- Explicit exclusions:
- Owners, constraints, and decision authority:

## 2. Current-State Inventory

| Component/contract | Responsibility | Owner | Dependencies/data | Tests | Runtime evidence | Change risks |
|---|---|---|---|---|---|---|

## 3. Observable Contracts

| Contract | Consumers | Protected behavior | Evidence/test | Compatibility window |
|---|---|---|---|---|

Include data, access, errors, ordering, side effects, accessibility, performance,
recovery, and operational behavior.

## 4. Evidence-Backed Findings

| ID | Structural finding | Evidence | Business/engineering impact | Confidence | No-change consequence |
|---|---|---|---|---|---|

## 5. Characterization Gaps

| Behavior at risk | Existing evidence | Needed test | Test level | Owner | Gate |
|---|---|---|---|---|---|

## 6. Target Boundaries and Invariants

- Responsibility and ownership:
- Dependency direction:
- Interfaces and adapters:
- Data authority and transactions:
- Failure containment:
- Security, accessibility, performance, and operational invariants:

## 7. Option Analysis

| Option | Benefit | Cost/effort | Risk | Reversibility | Prerequisites | Decision |
|---|---|---|---|---|---|---|

Include no change.

## 8. Prioritized Stages

| Order | Stage | Structural change | Protected behavior | Dependencies | Verification | Recovery | Cleanup |
|---:|---|---|---|---|---|---|---|

## 9. Compatibility and Migration

| Contract/data/client | Expand | Migrate | Switch | Verify | Contract/remove |
|---|---|---|---|---|---|

## 10. Verification and Release

- Static, unit, characterization, contract, integration, and end-to-end gates:
- Accessibility, security, performance, and migration gates:
- Feature flags, shadowing, rollout, and observation:
- Authoritative business-state verification:
- Abort thresholds and rollback or forward-fix:

## 11. Completion

- Consumer migration evidence:
- Old-path usage evidence:
- Adapter, flag, schema, dependency, test, and documentation cleanup:
- Measures before and after:
- Residual risks and owners:
- Open decisions:
