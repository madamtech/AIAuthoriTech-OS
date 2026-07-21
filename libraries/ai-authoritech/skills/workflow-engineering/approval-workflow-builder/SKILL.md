---
name: approval-workflow-builder
description: Build governed approval workflows with clear decision rights, criteria, evidence, thresholds, segregation of duties, delegation, expiry, escalation, appeals, audit, and service levels. Use for financial, access, content, release, risk, policy, and exception approvals. Do not automate authority that has not been delegated or use approval as a substitute for effective controls.
---

# Approval Workflow Builder

1. Define decision, authority source, requester, subject, approvers, thresholds, risk, and required evidence.
2. Map single, sequential, parallel, quorum, conditional, and escalation patterns with conflict rules.
3. Enforce identity, least privilege, segregation, delegation limits, absence coverage, and conflict disclosure.
4. Define approve, reject, request changes, defer, expire, withdraw, appeal, revoke, and emergency behavior.
5. Preserve immutable request version, evidence, comments, timestamps, decisions, and downstream effects.
6. Set service levels, reminders, workload routing, duplicate prevention, and authoritative status verification.
7. Test unauthorized, self-approval, stale evidence, changed request, timeout, split decision, and revocation.
8. Deliver authority matrix, flow, criteria, states, controls, notifications, tests, and audit requirements.

## Rules
- Do not allow self-approval where segregation is required.
- Do not reuse approval after material request changes.
- Do not infer approval from timeout or lack of response.
- Do not expose evidence beyond approvers' authorized need.
