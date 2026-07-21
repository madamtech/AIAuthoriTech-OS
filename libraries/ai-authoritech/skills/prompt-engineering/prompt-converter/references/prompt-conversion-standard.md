# Prompt Conversion Standard

## Capability mapping

Assess exact source and target versions across:

| Area | Questions |
|---|---|
| Authority | Which roles exist, who controls them, and how are conflicts resolved? |
| Context | What limits, truncation, caching, retrieval, and persistence apply? |
| Variables | How are runtime values typed, delimited, validated, and escaped? |
| Outputs | Is schema enforcement native, best-effort, or external? |
| Tools | How are definitions, approvals, side effects, errors, and results represented? |
| Safety | Which controls are platform-enforced versus prompt-dependent? |
| Runtime | Which parameters, modalities, streaming, and concurrency behaviors differ? |
| Operations | How are versions, logs, costs, latency, monitoring, and rollback handled? |

Classify each feature:

- **Direct:** Equivalent native construct with tested behavior.
- **Mapped:** Different construct that preserves observable behavior.
- **Emulated:** External validation or orchestration is required.
- **Unsupported:** Target cannot preserve the protected behavior.
- **Unknown:** Documentation or evidence is insufficient.

## Semantic preservation

Trace every protected requirement from the canonical contract to the adapter,
runtime control, and equivalence test. A textual similarity score is not semantic
evidence. Compare observable decisions, outputs, tool effects, failure states,
authority boundaries, and segment performance.

Block release if conversion weakens a critical safety, privacy, authorization,
truthful-status, destructive-action, or mandatory-schema invariant. Mark partial
parity when an external control preserves behavior but changes deployment needs.

## Adapter lifecycle

Give each adapter its own ID and version while referencing the canonical prompt
version and compatible range. Re-evaluate when the canonical prompt, target model,
provider behavior, API version, SDK, tool schema, knowledge interface, safety
policy, context limit, or structured-output mechanism changes. Preserve the last
approved adapter and exact target configuration for rollback.
