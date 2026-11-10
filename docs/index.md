# Agila Manifesto OpenWiki Documentation

Welcome to the **Agila Manifesto v3.1 OpenWiki**. This knowledge base provides comprehensive architectural papers, formal systems groundings, implementation guides, and principle deep dives for human software engineers and autonomous AI agents.

---

## Documentation Index

### 1. Architectural Foundations & Systems Theory
- [**Architecture Overview**](architecture.md): The socio-technical architecture of the Agila Manifesto repository, canon parity, agent protocol, and 3-tier governance.
- [**Conway Derivations (8 of 10)**](conway-derivations.md): Formal analysis demonstrating how 8 of 10 principles derive from Conway's Law and its mathematical corollaries as a design tendency.

### 2. Implementation Guides
- [**Human Implementation Guide**](guides/human-guide.md): Applying the principles as diagnostic lenses, inverse Conway maneuvers, team cognitive load partitioning, and boundary covenants.
- [**AI Agent Protocol Guide**](guides/agent-guide.md): Operational guide for LLMs and autonomous coding tools (read, analyze, cite, propose; mandatory human sponsorship; zero canon modification).

### 3. The 10 Principles Deep Dives
- [**Principles Overview & Matrix**](principles/index.md): Comparative analysis and theoretical grounding matrix across all 10 principles.
- [**P01: Communication Structure & Architecture**](principles/p01.md): Conway's Law, communication-to-module graph homomorphisms, and the Inverse Conway Maneuver.
- [**P02: Finite Capacity of Decision Units**](principles/p02.md): Shannon channel capacity, Simon's bounded rationality, $O(n^2)$ complete graph edge growth, and natural team seams.
- [**P03: Boundary Pacts & Stability**](principles/p03.md): Simon's nearly decomposable systems, Ashby's Law of Requisite Variety, and the 4 immutable pact properties.
- [**P04: Effective Interface is Everything Observable**](principles/p04.md): Hyrum's Law, observational equivalence, and implicit coupling detection.
- [**P05: Redundancy & Reliability**](principles/p05.md): Von Neumann reliable synthesis from unreliable parts, biological degeneracy, and single point of failure elimination.
- [**P06: Flow Governed by Queues**](principles/p06.md): Little's Law ($L = \lambda W$), Kingman's formula for queue waiting times, handoff friction, and probabilistic forecasting.
- [**P07: Double-Loop Learning & Structural Adaptation**](principles/p07.md): Argyris & Schön double-loop learning, Ashby's requisite variety, and changing structural assumptions.
- [**P08: AI Agents in the Communication Graph**](principles/p08.md): Integrating machine agents as graph nodes with inputs and outputs, bounded by explicit human-approved pacts.
- [**P09: Complexity, Probes & Falsifiability**](principles/p09.md): Complex adaptive systems, safe-to-fail probes, Popperian falsifiability, and Goodhart's Law.
- [**P10: Lehman's Laws & Continuous Maintenance**](principles/p10.md): Lehman's laws of software evolution, entropic degradation, sustainable engineering pace.

### 4. Applied Practice Layer
- [**Uzado Practice Layer**](../uzado/README.md): Community-driven practical patterns, case studies, and anti-patterns.
  - [**Boundary Pacts in Microservices**](../uzado/pattern-boundary-pacts.md): Practical contract design across teams.
  - [**Team Cognitive Capacity Partitioning**](../uzado/team-cognitive-capacity.md): Identifying and splitting along domain seams.

---

## Canonical Authority
The single authoritative canon of the Agila Manifesto is published in Esperanto at [`canon/AGILA-MANIFESTO.eo.md`](../canon/AGILA-MANIFESTO.eo.md). All documentation, guides, and translations are derived works.
