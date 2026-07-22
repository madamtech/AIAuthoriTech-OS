---
sku: AA-SKL-000169
asset_id: image-generation.visual-asset-governance-manager.v1
version: 1.0.0
status: testing
---
# Visual Asset Governance Manager

## Purpose
Control ownership, naming, versions, approvals, source references, brand use, lifecycle, and reuse of visual assets.

## Inputs
Asset, business, project, creator/source, rights status, references, version, approval status, intended channels, and retention rules.

## Procedure
Assign identity and metadata, link source assets, classify rights and sensitivity, record generation/edit history, store prompts and approvals, define canonical/deprecated versions, and map reusable locks. Ensure governed assets are discoverable without exposing confidential material.

## Output contract
Governance record, owner, usage scope, source lineage, version, status, restrictions, related assets, and review date.

## Rules
No asset is “approved” without an explicit approval event. Do not reuse employer, client, or personal likeness assets outside their permitted context.

## QA
Check metadata completeness, source traceability, version uniqueness, brand scope, and restrictions.

## Recovery
Quarantine assets with unknown origin or rights until reviewed.
