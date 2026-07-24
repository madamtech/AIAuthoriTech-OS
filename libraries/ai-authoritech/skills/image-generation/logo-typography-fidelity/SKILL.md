---
name: logo-typography-fidelity
description: "Protect exact logos, lettering, wordmarks, monograms, spelling, capitalization, and signature letterforms in generated or edited visuals. Use when creating, reviewing, revising, governing, or validating image-generation work that needs explicit inputs, constraints, rights, continuity, quality checks, recovery handling, and a reusable production-ready output."
---
# Logo and Typography Fidelity Controller

Use the [operating standard](references/operating-standard.md) and [working template](assets/working-record.md).

## Purpose
Protect exact logos, lettering, wordmarks, monograms, spelling, capitalization, and signature letterforms in generated or edited visuals.

## Inputs
Canonical logo/wordmark, exact text, font reference, letterform notes, placement, material/finish, and unchanged elements.

## Procedure
Create an exact-text lock, identify distinctive glyphs and tails, define spacing, baseline, scale, clear space, material, and orientation. Prefer compositing supplied vector/raster assets when generation cannot guarantee fidelity. Verify each character visually.

## Output Contract
Typography lock sheet, exact text, glyph notes, logo placement, production method recommendation, and QA checklist.

## Guardrails
No invented approximations of logos. No spelling changes. Matching one letter means matching its repeated instances unless the reference intentionally differs.

## QA
Character-by-character comparison, kerning, alignment, stroke shape, tails, logo geometry, color, finish, and legibility.

## Recovery
Remove generated text and apply the canonical asset in post-production when model output remains unreliable.
