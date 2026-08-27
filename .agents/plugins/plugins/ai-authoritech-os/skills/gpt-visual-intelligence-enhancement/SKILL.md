---
name: gpt-visual-intelligence-enhancement
description: "Add an evaluation-led visual intelligence layer to an existing GPT without replacing its domain expertise. Use for image creation, image editing, branded visuals, thumbnails, product concepts, print-ready artwork, visual references for 3D production, and any request where the GPT must translate user intent into a controlled visual brief, route the correct image-generation skills, verify the result, and preserve explicit constraints through revision."
---
# GPT Visual Intelligence Enhancement

## Purpose
Enhance an existing GPT with reusable visual-production capability while preserving the GPT's original role, business rules, tone, knowledge boundaries, and decision authority.

This skill is additive. It must not replace, weaken, or silently rewrite the host GPT's core instructions.

## Activation
Activate when the user asks to create, generate, design, render, visualize, edit, restore, enhance, retouch, resize, isolate, remove, replace, stylize, mock up, storyboard, or prepare an image or visual asset.

Also activate when a non-image request would clearly benefit from a visual deliverable and the user has authorized creation.

## Required orchestration
1. Preserve the host GPT's domain role and active business context.
2. Route the request through `personalized-capability-framework` as the primary visual orchestrator.
3. Classify the task: new generation, edit, continuity, campaign, product, technical, printable, 3D reference, or workflow design.
4. Apply the host GPT's normal evaluation process to the visual request before generation.
5. Build a complete visual brief using the approved prompt architecture.
6. Select only the smallest complete chain of existing image-generation skills.
7. Generate or edit using an available image-capable tool. Never imply that this SKILL.md creates images by itself.
8. Evaluate the result against the acceptance gates.
9. Revise only the failed elements while preserving approved elements and explicit locks.
10. Return the visual result plus only the usage information needed by the user.

## Evaluation correlation
The host GPT's evaluation process must be applied in this order:

### 1. Intent alignment
Confirm the visual's purpose, audience, use environment, and success condition.

### 2. Evidence and context
Use supplied images, approved brand assets, current conversation instructions, and verified repository references. Label inferred details. Do not claim preservation without a usable reference.

### 3. Constraint control
Create explicit locks for identity, facial features, body proportions, product geometry, logo, wording, spelling, colors, dimensions, background, layout, file format, and elements that must not change.

### 4. Capability and tool fit
Distinguish among prompt preparation, image generation, image editing, vector preparation, production guidance, and file conversion. Do not promise unsupported formats or capabilities.

### 5. Quality and risk review
Evaluate composition, hierarchy, readability, brand consistency, continuity, technical suitability, commercial readiness, safety, and rights risk.

### 6. Recovery
When the request, reference, and remembered preference conflict, prioritize the newest explicit user instruction. Stop and request clarification only when the conflict prevents safe or accurate execution.

## Visual brief contract
The internal or user-visible brief must resolve:
- subject and action
- intended use and audience
- composition and framing
- environment and background
- lighting and camera treatment
- materials and texture
- palette and brand boundaries
- typography and exact text
- output dimensions or aspect ratio
- transparency and production requirements
- identity, style, geometry, and layout locks
- exclusions and negative constraints
- acceptance tests

## Quality gates
A result is complete only when:
- the user's primary request is visibly satisfied;
- all explicit locks are preserved;
- exact text is correct and legible when text is required;
- composition and hierarchy support the intended use;
- brand rules do not leak between businesses or projects;
- the output is technically appropriate for the stated destination;
- no unsupported claim is made about resolution, vector status, transparency, print readiness, or rights clearance;
- the requested delivery pattern is followed, including one-at-a-time delivery when specified.

## Revision protocol
For revision requests:
1. Restate the requested change internally as a delta.
2. Freeze every approved element not named in the delta.
3. Apply the smallest possible modification.
4. Recheck all locks after the edit.
5. Do not add decorative elements, logos, backgrounds, text, or style changes that were not requested.

## Output behavior
Do not expose hidden reasoning. Provide the finished visual or an executable production brief, followed by concise specifications only when useful.

When a tool requires an image upload or reference and none is available, request the missing image instead of inventing a target.

## Dependencies
Primary dependency:
- `personalized-capability-framework`

Common downstream skills include:
- `brand-visual-translator`
- `commercial-composition-director`
- `image-revision-qa-controller`
- `character-identity-lock`
- `controlled-style-fusion`
- `commercial-readiness-rights-checker`
- `image-to-3d-reference-designer`

Use repository routing and catalog records as the source of truth for the full skill chain.

## Completion record
For governed workflows, record:
- host GPT or agent identifier
- activated visual skills
- input references
- assumptions
- locks
- acceptance results
- unresolved limitations
- revision count
