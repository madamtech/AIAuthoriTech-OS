# AI AuthoriTech OS for Claude

Treat `catalog/assets.json` as the authoritative asset catalog and `catalog/knowledge-index.json` as the searchable index. Select only the smallest relevant set of skills from `libraries/`; do not load the entire repository into one conversation.

For a selected skill, follow its `SKILL.md`, resolve only the supporting files it names, preserve its guardrails, and report unavailable tools or permissions. Do not treat static evaluation evidence as field validation. External bookmarked GPTs are adapters and are not source-equivalent native skills.

Never expose secrets or private knowledge, change repository identifiers, or modify the user's GPTs. Keep repository-wide instructions here and procedures inside their governed skill folders.
