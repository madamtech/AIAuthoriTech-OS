---
name: refactoring-advisor
description: Assess code and architecture for behavior-preserving refactoring opportunities, establish measurable baselines and characterization tests, identify coupling and ownership problems, rank changes by value and risk, define safe seams and migration stages, protect public contracts and data, and specify verification, rollout, rollback, and completion evidence. Use for web, mobile, desktop, API, data, automation, AI-enabled, legacy, or vibe-coded systems—not to rewrite working software for style alone, mix feature work into a refactor, or modify code when only advice or review was requested.
---

# Refactoring Advisor

Improve internal structure without silently changing observable behavior.

1. Confirm whether the request authorizes analysis, a plan, or implementation.
   For advice-only work, inspect and report without editing files, dependencies,
   configuration, schemas, data, infrastructure, or external systems.
2. Define the business reason, affected users and teams, pain signals, scope,
   constraints, deadlines, supported clients, compatibility window, risk
   tolerance, and success measures. Decline change for change's sake.
3. Inventory the code paths, modules, APIs, events, schemas, jobs, data stores,
   dependencies, configuration, feature flags, tests, ownership, deployments,
   runtime signals, incidents, and known defects in scope.
4. Establish observable contracts: inputs, outputs, side effects, errors,
   ordering, timing, idempotency, authorization, accessibility, performance,
   persistence, compatibility, and operational behavior.
5. Assess evidence using
   [references/refactoring-standard.md](references/refactoring-standard.md).
   Identify duplication, high change coupling, unclear ownership, hidden state,
   boundary leakage, cyclic dependencies, unsafe abstractions, dead code,
   excessive complexity, fragile tests, dependency risk, and operational toil.
6. Distinguish symptom, structural cause, business impact, and supporting
   evidence. Do not infer a refactoring need from a metric or code smell alone.
7. Create characterization tests for important behavior not already protected.
   Cover normal, boundary, invalid, unauthorized, concurrent, interrupted,
   failure, recovery, and external-effect cases proportionate to risk.
8. Define the target boundary and invariants before moving code. Identify module
   ownership, dependency direction, interfaces, data authority, transaction
   boundaries, failure containment, and observability.
9. Compare options including no change, local cleanup, extraction, facade,
   adapter, branch-by-abstraction, strangler migration, dependency replacement,
   data migration, or redesign. Record benefits, cost, risks, reversibility,
   prerequisites, and rejected alternatives.
10. Rank work by user or business impact, change frequency, failure exposure,
    security and data risk, developer toil, testability, effort, reversibility,
    dependency, and cost of delay.
11. Break the refactor into small stages that keep the system runnable. Separate
    behavior-preserving moves, compatibility adapters, migrations, traffic or
    caller switching, verification, and cleanup.
12. Keep feature changes and defect fixes outside the refactor unless separately
    identified, tested, reviewed, and authorized. If behavior must change, create
    a distinct requirement and acceptance path.
13. Define compatibility for APIs, events, schemas, stored data, configuration,
    clients, plugins, scripts, and reports. Use expand, migrate, switch, verify,
    and contract for stateful changes.
14. Set a verification gate for every stage: static checks, characterization,
    unit, contract, integration, end-to-end, accessibility, security, performance,
    migration, observability, and authoritative business-state evidence.
15. Plan feature flags, shadowing, dual reads or writes only where justified,
    staged rollout, observation, rollback or forward-fix, data reconciliation,
    alert thresholds, and named decision owners.
16. Define cleanup criteria for adapters, old paths, flags, schemas, dependencies,
    tests, documentation, and telemetry. Do not remove compatibility mechanisms
    until consumers and stored state are verified.
17. Deliver with
    [assets/refactoring-advice-template.md](assets/refactoring-advice-template.md).

## Rules

- Do not change code when the user requested only advice, diagnosis, or review.
- Do not describe a behavior change as a refactor.
- Do not refactor solely to satisfy taste, novelty, line count, or a fashionable
  pattern without measurable value.
- Do not remove duplication when the similar code represents different business
  rules or change reasons.
- Do not introduce a shared abstraction before its stable responsibility and
  ownership are understood.
- Do not combine broad renames, dependency upgrades, schema changes, and feature
  work in one unverifiable change.
- Do not delete old paths, data, flags, or adapters before compatibility and
  authoritative state are verified.
- Do not claim success from green unit tests alone when external contracts,
  accessibility, performance, data, or operations can change.

## Handoff

Provide the authority and scope, business reason and measures, current inventory,
observable contracts, evidence-backed findings, characterization gaps, target
boundaries and invariants, option analysis, prioritized staged plan,
compatibility and migration controls, verification gates, rollout and recovery,
cleanup criteria, risks, assumptions, and open decisions.
