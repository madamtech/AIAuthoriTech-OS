---
sku: AA-SKL-000159
asset_id: image-generation.reference-preserving-image-editor.v1
version: 1.0.0
status: testing
---
# Reference-Preserving Image Editor

## Purpose
Modify only requested elements while protecting every approved feature of the source image.

## Inputs
Source image, explicit change list, unchanged-elements list, reference assets for replacements, output dimensions, and quality target.

## Procedure
Confirm the target image, create a preservation mask concept, list requested edits, identify dependencies, perform the smallest viable edit, and compare before/after. Treat “do not make any other changes” as a hard lock.

## Output contract
Edit specification, changed elements, protected elements, replacement references, comparison checklist, and final edit prompt.

## Rules
Never edit an image that is not actually available. Do not regenerate the entire scene for a localized change unless the user approves. Preserve crop, lighting, identity, product count, and layout when locked.

## QA
Pixel-level visual comparison of all protected regions and semantic comparison of the requested change.

## Recovery
Revert to the original and isolate the edit more narrowly if collateral changes appear.
