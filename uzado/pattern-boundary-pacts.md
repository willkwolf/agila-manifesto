# Practical Pattern: Implementing Boundary Pacts Across Microservice Squads

**Author**: Agila Community  
**Applicable Principles**: [P03 (Boundary Pacts)](../docs/principles/p03.md), [P04 (Effective Interface)](../docs/principles/p04.md)  
**Governance Tier**: Tier 3 (Uzado)

---

## 1. Problem Context

In distributed microservice architectures, teams frequently struggle with two opposing failure modes:
1. **Coupling via Coordinating Meetings**: Squads spend excessive hours in weekly sync meetings attempting to coordinate API schema changes.
2. **Coupling via Production Surprises**: Squads deploy "harmless" internal changes that break downstream consumers unexpectedly (Principle 4 / Hyrum's Law).

---

## 2. The Boundary Pact Pattern

Rather than scheduling more coordination meetings, teams implement an explicit **Boundary Pact** exhibiting the four properties defined in Principle 3:

```
┌───────────────────────────┐                     ┌───────────────────────────┐
│     Provider Squad        │                     │     Consumer Squad        │
│  (e.g., Billing Service)  │                     │  (e.g., Checkout Service) │
└─────────────┬─────────────┘                     └─────────────┬─────────────┘
              │                                                 │
              │         1. Mutual Consent & Negotiation         │
              │◄───────────────────────────────────────────────►│
              │                                                 │
              │         2. Named Owner Commitment in Git        │
              │         (@billing-lead & @checkout-lead)        │
              │                                                 │
              │         3. Traceable Contract in Version Control│
              ├─────────────────────────────────────────────────┤
              │         pacts/checkout-billing-contract.json    │
              │                                                 │
              │         4. Verifiable Fulfillment in CI         │
              │◄───────────────────────────────────────────────►│
              │   (Provider verification tests in CI build)     │
```

### The 4 Invariants in Practice:

1. **Mutual Consent**:
   - The consumer writes a Consumer-Driven Contract (CDC) specifying only the fields, HTTP methods, headers, and status codes they actively consume.
   - The provider approves the pull request containing this contract.

2. **Named Commitments**:
   - The contract metadata specifies human maintainers:
     ```yaml
     contract_id: "checkout-v1-to-billing-v2"
     consumer_owner: "@sarah-chen"
     provider_owner: "@marcus-vance"
     last_verified: "2026-11-10"
     ```

3. **Traceable History**:
   - Contracts are committed into version control under a dedicated directory (`contracts/` or a contract broker like Pact Broker).
   - Any deprecation or field addition follows a documented SemVer lifecycle.

4. **Verifiable Fulfillment**:
   - Provider CI runs automated contract verification against the consumer's published pacts on every commit.
   - If a provider's proposed change would break an observable field in the pact, the provider's build fails before merging.

---

## 3. Observed Outcomes

- **Meeting Reduction**: Weekly inter-team API coordination meetings decreased from 3 hours/week to near zero.
- **Breaking Changes Eliminated**: Zero unanticipated boundary breakages in production over 12 months.
- **Autonomous Deployments**: Providers deploy continuously without notifying consumers in advance, secure in the knowledge that CI verifies all pacts.
