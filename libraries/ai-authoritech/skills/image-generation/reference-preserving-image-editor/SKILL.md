---
name: reference-preserving-image-editor
description: "Modify only requested elements while protecting every approved feature of the source image. Use when creating, reviewing, revising, governing, or validating image-generation work that needs explicit inputs, constraints, rights, continuity, quality checks, recovery handling, and a reusable production-ready output."
---
# Reference-Preserving Image Editor

Use the [operating standard](references/operating-standard.md) and [working template](assets/working-record.md).

## Purpose
Modify only requested elements while protecting every approved feature of the source image.

## Inputs
Source image, explicit change list, unchanged-elements list, reference assets for replacements, output dimensions, and quality target.

## Procedure
Confirm the target image, create a preservation mask concept, list requested edits, identify dependencies, perform the smallest viable edit, and compare before/after. Treat do not make any other changes as a hard lock.

## Output Contract
Edit specification, changed elements, protected elements, replacement references, comparison checklist, and final edit prompt.

## Guardrails
Never edit an image that is not actually available. Do not regenerate the entire scene for a localized change unless the user approves. Preserve crop, lighting, identity, product count, and layout when locked.

## QA
Pixel-level visual comparison of all protected regions and semantic comparison of the requested change.

## Recovery
Revert to the original and isolate the edit more narrowly if collateral changes appear.
