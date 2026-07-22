---
sku: AA-SKL-000160
asset_id: image-generation.image-revision-qa-controller.v1
version: 1.0.0
status: testing
---
# Image Revision and QA Controller

## Purpose
Turn feedback into precise correction passes and prevent repeated mistakes, regressions, and false claims of completion.

## Inputs
Current image, original request, revision history, latest feedback, locks, and acceptance criteria.

## Procedure
Translate feedback into atomic changes; distinguish correction from preference; freeze approved elements; check for repeated failure patterns; create a revision prompt; perform before/after QA; update the acceptance checklist. Ask for confirmation before generation only when the user explicitly requires it or the target is missing.

## Output contract
Issue list, root cause, exact corrections, protected elements, revision prompt, QA results, and status: pass, revise, or blocked.

## Rules
Do not say a change was made unless it is visible. Do not repeat the same generation approach after the user identifies the same failure. Preserve all approved aspects.

## QA
Check every user statement individually, then perform global regression review for identity, text, count, color, layout, crop, and style.

## Recovery
Return to the last approved version and change one variable at a time.
