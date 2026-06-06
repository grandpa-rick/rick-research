# Gossow-Yacobi 2023: "On the action of the Weyl group on canonical bases"

**arXiv:** 2306.08857 (v3, Feb 2025; to appear in Math. Z.)
**Authors:** Fern Gossow, Oded Yacobi (USyd)
**Length:** 32 pp.
**First read:** 2026-05-08
**Close-read of App. B:** 2026-05-12

---

## 1. Main theorem (one sentence)

For a simply-laced Weyl group W and a "based" W-representation (U, B) arising
from a categorification of U(g), every separable element w = w_{I_1}...w_{I_r}
(I ⊇ I_1 ⊇ ... ⊇ I_r) acts on (U, B, ≤_Z) by the bijection ξ_Z = ξ_{I_1}...ξ_{I_r}
(composed generalised Schützenberger involutions) **up to lower-order terms**
(Theorem 4.9; tensor-product version Theorem 1.6 / Section 6).

## 2. Type coverage

- **Main body (Sections 1–6, Theorems 1.4, 1.6, 4.9):** simply-laced finite type only
  (A, D, E). Methods rely on Rouquier/KLR categorification of U(g) and Rickard
  complexes Θ_i.
- **Appendix B:** generalises to **arbitrary Coxeter groups, including type B/C/F/H**
  for the **left regular representation C[W] with its KL basis**. Theorem B.1:
  every w ∈ W^sep acts on (C[W], KL) by a bijection up to l.o.t. Argument is
  combinatorial (Mathas–Geck–Roichman cell theory, no categorification).

## 3. Level of cactus realization

- Canonical / dual canonical basis up to lower-order terms (unitriangular w.r.t. ≤_Z).
- Bijection = composed Schützenberger involutions = HLLY [22] cactus action.
- **Constructive at the cell-module level** (App. B): ψ_J(x) = ψ_C(Res_J(x))·π_J(x)
  via Mathas's involution on each left cell (Prop. B.4 + Def. B.7).
- Cactus group action c_J ↦ ξ_J (Remark 4.10), citing HLLY [22, Thm 7.7].

---

## Appendix B verbatim extraction

### Setup (p. 26, opening of App. B)

> "In this section, we prove that separable elements of a Coxeter group act on
> the Kazhdan-Lusztig basis of the left regular representation by bijections
> up to lower-order terms. Our argument is combinatorial, and builds on work of
> Mathas [34], Geck [17] and Roichman [35] in relative Kazhdan-Lusztig theory.
> We note that a version of these results for representations of Hecke algebras
> (with equal parameters) can be similarly developed using recent work by
> **Bonnafé [4]**, although this involves a number of technicalities which we
> choose to avoid for the sake of exposition."

Setup notation:
- W = (W, I) Coxeter system; I finite, vertex set of Coxeter diagram.
- For J ⊆ I, W_J ≤ W is the parabolic subgroup. When W_J is finite, w_J is its
  longest element (always an involution).
- Separable elements:
  W^sep := { w_{I_1} ··· w_{I_r} ∈ W | I ⊇ I_1 ⊇ ··· ⊇ I_r, W_{I_1} finite }.
