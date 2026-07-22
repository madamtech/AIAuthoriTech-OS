---
sku: AA-SKL-000156
asset_id: image-generation.fashion-product-collage-director.v1
version: 1.0.0
status: testing
---
# Fashion Product Collage Director

## Purpose
Arrange supplied fashion products and outfits into clean advertisement-style collages without altering, duplicating, or omitting source items.

## Inputs
All source images, product groupings, required order, poster dimensions, background, brand, and text requirements.

## Procedure
Inventory every image, identify duplicates and variants, group matching products, remove backgrounds only when authorized, establish a balanced grid or editorial layout, preserve product scale relationships, and reserve text space.

## Output contract
Asset inventory, grouping map, layout plan, placement list, unchanged-elements lock, and final QA count.

## Rules
Use the actual supplied images when requested. Never regenerate product details, double a shoe, omit an item, or alter logos/colors without approval.

## QA
Perform one-to-one source reconciliation: every required source appears exactly once unless a deliberate repeat is documented.

## Recovery
Rebuild from the inventory rather than patching a layout with uncertain counts.
