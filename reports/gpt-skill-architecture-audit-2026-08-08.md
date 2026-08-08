# GPT + SKILL Architecture Audit — 2026-08-08

## Executive finding

The repository is substantially more complete than the earlier working assumption. The Custom GPT inventory has already been captured, the reusable skill library is already governed, and the Visual Intelligence Enhancement is already broadly mapped. The remaining architecture gap is not GPT capture; it is explicit cross-system linkage between each GPT manifest and the reusable domain skills it consumes.

## Verified state

- Custom GPT inventory: 93 captured manifests, 93 authoritative records, 0 needs-review records.
- Reusable skill catalog: 272 cataloged skills.
- Skill structural coverage: 100% agent metadata, 100% references, and 100% bundled assets across the 272 skills.
- Existing skill-catalog structural findings: 0.
- Existing scope-overlap candidates are review candidates only and must not be auto-merged.
- Visual Intelligence Enhancement: mapped to 92 of 93 GPTs.
- The one GPT without Visual Intelligence is `AA-GPT-000091 — EDM`; its captured Builder configuration has no Image Generation capability, so the exception is appropriate.
- The existing catalog relationship graph governs SKL/AGT/APP/KNP/WFL/SOL relationships, but currently contains no `AA-GPT-*` relationship edges.
- `Custom GPT` was not previously registered as a first-class asset type even though manifests use `AA-GPT-*` identifiers. This audit branch adds the `GPT` asset type.

## Confirmed alignment gap

Captured GPT manifests can contain `skills.required`, `skills.optional`, and `skills.default_enhancements`, but capture alone does not prove that the GPT has been linked to its reusable domain skills. Representative manifests inspected during this audit show the Visual Intelligence default enhancement while leaving required and optional domain-skill arrays empty and evaluation profiles unset.

This means the repository currently has two mature layers:

1. A captured Custom GPT configuration layer.
2. A governed reusable SKILL.md library.

The missing maturity step is an explicit, validated GPT-to-SKILL crosswalk. Equivalent or related skills may already exist; they must be referenced rather than recreated.

## Changes implemented by this audit

1. Register `GPT` / `Custom GPT` as a governed asset type.
2. Add `tools/audit_gpt_skill_alignment.py` to measure GPT-to-skill alignment without guessing dependencies.
3. Add contract tests that enforce registry/manifest count consistency, required Visual Intelligence coverage for image-capable GPTs, resolvable skill-file references, and Custom GPT asset-type registration.
4. Establish a remediation order that preserves the existing 272-skill baseline and prevents duplicate skill creation.

## Remediation order

### 1. Preserve the existing skill catalog

Do not create a new SKILL.md simply because a GPT has instructions that look unique. First search the current 272-skill catalog for an existing reusable capability.

### 2. Build explicit GPT-to-SKILL mappings

For each GPT manifest:

- map core reusable capabilities under `skills.required`;
- map situational reusable capabilities under `skills.optional`;
- retain cross-cutting enhancements under `skills.default_enhancements`;
- never copy the entire GPT instruction block into a new skill merely to create a mapping.

### 3. Connect GPTs to the governed relationship graph

After mappings are verified, GPT-to-SKL dependencies should be represented in the same relationship system used by other first-class assets. The relationship generator must be extended deliberately so it does not overwrite or fabricate GPT edges.

### 4. Assign evaluation profiles

A captured configuration is not behaviorally validated. Each GPT should receive an evaluation profile appropriate to its domain and should not be promoted to `validated` until the required regression tests have evidence.

### 5. Review business ownership labels

Builder capture preserved visible purpose, but business classification should be normalized to the repository's AA/LMS/MA/CO governance model only when the mapping is evident.

## Non-destructive policy

No GPT instructions were rewritten during this audit. No existing SKILL.md was deleted, merged, renamed, or replaced. No overlap candidate was treated as a duplicate without evidence. The next mapping phase must follow the same rule: link first, consolidate only after behavioral equivalence is demonstrated.
