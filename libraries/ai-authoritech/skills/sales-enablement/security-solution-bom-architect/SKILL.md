---
name: security-solution-bom-architect
description: Translate validated security-system discovery inputs into a structured bill of materials using governed configuration rules, quantities, dependencies, and source references.
---

# Security Solution BOM Architect

## Procedure

1. Validate required discovery inputs and reject missing or invalid quantities instead of autofilling.
2. Apply documented configuration logic to select models, licenses, hardware, accessories, and quantity relationships.
3. Return a BOM with assumptions, source references, alternates when required, and unresolved configuration questions.

## Output Contract

Provide verified inputs, assumptions, findings or calculations, recommendations or output, unresolved questions, approval/validation needs, and next actions appropriate to the sales task.

## Guardrails

- Never invent SKUs, quantities, compatibility, licensing, or configuration rules.
- Use approved price lists, configuration documents, or user-provided rules as the source of truth.
- Keep BOM generation separate from final pricing approval.

## Recovery

If critical source data, authority, product evidence, pricing, customer facts, or decision criteria are missing, stop at the affected boundary. Preserve verified work, label the gap, and request only the minimum information or authorized review needed to continue.
