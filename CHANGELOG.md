# Changelog

All notable changes to the **Agila Manifesto** project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html) for canon evolution.

---

## [3.1.0] - 2026-11-10

### Added
- **Canonical Esperanto Anchor**:
  - Published authoritative v3.1 canon in `canon/AGILA-MANIFESTO.eo.md` (49 lines, pure LF line endings, byte-for-byte verified with SHA-256 `44dd1dc966874fceea8d53d9ac312397b1fcb5e9f51919bbe0e71b19d027c470`).
  - Reconciled typographic delimiters and grammatical/stylistic nuances (comparative ellipsis, observer reference, statistical dispersion terminology, passive limitation construction, and boundary traversal harmonisation) directly authorized by the author/proponent.
  - Generated machine-readable summary in `canon/manifesto.eo.yaml` modeling all 10 principles (P01–P10), theoretical bases, observable signals, and Conway derivations.
- **Agent Translation Skills**:
  - Created standardized agent skills in `skills/agila-manifesto-eo/` (canonical status), `skills/agila-manifesto-en/` (draft status), and `skills/agila-manifesto-es/` (draft status).
  - Established universal 4-verb agent protocol (read, analyze, cite, propose) with mandatory human ownership and non-dogmatic diagnostic lenses.
  - Provided `i18n/_template/` for community bootstrapping of new translations and cataloged 10 priority sought-after languages.
  - Published internationalization dashboard in `i18n/STATUS.md`.
- **Documentation & OpenWiki Tree**:
  - Structured primary English `README.md` strictly containing 13 ordered sections, transparent 8/10 Conway derivation declaration, real badges, and dynamic translation table markers.
  - Derived faithful `README.eo.md` and `README.es.md` with explicit derivative disclaimers.
  - Built comprehensive `docs/` OpenWiki covering philosophy, Conway derivations, in-depth architectural analyses of principles P01 through P10, and operational guides for humans and agents.
  - Created open usage layer in `uzado/` with real-world case studies, architectural patterns, and anti-patterns under low-protection governance.
  - Added machine-readable agent guides in `AGENTS.md` and `llms.txt`.
- **3-Tier Governance & Community Architecture**:
  - Defined 3-tier governance in `GOVERNANCE.md`: Fundamento (high/human-only, 14-day deliberation, $\ge 2$ human stewards, single-steward fallback), Tradukoj (medium, language maintainer + native reviewer), and Uzado (open, 1 review).
  - Codified SemVer rules for canon: MAJOR (principle count/semantic direction), MINOR (theoretical base/signal/framing), PATCH (typos/orthography).
  - Published `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md` (Contributor Covenant v2.1), `CITATION.cff` (Citation File Format v1.2.0), and `.github/CODEOWNERS`.
  - Established dual licensing in `LICENSE`: Creative Commons Attribution 4.0 International (CC BY 4.0) for written works and MIT License for software and scripts.
- **Automation & Continuous Integration**:
  - Implemented standalone Python verification utility `scripts/validate.py` (standard library only) supporting `--check` (exit code 0/1) and `--update` (synchronizing `i18n/STATUS.md` and `README.md` translation tables).
  - Implemented GitHub Actions CI workflows in `.github/workflows/`:
    - `pr-validation.yml`: Validates canon integrity, YAML parity, skill metadata, and internal markdown links on PRs.
    - `canon-drift.yml`: Automatically detects hash mismatches on canon updates and opens/updates language drift tracking issues.
    - `governance-guard.yml`: Enforces `Human-owner:` sponsor declaration on canon PRs and blocks unauthorized machine self-merges.
    - `release.yml`: Automates release asset generation, checksum publishing, and release notes extraction upon tag push.
  - Added GitHub issue templates (`01_canon_propono.yml`, `02_kontrauekzemplo.yml`, `03_nova_traduko.yml`, `04_korektu_tradukon.yml`, `05_uzado_kontribuo.yml`) and `pull_request_template.md`.

[3.1.0]: https://github.com/willkwolf/agila-manifesto/releases/tag/v3.1.0
