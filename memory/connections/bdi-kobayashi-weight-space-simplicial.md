# The BDI weight-space Kobayashi polytope is SIMPLICIAL

**Date.** 2026-05-21 (Day-29 deep work); **Day-60/62/64 Lean updates** 2026-06-09 → 2026-06-11. **Day-64: THEOREM G COMPLETE.**
**Connection rating.** ⭐⭐⭐⭐⭐ (closes OQ-K Layer 2 + structural surprise + verified Lean kernel fact).

## Lean formalisation status (Day-64 — COMPLETE)

`proofs/lean/bdi-polytope/BdiPolytope.lean`: **866 lines** pure stdlib,
zero Mathlib, zero warnings, zero sorries, `lake build` clean.
`#print axioms` ⊆ {`propext`, `Classical.choice`, `Quot.sound`}.

**Scoreboard (FINAL):**

| # | Lean name | Status |
|---|-----------|--------|
| 1 | H-rep facet def `InKone` | ✅ Day-60 |
| 2 | Each ray ∈ K_n (3 lemmas: `pairRay_in_Kone`, `sumRay_in_Kone`, `eRay_in_Kone`) | ✅ Day-60 (committed Day-62) |
| 3 | n rays linearly independent (`rays_lin_indep`) | ✅ Day-62 |
| 4 | Cone hull surjection (form b, N=2): `Kone_two_in_cone_hull` | ✅ **Day-64** |
| 5 | Uniqueness: `rays_lin_indep_unique` | ✅ **Day-64** |
| ★ | `theorem K_simplicial` headline bundle | ✅ **Day-64** |

**5/5 sub-lemmas + bundle DONE.**

**Lemma 4 (form b, N=2): `Kone_two_in_cone_hull`.** Every $v \in K_n$
($n \ge 3$) admits an explicit nonneg integer linear combination of
the $n$ rays equal to $2v$. Constructive witness `coneCoeff n v`:
- $c_k = 2 \cdot \text{partialSum}\, v\, (k+1)$ for $0 \le k \le n - 3$
  (pair-ray coeffs).
- $c_{n-2} = \text{partialSum}\, v\, n$ (sum-ray coeff).
- $c_{n-1} = \text{partialSum}\, v\, (n-1) - v_{n-1}$ (E-ray coeff).

**Clean facet ↔ coefficient bijection:** each `InKone` inequality forces
non-negativity of exactly one coefficient. Partial-sum facets
$\sum_{i=1}^{k} \lambda_i \ge 0$ ($k = 1, \dots, n-2$) ⇒ pair-ray
coeffs $c_k \ge 0$. Full-sum facet ⇒ sum-ray coeff $c_{n-2} \ge 0$.
E-facet ⇒ E-ray coeff $c_{n-1} \ge 0$. No chains, no Farkas.

**Proof shape:** case-split $j \in \{0, [1, n-3], n-2, n-1\}$; apply
one of four `partialSum_pair_*` lemmas (`_at_zero`, `_above`, `_at_j`,
`_below`); `sumRay` / `eRay` vanish for $j < n-2$ or evaluate to $\pm 1$;
`partialSum_step v n` unfolds the telescoping; `omega` closes linear
arithmetic.

**Lemma 5: `rays_lin_indep_unique`.** Port of `rays_lin_indep`'s
coordinate-descent argument to the difference $(c_k - c'_k)$. Avoided
the `Int`-distributivity subtraction route (would need ring tactic
from Mathlib) by inlining the case-by-case structure.

**Bundle: `K_simplicial`.** Three conjuncts in one statement: non-
negativity, $2v$ decomposition, uniqueness. Proof is `Kone_two_in_cone_hull`
for the first two, `rays_lin_indep_unique` for the third. Two lines
of actual content.

**Form (b) shipped per executive call.** Form (a) [pure $\mathbb{Q}_{\ge 0}$,
cleanest math] needs Mathlib's `Rat` infrastructure; form (c) [pure
integer with explicit 2-torsion correction] needs more elaborate setup.
Both deferred-but-buildable refactors of base; form (b) lands cleanly
stdlib-only. The factor of 2 = the **lattice-index obstruction**:
ray lattice has index 2 in $\mathbb{Z}^n$, so arbitrary $v \in K_n$
need not be an $\mathbb{N}$-combination but $2v$ always is.

**Commits:** `f708cfb` (Lemma 4), `8a6eab9` (Lemma 5 + bundle),
`96f032d` (memory SUMMARY update). All pushed to
`grandpa-rick/rick-research@prove-day-59`.

**What's NOT done:**
- Backward direction $v \in K_n \Leftarrow \exists c$ (closure-under-nonneg-sums).
  Not strictly needed for simpliciality. ~1h if asked.
- $n = 2$ corner case. ~10-line specialization.

**Phantom-completion calibration: HELD on Day-64.** Day-58 (F-easy)
and Day-60 (Theorem G start) both produced on-disk work without
shipping to git. Day-64 LEAN session shipped within-session (three
commits same hour). First clean LEAN session post-STABLE promotion.

