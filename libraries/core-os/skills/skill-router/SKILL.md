---
name: skill-router
description: Route a request to an existing skill, multi-skill sequence, registered workflow, direct response, knowledge lookup, tool action, skill creation, skill review, human escalation, or unsupported outcome. Use when capability selection is ambiguous or duplicate creation must be prevented.
---

# Skill Router

Select the smallest sufficient route.

1. Parse outcome, deliverable, constraints, domain, and action level.
2. Search catalog triggers, business, library, inputs, outputs, and relationships.
3. Remove candidates lacking required access or capability.
4. Prefer direct response for simple knowledge; one skill for one cohesive job;
   a sequence for independent jobs; a workflow for shared state, branches,
   approvals, retries, or recovery.
5. Score outcome fit 35, I/O fit 20, domain 15, access 15, dependencies 10,
   duplication avoidance 5.
6. Return route, confidence, rationale, inputs, dependencies, and fallback.

At 90+ route automatically; 75–89 state assumptions; 60–74 use a provisional
route and ask one question only if material; below 60 do not auto-route. Never
claim an unavailable capability exists.
