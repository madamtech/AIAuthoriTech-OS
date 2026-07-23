---
name: prompt-optimizer
description: Diagnose and improve existing production prompts through baseline measurement, failure classification, controlled candidate changes, representative evaluation, regression testing, and versioned rollout. Use when a prompt underperforms on quality, reliability, safety, format adherence, cost, latency, or portability and the task and authority contract already exist. Do not use to invent the original prompt architecture, mask product or retrieval defects, or approve an untested rewrite.
---

# Prompt Optimizer

Improve measured behavior while preserving the approved contract.

## Procedure

1. Obtain the canonical prompt, version, owner, task contract, instruction layers,
   variables, tools, output schema, adapters, parameters, and current evaluation
   evidence. Route missing architecture to Prompt Architect.
2. Define the optimization target and guardrails: primary metrics, minimum
   thresholds, protected behaviors, acceptable regressions, cost and latency
   budgets, supported models, and rollout constraints.
3. Reproduce the baseline on a versioned representative dataset. Use repeated
   runs where model variance matters and record model, adapter, parameters,
   tools, knowledge snapshot, and environment.
4. Classify each failure before editing. Separate prompt defects from model,
   tool, retrieval, knowledge, data, workflow, product, policy, and evaluation
   defects. Do not rewrite the prompt to conceal a non-prompt cause.
5. Form explicit hypotheses that connect an observed failure to a bounded change
   and a predicted metric effect. Rank hypotheses by expected value, risk, and
   test cost.
6. Produce candidate variants by changing one factor at a time when practical.
   Preserve task, authority, prohibited actions, tool permissions, output schema,
   and protected decisions unless their owner authorizes a change.
7. Prefer precise deletion, reordering, conditions, delimiters, typed variables,
   and examples over added verbosity. Remove conflicting, redundant, vague, and
   non-observable instructions.
8. Evaluate baseline and candidates using the same cases and scoring. Include
   normal, boundary, missing, conflicting, adversarial, injection, privacy,
   schema, tool-failure, long-input, and supported-adapter cases as applicable.
9. Apply deterministic checks before rubric judgment. Track per-case outcomes,
   aggregate metrics, variance, cost, latency, safety violations, and regressions.
   Keep failed and neutral trials; do not cherry-pick examples or runs.
10. Test the leading candidate on a holdout set not used to form hypotheses.
    Compare confidence intervals or repeated-run distributions when stochastic
    variation could explain the apparent gain.
11. Reject a candidate that violates a hard guardrail, moves a protected metric
    below threshold, improves only the tuning set, or lacks enough evidence to
    distinguish improvement from noise.
12. Create a semantic version, prompt diff, experiment record, compatibility
    statement, rollout cohort, monitoring signals, rollback trigger, and rollback
    artifact. Re-evaluate every supported adapter affected by the change.
13. Deliver the approved candidate and evidence using
    [assets/prompt-optimization-report-template.md](assets/prompt-optimization-report-template.md).
    Use [references/prompt-optimization-standard.md](references/prompt-optimization-standard.md)
    for failure classes, experiment design, and promotion rules.

## Guardrails

- Do not define "better" without measurable acceptance and regression criteria.
- Do not compare candidates across different datasets, parameters, tools, or
  knowledge snapshots unless the experiment explicitly controls that variable.
- Do not optimize from one example, one run, synthetic happy paths, or reviewer
  preference alone.
- Do not expose or request hidden chain-of-thought; evaluate conclusions,
  evidence, observable checks, and tool traces appropriate to the task.
- Do not place secrets, personal records, or confidential production payloads in
  prompts, fixtures, reports, or logs. Use sanitized representative cases.
- Do not weaken safety, authority, privacy, citation, or truthful-status rules to
  improve superficial task scores.
- Do not deploy silently. Preserve the baseline and provide a tested rollback.

## Recovery

If the baseline cannot be reproduced, a candidate violates a hard guardrail, or
results do not distinguish improvement from variance, reject promotion and keep
the validated baseline. Preserve failed trials, isolate non-prompt causes, and
roll back any staged candidate whose monitored behavior crosses a defined
threshold.

## Output Contract

Provide the baseline specification, target metrics and guardrails, failure
taxonomy, hypotheses, candidate diffs, evaluation dataset and scoring method,
per-candidate results, holdout evidence, selected version, rejected variants,
adapter compatibility, rollout and monitoring plan, rollback trigger, risks,
assumptions, and unresolved decisions.
