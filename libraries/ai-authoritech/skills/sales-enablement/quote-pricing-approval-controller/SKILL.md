---
name: quote-pricing-and-approval-controller
description: Calculate governed quote pricing from approved source data and formulas while preserving price-list provenance, renewal logic, approval boundaries, and calculation transparency.
---

# Quote Pricing and Approval Controller

## Procedure

1. Confirm the governing price list, effective date, currency, pricing basis, formulas, discounts if authorized, and renewal rules.
2. Calculate line totals, year-one totals, recurring totals, alternates, and exceptions with reproducible arithmetic.
3. Return pricing with source provenance, assumptions, approval status, and any required commercial review.

## Output Contract

Provide verified inputs, assumptions, findings or calculations, recommendations or output, unresolved questions, approval/validation needs, and next actions appropriate to the sales task.

## Guardrails

- Never invent prices, discounts, multipliers, approval authority, taxes, freight, or commercial terms.
- Do not use stale pricing when the effective date is uncertain.
- Do not represent calculated pricing as approved unless approval evidence is provided.

## Recovery

If critical source data, authority, product evidence, pricing, customer facts, or decision criteria are missing, stop at the affected boundary. Preserve verified work, label the gap, and request only the minimum information or authorized review needed to continue.
