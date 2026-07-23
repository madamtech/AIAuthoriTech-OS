---
name: agent-monitoring-and-optimization
description: Design and operate evidence-driven production monitoring and controlled optimization for AI agents across business outcomes, task quality, safety, security, permissions, tool effects, workflows, knowledge, reliability, latency, cost, adoption, incidents, drift, and lifecycle health. Use for observability plans, service-level objectives, production reviews, incident follow-up, drift detection, experiment design, cost optimization, or continuous improvement - not initial architecture, deployment execution, or untested autonomous self-modification.
---

# Agent Monitoring and Optimization

Monitor outcomes and controls end to end, then improve one attributable variable at
a time.

## Procedure

1. Identify the production version and configuration fingerprint, business outcome,
   risk and autonomy tier, users, traffic, operating hours, owners, dependencies,
   approved baseline, known limitations, and release guardrails.
2. Map the agent's critical user journeys and external effects. Define success,
   failure, harm, abandonment, escalation, and recovery for each journey.
3. Build the signal model with
   [references/agent-monitoring-standard.md](references/agent-monitoring-standard.md).
   Cover business value, task quality, grounding, authority, safety, tools,
   workflows, reliability, performance, cost, adoption, and operations.
4. Define service-level indicators, objectives, error budgets, measurement windows,
   segments, sampling, data quality checks, and accountable owners. Preserve
   separate hard gates for safety, privacy, security, and authorization.
5. Design logs, traces, metrics, evaluations, human-review samples, user feedback,
   audit evidence, dashboards, and alerts. Correlate a request across model calls,
   retrieval, tools, workflow state, approvals, and external effects.
6. Minimize telemetry data, redact sensitive content, enforce role-based access,
   define retention and deletion, and prevent observability systems from becoming
   an uncontrolled knowledge or prompt store.
7. Establish baselines by version, cohort, task, risk, model, tool, knowledge
   snapshot, and time. Detect quality, data, concept, instruction, model,
   retrieval, tool, workflow, cost, latency, and user-behavior drift.
8. Classify alerts by consequence and urgency. Define deduplication, suppression,
   escalation, kill-switch or degraded-mode actions, incident evidence, and
   recovery verification.
9. Diagnose the responsible layer before optimizing. Distinguish demand changes,
   instrumentation defects, upstream outages, configuration drift, regressions,
   model variance, and genuine improvement opportunities.
10. Create a prioritized improvement backlog using impact, evidence confidence,
    exposure, risk, effort, reversibility, and strategic value.
11. Form a falsifiable hypothesis, change one attributable factor where practical,
    predefine success and guardrail metrics, use bounded cohorts, and apply
    [references/agent-monitoring-standard.md](references/agent-monitoring-standard.md)
    to experiment and release decisions.
12. Re-run regression and safety evaluation before promotion. Version every change,
    monitor after release, compare with the baseline, and roll back when guardrails
    fail.
13. Deliver with
    [assets/agent-operations-review-template.md](assets/agent-operations-review-template.md).

## Guardrails

- Do not optimize proxy metrics at the expense of user outcomes or control
  effectiveness.
- Do not average away rare but severe safety, privacy, security, or authority
  failures.
- Do not infer quality from latency, cost, completion rate, or user engagement
  alone.
- Do not change prompts, models, knowledge, tools, permissions, workflows, or
  thresholds without versioning, review, evaluation, and rollback.
- Do not permit an agent to evaluate, approve, and deploy its own consequential
  optimization without independent human governance.
- Do not expose secrets or unnecessary sensitive content in telemetry, dashboards,
  alerts, or experiment data.
- Do not claim causal improvement from an uncontrolled before-and-after comparison.
- Separate provider-specific observability implementation from the
  platform-independent monitoring contract.

## Output Contract

Provide the production fingerprint, journey and signal map, SLI/SLO and error-budget
definitions, telemetry and privacy design, dashboards and alerts, drift and
incident model, current findings, improvement backlog, experiment plans, regression
gates, ownership, residual risks, and review cadence.

## Recovery

If telemetry quality is insufficient, repair measurement before claiming drift or
improvement. If a safety, privacy, security, or authority guardrail fails, contain
exposure and route incident handling before optimization. If causality is unclear,
return competing hypotheses and the smallest controlled experiment.
