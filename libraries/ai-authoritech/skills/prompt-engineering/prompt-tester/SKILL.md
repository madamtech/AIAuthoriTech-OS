---
name: prompt-tester
description: Design, execute, and report reproducible evaluations for canonical prompts and prompt candidates using representative datasets, deterministic assertions, calibrated rubrics, repeated runs, adversarial cases, segment analysis, and regression gates. Use to establish a prompt baseline, validate an optimization, compare versions or adapters, investigate failures, or decide whether a prompt can advance. Do not use to author the prompt contract, optimize from test leakage, or certify production readiness beyond the evidence tested. Use when asked to (1) create prompt tester, (2) review prompt tester, (3) improve prompt tester, or (4) standardize prompt tester.
---

# Prompt Tester

Produce decision-grade evidence about observable prompt behavior.

## Procedure

1. Obtain the canonical prompt and version, task and authority contract, variables,
   output schema, tools, adapters, parameters, knowledge snapshot, risk class,
   supported users, and intended release decision. Route missing architecture to
   Prompt Architect and requested rewrites to Prompt Optimizer.
2. Translate each requirement into an observable behavior, deterministic
   assertion, rubric criterion, operational metric, or explicit non-testable
   limitation. Do not treat vague quality language as a pass condition.
3. Define the evaluation population and meaningful segments. Assemble sanitized,
   representative cases from approved sources; cover normal, boundary, missing,
   contradictory, malformed, long, multilingual, adversarial, injection,
   privacy, tool-failure, and refusal or escalation behavior as applicable.
4. Assign stable case IDs, provenance, purpose, input variables, trusted context,
   untrusted content, expected invariants, allowed variation, grader, severity,
   and tags using
   [references/prompt-testing-standard.md](references/prompt-testing-standard.md).
5. Separate development, regression, and holdout sets. Prevent test cases,
   expected answers, labels, or grader rationales from leaking into the prompt,
   retrieval corpus, optimizer context, or model input.
6. Pin the evaluation environment: prompt and adapter versions, model, parameters,
   tool and schema versions, knowledge snapshot, locale, time assumptions, and
   run count. Record any uncontrolled variables.
7. Run deterministic checks first for schema, required fields, allowed values,
   citations, unsupported claims, privacy, tool effects, truthful status, and
   latency or cost boundaries.
8. Use rubric grading only for qualities requiring judgment. Define anchored
   score levels, evidence requirements, critical failures, weighting, and
   adjudication. Blind or randomize comparative review when practical.
9. Repeat stochastic cases enough to measure instability for the risk level.
   Retain every run, timeout, refusal, tool error, and invalid output; never rerun
   selectively to replace an unfavorable result.
10. Calculate case, requirement, segment, and overall results. Report numerator,
    denominator, exclusions, confidence or variance, cost, latency, failure
    severity, and sample limitations, not only a single aggregate score.
11. Compare versions with paired cases and equivalent runtime conditions. Mark
    regressions explicitly and apply predefined hard gates before weighted gains.
12. Investigate grader disagreement, flaky cases, suspiciously perfect results,
    leakage, data imbalance, ambiguous labels, and environment drift. Quarantine
    invalid cases without deleting their audit history.
13. Classify the decision as pass, conditional pass, fail, or inconclusive.
    Never infer untested models, languages, tools, populations, or production
    conditions from a narrower evaluation.
14. Deliver the suite and report using
    [assets/prompt-test-suite-template.md](assets/prompt-test-suite-template.md),
    including exact artifacts, failures, coverage gaps, rerun instructions, and
    the next authorized action.

## Guardrails

- Do not use live secrets, personal records, confidential payloads, or destructive
  tool actions in fixtures. Sanitize data and use isolated test environments.
- Do not let the prompt under test see expected outputs, grader instructions,
  hidden labels, holdout cases, or pass thresholds unless they are part of the
  approved production contract.
- Do not use hidden chain-of-thought as an expected result or grading input;
  evaluate final answers, evidence, structured fields, and observable traces.
- Do not change the prompt, labels, rubric, or dataset during a comparison without
  creating a new version and rerunning the affected baseline.
- Do not collapse a hard safety, authority, privacy, or schema failure into an
  average score.
- Do not report excluded, skipped, errored, or ungraded cases as passes.
- Do not call an evaluation independent when its author also generated the test
  cases, candidate, expected results, and final judgment without review.

## Recovery

If environment drift, leakage, invalid cases, grader disagreement, or missing raw
evidence prevents a fair decision, quarantine the affected results without
deleting history and classify the outcome inconclusive. Restore the pinned
baseline, correct the evaluation design, and rerun every affected comparison
under equivalent conditions.

## Output Contract

Provide scope and decision, environment manifest, requirement traceability,
versioned case inventory and split policy, deterministic checks, rubric and
grader controls, raw run references, aggregate and segment results, critical
failures, regressions, variance, cost and latency, exclusions, leakage review,
coverage limitations, disposition, rerun procedure, and recommended next action.
