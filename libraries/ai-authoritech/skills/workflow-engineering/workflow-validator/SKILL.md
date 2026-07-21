---
name: workflow-validator
description: Independently validate workflow specifications for completeness, reachability, ownership, decisions, handoffs, exceptions, controls, data, timing, metrics, authorization, testability, and stakeholder agreement. Use before automation, implementation, release, or governance approval. Do not edit the reviewed workflow in place or certify untested operations.
---

# Workflow Validator

1. Freeze the exact workflow version, scope, evidence, owners, requirements, and review boundary.
2. Trace triggers through every branch to explicit completion, failure, cancellation, or escalation.
3. Verify roles, decision authority, segregation, handoffs, inputs, outputs, systems, and source-of-truth rules.
4. Check exceptions, retries, timeouts, duplicates, concurrency, partial states, rework, and recovery.
5. Review privacy, security, accessibility, compliance, audit, retention, and human oversight controls.
6. Walk representative normal, boundary, failure, and unauthorized scenarios with stakeholders.
7. Record defects with evidence, severity, owner, remediation, and retest scope.
8. Issue valid, conditionally valid, invalid, or inconclusive limited to the reviewed version.

## Rules
- Do not infer agreement from silence or attendance.
- Do not average away unreachable states or critical control failures.
- Do not treat a diagram alone as an executable specification.
- Do not close defects without corrected evidence and retest.
