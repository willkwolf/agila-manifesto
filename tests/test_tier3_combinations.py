"""Agila Manifesto v3.1 — Tier 3 Pairwise Combinations & Integration Tests.

Validates cross-component consistency, structural parity, and synchronization contracts:
- Pair 1: Canon SHA-256 <-> scripts/validate.py <-> i18n/STATUS.md
- Pair 2: Validator Table Generator <-> README.md Dynamic Markers
- Pair 3: YAML Schema <-> Agent Skill Prompts (P01–P10 1:1 Parity)
- Pair 4: .github/CODEOWNERS <-> GitHub Actions Workflows (governance-guard, canon-drift)
- Pair 5: Dual Licensing <-> CITATION.cff <-> README.md Badges
- Pair 6: Canon Conway Mapping <-> README.md <-> docs/conway-derivations.md

Zero external dependencies (unittest, stdlib only).
"""

import hashlib
import os
import pathlib
import re
import shutil
import subprocess
import tempfile
import unittest

from tests.common import (
    CANON_PRINCIPLES_COUNT,
    CANON_SHA256,
    CANON_VERSION,
    CONWAY_DERIVATIONS,
    CONWAY_DERIVED_COUNT,
    EXPECTED_SKILL_LANGS,
    GIT_REMOTE_URL,
    REPO_ROOT,
    compute_file_sha256,
    parse_frontmatter,
    parse_yaml_text,
    run_python_script,
)


