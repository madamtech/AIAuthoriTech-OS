# Multi-Agent System Design

## Design control

- System and version:
- Business outcome:
- Risk and autonomy tier:
- Accountable owner:
- Platform constraints:

## Necessity decision

- Simplest viable baseline:
- Measured or expected multi-agent benefit:
- Rejected alternatives:
- Decision: Single agent / Workflow / Multi-agent

## Topology

- Selected topology and rationale:
- Orchestration and control plane:
- Human decision points:
- Trust and failure boundaries:

## Agent registry

| Agent | Mission | Owner | Inputs | Outputs | Knowledge | Tools | Authority | SLO |
|---|---|---|---|---|---|---|---|---|

## Authority matrix

| Action | Agent | Read | Propose | Draft | Modify | Execute | Communicate | Approver |
|---|---|---|---|---|---|---|---|---|

## Routing and assignment

| Request class | Eligibility | Selection rule | Confidence | No-match | Overload | Escalation |
|---|---|---|---|---|---|---|

## Communication contracts

| Message | Producer | Consumer | Schema | Authority | Validation | Expiry | Failure |
|---|---|---|---|---|---|---|---|

## Shared state

| State | Owner | Store | Writers | Readers | Consistency | Locking | Retention |
|---|---|---|---|---|---|---|---|

## Handoffs and conflicts

| Boundary | Preconditions | Evidence | Acceptance | Rejection | Timeout | Conflict rule |
|---|---|---|---|---|---|---|

## Failure containment

| Failure | Detection | Blast radius | Containment | Retry | Compensation | Escalation |
|---|---|---|---|---|---|---|

Cover loops, duplicates, stale messages, compromised agents, split-brain decisions,
dependency loss, cancellation, and partial completion.

## Evaluation and economics

| Measure | Single-system baseline | Multi-agent target | Guardrail | Evidence |
|---|---:|---:|---:|---|

Include contract, end-to-end, adversarial, contribution, ablation, latency, cost,
reliability, safety, and operator-burden tests.

## Deployment and operations

Define version compatibility, staged rollout, observability, alerting, kill switch,
incident ownership, rollback, change control, support, and retirement.

## Risks and implementation

| Risk or task | Owner | Mitigation or acceptance | Dependency | Due |
|---|---|---|---|---|
