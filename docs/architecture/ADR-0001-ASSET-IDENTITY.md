# ADR-0001: Asset identity

- Status: Accepted
- Date: 2026-07-20

Assign every asset a permanent business SKU, stable machine ID, semantic version,
business, library, lifecycle status, and maturity.

Use `AA`, `LMS`, `MA`, and `CO`. `LMS` identifies i-PRO learning-system assets.
Never reuse or renumber SKUs. Keep capability metadata outside the SKU so assets
can move libraries without breaking identity.
