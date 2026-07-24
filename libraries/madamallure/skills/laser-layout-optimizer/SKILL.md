---
name: laser-layout-optimizer
description: Optimize laser cutting and engraving layouts for material yield, grain, defects, kerf, heat accumulation, operation order, part stability, traceability, and safe production. Use when nesting verified artwork on sheets or fixtures after material and fire controls are confirmed.
---

# Laser Layout Optimizer

Use the [operating standard](references/laser-layout-standard.md) and [working template](assets/laser-layout-template.md).

## Procedure

1. Confirm material, sheet size, usable area, grain, defects, machine bed, kerf, operations, quantities, and priorities.
2. Nest parts with margins, hold-down strategy, common-line restrictions, heat spacing, labels, and remnant use.
3. Simulate or test the toolpath, document yield and cut order, and save a versioned production layout.

## Output Contract

Provide verified inputs, specifications, assumptions, risks, approvals, execution steps, owners, and validation criteria.

## Guardrails

- Use verified facts and label estimates.
- Protect customer, supplier, and proprietary information.
- Require approval before irreversible production, pricing, or customer communication.
- Do not claim safety, compliance, or successful validation without evidence.

## Recovery

If material safety, sheet condition, kerf, fixture, heat behavior, process order, or fire controls are unresolved, do not run the layout. Use a safe preview and coupon before committing the production sheet.
