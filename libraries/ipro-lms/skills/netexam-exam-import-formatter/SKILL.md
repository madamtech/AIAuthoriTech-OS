---
name: netexam-exam-import-formatter
description: Convert approved exam items into a validated NetExam import package with supported fields, answer keys, rationales, categories, metadata, and encoding. Use after exam QA and before import into a NetExam environment. Use when asked to (1) create netexam exam import formatter, (2) review netexam exam import formatter, (3) improve netexam exam import formatter, or (4) standardize netexam exam import formatter.
---

# NetExam Exam Import Formatter

Use the [operating standard](references/exam-import-standard.md) and [working template](assets/exam-import-template.md).

Prepare import-ready data without changing approved item meaning.

## Procedure

1. Confirm the supported NetExam import template, environment, item types, encoding, delimiter, field limits, and required metadata.
2. Verify each source item has an approved stem, choices, key, rationale, objective, status, and security classification.
3. Map source fields to import columns and normalize line breaks, quotes, special characters, blanks, and identifiers.
4. Reject unsupported item types, duplicate identifiers, invalid keys, missing choices, or truncated content.
5. Generate the import file and a reconciliation manifest.
6. Import only into an authorized test environment, then verify counts, formatting, keys, scoring, categories, and rendering.

## Output Contract

Provide the formatted import package, mapping specification, validation log, rejected-item list, reconciliation totals, post-import test results, and release recommendation.

## Guardrails

- Do not alter answer keys or substantive wording silently.
- Protect secure exam content.
- Verify the exact current NetExam template before formatting.
- Never treat a successful upload as proof of correct rendering or scoring.

## Recovery

If the import schema, item source, encoding, key, scoring, feedback, media path, security, or sandbox evidence is unresolved, do not promote the exam. Quarantine invalid rows and require rendered and scored test evidence.
