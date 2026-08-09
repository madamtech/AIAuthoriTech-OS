# Cross-Platform Deployment Guide

The GitHub repository is the editable source of truth. Deploy selected skills, not the entire catalog, and keep platform adapters thin.

## ChatGPT

Package the selected skill folder with `SKILL.md`, `agents/openai.yaml`, and only its required `references/`, `scripts/`, and `assets/`. Review for secrets and restricted content before upload. Upload/install status remains pending until the account's Skills interface is accessible and a clean conversation test is completed. The Bookmarked GPT Router remains an external-link adapter unless Builder configurations are captured.

## Codex

Use repository skill folders directly or copy selected governed folders into the user-owned Codex skills location. Preserve `SKILL.md` and `agents/openai.yaml`; do not edit plugin caches. Verify the default prompt triggers the intended skill and run intended-trigger, boundary, missing-input, and missing-tool tests.

## Claude

Use selected skill folders as project knowledge or Claude Code skill sources. Keep procedures in each `SKILL.md`; reserve `CLAUDE.md` for repository-wide instructions. Replace Codex-specific tools with documented Claude equivalents and test scripts in Claude's available runtime.

## Gemini web

Connect or import the private GitHub repository, select the relevant branch, and point Gemini to specific skill folders. Treat imports as snapshots unless synchronization is independently verified. Re-import after repository changes and do not assume write-back capability.

## Gemini CLI

Create and validate `gemini-extension.json` only for a selected distributable library. Keep `SKILL.md` as the portable core and `GEMINI.md` for repository-wide instructions. Installation is pending until the manifest, packaged layout, discovery, and representative execution are tested in an available Gemini CLI runtime.

## Compatibility status

| Platform | Portable core | Adapter/package | Independent runtime test |
|---|---|---|---|
| ChatGPT | Ready | Selective package pending | Pending |
| Codex | Ready | `agents/openai.yaml` available where applicable | Representative static validation complete |
| Claude | Ready | Guidance complete | Pending |
| Gemini web | Ready | Import guidance complete | Pending |
| Gemini CLI | Ready | Extension packaging pending selection | Pending |
