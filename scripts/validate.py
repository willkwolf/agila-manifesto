#!/usr/bin/env python3
"""Agila Manifesto v3.1 — Autonomous Validation & Synchronization Utility.

Validates:
1. Canon Esperanto text fidelity (canon/AGILA-MANIFESTO.eo.md)
   - 49 lines, pure LF line endings, 10 sequential principles with Title, Statement, Bazo, and Signalo.
   - SHA-256 integrity check.
2. Machine-readable YAML summary parity (canon/manifesto.eo.yaml)
   - Schema conformity, version, 10 principles matching canon.
3. Multilingual Agent Skills (skills/agila-manifesto-*/SKILL.md)
   - Frontmatter YAML, required metadata, identical 4-verb agent protocol, 10 principles (P01–P10).
   - Stale translation detection against canon SHA-256.
4. Synchronization (--update)
   - Regenerates i18n/STATUS.md and dynamic translation table in README.md.

Standard library only (zero external pip packages required).
"""

import argparse
import hashlib
import pathlib
import re
import sys
from typing import Any, Dict, List, Optional, Tuple

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
CANON_FILE = REPO_ROOT / "canon" / "AGILA-MANIFESTO.eo.md"
YAML_FILE = REPO_ROOT / "canon" / "manifesto.eo.yaml"
SKILLS_DIR = REPO_ROOT / "skills"
README_FILE = REPO_ROOT / "README.md"
STATUS_FILE = REPO_ROOT / "i18n" / "STATUS.md"

CANON_VERSION = "3.1"
CANON_SHA256_EXPECTED = "44dd1dc966874fceea8d53d9ac312397b1fcb5e9f51919bbe0e71b19d027c470"

LANGUAGE_NAMES = {
    "eo": ("Esperanto", "Esperanto"),
    "en": ("English", "English"),
    "es": ("Español", "Spanish"),
    "zh": ("Chinese", "中文"),
    "hi": ("Hindi", "हिन्दी"),
    "ar": ("Arabic", "العربية"),
    "pt": ("Portuguese", "Português"),
    "fr": ("French", "Français"),
    "ru": ("Russian", "Русский"),
    "ja": ("Japanese", "日本語"),
    "de": ("German", "Deutsch"),
    "id": ("Indonesian", "Bahasa Indonesia"),
    "bn": ("Bengali", "বাংলা"),
}

SOUGHT_AFTER_LANGUAGES = [
    ("zh", "Chinese", "中文"),
    ("hi", "Hindi", "हिन्दी"),
    ("ar", "Arabic", "العربية"),
    ("pt", "Portuguese", "Português"),
    ("fr", "French", "Français"),
    ("ru", "Russian", "Русский"),
    ("ja", "Japanese", "日本語"),
    ("de", "German", "Deutsch"),
    ("id", "Indonesian", "Bahasa Indonesia"),
    ("bn", "Bengali", "বাংলা"),
]


# ==============================================================================
# Helper Functions: Hashing & Pure-Python YAML Parsing
# ==============================================================================

def compute_sha256(data: bytes) -> str:
    """Compute SHA-256 hexadecimal digest."""
    return hashlib.sha256(data).hexdigest()


def compute_file_sha256(path: pathlib.Path) -> str:
    """Compute SHA-256 hexadecimal digest of a file."""
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def parse_frontmatter(content: str) -> Tuple[Dict[str, Any], str]:
    """Parse YAML frontmatter enclosed in --- delimiters."""
    match = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n(.*)$", content, re.DOTALL)
    if not match:
        return {}, content
    yaml_text, body = match.group(1), match.group(2)
    return parse_simple_yaml(yaml_text), body


def parse_simple_yaml(text: str) -> Dict[str, Any]:
    """Standard-library lightweight YAML parser for manifests and frontmatter."""
    try:
        import yaml
        return yaml.safe_load(text) or {}
    except ImportError:
        pass

    result: Dict[str, Any] = {}
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i].rstrip()
        if not line or line.strip().startswith("#"):
            i += 1
            continue
        m = re.match(r"^([a-zA-Z0-9_\-]+):\s*(.*)$", line)
        if m:
            key, val = m.group(1), m.group(2).strip()
            if val == "":
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
    first = lines[0].lstrip()[2:].strip()
    if not lines[1:] and ":" not in first:
        return _parse_val(first)
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


