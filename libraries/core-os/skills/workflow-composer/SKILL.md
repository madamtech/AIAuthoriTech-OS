---
name: workflow-composer
description: Design governed end-to-end workflows coordinating multiple registered skills, tools, people, decisions, shared state, validation gates, approvals, retries, recovery, and completion evidence. Use when asked to compose, orchestrate, or document a multi-stage process whose stages exchange state or require branching and control. Do not use for a single cohesive skill or to claim the designed workflow has been executed. Use when asked to (1) create workflow composer, (2) review workflow composer, (3) improve workflow composer, or (4) standardize workflow composer.
---

# Workflow Composer

Design the orchestration contract; do not execute it unless separately authorized.

## Procedure

1. Define the trigger, business outcome, owner, participants, scope, entry criteria, terminal states, and out-of-scope conditions.
2. Read [references/workflow-design-standard.md](references/workflow-design-standard.md) and verify every referenced skill, tool, agent, template, and knowledge pack in the catalog.
3. Define the minimum shared state, field ownership, sensitivity, retention, lineage, and allowed mutation.
4. For each stage specify stable ID, executor, prerequisites, input contract, action, output contract, validation, evidence, timeout, success route, and failure route.
5. Add branches only for explicit decision conditions; make every branch converge, terminate, or escalate.
6. Add human approval before external, irreversible, financial, legal, security-sensitive, or otherwise consequential action not already authorized.
7. Bound retries by count and condition. Distinguish retryable failures, compensating actions, rollback, graceful degradation, and terminal escalation.
8. Define observability: status, timestamps, correlation ID, decisions, tool calls, approvals, failures, and completion evidence.
9. Verify handoff compatibility, dependency availability, authorization, privacy, idempotency, recovery, and completion criteria.
10. Produce a `workflow.json` manifest conforming to `schemas/workflow.schema.json`, plus a readable stage and branch summary.
11. Run repository validation before catalog registration.

## Decision Rules

- Use a skill instead when one actor can complete one cohesive job without shared orchestration state.
- Use a sequence instead when tasks are independent and require no branches, approval, retries, or recovery.
- Use a subworkflow when a reusable group of stages has its own trigger, state boundary, and completion contract.
- Stop composition when a required capability, owner, authorization, or handoff contract is unresolved.

## Output Contract

Use [assets/workflow-design-template.json](assets/workflow-design-template.json). Include identity, trigger, state, stages, branches, approvals, retries, recovery, observability, completion criteria, dependencies, and unresolved decisions.

## Guardrails

- Do not reference nonexistent or incompatible assets.
- Do not allow unbounded loops or retries.
- Do not store sensitive state without a justified owner, access rule, and retention rule.
- Do not treat an attempted tool call or sent request as a completed business outcome.
- Preserve evidence lineage across every handoff.

## Recovery

When a dependency or handoff is invalid, preserve the valid stages, mark the workflow non-registerable, identify the exact contract gap, and provide the smallest safe revision.
