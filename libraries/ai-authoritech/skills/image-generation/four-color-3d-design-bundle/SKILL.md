---
name: four-color-3d-design-bundle
description: Create a coordinated bundle containing a user-specified number of original designs for decorating or producing user-specified physical blanks, with a design-appropriate four-color palette, genuine editable SVG vectors, and matching transparent PNG previews. Use when the user asks for a design bundle of any size, four-color artwork, multicolor 3D-print graphics, slicer-ready SVGs, or individually downloadable design files.
---

# Four-Color 3D Design Bundle

Create the requested number of distinct, coordinated designs that the user can import individually into slicer software.

## Intake

Collect or infer the number of designs, design subject, intended blank or product, dimensions or aspect ratio, audience, style, text, and prohibited elements. Ask only for information that materially changes the artwork. Keep the quantity, subject, and blank dynamic for every run. Use 10 only when the quantity is omitted.

## Production workflow

1. Define a shared visual direction and the requested number of clearly different concepts. Avoid near-duplicate recolors.
2. Select exactly four flat colors related to the subject. State their names and hex values. Favor visibly distinct colors that remain easy to replace in a slicer.
3. Create each design as original vector geometry. Use paths and basic SVG shapes; convert lettering to paths when tooling permits. Never place a raster image inside an SVG or disguise traced bitmap noise as vector art.
4. Organize every SVG into four top-level groups named `color-1`, `color-2`, `color-3`, and `color-4`. Use only the declared palette plus transparency. Avoid gradients, filters, masks, clipping that breaks import, patterns, excessive nodes, hairline strokes, and isolated details too small to print.
5. Make same-color regions easy to select and recolor. Prefer closed, filled geometry and simple overlaps. Ensure the design has no background rectangle unless the background is an intentional printable layer.
6. Export each design separately using zero-padded sequential names such as `01-short-name.svg` through the requested final number. Render a matching transparent PNG with the same basename at high resolution.
7. Create `bundle-manifest.md` from [the manifest template](assets/bundle-manifest-template.md), listing the palette, dimensions, filenames, concept notes, and validation status.
8. Run `python scripts/validate_bundle.py <bundle-directory> <requested-count>`. Fix all errors before delivery.
9. Present two individual download links per design, grouped by design, with SVG first and PNG second. Do not substitute a contact sheet or ZIP for the individual files; a ZIP may be offered only as an extra.

## SVG truthfulness

Call a file SVG only when it contains editable vector elements and no embedded raster data. If the available image tool can produce only raster output, deliver the PNGs, label SVG production as unavailable, and do not fabricate `.svg` wrappers around PNGs. When vector authoring tools are available, create and validate the SVGs directly.

## Quality checks

- Confirm the SVG and matching PNG counts both equal the requested quantity.
- Confirm every SVG has a `viewBox`, transparent background, four named color groups, and no `<image>`, gradients, filters, scripts, or external resources.
- Confirm the palette is exactly four subject-relevant colors across the bundle.
- Inspect representative PNGs for clipping, malformed text, unintended artifacts, adequate contrast, and visual distinction.
- Treat printability as conditional on the user's slicer, nozzle, material, scale, and machine. Recommend a small test print before production.

## Delivery

Lead with the finished bundle. Include the four-color palette and concise slicer notes. Give each SVG and PNG its own clickable link so the user can download every image independently.
