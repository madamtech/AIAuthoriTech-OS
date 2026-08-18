---
name: multi-agent-system-designer
description: Determine whether multiple AI agents are justified and design a bounded multi-agent system with explicit roles, authority, routing, coordination, shared state, message contracts, handoffs, conflict resolution, human approvals, failure containment, evaluation, deployment, monitoring, and ownership. Use for orchestrator-worker systems, specialist agent teams, parallel agent workflows, reviewer patterns, or cross-domain coordination - not decorative agent personas, simple sequential workflows, or implementation on an unspecified platform. Use when asked to (1) design multi agent system, (2) revise multi agent system, (3) compare options for multi agent system, or (4) document specifications for multi agent system.
---

# Multi-Agent System Designer

Use the fewest independently operating agents needed to achieve a measurable
benefit.

## Procedure

1. Define the outcome, tasks, dependencies, consequence, volume, latency, privacy,
   specialization needs, and success measures.
2. Apply the multi-agent necessity test in
   [references/multi-agent-design-standard.md](references/multi-agent-design-standard.md).
   Prefer one agent, deterministic components, or ordinary workflows unless
   separation produces a concrete benefit.
3. Choose orchestration, hierarchy, peer collaboration, pipeline, supervisor-
   reviewer, market, or hybrid topology. State why the selected topology is safer
   or more effective than the alternatives.
4. Give each agent one bounded mission, inputs, outputs, knowledge, memory, tools,
   permissions, constraints, service objectives, failure behavior, and owner.
5. Define the system authority matrix. Prevent delegation from expanding the
   originating user's authority or bypassing human approval.
6. Define routing and assignment using explicit capability, risk, data, cost,
   capacity, and confidence rules. Specify no-match, tie, overload, and unavailable
   behavior.
7. Define message envelopes, schemas, provenance, correlation, idempotency,
   deadlines, version compatibility, validation, and rejection behavior.
8. Keep durable shared state outside model context. Define ownership, locking,
   consistency, stale-data handling, access isolation, retention, and audit history.
9. Define handoffs with preconditions, acceptance criteria, evidence, downstream
   validation, rejection, correction, timeout, cancellation, and escalation.
10. Resolve disagreement through evidence, deterministic policy, independent
    review, or accountable human decision. Do not use repeated debate as a safety
    control.
11. Model partial failure, duplicate work, loops, cascading retries, split-brain
    decisions, poisoned messages, compromised agents, dependency loss, and
    containment boundaries.
12. Define end-to-end and per-agent evaluation, adversarial scenarios, contribution
    and ablation tests, latency and cost budgets, observability, incident response,
    deployment, rollback, and retirement.
13. Deliver with
    [assets/multi-agent-system-template.md](assets/multi-agent-system-template.md).

## Guardrails

- Do not create an agent for a role that can be a deterministic function, policy,
  tool, queue, or workflow step.
- Do not grant all agents the union of every tool and permission.
- Do not trust another agent's identity, claim, output, or completion without
  authenticated context and validation appropriate to risk.
- Do not place critical shared state only in conversation history.
- Do not allow agents to approve each other's high-consequence actions when
  independent human approval is required.
- Do not let retries, delegation, or handoffs duplicate consequential effects.
- Do not use majority vote to resolve factual, policy, safety, or authority issues
  without evidence and an accountable decision rule.
- Keep platform-specific runtime configuration in adapters.

## Output Contract

Provide the necessity decision, topology, agent cards, authority matrix, routing
rules, communication and state contracts, handoff and conflict policies, failure
containment, human gates, evaluation plan, operating model, cost and latency model,
risks, and implementation tasks.

## Recovery

If multi-agent benefit is not demonstrated, collapse the design to one agent or a
deterministic workflow. If agents disagree, apply evidence and the accountable
decision rule rather than repeated debate. If identity, shared state, or authority
cannot be validated, reject the handoff and contain the affected branch.
