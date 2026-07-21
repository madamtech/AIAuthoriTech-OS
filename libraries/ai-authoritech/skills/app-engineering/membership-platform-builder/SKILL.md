---
name: membership-platform-builder
description: Create build-ready specifications for secure, accessible membership platforms covering audiences, member lifecycle, plans, entitlements, subscriptions, trials, onboarding, profiles, content, learning, events, community, moderation, notifications, support, analytics, retention, privacy, integrations, testing, deployment, and operations. Use for associations, paid communities, subscription content, professional networks, coaching programs, alumni groups, clubs, or hybrid memberships—not to invent policies, process raw payment credentials, provide tax advice, or deploy without authorization and verification.
---

# Membership Platform Builder

Design membership as a governed lifecycle and entitlement system, not a paywall.

1. Confirm the member outcome, segments, value proposition, business model,
   governance, brand, devices, languages, accessibility, data sensitivity,
   obligations, success measures, and owners.
2. Define person, household, organization, chapter, cohort, group, membership,
   administrator, moderator, sponsor, resource, and delegation boundaries.
3. Model the lifecycle: prospect, applicant, invited, trial, pending, active,
   grace, past due, paused, suspended, expired, cancelled, alumni, rejected, and
   deleted. Define triggers, effects, notifications, recovery, and audit.
4. Separate catalog, plan, price, membership status, entitlement, limit,
   subscription, payment status, discount, scholarship, sponsorship, and benefit.
   Apply [references/membership-platform-standard.md](references/membership-platform-standard.md).
5. Define signup, eligibility, consent, verification, approval, onboarding,
   profile, preferences, directory visibility, renewal, upgrade, downgrade,
   pause, cancellation, reinstatement, export, and deletion.
6. Enforce role, membership, resource, organization, chapter, cohort, and
   entitlement authorization server-side. Define admin support, impersonation,
   break-glass, access review, and audit.
7. Model content and learning by type, owner, audience, prerequisite, release
   schedule, expiration, progress, completion, accessibility, search, version,
   retention, download, and rights.
8. Model events by eligibility, capacity, waitlist, time zone, registration,
   attendance, cancellation, communications, accommodations, recordings, and
   post-event outcomes.
9. Define community spaces, posts, comments, messages, mentions, attachments,
   reporting, moderation, appeals, blocking, privacy, retention, conduct rules,
   and safeguarding escalation.
10. Treat commerce as an integration with an authoritative provider. Define hosted
    checkout, webhook verification, idempotency, reconciliation, invoices, taxes
    through qualified services, refunds, disputes, grace, and failed-payment
    behavior.
11. Define notification events, consent and preferences, transactional versus
    promotional purpose, channels, templates, localization, quiet hours, digests,
    delivery state, unsubscribe, escalation, and sensitive-content limits.
12. Define support, membership exceptions, manual adjustments, complaints,
    appeals, service expectations, evidence, approvals, and separation of duties.
13. Define metrics from eligibility through activation, benefit use, engagement,
    successful outcomes, renewal, churn, support, moderation, accessibility, and
    unit economics. Separate availability, activity, satisfaction, and value.
14. Define responsive and accessible journeys, all system states, source-of-truth
    mappings, integrations, data lifecycle, observability, security, recovery,
    vertical slices, tests, deployment, and maintenance.
15. Deliver with
    [assets/membership-platform-template.md](assets/membership-platform-template.md).

## Rules

- Do not make payment status the sole authorization decision; resolve effective
  membership and entitlements.
- Do not trust client-supplied group, chapter, organization, or member identifiers.
- Do not expose private profiles, community content, eligibility, or payment state
  beyond authorized audiences.
- Do not collect raw payment credentials when hosted provider surfaces are
  available.
- Do not silently change grandfathered benefits, pricing, consent, or renewal
  terms.
- Do not equate logins or page views with member value.
- Do not automate moderation sanctions or eligibility rejection without the
  required human review and appeal path.
- Preserve export, cancellation, deletion, and offboarding paths.

## Handoff

Provide the platform charter, member and organization model, lifecycle state
machine, plans and entitlements, journeys, permissions, content and learning,
events, community and moderation, commerce, notifications, support, analytics,
data lifecycle, accessibility, integrations, implementation slices, testing,
deployment, operations, risks, assumptions, and open decisions.
