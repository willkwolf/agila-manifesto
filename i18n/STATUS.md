# Agila Manifesto Translation & i18n Status

This dashboard tracks the operational state, canonical version alignment, and drift status of all translations of the **Agila Manifesto v3.1**.

## Canonical Reference

- **Authoritative Canon**: `canon/AGILA-MANIFESTO.eo.md` (Esperanto)
- **Canon Version**: `3.1`
- **Canon SHA-256**: `44dd1dc966874fceea8d53d9ac312397b1fcb5e9f51919bbe0e71b19d027c470` (short: `44dd1dc96687`)
- **Total Principles**: 10 (P01–P10)

---

## Active Translations (Tier 1)

| Lang | Language | Status | Canon Ver | Canon SHA-256 Match | Translators / Reviewers | Skill File |
|---|---|---|---|---|---|---|
| `en` | English | `draft` | 3.1 | `44dd1dc96687` (Match) | AI Agent (Draft), @willkwolf | [`skills/agila-manifesto-en/SKILL.md`](../skills/agila-manifesto-en/SKILL.md) |
| `eo` | Esperanto | `reviewed` | 3.1 | `44dd1dc96687` (Match) | canon, @willkwolf | [`skills/agila-manifesto-eo/SKILL.md`](../skills/agila-manifesto-eo/SKILL.md) |
| `es` | Español | `draft` | 3.1 | `44dd1dc96687` (Match) | AI Agent (Borrador), @willkwolf | [`skills/agila-manifesto-es/SKILL.md`](../skills/agila-manifesto-es/SKILL.md) |

---

## Priority Sought-After Translations (Tier 2 Backlog)

The community actively seeks maintainers and native reviewers for the following 10 languages:

| # | Code | Language (EN) | Native Name | Target Directory | Status | Contributors Needed |
|---|---|---|---|---|---|---|
| 1 | `zh` | Chinese | 中文 | `skills/agila-manifesto-zh/` | Wanted | Maintainer + Native Reviewer |
| 2 | `hi` | Hindi | हिन्दी | `skills/agila-manifesto-hi/` | Wanted | Maintainer + Native Reviewer |
| 3 | `ar` | Arabic | العربية | `skills/agila-manifesto-ar/` | Wanted | Maintainer + Native Reviewer |
| 4 | `pt` | Portuguese | Português | `skills/agila-manifesto-pt/` | Wanted | Maintainer + Native Reviewer |
| 5 | `fr` | French | Français | `skills/agila-manifesto-fr/` | Wanted | Maintainer + Native Reviewer |
| 6 | `ru` | Russian | Русский | `skills/agila-manifesto-ru/` | Wanted | Maintainer + Native Reviewer |
| 7 | `ja` | Japanese | 日本語 | `skills/agila-manifesto-ja/` | Wanted | Maintainer + Native Reviewer |
| 8 | `de` | German | Deutsch | `skills/agila-manifesto-de/` | Wanted | Maintainer + Native Reviewer |
| 9 | `id` | Indonesian | Bahasa Indonesia | `skills/agila-manifesto-id/` | Wanted | Maintainer + Native Reviewer |
| 10 | `bn` | Bengali | বাংলা | `skills/agila-manifesto-bn/` | Wanted | Maintainer + Native Reviewer |

---

## Translation Lifecycle States

1. `draft`: Initial draft submitted or machine-translated; undergoing community and native speaker review.
2. `reviewed`: Verified by at least one language maintainer and one native speaker reviewer; passes all schema validation.
3. `stale`: Canon evolved (`canon_sha256` mismatch with current canon); translation requires updating before being marked reviewed again.
