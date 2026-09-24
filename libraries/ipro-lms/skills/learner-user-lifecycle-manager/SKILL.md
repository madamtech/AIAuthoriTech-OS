---
name: learner-user-lifecycle-manager
description: Design and audit learner identity and access lifecycle across hiring, provisioning, updates, leave, rehire, termination, external users, merges, and archival. Use when LMS accounts, audiences, assignments, or records depend on HR, CRM, SSO, or manual identity processes. Use when asked to (1) manage learner user lifecycle, (2) review learner user lifecycle, (3) resolve issues in learner user lifecycle, or (4) improve learner user lifecycle.
---

# Learner User Lifecycle Manager

Use the [operating standard](references/learner-lifecycle-standard.md) and [working template](assets/learner-lifecycle-template.md).

Keep access current while preserving authoritative learning history.

## Procedure

1. Identify user populations, identity sources, unique keys, account owners, authentication, and data-classification requirements.
2. Map lifecycle events from creation through activation, updates, leave, transfer, rehire, separation, deactivation, and archival.
3. Define field ownership, update frequency, matching, merge, duplicate, and conflict rules.
4. Specify access, role, branch, audience, assignment, and notification impacts for each event.
5. Protect transcripts and certification history through identity changes.
6. Define failed-provisioning, stale-account, orphan, shared-email, contractor, and retroactive-correction handling.
7. Test normal and boundary events, reconcile populations, and establish operational monitoring.

## Output Contract

Provide lifecycle state model, system-of-record matrix, identity rules, access matrix, event mappings, exception procedures, reconciliation controls, retention requirements, and test plan.

## Guardrails

- Never use mutable attributes as the only identity key when a stable key exists.
- Apply least privilege and timely deprovisioning.
- Do not erase required learning records when access ends.
- Require authorization for account merges and manual overrides.

## Recovery

If identity authority, joiner or mover rules, deactivation timing, transcript retention, merge evidence, privacy, or override approval is unresolved, preserve the account and learning record. Escalate through the authorized identity process.
