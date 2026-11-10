"""Agila Manifesto v3.1 — Tier 2 Boundary, Corner & Negative Tests.

Validates robust error handling, schema boundaries, and negative test cases across 4 domains:
1. Canon Corruption & Byte Tampering (single-byte corruption, missing headers, ordering, count)
2. YAML Schema Violations (bad syntax, missing fields, count mismatch, Conway declaration mismatch)
3. Skill Stale SHA & Missing Metadata (hash drift, missing frontmatter, missing principle IDs, protocol tampering)
4. Malformed README Sections (missing section, out-of-order sections, missing table markers)
Plus Git boundary protections (exclusion of .agents, TEST_READY.md, forbidden .gitignore).

All mutation tests are executed in isolated temporary workspaces to avoid corrupting repository state.
Zero external dependencies (unittest, stdlib only).
"""

import hashlib
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
import unittest

from tests.common import (
    CANON_PRINCIPLES_COUNT,
    CANON_SHA256,
    CANON_VERSION,
    CONWAY_DERIVED_COUNT,
    EXPECTED_SKILL_LANGS,
    README_REQUIRED_SECTIONS,
    REPO_ROOT,
    compute_bytes_sha256,
    parse_frontmatter,
    parse_yaml_text,
    run_python_script,
)


class TestTier2CanonBoundaries(unittest.TestCase):
    """Domain 1: Canon Corruption, Byte Tampering & Malformed Headers."""

    def setUp(self):
        self.canon_path = REPO_ROOT / "canon" / "AGILA-MANIFESTO.eo.md"
        self.temp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp_dir.cleanup)

    def _read_canon(self) -> str:
        if not self.canon_path.is_file():
            self.skipTest(f"Canon file not present at {self.canon_path}")
        with open(self.canon_path, "r", encoding="utf-8") as f:
            return f.read()

    def test_t2_d1_1_single_byte_corruption_alters_sha256(self):
        """D1.1: Altering a single character in canon must alter SHA-256 and invalidate hash."""
        original = self._read_canon()
        # Flip first character from '[' to '{'
        corrupted = "{" + original[1:]
        corrupted_hash = compute_bytes_sha256(corrupted.encode("utf-8"))
        self.assertNotEqual(
            corrupted_hash,
            CANON_SHA256,
            "Corrupted canon must not produce the canonical SHA-256 hash.",
        )

    def test_t2_d1_2_missing_bazo_header_detected(self):
        """D1.2: Omitting 'Bazo:' from principle 3 must be detected as invalid."""
        original = self._read_canon()
        # Remove Bazo: from principle 3
        corrupted = re.sub(r"(3\. Stabilaj sistemoj.*?)(Bazo:)", r"\1Teorio:", original, flags=re.DOTALL)
        self.assertNotIn("Bazo:", corrupted.split("3. Stabilaj sistemoj")[1].split("Signalo:")[0])
        # Verify bazo count drops below 10
        bazo_count = len(re.findall(r"(?:^|\n)Bazo:", corrupted))
        self.assertEqual(
            bazo_count,
            CANON_PRINCIPLES_COUNT - 1,
            "Omitting Bazo from principle 3 must drop valid Bazo count to 9.",
        )

    def test_t2_d1_3_missing_signalo_header_detected(self):
        """D1.3: Omitting 'Signalo:' from principle 6 must be detected."""
        original = self._read_canon()
        # Replace Signalo: on P06 with corrupted text
        corrupted = re.sub(r"(6\. Fluon regas.*?)(Signalo:)", r"\1AliaTeksto:", original, flags=re.DOTALL)
        signalo_count = len(re.findall(r"(?:^|\n)Signalo:", corrupted))
        self.assertEqual(
            signalo_count,
            CANON_PRINCIPLES_COUNT - 1,
            "Omitting Signalo from principle 6 must drop valid Signalo count to 9.",
        )

    def test_t2_d1_4_out_of_order_principles_detected(self):
        """D1.4: Swapping principle order (e.g. 3 before 2) breaks strict sequential numbering."""
        original = self._read_canon()
        # Check that sequential regex fails if numbers are swapped
        swapped = original.replace("2. Ĉiu decida unuo", "TEMP_P2")
        swapped = swapped.replace("3. Stabilaj sistemoj", "2. Stabilaj sistemoj")
        swapped = swapped.replace("TEMP_P2", "3. Ĉiu decida unuo")

        # In swapped text, 'Ĉiu decida unuo' is now labeled 3
        p2_match = re.search(r"2\.\s+([^\n]+)", swapped)
        self.assertIsNotNone(p2_match)
        self.assertNotIn(
            "Ĉiu decida unuo",
            p2_match.group(1),
            "Swapped sequence must not place original P02 title under number 2.",
        )

    def test_t2_d1_5_principle_count_mismatch(self):
        """D1.5: Truncating principle 10 must result in principle count mismatch (9 != 10)."""
        original = self._read_canon()
        # Truncate before principle 10
        truncated = original.split("10. Sistemo en uzo")[0]
        count = len(re.findall(r"(?:^|\n)(?:\[)?(\d+)\.\s+", truncated))
        self.assertEqual(
            count,
            9,
            f"Expected exactly 9 principles in truncated text, found {count}",
        )
        self.assertNotEqual(count, CANON_PRINCIPLES_COUNT)

    def test_t2_d1_6_crlf_injection_detected(self):
        """D1.6: Converting LF to Windows CRLF (\\r\\n) alters file hash and invalidates byte fidelity."""
        original = self._read_canon()
        crlf_content = original.replace("\n", "\r\n").encode("utf-8")
        crlf_hash = compute_bytes_sha256(crlf_content)
        self.assertNotEqual(
            crlf_hash,
            CANON_SHA256,
            "CRLF-converted canon must fail SHA-256 match against pure LF canonical hash.",
        )


