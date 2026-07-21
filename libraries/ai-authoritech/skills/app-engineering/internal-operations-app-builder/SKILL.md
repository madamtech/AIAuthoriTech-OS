---
name: internal-operations-app-builder
description: Convert validated internal workflows into build-ready operations-app specifications covering actors, work items, queues, states, assignments, approvals, service levels, exceptions, data ownership, integrations, automation, permissions, audit, dashboards, notifications, accessibility, migration, testing, deployment, and support. Use for case management, request intake, review queues, fulfillment, back-office administration, compliance operations, inventory workflows, or internal command centers—not to automate an unvalidated process, erase necessary controls, monitor employees covertly, or deploy without authorization.
---

# Internal Operations App Builder

Build the operating model and exception paths before generating screens.

1. Confirm the validated current-state workflow, intended outcome, process owner,
   participants, volume, variants, service expectations, pain points, controls,
   risks, evidence status, and success measures.
2. Define future-state boundaries and non-goals. Remove, simplify, standardize, or
   clarify work before automating it; preserve disputed decisions for the
   accountable owner.
3. Model request, case, order, task, approval, exception, document, communication,
   party, asset, and reference data with stable IDs, source of truth, ownership,
   sensitivity, lifecycle, and audit.
4. Define state machines with allowed transitions, actor, prerequisites, business
   rules, deadlines, effects, idempotency, evidence, reversal, and escalation using
   [references/internal-operations-standard.md](references/internal-operations-standard.md).
5. Define intake channels, required information, validation, duplicate detection,
   classification, prioritization, acknowledgement, routing, and correction.
6. Define queues, skills or roles, capacity, assignment, claiming, reservation,
   concurrency, reassignment, handoff, aging, service clocks, pause rules,
   escalation, and workload balancing.
7. Define decisions and approvals with authority, separation of duties, thresholds,
   delegation, evidence, version, expiration, rejection, override, appeal, and
   audit. Do not replace accountable judgment with an unexplained score.
8. Define normal, alternate, exception, cancellation, correction, reopen, partial,
   duplicate, timeout, unavailable-system, and manual-recovery paths.
9. Define roles and resource-level permissions for requesters, operators,
   supervisors, approvers, auditors, administrators, support, integrations, and
   automation. Control bulk actions, export, impersonation, and break-glass access.
10. Define source-of-truth mapping, integration triggers, contracts, field
    mapping, service identities, idempotency, retries, reconciliation, exception
    queues, freshness, and failure ownership.
11. Assign automation only deterministic, authorized work with measurable
    outcomes and safe recovery. Define human review, confidence thresholds,
    override, monitoring, fallback, and evaluation for AI-assisted steps.
12. Design role-specific workspaces for today's work, priority, blockers,
    deadlines, exceptions, context, next action, history, and help. Define all
    loading, empty, stale, partial, denied, error, success, and recovery states.
13. Define notifications by event, audience, purpose, channel, timing, preference,
    acknowledgement, escalation, sensitive-content limit, and relation to
    authoritative workflow state.
14. Define operational metrics for demand, arrival rate, work in progress,
    throughput, age, cycle and wait time, service attainment, rework, exceptions,
    quality, control effectiveness, automation, cost, and outcome. Avoid ranking
    individual workers from context-free activity counts.
15. Define migration, parallel operation, reconciliation, cutover, rollback,
    training, support, runbooks, access review, continuity, retention, and
    retirement of spreadsheets, forms, inboxes, or legacy tools.
16. Decompose delivery into vertical slices that complete a real request or case
    with rules, permissions, integrations, evidence, tests, deployment,
    observability, and support.
17. Deliver with
    [assets/internal-operations-app-template.md](assets/internal-operations-app-template.md).

## Rules

- Do not automate a disputed or unvalidated workflow as though it were approved.
- Do not encode policy only in UI visibility; enforce rules server-side and at the
  data layer.
- Do not silently drop, overwrite, or strand duplicate, invalid, partial, or
  failed work.
- Do not let bulk actions bypass per-record authorization, validation, audit, or
  recovery.
- Do not call a request complete until authoritative effects are reconciled.
- Do not remove a control solely because it slows the happy path; validate its
  purpose and redesign it explicitly.
- Do not use productivity telemetry for covert surveillance or unsupported
  performance judgments.
- Do not allow automation to approve its own consequential exceptions.

## Handoff

Provide the current and future-state boundaries, actor and work-item model, state
machines, intake and queues, assignments and service clocks, approvals, exceptions,
permissions, integrations, automation controls, workspace and state design,
notifications, metrics, migration, vertical slices, testing, deployment,
operations, risks, assumptions, and open decisions.
