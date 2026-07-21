---
name: skill-library-architect
description: Create or substantially redesign governed Codex skill packages from a capability idea, repeated process, SOP, prompt, or existing asset. Use when asked to build a reusable skill, convert expertise into a skill, standardize a skill folder, or resolve overlapping skill scope.
---

# Skill Library Architect

1. Interpret concrete triggers, desired output, and non-triggers.
2. Search the catalog and existing skills for overlap.
3. Assign business, library, permanent SKU, asset ID, and semantic version.
4. Define one cohesive reusable capability.
5. Initialize new skills with the official `init_skill.py`.
6. Put all triggering guidance in the frontmatter description.
7. Write concise imperative procedures, decisions, validation, and recovery.
8. Include only necessary scripts, references, and assets.
9. Test scripts and run `quick_validate.py`.
10. Register only after filesystem validation passes.

Keep `SKILL.md` under 500 lines. Do not create per-skill README, changelog,
installation, or quick-reference files. Never invent dependencies or evidence.
Never label an unvalidated skill approved.
