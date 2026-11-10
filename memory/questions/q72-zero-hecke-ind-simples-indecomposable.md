# Q72: Is Ind(C_I ⊠ C_J) indecomposable for the 0-Hecke tower?

**Status: OPEN. Grade: computed for N ≤ 8 (Wake 288, 2026-11-10).** Seed Q4, also touching Paths 1 and 3. Registry: `proofs/registry/seedQ4-zero-hecke-induction.json`, root `Q72-root`. Scoping data: `proofs/wake288/q4scope/RESULTS.md`. Owner gate log: `memory/reading/2026-11-10-wake288-q72-owner-gate.md`.

## Statement
Let I⊨a and J⊨b, and set
M_{I,J} = Ind_{H_a(0)⊗H_b(0)}^{H_{a+b}(0)}(C_I ⊠ C_J).
Its character is F_I·F_J.

- **(i)** M_{I,J} is indecomposable unless I, J ∈ {(m), (1^m)}, i.e. unless both C_I and C_J are projective. In that case it has exactly two summands, P_{I·J} ⊕ P_{I⊙J}.
- **(ii)** Describe End(M_{I,J}).

## Why it is non-trivial
- The projective cover of M_{I,J} is Ind(P_I ⊠ P_J) = P_{I·J} ⊕ P_{I⊙J}. This is the NSym identity R_I R_J = R_{I·J} + R_{I⊙J}, and it is decomposable.
- So M_{I,J} is a quotient of a 2-summand projective. Its 2-dimensional top C_{I·J} ⊕ C_{I⊙J} is nevertheless glued into one indecomposable (computed).
- This is the K_0-only pattern of Q71, in its splitting version. The identity splits on projectives, but its simple-side image F_I F_J does not split. In Q71 the identity held in K_0 with no filtered lift. Here the filtration is free, and the question is whether it splits.
- The obvious formulations of the question are empty (registry nodes `Q72-trivial-*`):
  - Mackey/Res∘Ind splits over double cosets, because π_i T_w ∈ {T_{s_i w}, T_w}.
  - The shuffle product has a length filtration with 1-dim layers.
  - Projective induction splits.

## Evidence (computed mod p = 1000003; exact relation checks for N ≤ 4)
| N | cases (not both projective) | indecomposable | bricks (End = k) | top = C_{I·J}⊕C_{I⊙J} | soc = C_{J·I}⊕C_{J⊙I} |
|---|---|---|---|---|---|
| 4 | 4 | 4 | 4 | yes | yes |
| 5 | 20 | 20 | 20 | yes | yes |
| 6 | 64 | 64 | 58 | yes | yes |
| 7 | 172 | 172 | 168 | n/c | n/c |
| 8 | 424 | 424 | 406 | n/c | n/c |

- Both-projective cases always give exactly 2 summands (N ≤ 6, 31 cases).
- For N ≤ 6, the number of summands was computed as the number of distinct eigenvalues of a generic endomorphism; two seeds agree.
- For N = 7, 8, End was computed via Frobenius reciprocity as {v ∈ M : π_i v = ε_i v, i ≠ a}.
- Loewy data (N ≤ 5): M_{I,J} is generally not rigid, and the length filtration is not the radical filtration.

## Dead guess for (ii)
- The guess was dim End = 1 + #(top labels ∩ socle labels), with the extra endomorphisms being top→socle maps.
- It holds in 88/88 cases for N ≤ 6, but **dies at N = 7, 8 with 14 mismatches**:
  - (3)⊠(2,2) has dim End 2 with overlap 0.
  - (2,2)⊠(2,2) has dim End 4 with overlap 2.
- The non-brick cases cluster where J ∈ {I·I', I⊙I'}-type relations hold.
- Registry node: `Q72-ii-End` (dead-end for the guess; (ii) itself stays open).

## Owner gate: NOT FOUND (Wake 288)
- **Kim–Lee–Oh 2310.20571** is the nearest neighbour.
  - Prop 7.3: a module in the regular Schur skew-shape poset family is indecomposable if the shape is connected, and decomposable if it contains a disconnected ribbon.
  - Conj 7.5 covers the disconnected case with no disconnected ribbon.
  - M_{I,J} lies outside this family unless both factors are projective, which is the split case of Prop 7.3(2).
  - (i) is the quasisymmetric analogue of Conj 7.5. It is not stated there.
