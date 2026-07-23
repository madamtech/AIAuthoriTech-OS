---
name: certification-renewal-manager
description: Define and operationalize certification renewal, expiration, grace, reinstatement, reminders, exceptions, and audit controls by translating approved policy into explicit dates, statuses, learner actions, communications, LMS behavior, monitoring, and test cases. Use for credential lifecycle design or remediation. Do not infer policy from system behavior or silently change credentials.
---

# Certification Renewal Manager

Use the [renewal lifecycle standard](references/renewal-lifecycle-standard.md) and [renewal control template](assets/renewal-control-template.md).

## Procedure

1. Confirm validity period, renewal window, calculation anchor, timezone, grace period, and reinstatement policy.
2. Define qualifying renewal activities, prerequisites, evidence, fees if applicable, and completion rules.
3. Model dates for initial issue, renewal, late completion, leap years, inactive users, and policy changes.
4. Map statuses and transitions, including active, renewal due, grace, expired, revoked, and reinstated.
5. Specify reminder audiences, timing, channels, ownership, suppression, and escalation.
6. Define exception approval and audit-trail requirements.
7. Test boundary dates, missed notices, duplicate records, retroactive completions, and integration delays.

## Output Contract

Provide lifecycle rules, status-transition table, date examples, renewal journey, notification schedule, exception matrix, LMS configuration handoff, test cases, and monitoring measures.

## Guardrails

- Never infer policy from current system behavior alone.
- State timezone and inclusive/exclusive boundary rules.
- Do not silently extend or revoke credentials.
- Flag discrepancies between policy, configuration, communications, and reports.

## Recovery

If validity anchors, timezone, boundary rules, grace, reinstatement, exceptions, or notification ownership conflict, freeze automated status changes for affected records where authorized. Document examples, preserve current evidence, and escalate the policy decision to the credential owner.
