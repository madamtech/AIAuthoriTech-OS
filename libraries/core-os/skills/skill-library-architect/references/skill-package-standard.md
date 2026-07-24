# Skill Package Standard

## Classification

| Asset | Use when |
|---|---|
| Skill | One reusable capability performs one cohesive job. |
| Workflow | Multiple capabilities share state, branches, approval, retry, or recovery. |
| Agent | An autonomous role selects actions or workflows toward a mission. |
| App | Users access capabilities through a software interface and runtime. |
| Template | A reusable output structure is the primary value. |
| Knowledge pack | Curated facts and sources are the primary value. |

## Required package

- `SKILL.md` with only `name` and `description` in frontmatter.
- `agents/openai.yaml` with display name, 25-64 character description, and a default prompt invoking `$skill-name`.
- Scripts, references, and assets only when execution requires them.
- Catalog identity and relationships after validation.

## Trigger test

A description is acceptable when an unfamiliar router can answer:

1. What job does the skill perform?
2. Which concrete requests should activate it?
3. Which nearby capability should handle non-triggers?

## Resource test

- Use a script for deterministic or fragile repeated mechanics.
- Use a reference for detailed, non-obvious, or changing domain knowledge.
- Use an asset when the skill copies or transforms a reusable source deliverable.
- Do not add an empty resource directory.

## Registration gate

Require valid folder identity, frontmatter, UI metadata, resource links, scripts, catalog metadata, dependencies, and tests. Registration does not imply maturity 3 or release approval.
