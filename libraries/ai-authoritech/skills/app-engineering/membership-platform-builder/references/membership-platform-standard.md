# Membership Platform Standard

## Lifecycle

Represent membership with explicit states and versioned transitions. Each
transition needs trigger, authority, prerequisites, effective time, entitlements,
commercial effect, notifications, audit, retry, reconciliation, and reversal or
appeal behavior. Never infer completed activation or cancellation from one
external webhook.

## Entitlements

Keep membership status, plan, price, payment status, and entitlement separate.
Resolve access from effective, auditable entitlement rules that support trials,
grace periods, grandfathering, sponsorships, scholarships, manual exceptions,
future-dated changes, and expiration.

## Community safety

Publish conduct rules and define reporting, evidence, triage, severity,
containment, moderator permissions, member notification, appeal, restoration,
retention, and escalation. Protect reporters and minors or vulnerable groups
where relevant. Use proportionate human review for consequential actions.

## Commerce

Use hosted checkout and verified provider events. Deduplicate and reconcile
subscriptions, invoices, payments, refunds, disputes, credits, and cancellations.
Keep tax, accounting, and legally binding terms in approved specialist systems and
review processes.

## Measurement

Measure the funnel from eligible audience to signup, activation, benefit
utilization, successful outcome, repeat value, renewal, and referral. Segment
voluntary churn, involuntary churn, suspension, expiration, and administrative
closure. Track community health, support burden, moderation, accessibility,
content usefulness, and unit economics without treating engagement as value.

## Verification

Test state transitions, duplicate and delayed commerce events, grace and
grandfathering, role and group isolation, content schedules, waitlists, time
zones, notification consent, moderation appeals, export, cancellation, deletion,
accessibility, recovery, and authoritative reconciliation.
