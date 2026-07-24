---
name: filament-material-advisor
description: Select and compare 3D-printing filaments based on function, printer compatibility, environment, appearance, post-processing, safety, cost, and production risk. Use before prototyping or changing material.
---

# Filament Material Advisor

Use the [operating standard](references/filament-selection-standard.md) and [working template](assets/filament-selection-template.md).

## Procedure

1. Define mechanical, thermal, moisture, UV, flexibility, appearance, contact, and lifecycle requirements.
2. Confirm printer enclosure, hotend, bed, nozzle, ventilation, drying, and manufacturer limits.
3. Compare candidate materials and identify tradeoffs, additives, abrasiveness, warping, fumes, and storage needs.
4. Recommend test coupons and acceptance criteria before committing to production.

## Output Contract

Provide a requirements matrix, ranked materials, printer changes, drying/storage plan, test plan, cost/risk notes, and final recommendation.

## Guardrails

- Do not make unsupported food-safe, skin-safe, medical, or structural claims.
- Use manufacturer data for exact limits.
- Require ventilation and PPE appropriate to the material.

## Recovery

If use environment, loads, temperature, chemical exposure, skin or food contact, printer compatibility, drying, ventilation, or supplier evidence is unresolved, recommend a test plan rather than a definitive material. Exclude unsupported safety-critical uses.
