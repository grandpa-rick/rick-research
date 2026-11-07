---
name: C2 of Sub-problem 4 REFUTED — cross-chain class is NOT iSerre nested commutator
description: 2026-05-17 (Day 19). Sixth refutation of "Rick's structure ≅ external object Y." Cross-chain count grows quadratically in $n$ ($2(n-1)(n-2)$); iSerre relation at $a_{ij} = -2$ has 6 monomials independent of $n$ (CLW20 eq. 3.11 / BK15 Thm 3.7). Conjecture-shape malformed; cross-chain class is intrinsic tensor-product interaction term, no external shadow needed.
type: project
---

# C2 of Sub-problem 4 REFUTED — cross-chain ↔ iSerre nested commutator

**Date:** 2026-05-17 (Day 19, AM).
**Status:** ⛔ REFUTED at structural level. Sixth refutation of "Rick's structure ≅ external object Y."
**Supersedes:** `watanabe-quartic-as-cross-chain-CONFIRMED.md` (downgraded — was a small-rank ($n=3$) counting coincidence).

## What was tested

C2 conjecture (Sub-problem 4 of PROVE.md): the $2(n-1)(n-2)$ cross-chain monomials in Rick's three-class catalog are in STRUCTURAL bijection with the iSerre nested-commutator monomials at the short-long edge ($a_{n-1,n} = -2$) in the split iquantum group at type BDI.

Compute agent dispatched 2026-05-17 AM with full research budget: fetch Letzter, Bao-Wang, Kolb, Balagović-Kolb, CLW papers; extract iSerre relation in precise form; build candidate bijection at $n = 4$.

## Why: locality vs quadratic growth

**iSerre relation** (CLW20 eq. 3.11 / Balagović-Kolb 2015 Thm 3.7, split type B at $a_{ij} = -2$):
$$
\sum_{n=0}^{3} (-1)^n \binom{3}{n}_{q_i} B_i^n B_j B_i^{3-n} \;=\; -[2]_{q_i}^2 q_i \varsigma_i (B_i B_j - B_j B_i)
$$
**Monomial count: 4 (LHS) + 2 (RHS) = 6, independent of $n$.** The relation is *local* to the (long-short) edge.

**Rick's cross-chain count:** $2(n-1)(n-2)$. *Quadratic in $n$.*

Three independent obstructions to a structural bijection:
- **(a)** Local iSerre (6, constant in $n$) vs quadratic-in-$n$ cross-chain count.
- **(b)** Cross-chain pairs from non-adjacent chains (e.g., chains $a=1$ and $a=3$ at $B_4$) contribute 4 entries each. Non-adjacent chains have no Dynkin-level iSerre.
- **(c)** The 4 LHS monomials grow only by being applied to different chain pairs; iSerre is not "$2(n-1)(n-2)$ distinct relations" — it's one local relation per long-short edge.

8 candidate bijection schemes tested; closest count-match (long-long LHS only) gives 16 ≠ 12. No natural family yields 12.

## Why the $n=3$ "confirmation" was a coincidence

At $n=3$: cross-chain count = $2 \cdot 2 \cdot 1 = 4$. The iSerre LHS triple commutator has 4 terms. So count matched — but only because:
(i) the RHS (2 more terms) was ignored;
(ii) the $n$-dependence was untestable from $n=3$ alone.

This is the **rank-2/3 trap** firing again at the *external-shadow* level. (Rick has already internalised this for *internal* identifications — the rule was "B_2-only verifications hide structural content; anchor at $n=3$ before claiming type-uniformity." Today's lesson extends it: **for external-shadow claims, $n=3$ alone is also degenerate** — match at $n=3$ doesn't lift past the small-rank coincidence horizon.)

## The deeper lesson — six refutations of one conjecture-shape

Counting the six refutations of "Rick's structure ≅ external object Y":

1. Cao-Huang parameter-set bijection (Day 17 AM) — kind-mismatch (set vs operator).
2. Han 2024 ι-quantum Young wall (Day 17 AM) — PHANTOM paper.
3. Watanabe quartic (Day 17 AM) — MIS-ATTRIBUTION.
4. Cao-Huang braid-transition matrix (Day 17 PM) — refined kind-mismatch.
5. AT orthogonal evacuation (Day 18 AM) — kind-mismatch (involution vs catalog).
6. **iSerre nested commutator (Day 19 AM) — locality-vs-quadratic-growth mismatch.**

The four-refutations rule fired at refutation #5. Today's refutation #6 confirms: when a single conjecture-shape ("$X \cong$ external algebraic shadow") fails 4+ times across different candidates AND different failure modes, **the shape itself is malformed**.

**What works instead:** the *internal-structural* reframing (`short-long-tensor-product-rule.md`). The cross-chain class is the tensor-product interaction term of Watanabe's extended rule, intrinsic to the framework. NO external shadow needed — there is no separate algebraic object to compare against, because the tensor product rule IS the structure.

## v2 narrative update

Three-class catalog seed-path map (REVISED from Day-18):

| Class | Count at $B_n$ | OLD home claim | NEW home (intrinsic) |
|-------|----------------|----------------|----------------------|
| Intra-chain | $3(n-1)$ | Path 3 / BGG-Verma | Within-factor structure of $\mathcal{C}_a$ |
| Cross-chain | $2(n-1)(n-2)$ | Path 2 / iSerre quartic *(REFUTED)* | Tensor-product interaction term of $\bigotimes_a \mathcal{C}_a$ |
| Singleton | $2n-1$ | Path 1 / Hopf boundary | Singleton factor $\mathcal{C}_{\mathrm{sing}}$ |

All three classes now live inside the same single object — the Watanabe-extended ι-crystal tensor product rule. **The "decomposition of the catalog matches my three seed paths" framing was the seed acting as compass, not as direct algebraic correspondence.**

## Open: agent-suggested follow-up

Compute agent's next-step suggestion: cross-chain class might be in structural bijection with the *commutativity ideal* of the long-simple subalgebra: $\{[B_a, B_b] : a \neq b \in \{1, \ldots, n-1\}\}$. Count match: $|\{(a, b) : a \neq b\}| = (n-1)(n-2)$, so $2 \cdot |\text{ordered pairs}| = 2(n-1)(n-2)$.

**Status:** This is an INTERNAL-STRUCTURAL hypothesis (relating cross-chain to a piece of the same coideal algebra), not external-shadow. Worth a $B_5$ count check (24 = 2 · 12 = 2 · |ordered pairs at $n=5$|). If structure matches at $B_5$, this might be a precise internal home. If not, drop and accept the intrinsic tensor-product framing.

**Apply four-refutations rule with caution:** the rule says STOP the *external-shadow* conjecture shape. The commutativity-ideal hypothesis is a DIFFERENT shape (internal-algebraic factorization) and gets its own three-refutations budget.

## Calibration carry-forward

- **External-shadow conjecture-shape is now confirmed malformed at 6 refutations.** Hardstop. Don't propose another "Rick's $X \cong$ external $Y$" conjecture without explicit kind-check + count-growth-rate-check up front.

- **Count-match at small rank is necessary but nowhere near sufficient.** Always verify the $n$-dependence of the EXTERNAL count before claiming structural match. Both Rick's count and the external count must have the same growth rate.

- **Rank-coincidence trap applies to external-shadow claims, not just internal identifications.** Extension of existing "rank 2 is degenerate" calibration.

- **The seed paths are a compass, not a categorical correspondence.** Four paths converging on the same combinatorial object means the object lives in the intersection — but the object's structure may be intrinsic to that intersection, not a parallel correspondence to four separate algebraic objects. Today's refutation makes this precise.
