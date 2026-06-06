# Notes: arXiv:2509.18982 — Weinan Zhang

**Title:** Quantum Howe Duality and Schur Duality of Type AIII
**Author:** Weinan Zhang
**Version:** v2, 10 Jan 2026
**Length:** 32 pages, 6 sections + refs
**MSC:** 17B37

## Main Theorems (verbatim / near-verbatim)

**Theorem A (= Thm 3.3, Thm 4.3).** "Let c = ı or ȷ. There is an explicit isomorphism of U^c_m-modules V^{c,0}_{m|n,n} ≅ V^{⊗n}."

**Theorem B (= Prop 3.8, Thm 3.9, Thm 4.4, Prop 4.5).** "Let c = ı or ȷ. Relative braid group symmetries T_i on V^{c,0}_{m|n,n} satisfy the Hecke relation, and hence they induce an action of the type B Hecke algebra H_B(n) on V^{c,0}_{m|n,n}. Moreover, under the isomorphism V^{c,0}_{m|n,n} ≅ V^{⊗n} in Theorem A, this H_B(n)-action coincides with the H_B(n)-action in (1.2) on V^{⊗n}."

**Theorem C (= Thm 5.3).** "The U^c_n-weight space (L̃^{[n],c}_λ)_ρ for any λ ∈ Par^c_n(n) is an irreducible H_B(n)-module."

**Theorem D (= Thm 6.5, Cor 6.6).** "Up to scalars, the braid group action constructed using R-matrices and K-matrices of U(gl_M), U^ı_m coincides with the relative braid group action induced by T_i, i ∈ [0, n−1]."

## Two sides of the isomorphism

- **iHowe side (Luo–Xu LX22):** Two commuting iquantum groups U^c_m and U^c_n act on V^c_{m|n,d}. Set d=n. Pick the U^c_n-weight ρ (analog of weight 0, fixed by relative Weyl group). The ρ-weight space is U^c_m-stable; relative braid group T_i (Wang–Zhang WZ23/WZ25) act on it.
- **iSchur side (Bao–Wang BW18a):** U^c_m acts on V^{⊗n} (V = natural rep of U(gl_M), m=⌊M/2⌋); type B Hecke algebra H_B(n) commutes.
- The iso is U^c_m-equivariant; transports relative braid group symmetries to the H_B(n) action.
- Yes, weight SPACES (not just weights) and finite-dim modules. Theorem C lifts to irreducible-module level.

## Crystal / Kashiwara / q→0 — NO

Zero matches for "crystal", "Kashiwara", "q = 0". Only specialization mentioned is q→1 (lines 305, 327) for the underlying symmetric pair (gl_{2n}, gl_n ⊕ gl_n). "Icanonical basis" mentioned once in passing (line 352) citing BW18a/BeW18/CLW21 — context only. No crystal-level descent is established or claimed.

## BDI / quasi-split type B iquantum — PARTIAL

- "Quasi-split type AIII" throughout (lines 58, 80, 86, 136, 144). This IS the relevant iquantum, with Iwahori–Matsumoto/Satake diagram of type AIII.
- "Note that, for quasi-split type AIII, the relative Weyl group is isomorphic to the type B Weyl group, and hence T_i satisfy type B braid relations." (paraphrased from lines 144–146).
- No explicit "BDI" terminology; no discussion of the short-long edge a_{n-1,n}=-2 in the iCartan / no Satake diagram diagnostics.
- Pairs treated: (U^ı, U^ı) and (U^ȷ, U^ȷ); mixed pairs (U^ı, U^ȷ), (U^ȷ, U^ı) left to similar treatment.

## Tensor product rules — NO

No tensor-product / fusion / Clebsch–Gordan / branching rules. The only "tensor" hits are about R-matrix acting on tensor factors of V_{M|1} (line 2021ff). What IS present: multiplicity-free decomposition of V^c_{m|n,n} as bimodule (Sec 5, citing LX22 + Watanabe Wat21), used to derive Theorem C.

## Verdict (one line)

**Supports the Path 2 ↔ Path 3 framework-level bridge for v2 at the q-generic algebraic level (iquantum weight space ↔ H_B(n) module is now a theorem), but the bridge does NOT descend to crystal / q→0; Rick's one-line summary was correct in substance but the crystal-level descent question remains open.**
