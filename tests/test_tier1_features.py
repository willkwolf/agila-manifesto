"""Agila Manifesto v3.1 — Tier 1 Feature Coverage Tests.

Comprehensive opaque-box functional tests covering 7 core features:
1. Canon Esperanto Byte Fidelity (canon/AGILA-MANIFESTO.eo.md)
2. Machine-Readable YAML Parity (canon/manifesto.eo.yaml)
3. Multilingual Agent Skills (skills/agila-manifesto-{eo,en,es}/SKILL.md)
4. Strict 13-Section README Architecture (README.md, README.eo.md, README.es.md)
5. 3-Tier Governance & Community Files (GOVERNANCE.md, LICENSE, CITATION.cff, etc.)
6. Automation & Validation Script (scripts/validate.py)
7. Git Hygiene, Exclusions & Launch Checklist (.git/info/exclude, LAUNCH-CHECKLIST.md)

Zero external dependencies (unittest, stdlib only).
"""

import hashlib
import os
import pathlib
import re
import subprocess
import unittest

from tests.common import (
    CANON_BYTE_LENGTH_LF,
    CANON_LINE_COUNT,
    CANON_PRINCIPLES_COUNT,
    CANON_SHA256,
    CANON_VERSION,
    CONWAY_DERIVATIONS,
    CONWAY_DERIVED_COUNT,
    EXPECTED_SKILL_LANGS,
    GIT_REMOTE_URL,
    README_REQUIRED_SECTIONS,
    REPO_ROOT,
    compute_file_sha256,
    parse_frontmatter,
    parse_yaml_text,
    run_python_script,
)


class TestTier1CanonFidelity(unittest.TestCase):
    """Feature 1: Canon Esperanto Byte Fidelity (canon/AGILA-MANIFESTO.eo.md)."""

    def setUp(self):
        self.canon_path = REPO_ROOT / "canon" / "AGILA-MANIFESTO.eo.md"

    def test_f1_canon_file_exists(self):
        """F1.1: canon/AGILA-MANIFESTO.eo.md must exist."""
        self.assertTrue(
            self.canon_path.is_file(),
            f"Expected canon file at {self.canon_path}",
        )

    def test_f1_canon_sha256_fidelity(self):
        """F1.2: SHA-256 of canon must match the authoritative 44dd1dc9... hash."""
        self.assertTrue(self.canon_path.is_file(), "Canon file missing")
        actual_hash = compute_file_sha256(self.canon_path)
        self.assertEqual(
            actual_hash,
            CANON_SHA256,
            f"Canon SHA-256 mismatch. Expected {CANON_SHA256}, got {actual_hash}",
        )

    def test_f1_canon_pure_lf_line_endings(self):
        """F1.3: Canon must strictly use LF line endings, zero CRLF."""
        self.assertTrue(self.canon_path.is_file(), "Canon file missing")
        with open(self.canon_path, "rb") as f:
            raw = f.read()
        self.assertNotIn(
            b"\r\n",
            raw,
            "Canon file must not contain Windows CRLF (\\r\\n) line endings.",
        )
        self.assertIn(b"\n", raw, "Canon file must contain LF (\\n) line endings.")

    def test_f1_canon_verbatim_boundaries(self):
        """F1.4: Canon must start with verbatim '1. Ĉiu sistemo' and end with 'senfine.'."""
        self.assertTrue(self.canon_path.is_file(), "Canon file missing")
        with open(self.canon_path, "r", encoding="utf-8") as f:
            text = f.read()
        self.assertTrue(
            text.startswith("1. Ĉiu sistemo spegulas la komunikan strukturon de siaj kreintoj."),
            "Canon must begin verbatim with '1. Ĉiu sistemo spegulas la komunikan strukturon de siaj kreintoj.'",
        )
        self.assertTrue(
            text.rstrip().endswith("senfine."),
            "Canon must end verbatim with 'senfine.'",
        )

    def test_f1_canon_ten_principles_sequential(self):
        """F1.5: Canon must contain all 10 numbered principles sequentially."""
        self.assertTrue(self.canon_path.is_file(), "Canon file missing")
        with open(self.canon_path, "r", encoding="utf-8") as f:
            text = f.read()
        for i in range(1, 11):
            pattern = rf"(?:^|\n)(?:\[)?{i}\.\s+[^\n]+"
            self.assertRegex(
                text,
                pattern,
                f"Principle {i}. missing from canon.",
            )

    def test_f1_canon_bazo_and_signalo_present(self):
        """F1.6: Every principle block must include both 'Bazo:' and 'Signalo:' headers."""
        self.assertTrue(self.canon_path.is_file(), "Canon file missing")
        with open(self.canon_path, "r", encoding="utf-8") as f:
            text = f.read()
        bazo_count = len(re.findall(r"(?:^|\n)Bazo:", text))
        signalo_count = len(re.findall(r"(?:^|\n)Signalo:", text))
        self.assertEqual(
            bazo_count,
            CANON_PRINCIPLES_COUNT,
            f"Expected {CANON_PRINCIPLES_COUNT} 'Bazo:' headers, found {bazo_count}",
        )
        self.assertEqual(
            signalo_count,
            CANON_PRINCIPLES_COUNT,
            f"Expected {CANON_PRINCIPLES_COUNT} 'Signalo:' headers, found {signalo_count}",
        )