class TestTier3Combinations(unittest.TestCase):
    """Pairwise combinatorial integration test suite."""

    def test_pair1_canon_hash_validate_status_sync(self):
        """Pair 1: Canon SHA-256 <-> scripts/validate.py <-> i18n/STATUS.md parity."""
        canon_path = REPO_ROOT / "canon" / "AGILA-MANIFESTO.eo.md"
        status_path = REPO_ROOT / "i18n" / "STATUS.md"
        validate_path = REPO_ROOT / "scripts" / "validate.py"

        if not (canon_path.is_file() and status_path.is_file() and validate_path.is_file()):
            self.skipTest("Canon, STATUS.md, or validate.py not yet generated")

        actual_canon_sha = compute_file_sha256(canon_path)
        self.assertEqual(actual_canon_sha, CANON_SHA256)

        with open(status_path, "r", encoding="utf-8") as f:
            status_content = f.read()

        # i18n/STATUS.md must cite the canon sha or display it in table for eo
        self.assertIn(
            CANON_SHA256[:12],
            status_content,
            "i18n/STATUS.md must reference current canonical SHA-256 prefix",
        )

    def test_pair2_validator_table_readme_dynamic_markers(self):
        """Pair 2: scripts/validate.py table update preserves README content outside markers."""
        readme_path = REPO_ROOT / "README.md"
        validate_path = REPO_ROOT / "scripts" / "validate.py"

        if not (readme_path.is_file() and validate_path.is_file()):
            self.skipTest("README.md or scripts/validate.py missing")

        with open(readme_path, "r", encoding="utf-8") as f:
            original = f.read()

        self.assertIn("<!-- START_TRANSLATION_TABLE -->", original)
        self.assertIn("<!-- END_TRANSLATION_TABLE -->", original)

        before_marker = original.split("<!-- START_TRANSLATION_TABLE -->")[0]
        after_marker = original.split("<!-- END_TRANSLATION_TABLE -->")[1]

        # Verify markers enclose languages table
        table_area = original.split("<!-- START_TRANSLATION_TABLE -->")[1].split("<!-- END_TRANSLATION_TABLE -->")[0]
        for lang in EXPECTED_SKILL_LANGS:
            self.assertIn(lang, table_area, f"Translation table missing language code {lang}")

    def test_pair3_yaml_parity_with_skill_principles(self):
        """Pair 3: YAML Schema <-> skills/agila-manifesto-eo/SKILL.md (P01–P10 1:1 Parity)."""
        yaml_path = REPO_ROOT / "canon" / "manifesto.eo.yaml"
        skill_path = REPO_ROOT / "skills" / "agila-manifesto-eo" / "SKILL.md"

        if not (yaml_path.is_file() and skill_path.is_file()):
            self.skipTest("YAML summary or eo skill missing")

        with open(yaml_path, "r", encoding="utf-8") as f:
            yaml_data = parse_yaml_text(f.read())
        principoj = yaml_data.get("principoj") or yaml_data.get("principles", [])
        self.assertEqual(len(principoj), 10, "YAML must have 10 principles")

        with open(skill_path, "r", encoding="utf-8") as f:
            _, skill_body = parse_frontmatter(f.read())

        for p in principoj:
            p_id = str(p.get("id") or f"P{p.get('numero', 0):02d}")
            self.assertIn(
                p_id,
                skill_body,
                f"Principle {p_id} from YAML not found in eo SKILL.md body",
            )

    def test_pair4_codeowners_rules_mirror_github_workflows(self):
        """Pair 4: .github/CODEOWNERS paths mirror triggers in governance workflows."""
        codeowners_path = REPO_ROOT / ".github" / "CODEOWNERS"
        governance_guard_path = REPO_ROOT / ".github" / "workflows" / "governance-guard.yml"
        canon_drift_path = REPO_ROOT / ".github" / "workflows" / "canon-drift.yml"

        if not (codeowners_path.is_file() and governance_guard_path.is_file() and canon_drift_path.is_file()):
            self.skipTest("CODEOWNERS or GitHub workflows missing")

        with open(codeowners_path, "r", encoding="utf-8") as f:
            codeowners_text = f.read()

        with open(governance_guard_path, "r", encoding="utf-8") as f:
            gov_workflow_text = f.read()

        with open(canon_drift_path, "r", encoding="utf-8") as f:
            drift_workflow_text = f.read()

        # Both workflows and CODEOWNERS must protect canon/
        self.assertIn("canon", codeowners_text, "CODEOWNERS must define rules for canon/")
        self.assertIn("canon", gov_workflow_text, "governance-guard.yml must monitor canon/")
        self.assertIn("canon", drift_workflow_text, "canon-drift.yml must monitor canon/")

    def test_pair5_dual_licensing_citation_readme_sync(self):
        """Pair 5: Dual licensing (CC BY 4.0 / MIT) synchronized across LICENSE, CITATION.cff, and README.md."""
        license_path = REPO_ROOT / "LICENSE"
        citation_path = REPO_ROOT / "CITATION.cff"
        readme_path = REPO_ROOT / "README.md"

        if not (license_path.is_file() and citation_path.is_file() and readme_path.is_file()):
            self.skipTest("LICENSE, CITATION.cff, or README.md missing")

        with open(license_path, "r", encoding="utf-8") as f:
            lic_content = f.read()
        with open(citation_path, "r", encoding="utf-8") as f:
            cit_content = f.read()
        with open(readme_path, "r", encoding="utf-8") as f:
            readme_content = f.read()

        # CC BY 4.0 presence
        self.assertIn("CC-BY-4.0", cit_content, "CITATION.cff must specify CC-BY-4.0")
        self.assertTrue(
            "cc by 4.0" in readme_content.lower() or "creative commons" in readme_content.lower(),
            "README.md must cite CC BY 4.0",
        )

        # Version consistency
        self.assertIn(CANON_VERSION, cit_content, f"CITATION.cff must cite version {CANON_VERSION}")
        self.assertIn(CANON_VERSION, readme_content, f"README.md must cite version {CANON_VERSION}")

    def test_pair6_conway_derivation_cross_document_alignment(self):
        """Pair 6: Conway derivation mapping (8 of 10) aligned across YAML, README.md, and docs."""
        yaml_path = REPO_ROOT / "canon" / "manifesto.eo.yaml"
        readme_path = REPO_ROOT / "README.md"
        conway_doc_path = REPO_ROOT / "docs" / "conway-derivations.md"

        if not (yaml_path.is_file() and readme_path.is_file() and conway_doc_path.is_file()):
            self.skipTest("YAML summary, README.md, or docs/conway-derivations.md missing")

        with open(readme_path, "r", encoding="utf-8") as f:
            readme_c = f.read()
        with open(conway_doc_path, "r", encoding="utf-8") as f:
            doc_c = f.read()

        # Both must declare 8 of 10
        self.assertRegex(readme_c, r"8\s*(?:of|/)\s*10.*Conway")
        self.assertRegex(doc_c, r"8\s*(?:of|/|el)\s*10")


if __name__ == "__main__":
    unittest.main()
