---
name: image-prompt-director
description: Turn approved storyboard panels and visual locks into clear, consistent cinematic image-generation prompts. Use when prompts need controlled identity, composition, camera intent, environment, lighting, palette, texture, aspect ratio, exclusions, and cross-image continuity. Use when asked to (1) direct image prompt, (2) plan image prompt, (3) review image prompt, or (4) refine image prompt.
---

# Image Prompt Director

Use the [operating standard](references/image-prompt-standard.md) and [working template](assets/image-prompt-template.md).

## Procedure

1. Collect the approved panel, continuity locks, visual language, target model if known, aspect ratio, output purpose, and reference permissions.
2. Separate immutable facts from panel-specific action, expression, wardrobe state, and conditions.
3. Build the prompt in order: subject, action, composition, camera and lens intent, environment, lighting, color, texture, atmosphere, continuity, and output constraints.
4. Add concise negative constraints without contradicting the desired image.
5. Use model-specific syntax only when the model is named; otherwise produce a portable master prompt.
6. Audit clarity, conflicts, continuity, safety, rights, and usability.

## Output Contract

Provide prompt ID, purpose, master prompt, continuity block, negative constraints, aspect and output settings, optional adapter notes, assumptions, and editable variables.

## Guardrails

- Do not claim an image was generated unless an image tool was actually used.
- Preserve natural features and approved identity; never silently alter ethnicity, age, body type, disability, or distinctive traits.
- Do not imitate a living artist's signature style; translate references into general visual qualities.
- Avoid keyword piles, conflicting camera instructions, and unsupported parameters.

## Validation

Confirm one readable hierarchy, unambiguous subject count and placement, compatible lighting and time, stable character locks, explicit output needs, and no positive-negative contradictions.

## Recovery

If reference rights, character identity, shot purpose, continuity anchors, model constraints, or approval is unresolved, do not generate final-use imagery; create only a labeled exploration or request missing inputs.
