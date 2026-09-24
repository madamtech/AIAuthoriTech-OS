---
name: implementation-planner
description: Convert an approved roadmap, initiative charter, proposal, or statement of work into an executable implementation plan covering workstreams, deliverables, dependencies, resources, environments, governance, testing, controls, adoption, cutover, rollback, support, and benefits realization. Use for delivery mobilization, pilot planning, production implementation, or phased rollout - not for inventing scope, changing contractual commitments, or replacing detailed specialist engineering plans. Use when asked to (1) plan implementation, (2) revise implementation, (3) evaluate options for implementation, or (4) prepare implementation of implementation.
---

# Implementation Planner

Create a traceable plan that can be governed and safely executed.

## Procedure

1. Confirm the authoritative scope, outcomes, constraints, acceptance criteria,
   owners, funding, target range, and change-control authority.
2. Reconcile roadmap and SOW conflicts before planning; do not silently resolve them.
3. Decompose delivery into workstreams using
   [references/implementation-standard.md](references/implementation-standard.md).
4. Define milestones and tasks with owner, inputs, outputs, dependencies, effort,
   capacity, due condition, validation, and completion evidence.
5. Map the critical path, external dependencies, lead times, decision deadlines,
   environments, access, data, procurement, and resource bottlenecks.
6. Add governance, architecture, security, privacy, AI-risk, model, data, and release
   gates appropriate to the initiative.
7. Define test strategy, entry and exit criteria, defect severity, acceptance,
   cutover, rollback, continuity, and hypercare.
8. Plan communications, stakeholder engagement, training, adoption, support, and
   operating ownership.
9. Establish baseline measures, benefit owners, instrumentation, review cadence,
   and stop or redesign triggers.
10. Deliver with [assets/implementation-plan-template.md](assets/implementation-plan-template.md).

## Guardrails

- Do not turn planning ranges into committed dates without dependency and capacity
  evidence.
- Do not schedule production deployment before required approval and test gates.
- Do not treat training delivery as evidence of adoption.
- Do not leave rollback, ownership, monitoring, support, or retirement undefined.
- Keep changes outside approved scope in the change register.
- Use one focused question only when missing authority or scope prevents a valid plan;
  otherwise mark assumptions and produce a provisional plan.

## Output Contract

Provide the integrated plan, workstream plans, critical path, RACI, RAID and decision
logs, quality gates, cutover and rollback plan, adoption plan, benefits plan, and
open items requiring specialist design or change approval.

## Recovery

If scope or authority is unresolved, isolate the affected workstream and return a
provisional plan with a decision deadline. If capacity or dependencies cannot
support the target range, show a feasible scenario and escalation path. If a
required production gate fails, hold deployment and preserve rollback readiness.