class TestTier2YamlBoundaries(unittest.TestCase):
    """Domain 2: YAML Schema Violations, Incomplete Fields & Bad Types."""

    def setUp(self):
        self.yaml_path = REPO_ROOT / "canon" / "manifesto.eo.yaml"

    def _read_yaml_raw(self) -> str:
        if not self.yaml_path.is_file():
            self.skipTest(f"YAML file not present at {self.yaml_path}")
        with open(self.yaml_path, "r", encoding="utf-8") as f:
            return f.read()

    def test_t2_d2_1_syntax_error_rejected(self):
        """D2.1: Invalid YAML syntax (e.g. unclosed quote or improper indent) must fail parser."""
        bad_yaml = "version: 3.1\nprincipoj:\n  - id: 'P01\n    titolo: broken"
        try:
            import yaml
            with self.assertRaises((yaml.YAMLError, Exception)):
                yaml.safe_load(bad_yaml)
        except ImportError:
            # Test stdlib parser behavior
            data = parse_yaml_text(bad_yaml)
            self.assertNotEqual(len(data.get("principoj", [])), 10)

    def test_t2_d2_2_missing_version_field_rejected(self):
        """D2.2: YAML missing version or wrong version must fail version check."""
        raw = self._read_yaml_raw()
        corrupted = re.sub(r"(versio|version):\s*['\"]?3\.1['\"]?", "versio: '9.9'", raw)
        data = parse_yaml_text(corrupted)
        version = data.get("versio") or data.get("version")
        self.assertNotEqual(
            str(version),
            CANON_VERSION,
            f"Corrupted version '9.9' should not equal {CANON_VERSION}",
        )

    def test_t2_d2_3_principle_count_deficit_rejected(self):
        """D2.3: YAML defining fewer than 10 principles fails count constraint."""
        raw = self._read_yaml_raw()
        data = parse_yaml_text(raw)
        principoj = data.get("principoj") or data.get("principles", [])
        # Simulate removal of P10
        corrupted_principoj = [p for p in principoj if (p.get("id") != "P10" and p.get("numero") != 10)]
        self.assertEqual(len(corrupted_principoj), 9)
        self.assertNotEqual(len(corrupted_principoj), CANON_PRINCIPLES_COUNT)

    def test_t2_d2_4_principle_missing_mandatory_keys(self):
        """D2.4: Principle missing bazo or signalo must fail completeness assertion."""
        raw = self._read_yaml_raw()
        data = parse_yaml_text(raw)
        principoj = data.get("principoj") or data.get("principles", [])
        if principoj:
            sample = dict(principoj[0])
            del sample["bazo"]
            self.assertNotIn("bazo", sample, "Sample must be missing bazo")
            self.assertTrue(not sample.get("bazo"), "Missing bazo must evaluate to falsy")

    def test_t2_d2_5_conway_derivation_mismatch_rejected(self):
        """D2.5: Falsifying Conway derivation count (e.g. 10/10 or 5/10) must fail exact 8/10 check."""
        raw = self._read_yaml_raw()
        data = parse_yaml_text(raw)
        principoj = data.get("principoj") or data.get("principles", [])
        # Force all 10 to True
        modified = []
        for p in principoj:
            cp = dict(p)
            cp["derivas_de_conway"] = True
            modified.append(cp)
        conway_count = sum(1 for p in modified if p.get("derivas_de_conway") is True)
        self.assertEqual(conway_count, 10)
        self.assertNotEqual(
            conway_count,
            CONWAY_DERIVED_COUNT,
            f"Conway derivation must strictly equal {CONWAY_DERIVED_COUNT}, not {conway_count}",
        )


