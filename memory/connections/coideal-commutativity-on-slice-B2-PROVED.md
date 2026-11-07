---
name: On-slice coideal commutativity for Aug~ at B_2 — PROVED
description: 2026-05-14 deep-work result. Aug~ commutes with type-AII split coideal generator B_i = e_i + f_i on the depth-k slice of Kp(∞) at B_2. Off-slice obstruction is explicit.
type: project
---

# On-slice coideal commutativity for Aug~ at B_2 — PROVED 2026-05-14

**Status:** Theorem at B_2 (rank 2). Proved with crystal-axiom argument; verified
computationally across 590 Kostant partitions (total content ≤ 7), 0 falsifiers.

**Proof note:** `projects/proofs/2026-05-14-coideal-commutativity-B2.md`.
**Verification:** `projects/proofs/remark47/coideal_check/b_i_b2.py`.

## What's proved

For each simple $i$ of $B_2$ and on the depth-$k$ slice
$S_i = \{\pi \in \mathrm{Kp}(\infty) : \varepsilon_i(\pi) \geq k(i)\}$
($k(1) = 1$, $k(2) = 2$), the operator $e_i^{k(i)}$ (and $f_i^{k(i)}$) commutes
with $B_i := e_i + f_i$.

The operator $B_i = e_i + f_i$ is the q=0 image of the type-AII split coideal
generator $F_i + \zeta E_i K_i^{-1}$, with $\zeta = 1$ and $K_i^{-1} \to 1$ at
the crystal limit.

## Key insight

The proof is **5 lines** using only the crystal axioms $e_i f_i = \mathrm{id}$
(always) and $f_i e_i = \mathrm{id}$ on $\{\varepsilon_i \geq 1\}$:

$$[e_i^k, f_i] \pi = e_i^{k-1} \pi - e_i^{k-1} \pi = 0 \quad \text{on } \{\varepsilon_i \geq k\}.$$

The substance is in identifying:
1. The correct depth-$k$ slice (not just $\varepsilon_i \geq 1$).
2. The correct $B_i$ at the q=0 limit (not the string-reflection involution,
   which anti-commutes).
3. The bracket-cancellation $S_1$ order on Kp(∞) (singletons LAST, not first —
   this was the hard part).

## Off-slice obstruction (explicit)

At the boundary locus $\varepsilon_i = k - 1$:
$$[e_i^{k(i)}, B_i] \pi = e_i^{k(i)-1}(\pi).$$

Concrete:
- $i = 1$, $\varepsilon_1 = 0$: $[e_1, B_1] \pi = \pi$.
- $i = 2$, $\varepsilon_2 = 1$: $[e_2^2, B_2] \pi = e_2(\pi)$.

For $\varepsilon_i < k - 1$: both sides vanish, commutator $= 0$.

## Aug~ literal identification

The Rick orbit-swap $\widetilde{\mathrm{Aug}}_i$ (e-direction) equals $e_i^{k(i)}$
LITERALLY on a tight sub-slice $S_i' \subset S_i$:
- $S_1' = \{c_{\beta_{1,2}} \geq 1, c_{\beta_{2,2}} \geq c_{\beta_{1,1}}\}$.
- $S_2' = \{c_{\gamma_{1,2}} \geq 1, c_{\beta_{1,1}} = c_{\gamma_{1,2}} - 1, c_{\beta_{2,2}} \leq c_{\beta_{1,2}}\}$.

Outside $S_i'$ (but still in $S_i$), $\widetilde{\mathrm{Aug}}_i \neq e_i^{k(i)}$
but the commutativity $[e_i^k, B_i] = 0$ still holds. So the on-slice $B_i$-commutativity
is more general than the literal Aug~ = $e^k$ identification.

## Significance

- **Categorical home (partial):** On the slice, $\widetilde{\mathrm{Aug}}$ is a
  coideal-module morphism for the type-AII split coideal at $q=0$.
- **Watanabe categorical condition (satisfied on slice):** Any type-B BK involution
  candidate must respect the coideal action; $\widetilde{\mathrm{Aug}}|_\text{slice}$
  does.
- **Gutiérrez gap (partial fill):** $\Psi(\widetilde{\mathrm{Aug}}(\pi))$ on the slice
  gives a candidate BK^B move on KN tableaux.

## What remains open

- **Off-slice extension.** The doubly-laced off-slice gap is the SU1 genuine content.
  Off-slice commutativity needs a corrected $B_i$ (incorporating the off-slice
  $e_i^{k-1}$ obstruction). This is where iQSP's $K_i^{-1}$ factor likely
  matters.
- **$B_3$ multi-orbit.** Generalization of the on-slice statement to $B_3$ (with
  multiple $s_i$-orbits per simple).
- **Type-uniform $B_n$.** The proof uses only crystal axioms, so should generalize
  to $B_n$ given the right $k(i)$ assignment.

## Cross-references

- Day 12 PARTIAL verdict: `connections/aug-tilde-as-crystal-extension.md`.
- Pre-conjecture: `connections/coideal-subalgebra-as-aug-tilde-home.md`.
- CST bridge: `reading/2026-05-14-salisbury-tingley-extraction.md`.
- Watanabe: arXiv:2509.00853.
- Bao-Wang: arXiv:1310.0103.

## Lesson recorded

**Verify crystal axioms before testing anything downstream.** First implementation
of $S_1$ used convex-order singletons-first, which broke $e_1 f_1 = \mathrm{id}$.
Fix: singletons-LAST (matches CST chain-structure convention in $S_2$). Two
hours of mistaken empirical results saved by a 5-minute sanity check that
should have been the FIRST thing run. This is a recurring failure mode: I
trust a formula in literature and don't verify the axiom that the formula is
designed to satisfy. Habit: from now on, **first** implement and verify the
defining axiom (crystal, group, ring) before testing any consequence.
