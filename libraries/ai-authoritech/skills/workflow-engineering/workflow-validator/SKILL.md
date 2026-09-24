---
name: workflow-validator
description: Independently validate workflow specifications for completeness, reachability, ownership, decisions, handoffs, exceptions, controls, data, timing, metrics, authorization, testability, and stakeholder agreement. Use before automation, implementation, release, or governance approval. Do not edit the reviewed workflow in place or certify untested operations. Use when asked to (1) create workflow validator, (2) review workflow validator, (3) improve workflow validator, or (4) standardize workflow validator.
---

# Workflow Validator

Use the [workflow validation standard](references/workflow-validation-standard.md) and record independent evidence in the [workflow validation report template](assets/workflow-validation-report-template.md).

## Procedure

1. Freeze the exact workflow version, scope, evidence, owners, requirements, and review boundary.
2. Trace triggers through every branch to explicit completion, failure, cancellation, or escalation.
3. Verify roles, decision authority, segregation, handoffs, inputs, outputs, systems, and source-of-truth rules.
4. Check exceptions, retries, timeouts, duplicates, concurrency, partial states, rework, and recovery.
5. Review privacy, security, accessibility, compliance, audit, retention, and human oversight controls.
6. Walk representative normal, boundary, failure, and unauthorized scenarios with stakeholders.
7. Record defects with evidence, severity, owner, remediation, and retest scope.
8. Issue valid, conditionally valid, invalid, or inconclusive limited to the reviewed version.

## Guardrails
- Do not infer agreement from silence or attendance.
- Do not average away unreachable states or critical control failures.
- Do not treat a diagram alone as an executable specification.
- Do not close defects without corrected evidence and retest.

## Recovery

If the reviewed version changes, evidence is missing, a critical path is unreachable, or stakeholder authority conflicts, suspend the verdict. Preserve the frozen review package, issue an inconclusive or invalid result, and retest only the affected corrected version.

## Output Contract

Deliver the frozen scope and version, trace results, scenario evidence, defects, severities, owners, remediation and retest scope, control findings, stakeholder decisions, limitations, and valid, conditional, invalid, or inconclusive verdict.
