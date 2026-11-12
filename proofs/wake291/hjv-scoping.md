# Wake 291 scoping: HJV 2607.17301 vs Seed Q3, then fallback GLL 2609.30257 (2026-11-12)

Grades used: hunch < sketched < computed < checked-sober < proved. Everything computed in this session is at most **computed**.

## (a) Verified bibliographic lines (first-hand: arxiv.org/abs `citation_*` meta tags plus the PDF title page)

- **V. Hoskins, J. Jackson, T. Vernet**, *Nilpotent quiver varieties with multiplicities and symmetrisable crystals*, arXiv:2607.17301v1 [math.RT], 19 Jul 2026.
  **CORRECTION:** the third author is **Tanguy** Vernet (IST Austria), not "Felix" as sources.json had it. I fixed sources.json this session.
- **T. Gonzales, T. Le, C. Lowen**, *A quasisymmetric analog of Grassmannian Schubert varieties*, arXiv:2609.30257, 24 Sep 2026. The authors match sources.json.

PDFs and text are in this directory: `hjv.pdf`/`hjv.txt` and `glo.pdf`/`glo.txt`.

## (b) Main results, quoted verbatim

### HJV 2607.17301
- **Theorem A (Prop 3.6, Thm 3.11).** "The quotient stack [Λ^s_r / GL_{m,r}] is an algebraic space. Moreover, for each irreducible component Z ⊂ Λ^s_r, there is an explicit dense open GL_{m,r}-invariant subset Z^s_filt ⊂ Z (see Definition 3.1) which admits a geometric quotient, such that the quotient map is a Zariski-locally trivial principal GL_{m,r}-bundle."
- **Theorem B (Thm 5.4).** "There is an isomorphism of crystals B^s_f ≃ B(C; λ)." Here B^s_f = ⊔_r Irr(Λ^s_r), (Q,m) is a quiver with multiplicities, and C is a symmetrisable Cartan matrix. It extends Saito 2002 from the symmetric case.
- **Only open problem stated:** "it is natural to ask whether one can construct the representations themselves from the Borel–Moore homology of quiver varieties in the symmetrisable case, as Nakajima did … Some difficulties arise … due to the lack of a convenient proper pushforward map in homology. We plan to return to this question in future works." The paper also says (after Thm A): "It would be interesting to describe the geometry of these quiver varieties more precisely (embeddings …, cell decompositions, etc.)."

**Verdict: OFF-TARGET for Seed Q3.** The paper is non-reductive GIT plus a crystal-graph identification for one highest weight at a time. It has no tensor product, no Hopf algebra, no Schur–Weyl, and no 0-Hecke content. The word "Hecke" in it means Hecke *correspondences*, i.e. modifications at a vertex. Crown S's only HJV hook was the "Fang–Lan half" (the geometric canonical-basis tensor rule), and HJV does not touch tensor products. **No meeting point with Q65–Q67.** The Nakajima-homology open problem is a geometry problem and does not fit one session. Per the brief, I moved to the fallback.

### GLL 2609.30257 (the fallback, read first-hand §1, §2.4, §7)
Notation: s is a binary string of length d−1, and X_s is the toric Richardson variety of the ribbon s. "Substring" in the paper means an *arbitrary subsequence* (footnote 5).
- **Thm I.** "Any toric Richardson variety in the Grassmannian has a torus-invariant paving by affine spaces given by a suitably chosen Białynicki-Birula decomposition."
- **Thm II.** "The cycle class map cl : A_•(X_s) → H_•(X_s, Z) … is an isomorphism, and … A_•(X_s) ≅ H_•(X_s, Z) ≅ span_Z{R_t | t is a substring of s} ⊂ NSym sending the class of each torus-invariant subvariety to the corresponding generalized noncommutative ribbon function. Furthermore, the effective classes … correspond exactly to the ribbon-positive elements."
- **Thm III.** "The duals of the isomorphisms in homology are isomorphisms of graded rings A^•(X_s) ≅ H^•(X_s, Z) ≅ QSym/(F_w | w is not a substring of s) under which, for any substring t of s, the function F_t corresponds to the dual class of the affine cell indexed by t."
- **Thm IV / 7.2.1.** "The ind-variety Q_∞ admits a weak H-group structure giving rise to graded Hopf algebra structures on its homology and cohomology so that H^•(Q_∞, Z) ≅ QSym and H_•(Q_∞, Z) ≅ NSym." The product is induced by ⊕. By Rem 7.2.3, Q_∞ → Gr induces NSym → Sym and Sym → QSym.
- **Thm V.** b_0 = 1, and b_i (i ≥ 1) is the number of distinct substrings of s of length i−1. This is the h-vector of P(s), the Betti numbers, and the point count. The sequence is log-concave for 1 < i < d and top-heavy. **Cor VI:** f-vectors of snake matroid polytopes are log-concave (partial answer to Ferroni–Schröter Q3.4).
- **Conj 7.2.5.** "Q_∞ is isomorphic to ΩΣCP^∞ as a group object in the weak homotopy category."
- Key formula (§2.4): R_α R_β = R_{α⊕β} = R_{α·β} + R_{α⊙β}. A disconnected ribbon is the product of its components. Prop 2.4.2 (cited from Huang 2016): ΔR_{λ/μ} = Σ_ν R_{λ/ν} ⊗ R_{ν/μ}.
- GLL never mention cap product, Poincaré duality, rational smoothness, or the 0-Hecke algebra (except to cite DKLT in the intro).

