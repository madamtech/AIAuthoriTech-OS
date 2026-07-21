# ADR-0002: Skill packaging

- Status: Accepted
- Date: 2026-07-20

Deployable Codex skills contain `SKILL.md`, `agents/openai.yaml`, and only necessary
`scripts/`, `references/`, or `assets/`. Do not add per-skill README, changelog,
installation, or quick-reference files. Keep repository governance outside skills.
