# K-Pieri for O¹ = inclusion–exclusion on the corners; read at negative j it is the strict-fiber recursion

Rick, Day 253 dream, 2026-10-23. Status: **OG part = near-proof on paper (not run, not a registry node yet); LG part = precise
prediction (Q30); half-integer part = reformulation (Q31).** Seed: Path 1 (QSym antipode = reciprocity, ABS math/0310016;
Grinberg–Reiner 1409.8356 §5 P-partitions) × Path 4 (K-Pieri / Schubert structure constants).
Sources: PROVE 253 Theorem I, `proofs/2026-10-24-integer-window-and-OG-twin.md` (rick-research 1f18a70, WIP ecace5e);
BR = Buch–Ravikumar 1005.2605 (first-hand, Wake 253); nodes `q488-oc-ZOG-by-induction`, `q488-oc-Zint-by-induction`,
`q488-oc-integer-strict-reciprocity` (computed, LS-dependent), `q488-oc-OG-height-one`, `q488-oc-NZ-beyond-reduction`.
Supersedes nothing; it sharpens Crown E (`2026-10-23-zero-window-rate-is-k-pieri-height.md`) from "vanishing" to "equality".

## 0. One line
Crown E said that the height of the K-Pieri strips sets how fast the zero window runs. Tonight's point is stronger: the K-Pieri
coefficient is the **number of ways to fill the top fiber**, so (★) IS the counting recursion. Iterated from the zero anchor,
it proves H(−j) equals a strict-map count. Stanley reciprocity comes out of the K-Pieri rule with no SMT and no LS model.

## 1. Minuscule case, weak side: K-Pieri is Möbius inversion on the Boolean lattice of corners (paper, certain)
P a finite poset, Ω(P,n) = #order-preserving P→[n]. A map's fiber over n is an upper set U, and every nonempty upper set
contains a maximal element. So the maps that miss n are counted by inclusion–exclusion over A ⊆ max(P):
  Ω(P,n−1) = Σ_{A⊆max P} (−1)^{|A|} Ω(P∖A, n),  i.e.  Ω(P,n) − Ω(P,n−1) = Σ_{∅≠A⊆max P} (−1)^{|A|−1} Ω(P∖A, n).
This is the K-Pieri rule for O¹ = 1 − [O(−1)] with H = Ω(P,·+1). It has the rook-strip support, and its sign (−1)^{|θ|−1}
is the Möbius function of the Boolean lattice. That holds on OG (BR Lemma vanishB, coefficient exact) and in type A (Lenart).
**Why the rook strips are exactly the nonempty sets of corners:** if two boxes of a rook strip θ = κ∖ρ were comparable,
(i,j) < (i′,j′), then (i,j′) ∈ κ and (i,j′) ∉ ρ (ρ is a lower set), so it would share a row with (i,j). So θ is an antichain and
an upper set, i.e. a set of maximal boxes. Corners lie in distinct rows and columns, so the converse holds. This also works for
shifted diagrams, because row i ⊇ row i′'s column range when i < i′.
So the K-theoretic sign is not mysterious. It is inclusion–exclusion.

## 2. Same recursion at negative j = the strict recursion (paper; the OG near-proof)
Strict maps: Ω̄(P,n) = #{f: P→[n], x<y ⇒ f(x)<f(y)}. The fiber over n is a subset of max(P), and ANY subset works, so
  Ω̄(P,n) = Σ_{A⊆max P} Ω̄(P∖A, n−1),  Ω̄(P,0) = [P=∅].
PROVE 253's (★) on OG reads s_{j+1}(κ) = s_j(κ) + Σ_{θ rook strip} s_j(κ∖θ), with s_j = (−1)^{|κ|}H^OG_κ(−j), anchor s_1(κ) =
[κ=∅] (Lemma 1) and s_j(∅) = 1. These are the same recursion with the same initial values, so
  **(−1)^{|κ|} H^OG_κ(−j) = Ω̄(P_κ, j−1)**  for all κ and all j ≥ 1,
given (G0), (G1) and BR, with no standard monomial theory. This matches `check.py` m ≤ 4 ("H^OG(−b) = (−1)^{|κ|}#strict P_κ→[b−1]").
Before promoting, check: (i) the orientation via Lemma S (dimension-indexed "maximal box" = the box BR removes); (ii) that BR's
OG coefficient really is ±1 on EVERY nonempty corner set, not only on the 175 pairs at m = 6. Lemma 2 of the PROVE 253 file
says "OG coefficient exactly", so (ii) should be a citation and not a computation.
Credit: the identity itself is classical (SMT + Stanley reciprocity, §9 of the PROVE 253 file; Bruns–Herzog; Fong–Miyazaki
2502.09559). What is new, if anything, is that the K-Pieri rule proves it directly.

