---
name: agent-workflow-builder
description: Convert an approved agent architecture into durable, recoverable execution workflows with events, state, checkpoints, tool actions, approvals, resumability, concurrency, idempotency, retries, compensation, human and agent handoffs, completion evidence, and observability. Use for long-running agent workflows, tool-executing agents, human-in-the-loop orchestration, or multi-agent handoffs - not general business-process mapping or agent architecture.
---

# Agent Workflow Builder

Specialize the Core Workflow Composer for reliable agent execution.

## Procedure

1. Confirm the approved agent purpose, autonomy, authority matrix, workflows, tools,
   state, memory, human gates, failure policy, and operating constraints.
2. Define trigger events, correlation and idempotency keys, caller identity, input
   schema, authorization context, deadlines, and terminal events.
3. Define the durable state and action-journal contract using
   [references/agent-workflow-standard.md](references/agent-workflow-standard.md).
4. Decompose execution into bounded steps with preconditions, executor, input,
   effect, output, verification, checkpoint, timeout, and failure transition.
5. Separate reasoning steps from effectful tool actions. Revalidate authority and
   inputs immediately before every consequential action.
6. Add approval states that suspend safely and define approve, reject, amend,
   expire, cancel, unavailable-reviewer, and resume behavior.
7. Define retry eligibility, backoff, attempt limit, duplicate suppression,
   compensation, partial completion, dead-letter handling, and escalation.
8. Define concurrency, ordering, locking, stale-event, duplicate-event, and
   out-of-order behavior.
9. Validate every human, tool, workflow, and agent handoff against explicit schemas
   and authority; never rely on free-form trust.
10. Define logs, traces, metrics, alerts, audit evidence, cost and latency budgets,
    replay controls, rollback, and recovery objectives.
11. Deliver with [assets/agent-workflow-template.md](assets/agent-workflow-template.md).

## Guardrails

- Do not keep critical workflow state only in model context.
- Do not retry non-idempotent actions without duplicate protection or compensation.
- Do not mark a step complete before verifying its external effect.
- Do not allow an expired approval to authorize a later changed action.
- Do not let one agent's assertion substitute for downstream validation.
- Minimize sensitive state and separate secrets from workflow payloads.
- Keep runtime-specific code and configuration in platform adapters.

## Output Contract

Provide event and state schemas, step contracts, action journal, approval states,
retry and compensation matrix, handoff contracts, observability plan, scenario
tests, and platform-adapter requirements.

## Recovery

If an external effect cannot be verified, leave the step unresolved and reconcile
state before retrying. If approval expires or the proposed action changes, request
new approval. If compensation is unavailable for a failed consequential action,
stop, preserve evidence, and escalate to the accountable operator.
