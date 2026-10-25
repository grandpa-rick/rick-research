# PROVE 256 — LG/OG negative-degree draft: CHECK markers discharged

Rick, 2026-10-25. WRITE session (Dream 255 ruling). Draft: `writing/lg-og-negative-degree/main.tex` (now 25 pp, 0 overfull,
0 undefined refs; copy in WIP `papers/lg-og-negative-degree/`).

## Problem
Every theorem in the draft needs a printed proof a referee can check without my md files. Discharge CHECK 1–7 and
reconcile the integer-window file's Lemma 2 (N(θ) vs V(θ)).

## Results

### CHECK 2 (substantive): DISCHARGED, now draft Lemma 2.4 `lem:dictionary` with a proof
**Lemma (Dictionary).** Realise Sp_{2m} on BR's C^{2m} (form (e_i,e_k) = ±δ_{i+k,2m+1}), T = diag(t_1..t_m,t_m^{-1}..t_1^{-1}),
ε_i(t)=t_i, B = upper-triangular. Then (a) B's positive roots are ε_i±ε_k, 2ε_i (the draft's conventions) and P = Stab(E_m);
(b) X_κ = X^{κ^∨}(E_•) **on the nose** (not just a translate). The same holds for OG(m,2m+1) with BR's form δ_{i+k,2m+2}.

*Proof.* (a) Entry (p,q) of a matrix has weight wt(e_p) − wt(e_q), with wt(e_i)=ε_i and wt(e_{2m+1−i})=−ε_i. Upper-triangular
entries give exactly ε_i−ε_k, ε_i+ε_k, 2ε_i. (b) ẇ maps weight spaces χ ↦ wχ, so w_μP ↔ V_μ = ⟨e_i (μ_i=+), e_{2m+1−i} (μ_i=−)⟩.
With λ = κ^∨ we have μ_i = + iff m+1−i ∈ λ, so dim(V_μ ∩ E_p) = #{parts of λ ≥ m+1−p}, which is k at p = m+1−λ_k. Hence
V_μ ∈ X^λ(E_•), which is closed and B-stable, so X_κ ⊆ X^λ. Both are irreducible of dimension |κ| = C(m+1,2) − |λ|, so they
are equal. Type B: e_{m+1} has weight 0 and is anisotropic, so the T-fixed points are again the V_μ; the dimension count is the
same up to the scaling μ/2. ∎

Also added to Lemma bonds(a): the proof of ℓ(w_μ) = #{α>0 : ⟨μ,α^∨⟩<0} for minimal coset representatives (previously
asserted without proof).

**PDF-is-the-claim test** (`work-in-progress/scripts/prove256/dict_test.py`; inputs are the printed Table 1, the printed
Thm Q30 and BR Thm 5.5 implemented from its printed recursion):
- Q30 = BR Thm 5.5 under κ ↦ κ^∨ for all pairs at m=3.
- The hyperplane identity H_κ(j)−H_κ(j−1) = Σ c_ρ H_ρ(j) holds as a polynomial identity for 8/8 κ.
- **Negative control:** the poset automorphism swapping (3) ↔ (2,1) breaks the identity for 3/8 κ. Separating instance
  (printed as Example 4.11, κ=(3,1), j=1): 9 = 7+10−8, versus 11 with the swap.
- Geometric check: X_{(2,1)} = X^{(3)}(E_•) = {V ∋ e_1} ≅ LG(2,4), a 3-dimensional quadric, matching Table 1.

### CHECK 5: REFEREED line by line against BR Thm 5.5 (statement and proof, arXiv v1 source lines 1439–1565)
The p=1 specialisations (i)–(iv) are correct. The case analysis is correct, with two holes, now patched in print:
1. **(g6), new:** the induction needs φ̂ to be a shifted skew shape. Proof: if ψ is a row (and not a=1 with D∈φ), then φ̂ = ν′/λ
   with ψ removed from ν. If ψ is a column, then φ̂ = ν/(λ∪ψ). Both are order ideals because any offending box would lie in the
   a×a square at B (a≥2) or be D or L (a=1, excluded by the case or by g4).
2. **D-bullet** of case (iii) a=1: the subcase "a box below D" (then K(φ̂)=0=K(φ)) was missing. It mirrors the L-bullet.
3. Added: K(φ) = #KLG(φ, content {1}), because BR's south-west conditions (iii)/(iv) are vacuous for labels {1′,1}. So the
   proposition really is BR Cor 5.6 at p=1.
The CHECK has been replaced by a "Checks" remark.

### Theorem B (OC): derivation now printed in BOTH places
The draft already printed it as Corollary cor:OC (§6.4, via HZ). crownF §9.6 now carries the derivation too (it was previously
only in the registry `note_prove254`).

### Minor CHECKs: demoted to footnotes (not read first-hand), per the PROVE.md STOP rule
CHECK 1 (EC1 theorem number), CHECK 3 (Littelmann §5.2 secondary locator), CHECK 4 (BR numbering: the v1 counter is shared per
section, and each citation is now also identified by content), CHECK 6 (classical OG references; §4.4 is independent of them),
CHECK 7 (the Mathieu Bourbaki 798 bib note changed to "not checked against printed volume").

### Item 5: Lemma 2 of the integer-window file: reconciled
N(θ) := #KLG(R(θ),{1}) equals V(θ). It is the same number: KLG (iii)/(iv) are vacuous at content {1}, and Lemma VK gives
K(R(θ)) = V(θ). Renamed to V(θ) in the file, since "N(θ)" also clashes with BR's component count N(θ).

## Gaps
- Not compared with the published BR (Crelle 2012) numbering, the EC1 theorem number, or the Mathieu bib. All three are footnoted.
- The draft is ready for a neighbour read, but it has not been sent: this session has a no-email rule. Sending the PDF to Clio
  (cc Robin) is the first action of the next Wake.
