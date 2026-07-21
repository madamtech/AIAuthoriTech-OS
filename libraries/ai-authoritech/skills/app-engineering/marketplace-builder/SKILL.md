---
name: marketplace-builder
description: Create build-ready specifications for trusted multi-sided marketplaces covering participants, onboarding, verification, listings, catalog, search, matching, pricing, availability, transactions, fulfillment, payments and payouts, fees, refunds, disputes, reviews, moderation, fraud controls, support, analytics, compliance boundaries, integrations, testing, deployment, and operations. Use for product, service, talent, digital-asset, agent, app, skill, or B2B marketplaces—not to determine legal classification, custody funds directly, guarantee provider quality, or deploy without authorization and specialist review.
---

# Marketplace Builder

Design trust, transaction states, and accountability before discovery features.

1. Confirm the marketplace outcome, buyer and supplier segments, offering types,
   geography, business model, platform role, regulated activities, risk,
   accessibility, scale, success measures, and accountable owners.
2. Define participant, organization, team, representative, provider, buyer,
   beneficiary, administrator, moderator, support, service identity, listing,
   order, engagement, and resource boundaries.
3. Define onboarding, identity or business verification, eligibility, credentials,
   beneficial ownership where required, consent, screening, approval, renewal,
   suspension, appeal, offboarding, and data deletion. Route legal and regulatory
   determinations to qualified specialists.
4. Define listing types, categories, attributes, variants, prices, availability,
   service areas, media, evidence, policies, rights, quality rules, moderation,
   versioning, expiration, and prohibited offerings using
   [references/marketplace-standard.md](references/marketplace-standard.md).
5. Define search, browse, filters, ranking, recommendations, matching, sponsored
   placement, diversity, cold start, personalization, explanations, feedback, and
   manipulation controls. Clearly label paid influence.
6. Model inquiry, quote, booking, order, contract, delivery, acceptance,
   cancellation, refund, dispute, chargeback, payout, reversal, and closure as
   explicit state machines with actors, deadlines, evidence, and recovery.
7. Define pricing authority, taxes through qualified services, platform fees,
   commissions, discounts, deposits, escrow-like behavior, credits, currency,
   rounding, invoices, and immutable financial records. Do not assume the
   platform may hold or transmit funds.
8. Integrate an approved marketplace payment provider for hosted collection,
   connected accounts, verification, webhook signatures, idempotency,
   reconciliation, payout timing, reserves, refunds, disputes, and failure.
9. Define fulfillment evidence for physical, digital, service, appointment, or
   automated offerings. Cover inventory, scheduling, delivery, access grants,
   completion, acceptance, no-show, partial fulfillment, and compensation.
10. Define reviews and reputation by eligibility, verified transaction, dimensions,
    timing, edits, responses, moderation, fraud, appeals, aggregation, recency,
    minimum sample, portability, and removal. Never present reputation as a
    guarantee.
11. Define prohibited behavior, reporting, evidence, triage, risk scoring, human
    review, temporary controls, sanctions, appeals, reinstatement, law-enforcement
    escalation, and audit. Protect reporters and avoid opaque consequential
    automation.
12. Define communications, privacy masking, notification preferences, retention,
    moderation, off-platform leakage policy, support, complaint handling, service
    expectations, and emergency escalation.
13. Define tenant and resource authorization, data minimization, encryption,
    secrets, audit, retention, export, deletion, regional controls, incident
    response, accessibility, reliability, and recovery.
14. Measure liquidity and outcomes: qualified supply and demand, search-to-match,
    time to first response, conversion, fulfillment, repeat use, cancellations,
    disputes, fraud loss, support, concentration, take rate, contribution margin,
    and participant success. Avoid optimizing gross volume at the expense of trust.
15. Decompose delivery into vertical slices with authoritative state,
    permissions, UI states, provider integrations, reconciliation, tests,
    deployment, support, and monitoring.
16. Deliver with
    [assets/marketplace-plan-template.md](assets/marketplace-plan-template.md).

## Rules

- Do not assume the platform is the merchant, employer, agent, broker, custodian,
  or guarantor; document and review the intended role.
- Do not hold raw payment credentials or invent a ledger from mutable order state.
- Do not release payouts solely because a client reports success; reconcile
  authoritative transaction and fulfillment state.
- Do not let ranking, reviews, filters, messages, or exports leak restricted data.
- Do not automate consequential rejection, suspension, or sanctions without the
  required human review and appeal.
- Do not mix sponsored and organic placement without clear disclosure.
- Do not display an unverified credential, review, or provider claim as verified.
- Preserve evidence and recovery for duplicate, delayed, partial, reversed, and
  disputed transactions.

## Handoff

Provide the marketplace charter and platform role, participant model, onboarding
and verification, listing governance, discovery and ranking, transaction and
fulfillment state machines, commerce and payout boundary, reviews and reputation,
trust and safety, communications and support, authorization and data lifecycle,
analytics and economics, vertical slices, tests, operations, risks, assumptions,
and specialist decisions.
