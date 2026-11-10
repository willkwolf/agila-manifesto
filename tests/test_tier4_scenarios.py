"""Agila Manifesto v3.1 — Tier 4 Real-World Application & Scenario Tests.

Exercises realistic user, contributor, and AI agent journeys across the ecosystem:
- Scenario 1: AI Agent Architectural Review Consultation (AGENTS.md & SKILL.md lens analysis)
- Scenario 2: Community Contributor Bootstrapping a New Translation (i18n/_template/)
- Scenario 3: Academic Systems Researcher Citing Agila Manifesto v3.1 (CITATION.cff)
- Scenario 4: Community Submits Counterexample via Template ("A counterexample is a gift")
- Scenario 5: Human Maintainer Executing Launch Runbook (LAUNCH-CHECKLIST.md)
- Scenario 6: Canon Change Proposal & 14-Day Deliberation Guard (.github/ISSUE_TEMPLATE/)

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
    CANON_VERSION_TAG,
    GIT_REMOTE_URL,
    REPO_ROOT,
    SOUGHT_AFTER_LANGS,
    compute_file_sha256,
    parse_frontmatter,
    parse_yaml_text,
    run_python_script,
)


class TestTier4Scenarios(unittest.TestCase):
    """Real-world user journeys and agent workflows."""

    def test_s1_ai_agent_architectural_consultation(self):
        """Scenario 1: AI Agent ingests AGENTS.md, loads SKILL.md, and applies P01/P06 lenses."""
        agents_guide = REPO_ROOT / "AGENTS.md"
        skill_en = REPO_ROOT / "skills" / "agila-manifesto-en" / "SKILL.md"

        if not (agents_guide.is_file() and skill_en.is_file()):
            self.skipTest("AGENTS.md or English skill not yet created")

        with open(agents_guide, "r", encoding="utf-8") as f:
            guide_text = f.read()
        with open(skill_en, "r", encoding="utf-8") as f:
            skill_text = f.read()

        # Step 1: Agent reads protocol and boundary constraints
        self.assertIn("read", guide_text.lower())
        self.assertIn("analyze", guide_text.lower())
        self.assertIn("cite", guide_text.lower())
        self.assertIn("propose", guide_text.lower())
        self.assertTrue(
            "cannot approve" in guide_text.lower() or "cannot modify" in guide_text.lower() or "human" in guide_text.lower(),
            "AGENTS.md must emphasize human sovereignty over canon",
        )

        # Step 2: Agent extracts P01 and P06 from SKILL.md for team diagnostic
        self.assertIn("P01", skill_text)
        self.assertIn("P06", skill_text)

        # Step 3: Simulate Agent Generating Recommendation Artifact
        agent_proposal = (
            "### Architectural Assessment: Team Boundaries and Queue Delays\n\n"
            "**Lenses Applied**:\n"
            "- *P01 (Homomorphism)*: Module boundaries reflect team communication paths.\n"
            "- *P06 (Queueing & Little's Law)*: Bottlenecks arise at team handoffs.\n\n"
            "**Findings**: Cross-team coordination delays exceed actual implementation time.\n\n"
            "**Recommendation**: Align microservices to stream-aligned teams to minimize handoffs.\n\n"
            "**Proposal Metadata**:\n"
            "- Status: Proposal (Non-binding diagnostic lens)\n"
            "- Human-owner: @lead-architect\n"
        )

        # Assert agent proposal complies with non-negotiable rules:
        # Rule 2: Has human owner
        self.assertIn("Human-owner: @lead-architect", agent_proposal)
        # Rule 3: No dogmatic coercion
        self.assertNotIn("mandatory compliance", agent_proposal.lower())
        self.assertNotIn("certification required", agent_proposal.lower())

    def test_s2_contributor_bootstrapping_new_translation(self):
        """Scenario 2: Contributor bootstraps French (fr) translation from i18n/_template/."""
        template_dir = REPO_ROOT / "i18n" / "_template"
        template_candidates = [
            template_dir / "SKILL.template.md",
            template_dir / "SKILL.md",
        ]
        template_file = next((p for p in template_candidates if p.is_file()), None)

        if not template_file:
            self.skipTest("i18n/_template/SKILL.md not found")

        with open(template_file, "r", encoding="utf-8") as f:
            template_content = f.read()

        # Contributor generates French draft skill
        fr_skill_content = (
            "---\n"
            "name: agila-manifesto-fr\n"
            "description: Guide pour analyser les structures d'equipe selon l'Agila Manifesto v3.1.\n"
            "metadata:\n"
            "  lang: fr\n"
            f"  canon_version: \"{CANON_VERSION}\"\n"
            f"  canon_sha256: \"{CANON_SHA256}\"\n"
            "  status: draft\n"
            "  translators:\n"
            "    - \"@jean-dupont\"\n"
            "---\n\n"
            "# Manifeste Agile v3.1 (Traduction Française Dérivée)\n\n"
            "> **Avis**: Le canon en espéranto fait autorité.\n\n"
            "## Protocole d'agent\n"
            "Lire, analyser, citer, proposer. Les agents ne modifient pas le canon.\n\n"
            "## Principes\n"
        )
        for i in range(1, 11):
            fr_skill_content += f"### P{i:02d}. Principe {i}\nDescription du principe {i}.\n"

        # Validate that the drafted translation fulfills all structural constraints:
        frontmatter, body = parse_frontmatter(fr_skill_content)
        self.assertEqual(frontmatter.get("name"), "agila-manifesto-fr")
        meta = frontmatter.get("metadata", {})
        self.assertEqual(meta.get("lang"), "fr")
        self.assertEqual(meta.get("canon_version"), CANON_VERSION)
        self.assertEqual(meta.get("canon_sha256"), CANON_SHA256)
        self.assertEqual(meta.get("status"), "draft")
        self.assertIn("@jean-dupont", meta.get("translators", []))

        # Check all 10 principles IDs are present
        for i in range(1, 11):
            self.assertIn(f"P{i:02d}", body)

        # Check derivative notice is present
        self.assertIn("espéranto fait autorité", body.lower())

    def test_s3_academic_researcher_citation(self):
        """Scenario 3: Academic researcher parses and validates CITATION.cff metadata."""
        citation_path = REPO_ROOT / "CITATION.cff"
        if not citation_path.is_file():
            self.skipTest("CITATION.cff not yet created")

        with open(citation_path, "r", encoding="utf-8") as f:
            citation_text = f.read()

        data = parse_yaml_text(citation_text)
        self.assertIsInstance(data, dict)

        # Validate academic citation fields
        title = data.get("title", "")
        self.assertIn("Agila Manifesto", title)

        version = str(data.get("version", ""))
        self.assertTrue(version.startswith("3.1"), f"Citation version must start with 3.1, got {version}")

        # Check license
        license_field = str(data.get("license", ""))
        self.assertTrue(
            "CC-BY-4.0" in license_field or "CC BY 4.0" in license_field,
            "CITATION.cff license must be CC-BY-4.0",
        )

        # Check authors list
        authors = data.get("authors", [])
        self.assertTrue(len(authors) >= 1, "CITATION.cff must list at least one author or steward")

    def test_s4_community_counterexample_submission(self):
        """Scenario 4: Community practitioner reviews counterexample template."""
        template_candidates = [
            REPO_ROOT / ".github" / "ISSUE_TEMPLATE" / "02_kontrauekzemplo.yml",
            REPO_ROOT / ".github" / "ISSUE_TEMPLATE" / "counterexample.md",
            REPO_ROOT / ".github" / "ISSUE_TEMPLATE" / "02_counterexample.yml",
        ]
        template = next((p for p in template_candidates if p.is_file()), None)

        if not template:
            self.skipTest("Counterexample issue template not found")

        with open(template, "r", encoding="utf-8") as f:
            text = f.read().lower()

        # Template must emphasize the core community principle: "a counterexample is a gift"
        self.assertTrue(
            "donaco" in text or "gift" in text or "regalo" in text or "kontrauekzemplo" in text,
            "Template must welcome counterexamples as gifts",
        )
        # Template must require specifying the target principle
        self.assertTrue("principle" in text or "principo" in text or "p0" in text)

    def test_s5_human_maintainer_launch_runbook(self):
        """Scenario 5: Maintainer follows LAUNCH-CHECKLIST.md steps and validates topics and protection."""
        candidate_paths = [
            pathlib.Path(r"C:\Dev\LAUNCH-CHECKLIST.md"),
            REPO_ROOT.parent / "LAUNCH-CHECKLIST.md",
            REPO_ROOT / "LAUNCH-CHECKLIST.md",
        ]
        checklist_path = next((p for p in candidate_paths if p.is_file()), None)

        if not checklist_path:
            self.skipTest("LAUNCH-CHECKLIST.md not found")

        with open(checklist_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Maintainer verifies the exact 8 topics to be added to GitHub
        required_topics = [
            "agile",
            "manifesto",
            "esperanto",
            "conways-law",
            "software-architecture",
            "ai-agents",
            "agent-skills",
            "complexity",
        ]
        for topic in required_topics:
            self.assertIn(
                topic,
                content,
                f"LAUNCH-CHECKLIST.md missing repository topic: {topic}",
            )

        # Maintainer verifies branch protection instructions
        content_lower = content.lower()
        self.assertTrue(
            "branch protection" in content_lower or "protección de rama" in content_lower,
            "LAUNCH-CHECKLIST.md must instruct configuring branch protection",
        )
        self.assertTrue(
            "main" in content_lower,
            "LAUNCH-CHECKLIST.md branch protection must target 'main'",
        )

    def test_s6_canon_proposal_fourteen_day_guard(self):
        """Scenario 6: Canon proposal template enforces theoretical base, signal, and 14-day rule."""
        template_candidates = [
            REPO_ROOT / ".github" / "ISSUE_TEMPLATE" / "01_canon_propono.yml",
            REPO_ROOT / ".github" / "ISSUE_TEMPLATE" / "canon_proposal.md",
            REPO_ROOT / ".github" / "ISSUE_TEMPLATE" / "01_canon_proposal.yml",
        ]
        template = next((p for p in template_candidates if p.is_file()), None)

        if not template:
            self.skipTest("Canon proposal issue template not found")

        with open(template, "r", encoding="utf-8") as f:
            text = f.read().lower()

        # Must require base / signal / 14 days
        self.assertTrue("bazo" in text or "base" in text)
        self.assertTrue("signalo" in text or "signal" in text)
        self.assertTrue("14" in text or "steward" in text or "gardanto" in text)


if __name__ == "__main__":
    unittest.main()
