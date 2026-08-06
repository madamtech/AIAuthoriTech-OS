---
name: ai-authoritech-gpt-router
description: Select and load one of Tanika Crawford's registered AIAuthoriTech Custom GPT configurations by exact registry ID, GPT name, or task-purpose match. Use when a user asks to use, recall, combine, locate, list, or choose one of the captured GPTs, or asks which GPT should handle a request. Resolve duplicate names safely and never guess an ambiguous GPT.
---

# AIAuthoriTech GPT Router

Select a GPT configuration; do not silently alter a live GPT.

## Procedure

1. Run `node scripts/route-gpt.mjs --query "<GPT name, ID, or task>"`.
2. For inventory requests, run `node scripts/route-gpt.mjs --list`.
3. If the result is `ambiguous`, present the candidate IDs and ask the user to choose.
4. If confidence is below 0.60, treat the route as provisional and ask one focused question.
5. Read the returned `manifest_path` completely.
6. Use `$apply-gpt-configuration` to execute with that manifest.
7. Load only skills mapped in the manifest or clearly required by the request.
8. For visual work, use `$gpt-visual-intelligence-enhancement` only when mapped and applicable.
9. For a new skill-to-GPT pairing or any live deployment, use `$check-gpt-skill-compatibility` first.
10. State the selected GPT name, registry ID, and activated skills in the result.

## Selection rules

- Prefer an exact registry ID over every other signal.
- Prefer an exact unique name over purpose matching.
- Never choose between duplicate names such as `i-PRO Sales Intelligence` or `Untitled` without an ID or disambiguating context.
- Preserve the selected GPT's domain purpose, instructions, knowledge boundaries, and tool constraints.
- Do not claim the live Custom GPT was invoked. Say the repository configuration was applied unless the user is actually working inside that GPT.

## Data

The skill carries a self-contained snapshot under `references/` so it works both inside the plugin and as a standalone user-level installation. `gpts.json` is the index and `manifests/AA-GPT-NNNNNN.json` contains the flattened authoritative configurations.
