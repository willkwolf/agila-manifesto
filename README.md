# Agila Manifesto

**Deliver quality software.**

A living socio-technical manifesto, readable by humans and machines, with its sole canonical anchor in Esperanto, modifiable only by people.

---

## 1. Deliver quality software

The **Agila Manifesto** (v3.1) is an international, open-source socio-technical framework for delivering quality software in modern distributed organizations and complex adaptive systems.

Unlike traditional methodologies that dictate ceremonies or dogmatic practices, the Agila Manifesto formalizes the structural invariants that govern software architecture, organizational topologies, and collaborative flow. It bridges organizational design and system architecture under the mathematical reality of Conway's Law and systems theory.

Key characteristics:
- **Living Manifesto**: Evolving continuously under rigorous public governance, open counterexamples, and empirical observation.
- **Dual-Audience Architecture**: Engineered from day one to be equally consumable by human teams and autonomous AI agents.
- **Sole Sovereign Canon in Esperanto**: Anchored in a politically neutral international language (`canon/AGILA-MANIFESTO.eo.md`) to establish an equitable foundation free from cultural or linguistic hegemony.
- **Human Sovereignty**: While machines can read, analyze, cite, and propose structural improvements, only humans hold the authority to approve and evolve the canon.

---

## 2. Badges

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-blue.svg)](LICENSE)
[![Code License: MIT](https://img.shields.io/badge/Code_License-MIT-green.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-v3.1-blue.svg)](CHANGELOG.md)
[![CI Validation](https://github.com/willkwolf/agila-manifesto/actions/workflows/pr-validation.yml/badge.svg)](https://github.com/willkwolf/agila-manifesto/actions)
[![Languages](https://img.shields.io/badge/languages-3_available-informational.svg)](i18n/STATUS.md)

*Note on Badge Transparency*: All badges displayed above reflect verified repository attributes. In accordance with our honesty mandate, this repository rejects fictitious vanity badges, purchased stars, or synthetic endorsements.

---

## 3. In 30 seconds

- **Socio-technical Foundations**: Grounded in systems theory, queueing models, and Conway's Law rather than subjective methodologies.
- **Dual-Audience Architecture**: Designed for humans and AI agents with a single neutral canonical source in Esperanto and machine-readable YAML.
- **Descriptive, Non-Dogmatic Lenses**: Analytical diagnostics to assess organizational and architectural friction, never a checklist or certification scheme.

---

## 4. The 10 Principles at a Glance

> **Declaration on Conway Derivations**: 8 of 10 principles (P01 through P08) derive from Conway's Law (1968) or its mathematical and graph-theoretical corollaries (communication graph homomorphism, channel capacity, near-decomposability, interface visibility, redundant paths, queueing across handoffs, structural adaptation, and multi-agent graph membership). This is declared with full transparency as a **design tendency**, not an immutable physical rule. Principles P09 (Complexity & Probes) and P10 (System Degradation) derive respectively from Complex Adaptive Systems / Epistemology and Lehman's Laws of Software Evolution.

| # | Principle | Theoretical Base Status | Derives from Conway? |
|---|-----------|-------------------------|----------------------|
| [**P01**](docs/principles/p01.md) | Every system mirrors the communication structure of its creators | Theorem / Model (Homomorphism between communication graph and module graph; inverse Conway maneuver) | **Yes** (Direct Conway's Law) |
| [**P02**](docs/principles/p02.md) | Every decision unit has finite capacity | Model / Theorem (Shannon channel capacity, Simon's bounded rationality, $O(n^2)$ communication graph edges) | **Yes** (Cognitive load & communication scaling corollary) |
| [**P03**](docs/principles/p03.md) | Stable systems are strong inside and weak across boundaries | Model / Theorem (Simon's nearly decomposable systems, Ashby's law of requisite variety, type theory for pacts) | **Yes** (System modularity & boundary covenant corollary) |
| [**P04**](docs/principles/p04.md) | The effective interface is everything observable | Model / Empirical Tendency (Observational equivalence, Hyrum's Law) | **Yes** (Interface boundary & implicit coupling corollary) |
| [**P05**](docs/principles/p05.md) | Reliability is born from redundancy | Theorem / Model (Von Neumann synthesis of reliable organisms from unreliable components, biological degeneracy) | **Yes** (Communication graph topology & bus factor corollary) |
| [**P06**](docs/principles/p06.md) | Flow is governed by waiting, not effort | Theorem / Model (Little's Law $L = \lambda W$, Kingman's formula for queue waiting times) | **Yes** (Handoff friction across organizational boundaries) |
| [**P07**](docs/principles/p07.md) | A learning system changes its structure, not just its actions | Model / Interpretation (Argyris & Schön double-loop learning, Ashby's requisite variety under environmental shift) | **Yes** (Inverse structural realignment corollary) |
| [**P08**](docs/principles/p08.md) | Every agent is part of the communication structure | Model (Graph theory with human and AI agent nodes, boundary traversal via explicit pacts) | **Yes** (Socio-technical graph expansion to artificial agents) |
| [**P09**](docs/principles/p09.md) | In complexity, understanding follows action | Empirical Tendency / Model (Complex adaptive systems, Popperian falsifiability, Goodhart/Campbell's Law) | **No** (Complexity science & scientific epistemology) |
| [**P10**](docs/principles/p10.md) | A system in use degrades without continuous maintenance | Empirical Tendency (Lehman's Laws of Software Evolution, open thermodynamic non-equilibrium systems) | **No** (Lehman's evolutionary dynamics) |

For comprehensive mathematical foundations, proof sketches, and operational signals, see [docs/conway-derivations.md](docs/conway-derivations.md) and individual deep dives in [docs/principles/](docs/principles/).

---

## 5. Distinctions from the 2001 Agile Manifesto

The Agila Manifesto stands upon the historic foundations laid by the 2001 Agile Manifesto, which liberated software engineering from bureaucratic waterfall processes by centering individuals, working software, collaboration, and responding to change.

Over the past quarter-century, the engineering landscape has evolved fundamentally:
1. **From Subjective Values to Structural Invariants**: While the 2001 manifesto expressed human preferences ("value X over Y"), the Agila Manifesto identifies formal socio-technical laws (homomorphisms, graph capacities, queueing limits) that govern whether software delivery succeeds or stalls.
2. **From Human-Only Teams to Human-Agent Ecosystems**: Autonomous AI agents, code generators, and algorithmic synthesizers now participate actively in the communication and development graph. Principle 8 formally integrates non-human agents with explicit boundary pacts and human ownership.
3. **From Process Dogma to Diagnostic Lenses**: Rather than providing a template for agile meetings or commercial certification schemes, the Agila Manifesto provides analytical lenses to diagnose architectural friction and organizational debt.
4. **Observable Signals Over Aspirational Slogans**: Every principle pairs a theoretical grounding (`Bazo`) with an observable empirical indicator (`Signalo`), enabling teams to identify structural dysfunction before failure cascades occur.

---

## 6. Status, Without Dogma, Minimal Formal Language, Why Esperanto

*(Derived and adapted into English from the canonical declarations)*

### Status
The Agila Manifesto v3.1 is an open, living proposal. It does not present itself as an official industry standard or a corporate mandate, but as an empirical and theoretical foundation continuously refined through public observation and community counterexamples.

### Without Dogma
The manifesto rejects dogmatism in all forms. Its principles must **never** be used as:
- Mandatory compliance checklists or prescriptive organizational commandments.
- Criteria for employee ranking, developer evaluation, or performance grading.
- Proprietary commercial certification products or consultancy licensing gates.

### Minimal Formal Language
Formalisms—including graph theory, Shannon information theory, Little's Law, and Ashby's cybernetic models—are used strictly where necessary to prevent semantic ambiguity. We employ formal language as a tool of precision, not academic pretension.

### Why Esperanto?
Esperanto serves as the sole canonical anchor (`canon/AGILA-MANIFESTO.eo.md`) for three principled reasons:
1. **Linguistic Neutrality**: It belongs equally to all contributors worldwide, avoiding cultural privilege and semantic bias inherent in dominant geopolitical languages.
2. **Structural Regularity**: Its agglutinative and unambiguous morphology ensures precise, stable definitions of socio-technical concepts.
3. **Deliberate Consensus**: Requiring canonical changes to be articulated and reviewed in a shared bridge language fosters intentional, thoughtful consensus and prevents unexamined churn.

---

## 7. For Humans

The manifesto is designed to help human software engineers, architects, managers, and organizational designers diagnose systemic friction.

### The Tripartite Diagnostic Structure
Each principle is articulated through three distinct components:
1. **The Statement**: The concise universal socio-technical law or tendency.
2. **The Grounding (`Bazo`)**: The underlying mathematical theorem, cybernetic model, or empirical trend explaining *why* the phenomenon occurs.
3. **The Observable Signal (`Signalo`)**: The real-world symptom indicating that a team or architecture is violating this structural boundary.

### Applying the Diagnostic Lenses
When a team experiences delays, frequent defects, or coordination overhead:
- Do not add more meetings or bureaucratic gates.
- Consult the principles as diagnostic lenses: Is cognitive load exceeded (P02)? Are interfaces unpacted (P03)? Are queues exploding due to near-100% resource utilization (P06)?
- Consult the practical patterns and case studies in the [Open Practice Layer (`uzado/`)](uzado/README.md).
- Read the detailed human implementation guide in [docs/guides/human-guide.md](docs/guides/human-guide.md).

---

## 8. For AI Agents

Autonomous agents, coding assistants, and LLM-based tools are first-class participants in the modern development graph.

### How to Install the Skill
- **Claude Code**: Clone or copy `skills/agila-manifesto-en/` into your local `.claude/skills/agila-manifesto/` directory.
- **Other AI Agents & Toolchains**: Ingest the machine-readable specifications defined in [AGENTS.md](AGENTS.md) and [llms.txt](llms.txt).
- **Structured Schema**: Load [canon/manifesto.eo.yaml](canon/manifesto.eo.yaml) for direct programmatic access to all principles, bases, and signals.

### Non-Negotiable Agent Boundaries
1. **Read, Analyze, Cite, Propose**: Agents are authorized to inspect codebases, analyze communication graphs, cite principles by ID (`P01`–`P10`), and propose refactorings.
2. **Zero Modification Authority**: Machines cannot modify and never modify the canon, nor approve changes to the canon.
3. **Mandatory Human Sponsorship**: All agent-generated suggestions must be submitted as proposals tagged with an explicit human sponsor (`Human-owner: @username`).
4. **Lenses, Never Dogma**: Agents must never evaluate human performance, enforce compliance metrics, or score developer output against these principles.

For full agent operational protocols, see [docs/guides/agent-guide.md](docs/guides/agent-guide.md).

---

## 9. Governance

The Agila Manifesto implements a three-tier governance model to balance canonical integrity with open community participation:

| Tier | Scope | Protection Level | Authorized Actors | Approval Criteria | Deliberation SLA |
|---|---|---|---|---|---|
| **Tier 1: Fundamento** | `canon/` | **High ("Jealous")** | Humans only | $\ge 2$ human stewards | Minimum 14 calendar days |
| **Tier 2: Tradukoj** | `skills/`, `i18n/` | **Medium** | Language maintainers | Maintainer + 1 native reviewer | Standard PR cycle |
| **Tier 3: Uzado** | `uzado/` | **Low (Open)** | Any contributor | 1 maintainer or peer review | Rapid review |

### Canon Evolution Rules
Modifications to the canon adhere to strict Semantic Versioning (`vMAJOR.MINOR.PATCH`):
- **MAJOR**: Adding, deleting, or reversing the fundamental semantic meaning of a principle.
- **MINOR**: Altering a principle's theoretical base (`Bazo`), observable signal (`Signalo`), or canonical preamble/declaration.
- **PATCH**: Wording improvements, orthographic adjustments, or typographical corrections in the Esperanto text.

For full governance procedures and single-steward fallback rules, see [GOVERNANCE.md](GOVERNANCE.md).

---

## 10. Languages & Translation Drift

Translations are maintained by the global open-source community. Automated CI workflows monitor the canonical SHA-256 hash to immediately flag any language that experiences translation drift.

<!-- START_TRANSLATION_TABLE -->
| Lang | Language | Status | Canon Ver | Canon SHA-256 Match | Translators / Reviewers | Skill File |
|---|---|---|---|---|---|---|
| `en` | English | `draft` | 3.1 | `44dd1dc96687` (Match) | AI Agent (Draft), @willkwolf | [`skills/agila-manifesto-en/SKILL.md`](skills/agila-manifesto-en/SKILL.md) |
| `eo` | Esperanto | `reviewed` | 3.1 | `44dd1dc96687` (Match) | canon, @willkwolf | [`skills/agila-manifesto-eo/SKILL.md`](skills/agila-manifesto-eo/SKILL.md) |
| `es` | Español | `draft` | 3.1 | `44dd1dc96687` (Match) | AI Agent (Borrador), @willkwolf | [`skills/agila-manifesto-es/SKILL.md`](skills/agila-manifesto-es/SKILL.md) |
<!-- END_TRANSLATION_TABLE -->

### Adding a New Language
To contribute a new translation:
1. Review the translation guidelines and copy `i18n/_template/SKILL.template.md` to `skills/agila-manifesto-<lang>/SKILL.md`.
2. Translate all 10 principles preserving canonical IDs `P01` through `P10` and include the mandatory derivative disclaimer.
3. Open an issue using the [New Translation Issue Template](.github/ISSUE_TEMPLATE/03_nova_traduko.yml).
4. See [i18n/STATUS.md](i18n/STATUS.md) for the active list of 10 priority sought-after languages.

---

## 11. How to Contribute

We welcome contributions across four distinct avenues:

1. **Propose a Canon Change**: Submit an RFC issue using [Canon Proposal Template](.github/ISSUE_TEMPLATE/01_canon_propono.yml). Must include `Bazo`, `Signalo`, address counterexamples, and undergo at least 14 days of public discussion.
2. **Submit a Counterexample**: *"A counterexample is a gift."* If you discover a context where a principle fails or produces harmful outcomes, open a [Counterexample Issue](.github/ISSUE_TEMPLATE/02_kontrauekzemplo.yml).
3. **Contribute Translations**: Help maintain or translate new languages using `i18n/_template/`.
4. **Contribute to Uzado**: Share practical patterns, real-world case studies, or anti-patterns in the [uzado/](uzado/README.md) directory.

All contributors must abide by our [Code of Conduct](CODE_OF_CONDUCT.md). Detailed contribution workflows are documented in [CONTRIBUTING.md](CONTRIBUTING.md).

---

## 12. Versioning, Citation & License

### Versioning
This repository publishes **Agila Manifesto Version 3.1** (`v3.1.0`). Any release altering canonical principles or documentation follows SemVer conventions documented in [CHANGELOG.md](CHANGELOG.md).

### Citation
If you cite the Agila Manifesto in academic literature, industry whitepapers, or technical presentations, please consult [CITATION.cff](CITATION.cff) for complete bibliographic metadata:
```bibtex
@misc{agila_manifesto_2026,
  title        = {Agila Manifesto: Socio-technical Foundations for Software Architecture},
  author       = {Wolf, Will and Contributors},
  year         = {2026},
  version      = {3.1.0},
  url          = {https://github.com/willkwolf/agila-manifesto}
}
```

### License
This project operates under a dual-licensing scheme detailed in [LICENSE](LICENSE):
- **Documentation, Canon & Content**: Licensed under the [Creative Commons Attribution 4.0 International (CC BY 4.0)](LICENSE) license.
- **Automation Scripts & Code**: Licensed under the [MIT License](LICENSE).

---

## 13. FAQ

### Does this replace the 2001 Agile Manifesto?
**No.** The Agila Manifesto does not purport to be an official replacement or regulatory update to the original 2001 Agile Manifesto. Rather, it is an independent evolutionary proposal that builds upon 25 years of empirical progress in distributed computing, team topologies, systems thinking, and artificial intelligence.

### Why is the canon written in Esperanto?
Esperanto was created deliberately as a neutral international auxiliary language. Having an invariant canonical version in Esperanto guarantees that no single linguistic culture dominates the manifesto's evolution, ensures that translations are treated with equal gravity, and requires deliberate, conscious consensus for any structural change.

### Can an AI agent modify the manifesto?
**Never.** Autonomous AI agents are valuable partners for reading, parsing, indexing, and identifying potential architectural anti-patterns, but they cannot approve or merge changes into the canon. Every canonical change requires human sponsorship (`Human-owner: @username`) and approval by at least two human stewards.

### Do we have to adopt all ten principles?
**No.** The Agila Manifesto is deliberately non-dogmatic. The ten principles represent observable socio-technical laws and design tendencies, not a checklist or compliance audit. Teams and organizations should use them as diagnostic lenses to identify where structural misalignment is creating friction.
