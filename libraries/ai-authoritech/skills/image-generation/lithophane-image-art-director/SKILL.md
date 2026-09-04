---
name: lithophane-image-art-director
description: "Create and revise high-resolution grayscale artwork specifically for lithophane 3D printing, with strong tonal depth, dark connected shadow masses, protected highlights, rich midtones, crisp edges, layered depth separation, and print-scale-aware detail. Use whenever an image is being designed, prompted, edited, evaluated, or prepared for conversion into a lithophane, lamp panel, lightbox, curved shade, flat shade, or other backlit relief print."
---
# Lithophane Image Art Director

Use the [operating standard](references/lithophane-image-standard.md) and [prompt template](assets/lithophane-prompt-template.md).

## Purpose
Create source images that translate into strong, prominent, readable 3D lithophane depth instead of flat, muddy, washed-out, or weak relief.

This skill governs the **image-design stage** before conversion to a lithophane mesh. It optimizes the source artwork for tonal depth, edge readability, dimensional separation, and high-resolution detail.

## Trigger Conditions
Use this skill whenever the user mentions or implies:
- lithophane
- 3D printed photo or image relief
- lamp shade artwork intended for lithophane conversion
- lightbox artwork
- backlit 3D image panel
- image-to-lithophane preparation
- improving grayscale depth before 3D conversion
- making a lithophane image darker, stronger, more detailed, or more prominent

## Core Principle
Do **not** optimize for maximum contrast everywhere. Optimize for **strategic contrast and tonal hierarchy**.

A strong lithophane image should contain:
1. deep connected dark masses
2. protected bright highlights
3. rich separated midtones
4. strong local contrast around important features
5. crisp sculpted edges
6. clear foreground / subject / background separation
7. directional dimensional lighting
8. dense but print-readable texture
9. minimal muddy gray-on-gray merging
10. a strong focal point
11. high native image resolution

## High-Resolution Requirement
Always request the **highest practical native resolution available** from the image model or generation tool.

Preferred output guidance:
- PNG whenever possible
- lossless output preferred over JPEG
- target at least **3000 px on the long edge** for finished artwork when the tool supports it
- prefer **4K-class output or larger** for detailed lithophane source art when available
- preserve the requested final aspect ratio from the beginning
- avoid repeated low-quality resampling
- if upscaling is required, upscale after composition is approved and preserve edges, texture, and tonal gradients

High resolution helps preserve hair strands, facial features, jewelry, fabric texture, typography edges, gem facets, folds, and subtle grayscale transitions. It does not replace good tonal design, but it materially improves the quality of the source data available for lithophane conversion.

## Visual Design Standard

### 1. High-Contrast Grayscale
Use a controlled grayscale palette from near-white through multiple midtones to deep charcoal/black.

Do not create a pale, low-contrast gray wash.

### 2. Deep Connected Shadow Masses
Use larger intentional dark zones rather than only tiny scattered dark pixels.

Good locations include:
- hair masses and deep curls
- eye makeup and lashes
- folds and recesses
- shadowed sides of objects
- background tufting recesses
- typography shadows
- negative spaces between overlapping objects

Connected dark areas generate stronger perceived relief than isolated noise.

### 3. Protected Highlight Zones
Reserve the brightest whites and near-whites for important visual accents such as:
- eyes
- facial highlights
- pearls
- diamonds
- jewelry
- metallic reflections
- perfume glass highlights
- lettering highlights
- rim lighting

Do not flood the whole image with white. Too many bright areas flatten the tonal hierarchy.

### 4. Rich Midtone Separation
Build distinct tonal bands rather than only black and white.

Use multiple readable zones such as:
- deep charcoal
- dark gray
- medium gray
- light gray
- near-white

Midtones are essential because they create many of the intermediate thickness levels that make the final lithophane appear dimensional.

### 5. Strong Local Contrast
Important objects must separate from adjacent areas.

Examples:
- dark hair against a lighter face
- bright pearls against darker fabric
- pale perfume glass against a deeper background
- dark text shadow against a lighter plaque
- bright facial highlights against shaded cheeks

If adjacent elements are too similar in grayscale value, revise them before generation or editing is complete.

### 6. Crisp Sculpted Edges
Use clean, well-defined edges on important features.

Strengthen edge definition around:
- eyes
- eyebrows
- lips
- nose and nostril definition
- jawline
- fingers
- jewelry
- text
- money edges
- bottle silhouettes
- gems
- hair boundaries

Slightly stronger visual definition is preferred because conversion and printing can soften subtle edges.

### 7. Directional Sculpted Lighting
Lighting should describe form.

Prefer:
- clear key-light direction
- visible highlight side
- visible shadow side
- shaped facial lighting
- dimensional object shadows
- rim or specular highlights where appropriate

Avoid flat front lighting that leaves objects visually level with the background.

### 8. Depth Hierarchy
Build the composition in layers.

