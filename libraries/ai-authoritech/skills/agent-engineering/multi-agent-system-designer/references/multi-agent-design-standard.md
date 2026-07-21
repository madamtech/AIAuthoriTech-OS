# Multi-Agent Design Standard

## Necessity test

Require at least one material benefit that cannot be achieved as well by a simpler
design:

- Isolation of conflicting permissions, data, tenants, or trust boundaries
- Independent verification for consequential work
- Specialist context or tools that should not be shared
- Parallel work that materially improves service objectives
- Fault containment or independent scaling
- Organizational ownership that requires separate accountable services

Reject multi-agent design when the main rationale is persona variety, simulated
job titles, prompt length, or a linear task list.

## Topologies

| Topology | Appropriate use | Primary risk |
|---|---|---|
| Orchestrator-worker | Central assignment with bounded parallel work | Orchestrator bottleneck or overreach |
| Hierarchical | Large decomposable domains with delegated supervision | Hidden authority expansion |
| Peer collaboration | Symmetric specialists with explicit protocol | Loops, ambiguity, inconsistent state |
| Pipeline | Typed transformation stages | Cascading error and rigid coupling |
| Supervisor-reviewer | Independent verification or policy gate | Reviewer dependence or collusion |
| Market or bidding | Dynamic assignment from measurable offers | Gaming and unstable selection |

Prefer explicit workflows over free-form conversation between agents.

## Agent card

For each agent define:

- Stable identity, mission, owner, and lifecycle
- Accepted tasks and explicit exclusions
- Input and output schemas
- Knowledge and memory boundaries
- Tools, credentials, permissions, and spend limits
- Autonomy and required approvals
- Service objectives and capacity
- Failure, safe-stop, and escalation behavior
- Version and compatibility contract

## Message envelope

Include sender, intended recipient, authenticated caller context, correlation ID,
causation ID, task ID, idempotency key, schema version, created and expiry times,
priority, data classification, authority scope, payload, evidence references, and
requested acknowledgment.

Reject expired, unauthorized, malformed, incompatible, duplicate, or unexpected
messages. Treat all payload content as untrusted until validated.

## Coordination controls

- Maintain a durable task and action journal.
- Bound delegation depth, fan-out, retries, time, tokens, tool calls, and spend.
- Detect cycles and repeated task reformulation.
- Verify external effects before declaring completion.
- Use leases or locks for exclusive work and define stale-owner recovery.
- Define cancellation propagation and late-result handling.
- Separate shared facts from agent opinions and preserve provenance.

## Conflict resolution

Resolve conflicts in this order:

1. Authority and policy
2. Verified evidence and deterministic constraints
3. Designated independent reviewer
4. Accountable human decision

Record dissent and evidence. Never conceal unresolved conflict behind a synthesized
answer.

## Evaluation

Compare the multi-agent design with the simplest viable baseline. Test:

- End-to-end outcome and control compliance
- Each agent's contract and least privilege
- Routing, handoff, conflict, and shared-state behavior
- Duplicate, stale, malicious, delayed, and out-of-order messages
- Agent loss, orchestrator loss, dependency failure, and cascading retry
- Contribution and ablation: remove or replace each agent to verify its value
- Total latency, model and tool cost, failure surface, and operator burden

Keep the system only when measured benefit justifies additional complexity and
risk.