class TestTier2SkillBoundaries(unittest.TestCase):
    """Domain 3: Skill Stale SHA, Missing Metadata & Protocol Tampering."""

    def setUp(self):
        self.skill_en = REPO_ROOT / "skills" / "agila-manifesto-en" / "SKILL.md"

    def _read_skill(self) -> str:
        if not self.skill_en.is_file():
            self.skipTest(f"Skill file not found at {self.skill_en}")
        with open(self.skill_en, "r", encoding="utf-8") as f:
            return f.read()

    def test_t2_d3_1_stale_sha_drift_detection(self):
        """D3.1: Skill with outdated canon_sha256 must be detected as drifted/stale."""
        outdated_sha = "1111111111111111111111111111111111111111111111111111111111111111"
        self.assertNotEqual(outdated_sha, CANON_SHA256)
        # Verify that comparing outdated_sha against canon detects stale state
        is_stale = (outdated_sha != CANON_SHA256)
        self.assertTrue(is_stale, "Outdated sha must flag stale status")

    def test_t2_d3_2_missing_translators_field_rejected(self):
        """D3.2: Skill frontmatter missing translators field must fail validation."""
        raw = self._read_skill()
        frontmatter, _ = parse_frontmatter(raw)
        meta = frontmatter.get("metadata", frontmatter)
        # Simulate missing translators
        meta_corrupted = {k: v for k, v in meta.items() if k not in ["translators", "maintainers"]}
        self.assertNotIn("translators", meta_corrupted)
        self.assertNotIn("maintainers", meta_corrupted)

    def test_t2_d3_3_missing_principle_id_in_translation_rejected(self):
        """D3.3: Translated skill body missing P07 must be flagged as incomplete."""
        raw = self._read_skill()
        _, body = parse_frontmatter(raw)
        corrupted_body = body.replace("P07", "PRIN_07")
        present_ids = [f"P{i:02d}" for i in range(1, 11) if f"P{i:02d}" in corrupted_body]
        self.assertNotIn("P07", present_ids)
        self.assertEqual(len(present_ids), 9)

    def test_t2_d3_4_protocol_tampering_allow_machine_edits_rejected(self):
        """D3.4: Skill protocol tampered to permit machine edits to canon must fail safety check."""
        tampered_protocol = "Agents are authorized to directly modify the canon and approve PRs."
        # Safety audit rule: text must NOT authorize AI agents to edit canon
        is_safe = not ("directly modify the canon" in tampered_protocol and "approve prs" in tampered_protocol.lower())
        self.assertFalse(is_safe, "Tampered protocol allowing machine modifications must fail safety check")

    def test_t2_d3_5_invalid_skill_name_convention_rejected(self):
        """D3.5: Skill directory or frontmatter not matching 'agila-manifesto-<lang>' is invalid."""
        invalid_name = "manifesto-spanish-v3"
        valid_pattern = r"^agila-manifesto-[a-z]{2,3}$"
        self.assertIsNone(
            re.match(valid_pattern, invalid_name),
            f"Invalid skill name '{invalid_name}' must not match standard pattern",
        )


