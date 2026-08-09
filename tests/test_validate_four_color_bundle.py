from pathlib import Path
import subprocess
import sys


SCRIPT = (
    Path(__file__).parents[1]
    / "libraries"
    / "ai-authoritech"
    / "skills"
    / "image-generation"
    / "four-color-3d-design-bundle"
    / "scripts"
    / "validate_bundle.py"
)


def make_bundle(directory: Path) -> None:
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
<g id="color-1"><path fill="#111111" d="M0 0h25v100H0z"/></g>
<g id="color-2"><path fill="#333333" d="M25 0h25v100H25z"/></g>
<g id="color-3"><path fill="#777777" d="M50 0h25v100H50z"/></g>
<g id="color-4"><path fill="#FFFFFF" d="M75 0h25v100H75z"/></g>
</svg>"""
    for number in range(1, 11):
        stem = f"{number:02d}-design"
        (directory / f"{stem}.svg").write_text(svg, encoding="utf-8")
        (directory / f"{stem}.png").write_bytes(b"PNG fixture")


def test_valid_bundle_passes(tmp_path: Path) -> None:
    make_bundle(tmp_path)
    result = subprocess.run([sys.executable, str(SCRIPT), str(tmp_path)], capture_output=True, text=True)
    assert result.returncode == 0, result.stdout + result.stderr


def test_embedded_raster_fails(tmp_path: Path) -> None:
    make_bundle(tmp_path)
    target = tmp_path / "01-design.svg"
    target.write_text(target.read_text(encoding="utf-8").replace("</svg>", '<image href="art.png"/></svg>'), encoding="utf-8")
    result = subprocess.run([sys.executable, str(SCRIPT), str(tmp_path)], capture_output=True, text=True)
    assert result.returncode == 1
    assert "forbidden <image>" in result.stdout
