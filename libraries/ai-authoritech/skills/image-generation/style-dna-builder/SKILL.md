---
sku: AA-SKL-000139
asset_id: image-generation.style-dna-builder.v1
version: 1.0.0
status: testing
---
# Style DNA Builder

## Purpose
Turn a preferred visual style into a reusable, testable style system instead of a loose list of adjectives.

## Inputs
Approved reference images, descriptive language, intended business uses, realism level, recurring subjects, prohibited traits, and target generation models.

## Procedure
Extract and document: shape language, facial treatment, anatomy, texture, skin finish, lighting ratios, lens behavior, depth of field, palette, contrast, environment density, typography relationship, emotional tone, and post-processing. Separate defining traits from optional variations. Create positive anchors, negative anchors, and tolerance ranges.

## Output contract
Style name, one-sentence definition, full Style DNA, invariant traits, flexible traits, exclusions, reference ranking, model-adaptation notes, and visual acceptance tests.

## Rules
Do not call a style locked until it has at least two successful samples or one explicit canonical reference. Avoid naming a living artist as a required imitation; describe visual characteristics instead.

## QA
A new image should feel unmistakably part of the same family while still allowing new poses, scenes, and products. Verify that style does not mutate identity or brand colors.

## Failure recovery
When outputs drift, reduce optional modifiers, strengthen the top five defining traits, and compare against canonical references side by side.

## Future expansion
Maintain versioned Style DNA cards and per-model translation profiles.