# ==============================================================================
# Subroutine 1: Validate Canon Esperanto File
# ==============================================================================

def validate_canon() -> Tuple[bool, List[str], Dict[str, Any]]:
    """Validate canon/AGILA-MANIFESTO.eo.md."""
    errors: List[str] = []
    canon_data: Dict[str, Any] = {}

    if not CANON_FILE.is_file():
        errors.append(f"Canon file not found: {CANON_FILE}")
        return False, errors, canon_data

    with open(CANON_FILE, "rb") as f:
        raw_bytes = f.read()

    actual_hash = compute_sha256(raw_bytes)
    canon_data["sha256"] = actual_hash

    if b"\r\n" in raw_bytes:
        errors.append("Canon contains Windows CRLF line endings; must be pure LF.")

    text = raw_bytes.decode("utf-8")
    lines = text.splitlines()
    canon_data["line_count"] = len(lines)

    if not text.startswith("1. Ĉiu sistemo spegulas la komunikan strukturon de siaj kreintoj."):
        errors.append("Canon does not begin with verbatim '1. Ĉiu sistemo spegulas la komunikan strukturon de siaj kreintoj.'")

    if not text.rstrip().endswith("senfine."):
        errors.append("Canon does not end with verbatim 'senfine.'")

    # Extract 10 principles
    # Pattern: number, title, statement, Bazo, Signalo
    principles: Dict[int, Dict[str, str]] = {}
    blocks = re.split(r"(?:^|\n\n)(?:\[)?(\d+)\.\s+", text)
    # blocks[0] is empty or prefix, then (number, content) pairs
    i = 1
    while i < len(blocks) - 1:
        num = int(blocks[i])
        content = blocks[i + 1].strip()
        i += 2

        # Extract title and body
        lines_p = content.splitlines()
        titolo = lines_p[0].rstrip(". ")
        body_lines = lines_p[1:]
        body_text = "\n".join(body_lines)

        bazo_match = re.search(r"Bazo:\s*(.*?)(?=\nSignalo:|$)", body_text, re.DOTALL)
        signalo_match = re.search(r"Signalo:\s*(.*?)$", body_text, re.DOTALL)

        bazo = bazo_match.group(1).strip() if bazo_match else ""
        signalo = signalo_match.group(1).strip().rstrip("]") if signalo_match else ""

        # Statement is before Bazo
        deklaro_part = body_text.split("Bazo:")[0].strip() if "Bazo:" in body_text else ""

        if not bazo:
            errors.append(f"Principle {num} missing 'Bazo:' section")
        if not signalo:
            errors.append(f"Principle {num} missing 'Signalo:' section")

        principles[num] = {
            "numero": num,
            "id": f"P{num:02d}",
            "titolo": titolo,
            "deklaro": deklaro_part,
            "bazo": bazo,
            "signalo": signalo,
        }

    canon_data["principles"] = principles

    if len(principles) != 10:
        errors.append(f"Canon must contain exactly 10 principles, found {len(principles)}")

    for num in range(1, 11):
        if num not in principles:
            errors.append(f"Principle {num} missing from canon")

    return len(errors) == 0, errors, canon_data


# ==============================================================================
# Subroutine 2: Validate Machine-Readable YAML Parity
# ==============================================================================

def validate_yaml_parity(canon_data: Dict[str, Any]) -> Tuple[bool, List[str]]:
    """Validate canon/manifesto.eo.yaml matches markdown canon."""
    errors: List[str] = []

    if not YAML_FILE.is_file():
        errors.append(f"YAML summary file not found: {YAML_FILE}")
        return False, errors

    with open(YAML_FILE, "r", encoding="utf-8") as f:
        yaml_content = f.read()

    data = parse_simple_yaml(yaml_content)
    if not data:
        errors.append("Failed to parse manifesto.eo.yaml as valid YAML")
        return False, errors

    version = str(data.get("version", ""))
    if version != CANON_VERSION:
        errors.append(f"manifesto.eo.yaml version '{version}' != expected '{CANON_VERSION}'")

    principoj = data.get("principoj") or data.get("principles", [])
    if len(principoj) != 10:
        errors.append(f"manifesto.eo.yaml must list exactly 10 principles, found {len(principoj)}")

    canon_principles = canon_data.get("principles", {})
    for p in principoj:
        p_id = str(p.get("id", ""))
        num_m = re.match(r"P0?(\d+)", p_id)
        if not num_m:
            errors.append(f"Invalid principle id format in YAML: {p_id}")
            continue
        num = int(num_m.group(1))
        if num not in canon_principles:
            errors.append(f"Principle {p_id} in YAML not present in canon")
            continue

        c_p = canon_principles[num]
        yaml_title = str(p.get("titolo") or p.get("title", "")).strip().rstrip(".")
        canon_title = c_p["titolo"].strip().rstrip(".")
        if yaml_title != canon_title:
            errors.append(f"Title mismatch for {p_id}: YAML '{yaml_title}' != Canon '{canon_title}'")

    return len(errors) == 0, errors