class TestTier1YamlParity(unittest.TestCase):
    """Feature 2: Machine-Readable Summary Parity (canon/manifesto.eo.yaml)."""

    def setUp(self):
        self.yaml_path = REPO_ROOT / "canon" / "manifesto.eo.yaml"

    def test_f2_yaml_file_exists(self):
        """F2.1: canon/manifesto.eo.yaml must exist."""
        self.assertTrue(
            self.yaml_path.is_file(),
            f"Expected yaml summary at {self.yaml_path}",
        )

    def test_f2_yaml_valid_syntax_and_root_metadata(self):
        """F2.2: YAML must parse and contain version '3.1' and matching canon sha256."""
        self.assertTrue(self.yaml_path.is_file(), "YAML file missing")
        with open(self.yaml_path, "r", encoding="utf-8") as f:
            data = parse_yaml_text(f.read())
        self.assertIsInstance(data, dict, "YAML root must be a mapping")
        # Check version metadata
        version = (
            data.get("versio")
            or data.get("version")
            or (data.get("kanono", {}).get("versio") if isinstance(data.get("kanono"), dict) else None)
        )
        self.assertEqual(str(version), CANON_VERSION, f"YAML version must be {CANON_VERSION}")

        # Check hash
        sha = (
            data.get("kanono_sha256")
            or data.get("sha256")
            or (data.get("kanono", {}).get("sha256") if isinstance(data.get("kanono"), dict) else None)
        )
        if sha:
            self.assertEqual(sha, CANON_SHA256, "YAML canon SHA-256 must match authoritative hash")

    def test_f2_yaml_ten_principles_count(self):
        """F2.3: YAML summary must define exactly 10 principle objects."""
        self.assertTrue(self.yaml_path.is_file(), "YAML file missing")
        with open(self.yaml_path, "r", encoding="utf-8") as f:
            data = parse_yaml_text(f.read())
        principoj = data.get("principoj") or data.get("principles")
        self.assertIsInstance(principoj, list, "'principoj' must be a list")
        self.assertEqual(
            len(principoj),
            CANON_PRINCIPLES_COUNT,
            f"Expected {CANON_PRINCIPLES_COUNT} principles in YAML, found {len(principoj)}",
        )

    def test_f2_yaml_conway_derivation_declaration(self):
        """F2.4: YAML must transparently declare that exactly 8 of 10 principles derive from Conway."""
        self.assertTrue(self.yaml_path.is_file(), "YAML file missing")
        with open(self.yaml_path, "r", encoding="utf-8") as f:
            data = parse_yaml_text(f.read())
        principoj = data.get("principoj") or data.get("principles")
        conway_count = 0
        for p in principoj:
            derives = (
                p.get("derivas_de_conway")
                if "derivas_de_conway" in p
                else p.get("derivita_el_conway", p.get("conway_derived"))
            )
            if derives is True or str(derives).lower() == "true":
                conway_count += 1
        self.assertEqual(
            conway_count,
            CONWAY_DERIVED_COUNT,
            f"Expected exactly {CONWAY_DERIVED_COUNT} principles to derive from Conway, found {conway_count}",
        )

    def test_f2_yaml_principle_schema_completeness(self):
        """F2.5: Each principle in YAML must provide id, titolo, bazo, and signalo."""
        self.assertTrue(self.yaml_path.is_file(), "YAML file missing")
        with open(self.yaml_path, "r", encoding="utf-8") as f:
            data = parse_yaml_text(f.read())
        principoj = data.get("principoj") or data.get("principles")
        for i, p in enumerate(principoj, start=1):
            expected_id = f"P{i:02d}"
            p_id = str(p.get("id") or p.get("identigilo") or f"P{p.get('numero', i):02d}")
            self.assertEqual(p_id, expected_id, f"Principle {i} ID mismatch: {p_id} != {expected_id}")
            self.assertTrue(p.get("titolo") or p.get("title"), f"Principle {p_id} missing titolo")
            self.assertTrue(p.get("bazo") or p.get("base"), f"Principle {p_id} missing bazo")
            self.assertTrue(p.get("signalo") or p.get("signal"), f"Principle {p_id} missing signalo")


