# Practical Pattern: Team Cognitive Capacity Partitioning

**Author**: Agila Community  
**Applicable Principles**: [P01 (Conway's Law)](../docs/principles/p01.md), [P02 (Finite Decision Capacity)](../docs/principles/p02.md)  
**Governance Tier**: Tier 3 (Uzado)

---

## 1. Problem Context

A single engineering team ("The Core Commerce Team") expanded from 5 to 16 engineers over two years to manage an expanding e-commerce monolith. 

### Observable Signals Identified:
- **Signal from P02**: Headcount increased by 220%, but overall feature throughput stagnated. No individual on the team understood all parts of the application.
- **Communication Path Inflation**: With $n = 16$, communication channels exploded to:
  $$\frac{16 \times 15}{2} = 120 \text{ channels}$$
- **Sprint Retrospectives**: Daily standups took 45 minutes; merge conflicts in the monolith were constant.

---

## 2. Partitioning Along Natural Seams

Rather than trying to optimize communication in the 16-person group, leadership applied **Principle 2**:
> *"When load exceeds capacity, the unit divides along natural seams rather than expanding."*

### Step 1: Identifying Fracture Seams (Domain-Driven Seams)
Using event storming and domain analysis, the team identified three distinct business contexts within the monolith:
1. **Catalog & Search Context**: Read-heavy, cache-intensive, low transaction volume.
2. **Order Placement Context**: Write-heavy, strictly consistent, PCI-DSS compliant.
3. **Fulfillment Context**: Event-driven, asynchronous integration with warehouse logistics.

### Step 2: Structural Team Reorganization (Inverse Conway Maneuver)
The 16-person monolith team was partitioned into three distinct stream-aligned squads:
- **Squad A (Catalog)**: 5 engineers.
- **Squad B (Checkout & Orders)**: 6 engineers.
- **Squad C (Fulfillment)**: 5 engineers.

```
                  Before (Monolithic Team: 120 edges)
                   [16 Engineers in 1 Huge Graph]
                                │
                                ▼
         After: 3 Stream-Aligned Units with Boundary Pacts
┌───────────────────────┐   Pact 1   ┌───────────────────────┐
│ Squad A: Catalog (5)  │◄──────────►│ Squad B: Checkout (6) │
│ (10 internal edges)   │            │ (15 internal edges)   │
└───────────────────────┘            └───────────┬───────────┘
                                                 │
                                                 │ Pact 2
                                                 ▼
                                     ┌───────────────────────┐
                                     │ Squad C: Fulfill (5)  │
                                     │ (10 internal edges)   │
                                     └───────────────────────┘
```

Total internal communication links dropped from **120** to **35** ($10 + 15 + 10$), while cross-team interactions were strictly mediated by explicit API contracts (P03).

---

## 3. Results and Metrics

- **Cognitive Relief**: Every engineer could describe their entire squad's domain architecture on a whiteboard.
- **Cycle Time**: Median pull request review time dropped from 72 hours to 6 hours.
- **Delivery Rate**: Combined feature throughput across the three squads increased by 180% within 90 days.