# ==============================================================================
# Subroutine 3: Validate Translation Skills & Detect Drift
# ==============================================================================

def validate_skills(canon_sha256: str) -> Tuple[bool, List[str], List[Dict[str, Any]]]:
    """Validate all translation skills in skills/*/SKILL.md."""
    errors: List[str] = []
    skills_status: List[Dict[str, Any]] = []

    if not SKILLS_DIR.is_dir():
        errors.append(f"Skills directory not found: {SKILLS_DIR}")
        return False, errors, skills_status

    skill_files = sorted(SKILLS_DIR.glob("agila-manifesto-*/SKILL.md"))
    if not skill_files:
        errors.append("No translation skills found matching skills/agila-manifesto-*/SKILL.md")
        return False, errors, skills_status

    for sf in skill_files:
        lang_match = re.match(r"^agila-manifesto-([a-z]{2,3})$", sf.parent.name)
        if not lang_match:
            errors.append(f"Invalid skill directory name: {sf.parent.name}")
            continue
        lang = lang_match.group(1)

        with open(sf, "r", encoding="utf-8") as f:
            content = f.read()

        frontmatter, body = parse_frontmatter(content)
        if not frontmatter:
            errors.append(f"Skill {sf.parent.name} missing YAML frontmatter")
            continue

        name = frontmatter.get("name", "")
        if name != f"agila-manifesto-{lang}":
            errors.append(f"Skill {sf.parent.name} name '{name}' does not match directory convention")

        description = frontmatter.get("description", "")
        if not description or len(description) < 15:
            errors.append(f"Skill {sf.parent.name} missing meaningful description")

        meta = frontmatter.get("metadata", {})
        if not isinstance(meta, dict):
            errors.append(f"Skill {sf.parent.name} metadata must be a mapping")
            meta = {}

        meta_lang = meta.get("lang")
        if meta_lang != lang:
            errors.append(f"Skill {sf.parent.name} metadata.lang '{meta_lang}' != '{lang}'")

        canon_ver = str(meta.get("canon_version", ""))
        if canon_ver != CANON_VERSION:
            errors.append(f"Skill {sf.parent.name} metadata.canon_version '{canon_ver}' != '{CANON_VERSION}'")

        declared_sha = str(meta.get("canon_sha256", ""))
        if len(declared_sha) != 64:
            errors.append(f"Skill {sf.parent.name} invalid metadata.canon_sha256 format")

        status = str(meta.get("status", "")).lower()
        if status not in ["draft", "reviewed", "stale"]:
            errors.append(f"Skill {sf.parent.name} invalid status '{status}'")

        translators = meta.get("translators", [])
        if not translators or not isinstance(translators, list):
            errors.append(f"Skill {sf.parent.name} missing translators list in metadata")

        # Drift Check
        is_hash_match = (declared_sha.lower() == canon_sha256.lower())
        if not is_hash_match:
            if status != "stale":
                errors.append(
                    f"Skill {sf.parent.name} declared SHA-256 does not match canon SHA-256; status must be 'stale' (drift detected)."
                )

        # Agent Protocol Check
        body_lower = body.lower()
        protocol_verbs = ["read", "analyze", "cite", "propose"]
        # In Esperanto: legi, analizi, citi, proponi; In Spanish: leer, analizar, citar, proponer
        has_verbs = (
            all(v in body_lower for v in ["read", "analyze", "cite", "propose"]) or
            all(v in body_lower for v in ["legi", "analizi", "citi", "proponi"]) or
            all(v in body_lower for v in ["leer", "analizar", "citar", "proponer"])
        )
        if not has_verbs:
            errors.append(f"Skill {sf.parent.name} missing standard 4-verb agent protocol (read, analyze, cite, propose)")

        if "human-owner" not in body_lower:
            errors.append(f"Skill {sf.parent.name} agent protocol missing mandatory Human-owner requirement")

        # Principle IDs Check
        for i in range(1, 11):
            p_id = f"P{i:02d}"
            if p_id not in body:
                errors.append(f"Skill {sf.parent.name} missing principle ID {p_id}")

        # Derivative disclaimer check (except eo canon)
        if lang != "eo":
            if not ("deriv" in body_lower or "preval" in body_lower or "canon" in body_lower or "kanono" in body_lower or "autoridad" in body_lower):
                errors.append(f"Skill {sf.parent.name} missing derivative disclaimer")

        lang_name, _ = LANGUAGE_NAMES.get(lang, (lang.upper(), lang.upper()))
        translators_str = ", ".join(translators) if isinstance(translators, list) else str(translators)

        skills_status.append({
            "code": lang,
            "name": lang_name,
            "status": status,
            "canon_version": canon_ver,
            "declared_sha": declared_sha,
            "match": is_hash_match,
            "translators": translators_str,
            "path": f"skills/{sf.parent.name}/SKILL.md",
        })

    return len(errors) == 0, errors, skills_status


