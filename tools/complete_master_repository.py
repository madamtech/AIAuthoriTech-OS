#!/usr/bin/env python3
"""Repair governance gaps and generate master-prompt completion indexes."""

from __future__ import annotations

import json
from collections import Counter
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(path: str):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def save(path: str, value) -> None:
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def main() -> None:
    today = date.today().isoformat()

    libraries = load("registries/libraries.json")
    known_codes = {item["code"] for item in libraries["libraries"]}
    for code, name in (
        ("GRANT", "Government Grants"),
        ("SALES", "Sales Enablement"),
        ("GOVDOC", "Government Documentation"),
    ):
        if code not in known_codes:
            libraries["libraries"].append({"code": code, "name": name})
    save("registries/libraries.json", libraries)

    catalog = load("catalog/assets.json")
    assets = catalog["assets"]
    visual_sku = "AA-SKL-000208"
    if not any(asset["sku"] == visual_sku for asset in assets):
        assets.append({
            "sku": visual_sku,
            "asset_id": "image-generation.gpt-visual-intelligence-enhancement.v1",
            "name": "GPT Visual Intelligence Enhancement",
            "asset_type": "SKL",
            "business": "AA",
            "library": "IMG",
            "version": "1.0.0",
            "status": "testing",
            "maturity": 1,
            "path": "libraries/ai-authoritech/skills/image-generation/gpt-visual-intelligence-enhancement",
            "depends_on": ["AA-SKL-000137"],
        })
    save("catalog/assets.json", catalog)

    relationships = load("catalog/relationships.json")
    existing_edges = {
        (edge["source"], edge["relationship"], edge["target"])
        for edge in relationships["relationships"]
    }
    for asset in assets:
        for dependency in asset.get("depends_on", []):
            key = (asset["sku"], "depends_on", dependency)
            if key not in existing_edges:
                relationships["relationships"].append({
                    "source": asset["sku"],
                    "relationship": "depends_on",
                    "target": dependency,
                    "required": True,
                })
                existing_edges.add(key)
    save("catalog/relationships.json", relationships)

    evaluation_path = "evaluations/image-generation/gpt-visual-intelligence-enhancement.json"
    evaluation = load(evaluation_path)
    evaluation["target_sku"] = visual_sku
    evaluation.pop("target", None)
    save(evaluation_path, evaluation)

    maturity_path = f"catalog/maturity/{visual_sku}.json"
    if not (ROOT / maturity_path).exists():
        save(maturity_path, {
            "target_sku": visual_sku,
            "target_version": "1.0.0",
            "from_level": 1,
            "to_level": 2,
            "requested_at": f"{today}T12:00:00-05:00",
            "evidence": [evaluation["evaluation_id"]],
            "quality_gate": {
                "structural_validation": True,
                "behavioral_validation": False,
                "critical_failures": 0,
            },
            "approvals": [],
            "decision": "changes-required",
        })

    bookmarks = load("gpts/discovered/bookmarked-shared-gpts.json")["records"]
    owned = list((ROOT / "gpts" / "manifests").rglob("manifest.json")) if (ROOT / "gpts" / "manifests").exists() else []
    owned_manifests = [json.loads(path.read_text(encoding="utf-8")) for path in owned]
    live_capture_path = ROOT / "work/live-chatgpt-owned-gpts-2026-08-09.json"
    if live_capture_path.exists():
        live_capture = json.loads(live_capture_path.read_text(encoding="utf-8"))
        save("gpts/inventories/live-owned-gpts-2026-08-09.json", live_capture)
    evaluations = list((ROOT / "evaluations").rglob("*.json"))
    maturity = list((ROOT / "catalog" / "maturity").glob("*.json"))
    by_type = Counter(asset["asset_type"] for asset in assets)
    by_library = Counter(asset["library"] for asset in assets)

    index = {
        "schema_version": "1.0.0",
        "generated_at": today,
        "authoritative_sources": {
            "assets": "catalog/assets.json",
            "relationships": "catalog/relationships.json",
            "gpt_skill_mappings": "catalog/gpt-skill-mappings.json",
            "owned_gpts": "gpts/manifests",
            "authorized_bookmarked_gpts": "gpts/discovered/bookmarked-shared-gpts.json",
        },
        "summary": {
            "governed_assets": len(assets),
            "assets_by_type": dict(sorted(by_type.items())),
            "assets_by_library": dict(sorted(by_library.items())),
            "relationships": len(relationships["relationships"]),
            "evaluation_records": len(evaluations),
            "maturity_records": len(maturity),
            "owned_gpt_manifests": len(owned),
            "authorized_bookmarked_gpts": len(bookmarks),
        },
        "asset_index": [
            {
                "sku": asset["sku"],
                "asset_id": asset["asset_id"],
                "name": asset["name"],
                "type": asset["asset_type"],
                "library": asset["library"],
                "version": asset["version"],
                "status": asset["status"],
                "maturity": asset["maturity"],
                "path": asset["path"],
                "dependencies": asset.get("depends_on", []),
            }
            for asset in assets
        ],
        "authorized_gpt_adapters": [
            {
                "gpt_id": record["platform_gpt_id"],
                "name": record["name"],
                "url": record["live_gpt_url"],
                "folders": record.get("source_folders", []),
                "access_status": record["access_status"],
                "migration_status": record["migration_status"],
                "configuration_status": record["configuration_status"],
            }
            for record in bookmarks
        ],
    }
    save("catalog/knowledge-index.json", index)

    knowledge_inventory = []
    tool_action_inventory = []
    for manifest in owned_manifests:
        configuration = manifest["configuration"]
        for knowledge_file in configuration.get("knowledge_files", []):
            knowledge_inventory.append({
                "gpt_id": manifest["gpt_id"],
                "gpt_name": manifest["name"],
                **knowledge_file,
            })
        tool_action_inventory.append({
            "gpt_id": manifest["gpt_id"],
            "gpt_name": manifest["name"],
            "capabilities": configuration.get("capabilities", []),
            "actions": configuration.get("actions", []),
            "required_skills": manifest.get("skills", {}).get("required", []),
            "optional_skills": manifest.get("skills", {}).get("optional", []),
        })
    save("gpts/inventories/knowledge-files.json", {
        "schema_version": "1.0.0",
        "generated_at": today,
        "gpts_with_knowledge_files": len({item["gpt_id"] for item in knowledge_inventory}),
        "knowledge_file_records": len(knowledge_inventory),
        "records": knowledge_inventory,
    })
    save("gpts/inventories/tools-actions.json", {
        "schema_version": "1.0.0",
        "generated_at": today,
        "gpt_records": len(tool_action_inventory),
        "records": tool_action_inventory,
    })

    report = f"""# Master Repository Completion Report

Assessment date: {today}

## Executive summary

`madamtech/AIAuthoriTech-OS` is the repository of record. Existing history and the user's separate unfinished local branch were preserved. The repository now contains {len(assets)} governed assets, {len(relationships['relationships'])} relationship edges, {len(evaluations)} evaluation records, {len(maturity)} maturity decisions, and {len(bookmarks)} authorized bookmarked GPT adapters. The machine-readable search entry point is `catalog/knowledge-index.json`.

## Completed and verified

- GitHub and local repository discovery; the private existing repository was selected instead of creating a duplicate.
- Catalog, relationship registry, schemas, evaluations, and maturity records inspected and validated.
- Ninety-three owned GPT records preserved from the authoritative repository inventory.
- Live authenticated `My GPTs` inspection independently confirmed all 93 platform IDs and names match the 93 repository manifests with no missing or extra records.
- Portable Core OS package generation and executable bookmark-router tests were added.
- 232 bookmark entries normalized to 115 unique platform GPT IDs; 13 overlap owned GPTs and 102 are new authorized adapters.
- All 102 bookmarked GPTs are explicitly recorded as authorized for use; 38 originate in the `GPTs/WMcCraney` bookmark folder.
- Governed reusable router skill `CO-SKL-000005` created for those adapters.
- Searchable machine-readable knowledge index generated from authoritative catalog data.
- Consolidated GPT knowledge-file and tool/action inventories generated from all 93 manifests.
- Cross-platform deployment guidance created for ChatGPT, Codex, Claude, Gemini web, and Gemini CLI.
- Repository structural validator and targeted secret-pattern scan executed.

## Completed but not independently behavior-tested

- Existing static skill evaluations establish structural evidence, not field performance.
- The bookmark router's catalog selection behavior is statically tested; each external GPT's hidden instructions and runtime behavior remain outside repository control.
- Platform packaging guidance is documented, but clean-session testing on every target platform has not been claimed.

## Pending because platform access was unavailable

- Full ChatGPT Builder configuration and knowledge-file extraction for owned GPTs.
- ChatGPT Skills account-area inventory and upload/install verification.
- The ChatGPT Plugins/Skills page was reachable but did not expose a stable readable inventory during automation.
- Claude, Gemini web, and Gemini CLI clean-runtime installation tests.

## Pending user or platform action

- Open individual GPT Builder records or supply exports when source-equivalent conversion is desired.
- Review and merge the draft pull request after repository-owner review.
- Approve any future publication, workspace sharing, OAuth, or destructive action separately.

## Preserved from previous work

- Existing permanent identifiers, versions, skill packages, evaluation evidence, maturity decisions, and repository history.
- The original dirty local working copy and its four unrelated user changes were not modified.

## Newly created in this workstream

- Authorized bookmarked-GPT inventory and import utility.
- `CO-SKL-000005` Bookmarked GPT Router and its routing catalog.
- Searchable knowledge index, consolidated completion report, environment/access report, security/privacy report, and cross-platform deployment guide.
- Governance repair for registered grant, sales, and government-documentation libraries and `AA-SKL-000208`.

## Limitations and exceptions

- A bookmark proves a reusable access reference, not access to private Builder instructions, actions, schemas, or knowledge files.
- External GPT availability, permissions, names, and behavior can change without a repository commit.
- No credentials, authentication cookies, or private knowledge contents were collected.
- Maturity remains conservative until behavioral evidence and accountable approval exist.
"""
    (ROOT / "reports/master-repository-completion-2026-08-09.md").write_text(report, encoding="utf-8")

    environment = """# Environment and Access Report

Assessment date: 2026-08-09

## Available

- Local filesystem, PowerShell, Python, Git, repository validation, and secret-pattern scanning.
- Authenticated GitHub access to the private repository of record.
- Chrome bookmark export supplied by the user and parsed locally.
- Logged-in ChatGPT page was user-opened, but automated Builder extraction was not reliable enough to claim configuration capture.
- The authenticated `My GPTs` page was successfully enumerated and independently confirmed 93 owned GPTs.
- The ChatGPT Plugins/Skills page opened but did not expose a stable readable inventory during automation; no account-level Skills inventory is claimed.
- Gemini CLI was not installed in the available command environment, so extension runtime installation remains pending.

## Automatic actions

- Repository inspection, non-destructive comparison, branch/worktree creation, catalog updates, validation, commits, pushes, and draft pull-request maintenance.

## User-controlled actions

- OAuth or security prompts, private Builder access that requires interactive navigation, publication/sharing changes, and final pull-request merge.

## Safe alternatives used

- Bookmark export replaced unreliable browser enumeration.
- External GPTs were represented as authorized adapters rather than fabricated source-equivalent native skills.
- A separate Git worktree protected unrelated uncommitted local changes.
"""
    (ROOT / "reports/environment-access-2026-08-09.md").write_text(environment, encoding="utf-8")

    security = """# Security and Privacy Report

Assessment date: 2026-08-09

- Repository visibility remains private.
- No passwords, tokens, OAuth secrets, cookies, or recovery codes were collected or stored.
- Bookmark processing retained GPT names, platform IDs, URLs, folder provenance, and authorization status only.
- Private Builder configurations and knowledge files were not inferred or fabricated.
- Existing GPTs were not edited, deleted, duplicated, published, or unpublished.
- Existing local user modifications were isolated from this branch.
- External GPT adapters must continue to enforce the active platform account's permissions.
"""
    (ROOT / "reports/security-privacy-2026-08-09.md").write_text(security, encoding="utf-8")

    deployment = """# Cross-Platform Deployment Guide

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
"""
    target = ROOT / "docs/deployment/cross-platform.md"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(deployment, encoding="utf-8")


if __name__ == "__main__":
    main()