## The connection

The chain-side polytope $\mathcal{P}_n$ at $B_n$ has $2n - 3$ carry-derived facets (Theorem F,
Day 28). Its image $\mathcal{K}_n = \Phi(\mathcal{P}_n)$ under the chain-to-weight map has only
$n$ facets (Theorem G, Day 29):

$$\lambda_1 + \cdots + \lambda_k \ge 0\;(k = 1, \dots, n-2), \quad \sum \lambda_i \ge 0, \quad \lambda_n \le \sum_{i < n} \lambda_i.$$

This is **the minimum possible number of facets for a full-dim cone in $\mathbb{R}^n$**, i.e.,
$\mathcal{K}_n$ is a *simplicial cone*. The structural surprise is *not* that the projection
contracts (expected, since chain → weight is many-to-one) but that it contracts to the
**simplest possible** structure.

## What's lost in projection

Of the $2n - 3$ chain facets:
- $E$ (singleton bound) survives → image facet $\lambda_n \le \sum_{i<n} \lambda_i$.
- $L_a, U_a$ for $a = 2, \ldots, n-1$ (the $2n - 4$ MB-bound facets): ALL COLLAPSE. They're
  redundant in the image H-rep (Farkas combinations with $\mu_E$ + chain non-negativity suffice
  to derive every image facet without using $\mu_{L_a}, \mu_{U_a}$).

## Why $E$ survives but $L_a, U_a$ don't

Asymmetry between $E$ and $L_a, U_a$:
- $E$ involves $S$ (which contributes only to $\lambda_n$ in $\Phi$) bounded by $P_{n-1}$
  (which involves all $B_a, T_a$). So $E$ has a "boundary" character — it relates the
  $\lambda_n$ direction to all others, defining a *new* hyperplane.
- $L_a, U_a$ involve $M_a$ bounded by $P_{a-1}$ or $P_a$, all interior chain quantities.
  In $\Phi$, $M_a, B_a, T_a$ all contribute to $\lambda_a$ symmetrically; the bound
  $M_a \le 2 \sum (B - T)$ becomes a weight-space ineq that's *weaker* than chain non-negativity
  already gives. So they collapse to interior.

## Implications

**For Kobayashi 2604.22262:** The weight-space "fence" decomposition for BDI branching at
$B_n$ should have $n$ fences (matching $\mathcal{K}_n$ facets). Kobayashi's framework is general
piecewise-linear; the *explicit* fence count is now known. **OQ-KOB-MATCH** (v4): does
Kobayashi's intrinsic fence list match my $n$ explicit ineqs?

**For Watanabe 2407 / Meereboer 2510:** Both give algebraic existence results that should
factor through the $n$-facet image polytope. Watanabe's $p_\nu$ projection should be
piecewise-polynomial on the $n$-simplex regions inside $\mathcal{K}_n$.

**For carry framework structure:** The carry $P_a$ has 4 roles (Day 28). Theorem G adds a
**5th role**: the carry chain $P_1, \ldots, P_{n-1}$ generates the "interior" structure
of $\mathcal{P}_n$, but only the *final* carry $P_{n-1}$ (via $E$) survives projection to
weight space. So:
- Carry as descent potential (role 1): chain-side only.
- Carry as cross-chain coupling (role 2): chain-side only.
- Carry as recursive scalar (role 3): chain-side only.
- Carry as polytope-completeness object (role 4): both sides, but $2n-3$ → $1$.
- **Carry as weight-projection invariant (role 5, NEW): only $P_{n-1}$ via $E$ survives.**

The first four roles live in chain space; the fifth role is the *one* trace of carry
visible in weight space. Strong contraction.

## Type-uniform statement

For $n \ge 2$:
- $|\mathcal{P}_n|_{\text{facets}} = 2n - 3$ (chain side)
- $|\mathcal{K}_n|_{\text{facets}} = n$ (weight side)
- Ratio $(2n-3)/n \to 2$ as $n \to \infty$. Each carry facet "doubles" the resolution that
  weight space can't see.

## What this rules out

The conjecture that the chain → weight map is "structure-preserving" (i.e., a near-bijection
on facet sets) is *refuted*. This was the "natural" expectation that motivated PROVE.md's
P=80% Q1=YES prior. The actual relationship is contractive — chain space is finer than
weight space.

This is structurally similar to the Day 22-25 asymmetric-mirror finding (forward and reverse
descent are NOT exchanged by a local involution): in both cases, what looks like it should
be symmetric / faithful turns out to have a deep contractive asymmetry baked in.

## Files

- `proofs/2026-05-21-weight-space-projection.md` — Theorem G full writeup.
- `proofs/2026-05-21-weight-space-projection/` — verification scripts.
- `memory/for-collaborator/2026-05-21-bdi-kobayashi-weight-space-G.md` — Robin/Clio note.
