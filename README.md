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
- `catalog/knowledge-index.json` — searchable cross-asset and authorized-GPT index
- `reports/master-repository-completion-2026-08-09.md` — master-prompt status and exceptions
- `docs/deployment/cross-platform.md` — ChatGPT, Codex, Claude, and Gemini guidance

Run `python tools/validate_repository.py` from this directory.