Recommended hierarchy:
- **Foreground:** sharpest edges and strongest selective contrast
- **Primary subject:** strong detail and controlled contrast
- **Secondary objects:** slightly less dominant
- **Background:** textural and dimensional but slightly more restrained

This prevents the entire image from competing at one visual depth.

### 9. Dense Detail Without Micro-Noise
Intricate detail is valuable, but it must be large enough to survive printing.

Prefer:
- defined hair waves and groups of strands
- larger gemstones and pearl clusters
- readable fabric stitching
- strong tufting
- visible object textures
- pronounced metallic engraving

Avoid relying on microscopic speckles or tiny low-contrast details as the main source of texture.

### 10. Metallic / Embossed Aesthetic
When appropriate to the art direction, use:
- embossed metallic texture
- beveled edges
- engraved details
- jeweled highlights
- pearl-like specular reflections
- sculpted relief appearance

This aesthetic naturally reinforces visual depth and often translates well to lithophane imagery.

### 11. Focal-Point Composition
Keep one clear dominant subject or focal region.

Supporting elements should reinforce the focal point rather than competing equally with it.

### 12. Print-Scale Awareness
Do not assume all digital detail will survive physical printing.

When the final physical dimensions are known, prioritize details that remain visible at that scale. Favor bold readable structure over fragile micro-detail.

## Portrait-Specific Rules
For portrait lithophanes, slightly exaggerate the readability of:
- eyes and lashes
- eyebrows
- lips
- nose structure
- jawline
- cheek shadows
- hairline
- major hair waves

Maintain natural anatomy, but do not allow facial features to dissolve into soft grayscale.

## Typography Rules
When text is part of a lithophane image:
- use clear letterforms
- keep adequate stroke thickness
- use strong tonal separation from the background
- avoid hairline scripts unless they are large enough to survive printing
- use bevel, shadow, or plaque separation when stylistically appropriate
- verify spelling before final generation

## Flat vs Curved Artwork Rule
Do not impose a curved lampshade shape unless the downstream maker specifically requires a curved source image.

If the maker accepts a flat image, output a **straight rectangular PNG** at the required aspect ratio. Let the maker or lithophane software perform the physical wrapping/curving.

## Prompt Construction Order
Build image prompts in this order:
1. subject and scene
2. composition and focal point
3. grayscale lithophane optimization
4. tonal hierarchy
5. lighting and dimensional shading
6. materials and micro-texture
7. edge clarity
8. depth separation
9. high-resolution output
10. negative constraints / avoid list
11. exact dimensions or aspect ratio if known

## Required Prompt Cue
Include this language, adapted to the scene:

> Lithophane-optimized high-resolution grayscale with deep connected shadow masses, protected bright highlights, rich separated midtones, strong local contrast, crisp sculpted edges, directional dimensional lighting, print-readable micro-detail, and clearly separated foreground, subject, and background depth.

Also include:

> Preserve deep blacks, luminous highlights, and smooth tonal gradients without muddy gray blending. Avoid washed-out tones, weak outlines, blown-out whites, low-contrast adjacent objects, excessive flat empty areas, and tiny details that will disappear in 3D printing.

## Image Review Checklist
Before accepting an image, verify:
- grayscale range reaches true dark values and bright highlights
- important objects have local contrast
- face remains readable at reduced preview size
- hair is not one featureless black block
- shadows are connected and intentional
- highlights are selective, not everywhere
- midtones are visibly separated
- background is detailed but subordinate
- edges are crisp around focal features
- text is correct and thick enough
- no large muddy gray regions dominate the image
- no huge empty featureless regions weaken the composition
- image aspect ratio matches the target
- source resolution is high enough for the intended physical size
- output is PNG/lossless when possible

## Recovery Strategy
If a generated image is too light or weak:
1. deepen connected shadow masses
2. increase local contrast around focal features
3. restore protected highlights
4. add richer midtone separation
5. strengthen edge definition
6. reduce flat empty areas
7. increase native resolution or use high-quality upscaling only after tonal issues are corrected

If a generated image is too dark or muddy:
1. open selected shadow regions
2. restore midtone detail
3. protect facial highlights
4. separate overlapping dark objects
5. reduce black crushing while preserving deep anchor shadows

## Output Contract
When this skill is used, produce as applicable:
- lithophane-ready art direction
- optimized image-generation prompt
- negative prompt / avoid list
- recommended aspect ratio or pixel dimensions
- depth hierarchy notes
- grayscale QA findings
- revision instructions
- final status: **ready for lithophane conversion**, **revise**, or **blocked by missing target dimensions**

## Guardrails
Do not claim an image is lithophane-ready solely because it is grayscale.
Do not equate maximum contrast with maximum quality.
Do not use high resolution as a substitute for tonal depth or edge clarity.
Do not invent curved source geometry when the downstream tool expects a flat image.
Do not allow decorative detail to destroy facial readability or focal hierarchy.
