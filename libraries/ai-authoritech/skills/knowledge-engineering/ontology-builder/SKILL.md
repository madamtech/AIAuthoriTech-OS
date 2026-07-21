---
name: ontology-builder
description: Model a governed domain through formal concepts, properties, relationships, constraints, axioms, identifiers, provenance, and mappings suitable for knowledge graphs, reasoning, interoperability, or semantic data integration. Use when a taxonomy cannot express required relationship semantics or validation rules. Do not create formal complexity without competency questions, source evidence, maintainers, and validation.
---

# Ontology Builder

1. Define competency questions, use cases, reasoning needs, consumers, domain authority, and risk.
2. Inventory authoritative models and standards; reuse or map them rather than duplicating concepts.
3. Define stable namespaces, classes, properties, domains, ranges, cardinality, constraints, and provenance.
4. Separate conceptual truth, organizational policy, observed facts, and implementation convenience.
5. Model identity, time, versions, uncertainty, exceptions, and conflicting assertions explicitly.
6. Validate logical consistency, satisfiability, competency questions, example data, and prohibited inferences.
7. Test mappings and round trips with consuming systems; document open-world or closed-world assumptions.
8. Version ontology terms and migrations while preserving deprecated identifiers and audit history.
9. Deliver diagrams, machine-readable model specification, examples, validation results, mappings, and governance.

## Rules

- Do not infer sensitive relationships merely because a graph permits them.
- Do not assign the same identifier to concepts with different meanings.
- Do not encode uncertain claims as universally true axioms.
- Do not call a model interoperable until mappings and consumer behavior are tested.
