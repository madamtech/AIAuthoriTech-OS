# Marketplace Standard

## Platform role

Document who contracts with whom; who sets price, terms, and acceptance; who
collects and transmits funds; who bears taxes, refunds, chargebacks, warranties,
insurance, safety, and service obligations; and what the platform verifies.
Require legal, tax, payments, employment, and regulated-industry review where
applicable.

## Transaction integrity

Use explicit, versioned state machines. Every transition requires actor,
authority, prerequisites, amount or scope, effective time, idempotency, evidence,
notifications, downstream effects, reversal or compensation, reconciliation, and
audit. Keep order, fulfillment, payment, payout, refund, and dispute state
separate.

## Trust and safety

Apply proportionate verification, listing review, abuse detection, reporting,
human review, temporary safeguards, sanctions, appeals, and reinstatement. Track
false positives, false negatives, decision consistency, response time, severe
harm, and repeat abuse. Do not treat automated risk scores as facts.

## Ranking and reputation

Publish the main ranking factors and label sponsorship. Test cold start, feedback
loops, popularity concentration, manipulation, discriminatory outcomes, stale
availability, and unauthorized personalization. Show review count, recency,
verified-transaction status, dimensions, and uncertainty.

## Commerce

Use approved marketplace payment infrastructure, immutable provider and internal
references, signed webhooks, idempotency, double-entry accounting where required,
daily reconciliation, exception queues, and separated duties. Route tax,
licensing, money transmission, escrow, and payout obligations to specialists.

## Verification

Test participant isolation, listing moderation, search permissions, ranking
disclosure, duplicate orders and webhooks, price changes, inventory races,
partial fulfillment, cancellation timing, refunds, disputes, chargebacks, payout
reversals, fraudulent reviews, sanctions and appeals, provider outage, export,
deletion, accessibility, and recovery.
