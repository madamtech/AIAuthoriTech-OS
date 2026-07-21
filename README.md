# AI AuthoriTech OS

Governed repository for reusable assets across AI AuthoriTech (`AA`), i-PRO
learning systems (`LMS`), MadamAllure (`MA`), and shared Core OS (`CO`).

Every asset has a permanent SKU (`[BUSINESS]-[TYPE]-[SEQUENCE]`), stable machine
ID (`<library>.<slug>.v<major>`), semantic version, lifecycle status, and maturity.

## Repository

- `catalog/` — source-of-truth asset records
- `libraries/` — deployable business assets
- `registries/` — controlled business, library, and asset-type codes
- `schemas/` — machine-readable contracts
- `tools/` — validation utilities
- `docs/` — architecture decisions

Run `python tools/validate_repository.py` from this directory.