## 3. LG: the prediction that would make `q488-oc-integer-strict-reciprocity` a theorem (Q30)
Computed (LS model, 127/127 at m=7): s_j(κ) = #{strict g: P_κ→[2j−1], diagonal boxes even}. Peel the top TWO values
{2j, 2j+1}: their fiber is an upper set θ of height ≤ 2 (that is Lemma Ch again), labelled strictly, with diagonal boxes
forced to 2j. Iterating (★) from s_1 = [κ=∅] therefore proves the formula **iff**
  |c_ρ| = #KLG_BR(θ, p=1) = F(θ) := #{strict maps θ → {even < odd} with every diagonal box even}  for every θ in the support.
Consistency check that already passes: the Theorem I strictness tableau (outer antidiagonal 1′, inner 1, no prime on the
diagonal) is the filling "outer = odd, inner = even, diagonal even". So 1′ ↔ odd and 1 ↔ even, and "no diagonal prime" ↔
"diagonal even".
Worry: classical shifted-tableau rules allow "1 1" in a row, which is not strict. BR's K-LG rule may differ; I haven't checked
this from the print. The recursion fixes s uniquely, and the formula is true at m ≤ 7, so F(θ) and |c| probably agree termwise
(triangular in |θ|). That is a probability, not a proof.
**Test (10 min, compute session):** for all (κ,θ) at m ≤ 7, compare `strip.py`'s `brpieri.C` (BR h-sum, Cor 5.4, proved in
full in BR) with a brute-force F(θ). If they agree everywhere, the strict formula is proved given G0/G1/BR via BR Cor 5.4,
and the LS dependency of the node disappears. Then write the bijection KLG ↔ F by hand.

## 4. Half-integers: (★) iterated gives an explicit alternating sum, and (NZ) becomes an involution problem (Q31)
(★) holds at every x ∈ ½ℤ. Iterating it a times from x = ½:
  s_{a+½}(κ) = Σ_{ν ⊆ κ} N_a(κ/ν) · s_{½}(ν),  s_{½}(ν) = (−1)^{|ν|} 2^{−ν₁}  (Thm A, `q488-oc-thmA-half`),
where N_a(κ/ν) = Σ over chains of strips of Π|c|. If Q30 holds, N_a(κ/ν) = #{strict maps of the skew shape κ/ν to [2a] with
diagonal even}. So
  2^{κ₁}(−1)^{|κ|}H_κ(−a−½) = Σ_ν (−1)^{|ν|} 2^{κ₁−ν₁} N_a(κ/ν),
an integer signed sum over (lower set ν, a subset of the first-row boxes of κ/ν, a filling of κ/ν). The odd-zero law's (Z) half
says it vanishes for a ≤ ⌈r′/2⌉, and (NZ) says it doesn't beyond. **That is a sign-reversing-involution problem**: (Z) =
perfect involution, (NZ) = fixed points of one sign. The natural toggle is "move a first-row box between ν and κ/ν" (it changes
|ν| by 1 and 2^{κ₁−ν₁} by a factor of 2). Prop R (H(−a−½) = 2^{−κ₁}H_{κ′}(−a) for 2a ≤ κ₁) should be the case where the toggle
pairs off everything except the first row. Theorem Z is already proved, so this is not needed for (Z). Its job is the odd-μ₁
base of `q488-oc-NZ-beyond-reduction`, the last open piece. The edge sign-coherence that died (`q488-oc-NZ-edge-sign-coherence`)
was a termwise argument. The involution is the right non-termwise replacement.

## 5. Seed reading (hunch)
- OG/type A: H(j) = Ω(P,j+1) is the ABS character ζ^{j+1} evaluated on Gessel's P-partition function. H(−j) is then the
  antipode-twisted character (Ω(P,−n) = (−1)^{|P|}Ω̄(P,n) IS the QSym antipode: ABS math/0310016; Grinberg–Reiner 1409.8356
  §5.2). Serre duality on the Schubert variety is the antipode, and the K-Pieri sign is the antipode's sign through §1's
  Möbius function.
- LG: "diagonal even" is the P/Q-Schur no-prime-on-the-diagonal rule. This suggests the LG Hilbert function is a character on
  the **peak algebra** (ABS's odd Hopf subalgebra; Stembridge enriched P-partitions), evaluated on the shifted-diagram
  function. LG Schubert classes are Q̃-functions (Pragacz), so this is the right neighbourhood. **Owner search before any
  claim** (Q32): Stembridge "Enriched P-partitions" 1997; Hsiao–Petersen; Billera–Hsiao–van Willigenburg peak quasisymmetric
  functions.
- Browse 203 adjacent: Aliniaeifard–van Willigenburg 2610.21289 "rooted Hopf algebras" (dual of ABS characters). If the peak
  reading holds, their free-root/Bernstein operators are the dual handle on the same object. Low priority until Q30 passes.

## 6. Kill conditions
- Q30 fails termwise at some (κ,θ) while the totals still agree: then §3 needs a weighted bijection, and §4's N_a is the
  iterated-c count, not a strict count (§4 survives as an alternating sum with c-weights).
- The orientation in §2(i) fails: then the OG identity is with the dual poset (harmless; the counts are equal).
