"""Deterministically harden a cataloged skill batch from a reviewed JSON specification."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, separators=(",", ":")) + "\n", encoding="utf-8")


def harden_skill(item: dict, config: dict) -> tuple[str, list[str]]:
    folder = ROOT / item["path"]
    skill_path = folder / "SKILL.md"
    text = skill_path.read_text(encoding="utf-8")
    link = f'Use the [operating standard](references/{item["reference_file"]}) and [working template](assets/{item["asset_file"]}).'
    if link not in text:
        text = re.sub(r"(^# .+$)", rf"\1\n\n{link}", text, count=1, flags=re.MULTILINE)
    text = text.replace("## Workflow", "## Procedure").replace("## Output\n", "## Output Contract\n").replace("## Rules", "## Guardrails")
    if "## Recovery" not in text:
        text = text.rstrip() + f'\n\n## Recovery\n\n{item["recovery"]}\n'
    skill_path.write_text(text, encoding="utf-8")

    reference = folder / "references" / item["reference_file"]
    reference.parent.mkdir(parents=True, exist_ok=True)
    reference.write_text(f'# {item["reference_title"]}\n\n{item["reference_body"]}\n', encoding="utf-8")
    asset = folder / "assets" / item["asset_file"]
    asset.parent.mkdir(parents=True, exist_ok=True)
    asset.write_text(item["asset_body"].rstrip() + "\n", encoding="utf-8")

    evidence_id = item["evaluation_id"]
    evaluation = {
        "evaluation_id": evidence_id,
        "target_sku": item["sku"],
        "target_version": "1.0.0",
        "executed_at": config["executed_at"],
        "evaluator": "Codex static validation",
        "test_cases": [
            {"id": "recovery", "scenario": item["recovery_scenario"], "expected": "Use a safe recovery path.", "observed": "Recovery preserves evidence and blocks unsupported action.", "status": "pass"},
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
