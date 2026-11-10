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


def parse_yaml_text(yaml_text: str) -> Dict[str, Any]:
    """Parse basic YAML into python dict/list using PyYAML if present, or stdlib fallback."""
    try:
        import yaml
        return yaml.safe_load(yaml_text) or {}
    except ImportError:
        pass

    # Standard-library lightweight fallback parser for manifest and frontmatters
    result: Dict[str, Any] = {}
    lines = yaml_text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i].rstrip()
        if not line or line.strip().startswith("#"):
            i += 1
            continue
        # top level key: value
        m = re.match(r"^([a-zA-Z0-9_\-]+):\s*(.*)$", line)
        if m:
            key, val = m.group(1), m.group(2).strip()
            if val == "":
                # list or subdict
                sub_lines: List[str] = []
                i += 1
                while i < len(lines) and (lines[i].startswith("  ") or not lines[i].strip()):
                    sub_lines.append(lines[i])
                    i += 1
                result[key] = _parse_yaml_block(sub_lines)
                continue
            else:
                result[key] = _parse_val(val)
        i += 1
    return result


def _parse_val(val: str) -> Any:
    val = val.strip()
    if val.startswith('"') and val.endswith('"') and len(val) >= 2:
        return val[1:-1]
    if val.startswith("'") and val.endswith("'") and len(val) >= 2:
        return val[1:-1]
    if val.lower() == "true":
        return True
    if val.lower() == "false":
        return False
    try:
        return int(val)
    except ValueError:
        pass
    try:
        return float(val)
    except ValueError:
        pass
    return val


def _parse_yaml_block(lines: List[str]) -> Any:
    """Parse an indented YAML block (list or mapping)."""
    # Check if list of items
    non_empty = [ln for ln in lines if ln.strip()]
    if not non_empty:
        return None
    if non_empty[0].lstrip().startswith("- "):
        items: List[Any] = []
        cur_item_lines: List[str] = []
        for ln in lines:
            if ln.lstrip().startswith("- "):
                if cur_item_lines:
                    items.append(_parse_yaml_item(cur_item_lines))
                    cur_item_lines = []
                cur_item_lines.append(ln)
            else:
                cur_item_lines.append(ln)
        if cur_item_lines:
            items.append(_parse_yaml_item(cur_item_lines))
        return items
    else:
        # subdict
        subdict: Dict[str, Any] = {}
        for ln in lines:
            s = ln.strip()
            if not s or s.startswith("#"):
                continue
            m = re.match(r"^([a-zA-Z0-9_\-]+):\s*(.*)$", s)
            if m:
                subdict[m.group(1)] = _parse_val(m.group(2))
        return subdict


def _parse_yaml_item(lines: List[str]) -> Any:
    """Parse single item in a YAML list."""
    first = lines[0].lstrip()[2:].strip()
    if not lines[1:] and ":" not in first:
        return _parse_val(first)
    # Mapping in list item
    item_dict: Dict[str, Any] = {}
    if first and ":" in first:
        k, v = first.split(":", 1)
        item_dict[k.strip()] = _parse_val(v.strip())
    for ln in lines[1:]:
        s = ln.strip()
        if not s or s.startswith("#"):
            continue
        m = re.match(r"^([a-zA-Z0-9_\-]+):\s*(.*)$", s)
        if m:
            item_dict[m.group(1)] = _parse_val(m.group(2))
    return item_dict


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
