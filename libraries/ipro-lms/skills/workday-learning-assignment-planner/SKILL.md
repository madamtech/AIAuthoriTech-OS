---
name: workday-learning-assignment-planner
description: Design controlled Workday Learning assignments using approved audiences, content, due dates, recurrence, exemptions, notifications, and completion rules. Use when planning mandatory or targeted learning assignments before tenant configuration. Use when asked to (1) plan workday learning assignment, (2) revise workday learning assignment, (3) evaluate options for workday learning assignment, or (4) prepare implementation of workday learning assignment.
---

# Workday Learning Assignment Planner

Use the [operating standard](references/assignment-control-standard.md) and [working template](assets/assignment-plan-template.md).

Translate an approved assignment requirement into a testable configuration plan.

## Procedure

1. Confirm business owner, learning item, required population, exclusions, start date, due-date policy, recurrence, and completion evidence.
2. Define audience criteria using authoritative worker attributes and effective dates.
3. Specify assignment initiation, due-date calculation, reassignment, cancellation, exemption, and late-completion behavior.
4. Map notifications, manager visibility, reporting, security, and integration impacts.
5. Estimate population and test representative eligible, ineligible, transferred, leave, rehire, and completed learners.
6. Plan approval, production launch, reconciliation, monitoring, and rollback.

## Output Contract

Provide an assignment charter, audience logic, date rules, exception matrix, configuration handoff, notification map, test cases, launch controls, and reconciliation plan.

## Guardrails

- Never infer mandatory populations without owner approval.
- State timezone and effective-date logic explicitly.
- Avoid duplicate assignments and preserve prior completions.
- Do not configure production without authorization.

## Recovery

If assignment authority, population, eligibility, due-date logic, effective dating, security, notification, exception, test evidence, or production approval is unresolved, keep the assignment inactive. Model affected populations and require accountable validation before launch.
