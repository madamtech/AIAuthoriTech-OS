---
sku: AA-SKL-000167
asset_id: image-generation.model-specific-prompt-adapter.v1
version: 1.0.0
status: testing
---
# Model-Specific Prompt Adapter

## Purpose
Translate a model-neutral visual specification into the syntax, structure, constraints, and iteration strategy best suited to a specific generation or editing model.

## Inputs
Master visual brief, target model/tool, reference capabilities, aspect ratio, editing mode, known limitations, and output target.

## Procedure
Preserve meaning while adapting prompt order, detail density, reference handling, negative prompting, parameter use, text strategy, and edit granularity. Maintain a model capability table and version notes.

## Output contract
Model-ready prompt, parameters, reference instructions, limitations, fallback method, and expected QA risks.

## Rules
Do not remove locked requirements to shorten a prompt. Do not claim unsupported tool capabilities. Treat product and text fidelity as higher-risk areas.

## QA
Compare adapted prompt against the master brief field by field.

## Recovery
Use staged generation/editing or post-production when one-pass prompting cannot meet requirements.
