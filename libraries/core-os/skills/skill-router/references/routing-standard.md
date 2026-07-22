# Routing Standard

## Route types

- `direct_response`: simple knowledge or explanation needs no registered capability.
- `single_skill`: one cohesive job maps to one skill.
- `multi_skill_sequence`: independent jobs can run in a defined order without shared control state.
- `workflow`: stages share state, branch, approve, retry, recover, or coordinate actors.
- `knowledge_lookup`: authoritative stored facts are the principal need.
- `tool_action`: the requested result is primarily a permitted tool operation.
- `skill_creation`: no capability exists and a reusable procedural gap is confirmed.
- `skill_review`: the user requests evaluation or maturity approval.
- `human_escalation`: judgment, authority, or access must come from a person.
- `unsupported`: no safe available route can satisfy the outcome.

## Candidate scoring

Score only evidence:

- Outcome fit: 0-35
- Input/output compatibility: 0-20
- Domain and business fit: 0-15
- Access and authorization: 0-15
- Dependency readiness: 0-10
- Duplication avoidance: 0-5

Reject a candidate before scoring when it is unavailable, deprecated, inaccessible, or incapable of the requested output.

## Ambiguity

Ask one question only if different answers would select materially different routes. Otherwise choose the safest provisional route and label assumptions.

## Cross-business routing

Do not route i-PRO or MadamAllure proprietary knowledge into generic AI AuthoriTech work unless reuse is explicitly permitted. Shared Core OS assets may serve every business.
