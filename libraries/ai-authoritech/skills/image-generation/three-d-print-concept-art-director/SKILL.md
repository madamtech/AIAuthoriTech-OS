---
sku: AA-SKL-000154
asset_id: image-generation.three-d-print-concept-art-director.v1
version: 1.0.0
status: testing
---
# 3D Print Concept Art Director

## Purpose
Design printable-object concepts that respect manufacturing constraints before CAD or sculpting begins.

## Inputs
Printer, nozzle, material, target dimensions, use, assembly, color count, support tolerance, strength needs, and aesthetic references.

## Procedure
Translate the concept into printable masses, stable stance, minimum feature sizes, wall-thickness intent, support strategy, part orientation, color separations, connection methods, and post-processing plan. Identify features that require engineering validation.

## Output contract
Concept brief, printable part breakdown, risk list, support/overhang guidance, color plan, dimension assumptions, and handoff to STL production.

## Rules
Never label concept art as print-ready geometry. Avoid fragile floating details, impossible cavities, unsupported thin elements, and inaccessible NFC/tag placements.

## QA
Check stability, feature thickness, assembly access, part count, orientation, and printer compatibility.

## Recovery
Thicken, simplify, split, or reposition features before visual refinement.
