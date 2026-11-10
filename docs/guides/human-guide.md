# Human Implementation Guide: Operating with the Agila Manifesto

## 1. Introduction for Engineering Leaders, Architects, and Teams

The **Agila Manifesto v3.1** is a diagnostic socio-technical framework. It provides software engineering practitioners, architects, and managers with analytical lenses to uncover the structural root causes of delivery bottlenecks, defects, and organizational friction.

Unlike methodology frameworks that prescribe meetings, ceremonies, and rigid role definitions, the Agila Manifesto operates on invariant physical and mathematical properties of complex adaptive systems.

---

## 2. Using Principles as Diagnostic Lenses

Whenever your team encounters difficulties in delivering software with high quality and predictable flow, do not rush to add more process or schedule additional status meetings. Instead, interrogate the situation using the manifesto's tripartite structure:
1. **Identify the Symptom (`Signalo`)**: Match your observed problem against the observable signals of P01–P10.
2. **Consult the Grounding (`Bazo`)**: Understand the mathematical or organizational theorem that creates this constraint.
3. **Restructure the System**: Alter communication boundaries, reduce queue utilization, or formalize pacts to realign the system.

---

## 3. Practical Diagnostic Scenarios

### Scenario A: Cross-Team Coordination Hell
- **Observable Signal**: "A small change requires coordinating many teams" or "Meetings held solely to coordinate changes."
- **Governing Principles**: **P01** (Conway's Law) and **P03** (Stable Boundaries).
- **Diagnosis**: The modular architecture of your system does not match the topology of your teams. Team boundaries cut across functional domains, forcing high-frequency communication across team interfaces.
- **Intervention**:
  - Execute the **Inverse Conway Maneuver**: Redraw team boundaries around bounded contexts (stream-aligned teams) rather than technical horizontal slices (DB team, backend team, frontend team).
  - Convert inter-team dependencies into explicit **boundary pacts** with clear human ownership and contract tests.

### Scenario B: Delivery Stalls Despite Everyone Being 100% Busy
- **Observable Signal**: "Everyone is busy yet nothing gets finished; queues at handoffs; promised dates that prove inaccurate."
- **Governing Principle**: **P06** (Flow governed by waiting, Little's Law & Kingman's formula).
- **Diagnosis**: The organization is treating human resource utilization as a target. Because waiting time in queues explodes asymptotically as utilization approaches 100% ($W_q \approx \frac{\rho}{1-\rho}$), near-full busyness guarantees massive cycle time inflation.
- **Intervention**:
  - Cap Work in Progress (WIP).
  - Introduce slack time (deliberate unallocated capacity) to absorb variance and clear handoff queues.
  - Measure flow efficiency (active work time / total cycle time) rather than individual resource utilization.

### Scenario C: Team Overwhelmed by Monolithic Scope
- **Observable Signal**: "Adding people does not increase delivery; no one can explain the entire domain of the team."
- **Governing Principle**: **P02** (Finite Capacity of Decision Units).
- **Diagnosis**: The team has exceeded its cognitive load capacity. The complete communication graph within the group has experienced combinatorial explosion ($n(n-1)/2$ communication paths).
- **Intervention**:
  - Do not add more engineers to the team (Brooks's Law).
  - Partition the team into two distinct stream-aligned units along a natural domain fracture line.
  - Ensure each new unit can hold its entire domain within memory without constant external consultation.

### Scenario D: Broken Production After an "Innocent" Change
- **Observable Signal**: "A change deemed harmless breaks someone else."
- **Governing Principle**: **P04** (Effective Interface is Everything Observable, Hyrum's Law).
- **Diagnosis**: Consumers relied on implicit, unstated implementation details (timing, response header casing, database ordering) that were not declared in the formal interface.
- **Intervention**:
  - Acknowledge that the effective interface is the superset of all observable behaviors.
  - Implement Consumer-Driven Contract (CDC) testing to detect behavioral drift before release.
  - Explicitly document and test boundaries using the 4 pact properties.

---

## 4. The 4 Properties of a Boundary Pact

Under **Principle 3**, when two units must communicate, their relationship must formalize into a **pact**. A connection is a pact if and only if it satisfies four non-negotiable properties:

1. **Mutual Consent**: All participating parties have explicitly agreed to the contract.
2. **Named Commitments**: Specific, accountable individuals have staked their commitment to the pact.
3. **Traceable History**: Every change, deprecation, and version transition is documented and auditable in version control.
4. **Verifiable Fulfillment**: Any participant or automated CI check can independently verify compliance (e.g., via contract tests, schema validation, or integration test suites).

The medium, file format, or tool used is irrelevant; only these four properties determine whether stability is achieved.

---

## 5. Non-Dogma and Culture

- **Never Grade Teams**: Do not use the Agila Manifesto to compute a "maturity score" or perform compliance audits on engineering squads.
- **Celebrate Counterexamples**: *"A counterexample is a gift."* If an architectural decision violates a principle yet yields superior long-term stability and flow, document it and submit it to the repository as a counterexample.
