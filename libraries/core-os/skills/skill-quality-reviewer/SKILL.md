---
name: skill-quality-reviewer
description: Independently review a Codex skill package for trigger precision, procedural completeness, resources, safety, testability, metadata consistency, and release readiness. Use when asked to review, score, approve, audit, or improve a skill before registration or release.
---

# Skill Quality Reviewer

Review evidence, not intent.

1. Inventory `SKILL.md`, UI metadata, and bundled resources.
2. Check name, folder, description, triggers, and catalog identity.
3. Evaluate scope cohesion, procedure, decisions, recovery, and outputs.
4. Verify references are discoverable and not duplicated.
5. Run official structural validation and required scripts.
6. Score: triggers 20; procedure 25; resources 15; safety 15; testability 15;
   metadata 10.
7. Report verdict, evidence, severity-ranked findings, and exact revisions.

Approve only at 85+, with no critical failure and passing structural validation.
Missing frontmatter, misleading triggers, unsafe actions, fabricated evidence,
broken references, or nonfunctional required scripts are critical. Do not implement
repairs unless the user also asks for changes.
