---
name: three-d-print-concept-art-director
description: "Design printable-object concepts that respect manufacturing constraints before CAD or sculpting begins. Use when creating, reviewing, revising, governing, or validating image-generation work that needs explicit inputs, constraints, rights, continuity, quality checks, recovery handling, and a reusable production-ready output."
---
# 3D Print Concept Art Director

Use the [operating standard](references/operating-standard.md) and [working template](assets/working-record.md).

## Purpose
Design printable-object concepts that respect manufacturing constraints before CAD or sculpting begins.

## Default Production Environment
Unless the user explicitly requests another machine, route all print-production planning to one of these two approved printer/slicer pairs:
1. **Bambu Lab P1S + Bambu Studio**
2. **FlashForge Adventurer 5M + FlashForge Studio**

Use `three-d-print-production-router` for printer-specific settings and final slicer planning.

## Inputs
Printer, nozzle, material, target dimensions, use, assembly, color count, support tolerance, strength needs, and aesthetic references.

## Procedure
Translate the concept into printable masses, stable stance, minimum feature sizes, wall-thickness intent, support strategy, part orientation, color separations, connection methods, and post-processing plan. Identify features that require engineering validation.

For batch product ideation, route to `three-d-product-batch-ideation-architect` first, then use the specialty skill that matches the product family.

## Output Contract
Concept brief, printable part breakdown, risk list, support/overhang guidance, color plan, dimension assumptions, printer route, and handoff to STL/model production.

## Guardrails
Never label concept art as print-ready geometry. Avoid fragile floating details, impossible cavities, unsupported thin elements, and inaccessible NFC/tag placements.

## QA
Check stability, feature thickness, assembly access, part count, orientation, and compatibility with the selected P1S/Bambu Studio or Adventurer 5M/FlashForge Studio workflow.

## Recovery
Thicken, simplify, split, or reposition features before visual refinement.
