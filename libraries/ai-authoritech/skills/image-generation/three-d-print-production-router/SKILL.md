---
name: three-d-print-production-router
description: "Route all non-lithophane 3D printing work to the user's two approved printer/slicer workflows: Bambu Lab P1S in Bambu Studio and FlashForge Adventurer 5M in FlashForge Studio. Use whenever a 3D product concept is being prepared for slicing, printer-specific setup, quality tuning, orientation, support planning, multicolor strategy, or final print QA."
---
# 3D Print Production Router

## Purpose
Standardize 3D print recommendations around the user's two primary machines and slicers so every product concept can move into production with a consistent quality workflow.

## Approved Printer / Slicer Pairs
1. **Bambu Lab P1S** — use **Bambu Studio**
2. **FlashForge Adventurer 5M** — use **FlashForge Studio**

Do not default to another printer or slicer unless the user explicitly asks.

## Required Intake
Resolve, when relevant:
- printer: P1S or Adventurer 5M
- slicer: Bambu Studio or FlashForge Studio
- nozzle size
- filament type and brand/profile
- number of colors/materials
- finished dimensions
- functional load / handling needs
- cosmetic quality target
- support tolerance
- assembly method
- whether the item is decorative, functional, wearable/portable, structural, illuminated, or a collectible

## Quality Flow
Return production guidance in this order:
1. **Printer / slicer selection**
2. **Model preparation** — scale, orientation, split parts, color separation, connectors, tolerances
3. **Layer / wall / infill strategy**
4. **Support strategy**
5. **Speed and visible-surface quality strategy**
6. **Adhesion / brim / stability strategy**
7. **Material-specific considerations**
8. **Multicolor / purge / seam strategy when applicable**
9. **Preview QA before printing**
10. **Post-processing / assembly**

## P1S Rules
For Bambu Lab P1S jobs:
- express settings using Bambu Studio terminology
- preserve calibrated filament-specific temperature, flow, and pressure settings when available
- use modifier meshes, color painting, object/part assignments, adaptive layers, support painting, and seam placement where they improve quality
- consider AMS color-change time and purge waste for multicolor products
- inspect first-layer contact, overhangs, color boundaries, and thin raised details in Preview before printing

## Adventurer 5M Rules
For FlashForge Adventurer 5M jobs:
- express settings using FlashForge Studio terminology
- preserve tested filament profiles when available
- prioritize stable orientation, clean supports, appropriate wall count, and controlled visible-wall speed
- verify any color-part separation or manual filament-change workflow before slicing
- inspect support contact, small isolated islands, thin features, and tall narrow parts before printing

## Cross-Printer Principle
Do not copy numeric settings blindly between Bambu Studio and FlashForge Studio. Match the same **quality intent** across the two machines, then express it using the correct slicer's controls.

## Output Contract
When a printer is named, return:
- printer and slicer
- recommended print orientation
- layer height
- walls / shells
- top and bottom layers when relevant
- infill type and percentage
- support type / placement
- brim or adhesion recommendation
- visible-wall / detail speed guidance
- seam strategy
- multicolor strategy if applicable
- expected risk points
- slice-preview checklist
- final status: **ready to slice**, **revise model**, or **needs dimensions/material details**

## Guardrails
Do not invent printer-specific settings when a filament or hardware constraint is unknown and materially affects the result. Do not claim a concept image is print-ready geometry. Preserve product-specific fit dimensions and safety requirements.