# Architecture of the Agila Manifesto Repository

## 1. Architectural Philosophy

The **Agila Manifesto** is engineered as an open, multilingual socio-technical repository. It serves as both an authoritative publication of the manifesto v3.1 and an active platform for automated agent collaboration and community governance.

```
                          ┌──────────────────────────┐
                          │   canon/ (Esperanto)     │
                          │   AGILA-MANIFESTO.eo.md   │
                          │   manifesto.eo.yaml       │
                          └─────────────┬────────────┘
                                        │ (Authority: Sovereign Canon)
                                        ▼
      ┌─────────────────────────────────┼─────────────────────────────────┐
      │                                 │                                 │
      ▼                                 ▼                                 ▼
┌──────────────┐              ┌──────────────────┐              ┌──────────────────┐
│   skills/    │              │      docs/       │              │     uzado/       │
│  eo, en, es  │              │  OpenWiki Guides │              │ Applied Patterns │
└──────────────┘              └──────────────────┘              └──────────────────┘
      ▲                                 ▲                                 ▲
      │                                 │                                 │
      └─────────────────────────────────┴─────────────────────────────────┘
                                        │ (Operational Guidance)
                                        │
                         ┌──────────────┴─────────────┐
                         │   AGENTS.md & llms.txt     │
                         │   (Human-in-the-loop)      │
                         └────────────────────────────┘
```

---

## 2. Core Repository Layers

### 2.1 The Canonical Core (`canon/`)
The foundation of the entire system resides in `canon/`:
- `canon/AGILA-MANIFESTO.eo.md`: Byte-for-byte exact Esperanto canon text. No automated script, machine agent, or translator can alter this file without human steward consensus.
- `canon/manifesto.eo.yaml`: Structured, machine-readable representation of the 10 principles, their mathematical bases (`bazo`), observable signals (`signalo`), and Conway mapping.

### 2.2 Translation & Agent Skills (`skills/`)
Each supported language provides an agent skill in `skills/agila-manifesto-<lang>/SKILL.md`:
- Encapsulates YAML frontmatter with strict metadata (`lang`, `canon_version`, `canon_sha256`, `status`, `translators`).
- Embeds the non-negotiable 4-verb agent protocol: **read**, **analyze**, **cite**, and **propose**.
- Mandates explicit human ownership (`Human-owner: @username`) for all agent recommendations.
- Preserves universal identifiers `P01` through `P10`.

### 2.3 Documentation OpenWiki (`docs/`)
Comprehensive architectural deep dives, epistemological foundations, and practical adoption guides for humans and machines:
- Principles breakdown (`docs/principles/p01.md` through `p10.md`).
- Mathematical analysis of Conway derivations (`docs/conway-derivations.md`).
- Human and agent operational guides (`docs/guides/`).

### 2.4 Open Practice Layer (`uzado/`)
A community-driven tier operating under low protection:
- Houses empirical case studies, anti-patterns, and architectural recipes.
- Enables rapid knowledge exchange without modifying canonical theory.

---

## 3. Governance Integration

The repository enforces three tiers of governance:
1. **Tier 1 (Fundamento - High / Jealous)**: Protects `canon/`. Only human stewards ($\ge 2$) can approve changes after a mandatory 14-day public RFC. No AI agent may merge or approve canon changes.
2. **Tier 2 (Tradukoj - Medium)**: Protects `skills/` and `i18n/`. Requires review by the language maintainer plus a native speaker.
3. **Tier 3 (Uzado - Open)**: Protects `uzado/`. Fast-track review requiring one maintainer or peer approval.

---

## 4. Verification and Parity

Continuous Integration (`.github/workflows/`) and autonomous verification scripts (`scripts/validate.py`) ensure:
- Exact SHA-256 integrity of the Esperanto canon.
- 1:1 parity between canonical markdown and YAML representations.
- Detection of translation drift whenever the canon evolves.
- Validation that all internal links resolve across documentation.
