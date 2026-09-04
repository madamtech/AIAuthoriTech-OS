---
name: parametric-lamp-interface-designer
description: "Design reusable, measurement-driven lamp interfaces connecting 3D printed lamp bases, necks/adapters, lamp hardware, and lampshades. Use when creating or resizing lamp bases, necks, shade adapters, socket interfaces, cable passages, or coordinated lamp families for Bambu Lab P1S/Bambu Studio or FlashForge Adventurer 5M/FlashForge Studio."
---
# Parametric Lamp Interface Designer

Use this skill whenever a lamp concept requires the base, neck/adapter, hardware, and lampshade to fit together reliably.

## Purpose
Prevent blind whole-model scaling from breaking lamp fit. Treat decorative geometry and functional interfaces separately so a successful lamp can become a reusable profile and then generate smaller, larger, shorter, taller, wider, narrower, or stylistically different variants without losing compatibility.

## Default Production Environment
Unless the user explicitly specifies otherwise, route all print settings to one of these two printer/slicer pairs:

1. **Bambu Lab P1S -> Bambu Studio**
2. **FlashForge Adventurer 5M -> FlashForge Studio**

## Core Assembly Model
Treat the lamp as five coordinated zones:

1. decorative lamp base
2. standardized base interface / receiver
3. swappable neck or adapter
4. real lamp hardware interface and cable path
5. shade interface / fitter

Never assume that all five zones scale together.

## Required Measurements
Capture or derive, as applicable:
- base overall width, depth/thickness, and height
- base receiver opening diameter or width/height
- receiver insertion depth
- neck outside diameter or cross-section
- neck height
- neck lower insertion diameter
- neck upper interface diameter
- center bore / cable passage diameter
- shoulder or flange diameter and thickness
- lamp socket / nipple / LED puck / insert dimensions
- lampshade lower opening / fitter dimensions
- lampshade overall diameter or width and height
- clearance/tolerance required for the actual printer/material pair

## Scaling Rule
**Do not uniformly scale functional interfaces.**

Decorative body geometry may be resized, reshaped, or proportionally scaled. Functional dimensions tied to real hardware, cords, sockets, shade fitters, inserts, screws, LEDs, or mating printed parts must be preserved or intentionally re-engineered.

## Variation Logic
When the user requests smaller or larger lamps, offer one of these modes:

### Mode A — Preserve Interface
Resize the decorative base and/or shade while keeping the proven neck and hardware interface unchanged. Best for fastest, lowest-risk product variations.

### Mode B — Re-proportion Neck
Keep the hardware bores and mating diameters fixed while changing neck height, visible outside diameter, taper, shape, or ornamentation.

### Mode C — New Interface Family
Create a new receiver/neck/shade interface when the user intentionally changes hardware or requires a substantially different shade/base proportion. Record it as Profile B, C, D, etc.

## Batch Variations
For creative-stage batch work, this skill can produce coordinated variations such as:
- XS / small / medium / large lamp bodies
- short / medium / tall necks
- straight / tapered / fluted / sculptural / stepped necks
- narrow / standard / wide shade interfaces
- compact desk lamp / bedside lamp / statement lamp versions

Each variation must list which dimensions are **locked**, **scaled**, or **re-engineered**.

## Profile A
Use `references/profile-a-cardi-bag-lamp.md` as the first known-good physical reference profile.

Profile A is a reference, not a mandatory size. The Cardi bag lamp is treated as the **largest/reference-scale member** of the family unless the user explicitly requests something larger.

## Quality Flow
For every lamp concept, return:
1. target overall dimensions
2. locked hardware/interface dimensions
3. neck/adapter dimensions
4. lampshade interface dimensions
5. fit/tolerance notes
6. part breakdown and assembly sequence
7. recommended printer/slicer pair
8. slicer starting settings appropriate to the selected printer/material
9. test-fit recommendation before committing to a full print
10. status: reference-compatible / new interface required / blocked by missing measurement

## Safety
Use real rated lamp electrical hardware for mains-powered lamps. Do not treat printed PLA/PETG as a substitute for electrical socket hardware. Prefer low-heat LED lighting and maintain safe clearance from printed plastic. For open-flame candle-adjacent products, use heat-safe nonflammable inserts or redesign for flameless LEDs rather than placing flame directly against printed thermoplastic.
