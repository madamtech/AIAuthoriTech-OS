#!/usr/bin/env python3
"""Validate the structural delivery contract for a four-color design bundle."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys
import xml.etree.ElementTree as ET


FORBIDDEN = {"image", "linearGradient", "radialGradient", "filter", "pattern", "script"}
EXPECTED_GROUPS = {f"color-{number}" for number in range(1, 5)}


def local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def validate_svg(path: Path) -> list[str]:
    errors: list[str] = []
    try:
        root = ET.parse(path).getroot()
    except (ET.ParseError, OSError) as exc:
        return [f"{path.name}: unreadable SVG ({exc})"]

    if local_name(root.tag) != "svg":
        errors.append(f"{path.name}: root element is not svg")
    if not root.get("viewBox"):
        errors.append(f"{path.name}: missing viewBox")

    found_groups: set[str] = set()
    for element in root.iter():
        name = local_name(element.tag)
        if name in FORBIDDEN:
            errors.append(f"{path.name}: forbidden <{name}> element")
        identifier = element.get("id")
        if name == "g" and identifier in EXPECTED_GROUPS:
            found_groups.add(identifier)
        for attribute in ("href", "{http://www.w3.org/1999/xlink}href"):
            value = element.get(attribute, "")
            if value and not value.startswith("#"):
                errors.append(f"{path.name}: external resource reference")

    missing = sorted(EXPECTED_GROUPS - found_groups)
    if missing:
        errors.append(f"{path.name}: missing groups {', '.join(missing)}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("bundle_directory", type=Path)
    parser.add_argument("expected_count", type=int, nargs="?", default=10)
    args = parser.parse_args()
    if args.expected_count < 1:
        parser.error("expected_count must be at least 1")
    directory = args.bundle_directory
    svg_files = sorted(directory.glob("*.svg"))
    png_files = sorted(directory.glob("*.png"))
    errors: list[str] = []

    if len(svg_files) != args.expected_count:
        errors.append(f"expected {args.expected_count} SVG files, found {len(svg_files)}")
    if len(png_files) != args.expected_count:
        errors.append(f"expected {args.expected_count} PNG files, found {len(png_files)}")
    if {p.stem for p in svg_files} != {p.stem for p in png_files}:
        errors.append("SVG and PNG basenames do not match")
    for svg_file in svg_files:
        errors.extend(validate_svg(svg_file))

    if errors:
        print("Bundle validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Bundle validation passed: {args.expected_count} SVGs, matching PNGs, valid SVG structure.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
