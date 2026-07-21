---
name: prompt-converter
description: Convert an approved canonical prompt contract into versioned model-, API-, agent-, workflow-, or platform-specific adapters while preserving task semantics, instruction authority, variables, tool permissions, output schemas, safety controls, uncertainty behavior, and observable acceptance criteria. Use when migrating or porting prompts across providers, models, SDKs, structured-output modes, custom-agent builders, or automation platforms. Do not translate an undefined prompt, silently redesign behavior, claim universal portability, or approve an adapter without equivalence testing.
---

# Prompt Converter

Create a target adapter, not an ungoverned rewrite.

1. Obtain the approved canonical prompt contract, version, owner, task and
   non-goals, instruction layers, precedence, variables, knowledge interfaces,
   tool contracts, output schema, safety rules, test suite, and baseline evidence.
   Route missing architecture to Prompt Architect.
2. Define the source and target environment precisely: provider, product, model,
   API or UI surface, SDK, message roles, tool syntax, structured-output support,
   context limits, parameters, modalities, streaming, persistence, and policy.
3. Build a capability-difference matrix using
   [references/prompt-conversion-standard.md](references/prompt-conversion-standard.md).
   Classify each feature as direct, mapped, emulated, unsupported, or unknown.
4. Freeze protected semantics: authorized task, prohibited actions, authority
   order, trust boundaries, required inputs, allowed decisions, completion,
   escalation, failure representation, tool permissions, and output invariants.
5. Map instruction layers to the target's actual authority model. Never place
   privileged rules into a lower-authority field merely because the target lacks
   an equivalent role; document the limitation or block conversion.
6. Map typed variables and runtime context. Preserve source, trust, sensitivity,
   validation, delimiters, missing-value behavior, and size limits. Do not embed
   secrets or volatile knowledge in the converted prompt.
7. Translate tool definitions, schemas, approvals, side effects, retry behavior,
   and truthful-status rules to native target constructs. Do not simulate tool
   authority with prose when enforcement is required.
8. Translate structured outputs with the strongest supported enforcement. When
   exact schema enforcement is unavailable, add validation and retry outside the
   prompt and mark behavioral parity as partial.
9. Adapt examples, delimiters, formatting, token budgets, and parameters only as
   needed for target syntax and capability. Keep examples data-only and prevent
   target-specific syntax from changing canonical meaning.
10. Produce a requirement-by-requirement mapping and an explicit semantic diff.
    Label intentional, unavoidable, and prohibited drift. Obtain owner approval
    for any intentional contract change before continuing.
11. Run the canonical regression suite against source and target under equivalent
    conditions. Add target-specific cases for role handling, tool calls, schemas,
    truncation, streaming, refusals, and unsupported features.
12. Compare observable results by requirement and segment, including safety,
    privacy, authority, schema, cost, latency, and repeated-run consistency. Route
    tuning to Prompt Optimizer and evaluation gaps to Prompt Tester.
13. Assign an adapter ID and semantic version. Record canonical dependency,
    compatibility range, target configuration, limitations, test evidence,
    release boundary, monitoring, re-evaluation triggers, and rollback artifact.
14. Deliver with [assets/prompt-conversion-package-template.md](assets/prompt-conversion-package-template.md).

## Rules

- Do not use provider names, model labels, or platform marketing as evidence of
  capability; verify the exact target version and surface.
- Do not flatten instruction roles or trust levels without documenting and
  testing the authority consequence.
- Do not broaden tool access, data access, autonomy, persistence, or allowed
  decisions during conversion.
- Do not discard required failure states, citations, assumptions, approvals, or
  schema fields to fit a target limitation without owner authorization.
- Do not expose credentials, personal records, confidential examples, hidden
  test labels, or private reasoning in adapter artifacts.
- Do not call the adapter equivalent when protected behavior is unsupported,
  untested, or materially degraded. Use partial, blocked, or inconclusive.
- Do not overwrite the canonical prompt; adapters depend on it and remain
  separately versioned.

## Handoff

Provide source and target manifests, capability matrix, protected semantics,
instruction and variable mappings, tool and schema mappings, converted adapter,
semantic diff, unsupported or emulated features, equivalence test results,
cost and latency impact, compatibility, limitations, version metadata, rollout,
monitoring, re-evaluation triggers, rollback, risks, and open decisions.
