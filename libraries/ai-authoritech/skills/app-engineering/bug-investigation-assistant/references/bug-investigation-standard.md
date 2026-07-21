# Bug Investigation Standard

## Evidence states

Label every important statement:

- **Fact:** directly supported by retained evidence.
- **Observation:** reported or witnessed but not independently verified.
- **Interpretation:** a meaning assigned to evidence.
- **Assumption:** temporarily accepted to continue.
- **Contradiction:** incompatible observations or sources exist.
- **Unknown:** required evidence is absent.

Preserve source, timestamp, environment, version, and collection method.

## Safe reproduction

A reproduction must define:

- clean preconditions and authoritative seed state;
- exact input and action sequence;
- expected and observed result;
- frequency and timing;
- environment, identity, version, configuration, and dependencies;
- correlation identifiers and evidence capture;
- external effects, containment, cleanup, and reset.

Prefer local, test, preview, sandbox, replay, read-only, or mocked environments.
Use production only when explicitly authorized and when blast radius, privacy,
recovery, monitoring, and abort conditions are controlled.

## Layer isolation

Trace the same transaction or state across boundaries. At each boundary ask:

1. What input entered?
2. Which identity and authorization applied?
3. Which version and configuration processed it?
4. What output or state change occurred?
5. Where is the authoritative evidence?

The first divergence is not automatically the root cause, but it sharply narrows
the search.

## Hypothesis matrix

Each hypothesis needs:

- causal statement;
- supporting and conflicting evidence;
- predicted observation if true;
- predicted observation if false;
- one-variable discriminating test;
- safety and cleanup;
- result and confidence change.

Prefer tests that distinguish several plausible causes without changing live
state. Reject hypotheses when predictions fail; do not preserve them through
post-hoc explanation.

## Causal chain

Document separately:

- **Trigger:** event that exposed the defect.
- **Defective condition:** incorrect code, state, contract, configuration, or
  process.
- **Root cause:** why the defective condition existed.
- **Contributors:** factors that increased likelihood or impact.
- **Control failure:** why tests, validation, monitoring, rollout, or recovery did
  not prevent or contain it.
- **Symptom:** what users or systems observed.

Avoid “human error” as a stopping point. Identify the system conditions that made
the action possible and undetected.

## Confidence

- **Confirmed:** direct evidence or controlled reproduction establishes causality.
- **Strongly supported:** converging evidence with no material contradiction.
- **Plausible:** evidence is compatible but a discriminating test remains.
- **Weak:** limited support or substantial alternatives.
- **Unknown:** evidence is insufficient.

State what evidence would raise or lower confidence.

## Verification

For an authorized fix:

- create a regression that demonstrates the defect before the change;
- apply the smallest controlled change;
- rerun reproduction and adjacent boundary tests;
- inspect authoritative data and external effects;
- compare performance, security, accessibility, and compatibility;
- monitor the original signal and control-failure indicators;
- preserve rollback or forward-fix capability.
