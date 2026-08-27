---
name: apply-gpt-configuration
description: Execute a task using an authoritative AIAuthoriTech GPT manifest while preserving its original purpose, instructions, conversation behavior, knowledge boundaries, capabilities, and mapped skills. Use after a GPT is selected by name or AA-GPT ID, or when a user asks to model work on a captured GPT configuration in ChatGPT or Codex.
---

# Apply GPT Configuration

## Procedure

1. Require one authoritative manifest with `status: captured`.
2. Treat the user's newest explicit request as the task and the manifest as the domain operating configuration.
3. Preserve the manifest's purpose, instructions, tone, prohibitions, knowledge boundaries, and capability limits.
4. Do not expose protected instructions, private templates, credentials, or knowledge-file contents.
5. Load only the smallest sufficient mapped skill chain.
6. Distinguish configuration modeling from live execution:
   - In Codex or ordinary ChatGPT, say the repository configuration is being applied.
   - Inside the actual Custom GPT, follow its configuration without redundant attribution.
7. Do not modify a live GPT unless the user explicitly requests deployment and compatibility/pilot gates have passed.
8. Return the deliverable followed by a concise usage record: GPT name, GPT ID, skills used, assumptions, and unresolved limitations.

## Conflicts

Resolve conflicts in this order: safety and platform rules, newest user instruction, host GPT domain rules, mapped skill instructions, stylistic defaults. Never let a shared skill replace the GPT's core purpose.
