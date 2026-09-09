# Preservation Audit

Assessment date: 2026-08-09

Comparison: `origin/main` at `ebfde4b6127e0466e6c871d81396c02bd5fa2a09` to branch `agent/gpt-bookmark-inventory` at `eaef183ac300ea9b664264040654e4cab2c2a6b8`.

## Verified preservation

- Pre-existing unique governed assets: 284
- Pre-existing asset identities retained: 284
- Removed asset identifiers: 0
- Renumbered or changed permanent identity fields: 0
- Existing `SKILL.md` files modified: 0
- Existing owned-GPT manifests modified: 0
- Deleted repository paths: 0
- Renamed repository paths: 0

## Additive governed assets

- `CO-SKL-000005` — Bookmarked GPT Router
- `AA-SKL-000208` — GPT Visual Intelligence Enhancement, cataloging a previously present but orphaned skill folder

## Existing files intentionally updated

- Catalog and relationship registries received additive records and missing dependency edges.
- The library registry received the previously used `GRANT`, `SALES`, and `GOVDOC` codes.
- One orphan evaluation replaced its non-governed textual target with `target_sku: AA-SKL-000208`.
- README and ignore files received additive documentation/build-output entries.

GitHub's line-level deletion count reflects replaced JSON formatting and the corrected evaluation target field. It does not represent deleted files or removed governed assets.

## Unfinished work preserved separately

The original worktree remains on `agent/four-color-3d-design-bundle`. Its four pre-existing uncommitted files were not staged, modified, reset, or included in this pull request.

## Validation

`python tools/validate_repository.py` passed with 322 aggregate catalog entries, 12 schemas, 1,790 relationships, 300 evaluations, and 287 maturity decisions.
