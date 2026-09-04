---
name: three-d-premium-decor-lighting-designer
description: "Develop print-aware concepts for modern wall art, candle holders, lamp bases, sculptural decor, decorative vessels, tabletop objects, and other premium home or display pieces. Use when creating batches or refining premium 3D products that need elevated form, safe functional interfaces, coordinated materials, and strong presentation value."
---
# 3D Premium Decor and Lighting Designer

## Purpose
Create premium-looking decorative and functional 3D products that can be developed into cohesive collections and printed on the Bambu Lab P1S or FlashForge Adventurer 5M.

## Supported Products
- modern wall art
- dimensional wall panels
- candle holders
- LED candle sleeves and lantern-style holders
- lamp bases
- sculptural lighting bases
- tabletop sculpture
- decorative vessels and display objects
- premium giftable decor
- coordinated sculptural accessories

## Required Intake
Resolve when relevant:
- product type and intended environment
- target dimensions
- freestanding, wall-mounted, framed, or integrated format
- lighting or candle source
- hardware/insert dimensions
- material and finish plan
- number of colors
- weight/stability needs
- one-piece vs assembled construction
- printer choice

## Premium Aesthetic Standard
Prioritize:
- distinctive silhouette
- layered depth and intentional negative space
- refined edge treatment
- sculptural surface texture
- controlled symmetry or purposeful asymmetry
- premium material contrast such as matte + silk/metallic appearance
- integrated rather than exposed hardware when practical
- a clean back/underside as well as a strong front view
- collection-ready visual language

## Candle Holder Rules
- default to **LED/flameless candles** for PLA/PETG printed decor unless the user explicitly specifies a heat-safe insert and suitable material/clearance
- do not treat printed plastic as a direct open-flame candle vessel
- design around the actual LED candle, glass insert, or metal cup dimensions when fit matters
- provide ventilation and clearance guidance for any enclosed light source
- prioritize stable bases and tip resistance

## Lamp Base Rules
- treat electrical hardware dimensions as required fit inputs when the design interfaces with sockets, cords, LED pucks, switches, threaded rods, or prebuilt lamp components
- create cable-routing channels and access points when needed
- keep heat-generating components away from printed plastic and favor low-heat LED lighting
- size the base for stability relative to the shade and overall lamp height
- separate decorative shell from functional hardware carrier when that improves safety and serviceability
- when paired with lithophane panels, route image and lithophane geometry work to **lithophane-image-art-director**

## Modern Wall Art Rules
- define final wall dimensions and viewing distance before choosing feature size
- avoid fragile disconnected islands unless a backplate or connector strategy is intentional
- consider multi-panel/modular construction for larger pieces
- design integrated mounting points, keyholes, standoffs, magnets, or hidden cleats only after hardware dimensions are known
- use layered relief, shadow gaps, negative space, and mixed surface finishes to create premium depth
- plan seams to read as part of the composition when the piece must be split for the printer bed

## Sculptural Decor Rules
- prioritize stable center of gravity and broad enough contact area
- avoid delicate protrusions at exposed handling points
- split large forms at natural visual seams
- use hollow shells only when wall thickness and structural needs are validated
- consider removable bases, inserts, or accent pieces for easier multicolor printing and premium finishing

## Batch / Collection Logic
When generating a premium collection:
- create one shared design language and 5–10 distinct forms
- include a hero product, medium-size companion, and smaller add-on
- reuse compatible bases, inserts, mounting systems, or lighting hardware where possible
- vary silhouette and function rather than only color
- identify pieces that can share source textures, motifs, or modular parts
- include at least one easy-print concept and one statement piece

## Output Contract
Return concept summary, dimensions, silhouette/form strategy, part breakdown, hardware/light/candle interface, material/color plan, stability strategy, safety notes, assembly plan, support/orientation strategy, premium-value features, collection-extension ideas, printer routing, and status of **concept ready**, **needs hardware dimensions**, **needs safety/material validation**, or **ready for slicer planning**.

## Guardrails
Do not recommend direct open flame against printed plastic. Do not invent electrical or hardware fit dimensions. Do not sacrifice stability, clearance, or service access for aesthetics. Do not claim concept art is final printable geometry.