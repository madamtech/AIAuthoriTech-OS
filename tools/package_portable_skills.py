#!/usr/bin/env python3
"""Build deterministic, reviewable platform packages without duplicating source files."""

from __future__ import annotations

import argparse
import json
import shutil
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SKILLS = [
    "libraries/core-os/skills/skill-router",
    "libraries/core-os/skills/bookmarked-gpt-router",
]


def copy_skill(relative: str, destination: Path) -> None:
    source = ROOT / relative
    if not (source / "SKILL.md").is_file():
        raise ValueError(f"Not a skill package: {relative}")
    shutil.copytree(source, destination / source.name)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="dist/aiauthoritech-core-os")
    parser.add_argument("--zip", action="store_true")
    args = parser.parse_args()
    output = ROOT / args.output
    if output.exists():
        shutil.rmtree(output)
    output.mkdir(parents=True)

    gemini = ROOT / "platforms/gemini/core-os"
    shutil.copy2(gemini / "gemini-extension.json", output / "gemini-extension.json")
    shutil.copy2(gemini / "GEMINI.md", output / "GEMINI.md")
    skills_dir = output / "skills"
    skills_dir.mkdir()
    for skill in DEFAULT_SKILLS:
        copy_skill(skill, skills_dir)

    manifest = {
        "package": "aiauthoritech-core-os",
        "version": "1.0.0",
        "source_repository": "madamtech/AIAuthoriTech-OS",
        "skills": DEFAULT_SKILLS,
        "limitations": [
            "External GPT adapters require an authorized logged-in ChatGPT session.",
            "Packaging does not establish field validation.",
        ],
    }
    (output / "PACKAGE-MANIFEST.json").write_text(
        json.dumps(manifest, indent=2) + "\n", encoding="utf-8"
    )

    if args.zip:
        archive = output.with_suffix(".zip")
        if archive.exists():
            archive.unlink()
        with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED) as bundle:
            for path in sorted(output.rglob("*")):
                if path.is_file():
                    bundle.write(path, path.relative_to(output.parent))
        print(archive.relative_to(ROOT))
    else:
        print(output.relative_to(ROOT))


if __name__ == "__main__":
    main()
