# Skill Quality Rubric

## Scoring

| Criterion | Points | Evidence |
|---|---:|---|
| Trigger precision | 20 | Description names the job, concrete activation contexts, and nearby exclusions. |
| Procedure and decisions | 25 | Steps, input handling, decision rules, output contract, validation, and recovery are executable. |
| Resources | 15 | Required resources exist, are linked, non-duplicative, and tested where executable. |
| Safety and authority | 15 | Tool, privacy, security, domain, and external-action boundaries are explicit. |
| Testability | 15 | Representative cases, observable expectations, and executed evidence exist. |
| Metadata and catalog | 10 | Folder, names, UI metadata, identity, version, dependencies, and relationships agree. |

Do not award partial evidence as complete. Record `not evaluated` when a check could not run.

## Severity

- Critical: invalidates approval regardless of score.
- High: can cause incorrect, unsafe, or unusable execution.
- Medium: reduces reliability but has a bounded repair.
- Low: clarity, maintainability, or efficiency improvement.

## Critical failures

- Missing or invalid frontmatter.
- Misleading trigger or incorrect asset classification.
- Fabricated validation, evidence, capability, approval, or maturity.
- Unsafe or unauthorized required action.
- Broken required resource or nonfunctional required script.
- Catalog identity or dependency conflict.

## Gate interpretation

Structural validation proves package shape only. Behavioral validation proves tested outcomes only. Field-tested and enterprise-proven maturity require real-use evidence beyond synthetic tests.