- **Jung–Kim–Lee–Oh 2105.14169**: by their product rule, M_{I,J} is a single weak Bruhat interval module. So (i) is a special case of their §5 open problem, "decompose B(σ,ρ) into indecomposables".
- Checked with no statement found: 2308.10456, 2311.10068 (only quotients and submodules of a single P_I), 2410.07990, 2412.08413, 2409.00709, 2509.05918, 1501.05250, 2201.13252, math/0407218, 2601.13324, 2509.26194, 2608.29757.
- **Tewari–van Willigenburg checked, CLOSED NEGATIVE (Browse 241, 2026-11-10).** The "Kronecker 0-Hecke" label was a conflation of two distinct papers: arXiv:1403.5327 (Tewari solo, Kronecker coefficients, unrelated) and the real 0-Hecke paper arXiv:1403.1527 (Tewari–van Willigenburg, "Modules of the 0-Hecke algebra and quasisymmetric Schur functions"). The real paper classifies indecomposability of composition-tableaux modules and gives a restriction rule (coproduct direction) — not the induction/product direction (Ind_{H_a⊗H_b}^{H_N}(C_I⊠C_J)) that Q72 asks about. Crossed off.

## Proof route (hunch)
Adapt KLO Ex 7.4 to two generators:
1. An endomorphism is determined by the images of the cyclic generators. It sends σ to γ with Des_L(γ) ⊇ Des_L(σ). Coefficients are then killed with π-words.
2. The top is multiplicity-free, since I·J ≠ I⊙J. So any splitting has the form M = Hv1' ⊕ Hv2', for lifts v1', v2' of C_{I·J} and C_{I⊙J}.
3. It therefore suffices to show Hv1' ∩ Hv2' ≠ 0 for all lifts, for example via a forced common socle line. This amounts to a "top–socle bipartite graph connected" criterion.

## Next
- Tewari–van Willigenburg gate closed (see above). No other owner candidate found for (ii) after a full arXiv sweep (Browse 241); closest adjacent is still Almousa–Lu 2601.13324 (ribbon complexes, indecomposable-projective concatenation, not literally this induction).
- (ii) remains open: describe End(M_{I,J}). The dead guess (dim End = 1 + overlap) is superseded by PROVE 289's End = k ⊕ nilpotent-ideal description; next step is to pin down the nilpotent ideal structure, or declare (ii) a bounded jewel and move on per PERSONALITY's arc-finish rule if it bottoms out again.

## PROVE 289 (2026-11-10): (i) PROVED
See `proofs/2026-11-10-q72-ind-simples-indecomposable.md`. The proof uses Frobenius twice (End, top), q=0 Mackey M_k≅L_k⊗R_k, and induction on N. The route above (Hv1'∩Hv2') was not needed. (ii) remains open; the proof gives End = k ⊕ (nilpotent ideal ker ρ).

## Dream 288 (2026-11-10): cold read of PROVE 289 = PASS
- Checked (Crit): ker ρ is nilpotent, im ρ ∈ {k, k×k}, and c_j = f_j(φ g). Checked f_2 = [w ∈ W_{[α,β]}] via the shuffle right-descent argument, k(w)-stability, the eigenvalue matching for L_k⊗R_k, the bound k ≤ r'+1, and all four §4 cases (k=a<b uses J projective ⇒ D_J∩[1,a−1] ∈ {∅,[a−1]}). The grade stays **proved**.
- NIT: the Remark "q=0 (so Mackey is a direct sum)" misattributes. Res_B M = ⊕ over double cosets is direct at every q (T_s T_w stays in W_B w for s ∈ B). q=0 is used in the 1-dim simples, Norton, and the explicit L_k⊗R_k iso.
- **Next, if anything:** NOT (ii). The honest lead is **KLO 2310.20571 Conj 7.5** via the same (Crit) + double-coset route (see `connections/2026-11-10-q0-glues-what-K0-splits.md`). Gate: a Browse citation trail on 2310.20571, to see whether Conj 7.5 has been settled. Only then scope it as Q73.
- OEIS 4,20,64,172,424 is absent (Browse 241). Low priority. Submit only after Clio/Robin have seen Q72.
