---
name: taxonomy-builder
description: Design and govern hierarchical or faceted classification systems with clear concepts, preferred labels, synonyms, definitions, scope notes, inclusion and exclusion rules, identifiers, mappings, and maintenance ownership. Use for content organization, metadata, navigation, reporting, routing, controlled vocabularies, and search filters. Do not force ontology-like relationships into a simple hierarchy or publish untested labels without stakeholder and corpus validation.
---

# Taxonomy Builder

Create a classification system that users can apply consistently and govern safely.

## Procedure

1. Define users, classification decisions, corpus, navigation and reporting needs, languages, and governance.
2. Reuse authoritative vocabularies where compatible; document licenses, versions, and mappings.
3. Derive concepts from representative evidence and user language, not brainstorming alone.
4. Assign stable nonsemantic IDs, preferred labels, synonyms, definitions, scope notes, examples, and exclusions using [references/taxonomy-standard.md](references/taxonomy-standard.md).
5. Choose hierarchy, facets, polyhierarchy, and depth based on use; prevent cycles and ambiguous parentage.
6. Define rules for multi-label classification, unknowns, deprecated terms, and crosswalks.
7. Test inter-rater agreement, findability, coverage, balance, orphan concepts, and real classification tasks.
8. Version changes; map merged, split, moved, and deprecated concepts without recycling IDs.
9. Deliver taxonomy, term records, mappings, test evidence, governance, migration, and open decisions with [assets/taxonomy-package-template.md](assets/taxonomy-package-template.md).

## Guardrails

- Do not encode confidential, discriminatory, or sensitive attributes without legitimate authorization and controls.
- Do not use labels whose meaning depends only on undocumented institutional knowledge.
- Do not equate search popularity with conceptual correctness.
- Do not delete deprecated concepts while content or integrations still reference them.

## Recovery

If labels, parentage, mappings, or classification rules remain ambiguous or fail
corpus and user testing, keep the affected concepts in draft and preserve current
IDs and mappings. Record disagreements, route them to the named steward, and
publish migration only after affected content and consumers are traced.

## Output Contract

Provide the purpose and corpus, concept scheme, term records, hierarchy and
facets, classification rules, mappings, validation results, governance roles,
version and migration plan, risks, and unresolved decisions.
