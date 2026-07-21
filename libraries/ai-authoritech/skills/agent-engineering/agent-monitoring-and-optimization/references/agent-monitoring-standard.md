# Agent Monitoring Standard

## Signal hierarchy

| Layer | Example measures |
|---|---|
| Business outcome | Cycle time, resolution, conversion, avoided effort, value realized |
| User outcome | Task success, correction, abandonment, escalation, satisfaction |
| Quality | Accuracy, completeness, groundedness, citation quality, uncertainty |
| Authority and safety | Unauthorized attempts or effects, approval compliance, refusals, leakage, harmful output |
| Knowledge and memory | Retrieval relevance, freshness, access-filter failures, memory errors |
| Tools and workflows | Tool success, argument validity, verified effects, retries, duplicates, stuck states, compensation |
| Reliability | Availability, end-to-end success, timeouts, recovery, dependency health |
| Performance and cost | End-to-end and stage latency, tokens, tool cost, spend, capacity |
| Operations | Alert quality, detection time, mitigation time, rollback success, support load |

Use leading and lagging indicators. Pair every efficiency metric with outcome and
risk guardrails.

## Measurement contract

For every measure define:

- Name, purpose, formula, unit, source, and owner
- Included and excluded events
- Version, cohort, journey, risk, and time dimensions
- Target, warning, critical, and rollback thresholds
- Measurement window, minimum sample, and confidence treatment
- Data-quality validation, late-event handling, and retention
- Response action and escalation path

Use rates with denominators, not isolated counts. Report uncertainty when samples
are small or human labels are inconsistent.

## Hard gates and error budgets

Safety, privacy, security, authorization, and irreversible external effects are
hard gates where consequence demands it. Do not convert them into ordinary error
budgets.

Use error budgets for service objectives where bounded failure is acceptable.
When a budget is exhausted, pause risky releases and prioritize reliability until
the service returns within policy.

## Drift classes

- **Input drift:** User requests, populations, languages, files, or traffic change.
- **Concept drift:** The correct outcome or real-world relationship changes.
- **Knowledge drift:** Sources become stale, missing, inconsistent, or inaccessible.
- **Behavior drift:** Instructions, model, parameters, tools, or workflows change
  observed behavior.
- **Control drift:** Permissions, approvals, logging, filters, or guardrails weaken.
- **Economic drift:** Latency, token use, provider rates, or tool cost changes.
- **Instrumentation drift:** Telemetry changes without an underlying system change.

Compare like-for-like cohorts and verify instrumentation before diagnosing the
agent.

## Incident levels

- **Critical:** Active severe harm, data exposure, unauthorized consequential
  action, security bypass, or uncontrolled irreversible effects. Contain
  immediately.
- **High:** Core service or control failure with material exposure. Stop or reduce
  affected operation and escalate urgently.
- **Medium:** Material degradation with a viable workaround or limited exposure.
- **Low:** Localized defect or improvement opportunity without material risk.

Record detection, acknowledgment, containment, correction, recovery, verification,
root cause, contributing controls, and prevention work.

## Optimization experiment

Require:

1. Baseline and reproducible problem statement
2. Hypothesis and one attributable intervention where practical
3. Primary outcome, guardrails, minimum sample, and decision rule defined in advance
4. Representative and ethically appropriate cohort assignment
5. Versioned candidate and rollback
6. Regression, safety, authority, and external-effect evaluation
7. Monitoring for novelty and delayed harms
8. Promote, iterate, reject, or roll back decision with evidence

Never ship an improvement that raises the primary metric while breaching a hard
gate or material guardrail.