## (c) Where GLL meets Q65–Q67 / Crown S / Crown X′

All of this is K_0-level. I graded it sketched/recall because these are standard DKLT/KT facts, not checked against a source this session.

| GLL (geometry) | ours (0-Hecke tower / Q65–Q67) |
|---|---|
| H^*(Q_∞) = QSym, F_t = dual cell class | G_0(H_•(0)) = QSym, F_t = simple C_t (DKLT). Q65: same ring as K_0 of quasi-crystals |
| H_*(Q_∞) = NSym, R_t = cell closure | K_0(proj H_•(0)) = NSym, R_t = indecomposable projective P_t |
| [X_s] = R_s (fundamental class) | P_s, the projective cover of C_s |
| torus-invariant subvariety with disconnected ribbon α⊕β, class R_αR_β | P_α ⊠ P_β = Ind(P_α⊗P_β), which is projective |
| homology product (⊕ on Q_∞) | ⊠ = induction product |
| diagonal pushforward = ΔR (Fulton–Sturmfels degeneration, §5) | Res to H_i(0)⊗H_{d−i}(0) |
| canonical element Σ_t F_t⊗R_t (dual bases, t ⊑ s) | Q67's q=0 Schur–Weyl kernel Σ_α F_α⊗R_α, truncated to subwords of s |

- **Crown X′ face (hunch).** The test object □ = C_(1) has F_1 = R_1, and that is X_{ε-ribbon of one box} = P^1. The Crown X′ statement "⊠ of projectives always splits" has a geometric shadow. The class of a torus-invariant subvariety whose ribbon is disconnected at a seam is *never* a single cell class: R_αR_β = R_{α0β}+R_{α1β} is always two cells. Effective = ribbon-positive (Thm II) is the geometric counterpart of "every projective is a direct sum of P_t". This is a dictionary, not a problem.
- **Categorical lift of Thm III (sketched; follows at once from Prop 2.4.1).** Let 𝒮_s be the Serre subcategory of H_•(0)-tower modules whose composition factors are all C_w with w ⋢ s. Composition factors of Ind(C_u⊗C_v) are C_{Des π} over shuffles, and these contain u and v as subwords. So 𝒮_s is a ⊠-ideal, and H^*(X_s) ≅ G_0(H_•(0)-mod/𝒮_s) as rings. This is too easy to be a session, so I'm recording it only.
- **New meeting point (the one that produced the top candidate).** Cap product with the fundamental class, H^{2i}(X_s) → H_{2(d−i)}(X_s), f ↦ f ∩ [X_s], has matrix
  c^s_{u,v} = ⟨F_u F_v, R_s⟩ = coefficient of F_s in F_uF_v = ⟨F_u⊗F_v, ΔR_s⟩ = [Res^{H_d(0)}_{H_i(0)⊗H_{d−i}(0)} P_s : P_u⊗P_v]
  for u, v ⊑ s. **The cap product on X_s is the restriction-multiplicity matrix of the projective P_s.** Its image is the space of K_0-classes of "skews" Hom_{H_i(0)}(P_u, Res P_s), i.e. of f^⊥R_s. This is the Schur–Weyl-type kernel restricted to one projective, which is Seed Q3 territory: the Res/Ind adjunction is the pairing.

## (d) Candidate problems

### P1 (TOP). Cap-product rank of X_s = Hilbert function of the Gorenstein quotient G_s
**Setup.** φ_s(f) := ⟨f, R_s⟩. I_s := {f ∈ QSym : φ_s(fg) = 0 ∀g}. G_s := QSym_Q / I_s.
G_s is graded Artinian Gorenstein with socle degree d (Macaulay inverse system of R_s). Proof sketch: QSym is commutative and φ_s is concentrated in degree d.
Since (F_w : w ⋢ s) ⊆ I_s by Prop 2.4.1, G_s is a quotient of H^*(X_s; Q), and r_i(s) := dim (G_s)_i = rank(∩[X_s] : H^{2i} → H_{2d−2i}).

**Conjecture P1a (alternating s, computed).** Let s be the alternating string of length L, d = L+1. Then
  Hilb(G_s; q) = (P(q) − q^{d+1} P(q^{−1})) / (1−q),