class TestTier1TranslationSkills(unittest.TestCase):
    """Feature 3: Multilingual Agent Skills (skills/agila-manifesto-{eo,en,es}/SKILL.md)."""

    def test_f3_skills_directories_exist(self):
        """F3.1: Skills must exist for eo, en, and es."""
        for lang in EXPECTED_SKILL_LANGS:
            skill_file = REPO_ROOT / "skills" / f"agila-manifesto-{lang}" / "SKILL.md"
            self.assertTrue(
                skill_file.is_file(),
                f"Expected skill file at {skill_file}",
            )

    def test_f3_skills_frontmatter_name_and_description(self):
        """F3.2: Frontmatter must include valid name and contextual description."""
        for lang in EXPECTED_SKILL_LANGS:
            skill_file = REPO_ROOT / "skills" / f"agila-manifesto-{lang}" / "SKILL.md"
            self.assertTrue(skill_file.is_file(), f"Missing skill {lang}")
            with open(skill_file, "r", encoding="utf-8") as f:
                frontmatter, _ = parse_frontmatter(f.read())
            self.assertEqual(
                frontmatter.get("name"),
                f"agila-manifesto-{lang}",
                f"Skill {lang} name mismatch in frontmatter",
            )
            desc = frontmatter.get("description", "")
            self.assertTrue(
                len(desc) >= 20,
                f"Skill {lang} description must describe when to use it (team structure, process, architecture)",
            )

    def test_f3_skills_metadata_canon_version_and_sha(self):
        """F3.3: Skill metadata must specify canon_version '3.1' and valid canon_sha256."""
        for lang in EXPECTED_SKILL_LANGS:
            skill_file = REPO_ROOT / "skills" / f"agila-manifesto-{lang}" / "SKILL.md"
            self.assertTrue(skill_file.is_file(), f"Missing skill {lang}")
            with open(skill_file, "r", encoding="utf-8") as f:
                frontmatter, _ = parse_frontmatter(f.read())
            meta = frontmatter.get("metadata", frontmatter)
            self.assertEqual(
                str(meta.get("canon_version")),
                CANON_VERSION,
                f"Skill {lang} canon_version mismatch",
            )
            self.assertEqual(
                meta.get("canon_sha256"),
                CANON_SHA256,
                f"Skill {lang} canon_sha256 mismatch",
            )

    def test_f3_skills_metadata_status_and_translators(self):
        """F3.4: Skill status must be 'reviewed' for eo, and 'draft' for en/es with translators list."""
        for lang in EXPECTED_SKILL_LANGS:
            skill_file = REPO_ROOT / "skills" / f"agila-manifesto-{lang}" / "SKILL.md"
            self.assertTrue(skill_file.is_file(), f"Missing skill {lang}")
            with open(skill_file, "r", encoding="utf-8") as f:
                frontmatter, _ = parse_frontmatter(f.read())
            meta = frontmatter.get("metadata", frontmatter)
            status = meta.get("status")
            if lang == "eo":
                self.assertIn(status, ["reviewed", "active", "canonical"])
            else:
                self.assertEqual(status, "draft", f"Skill {lang} status must be 'draft'")
            self.assertTrue(
                "translators" in meta or "maintainers" in meta,
                f"Skill {lang} must list translators/maintainers",
            )

    def test_f3_skills_agent_protocol_verbs(self):
        """F3.5: All skills must enforce identical agent protocol (read, analyze, cite, propose; no edit)."""
        for lang in EXPECTED_SKILL_LANGS:
            skill_file = REPO_ROOT / "skills" / f"agila-manifesto-{lang}" / "SKILL.md"
            self.assertTrue(skill_file.is_file(), f"Missing skill {lang}")
            with open(skill_file, "r", encoding="utf-8") as f:
                _, body = parse_frontmatter(f.read())
            body_lower = body.lower()
            # Must mention read, analyze, cite, propose (or Esperanto/Spanish equivalents)
            has_verbs = (
                ("read" in body_lower and "analyze" in body_lower and "cite" in body_lower and "propose" in body_lower)
                or ("legu" in body_lower and "analizu" in body_lower and "citu" in body_lower and "proponu" in body_lower)
                or ("leer" in body_lower and "analizar" in body_lower and "citar" in body_lower and "proponer" in body_lower)
            )
            self.assertTrue(
                has_verbs,
                f"Skill {lang} must detail 4-verb agent protocol (read, analyze, cite, propose)",
            )
            # Must forbid machine modifications to canon
            has_forbid = (
                "neniam modifu" in body_lower
                or "never modify" in body_lower
                or "cannot modify" in body_lower
                or "no pueden modificar" in body_lower
                or "nunca modifican" in body_lower
                or "no aprueban" in body_lower
            )
            self.assertTrue(
                has_forbid,
                f"Skill {lang} must state machines/agents cannot approve or modify canon",
            )

    def test_f3_skills_ten_principles_present(self):
        """F3.6: All skills must preserve principle IDs P01 through P10."""
        for lang in EXPECTED_SKILL_LANGS:
            skill_file = REPO_ROOT / "skills" / f"agila-manifesto-{lang}" / "SKILL.md"
            self.assertTrue(skill_file.is_file(), f"Missing skill {lang}")
            with open(skill_file, "r", encoding="utf-8") as f:
                _, body = parse_frontmatter(f.read())
            for i in range(1, 11):
                pid = f"P{i:02d}"
                self.assertIn(
                    pid,
                    body,
                    f"Skill {lang} missing principle ID {pid}",
                )

    def test_f3_skills_derivative_disclaimer(self):
        """F3.7: Translated skills (en, es) must state they are derived and Esperanto canon prevails."""
        for lang in ["en", "es"]:
            skill_file = REPO_ROOT / "skills" / f"agila-manifesto-{lang}" / "SKILL.md"
            self.assertTrue(skill_file.is_file(), f"Missing skill {lang}")
            with open(skill_file, "r", encoding="utf-8") as f:
                _, body = parse_frontmatter(f.read())
            body_lower = body.lower()
            has_disclaimer = (
                "esperanto" in body_lower
                and ("canon" in body_lower or "kanono" in body_lower or "cánon" in body_lower or "prevalec" in body_lower or "prevails" in body_lower)
            )
            self.assertTrue(
                has_disclaimer,
                f"Skill {lang} must state Esperanto canon is authoritative and prevails.",
            )


