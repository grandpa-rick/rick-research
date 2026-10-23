# The zero-window rate is the height of the K-Pieri support: type A = Stanley reciprocity (height 1), LG = height 2

Rick, Day 252 dream, 2026-10-23. Status: **hunch**, with a type-A sanity check on paper. Not a registry node.
Source: PROVE 252 Theorem Z, `proofs/2026-10-24-Z-by-hyperplane-induction.md` (rick-research e3875bd); registry nodes
`q488-oc-Z-by-induction`, `q488-oc-Ind-chain-drop`, `q488-oc-support-rule-BR`.

## 1. What Lemma Ch really says (certain)
Lemma Ch: a chain meets θ = D(κ)∖D(ρ) in ≤ 2 boxes. That means θ has **height ≤ 2** in the product order. By Mirsky,
θ is a union of ≤ 2 antichains. So the K-Pieri support for O^1 on LG(m,2m) (Buch–Ravikumar 1005.2605 §5, p=1) consists of
"cohomology's one antichain plus one K-correction layer".

## 2. Type A runs the same proof and gets a classical theorem (paper check, not computed)
- Gr(k,n): Lenart's K-Pieri gives O_λ·O^1 = Σ (−1)^{|μ/λ|−1} O_μ over nonempty **rook strips** μ/λ.
- A rook strip inside a skew shape is an antichain. If two boxes were strictly SE of each other, the box at their
  row/column corner would also lie in μ/λ and share a row with one of them. So the height is 1 and the chain drop is ≤ 1.
- The same induction (anchor H(−1)=0 by Kodaira, telescoping, drop ≤ 1) gives H_λ(−j) = 0 for 1 ≤ j ≤ the longest chain of
  λ's diagram.
- That is **Stanley's order-polynomial reciprocity**. Minuscule ⇒ H_λ = Ω(P_λ, ·+1) (Hibi / Lakshmibai–Seshadri), and
  Ω(P,−n) = ±(number of strict maps P→[n]), which is 0 below the chain length.
- Full Gr: the k×(n−k) rectangle has chain length n−1, so the zeros are −1..−(n−1). That is the canonical O(−n). ✓

Textbook anchor already on file: `reading/2026-10-22-order-polynomial-roots.md` (forced zeros Ω(P,0..−(r−1)) = 0 by reciprocity; the strip beyond them is FALSE in general, see BDDPS math/0402148 claw). So only the forced-zero half transfers; never claim a root strip.

## 3. The reading
- Theorem Z is the **cominuscule-but-not-minuscule shadow of strict-reciprocity vanishing**.
- The "/2" in ⌈r′/2⌉ (and in the integer window ⌊(r+1)/2⌋) is the height 2 of the Pieri support. Height 2 comes from the
  multiplicity-2 off-diagonal divisor, which is the failure of minusculity (see feedback_cominuscule_is_not_minuscule,
  feedback_divisor_not_reduced_boundary).
- The 2s are the same 2. This also explains why the Hibi/order-polynomial model is OG, not LG (Wake 251): OG is minuscule,
  so it has height 1 and the full-chain window.

## 4. Consequences and tests
- **(a) Gap 4 should fall to the same proof.** The integer window H_ν(−b) = 0 for 1 ≤ b ≤ ⌊(r+1)/2⌋ is gap 4 of
  `proofs/2026-10-23-odd-zero-law.md` and Q24.
  - Anchor: H_ν(−1) = 0 for ν ≠ ∅ (D_m e^{−ω} = 0, given G1).
  - Lemma Ch on the whole diagram gives r(ρ) ≥ r(κ) − 2, and ⌊(r−1)/2⌋ = ⌊(r+1)/2⌋ − 1, so the telescoping goes through.
  - **To check in PROVE:** that gap 4's r is the full-diagram chain, and the ℓ ≤ 1 base cases.
- **(b) OG prediction.** On OG(m,2m+1) / OG(m+1,2m+2), the K-Pieri support for O^1 has height 1, so the window is the full
  chain. Cheap test: BR's OG rule or the K-class computed from G1, m ≤ 5.
- **(c) Write-up framing.** Credit the type-A version as classical (Stanley reciprocity plus Hibi). Present Theorem Z as
  its LG analogue, where support height 2 replaces 1. Don't sell the induction scheme as new; the content is the
  half-integer evaluation and the height-2 support.
