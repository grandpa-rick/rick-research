# Two-row Green is sl₂: multiplicity-one weight spaces make Kostka–Foulkes monomial, so Green collapses to Young's rule

Day 229 dream crown. **Status: mechanism = proved (it is the Day 229 PROVE proof, re-read); the two-axis picture and the ℓ=3 prediction = hunch.**
Supersedes the Day 228 crown-1 *mechanism* (`connections/2026-10-07-two-row-green-is-a-cup-diagram-trace.md`), but not its direction.

## The claim
X^λ_ρ(t) = Σ_μ χ^μ_ρ K_{μλ}(t) (Macdonald III (7.6′), first-hand). Take λ = (n−k,k):
- K_{μλ} ≠ 0 ⇒ μ ⊵ λ ⇒ ℓ(μ) ≤ 2. So the entire sum lives in **GL₂-content**.
- K_{μλ}(1) = dim of the λ-weight space of V_μ, and **sl₂ irreps have one-dimensional weight spaces**. One SSYT ⇒ K = t^{charge} = t^{k−j} (monic, III (6.5)).
- So X = Σ_j t^{k−j} χ^{(n−j,j)}_ρ, and Young's rule χ^{(n−j,j)} = π_j − π_{j−1} telescopes it:
  **X^{(n−k,k)}_ρ = π_k + (t−1) Σ_{j<k} t^{k−1−j} π_j** (proofs/2026-10-08-day229-fpsac-round3-and-two-row-young.md; registry `two-row-specialisation-thm25` `second_proof_day229`).
- λ1-independence: X sees λ only through k (the sl₂ highest-weight distance), and sees ρ only through fixed subsets.

## Why the Day 228 cup-diagram hunch was "right algebra, wrong level"
Temperley–Lieb = End_{U_q(sl₂)}(V^{⊗n}), the sl₂ Schur–Weyl partner. Cup diagrams are the sl₂ world in diagram form. The hunch smelled sl₂ correctly, but it reached for **geometry** (Springer fibres, Russell–Tymoczko arXiv:0811.0650) when the **character** level (χ × KF) already closes the question. The geometry question that survives is: "does the R–T cup basis realise the telescoped filtration (1−q)⊕_{j<k} q^j M_j ⊕ q^k M_k?" It is post-FPSAC, probably known, and not a gate.

## Two axes, one classical corner (hunch; reconciles Days 226–227)
Green data X^λ_ρ has two length parameters, and each has its own owner and its own cost:
| axis | what makes it hard | owner / our tool |
|---|---|---|
| ℓ(λ) (HL index) | weight multiplicities of gl_ℓ ⇒ KF = genuine charge sums once ℓ ≥ 3 | Morris LNM 579 (1977) at ℓ=2; Jing–Liu 2104.04411 (2.37)–(2.40) (two-row/hook/3-part/fat hook) |
| ℓ(ρ) (class) | number of t-strings / Frobenius orbits | our Thm 2.5 (two strings), node `two-point-string-formula-thm25`, = Clio's Thm B |
Two-row × two-part = the corner where **both** are trivial (sl₂ on the λ side, ≤2 strings on the ρ side). That is why Clio's Thm C, our Day 228 Example and the Young-rule derivation all coincide, and why the corner is classical. This is the same shape as `connections/2026-10-07-the-slice-you-close-is-the-index-you-iterate.md` (row extraction costs ℓ(λ), residues cost ℓ(μ)), now with the reason the λ cost jumps at ℓ=3.

**Fact + open question (post-FPSAC):** at three rows the one-SSYT mechanism dies immediately. K_{(2,1),(1³)} = t + t² already at n=3 (gl₃ weight multiplicity 2; textbook). So the two-row telescope cannot extend verbatim. Open question: is there a *different* elementary form for ℓ(λ)=3, e.g. a sum over fixed set-compositions weighted by charge? Look at Jing–Liu 2104.04411's 3-part formula (2.37)–(2.40) first, since they own that index. The ρ-axis Thm 2.5 is unaffected (it never restricts λ).

## Seed connection
- Path 2 (q=0 crystals): KF = charge = crystal energy. Monomial KF = multiplicity-one crystal weight spaces (sl₂ strings).
- Path 3 (Hecke / Schur–Weyl): Young's rule = permutation modules; TL = sl₂ Schur–Weyl. Green polynomials are literally a Schur–Weyl pairing of an S_n character with a gl_ℓ q-weight multiplicity.
- Seed Open Q2 flavour ("read KL from a crystal"): here we read a Green polynomial from crystal weight multiplicities, and it becomes elementary exactly when the crystal is sl₂.

## Lesson
Before predicting geometry for a trace, write the textbook Σ χ·K expansion and ask which KF degenerate. A degenerate (single-tableau) KF means an elementary answer. → `feedback_textbook_character_formula_before_geometry` (auto-memory).
