---
title: "Day 76: coupling stratification — narrower theorem proved, broader claim falsified"
date: 2026-06-17
audience: Neil (and future me at 3am)
status: ONE clean uniform theorem + ONE honest negative finding
---

# TL;DR

The Day-76 PROVE target (PROVE.md: "(s_j, p_j) couple iff j=1 in
BDI-feasible pieces") turned out to be FALSE as literally stated. I
exhibit a BDI-feasible piece π^C_2 at n=5 that engineers both π^{p_2}
and π^{s_2}. The Day-75 CODE coupling matrix's clean "(s_1, p_1) only"
result is REGISTRY-BOUNDED, not structural.

What IS n-uniformly TRUE is a narrower statement: the **tight-cap engine
generator** g_{s_j} ∈ T_n admits a **2-ray (R_{p_j} + R_{s_j})
decomposition in a piece with BASE-CANONICAL π^{s_j}** iff j = 1. This
captures the right structural asymmetry — the engineering of g_{s_j}
can be "offloaded" from π^{s_j} to π^{p_j} iff j = 1.

This is Theorem 8.1 of `proofs/2026-06-17-coupling-stratification.md`.

# What's new

## Theorem 8.1 (n-uniform, modulo Conj D-pi at n ≥ 6)

For every n ≥ 3 and 1 ≤ j ≤ n-1:
  g_{s_j} := { 2 e_{B_1} + e_{T_1} + 2 e_S  if j = 1
             { e_{B_{j-1}} + e_{B_j} + e_{T_j} + 2 e_S  if j ≥ 2

is engine 2-ray decomposable ⟺ j = 1.

Proof:
- j = 1: exhibit π^{dRd}(2) := base + (S ← l_n + 2 p_1). BDI-feasible.
  2-ray R_{p_1} + R_{s_1} image = b_2 + (e_{B_1} + e_{T_1}) = g_{s_1}. ✓
- j ≥ 2: with base π^{s_j}, the equation reduces to
  π^{p_j} + π^{p_{j-1}} = e_{B_{j-1}} + 2 e_S.
  But π^{p_j} has B_j ≥ 1 by D-pi/RIGID, contradicting RHS B_j = 0. ✗

## The falsified broader claim and its counterexample

Construction 6.1: π^C_2 at n = 5 with
  π^{p_2} = e_{B_2} + e_S  (engineered, BINARY)
  π^{s_2} = e_{B_2} + e_{T_2} + 2 e_S  (engineered, s_2-engine)
  all other columns base.

Sub-agent ran `verify_piece_via_rays(π^C_2, n=5)`: PASS. All 15 AII rays
yield BDI lattice images. The piece simultaneously engineers (s_2, p_2)
— refuting the literal PROVE.md statement.

# Why the gap

The Day-75 CODE coupling matrix used the Day-72 augmented registry
(42 pieces at n=5). The registry was built from FAMILIES (base,
R-double, simple-divert, l_j-divert, class-1-aux), each modifying ≤1
coord at a time. π^C_2 lives OUTSIDE the registry — it's a *combined*
engineering not built into any known family.

So the Day-75 result is "no coupling in the registry," not "no coupling
structurally." Theorem 8.1 captures what IS structurally true.

# The open question

Is π^C_2 (and its generalisations π^C_j for j ≥ 2 at general n)
**image-redundant** with respect to the registry? I.e., is
  Im(π^C_2) ⊆ ∪_{π' in registry} Im(π')
in the BDI lattice?

Partial probe: the distinctive 2-ray sum lattice point
  e_{B_1} + 2 e_{B_2} + e_{T_2} + 3 e_S
IS reached by exactly 1 of 42 registry pieces (`Rdouble_lv2_alpha1`'s
R_{s_2} ray-image). But the FULL image-semigroup containment is not
verified.

→ Next CODE task: image-redundancy probe for π^C_j at j = 2, 3, ..., n-2
  for n = 5, 6, 7. Determines whether Day-75's "(s_1, p_1) unique
  coupling" holds in MINIMAL covers (if redundant) or fails to hold even
  in minimal covers (if not redundant).

# Why this still matters

Despite the broader claim's falsification, the **engine stratification
picture** is correct:

- For j = 1: the R-double family is the UNIQUE source of the
  α-parameter coupling p_1 to S. The g_{s_1} engine is "partially
  redundant" with π^{p_1} = b_2 (proved here).

- For j > 1: the s-engine columns at level j are GENUINE — no 2-ray
  decomposition exists, the column engineering is structurally unique
  (modulo D-pi).

- The R-AXIS = 1 result (Day-75) was right: only p_1 admits a 3-clique.
  The reason — proved here — is that only at j = 1 does the
  α-parameter LIVE on π^{p_1} (via R-double's S ← ... + α p_1).

# Calibration

- **Day-74 lesson revisited:** Day-74 PROVE was already right that the
  "rest-unique-canonical" claim needed weakening to "image-equivalence
  class." Day-76 extends this: the joint-engineering-coupling claim
  also needs weakening — to engine 2-ray decomposability.

- **The CODE-as-search-light:** Day-75 CODE found a clean pattern in
  the registry; the PROVE attempt revealed the pattern is sharper than
  the registry can support. The combined-piece π^C_2 is invisible to
  the registry but visible to feasibility. We learned where the
  registry's blind spot is.

- **Honest framing wins:** Theorem 8.1 with its clean Mod-D-pi caveat
  is publishable. Overclaiming the broader joint-engineering theorem
  would have set up a future contradiction with π^C_2-style pieces.

# What's next

- CODE: image-redundancy probe for π^C_j (this week's CODE.md candidate).
- LEAN: formalise Theorem 8.1 j=1 direction (~50 lines, π^{dRd}(2)
  feasibility + 2-ray sum = g_{s_1}).
- PROVE next: pick between (a) extending Theorem 8.1 to characterise
  ALL coupled pairs in the matrix (open), or (b) returning to the
  Lean axis side (`aii_cone_generated_by_rays`).

Probably (a): the matrix has 14 coupled pairs total at n=5; a uniform
coupling theorem for all of them would close out the n-uniform structural
analysis cleanly.

— Rick, Day 76, 2026-06-17
