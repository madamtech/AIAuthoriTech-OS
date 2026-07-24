---
name: skill-quality-reviewer
description: Independently review a Codex skill package for trigger precision, scope cohesion, procedural completeness, resources, safety, testability, metadata consistency, catalog integrity, and release readiness. Use when asked to audit, score, approve, reject, compare, or prescribe revisions for a skill before registration, maturity promotion, or release. Do not silently implement repairs unless the user also authorizes changes.
---

# Skill Quality Reviewer

Review evidence, not author intent. Remain independent from the skill's claimed quality.

## Procedure

1. Inventory `SKILL.md`, `agents/openai.yaml`, scripts, references, assets, catalog entry, relationships, test cases, and evaluation evidence.
2. Read [references/quality-rubric.md](references/quality-rubric.md) and identify the requested gate: structural, testing, registration, maturity promotion, or release.
3. Verify folder, frontmatter name, display metadata, SKU, asset ID, version, business, library, status, maturity, and dependency consistency.
4. Test whether the description distinguishes this skill from its nearest catalog neighbors and includes concrete triggers.
5. Evaluate scope, inputs, procedure, decision logic, output contract, validation, recovery, and escalation.
6. Verify every referenced resource exists, is discoverable, is not duplicated unnecessarily, and is appropriate for progressive disclosure.
7. Inspect tool rules, authorization boundaries, sensitive-data handling, unsupported claims, and domain-specific risk.
8. Run official structural validation and every required deterministic script. Treat unexecuted required checks as missing evidence.
9. Evaluate at least the standard, incomplete-input, conflicting-input, unsafe-request, and tool-failure scenarios when applicable.
10. Score only supported evidence; record critical failures separately because they override the numeric score.
11. Return a verdict, score breakdown, evidence inventory, findings by severity, exact revisions, retest requirements, and maturity recommendation.

## Verdict Rules

- **Approve:** score 85 or higher, no critical failure, all required validation passes, and evidence supports the requested gate.
- **Conditional:** score 75-84 with no critical failure and bounded revisions that do not change core scope.
- **Revise:** score below 75 or material workflow, trigger, safety, or resource gaps.
- **Reject:** the asset duplicates another capability, is misclassified, or cannot be made safe or testable within its proposed scope.
- **Blocked:** required files, tools, permissions, or evidence are unavailable.

Missing frontmatter, misleading triggers, fabricated evidence, unsafe authorization, broken required resources, nonfunctional required scripts, or false maturity claims are critical failures.

## Output Contract

Use [assets/skill-review-report-template.md](assets/skill-review-report-template.md). Cite the exact file and evidence for every finding. Separate required corrections from optional improvements.

## Guardrails

- Do not award points for planned or claimed work without evidence.
- Do not change the skill while acting only as reviewer.
- Do not lower a gate to achieve approval.
- Do not infer legal, security, privacy, accessibility, or domain compliance from structural validation alone.

## Recovery

When a check cannot run, preserve every completed review result, mark the affected criterion unevaluated, and return the minimum action needed to resume.
