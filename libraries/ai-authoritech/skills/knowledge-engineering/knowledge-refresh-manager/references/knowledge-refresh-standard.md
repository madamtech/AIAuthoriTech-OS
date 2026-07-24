# Knowledge Refresh Standard

## Freshness model

Assign a freshness tier from business impact, source volatility, authority, legal or safety sensitivity, and consumer exposure. Define maximum age, monitoring interval, change trigger, validation depth, approval, and response target for every tier. An ingestion timestamp proves processing time, not source currency or authority.

## Controlled refresh

1. Detect additions, changes, removals, permission changes, and source-version events.
2. Verify source identity and authority before extraction.
3. Create an immutable snapshot and impact analysis.
4. Re-extract only affected content while preserving provenance.
5. Validate structure, semantics, access, retrieval, citations, and downstream behavior.
6. Promote by approved cohort, invalidate affected caches, and notify consumers.
7. Retain rollback evidence and measure lag, failure, stale exposure, and cost.

Deletion and access restrictions receive urgent propagation. A failed or uncertain refresh must not replace the last verified version.
