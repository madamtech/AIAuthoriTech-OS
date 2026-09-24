---
name: skill-library-architect
description: Create or substantially redesign governed Codex skill packages from a capability idea, repeated process, SOP, prompt, or existing asset. Use when asked to build a reusable skill, convert expertise into a skill, standardize a skill folder, split or merge skill scope, or resolve a proposed skill that overlaps the existing catalog. Do not use for workflows, agents, apps, templates, or knowledge packs that should remain first-class assets. Use when asked to (1) architect skill library, (2) assess skill library, (3) refine skill library, or (4) document skill library.
---

# Skill Library Architect

Create one cohesive, reusable capability. Do not perform the capability's client work.

## Procedure

1. Capture concrete triggering requests, expected outputs, intended users, non-triggers, constraints, tools, evidence, and failure modes.
2. Search the catalog, frontmatter descriptions, relationships, and backlog for overlap. Classify the proposal as new skill, revision, merge, split, another asset type, or rejection.
3. Read [references/skill-package-standard.md](references/skill-package-standard.md) before assigning structure or metadata.
4. Define the smallest scope that completes one specialized job. Route orchestration to a workflow and static knowledge to a knowledge pack.
5. Confirm business, library, asset type, sequence availability, asset ID, owner, status, maturity, dependencies, and semantic version. Do not reserve a SKU without catalog authority.
6. For a new skill, initialize with the official `init_skill.py`; for an existing skill, preserve its identity and history.
7. Put all trigger and "when to use" guidance in the frontmatter description. Write imperative procedures, decisions, validation, recovery, and output requirements in the body.
8. Add only reusable resources justified by the task: deterministic scripts for fragile mechanics, references for non-obvious knowledge, and assets for deliverable inputs.
9. Generate or refresh `agents/openai.yaml`; ensure the default prompt explicitly invokes `$skill-name`.
10. Test scripts, run official skill validation, run repository validation, and confirm catalog and relationship consistency.
11. Deliver the package inventory, classification rationale, validation evidence, unresolved decisions, and registration changes.

## Decision Rules

- Revise when the outcome and user trigger substantially match an existing skill.
- Merge when two skills differ mainly by wording and share the same inputs, workflow, and output.
- Split only when independent triggers lead to independent outputs and loading both procedures would be wasteful.
- Create a workflow when stages share state, branch, require approval, retry, or recover.
- Create a knowledge pack when the proposed asset contains authoritative facts without a reusable procedure.
- Stop before registration when ownership, identity, dependencies, or required evidence is unresolved.

## Output Contract

Use [assets/skill-design-brief-template.md](assets/skill-design-brief-template.md). Provide the classification decision, complete package, resource inventory, test evidence, catalog change, relationship changes, and remaining limitations.

## Guardrails

- Keep `SKILL.md` under 500 lines and progressively disclose detailed knowledge.
- Do not add README, changelog, installation, or quick-reference files inside a skill.
- Do not invent dependencies, evidence, tools, permissions, approval, or maturity.
- Do not overwrite an existing skill or approved behavior without showing the impact.
- Never label a structurally or behaviorally unvalidated skill production-ready.

## Recovery

If evidence is incomplete, create a draft with explicit assumptions and blocked gates. If the proposal conflicts with an existing asset, return the comparison and recommended disposition before editing files.
