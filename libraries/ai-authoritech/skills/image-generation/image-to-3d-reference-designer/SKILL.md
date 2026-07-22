---
sku: AA-SKL-000153
asset_id: image-generation.image-to-3d-reference-designer.v1
version: 1.0.0
status: testing
---
# Image-to-3D Reference Designer

## Purpose
Create images that are useful as modeling references for MakerLab, CAD, sculpting, or mesh generation rather than merely attractive concept art.

## Inputs
Object purpose, desired dimensions, print process, viewing angles, symmetry, movable parts, overhang constraints, color/material plan, and reference images.

## Procedure
Define clean silhouette, complete unobstructed geometry, neutral pose, orthographic-style front/side/back/three-quarter views, consistent scale, closed surfaces, and clear separation between parts. Avoid hidden intersections and perspective distortion.

## Output contract
Reference-view plan, geometry notes, dimension assumptions, part breakdown, symmetry guidance, print-aware constraints, and modeler checklist.

## Rules
State clearly that an image is not an STL. Do not imply watertight geometry, tolerances, or print readiness from an image alone.

## QA
All views must describe the same object and expose every required surface and connection.

## Recovery
Simplify pose, remove accessories, and regenerate neutral views when model extraction is unreliable.