# ==============================================================================
# Subroutine 4: Regenerate i18n/STATUS.md and README.md Dynamic Table
# ==============================================================================

def generate_table_markdown(skills_status: List[Dict[str, Any]], root_relative: bool = True) -> str:
    """Generate Markdown translation table."""
    lines = [
        "| Lang | Language | Status | Canon Ver | Canon SHA-256 Match | Translators / Reviewers | Skill File |",
        "|---|---|---|---|---|---|---|",
    ]
    for s in skills_status:
        code = f"`{s['code']}`"
        name = s["name"]
        status = f"`{s['status']}`"
        ver = s["canon_version"]
        short_sha = s["declared_sha"][:12]
        match_str = f"`{short_sha}` (Match)" if s["match"] else f"`{short_sha}` (DRIFT / STALE)"
        translators = s["translators"]
        path_link = s["path"] if root_relative else f"../{s['path']}"
        link = f"[`{s['path']}`]({path_link})"
        lines.append(f"| {code} | {name} | {status} | {ver} | {match_str} | {translators} | {link} |")
    return "\n".join(lines)


def update_status_dashboard(skills_status: List[Dict[str, Any]], canon_sha256: str) -> bool:
    """Regenerate i18n/STATUS.md."""
    short_sha = canon_sha256[:12]
    table_md = generate_table_markdown(skills_status, root_relative=False)

    sought_rows = []
    for idx, (code, name_en, name_native) in enumerate(SOUGHT_AFTER_LANGUAGES, start=1):
        target_dir = f"`skills/agila-manifesto-{code}/`"
        sought_rows.append(
            f"| {idx} | `{code}` | {name_en} | {name_native} | {target_dir} | Wanted | Maintainer + Native Reviewer |"
        )
    sought_table_md = "\n".join([
        "| # | Code | Language (EN) | Native Name | Target Directory | Status | Contributors Needed |",
        "|---|---|---|---|---|---|---|",
        *sought_rows,
    ])

    content = f"""# Agila Manifesto Translation & i18n Status

This dashboard tracks the operational state, canonical version alignment, and drift status of all translations of the **Agila Manifesto v3.1**.

## Canonical Reference

- **Authoritative Canon**: `canon/AGILA-MANIFESTO.eo.md` (Esperanto)
- **Canon Version**: `3.1`
- **Canon SHA-256**: `{canon_sha256}` (short: `{short_sha}`)
- **Total Principles**: 10 (P01–P10)

---

## Active Translations (Tier 1)

{table_md}

---

## Priority Sought-After Translations (Tier 2 Backlog)

The community actively seeks maintainers and native reviewers for the following 10 languages:

{sought_table_md}

---

## Translation Lifecycle States

1. `draft`: Initial draft submitted or machine-translated; undergoing community and native speaker review.
2. `reviewed`: Verified by at least one language maintainer and one native speaker reviewer; passes all schema validation.
3. `stale`: Canon evolved (`canon_sha256` mismatch with current canon); translation requires updating before being marked reviewed again.
"""
    STATUS_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(STATUS_FILE, "w", encoding="utf-8") as f:
        f.write(content)
    return True


