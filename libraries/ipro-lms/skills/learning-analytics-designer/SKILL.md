---
name: learning-analytics-designer
description: Design trustworthy learning analytics that connect operational learning data to defined business questions, outcomes, measures, dimensions, cohorts, privacy controls, and decision workflows. Use when creating KPI frameworks, dashboards, scorecards, or evaluation plans. Use when asked to (1) design learning analytics, (2) revise learning analytics, (3) compare options for learning analytics, or (4) document specifications for learning analytics.
---

# Learning Analytics Designer

Use the [operating standard](references/learning-analytics-standard.md) and [working template](assets/learning-analytics-template.md).

Design measures that support decisions rather than dashboards that merely display available data.

## Procedure

1. Define the decision, stakeholders, intended actions, target outcomes, learner populations, and reporting cadence.
2. Create a measurement model spanning activity, reach, completion, quality, learning, application, and business outcomes as evidence permits.
3. Define every metric's numerator, denominator, grain, filters, time window, timezone, exclusions, source, owner, and refresh rate.
4. Map dimensions and cohorts while checking sample size, selection effects, confounders, and privacy risk.
5. Specify data quality, reconciliation, lineage, access, retention, and suppression controls.
6. Design dashboard hierarchy, thresholds, annotations, drilldowns, alerts, and action ownership.
7. Validate calculations against known cases and document limitations and interpretation rules.

## Output Contract

Provide a decision-to-metric map, KPI dictionary, source/lineage matrix, dashboard specification, privacy controls, validation plan, interpretation guidance, and governance cadence.

## Guardrails

- Do not claim causation without an appropriate design.
- Avoid vanity metrics and undefined percentages.
- Suppress or aggregate sensitive small cohorts.
- Keep operational completion measures distinct from performance outcomes.

## Recovery

If the decision question, population, metric definition, source lineage, privacy threshold, benchmark, reconciliation, or causal limitation is unresolved, publish only qualified descriptive results. Do not use them for individual performance decisions.