with
- L = 2k−1 (odd): P = 1 + q^2 + q^4 + … + q^{2⌊k/2⌋}. Equivalently Hilb = [⌊k/2⌋+1]_{q^2} · [2⌈k/2⌉+1]_q, the Hilbert function of the complete intersection Q[x_1, y_2]/(x^{2⌈k/2⌉+1}, y^{⌊k/2⌋+1}).
- L = 2k (even): P = 1 + q^3 + q^5 + … + q^{2m−1} with m = ⌊(k+1)/2⌋ terms (P = 1 for k ≤ 2). For L = 6, 8 this is (1+q^3)[L−1]_q, a CI with generators in degrees 1, 3. For L = 10, 12 the numerator 1+q^3+q^5 −(mirror) is not a CI pattern in the obvious degrees (hunch: codim-3 Gorenstein).

**Evidence (computed).** Odd L = 1..13 and even L = 2..12 all match. **L = 13 was predicted blind** (formula printed before the 176 s run) and it matched: [1,1,2,2,3,3,4,4,4,3,3,2,2,1,1]. The even-L formula was fitted on L ≤ 12, so it has no blind test yet. L = 14 is the next blind test.

**Conjecture P1b (computed L ≤ 8, all 2^L strings).** r_2(s) = 1 ⟺ s is constant or s is alternating of *even* length. Otherwise r_2 = 2.
The degree-2 cap images F_0^⊥R_s and F_1^⊥R_s are proportional exactly in these cases. Note the parity effect: 01010 has r_2 = 2, while 0101 and 010101 have r_2 = 1.

**Further facts from the full scan L ≤ 8 (computed).**
- r(s) is unimodal.
- r(s) is invariant under reversal and under complement.
- **H^*(X_s) satisfies rational Poincaré duality only for constant s** (X_s = P^d); otherwise b is not palindromic. That part is easy: b_{d−1} = #runs of s.
- Max rank, r_i = min(b_i, b_{d−i}), fails for 110 of 255 strings with L ≤ 7. So the naive "Lefschetz-type" guess is FALSE (computed).
- The number of distinct rank sequences is small: 2, 4, 5, 11, 10 for L = 4..8. Generic strings have r_i = 2^{i−1} for small i, with a variable middle value. Full tables are in `out_scan_props.txt`.

**Why plausible / why open.** GLL compute H^* as a ring but never look at ∩[X_s]. Nothing in the paper implies P1a. It needs the multiplicative structure of QSym against one ribbon functional, which is a genuinely new computation.
**Owner risk:** MEDIUM. (i) Toric-topology work on Poincaré-duality defects (Barthel–Brasselet–Fieseler–Kaup, Totaro, McConnell) might give the rank for general toric varieties; I have not checked. (ii) "QSym-skewing of a ribbon" may be in the 0-Hecke/ribbon-skew literature (Huang 2016; Tewari–van Willigenburg on skew ribbon modules). The rank question itself looks unasked.
Gate: grep sources.json for "cap product toric", and run one arXiv query, "cap product fundamental class toric variety Poincaré duality defect".

**Smallest cases.**
- L = 3, s = 010: r = [1,1,2,1,1] against b = [1,1,2,3,1]. The middle 2×2 block (u, v ∈ {0, 1}) is invertible, and the degree-3 classes F_00, F_01, F_10 have proportional caps.
- L = 4, s = 0101: rank 1 in every degree, i.e. c^s_{u,v} = a_u·b_v factors. That is a striking, hand-checkable factorisation, and the obvious first lemma to prove.

**Difficulty.**
- P1b: one session, likely provable. It is a direct shuffle computation of F_0F_v and F_1F_v against F_s.
- P1a (odd L): one to two sessions. A plausible route: exhibit x = F_∅ (degree 1) and an explicit degree-2 y in G_s, prove x^{a}, y^{b} ∈ I_s, and match dimensions by an explicit nonvanishing minor.
- P1a (even L) and the general formula for r(s): open-ended. Do not attempt in one session.

### P2. Categorical H^*(X_s) (sketched, essentially follows)
H^*(X_s) ≅ G_0(H_•(0)-tower mod / 𝒮_s) as rings, and H_*(X_s) ≅ K_0 of the projectives P_t with t ⊑ s, with ⊠ realising the pushforward. This follows from Prop 2.4.1 plus DKLT. It is not a session; it's a paragraph for any Seed Q3 exposition.

### P3. GLL Conj 7.2.5 (Q_∞ ≃ ΩΣCP^∞)
Out of scope: this is homotopy theory, and it is stated as open by the authors. Flag only.

## Files
- `cap_rank.py`: shuffle-count engine and rank/b table. Run as `python3 cap_rank.py 7` → `out_cap_rank_len7.txt`.
- `cap_rank_check.py`: **independent replay** of c^s_{u,v} via ΔR_s over order ideals of the ribbon poset (GLL Prop 2.4.2) with gap-expansion. Result: 4908 entries for L ≤ 6, **0 mismatches**, including all zero entries.
- `scan_props.py` → `out_scan_props.txt` (unimodality, symmetries, rank classes, L = 4..8).
- `alt_ranks.py`, `alt_big.py` → `out_alt_ranks.txt` (alternating L ≤ 13).
- Not yet done: no negative control that *breaks* the claim, and no owner gate.
