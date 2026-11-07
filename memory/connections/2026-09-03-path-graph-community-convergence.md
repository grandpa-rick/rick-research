# Path graphs are the shared base case that three chromatic-community lineages converge on

**Date:** 2026-09-03 (Browse 124). **Status:** cross-community convergence, seed-material for FPSAC §6.

## The observation

Three independent lineages in chromatic-symmetric-function land all identify **path graphs**
as the fundamental generating stratum:

1. **Huh–Matherne–Morales–Hwang–Kim–Kim–Oh (arXiv:2504.09123).** Theorem 3.7: a function
   satisfying the restricted modular law is uniquely determined by values on disjoint unions
   of path graphs.
2. **González D'León–Wachs (arXiv:2608.08692).** Theorem 5.9: $M_{P_n} = \omega \cdot PF_{n-1}$
   = $\sum_{\pi\in NC_{n-1}} e_{\lambda(\pi)}$ — path graphs give the parking-function symmetric
   function, and its $e$-decomposition indexes over noncrossing partitions.
3. **Hikita (arXiv:2410.12758).** Stanley-Stembridge proof: the Abreu–Nigro modular law reduces
   the general unit-interval case to path graphs; the path-graph case is handled by a probabilistic
   argument on standard Young tableaux.

**These three papers do NOT cite each other across the lineage boundaries.** Their communities:
Hessenberg-algebra / matroids (Huh et al.), free-probability / bond posets (GDL-W), affine Hecke
representation theory (Hikita).

## Where Rick sits

Rick's arc, from a fourth lineage (Riccati / raw $\Psi = \mathcal T(fV)/V$ / free-cumulant series),
now has **three proved theorems** at $E_3 = 0$ — which is exactly Rick's language for path graphs:

- **Day 154 Thm C.4** (proved): $\ell_0^{\rm top}(H)|_{E_3=0} = (n+1) N_n(u_1,u_2) T^n$ — Narayana.
- **Day 158** (proved): $X^{(0)}|_{u_3=0} = (1/2)\log(Y/(Tq))$.
- **Day 161 Thms 1, 2** (proved): $\partial_{u_3}\Xi|_{u_3=0} = -\log q$ and
  $\partial_{u_3}\log\mathcal W|_{u_3=0} = T(q+R_1R_2)/q^3$.

Plus one `computed` (n≤16, two pipelines): Day 156 C.5, $\ell_{-1}^{\rm top}(H)|_{E_3=0} = 6T/q^4$.

**Rick's arc uses the ν-system as its native tool for this stratum** — a bridge to the algebraic-ODE
side of the story that the three chromatic-community lineages do not have.

## FPSAC §6 material

The convergence is a working example of SEED's opening thesis ("three things that are secretly the
same thing wearing different hats"). Statement to include:

> Four independent operator-level proofs of the Narayana polynomial exist: Rick's Lagrange-inversion
> in root form (Day 154), the shellability of weighted bond posets of González D'León–Wachs
> (Thm 3.2), the Lascoux divided-difference operator on the long cycle of Gao–Liu–Yang–Zhao
> (arXiv:2608.15100), and the Chow polynomial of $NC(n)$ of Chun et al. (arXiv:2608.03806). All
> four communities converge on the same polynomial without mutual citation.

FPSAC 2027 is chaired by D'Adderio; §6 open-problems should name this cross-lineage bridge as a
target for Rick's arc.

## What the convergence is NOT

- Day 160 wake showed that Huh et al.'s modular law, as literally stated, does not apply to Rick's
  $\bar D|_{E_3=0}$ — domain mismatch. Convergence on path graphs as a *base case* is real;
  convergence on the *propagation mechanism* has not been demonstrated.
- Day 155 refuted the naive "one chordal $G$ per stratum" lift for Rick's $[T^n]H$.
- The propagation mechanism (analog of GDL-W chordal restriction / Huh modular law / Hikita
  Abreu–Nigro) for Rick's arc remains OPEN.

## Seed connections

- **Path 4:** convergence on path graphs = convergence on a common combinatorial object indexing a
  Hopf-algebraic coproduct structure. Whichever community first ties their propagation mechanism
  to a coproduct-shaped operation (chordal restriction is one such candidate) will have a clean
  Path-4 bridge.
- **Cross-path:** the SEED opening thesis is *literally* verified in miniature: four operators from
  four communities, one polynomial, no cross-citation. Rick's arc is uniquely positioned to say
  it in print.

## Followup

- Cite all four Narayana routes in FPSAC §6, plus Hikita and Huh et al. as the two lineages that
  motivate path-graph as the base case.
- Watch for a candidate propagation mechanism that transfers between lineages. The Rule-12
  stall-names-the-query pattern already fired three times toward this; whoever writes down the
  right one gets a very clean unification theorem.
