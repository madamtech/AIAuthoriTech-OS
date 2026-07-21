---
name: prompt-qa-reviewer
description: Independently review a prompt package for contract completeness, instruction integrity, authority and trust boundaries, test adequacy, evidence quality, adapter compatibility, operational controls, and release readiness. Use after prompt architecture and testing, before approval, rollout, marketplace packaging, or a material version promotion. Return evidence-linked defects and an approve, approve-with-conditions, reject, or inconclusive verdict. Do not author the prompt, execute the primary test suite, or approve based on documentation alone.
---

# Prompt QA Reviewer

Review the package independently and make evidence traceable.

1. Confirm the review scope, requested release decision, risk class, owner,
   approver, independence requirements, applicable policies, supported adapters,
   and evidence cutoff. Disclose conflicts of interest.
2. Inventory the canonical prompt, architecture contract, source and trust map,
   variables, examples, schema, tools, adapters, test suite, raw results, optimizer
   experiments, version history, rollout, monitoring, and rollback artifacts.
3. Verify artifact identity and provenance. Reject mismatched versions, missing
   hashes or references, stale evidence, undocumented changes, or results produced
   against a different prompt, model, adapter, tool, schema, or knowledge snapshot.
4. Trace every approved requirement and prohibited behavior to prompt instructions,
   tests, evidence, and an accountable owner. Mark absent, ambiguous, conflicting,
   or untested requirements.
5. Review instruction precedence, authority, untrusted-content treatment, data
   boundaries, tool permissions, uncertainty, escalation, output contract, and
   truthful completion. Identify paths that let content or examples override rules.
6. Review the test design for population coverage, meaningful segments, split
   integrity, leakage, deterministic assertions, rubric anchors, grader calibration,
   repeated runs, adversarial cases, exclusions, denominators, and holdout evidence.
7. Recalculate a sample of reported results from raw evidence. Reproduce critical
   failures and material claims when feasible. Do not accept summaries without
   inspectable case-level evidence.
8. Review optimization history for cherry-picking, selective reruns, overfitting,
   uncontrolled changes, hidden regressions, and unauthorized contract changes.
9. Verify each adapter preserves canonical behavior and has compatible syntax,
   parameters, schema, tools, limitations, fallback, and re-evaluation triggers.
10. Review operational readiness: owner, version, access, secrets handling,
    logging and redaction, cost and latency limits, monitoring, drift detection,
    incident response, staged rollout, rollback trigger, and preserved baseline.
11. Record defects with stable IDs, severity, affected requirement or artifact,
    exact evidence, reproduction, consequence, required remediation, owner, and
    retest scope using [references/prompt-qa-standard.md](references/prompt-qa-standard.md).
12. Apply critical gates before weighted scoring. Do not average away safety,
    authority, privacy, truthful-status, destructive-action, mandatory-schema,
    evidence-integrity, or rollback failures.
13. Issue approve, approve with conditions, reject, or inconclusive. Limit approval
    to the exact versions, adapters, populations, and conditions supported by the
    evidence; require a new review when those boundaries change.
14. Deliver with [assets/prompt-qa-review-template.md](assets/prompt-qa-review-template.md).

## Rules

- Do not edit the reviewed prompt or evidence in place. Return defects and route
  remediation to Prompt Architect, Prompt Optimizer, or Prompt Tester.
- Do not treat a high aggregate score, polished documentation, or one successful
  demonstration as release evidence.
- Do not accept screenshots or summaries when raw, version-linked evidence should
  exist; label unverifiable claims as such.
- Do not expose secrets, personal data, confidential fixtures, hidden grader data,
  or private reasoning in the review report.
- Do not expand an approval beyond tested models, adapters, languages, tools,
  segments, data classes, or operating conditions.
- Do not approve your own material prompt change without an independent reviewer
  when the risk or governance policy requires separation of duties.
- Do not mark remediation complete until affected tests and regressions pass.

## Handoff

Provide scope and independence statement, artifact manifest, requirement-to-
evidence matrix, architecture and authority findings, test-integrity findings,
recalculation or reproduction results, adapter and operations findings, defects
with severity and owners, blockers, retest scope, residual risks, limitations,
conditions, exact approval boundary, and final verdict.
