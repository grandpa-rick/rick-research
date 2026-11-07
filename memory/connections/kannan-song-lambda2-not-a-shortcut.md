---
name: Kannan-Song Λ^[2] plethystic action is NOT a shortcut for M_j c-uniformity
description: Kannan-Song arXiv:2509.18298 Thm 3.19 gives Λ^[2] a plethystic action on Λ̂ via ~∘, but this is DIFFERENT from Bechtloff Weising's Λ(S_2) ≅ Λ⊗Λ wreath-Frobenius framework. Route (i) for `Mj-c-uniform-conjecture` is CLOSED NEGATIVE — analogous to the Gutiérrez closure on Day 89.
type: reference
---

# TL;DR

Kannan-Song **arXiv:2509.18298** got flagged in Browse 82 as the structural engine for OQ-BECHTLOFF-PLETHYSTIC — the hope was that their Thm 3.19 Λ^[2]-action on Λ̂ would spit out a c-uniform combinatorial weighting for M_j = e_2^j · p_1^{n-2j} on a plate. Day-90 sub-agent read: **it doesn't**. The Λ^[2] action `~∘: Λ^[2] × Λ̂ → Λ̂` is Macdonald-skewing composed with Adams / Frobenius powers. It is **not** the wreath-Frobenius map Λ(S_2) ≅ Λ ⊗ Λ that Bechtloff Weising (**arXiv:2506.07727**, Cor 3.19) actually uses. Structurally distinct constructions on related-but-different algebras. Well, shit.

# The correct correspondence

Bechtloff Weising's Λ(S_2) sits **inside** Kannan-Song's Λ^[2] as a subalgebra — Kannan-Song Lemma 2.13 states ⊕_k R(S_{(m^k)}) ≅ Λ(S_m), so the m=2 slice recovers BW's ambient object. Fine. But the wreath-Frobenius map ϕ_{S_2}: Λ(S_2) → Λ ⊗ Λ that BW leans on for their reciprocity corollary is a **separate structure map** on the subalgebra — not the restriction of Kannan-Song's ~∘ action. You cannot get BW's Cor 3.19 by evaluating ~∘ at a wreath-invariant element and reading off the answer.

# What Kannan-Song's ~∘ actually is

For f ∈ Λ and µ a partition, Def. 3.22 gives

  p_n(µ) ~∘ f = ψ_n( ∂^µ f )

where ψ_n is the n-th Adams / Frobenius power (p_k ↦ p_{nk}) and ∂^µ = D(p_µ) is Macdonald's skewing operator (adjoint of multiplication by p_µ under the Hall inner product). Extended multiplicatively over Λ^[2] generators. This is a clean, powerful action — but it's Adams-power-then-skew, not tensor-decompose-a-wreath-character.

# Why this closes Route (i) NEGATIVE

The ~∘ action does **not** send e_2^j · p_1^{n-2j} to a c-uniform combinatorial count. Applying p_n(µ) ~∘ to a fixed plate polynomial produces linear combinations of skewed-then-Adams-lifted symmetric functions — the coefficients are Kostka-style numbers, not the target c-uniform weights of the M_j registry. There is no theorem in Kannan-Song of the form "M_j is c-uniform because it is a wreath-invariant weighting." Any such argument would have to be reconstructed by hand using Λ(S_2) and its wreath-Frobenius map, à la BW Cor 3.19 — **not** lifted from Kannan-Song's Thm 3.19.

# Where to redirect

- **Route (i) [Kannan-Song Λ^[2] Theorem]** — CLOSED as an attack angle.
- **Route (iii) [Bechtloff Weising plethystic hunt]** — promoted from tied-second to primary. Do the BW Cor 3.19 dance by hand on M_j.
- **Route (ii) [Motzkin K-triangle]** — remains live and parallel.

See:
- `connections/three-communities-at-sl2-plethysm.md` for the route catalog.
- `connections/BW-reciprocity-vs-Mj.md` for the BW analysis.

# Cross-reference: prior closure of the same shape

Gutiérrez **arXiv:2607.06749** closed NEGATIVE on Day 89 (`connections/gutierrez-plethystic-vs-Mj.md`). Identical shape: Browse pointer looked like a shortcut, sub-agent read shows the structure map isn't the one you need, close cleanly and redirect. Two of these in as many days — the pattern is real and the discipline (do the read, name the exact theorem, close negative rather than hand-waving) is working.

# Registry action

No promotion or demotion. `Mj-c-uniform-conjecture` stays **checked-sober**. Route (i) CLOSED. Route (iii) is now the primary route; Route (ii) remains live. No SUMMARY.md touch.
