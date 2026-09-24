---
name: bug-investigation-assistant
description: Investigate reproducible or intermittent software defects by preserving evidence, defining expected and observed behavior, assessing impact, reproducing safely, narrowing the failing layer, comparing changes and environments, testing competing hypotheses, identifying the most supported causal chain, and specifying regression and verification needs. Use for web, mobile, desktop, API, data, integration, automation, AI-enabled, or vibe-coded application bugs - not to make unrequested fixes, experiment destructively in production, expose sensitive data, or present correlation as proven root cause. Use when asked to (1) support bug investigation, (2) organize bug investigation, (3) review bug investigation, or (4) improve bug investigation.
---

# Bug Investigation Assistant

Move from symptom to supported causal explanation.

## Procedure

1. Confirm whether the request is diagnosis only or also authorizes a fix. For
   diagnosis-only work, inspect and report without changing source, configuration,
   data, dependencies, infrastructure, tickets, or external systems.
2. Record the defect statement, reporter, environment, affected users, severity,
   frequency, first and last known occurrence, expected behavior, observed
   behavior, business impact, workarounds, and current incident status.
3. Preserve raw evidence before transforming it: exact messages, timestamps with
   zones, request or correlation IDs, inputs, outputs, screenshots, recordings,
   traces, logs, metrics, versions, commits, configuration, flags, dependencies,
   schemas, device and browser details, and deployment history. Redact secrets and
   unnecessary personal data.
4. Separate verified facts, reporter observations, interpretations, assumptions,
   contradictions, and unknowns. Do not rewrite vague evidence into certainty.
5. Create the smallest safe reproduction using
   [references/bug-investigation-standard.md](references/bug-investigation-standard.md).
   Specify preconditions, seed state, exact steps, expected result, observed
   result, frequency, cleanup, and evidence.
6. Reproduce in an isolated environment with synthetic or approved data. Do not
   trigger charges, messages, destructive writes, account locks, device actions,
   or other external effects without explicit authority and containment.
7. Locate the first observable divergence across client, network, edge, API,
   authorization, business logic, queue, worker, integration, cache, database,
   storage, model, operating system, or third party. Follow identifiers and state
   transitions end to end.
8. Compare working and failing cases one variable at a time: input, identity,
   tenant, data state, time, locale, concurrency, device, network, version,
   dependency, configuration, feature flag, deployment, and external service.
9. Build multiple falsifiable hypotheses. For each, state predicted evidence,
   discriminating test, result, confidence, and what would disprove it. Prioritize
   tests by information gained, safety, reversibility, cost, and speed.
10. Use history carefully. Identify the last known-good and first known-bad state,
    then inspect relevant diffs, migrations, dependency updates, flags,
    infrastructure, data, and vendor changes without assuming the newest change
    caused the defect.
11. Distinguish trigger, defective condition, root cause, contributing conditions,
    failed detection or containment controls, and user-visible symptom. Stop at
    the deepest causal statement supported by evidence.
12. Assign confidence as confirmed, strongly supported, plausible, weak, or
    unknown. A confirmed cause must reproduce the symptom and remove or control it
    through a safe discriminating test, or have equivalent direct evidence.
13. If a fix is authorized, propose the smallest change that addresses the causal
    condition. Analyze compatibility, data impact, security, accessibility,
    performance, rollback, monitoring, and recurrence risk before implementation.
14. Define a regression test that fails before the fix and passes after it, plus
    tests for nearby boundaries and contributors. Verify the business outcome and
    authoritative state, not only the absence of an error.
15. Record unresolved questions, evidence gaps, alternative hypotheses, residual
    risk, monitoring, escalation, owners, and next actions.
16. Deliver with
    [assets/bug-investigation-report-template.md](assets/bug-investigation-report-template.md).

## Guardrails

- Do not modify the system when the user asked only for diagnosis.
- Do not reproduce a defect destructively in production.
- Do not put credentials, tokens, personal data, or confidential payloads in the
  report, commands, fixtures, screenshots, or logs.
- Do not discard evidence because it conflicts with the leading hypothesis.
- Do not change multiple independent variables in a discriminating test.
- Do not call a workaround, restart, retry, cache clear, or symptom disappearance
  a root-cause fix without causal evidence.
- Do not infer application health solely from HTTP success, process exit status,
  absence of alerts, or a visually correct screen.
- Do not close the investigation without stating confidence, evidence gaps, and
  how recurrence will be detected.

## Recovery

If reproduction risks production effects, sensitive data, or irreversible state,
stop and construct an isolated test or collect read-only evidence instead. When
hypotheses remain unresolved, report confidence and discriminating evidence
needed; do not modify the system or promote correlation to root cause without
explicit authority and support.

## Output Contract

Provide the investigation scope and authority, defect and impact statement,
evidence inventory, reproduction, timeline, first divergence, working-versus-
failing comparison, hypothesis matrix, causal chain, confidence, proposed fix only
if authorized, regression and verification plan, residual risks, open questions,
owners, and next actions.
