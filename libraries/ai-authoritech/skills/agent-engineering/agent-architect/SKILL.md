---
name: agent-architect
description: Design platform-agnostic AI agents with a justified purpose, bounded autonomy, explicit authority, workflows, tools, knowledge, memory, state, human approvals, safety controls, evaluation, deployment, monitoring, incident handling, versioning, and retirement. Use for custom-agent architecture, agent workflow design, single-versus-multi-agent decisions, agent requirements, or production-readiness planning - not prompt polishing alone or implementation on an unspecified platform.
---

# Agent Architect

Design the smallest controllable system that achieves the outcome.

## Procedure

1. Define the user, job, trigger, terminal outcome, operating environment, volume,
   consequence, latency, and success measures.
2. Apply the agent-necessity test in
   [references/agent-architecture-standard.md](references/agent-architecture-standard.md).
   Prefer a deterministic workflow, tool, or ordinary application when sufficient.
3. Select single agent, agent plus deterministic workflow, or multi-agent design.
   Require a concrete isolation or specialization benefit for every extra agent.
4. Set autonomy tier and an authority matrix covering read, propose, create draft,
   modify, execute, communicate, spend, delete, publish, and escalate.
5. Define skills, workflows, tools, credentials, inputs, outputs, state, context,
   knowledge sources, retrieval rules, and memory retention boundaries.
6. Specify human approval before consequential actions and define timeout,
   rejection, correction, and unavailable-reviewer behavior.
7. Model normal flow, exceptions, retries, idempotency, partial completion,
   compensation, safe-stop, and escalation.
8. Define threat boundaries for prompt injection, data leakage, tool misuse,
   privilege escalation, untrusted content, and cross-user contamination.
9. Define evaluation datasets, acceptance thresholds, adversarial tests, regression
   gates, cost and latency budgets, and human-review sampling.
10. Plan deployment, observability, incident response, rollback, change control,
    ownership, service support, and retirement.
11. Deliver with [assets/agent-architecture-template.md](assets/agent-architecture-template.md).

## Guardrails

- Do not grant a tool permission merely because a tool is available.
- Do not rely on persona language as a safety control.
- Do not store sensitive memory without purpose, authority, retention, deletion,
  and access rules.
- Do not let agents approve their own high-consequence actions.
- Do not use multi-agent architecture to decorate a simple sequence.
- Do not claim production readiness without evaluation evidence and operating owners.
- Keep platform adapters separate from the platform-agnostic agent contract.

## Output Contract

Provide the architecture, authority matrix, workflow and state contracts, tool and
data boundaries, human gates, evaluation plan, operational model, unresolved risks,
and implementation tasks for prompts, knowledge, integrations, QA, and deployment.

## Recovery

If purpose, authority, consequence, or accountable ownership is unresolved, return
a provisional architecture and decision register instead of granting autonomy. If
agent necessity is not demonstrated, recommend the simpler deterministic pattern.
If a critical control cannot be designed, reduce authority or stop the design.
