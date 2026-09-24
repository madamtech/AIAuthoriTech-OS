---
name: slicer-profile-builder
description: Build and validate versioned slicer profiles for a specific printer, firmware, nozzle, build surface, material batch, model class, and quality target. Use when calibrating or standardizing repeatable 3D-print settings with measured acceptance evidence and a reversible baseline. Use when asked to (1) build slicer profile, (2) refine slicer profile, (3) validate slicer profile, or (4) standardize slicer profile.
---

# Slicer Profile Builder

Use the [operating standard](references/slicer-profile-standard.md) and [working template](assets/slicer-profile-template.md).

## Procedure

1. Confirm hardware, firmware, nozzle, plate, material, drying, geometry, strength, finish, and time requirements.
2. Define temperatures, cooling, speeds, acceleration, layers, walls, infill, supports, adhesion, flow, and machine limits.
3. Run controlled coupons and representative prints, record results, lock the profile, and define retest triggers.

## Output Contract

Provide verified inputs, specifications, assumptions, risks, approvals, execution steps, owners, and validation criteria.

## Guardrails

- Use verified facts and label estimates.
- Protect customer, supplier, and proprietary information.
- Require approval before irreversible production, pricing, or customer communication.
- Do not claim safety, compliance, or successful validation without evidence.

## Recovery

If machine state, manufacturer limits, material condition, calibration evidence, or acceptance criteria is unresolved, preserve the last validated profile. Do not compensate for mechanical faults with unsafe temperatures or uncontrolled parameter changes.
