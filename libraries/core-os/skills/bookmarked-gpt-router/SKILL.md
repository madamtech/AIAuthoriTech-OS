---
name: bookmarked-gpt-router
description: Select and invoke an authorized GPT from the governed bookmark-derived catalog. Use when a request asks to use a bookmarked or shared GPT, names an entry from the GPTs or WMcCraney bookmark folders, or would benefit from an authorized external GPT. Do not use when a repository-native skill can complete the request without an external ChatGPT dependency.
---

# Bookmarked GPT Router

Route requests to authorized external GPTs without representing their uncaptured Builder configuration as repository-native behavior.

## Procedure

1. Read `references/routing-catalog.json` and identify candidates by exact name, folder, and intended outcome.
2. Search the repository skill catalog before selecting an external GPT. Prefer a validated repository-native skill when it is sufficient.
3. If several GPTs fit, choose the narrowest title-derived match. State when confidence is limited because the source configuration is not captured.
4. Confirm that the selected GPT URL opens in the user's authorized ChatGPT session.
5. Provide the request without adding credentials, restricted data, or unrelated private context.
6. Return the selected GPT name, platform GPT ID, result, and limitations.

## Decision Rules

- Treat the user's 2026-08-09 statement as authorization to use and reuse the cataloged GPTs.
- Treat each entry as an external adapter until its behavior is captured and independently validated.
- Do not infer hidden instructions, knowledge files, tools, or actions from a title.
- Do not create a duplicate native skill solely because an external GPT has a different name.
- Escalate to behavior capture when an output contract must be portable across platforms.

## Validation

- Verify the platform GPT ID and URL against the routing catalog.
- Verify accessibility before claiming the GPT was used.
- Check the result against requested format, privacy constraints, and acceptance criteria.
- Record failures as unavailable, missing-input, or behavior-not-captured.

## Output Contract

Return the selected GPT, rationale, access result, output or handoff, and limitations. Distinguish external GPT output from repository-native skill output.

## Guardrails

- Never claim source-equivalent behavior from bookmark metadata alone.
- Never expose credentials, private account state, or restricted information to an external GPT.
- Never edit, publish, unpublish, or change a GPT's sharing settings.

## Recovery

If the GPT cannot be opened, select a verified repository-native fallback or report the unavailable capability. If portability is required, create a behavior-capture and evaluation plan before converting it into a standalone native skill.
