# GPT Configuration Management

This directory makes AIAuthoriTech-OS the governed source of truth for GPT configurations.

## Directory contract

- `manifests/` contains one authoritative JSON manifest per verified GPT.
- `discovered/` contains non-authoritative records for GPTs referenced in conversation, notes, screenshots, or other evidence but not yet captured from the live Builder.
- `imports/` contains one-time Builder capture records used to create or update manifests.
- `deployment/` contains runtime-ready instruction packages and deployment notes.
- `changelogs/` records version history for each GPT.

## Truth states

1. `discovered-unverified` — the GPT name or purpose is known, but its live Builder configuration has not been captured.
2. `captured` — instructions, tools, knowledge, actions, and Builder metadata have been recorded.
3. `validated` — the manifest passes schema, mapping, completeness, and behavioral checks.
4. `deployed` — the validated version has been applied to the live runtime.
5. `retired` — the GPT is no longer active but remains auditable.

A discovered record must never be represented as a complete live configuration.

## Required capture fields

Each GPT must record:

- Exact GPT name and purpose
- Current description
- Complete Builder instructions
- Conversation starters
- Enabled capabilities and tools
- Every knowledge file and its repository equivalent
- Every action and schema reference
- Required and optional skills
- Evaluation profile and regression tests
- Runtime location and live GPT URL when available
- Capture evidence, date, verifier, version, and change log

## GPT-to-SKILL alignment contract

A captured GPT and a reusable SKILL.md are different governed assets. Capturing the GPT does not automatically prove that its reusable capabilities have been mapped to the skill catalog.

For every GPT manifest:

- `skills.required` contains reusable domain capabilities the GPT needs for its primary purpose.
- `skills.optional` contains reusable capabilities used only for supported secondary workflows.
- `skills.default_enhancements` contains cross-cutting enhancements that augment the GPT without replacing its role.
- Existing skills must be reused before a new skill is created.
- Full GPT instructions must not be duplicated into a new SKILL.md merely to satisfy a mapping requirement.
- A GPT must not be promoted from `captured` to `validated` until its skill references resolve, its evaluation profile is assigned, and required behavioral tests have evidence.

Use `python tools/audit_gpt_skill_alignment.py --write` to generate the GPT/SKILL alignment report and `--check` to verify that the committed report is current.

## Mandatory GPT Security Hardening default

Every governed GPT must inherit the following global enhancement:

`libraries/core-os/skills/gpt-security-hardening/SKILL.md`

This enhancement is mandatory for all GPT manifests and must appear in `skills.default_enhancements` regardless of domain, business, image capability, tool access, or runtime platform.

The security hardening skill provides defense-in-depth controls for confidential implementation protection, direct and indirect extraction resistance, reconstruction resistance, transformation/encoding resistance, guess-validation resistance, cumulative multi-turn extraction, prompt injection, authority claims, secrets, tool authorization, data minimization, cross-GPT isolation, output leakage review, safe redirects, and clean-room design.

A GPT must not be promoted to `validated` or `deployed` while the mandatory security enhancement is missing unless an explicit repository-governed exception documents equivalent or stronger platform-level controls.

When a GPT is recalled, reconstructed from its manifest, packaged for deployment, or revised from repository truth, the security hardening enhancement must be resolved and applied automatically as part of the default enhancement set. Do not require the operator to remember to request it manually.

Where a runtime cannot dynamically load the full SKILL.md, deployment packaging should include the minimum configure-instructions anchor defined inside the security hardening skill and keep the canonical SKILL.md as the governing source of truth.

## Visual Intelligence default

All image-capable GPTs should map the following enhancement unless a documented exception applies:

`libraries/ai-authoritech/skills/image-generation/gpt-visual-intelligence-enhancement/SKILL.md`

The enhancement is additive. It must not replace the GPT's primary role, business rules, or domain expertise.

## One-time import workflow

1. Open the GPT in ChatGPT Builder.
2. Copy the visible configuration into `imports/<slug>.capture.md` using the capture template.
3. Include screenshots or exported files as evidence when fields cannot be copied.
4. Convert the capture record to `manifests/<slug>/manifest.json`.
5. Validate it against `schemas/gpt-manifest.schema.json`.
6. Map reusable skills and knowledge assets, including the mandatory GPT Security Hardening default enhancement.
7. Run the GPT's evaluation profile.
8. Record deployment and version history.

After this one-time capture, maintain the repository manifest first and use it to prepare future Builder updates.
