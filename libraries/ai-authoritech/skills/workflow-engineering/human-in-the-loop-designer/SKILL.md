---
name: human-in-the-loop-designer
description: Design meaningful human review, approval, intervention, override, escalation, and appeal within automated or AI-assisted workflows, including authority, evidence, workload, timing, interfaces, competence, audit, and effectiveness metrics. Use where risk or policy requires accountable judgment. Do not use ceremonial review or shift impossible monitoring burdens to people.
---

# Human-in-the-Loop Designer

Use the [human review standard](references/human-review-standard.md) and record authority and workload in the [human review design template](assets/human-review-design-template.md).

## Procedure

1. Identify decisions, harms, uncertainty, reversibility, affected people, obligations, and required human authority.
2. Define when humans review all cases, samples, thresholds, exceptions, alerts, or appeals.
3. Provide sufficient evidence, provenance, alternatives, uncertainty, context, and time for an informed decision.
4. Specify reviewer qualifications, access, workload, independence, conflicts, segregation, and backup coverage.
5. Design approve, reject, edit, defer, escalate, override, appeal, and emergency-stop behavior.
6. Capture rationale and audit without demanding private reasoning or excessive personal data.
7. Test alert fatigue, automation bias, disagreement, queue overload, absence, urgency, and adversarial cases.
8. Measure intervention quality, reversals, misses, delay, consistency, workload, harm, and feedback loops.

## Guardrails
- Do not call a process human-supervised when reviewers cannot understand or change outcomes.
- Do not use confidence scores as the sole trigger without calibration.
- Do not punish good-faith overrides that follow policy.
- Do not expose sensitive data beyond what the reviewer needs.

## Recovery

If reviewers lack authority, evidence, competence, capacity, independence, or time, stop calling the workflow human-supervised. Route affected cases to a safe hold or emergency path, restore backup coverage, and resume only after effectiveness is verified.

## Output Contract

Deliver review triggers, authority, evidence shown, reviewer qualifications and access, workload and service levels, actions and appeals, audit, backup and emergency behavior, tests, effectiveness metrics, owners, and approval status.
