---
name: image-revision-qa-controller
description: "Turn feedback into precise correction passes and prevent repeated mistakes, regressions, and false claims of completion. Use when creating, reviewing, revising, governing, or validating image-generation work that needs explicit inputs, constraints, rights, continuity, quality checks, recovery handling, and a reusable production-ready output. Use when asked to (1) control image revision qa, (2) reconcile image revision qa, (3) audit image revision qa, or (4) plan image revision qa."
---
# Image Revision and QA Controller

Use the [operating standard](references/operating-standard.md) and [working template](assets/working-record.md).

## Purpose
Turn feedback into precise correction passes and prevent repeated mistakes, regressions, and false claims of completion.

## Inputs
Current image, original request, revision history, latest feedback, locks, and acceptance criteria.

## Procedure
Translate feedback into atomic changes; distinguish correction from preference; freeze approved elements; check for repeated failure patterns; create a revision prompt; perform before/after QA; update the acceptance checklist. Ask for confirmation before generation only when the user explicitly requires it or the target is missing.

## Output Contract
Issue list, root cause, exact corrections, protected elements, revision prompt, QA results, and status: pass, revise, or blocked.

## Guardrails
Do not say a change was made unless it is visible. Do not repeat the same generation approach after the user identifies the same failure. Preserve all approved aspects.

## QA
Check every user statement individually, then perform global regression review for identity, text, count, color, layout, crop, and style.

## Recovery
Return to the last approved version and change one variable at a time.
