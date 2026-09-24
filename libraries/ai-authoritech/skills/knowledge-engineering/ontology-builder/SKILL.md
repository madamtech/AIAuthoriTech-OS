---
name: ontology-builder
description: Model a governed domain through formal concepts, properties, relationships, constraints, axioms, identifiers, provenance, and mappings suitable for knowledge graphs, reasoning, interoperability, or semantic data integration. Use when a taxonomy cannot express required relationship semantics or validation rules. Do not create formal complexity without competency questions, source evidence, maintainers, and validation. Use when asked to (1) build ontology, (2) refine ontology, (3) validate ontology, or (4) standardize ontology.
---

# Ontology Builder

Model only the semantics required to answer approved competency questions.

## Procedure

1. Define competency questions, use cases, reasoning needs, consumers, domain authority, and risk.
2. Inventory authoritative models and standards; reuse or map them rather than duplicating concepts.
3. Define stable namespaces, classes, properties, domains, ranges, cardinality, constraints, and provenance using [references/ontology-standard.md](references/ontology-standard.md).
4. Separate conceptual truth, organizational policy, observed facts, and implementation convenience.
5. Model identity, time, versions, uncertainty, exceptions, and conflicting assertions explicitly.
6. Validate logical consistency, satisfiability, competency questions, example data, and prohibited inferences.
7. Test mappings and round trips with consuming systems; document open-world or closed-world assumptions.
8. Version ontology terms and migrations while preserving deprecated identifiers and audit history.
9. Deliver diagrams, machine-readable model specification, examples, validation results, mappings, and governance with [assets/ontology-package-template.md](assets/ontology-package-template.md).

## Guardrails

- Do not infer sensitive relationships merely because a graph permits them.
- Do not assign the same identifier to concepts with different meanings.
- Do not encode uncertain claims as universally true axioms.
- Do not call a model interoperable until mappings and consumer behavior are tested.

## Recovery

If the model becomes inconsistent, unsatisfiable, over-infers sensitive facts, or
fails competency questions, stop release and preserve the last valid namespace
and identifiers. Isolate the offending axiom or mapping, rerun logical and
consumer tests, and require steward approval before migration.

## Output Contract

Provide competency questions, source models, namespaces, concepts, properties,
constraints, assumptions, diagrams, machine-readable specification, example
data, validation and inference results, mappings, versioning, and governance.
