# Refactoring Standard

## Refactor test

A proposed change is a refactor only when its intended outcome is improved
internal structure while protected observable behavior remains equivalent. If
users, clients, data, permissions, timing guarantees, external effects, or
operational contracts intentionally change, track that work separately.

## Evidence for structural problems

Use multiple signals where possible:

- change history and files that repeatedly change together;
- incidents, regressions, support demand, and time to diagnose;
- dependency direction, cycles, boundary crossings, and ownership gaps;
- complexity, duplication, hidden state, side effects, and concurrency;
- test isolation, flakiness, setup cost, and feedback time;
- build, deploy, runtime, capacity, cost, security, and accessibility evidence;
- unsupported dependencies and vendor or platform lifecycle.

A code smell identifies where to inspect, not an automatic prescription.

## Protected contracts

Inventory:

- public and internal APIs, types, events, schemas, files, and CLI behavior;
- business rules, validation, errors, ordering, retries, and idempotency;
- authentication, authorization, tenant isolation, and audit;
- data ownership, transactions, retention, migration, and reconciliation;
- UI semantics, focus, keyboard behavior, accessibility, and responsive states;
- latency, throughput, memory, resource, reliability, and recovery budgets;
- logs, metrics, traces, alerts, runbooks, and support procedures.

Characterization must cover contracts at risk, including behavior that is odd but
currently depended upon. Mark defects separately rather than silently preserving
or correcting them.

## Safe change patterns

- **Local cleanup:** rename or simplify within a fully tested boundary.
- **Extract seam:** isolate side effects behind an interface before changing them.
- **Facade or adapter:** preserve callers while internals migrate.
- **Branch by abstraction:** run old and new implementations behind one contract.
- **Strangler:** move bounded capabilities incrementally.
- **Expand and contract:** add compatible schema or contract, migrate, switch,
  verify, then remove the old form.
- **Parallel or shadow comparison:** compare results without granting duplicate
  external authority.

Select the smallest pattern that controls risk. Avoid dual writes unless
idempotency, ordering, reconciliation, authority, and recovery are explicit.

## Stage gate

Every stage must define:

- intended structural change and protected behavior;
- files, contracts, data, dependencies, and consumers in scope;
- characterization and new tests;
- migration or adapter behavior;
- performance and operational thresholds;
- rollout, evidence, abort trigger, and recovery;
- completion and cleanup criteria.

Keep commits and reviews small enough to understand. Ensure the application builds
and the protected paths remain runnable after each stage.

## Prioritization

Rank using business impact, failure exposure, change frequency, security and data
risk, developer and operational toil, testability, effort, reversibility,
dependency sequence, and delay cost. Prefer enabling seams and tests before
structural movement.

## Completion

The refactor is complete only when protected contracts pass, authoritative state
reconciles, performance and operational measures remain within bounds, consumers
have migrated, old paths are unused, approved cleanup is finished, documentation
and ownership are current, and residual risk is recorded.
