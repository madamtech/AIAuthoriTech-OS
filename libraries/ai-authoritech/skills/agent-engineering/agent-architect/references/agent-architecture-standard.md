# Agent architecture standard

## Agent-necessity test

Use an agent only when the job materially benefits from context-dependent reasoning,
dynamic planning, uncertain tool selection, or adaptive recovery. Prefer:

- direct response for one-shot knowledge work
- deterministic code for stable calculations or transformations
- workflow orchestration for known steps and branches
- ordinary application logic for fixed business rules

## Autonomy tiers

- 0 advise only
- 1 draft for human review
- 2 execute reversible low-impact actions within explicit bounds
- 3 execute broader actions with pre-action approvals or policy gates
- 4 high autonomy in a tightly controlled domain with strong evidence and oversight

Tier 4 is not a default target.

## Required contracts

- purpose and non-goals
- users and affected parties
- authority and approval matrix
- workflow, state, and handoff schema
- tool permission and credential model
- knowledge provenance and freshness
- memory purpose, retention, deletion, and isolation
- error, retry, idempotency, compensation, and safe-stop behavior
- evaluation, monitoring, incident, rollback, and retirement ownership
