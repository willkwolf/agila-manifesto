# Agila Manifesto

**Deliver quality software.**

A living socio-technical manifesto of 10 invariant principles for distributed systems and human-agent teams.

---

## 1. Deliver quality software

The **Agila Manifesto** (v3.1) is an open-source socio-technical framework for delivering quality software in modern distributed organizations.

When software systems fail to scale or delivery stalls, the root cause is rarely algorithmic—it is structural. The Agila Manifesto formalizes the empirical invariants that govern system architecture, organizational communication, and collaborative flow under the mathematical reality of Conway's Law and systems theory.

- **The Problem It Solves**: Architectural misalignments, cognitive overload in teams, unpacted inter-service boundaries, queue explosions at handoffs, and unregulated AI agent outputs.
- **Dual Audience**: Built from day one to be directly understood and applied by human teams and autonomous AI agents.
- **Sole Canon in Esperanto**: Anchored in a politically neutral international language ([`canon/AGILA-MANIFESTO.eo.md`](canon/AGILA-MANIFESTO.eo.md)) to guarantee an equitable foundation free from cultural bias.
- **Human Sovereignty**: AI agents read, analyze, cite, and propose; only humans approve changes to the canon.

---

## 2. Badges

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-blue.svg)](LICENSE)
[![Code License: MIT](https://img.shields.io/badge/Code_License-MIT-green.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-v3.1-blue.svg)](CHANGELOG.md)
[![CI Validation](https://github.com/willkwolf/agila-manifesto/actions/workflows/pr-validation.yml/badge.svg)](https://github.com/willkwolf/agila-manifesto/actions)
[![Languages](https://img.shields.io/badge/languages-3_available-informational.svg)](i18n/STATUS.md)

---

## 3. In 30 seconds

- **Structural Invariants, Not Agile Ceremonies**: Replaces process dogma with empirical laws (Conway's Law, Little's Law, Ashby's requisite variety, bounded rationality).
- **Diagnostic Lenses, Not Scoring Rubrics**: Analytical lenses to identify friction in architectures and team topologies, never a certification scheme or developer ranking tool.
- **Human-Agent Collaboration**: Defines explicit boundary pacts and human ownership rules for AI coding agents participating in modern engineering workflows.

---

## 4. The 10 Principles at a Glance

> **Conway Derivation Notice**: 8 of 10 principles (P01 through P08) derive from Conway's Law (1968) or its mathematical corollaries. This is declared with full transparency as an empirical **design tendency**, not an immutable dogma. Principles P09 (Complexity) and P10 (Evolution) derive from complex adaptive systems and Lehman's laws.

| # | Principle | Theoretical Foundation (`Bazo`) | Derives from Conway? |
|---|-----------|----------------------------------|----------------------|
| [**P01**](docs/principles/p01.md) | Every system mirrors the communication structure of its creators | Homomorphism between communication graph and system module graph; inverse Conway maneuver | **Yes** (Direct Conway's Law) |
| [**P02**](docs/principles/p02.md) | Every decision unit has finite capacity | Shannon channel capacity, Simon's bounded rationality, $O(n^2)$ communication growth | **Yes** (Cognitive load corollary) |
| [**P03**](docs/principles/p03.md) | Stable systems are strong inside and weak across boundaries | Simon's nearly decomposable systems, Ashby's requisite variety, boundary pacts | **Yes** (Modularity corollary) |
| [**P04**](docs/principles/p04.md) | The effective interface is everything observable | Observational equivalence, Hyrum's Law (implicit dependencies) | **Yes** (Interface boundary corollary) |
| [**P05**](docs/principles/p05.md) | Reliability is born from redundancy | Von Neumann synthesis of reliable systems from unreliable components, degeneracy | **Yes** (Bus-factor topology corollary) |
| [**P06**](docs/principles/p06.md) | Flow is governed by waiting, not effort | Little's Law ($L = \lambda W$), Kingman's formula for queue waiting times | **Yes** (Handoff friction corollary) |
| [**P07**](docs/principles/p07.md) | A learning system changes its structure, not just its actions | Argyris & Schön double-loop learning, structural cybernetic adaptation | **Yes** (Inverse structural realignment) |
| [**P08**](docs/principles/p08.md) | Every agent is part of the communication structure | Graph theory with human and AI agent nodes; boundary traversal requires human pact | **Yes** (Multi-agent network expansion) |
| [**P09**](docs/principles/p09.md) | In complexity, understanding follows action | Complex adaptive systems, Popperian falsifiability, Goodhart/Campbell's Law | **No** (Complexity science) |
| [**P10**](docs/principles/p10.md) | A system in use degrades without continuous maintenance | Lehman's Laws of Software Evolution, open thermodynamic dissipative systems | **No** (Lehman's software dynamics) |

For complete mathematical foundations and proof sketches, see [docs/conway-derivations.md](docs/conway-derivations.md) and [docs/principles/](docs/principles/).

---

## 5. Distinctions from the 2001 Agile Manifesto

The Agila Manifesto builds upon the foundations of the 2001 Agile Manifesto while addressing the realities of modern software engineering:

1. **Structural Invariants Over Subjective Values**: Rather than preferences ("valuing X over Y"), it identifies systemic laws (graph homomorphisms, queueing limits) that govern whether architectures succeed or stall.
2. **Human-Agent Collaboration**: Explicitly incorporates autonomous AI agents into the communication graph with mandatory human ownership (P08).
3. **Observable Signals Over Aspirational Slogans**: Every principle pairs a theoretical basis (`Bazo`) with an observable symptom (`Signalo`) to diagnose debt before failures cascade.

---

## 6. Status, Without Dogma, Minimal Formal Language, Why Esperanto

*(Derived from the canonical Esperanto declarations)*

- **Living Status**: An open, living proposal (v3.1) refined through community observation and counterexamples.
- **Without Dogma**: Principles are diagnostic lenses, never compliance checklists, performance metrics, or certification schemes.
- **Minimal Formal Language**: Graph theory, queueing models, and cybernetics are used strictly for precision, avoiding unnecessary academic jargon.
- **Why Esperanto?**: Esperanto provides a politically neutral international anchor ([`canon/AGILA-MANIFESTO.eo.md`](canon/AGILA-MANIFESTO.eo.md)) that prevents cultural hegemony and ensures deliberate, conscious consensus for any structural change.

---

## 7. How to Use the Manifesto (For Humans)

Apply the principles as **diagnostic lenses** whenever your team or architecture encounters friction:

- **When to Use**:
  - **System & Service Design**: Ensuring module boundaries mirror team communication paths (P01, P03).
  - **Technical Proposals (RFCs / ADRs)**: Evaluating cognitive load, observable coupling, and cross-team dependencies (P02, P04, P06).
  - **Blocked Delivery Pipelines**: Diagnosing queue bottlenecks and near-100% resource utilization (P06).
  - **AI Tooling & Agent Integration**: Ensuring AI outputs cross team boundaries only with explicit human review and ownership (P08).
- **Practical Patterns**: See [Open Practice Layer (`uzado/`)](uzado/README.md) and the [Human Implementation Guide](docs/guides/human-guide.md).

---

## 8. For AI Agents & Integration

The Agila Manifesto is designed to be consumed by AI coding agents as a **complementary contract** during system design, technical proposal reviews, and architectural decision-making.

### Quick Installation by Platform

- **Claude Code**:
  Copy the skill to your project:
  ```bash
  mkdir -p .claude/skills/agila-manifesto
  cp skills/agila-manifesto-en/SKILL.md .claude/skills/agila-manifesto/
  ```
- **Google Antigravity**:
  Add `skills/agila-manifesto-en/SKILL.md` to your workspace skills or link it via `.gemini/antigravity/rules/`.
- **OpenAI Codex / Cursor / OpenCode**:
  Point your assistant to [`AGENTS.md`](AGENTS.md) and [`llms.txt`](llms.txt), or load [`canon/manifesto.eo.yaml`](canon/manifesto.eo.yaml) directly.
- **OpenHarness (`oh`)**:
  Drop `skills/agila-manifesto-en/` into your OpenHarness skills folder or reference it from your agent harness configuration.

For complete integration patterns and workflows, see the [Agent Integration Strategy Guide](docs/guides/integration-strategy.md).

### Non-Negotiable Agent Boundaries
1. **4 Verbs**: Agents **read** canon, **analyze** systems, **cite** principle IDs (`P01`–`P10`), and **propose** improvements.
2. **Zero Modification Authority**: Machines cannot modify or approve changes to the canon.
3. **Mandatory Human Sponsorship**: Every agent recommendation must be tagged with a human sponsor (`Human-owner: @username`).
4. **No Performance Grading**: Principles must never be used to evaluate or score human developers.

---

## 9. Governance

A 3-tier governance model balances canonical integrity with open community participation:

| Tier | Scope | Protection | Authorized Actors | Deliberation SLA |
|---|---|---|---|---|
| **Fundamento** | `canon/` | **High** | Humans only ($\ge 2$ stewards) | 14-day public discussion |
| **Tradukoj** | `skills/`, `i18n/` | **Medium** | Language maintainer + native reviewer | Standard PR review |
| **Uzado** | `uzado/` | **Open** | Any contributor (1 review) | Fast-track |

Canon modifications follow strict Semantic Versioning (`MAJOR` for principles, `MINOR` for bases/signals, `PATCH` for wording). Details in [GOVERNANCE.md](GOVERNANCE.md).

---

## 10. Languages & Translations

Community translations are tracked and monitored by CI against the canonical SHA-256 hash:

<!-- START_TRANSLATION_TABLE -->
| Lang | Language | Status | Canon Ver | Canon SHA-256 Match | Translators / Reviewers | Skill File |
|---|---|---|---|---|---|---|
| `en` | English | `draft` | 3.1 | `44dd1dc96687` (Match) | AI Agent (Draft), @willkwolf | [`skills/agila-manifesto-en/SKILL.md`](skills/agila-manifesto-en/SKILL.md) |
| `eo` | Esperanto | `reviewed` | 3.1 | `44dd1dc96687` (Match) | canon, @willkwolf | [`skills/agila-manifesto-eo/SKILL.md`](skills/agila-manifesto-eo/SKILL.md) |
| `es` | Español | `draft` | 3.1 | `44dd1dc96687` (Match) | AI Agent (Borrador), @willkwolf | [`skills/agila-manifesto-es/SKILL.md`](skills/agila-manifesto-es/SKILL.md) |
<!-- END_TRANSLATION_TABLE -->

To contribute a translation, see [i18n/_template/](i18n/_template/) and [i18n/STATUS.md](i18n/STATUS.md).

---

## 11. How to Contribute

- **Propose a Canon Change**: Open a [Canon Proposal Issue](.github/ISSUE_TEMPLATE/01_canon_propono.yml) (14-day public discussion).
- **Submit a Counterexample**: *"A counterexample is a gift."* Open a [Counterexample Issue](.github/ISSUE_TEMPLATE/02_kontrauekzemplo.yml).
- **Translate**: Help add or maintain languages using [`i18n/_template/`](i18n/_template/).
- **Share Usage Patterns**: Contribute real-world case studies or patterns to [`uzado/`](uzado/README.md).

See [CONTRIBUTING.md](CONTRIBUTING.md) and [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

---

## 12. Versioning, Citation & License

- **Version**: `v3.1.0` ([CHANGELOG.md](CHANGELOG.md)).
- **Citation**: Bibliographic metadata in [CITATION.cff](CITATION.cff):
  ```bibtex
  @misc{agila_manifesto_2026,
    title        = {Agila Manifesto: Socio-technical Foundations for Software Architecture},
    author       = {Wolf, Will and Contributors},
    year         = {2026},
    version      = {3.1.0},
    url          = {https://github.com/willkwolf/agila-manifesto}
  }
  ```
- **License**: Dual licensing under [LICENSE](LICENSE) — [CC BY 4.0](LICENSE) for documentation and canon; [MIT](LICENSE) for scripts and tooling.

---

## 13. FAQ

### Does this replace the 2001 Agile Manifesto?
**No.** It is an independent evolutionary proposal incorporating 25 years of empirical progress in distributed computing, team topologies, and AI agents.

### Why is the canon written in Esperanto?
Esperanto provides a neutral international auxiliary language that prevents cultural hegemony and requires deliberate consensus for structural change.

### Can an AI agent modify the manifesto?
**No.** Machines read, analyze, cite, and propose; only humans approve changes to the canon (`Human-owner: @username`).

### Must teams adopt all ten principles?
**No.** The manifesto is non-dogmatic. Use the principles as diagnostic lenses where systemic friction arises.