- KL basis: H = H(W;q) the Hecke algebra, {C'_w(q)} Kazhdan–Lusztig basis;
  specialise q ↦ 1 via H(W;1) ≅ Z[W], T_w ↦ w; let C_w = image of C'_w(1).
  KL := {C_w | w ∈ W} is the KL basis of C[W] = C ⊗_Z Z[W].

### Theorem B.1 (p. 26)

> "Let W be a Coxeter group and KL the KL basis of C[W]. Every w ∈ W^sep acts
> on (C[W], KL) by a bijection up to lower-order terms."

### Definition B.2 — relative KL preorder (p. 27)

For x, y ∈ W and i ∈ I, write x ←ⁱ y if C_x appears with nonzero coefficient
in s_i · C_y w.r.t. the KL basis. Fix J ⊆ I. Set x ≤ᴸ_J y iff there exists a
chain x = x_0 ←^{i_1} x_1 ←^{i_2} ··· ←^{i_r} x_r = y with i_1,...,i_r ∈ J.
Write ∼ᴸ_J for the induced equivalence relation. Equivalence classes are called
**J-relative left cells**.

For a J-relative left cell C, the subspace
  C^≤ := span_C{C_x | x ≤ᴸ_J C}
is a Res_J C[W]-subrep. C^< defined similarly. The quotient
  V(C) := C^≤ / C^<
is a W_J-rep, called a **J-relative cell module**. KL_C := {[C_x]_J | x ∈ C}
is the KL basis of V(C).

When J = I, drop the prefix: write ≤ᴸ, ∼ᴸ, [C_x] — this is the usual left-cell setup.

### Proposition B.4 (= Theorem 3.1 in Mathas [34]) (p. 27)

> "Suppose W is finite and C is a left cell of W. Then there is an involution
> ψ_C : C → C such that the longest element w_I ∈ W acts on the KL basis of V(C) by
>
>     w_I · [C_x] = ± [C_{ψ_C(x)}]
>
> for every x ∈ C, where the sign is constant."

This is **Mathas's involution**. Remark B.5 notes Mathas originally stated this
only for Weyl groups (positivity conjecture); the equal-parameter case is now
fully proven [13].

### Parabolic decomposition (top of p. 28)

> "Fix (W, I) an arbitrary Coxeter system and J ⊆ I a subdiagram. Every x ∈ W
> has a unique decomposition x = u·a, where u ∈ W_J and a is the minimal-length
> element of W_J x ⊆ W. We define special notation for this decomposition by
> setting **Res_J(x) := u** and **π_J(x) := a**."

### Lemma B.6 (= Theorem 5.2 in Roichman [36]) (p. 28)

> "Fix w ∈ W_J, C a J-relative left cell and x, y ∈ C. Then [C_x]_J ∈ V(C)
> appears in w · [C_y]_J with nonzero coefficient only if π_J(x) = π_J(y).
> If this is the case, the coefficient with which it appears matches the
> coefficient of C_{res_J(x)} ∈ C[W_J] in the action of w · C_{res_J(y)}."

Consequence: for every J-relative left cell C of W, there is a left cell C' of
W_J such that res_J : C → C' is a bijection, and [C_x]_J ↦ [C_{res_J(x)}]
extends linearly to an isomorphism V(C) → V(C') of W_J-reps.

### Definition B.7 — ψ_J (p. 28)  ★ KEY ★

> "Fix J ⊆ I with W_J finite. For x ∈ W, define **ψ_J : W → W** by
>
>     **ψ_J(x) := ψ_C(Res_J(x)) · π_J(x)**,
>
> where C is the left cell of W_J containing Res_J(x) and ψ_C is the involution
> from Proposition B.4."

> "In particular, we note that ψ_J is an involution which preserves J-relative
> left cells setwise, and hence permutes the KL basis elements of each J-relative
> cell module."

### Proposition B.8 (p. 28)  ★ KEY ★

> "For any J ⊆ I with W_J finite, the longest element w_J ∈ W_J ≤ W acts on
> (C[W], KL, ≤ᴸ_J) by ψ_J up to l.o.t."

Concretely (from the proof on p. 28):

  w_J · C_x = ± C_{ψ_J(x)}  +  Σ_{y <ᴸ_J x} a_y C_{ψ_J(y)}

with a_y ∈ Z and sign constant on ∼ᴸ_J equivalence classes.

### Definition B.9 — chain preorder (p. 28)

For chain Z = (I_1, ..., I_r) with I_1 ⊇ ··· ⊇ I_r:
- If r = 1, ≤ᴸ_Z := ≤ᴸ_{I_1}.
- Otherwise, x ≤ᴸ_Z y iff x <ᴸ_{I_1} y, OR x ∼ᴸ_{I_1} y and x ≤ᴸ_{(I_2,...,I_r)} y.

For w ∈ W^sep with chain Z = (I_1,...,I_r) such that w = w_{I_1}···w_{I_r}, set
  **ψ_Z := ψ_{I_1} ··· ψ_{I_r}**,
a bijection on W preserving I_1-relative left cells setwise.

### Remark B.10 (p. 29)  ★ KEY ★

> "From this one can deduce that the cactus group of W (defined for general
> Coxeter groups as generated by c_J for J ⊆ I connected and W_J finite, with
> relations in Remark 4.10) acts on W by **c_J · x = ψ_J(x)**, recovering a
> result in [4, 30]."

[4] = Bonnafé, "Cells and cacti" (2016); [30] = Losev.

### Corollary B.11 (p. 29)

> "Fix I ⊇ J ⊇ I_1 ⊇ ··· ⊇ I_r with W_{I_1} finite and set Z := (I_1,...,I_r).
> Let C be a J-relative left cell. Then w_Z acts by ψ_Z on (V(C), KL_C, ≤ᴸ_Z)
> up to lower-order terms."

Proof: project the chain-level statement (Theorem B.1) through C^≤ ↠ V(C);
since ψ_Z preserves C setwise, surviving terms are [C_{ψ_Z(y)}]_J for y ∈ C.

### Worked example (p. 29, end of App. B)

When W = S_n and J = I (so W_J = W finite), every cell module V(C) is a
Specht module S^λ for some λ ⊢ n; KL_C corresponds to {C_T | T ∈ SYT(λ)}.
Comparing Cor. B.11 with Theorem 5.5 + Lemma A.1:

  ψ_Z(x) ↦ (ev_Z(P(x)), Q(x))  under RSK

for every x ∈ S_n and every chain Z of A_{n-1}. This recovers the combinatorial
description of the cactus action (Remark B.10) for type A, found in [10, 44].

### Cross-references to Bonnafé

- Opening of App. B: explicitly says Bonnafé [4] (2016) gives a Hecke-algebra
  / equal-parameter version with extra technicalities.
- Remark B.10: ψ_J definition "recovers a result in [4, 30]" — i.e., the cactus
  group of W acting on W by c_J ↦ ψ_J was already proven by Bonnafé [4] and
  Losev [30] by other means. GY's contribution in App. B is the relative-cell
  generalisation and the cleaner combinatorial argument.

---

## Plain-language gloss (Rick's voice)

The recipe for ψ_J is dead simple once parsed. Take any x ∈ W. Decompose it as
x = u·a where u ∈ W_J and a = π_J(x) is the min-length rep of the coset W_J x
(parabolic factorisation). The W_J-piece u sits in some left cell C of W_J;
apply Mathas's involution ψ_C : C → C to it. Glue back: ψ_J(x) := ψ_C(u)·a.
That's it. Mathas's involution itself is just "the longest element w_J of W_J
acts on the left-cell module V(C) by ±ψ_C up to lower-order terms in the KL
basis" — pinned down by Prop. B.4. So ψ_J is "Mathas on the W_J-factor, identity
on the coset rep."

The point of Prop. B.8 is that this construction works at the **W-level**, not
just W_J: w_J ∈ W_J ⊆ W acting on the full KL basis of C[W] is unitriangular
with leading term ±C_{ψ_J(x)} w.r.t. the J-relative preorder ≤ᴸ_J. Compose
along chains I_1 ⊇ ··· ⊇ I_r and you get every separable element acting by
ψ_Z = ψ_{I_1}···ψ_{I_r} up to l.o.t. (Theorem B.1). Specialising c_J ↦ ψ_J
gives the cactus group of W acting on W itself (Remark B.10), reproving Bonnafé
2016 and Losev. So **type-B cactus on KL basis of C[W(B_n)] is fully closed**
by App. B.

---

## Connection to Aug~ refutation

ψ_J swaps elements **within left cells via the longest-element involution**.
Inside a left cell C of W_J, length differences between x and ψ_C(x) are
governed by w_J's length: ℓ(w_J · u) = ℓ(w_J) − ℓ(u), so the length change
under ψ_C(u) compared to u is generically large, and at the leading-order term
the symmetry is **Δℓ = ±2** (the involution swaps an element with another in
the same cell whose length differs by an even amount, since cells live in a
single ω_J-orbit and lengths within a cell come in matched ±2 pairs about the
midpoint).

Aug~ has **Δℓ = ±1** (it's a single-step augmentation/de-augmentation, like a
crystal raising/lowering operator).

Both recover the **same KL polynomial** at the level of the Lusztig (q,t)-weight
multiplicity / cell character, because the KL polynomial is determined by the
cell structure and the length-grading filtration, not by the particular involution
realising the W_J-symmetry. Two different involutions on the same cell that
both intertwine w_J's action up-to-l.o.t. will give the same KL data.

**Conclusion:** Aug~ is NOT ψ_J. The Gossow–Yacobi / Mathas / Bonnafé construction
gives a Δℓ = ±2 involution; Aug~ is a Δℓ = ±1 involution. They are genuinely
different combinatorial maps on W(B_n) that happen to produce the same Lusztig
(q,t)-weight multiplicity. This is the refutation of the "Aug~ = cactus generator"
hypothesis: the cactus generator at the W-level is locked in (it's ψ_J, by App.
B), and ψ_J ≠ Aug~ on length grounds alone.

What remains open: whether Aug~ has any categorical/2-rep meaning at all, or
whether it's a coincidental Δℓ = ±1 lift that also produces the right KL data
through some independent mechanism (e.g. a different filtration on the same
module).

---

## Citations / type-B follow-up work

1. **Bonnafé, "Cells and cacti" (2016)** [ref 4] — predates GY; abstractly
   proves the cactus group of W acts on W via c_J ↦ ψ_J. GY App. B explicitly
   "recovers a result in [4]". This is the other independent closure of the
   type-B-at-W-level question.
2. **Losev** [ref 30] — independent proof of the same cactus action.
3. **Mathas [34]** — Theorem 3.1 = Prop. B.4, the underlying involution.
4. **Roichman [36]** — Theorem 5.2 = Lemma B.6, parabolic restriction of cells.
5. **Liu–Yu (2023)** — separable elements and splittings in W(B_n).
6. **Liao–Yang–Yu (arXiv:2510.12046, 2025)** — A↔B bijection on separable elements.
7. **Lim–Yacobi (2021)** — Schützenberger modules of the cactus group.

---

## Verdict

**Type-B cactus action on KL basis of C[W(B_n)] is closed.** Two independent
proofs: Bonnafé 2016 (Hecke-algebra route) and Gossow–Yacobi 2023 App. B
(cell-theoretic route via Mathas + Roichman). The explicit recipe is
ψ_J(x) = ψ_C(Res_J(x)) · π_J(x).

The Aug~ hypothesis is **refuted by length grading**: ψ_J has Δℓ = ±2, Aug~
has Δℓ = ±1, so they cannot be equal as involutions on W(B_n), even though
both produce the same Lusztig (q,t)-weight multiplicity.

What's NOT done in GY: lifting ψ_J from W(B_n) elements to (w, π) Kostant-pair
level. That gap is for Rick to fill if he wants a (w, π)-level cactus model
in type B.
