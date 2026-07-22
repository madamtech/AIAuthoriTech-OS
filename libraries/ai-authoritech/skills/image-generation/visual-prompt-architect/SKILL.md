---
sku: AA-SKL-000138
asset_id: image-generation.visual-prompt-architect.v1
version: 1.0.0
status: testing
---
# Visual Prompt Architect

## Purpose
Convert intent, references, brand rules, and technical constraints into a complete image-generation specification that minimizes ambiguity and revision waste.

## Inputs
Objective, subject, audience, platform, dimensions, references, required text, visual locks, desired realism, style, environment, and exclusions.

## Procedure
Build the prompt in controlled layers: objective; subject identity and pose; wardrobe/product geometry; environment; composition and camera; lighting; material behavior; color grade; text/logo handling; output specifications; negative constraints; acceptance criteria. Separate creative freedom from locked requirements. Use measurable placement language and avoid contradictory adjectives.

## Output contract
Provide a master prompt, negative constraints, reference hierarchy, model-neutral scene specification, required aspect ratio/resolution, and a QA checklist.

## Rules
Do not bury critical requirements in prose. Repeat identity and text locks in both specification and QA. Do not use vague phrases such as “make it pop” without translating them into contrast, hierarchy, saturation, scale, or lighting behavior.

## Quality checks
Confirm subject count, hand/object interactions, exact text, brand colors, crop safety, readable hierarchy, background treatment, and production use.

## Failure recovery
When the model repeatedly ignores a requirement, isolate it, simplify competing details, move it earlier in the prompt, and create a separate edit pass if needed.

## Example
For a rose-gold product stand, specify exact lettering, finish, card-holder material, NFC cavity visibility rules, camera angle, and unchanged elements.
