# Knowledge Migration Standard

## Migration controls

Preserve content, identifiers, provenance, relationships, metadata, permissions, retention, legal holds, deletion obligations, versions, and consumer contracts unless an approved mapping explicitly changes them. Record every exclusion and lossy transformation. Never treat record counts as semantic, permission, or retrieval equivalence.

## Required gates

- Inventory and classification are complete enough to define scope.
- Source-to-target mappings and authority are approved.
- Pilot waves pass counts, hashes, sampling, relationship, access, search, citation, and consumer tests.
- Delta capture or freeze behavior prevents untracked changes.
- Cutover and rollback are rehearsed with named owners.
- Target acceptance is documented before source retirement.

When reconciliation fails, pause the affected wave, preserve the source, and investigate the variance. Decommission only after recovery artifacts, consumer validation, retention, and audit evidence are verified.
