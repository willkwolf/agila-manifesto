# Agila Manifesto v3.1 — E2E Test Suite Infrastructure (`TEST_INFRA.md`)

## 1. Overview & Architecture

The Agila Manifesto test suite provides an **Opaque-Box End-to-End (E2E) Verification Architecture** designed for human auditors and autonomous verification workflows. It treats the repository as a black box, validating file integrity, cryptographic checksums, schema structures, agent protocols, cross-file synchronization, and real-world user journeys.

### Core Architecture Principles
1. **Zero External Dependencies**: Built exclusively on Python's standard library (`unittest`, `hashlib`, `pathlib`, `re`, `subprocess`, `json`, `os`, `tempfile`, `shutil`). Runs out of the box in any standard Python $\ge 3.8$ environment without `pip install`.
2. **Deterministic & Isolated**: All negative, tampering, and mutation tests execute within isolated temporary workspaces (`tempfile.TemporaryDirectory`) to guarantee that the primary repository state remains pristine and uncorrupted.
3. **No Facade or Hardcoded Tests**: Every assertion verifies genuine specifications, byte-level invariants, or schema contracts derived directly from `ORIGINAL_REQUEST.md`.
4. **Progressive Testability**: Leverages `unittest.TestCase.skipTest` when encountering dependencies from downstream milestones during parallel development, turning strictly to full assertion passes once all artifacts are in place.

---

## 2. Directory Layout & Module Structure

```
tests/
├── __init__.py                  # Test package initialization
├── common.py                    # Shared authoritative constants, SHA-256 helpers, YAML/frontmatter parsers
├── test_tier1_features.py       # Tier 1: Feature coverage (F1 to F7, 44 tests)
├── test_tier2_boundaries.py     # Tier 2: Boundary, corner & negative tests (D1 to D5, 24 tests)
├── test_tier3_combinations.py   # Tier 3: Pairwise combinatorial integration tests (P1 to P6, 6 tests)
└── test_tier4_scenarios.py      # Tier 4: Real-world user & agent scenarios (S1 to S6, 6 tests)
```

### Module Responsibilities

| Module | Scope | Assertions / Tests | Key Verification Target |
|---|---|---|---|
| `tests/common.py` | Shared Infrastructure | Utilities & Constants | SHA-256 hashing, stdlib YAML parsing, frontmatter extraction, CLI execution |
| `tests/test_tier1_features.py` | Tier 1: Feature Coverage | 44 tests | Canon byte fidelity, YAML parity, skills metadata, strict 13-section README, 3-tier governance, scripts, git hygiene |
| `tests/test_tier2_boundaries.py` | Tier 2: Boundary & Corner | 24 tests | Single-byte corruption, missing headers, YAML syntax/count errors, skill hash drift, malformed READMEs, git exclusion |
| `tests/test_tier3_combinations.py` | Tier 3: Pairwise Combinations | 6 tests | Canon $\leftrightarrow$ YAML $\leftrightarrow$ Skills $\leftrightarrow$ README $\leftrightarrow$ CODEOWNERS $\leftrightarrow$ Workflows |
| `tests/test_tier4_scenarios.py` | Tier 4: Scenarios & Journeys | 6 tests | AI agent architecture review, bootstrapping translations (`fr`), citation parsing, counterexample submissions, launch runbook |

---

## 3. Test Runner Commands

### Standard Test Execution (Recommended)
To discover and run the entire 4-tier test suite using Python's standard library test runner:

```powershell
python -m unittest discover -s tests -p "test_*.py" -v
```

### Running Individual Tiers
```powershell
# Tier 1: Feature Coverage
python -m unittest tests/test_tier1_features.py -v

# Tier 2: Boundary & Corner Cases
python -m unittest tests/test_tier2_boundaries.py -v

# Tier 3: Pairwise Combinations
python -m unittest tests/test_tier3_combinations.py -v

# Tier 4: Real-World Scenarios
python -m unittest tests/test_tier4_scenarios.py -v
```

### Running Autonomous Validator Script Directly
```powershell
python scripts/validate.py --check
```

---

