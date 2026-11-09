# Q67 parked question: bimodule filtration of V^{⊗N} by D_I ⊠ M_I. Wake 286 compute + owner check (2026-11-09)

**Question.** Does V^{⊗N} (V=C^n), as an (S_0(n,N), H_N(0))-bimodule (equivalently U_0(gl_n) × H_N(0)), have a filtration whose subquotients are D_I ⊠ M_I, with I running over compositions of N with ℓ(I) ≤ n?
- D_I is the simple module. As an S_0-module it is S_{I•}; restricted to U_0 it is D_I, with character F_I.
- M_I is the **projective** indecomposable H_N(0)-module. KT NCSF IV p.360 l.1228: "M_I such that M_I/rad(M_I) ≃ C_I ... The family (M_I) forms a complete system of projective indecomposable H_N(0)-modules".
- If such a filtration exists, its K_0 class is the Q67 identity Σ F_I R_I. That class identity forces each I to occur exactly once.

## A. Owner check

1. **KT NCSF IV §7** (J. Alg. Comb. 1997, p.373–374, on disk). They state "two natural ways of decomposing V⊗N into A_0(n) × H_N(0)-bicomodules".
   - (13): V⊗N = ⊕ N_I, a direct sum.
   - §7.2: "these compositions factors are exactly the comodules D_I each of them occuring |QR(I)| times. But D_I considered as a left H_N(0)-module is isomorphic to M_I. It follows that there exists a basis of V⊗N indexed by pairs (Q,R)".
   - So KT give composition factors and a basis only. **No bimodule filtration is claimed.**
2. **KT NCSF V §5.3, Note 5.7** (IJAC 1999, on disk). The double commutant fails for (U_0, H).
   - Their numbers are dim ρ(U_0) = 19 < 20 = dim ρ(H_3(0))′ and dim ρ(H_3(0)) = 5 < 7 = dim ρ(U_0)′.
   - **We reproduce these exactly at V=C², N=3.** The text (as extracted) labels the case "n=3, N=3 / gl_3". At C³, N=3 we get 165/165/6/6, where the double commutant HOLDS. This looks like a label slip; check against the PDF.
3. **Jung–Oh, arXiv 2509.26194** (2025). This is the closest modern source.
   - (4.7): S_0(n,r) ≅ End_{H_r(0)}(V^{⊗r}).
   - Remark 4.3: "the double commutant property fails for the (U_0(gl_n), H_r(0))-bimodule V_0^{⊗r} (see [17, Note 5.7])".
   - Thm 4.13: G(F_α) ≅ S_{α•} and G(R_α) ≅ P_{α•}.
   - Cor 4.15: soc P_λ ≅ S_{λ^r}.
   - Citing Deng–Yang (JPAA 216 (2012) 1253; not on arXiv, not read): S_0 is Morita-equivalent to eH_r(0)e, and S_0 is self-injective (DY Prop 4.4).
   - Jung–Oh make no claim about a bimodule filtration or about (S_0, H) double centralizer.
4. **Other papers.** I checked these abstracts and text only for statements about tensor space (no bimodule-filtration or (S_0,H) double-centralizer statements found):
   - Jensen–Su 1207.6769 (geometric S_0)
   - Jensen–Su–Yang 1312.5487 (projectives of S_0)
   - Jensen–Su–Yang 1705.06084
   - Du–Jensen–Su 1511.04135
   - Miyamoto–Wang 2207.03079 (τ-tilting finiteness of S_0)

**Verdict.** The filtration question appears unowned and unasked. The (U_0,H) failure is owned (KT 1999, Jung–Oh). Deng–Yang was not read, so the (S_0,H) double centralizer status is unknown.

## B. Compute (scripts core.py, step1b.py, step1_endS.py, step2.py, step3.py; exact over Q via python-flint unless *)

Action: Jung–Oh (4.5), with π̄_i² = −π̄_i. The braid and far-commutation relations hold, and U_0 commutes with H, in all cases.

| (n,N) | n^N | dim ρ(H) | dim S_0 = C(n²+N−1,N) | dim End_{S_0}(V) | DC(S_0,H) | dim ρ(U_0) | dim ρ(U_0)′ | dim J(S_0) | Loewy dims rad^k V | filtration D_I⊠M_I |
|---|---|---|---|---|---|---|---|---|---|---|
| (2,2) | 4 | 2 | 10 | 2 | yes | 10 | 2 | 0 | 4,0 | YES (semisimple) |
| (2,3) | 8 | 5 | 20 | 5 | yes | 19 | 7 | 2 | 8,2,0 | **NO** |
| (3,3) | 27 | 6 | 165 | 6 | yes | 165 | 6 | 32 | 27,8,0 | **NO** |
| (2,4) | 16 | 14 | 35 | 14 | yes | 31 | 28 | 7 | 16,8,3,0 | **NO** |
| (3,4) | 81 | 23 | 495 | 23 | yes | 493* | 29* | 192 | 81,48,18,0 | **NO** |

\* These two values are mod p (p = 2147483629). The 493 elements are certified independent over Q, so 493 is an exact lower bound and the true dimension is at most 495.

**How "NO" is proved.**
1. Any bottom piece L_I⊠M_I lies in Soc_S(V) = {v : J(S)v = 0}. Multiplying it by soc(H_N(0)) gives L_I ⊠ C_{ν(I)}, where ν is the Nakayama permutation (computed: ν = reversal).
2. Dually, any top piece survives in (V/J(S)V)·soc(H).
3. Computed, in every non-semisimple case: the only allowed bottom and top pieces have dim M_I = 1, i.e. I=(N), plus (1^N) when n ≥ N.
4. When n<N, the bottom and top pieces must both be (N). That is impossible when there are at least 2 pieces, so the answer is NO.
5. For (3,3): the 1-dim pieces are forced and unique. After peeling them in either order, no allowed piece remains, so the answer is NO.

S-labels were identified by expanding weight characters in F_J. This relies on the cited fact that L_J has character F_J. It is consistent with the diagonal top layer.

**Structure seen (computed).**
- Top layer of V = ⊕ L_I⊠C_I.
- Socle layer = ⊕ L_I⊠C_{ν(I)}.
- The bimodule composition factors equal those of ⊕ L_I⊠M_I, so the K_0 identity holds.
- J(S_0) ≠ 0 acts, and it mixes S-labels in the middle layers (e.g. (3,4): L_22⊠C_13 and L_121⊠C_22 in rad²).
- So the Q67 K_0 identity does **not** lift to a filtration.
- DC(S_0,H) holds in all 5 cases. DC(U_0,H) fails exactly when ρ(U_0) ⊊ S_0.

## Grades

- Table and NO verdicts: **computed**.
- "Fails for all n ≥ 2, N ≥ 3, because only 1-dimensional M_I occur as end pieces": **hunch** (4 cases).
- "DC(S_0,H) always holds": **hunch**. It is computed for the 5 cases above; for n ≥ N it is standard Morita.
