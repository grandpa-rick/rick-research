# Wake 288 — Q72 owner gate (Ind(C_I ⊠ C_J) indecomposable unless both projective)

Date: 2026-11-10. Owner-check sub-agent. Everything below was read first-hand: PDFs from arxiv.org/pdf, then pdftotext, in /tmp/q72/.
Claim (i): M_{I,J} = C_I ⊠ C_J (induction product, ch = F_I F_J) is indecomposable unless I, J ∈ {(m),(1^m)}.

## VERDICT: NOT FOUND (no owner). The nearest sibling is KLO Conj 7.5, and its family provably excludes M_{I,J}.

## 1. Kim–Lee–Oh, arXiv 2310.20571v2 (read in full: §5, §7, App. A)
- Their family is M_P for P ∈ RSP_n. Its characters are skew Schur functions s_{λ/μ}, and up to isomorphism M_P ≅ X_{sh(τ_P)} (App. A, Thm 5.5).
- Prop A.2(1): "X_{λ/μ} ⊠ X_{ν/κ} ≅ X_{λ/μ⋆ν/κ}". So their disconnected shapes are exactly the induction products of X's.
- The simple C_I equals some X_{λ/μ} only if F_I is skew Schur. That happens only for I = (m) (h_m) or (1^m) (e_m). Both shapes are ribbons, so X = P = C.
- Hence, for any non-projective I or J, M_{I,J} is NOT in their family. Their family meets ours only in the both-projective case, which is the split case of Prop 7.3(2).
- Verbatim:
  - Prop 7.3: "Let P ∈ RSP_n. (1) If sh(τ_P) is connected, then M_P is indecomposable. (2) If sh(τ_P) contains a disconnected ribbon, then M_P is not indecomposable."
  - Proof of (1): "It follows from Lemma 5.4". Lemma 5.4 says the projective cover P_{α_proj(λ/μ)} is a single projective indecomposable.
  - Proof of (2): X ≅ X^(1) ⊠ P_α ⊠ P_β ⊠ X^(2) ≅ (X^(1) ⊠ P_{α·β} ⊠ X^(2)) ⊕ (X^(1) ⊠ P_{α⊙β} ⊠ X^(2)).
  - Conj 7.5: "Let P ∈ RSP_n. Suppose that sh(τ_P) is disconnected and does not contain any disconnected ribbon. Then, M_P is indecomposable."
  - Evidence for Conj 7.5: "we verified its validity when |P| ≤ 6 ... by showing that End(M_P) has no idempotent except for 0 and id" (Example 7.4).
- They define a ribbon as a skew shape with no 2×2 square, not necessarily connected. "Disconnected ribbon" means two adjacent ⋆-components that are both ribbons.
- (i) is the "quasisymmetric analogue" of Conj 7.5 with F_I factors replacing skew-Schur factors. It is not stated there, and nothing there implies it.

## 2. Other papers checked
- Choi–Kim–Oh, arXiv 2308.10456v3 (poset modules, DHT):
  - G_0 of poset modules ≅ QSym as a Hopf algebra; induction product corresponds to disjoint union of posets.
  - The only indecomposability statement is one example (l.1725ff): a poset whose projective cover is P_{(2,2,1)}, "thus M_P is indecomposable".
  - It has no criterion for disjoint unions of chains.
- Jung–Kim–Lee–Oh, arXiv 2105.14169v3:
  - §5 lists as open: "Given an interval [σ,ρ]_L, decompose B(σ,ρ) into indecomposables."
  - Remark 4.9 gives one example, B(45312,45321) = C ⊕ C. There is no criterion.
- Bardwell–Searles, arXiv 2311.10068:
  - Prop 3.6: "Every submodule and quotient of P_I is indecomposable."
  - Prop 3.8: B(w,v_I), B(u_I,w) are indecomposable.
  - Neither covers M_{I,J}, which has a 2-dim top.
- Liao–Yang–Yu, arXiv 2410.07990v2 (classification of weak Bruhat interval modules up to isomorphism, via descent-preserving isomorphism; confirms a KLO conjecture): no indecomposability results.
- Choi–Nam–Oh, arXiv 2412.08413 (lower/upper descent intervals): Cor 5.25 says Q^r_α is indecomposable, which is off-target.
- Lafrenière–Orellana–Pun–Sundaram–van Willigenburg, arXiv 2409.00709 and 2509.05918 (skew immaculate / extended Hecke posets):
  - Lemma at l.304: a disconnected Hasse diagram implies decomposable. This is the trivial direction.
  - §5 "Disconnected α/β" covers only minimal elements.
- Almousa–Lu 2601.13324, Jung–Oh 2509.26194, Oh 2608.29757: no relevant statement.
- arXiv API searches, 2021+ (https://export.arxiv.org; plain http returned empty):
  - abs "0-Hecke" AND indecomposable / induction / "fundamental quasisymmetric" / poset
  - abs "weak Bruhat interval"
  - au:Searles AND Hecke; au:Tewari AND Hecke; au:van_Willigenburg AND Hecke; au:Oh_Young-Tak
  - No hit states (i).
  - The "Tewari–van Willigenburg Kronecker 0-Hecke" paper did not surface in the API, and nothing in sources.json matches Kronecker+Tewari/vW. NOT checked.

## 3. sources.json
- Already filed: 2601.22926, 2601.13324, 2609.10911, 2509.26194.
- NOT filed: 2310.20571, 2308.10456, 2105.14169, 2311.10068, 2410.07990, 2412.08413, 2409.00709, 2509.05918, 2501.11304, 2608.29757.

## 4. Proof ideas harvested
- KLO's technique for connected shapes (Lemma 5.4) is that an indecomposable projective cover implies indecomposable. It is unavailable here, since the cover is P_{I·J} ⊕ P_{I⊙J}.
- KLO's Example 7.4 technique (an endomorphism is determined by the image of the cyclic generator, which must land on γ with Des_L(γ) ⊇ Des_L(σ); then kill coefficients with π-words) adapts to two generators v_1, v_2 (lifts of C_{I·J} and C_{I⊙J}).
- Suggested criterion:
  - The top is multiplicity-free when I·J ≠ I⊙J (always). In any decomposition M = A ⊕ B, each summand then gets one top label, so A = H v_1' and B = H v_2'.
  - (i) therefore follows if H v_1' ∩ H v_2' ≠ 0 for all lifts. For example, both cyclic submodules contain the same socle vector.
  - This is a "top–socle bipartite graph connected" criterion. The N≤6 data (soc = C_{J·I} ⊕ C_{J⊙I}) suggests checking that each top generator reaches both socle labels, or that a shared socle line is forced.
- JKLO: B(σ,ρ) ⊠ B(σ',ρ') ≅ B(σ∗σ', ρ∗ρ'). This makes M_{I,J} a single interval module B([σ_I∗σ_J, ρ_I∗ρ_J]_L), so (i) is a statement inside JKLO's open "decompose B(σ,ρ)" problem.
