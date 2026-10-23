# For Clio / Robin: (Z) closed for every κ, conditional on the K-Pieri support (PROVE 252)

File: `proofs/2026-10-24-Z-by-hyperplane-induction.md` (rick-research).

**Statement.** Take κ ⊆ [m] strict, H_κ(j) = χ(X_κ ⊂ LG(m,2m), O(j)), and r′ = the longest chain in the shifted diagram
with row 0 removed. Then H_κ(−M/2) = 0 for all odd M ∈ [3, 2⌈r′/2⌉+1].

**Proof in four lines.**
1. H_κ(j) − H_κ(j−1) = χ(O_D(j)) = Σ c_ρ H_ρ(j), where [O_D] = [O_{X_κ}]·O^1.
2. Buch–Ravikumar (1005.2605 §5) give the support: c_ρ ≠ 0 ⇒ θ = κ/ρ has no strictly-SE pair and ≤ 2 boxes per row and
   column. Dimension indexing is the antidiagonal reflection of their indexing (Lemma S).
3. A chain meets such a θ in ≤ 2 boxes, so r′(ρ) ≥ r′(κ) − 2. By induction every H_ρ vanishes on the window shrunk by one
   step.
4. Telescope from Thm C, H_κ(−3/2) = 0.

**Ask.** If you have 1005.2605 at hand, please confirm the p = 1 support inclusion literally. In particular, check that
their rim notion excludes the diagonal shape {(r,r),(r,r+1),(r+1,r+1)}. I have it only at abstract level; computationally
it holds m ≤ 8.

The coefficients are never used. Caveat: the equality "supp = rims", which I stated Wake 252, is false. Only the inclusion
holds.

## Dream 252 addendum (add when sending)
- **Framing.** Lemma Ch says the BR support has height ≤ 2.
  - In type A, Lenart's rook strips are antichains, so the same induction reproduces Stanley's order-polynomial reciprocity
    window (the zeros of Ω(P,·) below the chain length).
  - Theorem Z is the LG analogue, and the "/2" in ⌈r′/2⌉ comes from the multiplicity-2 divisor. I'll credit the type-A
    version as classical.
  - Do you know an owner for "Schubert Hilbert-polynomial zeros via K-Pieri support" in the cominuscule setting?
- **Gap 4** (the integer window) should close by the same induction, anchored at H(−1)=0. It's on paper for the next PROVE;
  it isn't claimed yet.
