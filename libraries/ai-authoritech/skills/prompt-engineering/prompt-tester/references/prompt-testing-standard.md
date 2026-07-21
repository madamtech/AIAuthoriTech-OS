# Prompt Testing Standard

## Test layers

| Layer | Purpose | Examples |
|---|---|---|
| Contract | Verify exact invariants | Schema, required field, refusal, citation |
| Capability | Measure task performance | Accuracy, extraction, classification, usefulness |
| Robustness | Expose unstable behavior | Paraphrase, ordering, length, malformed input |
| Safety and authority | Test protected boundaries | Injection, privacy, prohibited tool use, escalation |
| Operations | Measure service constraints | Cost, latency, timeout, tool and adapter failure |
| Regression | Protect approved behavior | Paired baseline-versus-candidate cases |

## Case contract

Give each case a stable ID and version. Record source and consent or synthetic
method, intended segment, risk and severity, prompt-visible input, hidden grading
data, environment requirements, exact assertions, allowed answer variation,
rubric criteria, and failure classification. Use sanitized fixtures that retain
the properties needed for the test.

Split cases before optimization. Development cases may guide diagnosis. Regression
cases protect known behavior. Holdout cases remain inaccessible until the final
decision. Track duplicates and near-duplicates across splits.

## Grading hierarchy

1. Treat execution errors and missing outputs as failures, not exclusions.
2. Run deterministic assertions where an exact observable condition exists.
3. Use reference-based grading when a bounded correct answer is available.
4. Use anchored rubrics for judgment with examples at the boundaries.
5. Require human adjudication for material disagreement or high-risk decisions.

For automated model graders, pin the grader prompt, model, parameters, and version;
test grader consistency; keep the grader isolated from candidate identity; and
sample results for human calibration. A model grader is evidence, not ground truth.

## Reporting and gates

Report counts and rates for passed, failed, errored, skipped, excluded, and
ungraded cases. Show results by requirement and meaningful segment with critical
failure details. Include repeated-run pass consistency, confidence or variance,
cost, latency, and the exact denominator.

Apply hard gates before aggregate thresholds. A critical privacy, authority,
safety, truthful-status, destructive-action, or mandatory-schema failure blocks
promotion even when the average score improves. Mark the outcome inconclusive
when coverage, sample size, label quality, grader reliability, or environmental
control is insufficient for the requested decision.

Archive the prompt, suite, environment manifest, raw outputs, tool traces, grader
versions, results, and decision together so another authorized tester can rerun
the evaluation.
