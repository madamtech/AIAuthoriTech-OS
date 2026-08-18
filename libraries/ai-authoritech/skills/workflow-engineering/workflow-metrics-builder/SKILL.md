---
name: workflow-metrics-builder
description: Define decision-ready workflow metrics for outcomes, demand, quality, cycle and wait time, throughput, capacity, queues, rework, exceptions, controls, user experience, cost, and equity with exact formulas, sources, owners, segments, thresholds, and action rules. Use before dashboards or optimization. Do not create vanity metrics or incentives that reward harmful gaming. Use when asked to (1) build workflow metrics, (2) refine workflow metrics, (3) validate workflow metrics, or (4) standardize workflow metrics.
---

# Workflow Metrics Builder

Use the [workflow metrics standard](references/workflow-metrics-standard.md) and record formulas and action rules in the [workflow metric dictionary template](assets/workflow-metric-dictionary-template.md).

## Procedure

1. Define business outcome, decisions, users, workflow boundaries, baseline, and controllable actions.
2. Select balanced outcome, process, quality, control, capacity, experience, cost, and risk measures.
3. Specify numerator, denominator, timestamps, exclusions, units, segments, source, latency, and owner.
4. Distinguish touch, wait, cycle, queue, throughput, work in progress, first-pass yield, and failure demand.
5. Set evidence-based targets, thresholds, alerts, review cadence, and required actions.
6. Test data completeness, lineage, duplicates, clock logic, bias, small samples, and reconciliation.
7. Review incentives and guardrails to prevent speed, volume, or automation rate from degrading outcomes.
8. Deliver metric dictionary, lineage, baseline, targets, segments, controls, dashboard requirements, and caveats.

## Guardrails
- Do not report averages without tails and meaningful segments where harm can hide.
- Do not count reopened or reworked items as new successful throughput.
- Do not use proxy measures without validating their relationship to the outcome.
- Do not expose individual performance or sensitive attributes without authorization.

## Recovery

If lineage, completeness, clock logic, reconciliation, sample size, or outcome validity fails, withdraw the affected metric from decision use. Preserve the raw evidence, label historical displays, correct and backfill only with owner approval, and revalidate incentives before reinstatement.

## Output Contract

Deliver a metric dictionary with exact formulas, timestamps, exclusions, units, segments, lineage, owners, baselines, targets, thresholds, actions, quality tests, incentive guardrails, dashboard requirements, and caveats.
