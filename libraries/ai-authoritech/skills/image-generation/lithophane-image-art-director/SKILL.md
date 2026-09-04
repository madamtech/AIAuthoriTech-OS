---
name: lithophane-image-art-director
description: "Create and revise high-resolution grayscale artwork specifically for lithophane 3D printing, then provide tool-specific model-generation and slicer settings for ItsLitho and MakerWorld MakerLab. Use whenever an image is being designed, prompted, edited, evaluated, or prepared for conversion into a lithophane, lamp panel, lightbox, framed backlit artwork, curved shade, flat shade, small lamp, or other backlit relief print."
---
# Lithophane Image Art Director

Use the [operating standard](references/lithophane-image-standard.md), [tool profiles](references/lithophane-tool-profiles.md), and [prompt template](assets/lithophane-prompt-template.md).

## Purpose
Create source images that translate into strong, prominent, readable 3D lithophane depth instead of flat, muddy, washed-out, or weak relief, and then guide the user through the correct conversion and print settings for the lithophane tool they are using.

This skill governs two connected stages:
1. **Image-design stage** — tonal depth, edge readability, dimensional separation, and high-resolution detail.
2. **Lithophane conversion/printing stage** — tool-specific geometry, thickness, resolution, fit, and slicer settings.

## Primary Lithophane Tools
Treat these as the two main lithophane-generation tools:

1. **ItsLitho** — `itslitho.com` / `tool.itslitho.com`
2. **MakerWorld MakerLab — Make My Lithophane** — `makerworld.com/makerlab/makeMyLithophane`

If the user specifies one of these tools, tailor all model-generation settings to that tool rather than giving generic lithophane advice.

When the user asks for a physical object such as a **small lamp, lampshade, framed lithophane, lightbox, night light, arc, cylinder, or other shaped lithophane**, provide both:
- the settings to use **inside ItsLitho or MakerLab**, and
- the settings to use **in the slicer**.

Do not mix generator settings and slicer settings together. Label them clearly.

## Trigger Conditions
Use this skill whenever the user mentions or implies:
- lithophane
- 3D printed photo or image relief
- lamp shade artwork intended for lithophane conversion
- lightbox artwork
- backlit 3D image panel
- framed lithophane artwork
- small lithophane lamp
- ItsLitho
- MakerWorld MakerLab / Make My Lithophane
- image-to-lithophane preparation
- improving grayscale depth before 3D conversion
- making a lithophane image darker, stronger, more detailed, or more prominent

## Required Product Intake
Before giving final physical settings, resolve as many of these as possible from the user's request and prior context:
- lithophane tool: ItsLitho or MakerLab
- target form: flat panel, frame, lightbox, small lamp, cylinder, arc, bell, sphere, lampshade, etc.
- physical width / height / diameter in mm
- printer and nozzle
- filament type and color
- light source and available internal clearance
- frame, slot, ledge, or base fit requirements
- monochrome vs CMYK/color lithophane

If the user wants an exact fit and dimensions are missing, ask for the required fit measurements instead of inventing them. If the user only wants a general cute/small lamp, give a practical starter size and label it as a **starting profile**.

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
Use a controlled grayscale palette from near-white through multiple midtones to deep charcoal/black. Do not create a pale, low-contrast gray wash.

### 2. Deep Connected Shadow Masses
Use larger intentional dark zones rather than only tiny scattered dark pixels. Good locations include hair masses and deep curls, eye makeup and lashes, folds and recesses, shadowed sides of objects, background tufting recesses, typography shadows, and negative spaces between overlapping objects.

### 3. Protected Highlight Zones
Reserve the brightest whites and near-whites for important visual accents such as eyes, facial highlights, pearls, diamonds, jewelry, metallic reflections, perfume glass highlights, lettering highlights, and rim lighting. Do not flood the whole image with white.

### 4. Rich Midtone Separation
Build distinct tonal bands rather than only black and white. Use deep charcoal, dark gray, medium gray, light gray, and near-white as readable zones.

### 5. Strong Local Contrast
Important objects must separate from adjacent areas. If adjacent elements are too similar in grayscale value, revise them before generation or editing is complete.

### 6. Crisp Sculpted Edges
Use clean, well-defined edges on important features, including eyes, eyebrows, lips, nose structure, jawline, fingers, jewelry, text, money edges, bottle silhouettes, gems, and hair boundaries.

### 7. Directional Sculpted Lighting
Prefer a clear key-light direction, visible highlight side, visible shadow side, shaped facial lighting, dimensional object shadows, and rim/specular highlights where appropriate. Avoid flat front lighting.

### 8. Depth Hierarchy
Recommended hierarchy:
- **Foreground:** sharpest edges and strongest selective contrast
- **Primary subject:** strong detail and controlled contrast
- **Secondary objects:** slightly less dominant
- **Background:** textural and dimensional but slightly more restrained

### 9. Dense Detail Without Micro-Noise
Prefer defined hair waves, grouped strands, larger gemstones, readable stitching, strong tufting, visible object textures, and pronounced metallic engraving. Avoid relying on microscopic speckles or tiny low-contrast noise.

### 10. Metallic / Embossed Aesthetic
When appropriate, use embossed metallic texture, beveled edges, engraved details, jeweled highlights, pearl-like specular reflections, and sculpted relief appearance.

### 11. Focal-Point Composition
Keep one clear dominant subject or focal region. Supporting elements should reinforce the focal point rather than competing equally with it.

### 12. Print-Scale Awareness
Favor bold readable structure over fragile micro-detail. When physical dimensions are known, prioritize details that will survive at that scale.

