# Notes on Defant-Searles, "0-Hecke Modules, Domino Tableaux, and Type-B Quasisymmetric Functions"

**Reference.** Colin Defant and Dominic Searles, arXiv:2404.04961v1 [math.CO], 7 Apr 2024 (CJM 2026). PDF cached at `/home/agent/papers/defant-searles-2404.04961.pdf`.

## What the paper does

The paper extends the **ascent-compatibility** framework of Searles (arXiv:2202.12022) from S_n to **all Coxeter groups (W,S)**, then specializes to type B (W=B_n).

**Main constructions:**

1. **Section 3 (ascent-compatibility, type-independent).** Theorem 3.1: if X ⊆ W is "ascent-compatible," then operators π_s on CX define an H_W(0)-action. Theorem 3.3: convex subsets of left weak order with a unique max are ascent-compatible.
2. **Section 3 (type-B applications).** Theorem 3.5: for ascent-compatible X ⊆ B_n, ch^B(CX) = ∑_{x∈X} F^B_{Des(x)}. Applied to Mayorova-Vassilieva sets D^B_I, L^B, type-B Knuth classes C^B_T, signed arc permutations A^B_n.
3. **Section 4 (domino-Schur modules).** Defines an H^B_n(0)-action on CSDT(λ) (standard domino tableaux of partition shape λ). The qsym characteristic gives Mayorova-Vassilieva's type-B Schur function. Introduces "shifted domino functions" H_λ as type-B Schur Q-analogues; proves they expand positively in Petersen's type-B peak functions.
4. **Section 5 (type-B 0-Hecke-Clifford algebra HCl^B_n).** Defines a type-B analogue of the Bergeron-Hivert-Thibon 0-Hecke-Clifford algebra. Modules induced from simple H^B_n(0)-modules realize Petersen's type-B peak functions K_(ζ,P).
5. **Section 6.** General formula for ch^B of Res∘Ind of an ascent-compatible module, applied to the shifted domino modules.

**Categorical level.** Throughout, the target is **G_0 (finite-dim modules)** mapping to **QSym^B** via Huang's quasisymmetric characteristic. NOT K_0^proj. Modules are constructed as cyclic CX with a filtration by simples; this is the **F-basis (fundamental) side**, not the ribbon/projective side.

## Does the paper build NSym^B = K_0^proj(H^B_*(0))? — NO

- The paper makes **no mention** of NSym^B, projective modules of H^B_n(0), Mantaci-Reutenauer, K_0^proj, indecomposable projective covers, or a ribbon basis. (Verified by full-text grep.)
- It cites Chow's thesis [6] only in passing as the source of QSym^B; Mantaci-Reutenauer is **not** cited at all.
- All H^B_n(0)-modules constructed (CX, CSDT(λ), CSShDT(λ̂)) are produced via ascent-compatibility filtrations whose successive quotients are **simples** S^B_I — placing them on the G_0/QSym^B side. Their characteristics live in QSym^B (and the peak subalgebra), never in NSym^B.

**The ingredients that ARE present:** (a) the type-B 0-Hecke algebra H^B_n(0) and a type-B 0-Hecke-Clifford algebra HCl^B_n; (b) parabolic induction/restriction H^B_n(0) ↔ HCl^B_n at the level of **G_0**; (c) explicit module constructions via subsets of B_n.

**The ingredients that are MISSING for NSym^B:** (i) Mantaci-Reutenauer or Chow ribbon-basis identification; (ii) any indecomposable projective P^B_α of H^B_n(0); (iii) tableau models for projectives (the Huang [Hua16] type-A SRT analogue is not done in type B here); (iv) parabolic-induction product H^B_m(0) ⊗ H^B_n(0) → H^B_{m+n}(0) at the K_0^proj level; (v) any K_0^proj-level Frobenius-characteristic isomorphism to NSym^B / Chow's Sym^B.

## Is there an Almousa-Lu-style ribbon-complex tower implicit? — NO

Almousa-Lu need: a tower H_m(0) ⊗ H_n(0) ↪ H_{m+n}(0) of 0-Hecke algebras whose parabolic induction takes projectives to projectives, with explicit gluing maps ∂_{α,β}, μ_{α,β} on indecomposable projectives P_α realizing R_α R_β = R_{α·β} + R_{α⊙β}. None of these appear in Defant-Searles:

- **No type-B tower.** The paper does not consider H^B_m(0) × H^B_n(0) → H^B_{m+n}(0) (the natural type-B parabolic). The only induction discussed is H^B_n(0) ↪ HCl^B_n (Section 5/6) — a **vertical** Clifford extension at fixed n, not the **horizontal** 0-Hecke tower.
- **No projectives.** Even if a tower were specified, the paper has no candidate P^B_α to compute Ind(P^B_α ⊗ P^B_β) on.
- **No ribbon product / no near-concatenation.** The combinatorial operations α·β, α⊙β on type-B compositions, and any module-level lift of the type-B Mantaci-Reutenauer multiplication, do not appear.
- **What IS present**: a Res∘Ind formula at the G_0/QSym^B level for the HCl^B_n vertical extension (Theorem 6.1) — orthogonal to what Almousa-Lu lift.

## Recommendation for Rick

**Option (a) is most natural — but it requires significant new work, and Defant-Searles is at best a *peripheral* foundation, not the technical engine.**

The realistic path:
1. Use **Chow (2001) / Bergeron-Hivert (2008) noncommutative symmetric functions of type B / Mantaci-Reutenauer descent algebra of type B** as the algebraic target (NSym^B). Defant-Searles cites Chow only as the source of QSym^B and does not engage with Chow's NSym^B at all.
2. Construct **indecomposable projective P^B_α** of H^B_n(0) for type-B compositions α. Norton 1979 ([12] in Defant-Searles) gives the abstract decomposition; the missing piece is a **Huang-style tableau model** (analogous to Huang's SRT(α) for type A) on which the π_i (i = 0, ..., n−1) act explicitly.
3. With (1) and (2) in hand, the parabolic-freeness lemma (H^B_{m+n}(0) free over H^B_m(0) ⊗ H^B_n(0); should hold by Norton/Geck-Pfeiffer for any Coxeter parabolic) gives a Krob-Thibon-style induction product on K_0^proj, and the Frobenius-characteristic map K_0^proj(H^B_*(0)) → NSym^B can be set up.

**Option (b) is premature.** Almousa-Lu's machinery requires P^B_α to even start (their splittings are tableau-level maps on SRT). It can be lifted *after* Step 2 above — which is the actual gap.

**Option (c) is partially right.** Defant-Searles is genuinely orthogonal to the NSym^B project: it is about **QSym^B-side modules** (simples, fundamental basis, peak functions), not about projectives. But it is a useful technical foundation for *the QSym^B side* of the type-B Krob-Thibon picture, and its ascent-compatibility framework may help organize the type-B parabolic-restriction combinatorics that will be needed once projectives are in hand.

**Where to look next.** (i) **Chow's 2001 thesis** — for the NSym^B = type-B noncommutative symmetric functions side (the algebraic target). (ii) **Huang, "A tableau approach to the representation theory of 0-Hecke algebras"** [Huang 2016] — to see if Huang or his successors have extended SRT to a type-B model giving P^B_α. (iii) **Bergeron-Hivert-Thibon arXiv:math/0307372** for Mantaci-Reutenauer descent algebra of type B as a Hopf algebra. (iv) **Kim-Searles 2026 (arXiv:2601.22926)** (the type-B poset-modules paper that builds on this one) — Rick already has it on his radar; worth checking whether *they* have moved to the projective side.
