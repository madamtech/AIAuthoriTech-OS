---
name: check-gpt-skill-compatibility
description: Evaluate whether a reusable skill can be safely added to a captured AIAuthoriTech GPT without changing its domain purpose or creating instruction, capability, privacy, security, or quality conflicts. Use before any new skill mapping, live GPT instruction change, pilot, or batch deployment.
---

# Check GPT Skill Compatibility

Evaluate one GPT manifest against one proposed skill.

## Gates

1. **Purpose preservation:** The skill is additive and does not replace the GPT's primary job.
2. **Instruction compatibility:** No conflict with locked wording, sequence, intake, output, or refusal rules.
3. **Capability fit:** Required tools exist in the GPT or the skill degrades honestly to a supported output.
4. **Knowledge boundaries:** The skill does not expose, invent, or bypass protected knowledge.
5. **Security and privacy:** No credentials, private prompts, sensitive data, or unauthorized external actions are introduced.
6. **Context fit:** The adapted instruction block is concise enough to avoid crowding out the original configuration.
7. **Quality measurability:** Before/after tests and acceptance criteria can detect improvement and regression.
8. **Rollback:** The original manifest is retained and restoration is practical.

## Decision

Return exactly one decision:

- `compatible`: use the skill without changing its essential workflow.
- `adapt`: use a purpose-specific reduced version and list every required adaptation.
- `reject`: do not deploy; state the blocking conflict.

Include GPT name and ID, skill name, evidence for every gate, proposed instruction delta, required tests, and manual-review items. Do not mark a pairing compatible when evidence is missing.

For Visual Intelligence, also evaluate identity, geometry, typography, production accuracy, one-at-a-time delivery rules, and whether image generation is central or incidental.