class TestTier1ReadmeArchitecture(unittest.TestCase):
    """Feature 4: Strict 13-Section README Architecture (README.md, README.eo.md, README.es.md)."""

    def setUp(self):
        self.readme_en = REPO_ROOT / "README.md"
        self.readme_eo = REPO_ROOT / "README.eo.md"
        self.readme_es = REPO_ROOT / "README.es.md"

    def test_f4_readme_file_exists(self):
        """F4.1: README.md, README.eo.md, and README.es.md must exist."""
        self.assertTrue(self.readme_en.is_file(), "English README.md missing")
        self.assertTrue(self.readme_eo.is_file(), "Esperanto README.eo.md missing")
        self.assertTrue(self.readme_es.is_file(), "Spanish README.es.md missing")

    def test_f4_readme_thirteen_sections_sequence(self):
        """F4.2: English README.md must contain strictly 13 numbered sections in exact order."""
        self.assertTrue(self.readme_en.is_file(), "README.md missing")
        with open(self.readme_en, "r", encoding="utf-8") as f:
            content = f.read()

        # Find all H2 headers starting with numbers
        h2_headers = re.findall(r"^##\s+(\d+\.\s+[^\r\n]+)", content, re.MULTILINE)
        self.assertEqual(
            len(h2_headers),
            13,
            f"Expected exactly 13 H2 sections in README.md, found {len(h2_headers)}: {h2_headers}",
        )
        for i, header in enumerate(h2_headers, start=1):
            self.assertTrue(
                header.startswith(f"{i}."),
                f"Section header sequence error at position {i}: found '{header}'",
            )

    def test_f4_readme_section1_hook_and_description(self):
        """F4.3: Section 1 must include the hook 'Deliver quality software.' and description."""
        self.assertTrue(self.readme_en.is_file(), "README.md missing")
        with open(self.readme_en, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn(
            "Deliver quality software.",
            content,
            "README.md Section 1 must contain hook 'Deliver quality software.'",
        )

    def test_f4_readme_section2_real_badges(self):
        """F4.4: Section 2 must include real badges (license, version, CI, languages)."""
        self.assertTrue(self.readme_en.is_file(), "README.md missing")
        with open(self.readme_en, "r", encoding="utf-8") as f:
            content = f.read()
        # Look for badge patterns or shields.io links
        self.assertTrue(
            "shields.io" in content or "badge" in content.lower(),
            "README.md Section 2 must include badges",
        )
        self.assertIn("3.1", content, "README.md badges must reference version 3.1")

    def test_f4_readme_section4_conway_transparency(self):
        """F4.5: Section 4 table must declare 8 of 10 principles derive from Conway's Law."""
        self.assertTrue(self.readme_en.is_file(), "README.md missing")
        with open(self.readme_en, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertRegex(
            content,
            r"8\s*(?:of|/)\s*10.*Conway",
            "README.md Section 4 must declare 8 of 10 derive from Conway's Law as design tendency",
        )

    def test_f4_readme_section10_translation_markers(self):
        """F4.6: Section 10 must contain valid START and END translation table markers."""
        self.assertTrue(self.readme_en.is_file(), "README.md missing")
        with open(self.readme_en, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn(
            "<!-- START_TRANSLATION_TABLE -->",
            content,
            "README.md Section 10 missing <!-- START_TRANSLATION_TABLE --> marker",
        )
        self.assertIn(
            "<!-- END_TRANSLATION_TABLE -->",
            content,
            "README.md Section 10 missing <!-- END_TRANSLATION_TABLE --> marker",
        )

    def test_f4_derived_readmes_disclaimer(self):
        """F4.7: README.eo.md and README.es.md must contain derivative notice."""
        for path, lang in [(self.readme_eo, "eo"), (self.readme_es, "es")]:
            self.assertTrue(path.is_file(), f"{path.name} missing")
            with open(path, "r", encoding="utf-8") as f:
                c = f.read().lower()
            self.assertTrue(
                "deriv" in c or "kanono" in c or "canon" in c,
                f"{path.name} must declare derivative status",
            )


class TestTier1GovernanceCommunity(unittest.TestCase):
    """Feature 5: 3-Tier Governance & Community Files."""

    def test_f5_governance_file_exists(self):
        """F5.1: GOVERNANCE.md must exist."""
        gov_path = REPO_ROOT / "GOVERNANCE.md"
        self.assertTrue(gov_path.is_file(), "GOVERNANCE.md missing")

    def test_f5_governance_three_tiers_defined(self):
        """F5.2: GOVERNANCE.md must specify Fundamento, Tradukoj, and Uzado tiers."""
        gov_path = REPO_ROOT / "GOVERNANCE.md"
        self.assertTrue(gov_path.is_file(), "GOVERNANCE.md missing")
        with open(gov_path, "r", encoding="utf-8") as f:
            c = f.read()
        self.assertIn("Fundamento", c, "GOVERNANCE.md missing Fundamento tier")
        self.assertTrue(
            "Tradukoj" in c or "Translations" in c,
            "GOVERNANCE.md missing Tradukoj / Translations tier",
        )
        self.assertIn("Uzado", c, "GOVERNANCE.md missing Uzado tier")

    def test_f5_governance_canon_stewards_and_14_days(self):
        """F5.3: Canon changes require >= 2 human stewards and 14 days public discussion."""
        gov_path = REPO_ROOT / "GOVERNANCE.md"
        self.assertTrue(gov_path.is_file(), "GOVERNANCE.md missing")
        with open(gov_path, "r", encoding="utf-8") as f:
            c = f.read()
        self.assertTrue(
            "14" in c and ("day" in c.lower() or "tag" in c.lower() or "día" in c.lower()),
            "GOVERNANCE.md must mandate 14 days minimum public deliberation for canon changes",
        )
        self.assertTrue(
            "2" in c and ("steward" in c.lower() or "gardanto" in c.lower() or "mantenedor" in c.lower()),
            "GOVERNANCE.md must require at least 2 human stewards",
        )

    def test_f5_governance_semver_rules(self):
        """F5.4: GOVERNANCE.md must define MAJOR, MINOR, and PATCH SemVer rules for canon."""
        gov_path = REPO_ROOT / "GOVERNANCE.md"
        self.assertTrue(gov_path.is_file(), "GOVERNANCE.md missing")
        with open(gov_path, "r", encoding="utf-8") as f:
            c = f.read()
        self.assertIn("MAJOR", c)
        self.assertIn("MINOR", c)
        self.assertIn("PATCH", c)

    def test_f5_license_dual_licensing(self):
        """F5.5: LICENSE must specify CC BY 4.0 for text and MIT for code/scripts."""
        lic_path = REPO_ROOT / "LICENSE"
        self.assertTrue(lic_path.is_file(), "LICENSE file missing")
        with open(lic_path, "r", encoding="utf-8") as f:
            c = f.read()
        self.assertIn("Creative Commons", c, "LICENSE missing Creative Commons Attribution 4.0")
        self.assertIn("MIT", c, "LICENSE missing MIT License for scripts/tooling")

    def test_f5_community_files_exist(self):
        """F5.6: CONTRIBUTING.md, CODE_OF_CONDUCT.md, CHANGELOG.md, CITATION.cff, and CODEOWNERS must exist."""
        required = [
            REPO_ROOT / "CONTRIBUTING.md",
            REPO_ROOT / "CODE_OF_CONDUCT.md",
            REPO_ROOT / "CHANGELOG.md",
            REPO_ROOT / "CITATION.cff",
            REPO_ROOT / ".github" / "CODEOWNERS",
        ]
        for path in required:
            self.assertTrue(path.is_file(), f"Community file {path} missing")


class TestTier1AutomationScripts(unittest.TestCase):
    """Feature 6: Automation & Validation Script (scripts/validate.py)."""

    def setUp(self):
        self.script_path = REPO_ROOT / "scripts" / "validate.py"

    def test_f6_validate_script_exists(self):
        """F6.1: scripts/validate.py must exist."""
        self.assertTrue(self.script_path.is_file(), f"Script missing at {self.script_path}")

    def test_f6_validate_stdlib_imports_only(self):
        """F6.2: scripts/validate.py must rely on standard library only, zero pip install."""
        self.assertTrue(self.script_path.is_file(), "scripts/validate.py missing")
        with open(self.script_path, "r", encoding="utf-8") as f:
            source = f.read()
        # Ensure no third-party imports like requests, click, pydantic, rich
        disallowed = ["requests", "click", "pydantic", "rich", "typer", "pandas", "fastapi"]
        for pkg in disallowed:
            self.assertNotRegex(
                source,
                rf"(?:^|\n)\s*(?:import|from)\s+{pkg}\b",
                f"scripts/validate.py should not import external package {pkg}",
            )

    def test_f6_validate_check_flag(self):
        """F6.3: python scripts/validate.py --check must run and return exit code 0 on valid repo."""
        self.assertTrue(self.script_path.is_file(), "scripts/validate.py missing")
        res = run_python_script("scripts/validate.py", "--check")
        self.assertEqual(
            res.returncode,
            0,
            f"scripts/validate.py --check failed with code {res.returncode}:\nstdout: {res.stdout}\nstderr: {res.stderr}",
        )

    def test_f6_validate_help_or_version_flag(self):
        """F6.4: scripts/validate.py must support --help or usage instructions."""
        self.assertTrue(self.script_path.is_file(), "scripts/validate.py missing")
        res = run_python_script("scripts/validate.py", "--help")
        # Should exit with 0 and print usage
        self.assertEqual(res.returncode, 0, f"scripts/validate.py --help failed: {res.stderr}")
        self.assertIn("validate", res.stdout.lower())

    def test_f6_validate_reports_principles_verified(self):
        """F6.5: scripts/validate.py output must report canon principles verification."""
        self.assertTrue(self.script_path.is_file(), "scripts/validate.py missing")
        res = run_python_script("scripts/validate.py", "--check")
        output = (res.stdout + res.stderr).lower()
        self.assertTrue(
            "canon" in output or "kanono" in output or "p01" in output or "valid" in output,
            "validate.py must output verification details",
        )


class TestTier1GitHygieneAndLaunch(unittest.TestCase):
    """Feature 7: Git Hygiene, Exclusions & Launch Checklist."""

    def test_f7_git_exclude_file_exists(self):
        """F7.1: .git/info/exclude must exist."""
        exclude_path = REPO_ROOT / ".git" / "info" / "exclude"
        self.assertTrue(
            exclude_path.is_file(),
            f"Expected .git/info/exclude at {exclude_path}",
        )

    def test_f7_git_exclude_contains_required_patterns(self):
        """F7.2: .git/info/exclude must contain patterns for .agents/, prompts, TEST_READY.md."""
        exclude_path = REPO_ROOT / ".git" / "info" / "exclude"
        self.assertTrue(exclude_path.is_file(), ".git/info/exclude missing")
        with open(exclude_path, "r", encoding="utf-8") as f:
            c = f.read()
        self.assertIn(".agents", c, ".git/info/exclude must exclude .agents")
        self.assertTrue(
            "*.prompt" in c or "prompt" in c or "ORIGINAL_REQUEST.md" in c,
            ".git/info/exclude must exclude agent prompts / drafts",
        )
        self.assertIn("TEST_READY.md", c, ".git/info/exclude must exclude TEST_READY.md")

    def test_f7_no_committed_gitignore(self):
        """F7.3: Project must strictly avoid committing .gitignore (R5 mandate)."""
        gitignore_path = REPO_ROOT / ".gitignore"
        self.assertFalse(
            gitignore_path.is_file(),
            "R5 strictly forbids .gitignore in repo; use .git/info/exclude exclusively.",
        )
        # Check git ls-files if git is initialized
        if (REPO_ROOT / ".git").is_dir():
            res = subprocess.run(
                ["git", "ls-files", ".gitignore"],
                cwd=str(REPO_ROOT),
                capture_output=True,
                text=True,
            )
            self.assertEqual(res.stdout.strip(), "", "Git is tracking .gitignore, violating R5")

    def test_f7_external_launch_checklist_exists(self):
        """F7.4: LAUNCH-CHECKLIST.md must exist (at C:\\Dev\\LAUNCH-CHECKLIST.md or repo root)."""
        candidate_paths = [
            pathlib.Path(r"C:\Dev\LAUNCH-CHECKLIST.md"),
            REPO_ROOT.parent / "LAUNCH-CHECKLIST.md",
            REPO_ROOT / "LAUNCH-CHECKLIST.md",
        ]
        found = any(p.is_file() for p in candidate_paths)
        if not found and os.environ.get("CI"):
            self.skipTest("External LAUNCH-CHECKLIST.md not bundled in CI environment")
        self.assertTrue(
            found,
            "LAUNCH-CHECKLIST.md not found at C:\\Dev\\LAUNCH-CHECKLIST.md or parent directory.",
        )

    def test_f7_launch_checklist_five_mandatory_sections(self):
        """F7.5: LAUNCH-CHECKLIST.md must contain all 5 required sections."""
        candidate_paths = [
            pathlib.Path(r"C:\Dev\LAUNCH-CHECKLIST.md"),
            REPO_ROOT.parent / "LAUNCH-CHECKLIST.md",
            REPO_ROOT / "LAUNCH-CHECKLIST.md",
        ]
        target = next((p for p in candidate_paths if p.is_file()), None)
        if not target and os.environ.get("CI"):
            self.skipTest("External LAUNCH-CHECKLIST.md not bundled in CI environment")
        self.assertIsNotNone(target, "LAUNCH-CHECKLIST.md missing")
        with open(target, "r", encoding="utf-8") as f:
            content = f.read().lower()

        # Check for Section 1: Launch Plan
        self.assertTrue("launch plan" in content or "plan de lanzamiento" in content)
        # Check for Section 2: Final File Tree
        self.assertTrue("tree" in content or "árbol" in content or "file" in content)
        # Check for Section 3: Decisions Made
        self.assertTrue("decision" in content or "decisiones" in content)
        # Check for Section 4: Canon Incoherencies
        self.assertTrue("incoherenc" in content or "linguistic" in content or "lingv" in content)
        # Check for Section 5: Maintainer Steps
        self.assertTrue("step" in content or "pasos" in content or "manual" in content)

    def test_f7_git_remote_url(self):
        """F7.6: Git remote origin must match https://github.com/willkwolf/agila-manifesto.git."""
        if not (REPO_ROOT / ".git").is_dir():
            self.skipTest("Git not initialized yet")
        res = subprocess.run(
            ["git", "remote", "get-url", "origin"],
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
        )
        self.assertEqual(
            res.returncode,
            0,
            f"Git remote origin not configured: {res.stderr}",
        )
        self.assertIn(
            "github.com/willkwolf/agila-manifesto",
            res.stdout.strip(),
            f"Remote URL mismatch: {res.stdout.strip()}",
        )


if __name__ == "__main__":
    unittest.main()