## Portrait-Specific Rules
For portrait lithophanes, slightly exaggerate the readability of eyes and lashes, eyebrows, lips, nose structure, jawline, cheek shadows, hairline, and major hair waves while maintaining natural anatomy.

## Typography Rules
When text is part of a lithophane image:
- use clear letterforms
- keep adequate stroke thickness
- use strong tonal separation from the background
- avoid hairline scripts unless large enough to survive printing
- use bevel, shadow, or plaque separation when stylistically appropriate
- verify spelling before final generation

## Flat vs Curved Artwork Rule
Do not impose a curved lampshade shape unless the downstream maker specifically requires a curved source image.

If the maker accepts a flat image, output a **straight rectangular PNG** at the required aspect ratio. Let ItsLitho, MakerLab, or the downstream maker perform the physical wrapping/curving.

## ItsLitho Workflow Rule
When the user says they are using **ItsLitho**, provide the exact settings categories they need inside ItsLitho, including as applicable:
- shape
- width / height / diameter
- minimum thickness
- maximum thickness
- mm per pixel / resolution
- grayscale/color treatment
- frame/border
- frame thickness/depth/angle
- lamp/base/interface dimensions
- final export guidance

Use the default starting ranges in the tool profile only when the user does not already have a tested filament-specific or model-specific profile.

For a general monochrome lithophane, the normal starting range is **0.8 mm minimum thickness**, **3.0–3.2 mm maximum thickness**, and **0.10 mm/px** when practical for high detail. Treat 5 mm maximum thickness as project-specific rather than universal.

For a general **small/cute lamp** with no exact dimensions, a reasonable starting envelope is approximately **85–110 mm tall** and **75–100 mm wide/diameter**, then adjust to the actual light source, mounting interface, and printer build volume.

## MakerWorld MakerLab Workflow Rule
When the user says they are using **MakerWorld MakerLab / Make My Lithophane**:
- size/crop the source image to the final product aspect ratio
- distinguish monochrome from CMYK/color lithophane workflows
- match exact panel dimensions to the receiving MakerWorld frame/lightbox when one is specified
- preserve high source-image detail
- use the generated model dimensions as the source of truth before slicing
- follow any model-specific LED board, frame slot, or enclosure requirements

Do not assume a generic panel size for a specific MakerWorld frame or lightbox.

## Slicer Baseline
Unless a proven printer/filament profile overrides it, start with:
- **layer height:** 0.10–0.12 mm
- **lithophane body:** fully solid, typically 100% infill or a validated all-wall strategy
- **detail-region speed:** approximately 30–45 mm/s as a quality-oriented starting point
- **flat panel orientation:** vertical/on edge when practical for image detail, with stabilization as needed
- **seam:** back or least-visible edge
- **supports:** avoid on the image surface unless the actual geometry requires them
- **material:** white PLA is the standard monochrome starting material

For a **Bambu Lab P1S with 0.4 mm nozzle**, use 0.10–0.12 mm layers as a practical high-detail baseline and retain the filament's calibrated temperature/flow settings.

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

## Conversion and Print QA
Before calling the job print-ready, verify:
- the correct tool profile was used: ItsLitho or MakerLab
- generator dimensions match the physical frame/lamp target
- minimum/maximum thickness is appropriate to filament and light transmission
- mm/px or quality setting preserves enough image detail
- the model is solid where lithophane tonal thickness is required
- slicer orientation is intentional
- seam placement avoids the focal image area
- supports do not scar the image surface
- the light source fits with safe clearance
- the sliced preview shows the expected full lithophane body and no accidental hollowing

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

If the **printed lithophane** is too washed out or weak:
1. confirm the model is fully solid
2. increase maximum thickness moderately if the filament transmits too much light
3. verify minimum thickness is not too thin for the filament
4. verify image contrast and midtone structure
5. reduce excessive backlight intensity if needed

If the **printed lithophane** is too dark:
1. reduce maximum thickness
2. confirm the light source is bright and evenly distributed
3. verify the source image is not crushed in the shadows
4. restore midtone separation in the source image

## Tool-Specific Output Contract
When a tool is specified, return settings in this order:
1. **Source image** — aspect ratio, orientation, resolution, grayscale/color guidance
2. **ItsLitho or MakerLab settings** — shape, dimensions, min/max thickness, resolution, frame/base/interface values
3. **Export** — STL/3MF or supported model output
4. **Slicer settings** — printer/nozzle, layer height, walls/infill, orientation, speed, brim/support, seam
5. **Lighting/fit check** — light-source clearance and heat/safety considerations
6. **QA before printing** — preview contrast, wall solidity, dimensions, frame fit, slice inspection

## Output Contract
When this skill is used, produce as applicable:
- lithophane-ready art direction
- optimized image-generation prompt
- negative prompt / avoid list
- recommended aspect ratio or pixel dimensions
- ItsLitho settings
- MakerWorld MakerLab settings
- slicer settings
- physical size / fit guidance
- depth hierarchy notes
- grayscale QA findings
- revision instructions
- final status: **ready for lithophane conversion**, **ready to slice**, **revise**, or **blocked by missing fit dimensions**

## Guardrails
Do not claim an image is lithophane-ready solely because it is grayscale.
Do not equate maximum contrast with maximum quality.
Do not use high resolution as a substitute for tonal depth or edge clarity.
Do not invent curved source geometry when the downstream tool expects a flat image.
Do not allow decorative detail to destroy facial readability or focal hierarchy.
Do not invent exact frame, slot, lamp-base, or LED-board dimensions when the user is fitting an existing part.
Do not present ItsLitho generator settings as if they were slicer settings, or vice versa.
Prefer low-heat LED lighting for PLA lithophane lamps and maintain safe clearance from the printed plastic.
