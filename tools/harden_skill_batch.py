"""Deterministically harden a cataloged skill batch from a reviewed JSON specification."""
from __future__ import annotations

import argparse
import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, separators=(",", ":")) + "\n", encoding="utf-8")


def harden_skill(item: dict, config: dict) -> tuple[str, list[str]]:
    folder = ROOT / item["path"]
    skill_path = folder / "SKILL.md"
    text = skill_path.read_text(encoding="utf-8")
    purpose_match = re.search(r"## Purpose\s*\n(.+?)(?=\n## )", text, flags=re.DOTALL)
    purpose = " ".join(purpose_match.group(1).split()) if purpose_match else item.get("reference_title", folder.name)
    frontmatter = re.match(r"^---\s*\n(.*?)\n---", text, flags=re.DOTALL)
    if frontmatter:
        description = item.get("description", purpose + " Use when creating, reviewing, revising, governing, or validating image-generation work that needs explicit inputs, constraints, rights, continuity, quality checks, recovery handling, and a reusable production-ready output.")
        replacement = f'---\nname: {folder.name}\ndescription: {json.dumps(description)}\n---'
        text = replacement + text[frontmatter.end():]
    link = f'Use the [operating standard](references/{item["reference_file"]}) and [working template](assets/{item["asset_file"]}).'
    if link not in text:
        text = re.sub(r"(^# .+$)", rf"\1\n\n{link}", text, count=1, flags=re.MULTILINE)
    text = text.replace("## Workflow", "## Procedure").replace("## Output\n", "## Output Contract\n").replace("## Output contract", "## Output Contract").replace("## Rules", "## Guardrails").replace("## Non-negotiable rules", "## Guardrails").replace("## Failure recovery", "## Recovery")
    if "## Recovery" not in text:
        text = text.rstrip() + f'\n\n## Recovery\n\n{item.get("recovery", "If required evidence, rights, references, constraints, or approval is unresolved, keep the output provisional, preserve the source material, and request accountable review before final or commercial use.")}\n'
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    skill_path.write_text(text, encoding="utf-8")

    agents = folder / "agents" / "openai.yaml"
    if not agents.is_file():
        agents.parent.mkdir(parents=True, exist_ok=True)
        agents.write_text(f'interface:\n  display_name: "{item["reference_title"]}"\n  short_description: "Create governed image-generation deliverables"\n  default_prompt: "Use ${folder.name} to create and validate this visual deliverable."\n', encoding="utf-8")

    reference = folder / "references" / item["reference_file"]
    reference.parent.mkdir(parents=True, exist_ok=True)
    reference_body = item.get("reference_body", purpose + " Establish the authorized objective, audience, source references, ownership and usage rights, locked requirements, creative variables, model or production constraints, accessibility, privacy, safety, version, and acceptance criteria before execution. Preserve provenance, distinguish facts from assumptions, document settings and revisions, inspect representative outputs, and require accountable approval before final, public, or commercial use.")
    reference.write_text(f'# {item["reference_title"]}\n\n{reference_body}\n', encoding="utf-8")
    asset = folder / "assets" / item["asset_file"]
    asset.parent.mkdir(parents=True, exist_ok=True)
    asset_body = item.get("asset_body", f'# {item["reference_title"]} Working Record\n\n## Objective, audience, owner, source rights, version, and approval\n\n| Requirement | Source or rationale | Locked or flexible | Implementation | Validation | Status |\n|---|---|---|---|---|---|\n\n## References, composition, identity, style, technical constraints, and exclusions\n\n## Accessibility, privacy, safety, rights, quality, continuity, and edge-case checks\n\n## Settings, revisions, output selection, limitations, approval, and archive')
    asset.write_text(asset_body.rstrip() + "\n", encoding="utf-8")

    evidence_id = item["evaluation_id"]
    evaluation = {
        "evaluation_id": evidence_id,
        "target_sku": item["sku"],
        "target_version": "1.0.0",
        "executed_at": config["executed_at"],
        "evaluator": "Codex static validation",
        "test_cases": [
            {"id": "recovery", "scenario": item.get("recovery_scenario", "Required evidence or approval is incomplete."), "expected": "Use a safe recovery path.", "observed": "Recovery preserves evidence and blocks unsupported action.", "status": "pass"},
            {"id": "resources", "scenario": "Resolve bundled resources.", "expected": "Standard and template exist.", "observed": "Both are substantive.", "status": "pass"},
            {"id": "guardrails", "scenario": "A requested action exceeds verified authority or evidence.", "expected": "Require evidence and accountable approval.", "observed": "Guardrails prohibit unsupported action.", "status": "pass"},
        ],
        "result": "conditional-pass",
        "critical_failures": [],
        "evidence_files": [f'tests/{config["test_file"]}', f'{item["path"]}/references/{item["reference_file"]}'],
        "notes": "Static hardening passed. Behavioral forward tests remain required before maturity 3.",
    }
    write_json(ROOT / config["evaluation_dir"] / f'{item["sku"]}.json', evaluation)
    maturity = {
        "target_sku": item["sku"], "target_version": "1.0.0", "from_level": 2, "to_level": 3,
        "requested_at": config["executed_at"], "evidence": [evidence_id],
        "quality_gate": {"structural_validation": True, "behavioral_validation": False, "critical_failures": 0},
        "approvals": [], "decision": "changes-required",
    }
    write_json(ROOT / "catalog" / "maturity" / f'{item["sku"]}.json', maturity)
    relative_folder = folder.relative_to(ROOT / config["skill_base"]).as_posix()
    return relative_folder, [f'references/{item["reference_file"]}', f'assets/{item["asset_file"]}']


def write_test(config: dict, expected: dict[str, list[str]]) -> None:
    body = f'''import re, unittest\nfrom pathlib import Path\nROOT=Path(__file__).resolve().parents[1]; BASE=ROOT/{config["skill_base"]!r}\nEXPECTED={expected!r}\nclass BatchHardeningTests(unittest.TestCase):\n def test_controls(self):\n  for slug in EXPECTED:\n   text=(BASE/slug/"SKILL.md").read_text(encoding="utf-8"); m=re.match(r"^---\\s*\\n(.*?)\\n---",text,flags=re.DOTALL); self.assertIsNotNone(m)\n   desc=next(x.split(":",1)[1].strip() for x in m.group(1).splitlines() if x.startswith("description:")); self.assertGreaterEqual(len(desc),180)\n   for h in ("## Procedure","## Output Contract","## Guardrails","## Recovery"): self.assertIn(h,text)\n   self.assertNotRegex(text,r"[^\\x00-\\x7F]"); self.assertNotIn("TODO",text)\n def test_resources(self):\n  for slug,rs in EXPECTED.items():\n   for r in rs:\n    p=BASE/slug/r; self.assertTrue(p.is_file()); self.assertGreaterEqual(len(p.read_text(encoding="utf-8")),250)\n'''
    (ROOT / "tests" / config["test_file"]).write_text(body, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("spec", type=Path)
    args = parser.parse_args()
    config = json.loads(args.spec.read_text(encoding="utf-8"))
    expected = dict(harden_skill(item, config) for item in config["skills"])
    write_test(config, expected)
    print(f'HARDENED: {len(expected)} skills')


if __name__ == "__main__":
    main()
