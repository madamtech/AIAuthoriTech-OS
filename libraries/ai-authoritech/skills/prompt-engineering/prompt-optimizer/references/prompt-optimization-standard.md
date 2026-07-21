# Prompt Optimization Standard

## Diagnose before editing

Classify the dominant cause:

| Class | Typical evidence | Correct owner |
|---|---|---|
| Prompt | Ambiguous precedence, missing condition, conflicting instruction | Prompt owner |
| Model or adapter | Capability gap, parameter or structured-output mismatch | Platform owner |
| Knowledge or retrieval | Missing, stale, irrelevant, or poorly ranked context | Knowledge owner |
| Tool | Bad contract, permission, availability, response, or retry behavior | Tool owner |
| Data | Invalid, biased, incomplete, or unrepresentative inputs | Data owner |
| Workflow or product | Wrong sequencing, authority, UX, or human decision boundary | Product owner |
| Evaluation | Bad labels, leakage, weak rubric, or nonrepresentative cases | Evaluation owner |

Escalate non-prompt causes instead of encoding brittle workarounds.

## Experiment record

For each trial record:

- experiment ID, prompt versions, hypothesis, and changed factor;
- dataset and holdout versions, sampling rationale, and sensitive-data treatment;
- model, adapter, parameters, tool versions, knowledge snapshot, and run count;
- deterministic checks, rubric, graders, adjudication, and known limitations;
- task quality, hard-failure rate, schema adherence, safety, cost, and latency;
- per-segment results, variance, regressions, and disposition.

Use paired evaluation: run the baseline and candidate on identical cases and
controlled runtime conditions. Randomize presentation for human review when
practical. Keep the holdout unavailable during candidate authoring.

## Candidate techniques

Use only where the diagnosis supports them:

- remove contradiction, duplication, non-observable adjectives, or obsolete text;
- clarify precedence, scope, definitions, completion, escalation, and uncertainty;
- reorder instructions around the actual decision path;
- type, validate, delimit, and bound runtime variables;
- separate rules, reference data, examples, tool contracts, and user content;
- add minimal examples for a demonstrated boundary or format failure;
- tighten the output schema and explicit failure representation;
- move volatile knowledge out of stable instructions;
- create adapter-specific syntax without changing the canonical contract.

## Promotion gate

Promote only when all hard checks pass, the primary metric improves by the agreed
margin on holdout data, protected metrics remain above threshold, no critical
segment regresses, cost and latency remain within budget, and the result is
reproducible enough for the risk level. Otherwise retain the baseline, gather
more evidence, revise the hypothesis, or route the defect to its actual owner.

Use a canary or limited cohort for material production changes. Monitor the same
metrics used for promotion plus drift, novel failures, overrides, and rollback
conditions. Preserve exact baseline and candidate artifacts.
