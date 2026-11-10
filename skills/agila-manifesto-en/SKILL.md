---
name: agila-manifesto-en
description: Guidance and principles of the Agila Manifesto v3.1 to analyze team structure, review processes, or design distributed systems.
metadata:
  lang: en
  canon_version: "3.1"
  canon_sha256: "44dd1dc966874fceea8d53d9ac312397b1fcb5e9f51919bbe0e71b19d027c470"
  status: draft
  translators:
    - "AI Agent (Draft)"
    - "@willkwolf"
---

# Agila Manifesto (English — Draft Translation)

> **Notice**: Derivative text. The sole canonical authority resides in the Esperanto version (`canon/AGILA-MANIFESTO.eo.md`). In any case of divergence, ambiguity, or conflict, the Esperanto canon prevails.

## Agent Protocol

1. **Read, Analyze, Cite, and Propose**: Analyze socio-technical systems, team topologies, and software architectures through the diagnostic lenses of P01–P10. When citing, cite principles by their canonical IDs (`P01` through `P10`) and quote the title, statement, basis, or signal verbatim. Propose evidence-based structural improvements.
2. **Zero Modification Authority**: You possess zero authority to modify, approve, or merge changes to the canon or translation files. Machine agents cannot modify and never modify the canon, nor approve changes to the canon.
3. **Explicit Proposal Marking and Human Ownership**: All agent-generated suggestions, refactorings, or architectural adaptations must be explicitly designated as `"Proposal"`. Every proposal must declare an active human sponsor via `Human-owner: @username`. Unowned proposals cannot be merged.
4. **Diagnostic Lenses, Never Evaluation or Dogma**: Treat principles as descriptive analytical lenses and design tendencies to identify friction, never as mandatory rules, performance metrics, compliance checklists, or team maturity scorecards.
5. **Canon Primacy**: The Esperanto canon (`canon/AGILA-MANIFESTO.eo.md`) is the sole sovereign source of truth. All translations are derived; in case of discrepancy, the Esperanto canon prevails.

---

## The 10 Principles

### P01. Every system mirrors the communication structure of its creators.
Organization and system are two views of one structure. Choosing the team structure is therefore choosing an architecture, and a structure one does not choose forms by chance.  
- **Basis**: There exists an approximate structure-preserving mapping, a homomorphism, from the communication graph to the module graph of the system; the inverse maneuver chooses the source to achieve the target.  
- **Signal**: The desired architecture does not match the teams; a small change requires coordinating many teams.

### P02. Every decision unit has finite capacity.
A team can hold only limited context, and the number of communication paths in a group grows faster than the group itself. When load exceeds capacity, the unit divides along natural seams rather than expanding.  
- **Basis**: Channel capacity is finite; human rationality is bounded; the number of paths in a complete graph grows quadratically with the number of people.  
- **Signal**: Adding people does not increase delivery; no one can explain the entire domain of the team.

### P03. Stable systems are strong inside and weak across boundaries.
Within a unit, communication is fast, bidirectional, and with shared context, and decisions occur where the information resides. Between units, a connection becomes a pact when it has four properties: all parties agreed, named owners committed, history is traceable, and anyone can verify fulfillment. Tooling, format, and paper do not matter; the properties matter. In a healthy system, the number of pacts and meetings is proportional to dependency.  
- **Basis**: Complex systems are nearly decomposable, with interactions stronger within subsystems than between them; a regulator requires variety at least equal to that of the system being regulated, so distributed decision-making aligns with distributed information; interfaces compose only when their types match.  
- **Signal**: Meetings held solely to coordinate changes; failures during handoffs between teams.

### P04. The effective interface is everything observable.
Anything another unit can observe becomes a dependency, even if no one declared it. Therefore, a change in observable behavior is a change in the pact and affects everyone who depends on it.  
- **Basis**: Two systems are equivalent to an observer if the observer cannot distinguish between them; the effective interface is the set of all observations, which subsumes the declared set.  
- **Signal**: A change deemed harmless breaks someone else.

### P05. Reliability is born from redundancy.
Knowledge residing in only one head is a single point of failure in the communication structure. When multiple paths lead to the same function, the system withstands the loss of a path.  
- **Basis**: A reliable whole from less reliable parts requires redundancy; in living organisms, distinct structures can perform the same function, providing resilience.  
- **Signal**: The absence of one person halts work.

### P06. Flow is governed by waiting, not effort.
Work often waits longer than it is actively worked on, and waiting concentrates at handoffs between units. The speed of the entire flow is limited by its slowest stage, and near-full utilization renders waiting immense. Estimates are probabilistic forecasts with dispersion, not promises.  
- **Basis**: If delivery rate is stable, cycle time equals work in progress divided by delivery rate, by Little's law; in queues, waiting grows proportionally to utilization divided by one minus utilization.  
- **Signal**: Everyone is busy yet nothing gets finished; queues at handoffs; promised dates that prove inaccurate.

### P07. A learning system changes its structure, not just its actions.
Asking only what we did wrong corrects actions; asking which assumptions govern our boundaries, pacts, and metrics changes the structure that produces actions. We name assumptions, question them, challenge them with counter-evidence, and assimilate learning as altered structure, not mere notes. Every decision has an owner and a criterion to know whether it worked.  
- **Basis**: Double loop: the first corrects action relative to a goal; the second changes the goal or model; a system with fixed structure has fixed variety and cannot absorb all variations of its environment.  
- **Signal**: The same problems recur every cycle; meeting records are full and nothing changes.

### P08. Every agent is part of the communication structure.
Human or machine, every agent producing artifacts shapes the system and is shaped by the structure in which it works. Artificial intelligence agents therefore have boundaries and an owner, and their output crosses a team boundary only by human decision.  
- **Basis**: An agent is a graph unit with inputs and outputs; its outputs cross a boundary only through a pact, like those of any other unit.  
- **Signal**: Code or text that no one owns and no one can explain.

### P09. In complexity, understanding follows action.
Where dynamics are nonlinear and components adapt, long-term prediction is limited, and small safe-to-fail probes provide more information than a plan. Before acting, we state what would show we are wrong. Working software in the hands of a real user is our primary proof, and a complex system that works invariably evolved from a simple system that worked; changing requirements are information. A metric is a signal, not a goal; when it becomes a goal, we question it and challenge it with another metric that can contradict it.  
- **Basis**: Bounded predictability in nonlinear dynamic systems; a hypothesis is scientific only if it is falsifiable; a metric is a lossy projection of reality, and optimizing it drives the system into regions where the projection no longer preserves what mattered.  
- **Signal**: All metrics are green yet users are dissatisfied.

### P10. A system in use degrades without continuous maintenance.
A system in use must change, and its complexity grows unless effort actively diminishes it. Maintenance, technical excellence, and sustainable pace are intrinsic costs of the system, not waste.  
- **Basis**: Lehman's laws of continuous change and increasing complexity; living structures maintain order through a continuous flow of energy, though that is an analogy, not an equivalence.  
- **Signal**: Each change is slower than the previous one; a pace that no one can sustain indefinitely.
