"""Agila Manifesto v3.1 — Shared Test Helpers & Authoritative Constants.

Standard library only (zero third-party dependencies required).
Authoritative source: ORIGINAL_REQUEST.md & PROJECT.md
"""

import hashlib
import os
import pathlib
import re
import subprocess
import sys
from typing import Any, Dict, List, Optional, Tuple

# Base repository root
REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.validate import parse_simple_yaml as parse_yaml_text


def ensure_local_git_exclude() -> None:
    """Ensure local .git/info/exclude contains required patterns to prevent leakage."""
    exclude_path = REPO_ROOT / ".git" / "info" / "exclude"
    if (REPO_ROOT / ".git").is_dir():
        exclude_path.parent.mkdir(parents=True, exist_ok=True)
        existing = ""
        if exclude_path.is_file():
            existing = exclude_path.read_text(encoding="utf-8")
        patterns = [".agents", "TEST_READY.md", "*.prompt", "ORIGINAL_REQUEST.md"]
        missing = [p for p in patterns if p not in existing]
        if missing:
            with open(exclude_path, "a", encoding="utf-8") as f:
                f.write("\n# Agila Manifesto Local Exclusions\n" + "\n".join(missing) + "\n")

ensure_local_git_exclude()

# Authoritative Constants
CANON_VERSION = "3.1"
CANON_VERSION_TAG = "v3.1.0"
CANON_SHA256 = "44dd1dc966874fceea8d53d9ac312397b1fcb5e9f51919bbe0e71b19d027c470"
CANON_BYTE_LENGTH_LF = 6213
CANON_LINE_COUNT = 49
CANON_PRINCIPLES_COUNT = 10

# Conway Attribution: exactly 8 of 10 derive from Conway or its corollaries
CONWAY_DERIVATIONS = {
    1: True,   # P01: Homomorfio de komunika grafo al modula grafo
    2: True,   # P02: Kapacito de decida unuo
    3: True,   # P03: Paktoj trans limoj (preskau dekomponeblaj)
    4: True,   # P04: Observebla interfaco kiel dependeco
    5: True,   # P05: Redundo kontraux ununura punkto de paneo
    6: True,   # P06: Fluon regas atendo cxe transdonoj
    7: True,   # P07: Lernanta sistemo sxangxas sian strukturon
    8: True,   # P08: Agento kiel unuo de la komunika grafo
    9: False,  # P09: Komplekseco, Cynefin, Popper, Goodhart
    10: False, # P10: Lehman-aj legxoj de softvara evoluo
}
CONWAY_DERIVED_COUNT = 8

EXPECTED_SKILL_LANGS = ["eo", "en", "es"]
SOUGHT_AFTER_LANGS = ["zh", "hi", "ar", "pt", "fr", "ru", "ja", "de", "id", "bn"]

README_REQUIRED_SECTIONS = [
    "1. Deliver quality software",
    "2. Badges",
    "3. In 30 seconds",
    "4. The 10 Principles at a Glance",
    "5. Distinctions from the 2001 Agile Manifesto",
    "6. Status, Without Dogma, Minimal Formal Language, Why Esperanto",
    "7. For Humans",
    "8. For AI Agents",
    "9. Governance",
    "10. Languages & Translation Drift",
    "11. How to Contribute",
    "12. Versioning, Citation & License",
    "13. FAQ",
]

GIT_REMOTE_URL = "https://github.com/willkwolf/agila-manifesto.git"


def compute_bytes_sha256(data: bytes) -> str:
    """Compute SHA-256 hex digest of raw bytes."""
    return hashlib.sha256(data).hexdigest()


def compute_file_sha256(path: pathlib.Path) -> str:
    """Compute SHA-256 hex digest of a file."""
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def parse_frontmatter(content: str) -> Tuple[Dict[str, Any], str]:
    """Parse YAML frontmatter enclosed in --- delimiters using pure stdlib regex."""
    match = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n(.*)$", content, re.DOTALL)
    if not match:
        return {}, content
    yaml_text, body = match.group(1), match.group(2)
    return parse_yaml_text(yaml_text), body





def run_python_script(script_relpath: str, *args: str, cwd: Optional[pathlib.Path] = None) -> subprocess.CompletedProcess:
    """Run a python script in subprocess using current python executable."""
    script_path = (cwd or REPO_ROOT) / script_relpath
    cmd = [sys.executable, str(script_path)] + list(args)
    return subprocess.run(
        cmd,
        cwd=str(cwd or REPO_ROOT),
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
