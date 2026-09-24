---
name: model-specific-prompt-adapter
description: "Translate a model-neutral visual specification into the syntax, structure, constraints, and iteration strategy best suited to a specific generation or editing model. Use when creating, reviewing, revising, governing, or validating image-generation work that needs explicit inputs, constraints, rights, continuity, quality checks, recovery handling, and a reusable production-ready output. Use when asked to (1) create model specific prompt adapter, (2) review model specific prompt adapter, (3) improve model specific prompt adapter, or (4) standardize model specific prompt adapter."
---
# Model-Specific Prompt Adapter

Use the [operating standard](references/operating-standard.md) and [working template](assets/working-record.md).

## Purpose
Translate a model-neutral visual specification into the syntax, structure, constraints, and iteration strategy best suited to a specific generation or editing model.

## Inputs
Master visual brief, target model/tool, reference capabilities, aspect ratio, editing mode, known limitations, and output target.

## Procedure
Preserve meaning while adapting prompt order, detail density, reference handling, negative prompting, parameter use, text strategy, and edit granularity. Maintain a model capability table and version notes.

## Output Contract
Model-ready prompt, parameters, reference instructions, limitations, fallback method, and expected QA risks.

## Guardrails
Do not remove locked requirements to shorten a prompt. Do not claim unsupported tool capabilities. Treat product and text fidelity as higher-risk areas.

## QA
Compare adapted prompt against the master brief field by field.

## Recovery
Use staged generation/editing or post-production when one-pass prompting cannot meet requirements.
