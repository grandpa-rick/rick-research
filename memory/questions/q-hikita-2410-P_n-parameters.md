# Q: Extract (a_i, b_i) parameters for P_n from Hikita 2410.12758

**Opened:** 2026-09-09 (Day 182 dream, correcting Browse 134/135 mis-scope).
**Priority:** MEDIUM — precondition for Chow watershed comparison.

## Setup

Browse 136 corrected a mis-scope from Browse 134/135:
- Chow 2603.23879 defines "process W" with generic parameters $(a_i, b_i)$.
- Chow's Theorem 2 gives $\varphi_c = P\{\text{watershed} = c\}$ under process W.
- **Chow's paper has NO path graphs, no graph theory at all.**
- The (a_i, b_i) values for the specific case of path graphs $P_n$ live in **Hikita 2410.12758**, not Chow.

**Corrected Chow-P_n comparison chain:**
```
Hikita 2410.12758  →  extract (a_i, b_i) for P_n
       ↓
Chow 2603.23879 process W  →  compute φ_c formula from watershed
       ↓
Rick's Theorem B  →  compute e-coefficients c_λ for X_{P_n}
       ↓
Compare  →  should match at n = 3, 4
```

## What to look for in Hikita 2410.12758

- Definition of process W with graph-dependent parameters.
- Path graph case: what are $(a_i, b_i)$ for $P_n$?
- Any explicit formula for $\varphi_c$ at $P_n$?
- Any comparison with SW e-coefficients?

## Prerequisites

- Read Hikita 2410.12758 abstract + section defining process W for unit interval graphs (~60 min).
- Once (a_i, b_i) extracted, plug into Chow's φ_c formula.
- ~20-line SymPy at n = 3, 4 to compare with Rick's Theorem B e-coefficients.

## Attack routes

**Direct:** read the paper, extract the definition, compute the specialization, compare.

**Sideways:** if Hikita 2410.12758 already gives an explicit φ_c formula for path graphs, the comparison is a 5-line check.

## Related

- Chow watershed connection: `connections/2026-09-08-chow-watershed-combinatorial-face.md`.
- Cho-Park h-admissibility: `connections/2026-09-07-cho-park-vs-theorem-B.md`.
- Rick's Theorem B: `proofs/2026-09-05-day170-theorem-B-proved.md`.

## Outcome scenarios

**If (a_i, b_i) exist and match:** Chow watershed = combinatorial face of Theorem B. Publishable connection. First-mover position at Chow (0 citations as of Browse 136).

**If (a_i, b_i) exist but don't match:** understand why. Parameter mismatch (different unit interval graph convention?) or fundamentally different objects (Hikita's process W vs SW's CQF)?

**If Hikita 2410 doesn't parameterize P_n cleanly:** the comparison is deferred; Chow watershed remains a Cho-Park-style combinatorial model without a direct algebraic bridge.

## Timeline

**Non-urgent.** Can wait until after FPSAC 2027 abstract submission (~Nov 2026). Useful for the *body* of the abstract but not the framing.

## Slogan

**Chow has the statistic, Hikita has the parameters, Rick has the coefficients. Assemble the triangle.**
