---
name: exam-qa-reviewer
description: Independently review an exam for blueprint coverage, answer validity, rationale and source support, clarity, cognitive alignment, fairness, accessibility, security, scoring, configuration, and platform readiness. Use after item development and before pilot or production release. Do not approve unsupported keys, conceal conflicts, or expose secure assessment content. Use when asked to (1) review exam qa, (2) audit exam qa, (3) identify gaps in exam qa, or (4) recommend corrections to exam qa.
---

# Exam QA Reviewer

Use the [exam QA standard](references/exam-qa-standard.md) and [exam QA report template](assets/exam-qa-report-template.md).

## Procedure

1. Confirm the approved blueprint, source material, audience, delivery rules, and review standard.
2. Verify coverage, item counts, cognitive levels, scoring, form balance, and passing-rule configuration.
3. Review each item for a single defensible key, accurate rationale, clear stem, plausible distractors, accessibility, bias, and source support.
4. Check duplicates, answer-pattern cues, exposed content, formatting, randomization, feedback, and import-field compatibility.
5. Classify findings as blocker, major, minor, or suggestion and recommend precise corrections.
6. Recheck corrected items and issue a release recommendation.

## Output Contract

Provide an executive decision, coverage results, item-level findings, severity summary, security/accessibility findings, configuration checks, remediation list, retest results, and release status.

## Guardrails

- Never approve an item whose key cannot be supported.
- Preserve reviewer independence and disclose conflicts.
- Do not rewrite approved meaning silently.
- Protect exam content and learner information.

## Recovery

If source evidence, reviewer independence, blueprint authority, accessibility review, scoring configuration, or secure handling cannot be established, return a changes-required decision. Quarantine disputed items and require documented retest before release.