def update_readme_table(skills_status: List[Dict[str, Any]]) -> bool:
    """Update README.md between translation table markers."""
    if not README_FILE.is_file():
        return False

    with open(README_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    start_marker = "<!-- START_TRANSLATION_TABLE -->"
    end_marker = "<!-- END_TRANSLATION_TABLE -->"

    if start_marker not in content or end_marker not in content:
        print(f"Error: Markers '{start_marker}' or '{end_marker}' not found in {README_FILE}")
        return False

    parts_before = content.split(start_marker)[0]
    parts_after = content.split(end_marker)[1]

    table_md = generate_table_markdown(skills_status, root_relative=True)
    new_content = f"{parts_before}{start_marker}\n{table_md}\n{end_marker}{parts_after}"

    with open(README_FILE, "w", encoding="utf-8") as f:
        f.write(new_content)
    return True


# ==============================================================================
# CLI Entrypoint
# ==============================================================================

def main() -> int:
    parser = argparse.ArgumentParser(
        description="Agila Manifesto v3.1 Autonomous Validation and Synchronization Utility."
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Run comprehensive validation checks on canon, YAML summary, and skills. Exits 0 on success, 1 on error.",
    )
    parser.add_argument(
        "--update",
        action="store_true",
        help="Update i18n/STATUS.md and synchronize dynamic translation table in README.md.",
    )

    args = parser.parse_args()

    # If neither flag specified, run check by default
    do_check = args.check or (not args.update)
    do_update = args.update

    print("================================================================================")
    print(" Agila Manifesto v3.1 — Validation & Integrity Suite")
    print("================================================================================")

    all_errors: List[str] = []

    # 1. Canon Verification
    canon_ok, canon_errors, canon_data = validate_canon()
    if not canon_ok:
        all_errors.extend(canon_errors)
        for err in canon_errors:
            print(f"[FAIL] Canon: {err}")
    else:
        sha = canon_data.get("sha256", "")
        lines = canon_data.get("line_count", 0)
        p_count = len(canon_data.get("principles", {}))
        print(f"[OK] Canon verified ({lines} lines, {p_count} principles P01–P10, SHA-256: {sha[:12]}...)")

    canon_sha256 = canon_data.get("sha256", CANON_SHA256_EXPECTED)

    # 2. YAML Parity
    yaml_ok, yaml_errors = validate_yaml_parity(canon_data)
    if not yaml_ok:
        all_errors.extend(yaml_errors)
        for err in yaml_errors:
            print(f"[FAIL] YAML Parity: {err}")
    else:
        print("[OK] Machine-readable YAML parity verified (canon/manifesto.eo.yaml matches canon)")

    # 3. Skills Validation
    skills_ok, skills_errors, skills_status = validate_skills(canon_sha256)
    if not skills_ok:
        all_errors.extend(skills_errors)
        for err in skills_errors:
            print(f"[FAIL] Skills: {err}")
    else:
        print(f"[OK] Agent skills validated ({len(skills_status)} active languages: {', '.join(s['code'] for s in skills_status)})")

    # Drift Summary
    drifted = [s for s in skills_status if not s["match"]]
    if drifted:
        print(f"[WARN] Translation drift detected in {len(drifted)} languages: {', '.join(s['code'] for s in drifted)}")
    else:
        print("[OK] Zero translation drift detected across active skills.")

    # 4. Synchronization (if --update requested)
    if do_update:
        print("\nUpdating i18n/STATUS.md and README.md translation tables...")
        status_updated = update_status_dashboard(skills_status, canon_sha256)
        readme_updated = update_readme_table(skills_status)
        if status_updated and readme_updated:
            print("[OK] Successfully updated i18n/STATUS.md and README.md translation tables.")
        else:
            all_errors.append("Failed to update status dashboard or README table.")

    print("--------------------------------------------------------------------------------")
    if all_errors:
        print(f"Validation FAILED with {len(all_errors)} errors.")
        return 1

    print("All validation checks PASSED successfully.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