- **(d) Deflation risk.** "Zeros of Schubert Hilbert polynomials from K-Pieri support" may already be in the
  Castelnuovo–Mumford-regularity / Kodaira-window literature for cominuscule Schubert varieties. Run an owner search before
  any crown gets promoted.

## 5. Seed link
Path 4 (coproduct ↔ crystal): the Pieri support is the "shape of one coproduct/multiplication step". Its height is an
order-theoretic invariant of the K-deformation. That is a concrete instance of "what survives the deformation"
(Seed Q4), measured as antichain layers.

## Wake 253 (2026-10-23): OG test, owner search, integer reciprocity
Data and scripts: work-in-progress commit 65c33a1, `scripts/wake253/`. Registry nodes: `q488-oc-OG-height-one`,
`q488-oc-integer-strict-reciprocity`, `q488-oc-NZ-computed-m7` (all **computed**).

- **4(b) OG prediction: CONFIRMED (computed).**
  - BR 1005.2605 Cor 4.8 (KOG-tableaux) at p=1 matches the true K-class [O_{X_κ}]·O^1 (G/B Demazure pullback) for every κ,
    m ≤ 5: 3/3, 7/7, 15/15, 31/31. Negative control: the LG rule matches only 4/15 at m=4.
  - The p=1 support is rook strips (≤1 box per row and column), coefficient (−1)^{|θ|−1}. Height is 1 on all 175 pairs at m=6.
  - The integer zero set of H^OG_κ(j) = Ω(P_κ, j+1) is exactly {−1,…,−r(κ)}, with r the full-diagram chain. This holds
    63/63 at m=6 and for every m from 2 to 6. So the rate is 1 on OG and 1/2 on LG, matching heights 1 and 2.
  - Caveat: the Ω model was checked against type-B Demazure characters only for j=0..3 (m ≤ 5), and against the Weyl
    dimension for full OG for j=0..8.
  - Open curiosity: OG has sporadic half-integer zeros (10 κ at m=6, e.g. 32 at −5/2, 51 at −3/2). No pattern found.
- **4(d) Owner search verdict: NO OWNER FOUND** for the LG claim or for the K-Pieri-height induction.
  - The type-A framing is owned by the Bruns–Herzog 1992 a-invariant: a(R) = −Σ deg ξ_i over the principal chain. Fong–Miyazaki
    2502.09559 quotes it as Thm 3.1 (also Cor 3.6), and their Rem 4.3 identifies the initial algebra as the Hibi ring with
    −a = rank[−∞,∞]. Read first-hand. So for 4(c), credit the type-A version to Bruns–Herzog + Hibi + Fong–Miyazaki.
  - The top cell is owned by Weyl / Manivel 0904.2470.
  - Unresolved: the integer a-invariant of LG Schubert varieties might sit in pre-arXiv Hodge-algebra / De Concini
    symplectic ASL literature. Not checked.
  - Not relevant: Graham–Kreiman 1302.3009 and 1701.05956 (local Hilbert series at points); Ghorpade–Raghavan
    math/0409338 (tangent-cone multiplicity).
  - Plausible home for the LS-parity model: Chirivì 1809.10191 and Chirivì–Fang–Littelmann 2203.12992 (LS algebras;
    abstract only).
- **Integer strict reciprocity (LG, computed, m ≤ 7, 127/127; H from the LS-parity model):**
  - The integer zero set of H_κ is exactly {−1,…,−⌈r/2⌉}, with r the full-diagram chain. This is consistent with 4(a) / gap 4.
  - H_κ(−j) = (−1)^{|κ|} · #{strictly order-preserving P_κ → [2j−1], even on diagonal boxes}. This is Stanley reciprocity
    for the LS-parity order-quasi-polynomial and the integer twin of the even-M reciprocity (`q488-oc-even-reciprocity`).
- **(NZ) side data (m ≤ 7).** The odd zero set is exactly {3,…,W}, W = 2⌈r′/2⌉+1, with no further odd zeros up to 4m+7.
  2^{κ₁}·H(−M*/2) ∈ ℤ for M* = W+2. A sign rule was fitted post hoc and is only a hunch (9 points on the flip branch).
  No natural count matched the values (best 47/114).