## 4. Pass / Fail Semantics

- **Exit Code 0**: All executed test assertions passed successfully.
- **Exit Code 1**: One or more assertions failed or encountered an unexpected runtime error.
- **Skip Semantics (`s`)**: Tests targeting files not yet created by parallel milestones cleanly skip and report their reason, allowing non-blocking progress until Milestone M7 (Final E2E Pass & Hardening).
- **Failure Diagnostics**: Every test failure produces a descriptive error message indicating:
  - Exact file path evaluated.
  - Expected authoritative value vs. observed value.
  - Violated specification requirement or non-negotiable rule.

---

## 5. Feature Checklist & Coverage Matrix

### Non-Negotiable Rules Coverage
- [x] **Rule 1 (Sole Esperanto Canon)**: Tested in `test_tier1_features.py` (F1.1 to F1.6) and `test_tier2_boundaries.py` (D1.1 to D1.6). Verifies verbatim LF line endings, 6,213 bytes, and canonical SHA-256 `44dd1dc966874fceea8d53d9ac312397b1fcb5e9f51919bbe0e71b19d027c470`.
- [x] **Rule 2 (Human Canon Sovereignty)**: Tested in `test_tier1_features.py` (F3.5), `test_tier2_boundaries.py` (D3.4), and `test_tier4_scenarios.py` (S1, S6). Verifies AI agents cannot approve or edit canon.
- [x] **Rule 3 (Without Dogma)**: Tested in `test_tier1_features.py` (F4.2), `test_tier2_boundaries.py` (D4.4), and `test_tier4_scenarios.py` (S1). Verifies principles are presented as analytical lenses, never mandatory compliance or certification.
- [x] **Rule 4 (Honesty & Transparency)**: Tested in `test_tier1_features.py` (F4.4, F4.5) and `test_tier3_combinations.py` (P6). Verifies real badges and transparent declaration that exactly 8 of 10 principles derive from Conway's Law as a design tendency.
- [x] **Rule 5 (Minimal Maintenance & CI Drift)**: Tested in `test_tier1_features.py` (F6.1 to F6.5), `test_tier2_boundaries.py` (D3.1), and `test_tier3_combinations.py` (P1, P2). Verifies autonomous drift detection and table regeneration.

### Acceptance Criteria Verification Matrix
| ID | Requirement | Test Case | Target Artifact |
|---|---|---|---|
| AC-1 | Verbatim Canon Extraction | `TestTier1CanonFidelity.test_f1_canon_sha256_fidelity` | `canon/AGILA-MANIFESTO.eo.md` |
| AC-2 | Machine Summary Parity | `TestTier1YamlParity.test_f2_yaml_ten_principles_count` | `canon/manifesto.eo.yaml` |
| AC-3 | Agent Skills & Metadata | `TestTier1TranslationSkills.test_f3_skills_directories_exist` | `skills/agila-manifesto-{eo,en,es}/SKILL.md` |
| AC-4 | Strict 13-Section README | `TestTier1ReadmeArchitecture.test_f4_readme_thirteen_sections_sequence` | `README.md` |
| AC-5 | 3-Tier Governance | `TestTier1GovernanceCommunity.test_f5_governance_three_tiers_defined` | `GOVERNANCE.md` |
| AC-6 | Dual Licensing | `TestTier1GovernanceCommunity.test_f5_license_dual_licensing` | `LICENSE` (CC BY 4.0 / MIT) |
| AC-7 | Automated Validation | `TestTier1AutomationScripts.test_f6_validate_check_flag` | `scripts/validate.py` |
| AC-8 | Local Git Exclusion | `TestTier1GitHygieneAndLaunch.test_f7_git_exclude_file_exists` | `.git/info/exclude` |
| AC-9 | Zero Committed .gitignore | `TestTier1GitHygieneAndLaunch.test_f7_no_committed_gitignore` | Repository root |
| AC-10 | External Launch Checklist | `TestTier1GitHygieneAndLaunch.test_f7_external_launch_checklist_exists` | `C:\Dev\LAUNCH-CHECKLIST.md` |
