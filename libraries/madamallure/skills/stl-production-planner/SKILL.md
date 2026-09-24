---
name: stl-production-planner
description: Prepare watertight, correctly scaled STL files for reliable 3D-print production. Use when validating mesh geometry, dimensions, tolerances, orientation, segmentation, and version readiness. Use when asked to (1) plan stl production, (2) revise stl production, (3) evaluate options for stl production, or (4) prepare implementation of stl production.
---

# Stl Production Planner

Use the [operating standard](references/stl-production-standard.md) and [working template](assets/stl-production-template.md).

## Procedure

1. Confirm intended use, dimensions, units, printer, material, tolerance, assembly, and revision.
2. Check manifold geometry, normals, walls, holes, intersections, detail size, clearances, and print orientation.
3. Define repairs, segmentation, test prints, file naming, version control, and release criteria.

## Output Contract

Provide verified inputs, specifications, assumptions, risks, approvals, execution steps, owners, and validation criteria.

## Guardrails

- Use verified facts and label estimates.
- Protect customer, supplier, and proprietary information.
- Require approval before irreversible production, pricing, or customer communication.
- Do not claim safety, compliance, or successful validation without evidence.

## Recovery

If units, dimensions, rights, source geometry, printer constraints, or acceptance evidence is unresolved, keep the STL in draft. Do not release it for safety-critical or irreversible production until representative slicing and fit tests pass.