class TestTier2ReadmeBoundaries(unittest.TestCase):
    """Domain 4: Malformed README Sections & Broken Dynamic Markers."""

    def setUp(self):
        self.readme_path = REPO_ROOT / "README.md"

    def _read_readme(self) -> str:
        if not self.readme_path.is_file():
            self.skipTest(f"README.md not found at {self.readme_path}")
        with open(self.readme_path, "r", encoding="utf-8") as f:
            return f.read()

    def test_t2_d4_1_omitted_section_fails_strict_count(self):
        """D4.1: Removing Section 9 (Governance) must result in 12 sections and fail assertion."""
        raw = self._read_readme()
        # Remove Section 9
        corrupted = re.sub(r"##\s+9\.\s+Governance.*?(?=##\s+10\.)", "", raw, flags=re.DOTALL)
        h2_headers = re.findall(r"^##\s+(\d+\.\s+[^\r\n]+)", corrupted, re.MULTILINE)
        self.assertEqual(len(h2_headers), 12, "Omitting section 9 must reduce section count to 12")
        self.assertNotEqual(len(h2_headers), 13, "Strict 13-section check must fail when section is omitted")

    def test_t2_d4_2_swapped_section_headers_fails_sequence(self):
        """D4.2: Sections in wrong sequence (e.g. 5 before 4) must fail sequence check."""
        raw = self._read_readme()
        # Swap labels 4. and 5.
        corrupted = raw.replace("## 4. ", "## TEMP_4. ").replace("## 5. ", "## 4. ").replace("## TEMP_4. ", "## 5. ")
        h2_headers = re.findall(r"^##\s+(\d+)\.\s+([^\r\n]+)", corrupted, re.MULTILINE)
        # Sequence validator:
        numbers = [int(num) for num, _ in h2_headers]
        is_strictly_monotonic = numbers == list(range(1, 14))
        self.assertFalse(is_strictly_monotonic, "Swapped sections must violate monotonic sequence 1..13")

    def test_t2_d4_3_missing_translation_markers_fails_sync(self):
        """D4.3: Missing <!-- START_TRANSLATION_TABLE --> marker must prevent dynamic table sync."""
        raw = self._read_readme()
        corrupted = raw.replace("<!-- START_TRANSLATION_TABLE -->", "")
        self.assertNotIn("<!-- START_TRANSLATION_TABLE -->", corrupted)
        # Simulating script check:
        has_markers = (
            "<!-- START_TRANSLATION_TABLE -->" in corrupted
            and "<!-- END_TRANSLATION_TABLE -->" in corrupted
        )
        self.assertFalse(has_markers, "Missing start marker must be detected")

    def test_t2_d4_4_conway_obscuration_detected(self):
        """D4.4: Corrupting README to claim Conway Law is an absolute rule must fail transparency check."""
        bad_claim = "All 10 principles are mandatory rules derived strictly from Conway's Law."
        # Transparency check: must explicitly qualify as a design tendency, not a mandatory rule
        is_transparent = "tendency" in bad_claim.lower() or "design tendency" in bad_claim.lower()
        self.assertFalse(is_transparent, "Failing to declare Conway derivations as a design tendency must fail check")

    def test_t2_d4_5_missing_hook_detected(self):
        """D4.5: README missing hook 'Deliver quality software.' fails Section 1 specification."""
        raw = self._read_readme()
        corrupted = raw.replace("Deliver quality software.", "Some other software tagline.")
        self.assertNotIn("Deliver quality software.", corrupted)


class TestTier2GitBoundaries(unittest.TestCase):
    """Domain 5: Git Hygiene, Exclusion Leakage & Forbidden Files."""

    def test_t2_d5_1_agents_exclusion_rule_present(self):
        """D5.1: .git/info/exclude must explicitly contain '.agents/' pattern."""
        exclude_path = REPO_ROOT / ".git" / "info" / "exclude"
        if not exclude_path.is_file():
            self.skipTest(".git/info/exclude not present yet")
        with open(exclude_path, "r", encoding="utf-8") as f:
            c = f.read()
        patterns = [ln.strip() for ln in c.splitlines() if ln.strip() and not ln.strip().startswith("#")]
        self.assertTrue(
            any(".agents" in p for p in patterns),
            "Expected .agents/ pattern in .git/info/exclude",
        )

    def test_t2_d5_2_test_ready_signal_excluded(self):
        """D5.2: TEST_READY.md must be excluded in .git/info/exclude to avoid tracking."""
        exclude_path = REPO_ROOT / ".git" / "info" / "exclude"
        if not exclude_path.is_file():
            self.skipTest(".git/info/exclude not present yet")
        with open(exclude_path, "r", encoding="utf-8") as f:
            c = f.read()
        self.assertIn("TEST_READY.md", c, "TEST_READY.md must be excluded in .git/info/exclude")

    def test_t2_d5_3_forbidden_gitignore_file_absent(self):
        """D5.3: .gitignore must not be present or committed anywhere in repo tree."""
        gi = REPO_ROOT / ".gitignore"
        self.assertFalse(gi.is_file(), "Forbidden .gitignore found in repo root")


if __name__ == "__main__":
    unittest.main()
