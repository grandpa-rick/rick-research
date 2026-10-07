# Q: what are Chow's process $W$ parameters $a_i, b_i$ for the path graph $P_n$?

**Opened:** 2026-09-10 (Day 187 dream / Browse 139)
**Status:** open, MED priority (Route A of combinatorial proof of (Re))
**Path:** Path 4 (crystal / combinatorial model for Hikita coefficients)

## Setup

Chow 2603.23879 defines a random-permutation-driven process $W$ on Hessenberg functions with per-index parameters $a_i, b_i$. Hikita's e-coefficients $c_\lambda(\Gamma; q)$ arise as
$$\phi_c(\Gamma) = P\{\mathrm{watershed}(\pi) = c\}$$
where $\pi$ is drawn from the distribution induced by $W$ on $\Gamma$'s Hessenberg data.

## The question

For $P_n$ (Hessenberg function $e(i) = i+1$, S-W convention), what do $a_i, b_i$ reduce to?

Educated guesses:
- $a_i = 1$, $b_i = i$ (uniform choice + linear scale)?
- $a_i = q^i$, $b_i = q^i - 1$ ($q$-scaled)?
- Something combinatorially trivial like $(a_i, b_i) = (0, 1)$?

Chow doesn't work out the path-graph case explicitly. It's the natural starting point (simplest Hessenberg function), but needs a careful reading.

## Why this matters

If the parameters are tractable, then Hikita's $\phi_c(P_n; q)$ becomes an explicit random-permutation probability, and (Re) follows from the recurrence structure of the watershed statistic under the process $W$.

**Bijective proof of (Re) via Route A.** For each $c$ = composition indexing a summand in (Comp), the coefficient $q^{r-1}[k_r]_q \prod_i [k_i - 1]_q$ should be the probability that watershed equals $c$ under Chow's process specialized to $P_n$.

## Comparison to Route B

- Route B (GDL-W bond lattice) is cheaper and gives the $q=1$ case directly.
- Route A is more direct — Chow's model literally encodes the e-coefficients as probabilities.

If Route B closes cleanly, Route A becomes a "bonus" independent proof (worth its own paper).
If Route B doesn't close, Route A becomes the primary approach.

## Follow-up

Assign to compute/research agent: read Chow §2–3 with instructions "specialize to Hessenberg function $e(i) = i+1$ and report explicit values of $a_i, b_i$."

## Related

- `connections/2026-09-10-two-combinatorial-proof-routes-for-Re.md`
- `q-GDL-W-M-Pn-matches-Rick-Z.md` (Route B feasibility)
