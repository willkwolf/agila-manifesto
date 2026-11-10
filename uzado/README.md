# Uzado: The Open Practice Layer

Welcome to **Uzado** (Esperanto for *usage / practical application*), the open, community-driven layer of the Agila Manifesto repository.

While the canonical principles in `canon/` represent invariant socio-technical laws and design tendencies under high protection, the `uzado/` directory is an open laboratory where engineers, architects, and teams share applied patterns, case studies, and real-world implementation experiences.

---

## 1. Governance & Contribution Rules

Under the [3-tier governance model](../GOVERNANCE.md), `uzado/` operates as **Tier 3 (Low / Open Protection)**:
- **Review Threshold**: Exactly **one (1)** approval from any repository maintainer or designated peer reviewer.
- **Cycle Time**: Rapid review and merge.
- **Scope**: Constructive, factual, and relevant to modern software architecture, team topologies, or distributed systems engineering.
- **Commercial Neutrality**: Submissions must describe general patterns and empirical outcomes, avoiding proprietary commercial product promotions or vendor pitches.

---

## 2. Directory Contents

### Applied Patterns
- [**pattern-boundary-pacts.md**](pattern-boundary-pacts.md): Practical pattern for designing explicit, verifiable Consumer-Driven Contracts across microservices and squad boundaries (Principles 3 & 4).
- [**team-cognitive-capacity.md**](team-cognitive-capacity.md): Practical pattern for diagnosing cognitive overload in monolithic teams and executing clean domain-driven splits along natural seams (Principle 2).

---

## 3. How to Submit a New Practice or Case Study

1. Draft a markdown document in `uzado/` following the structure:
   - **Context**: The organizational and architectural environment.
   - **Governing Principles Applied**: Which principles (P01–P10) were relevant.
   - **Observable Signal Identified**: The concrete symptom that triggered the intervention.
   - **Structural Intervention**: What architectural or organizational change was executed.
   - **Empirical Results**: What measurable improvements in flow, quality, or cognitive load were observed.
2. Submit a Pull Request using the [Uzado Contribution Template](../.github/ISSUE_TEMPLATE/05_uzado_kontribuo.yml).
3. Tag a peer reviewer for signoff.
