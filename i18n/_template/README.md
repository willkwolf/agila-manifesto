# Translation Guide and Internationalization Template

Welcome to the translation guide for the **Agila Manifesto v3.1**.

This directory provides the official templates and contribution guidelines for translating the Agila Manifesto into new human languages for use by humans and AI agents.

---

## 1. Single Canon Principle (Rule 1)

The Agila Manifesto maintains **exactly one authoritative canon: Esperanto** (`canon/AGILA-MANIFESTO.eo.md`).
- All translations (including English, Spanish, and any community translation) are strictly **derivative works**.
- In any event of discrepancy, semantic divergence, or ambiguity between a translation and the Esperanto text, **the Esperanto canon unconditionally prevails**.
- Translators must faithfully capture the nuances of the canon without injecting dogma, personal interpretations, or additional constraints.

---

## 2. Tier 2 Governance Rules for Translations

Under repository governance, translations fall under **Tier 2 (Tradukoj / Translations)**:
- **Protection Level**: Medium.
- **Review Requirements**: Approval by at least **one language maintainer** plus **one verified native speaker reviewer**.
- **Structural Invariants**:
  - Exact preservation of principle identifiers: `P01` through `P10`.
  - Preservation of the tripartite structure: Principle Title/Elaboration, Theoretical Basis (`Basis` / `Bazo` / `Base`), and Observable Signal (`Signal` / `Signalo` / `Señal`).
  - Strict preservation of the universal 5-point agent protocol (read, analyze, cite, propose; zero modification authority; explicit human owner; diagnostic lenses without dogma; canon primacy).
  - Explicit derivative notice blockquote at the top of the skill.
  - Pinning of canonical metadata in YAML frontmatter:
    - `canon_version: "3.1"`
    - `canon_sha256: "44dd1dc966874fceea8d53d9ac312397b1fcb5e9f51919bbe0e71b19d027c470"`
    - `status: draft` (promoted to `reviewed` after native community review).

---

## 3. Step-by-Step Translation Workflow

Follow this procedure to contribute a new translation:

1. **Check Existing Issues**: Check existing issues to verify that the language is not already being drafted. Open a new issue using `.github/ISSUE_TEMPLATE/03_nova_traduko.yml`.
2. **Branch**: Create a git branch named `i18n/<lang>` (where `<lang>` is the lowercase ISO 639-1 two-letter code, e.g. `i18n/fr`).
3. **Scaffold from Template**:
   - Create directory `skills/agila-manifesto-<lang>/`.
   - Copy `i18n/_template/SKILL.template.md` to `skills/agila-manifesto-<lang>/SKILL.md`.
4. **Translate**:
   - Update frontmatter: `name: agila-manifesto-<lang>`, `metadata.lang: <lang>`, and add your GitHub handle to `metadata.translators`.
   - Translate the primary title, derivative notice, 5-point agent protocol, and all 10 principles P01–P10.
   - Ensure theoretical basis and observable signal are translated consistently.
5. **Validate Locally**:
   - Run verification: `python scripts/validate.py --check` (or unit tests).
   - Verify frontmatter YAML parses correctly without syntax errors.
6. **Submit Pull Request**:
   - Submit PR with title `feat(i18n): add <Language Name> (<lang>) translation`.
   - Include `Human-owner: @your-username` in the description.
   - Tag a native speaker reviewer for peer review.

---

## 4. Priority Sought-After Languages

The following 10 languages represent priority target translations sought by the community:

| # | Code | English Name | Native Name | Target Skill File | Status |
|---|---|---|---|---|---|
| 1 | `zh` | Chinese | 中文 | `skills/agila-manifesto-zh/SKILL.md` | Wanted |
| 2 | `hi` | Hindi | हिन्दी | `skills/agila-manifesto-hi/SKILL.md` | Wanted |
| 3 | `ar` | Arabic | العربية | `skills/agila-manifesto-ar/SKILL.md` | Wanted |
| 4 | `pt` | Portuguese | Português | `skills/agila-manifesto-pt/SKILL.md` | Wanted |
| 5 | `fr` | French | Français | `skills/agila-manifesto-fr/SKILL.md` | Wanted |
| 6 | `ru` | Russian | Русский | `skills/agila-manifesto-ru/SKILL.md` | Wanted |
| 7 | `ja` | Japanese | 日本語 | `skills/agila-manifesto-ja/SKILL.md` | Wanted |
| 8 | `de` | German | Deutsch | `skills/agila-manifesto-de/SKILL.md` | Wanted |
| 9 | `id` | Indonesian | Bahasa Indonesia | `skills/agila-manifesto-id/SKILL.md` | Wanted |
| 10 | `bn` | Bengali | বাংলা | `skills/agila-manifesto-bn/SKILL.md` | Wanted |

Community translations for languages outside this list are also welcomed under Tier 2 governance.
