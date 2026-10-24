# Crown G (Dream 254): LG's diagonal parity is a marked alphabet, and the models fall out of reciprocity

> The integer step on LG factors as odd-layer × even-layer (A_oA_e = I+C, PROVE 254 Lemma 9.1). Read the odd values as
> primed letters and the even ones as unprimed letters. Then "diagonal even" is the shifted-tableau rule "no primes on the
> diagonal". The LG Hilbert function at negative degree counts strict marked fillings, and the half-integer twist is
> half a letter.

Inputs: `proofs/2026-10-25-crownF-strict-reciprocity.md` (PROVE 254; §4 SR_LG, §5 SR_OG, §9 Theorem HZ), registry
`proofs/registry/q488-converse.json`. Predecessors: Crown E (`2026-10-23-zero-window-rate-is-k-pieri-height.md`, now a theorem),
Crown F (`2026-10-23-kpieri-is-inclusion-exclusion-on-corners.md`, now Theorems Q30/SR, proved).

## 1. The dictionary (proved part = Lemma 9.1; identification with Stembridge = HUNCH)
- PROVE 254 Lemma 9.1: (A_oA_e)^{a−1}A_o counts strict order-preserving maps D(κ)∖D(ν) → [2a−1] with even diagonal. Odd
  value layers are antichains avoiding the diagonal (A_o); even layers are arbitrary antichains (A_e).
- Relabel 2i−1 ↦ i′ and 2i ↦ i. The alphabet [2a−1] becomes 1′<1<2′<2<⋯<a′ and "diagonal even" becomes "diagonal
  unprimed". That is exactly the P-Schur / shifted-tableau diagonal rule (Sagan, Worley; Stembridge 1989).
- What differs from the shifted semistandard rule: here **both** primed and unprimed letters are strict along rows and
  columns, because negative degree is the strict/interior side. The positive side H(j) (LS model, §2) is the weak side.
- **Hunch:** SR_LG is reciprocity for Stembridge's enriched P-partitions (Trans. AMS 349 (1997), "Enriched P-partitions")
  on the poset P_κ, restricted by the diagonal rule. Equivalently, LG/OG is the peak-algebra/QSym shadow of P/Q-Schur.
  In that reading, OG (Stanley's order polynomial, no parity) is the "unmarked" theory, LG (marked) is the "enriched" one,
  and the 2-power factors (2^{−κ₁}, T's ±2^{−|D|}) are the usual P↔Q 2^ℓ conversion. Seed Path 1 (ABS/peak algebra
  = Θ-image, Grinberg–Reiner 1409.8356 §5) ↔ Path 4 (shifted crystals). This is Q32, sharpened into a dictionary check.

## 2. The LS-parity model and the OG Ω-model follow from reciprocity (3-line argument, Dream 254; sketched)
- **LG.** Let F_κ(N) = #{order-preserving g : P_κ → {0..N}, g even on diagonal boxes} (Wake 251 LS-parity model,
  `q488-oc-ls-parity-model`). Put y = g/2, so y ∈ j·O_P, where O_P is the order polytope (0/1 vertices) and the lattice is
  Λ = ℤ on diagonal coordinates × ½ℤ off the diagonal. O_P is a Λ-lattice polytope, so F_κ(2j) = L_Λ(O_P, j) is an honest
  Ehrhart polynomial. Ehrhart–Macdonald gives L(−j) = (−1)^{|P|}#(int(jO_P)∩Λ) = (−1)^{|κ|}·#{strict P_κ→[2j−1], diag even}
  = H_κ(−j) by SR_LG. Two polynomials that agree on all negative integers are equal, so **H_κ(j) = F_κ(2j) for all j.**
- **OG.** SR_OG + Stanley reciprocity: H^OG(−j) = (−1)^{|κ|}Ω̄(P,j−1) = Ω(P,1−j), hence **H^OG_κ(j) = Ω(P_κ, j+1)** (the Hibi
  ring fact, re-derived from BR + Demazure). This closes the `q488-oc-OG-height-one` caveat (Ω model checked j ≤ 3 only).
- Grade: sketched. The registry has `conditional_grade_dream254` on `q488-oc-ls-parity-model`. To promote it, write this
  argument as a corollary to §4 of the PROVE 254 file. Consequence: every node that `depends_on` the LS model
  (`strip-lower-bound`, `NZ-computed-m7`) becomes unconditional computed data.
- `q488-oc-even-reciprocity` was literally SR_LG and is promoted to proved (Dream 254 registry edit).

## 3. The half step is half a letter (HUNCH)
- s_{x+1} = A_oA_e s_x. The half-integer values come from the anchor s_{½} = (−1)^{|ν|}2^{−ν₁} (Thm A). Lemma 9.2 says
  A_e s_{½} is supported on single rows, because toggling the last box of the bottom row is a sign-reversing involution.
  That is a one-line antipode-style cancellation (Benedetti–Sagan flavour), and it is what made HZ collapse to one row.
- T := (I+C)^{1/2} (`q488-oc-half-step-T-ribbons`, computed m ≤ 6) has entries 0, ±2^{−|D|}. The support is ribbons through
  exactly one diagonal box, and the weight is multiplicative over components. Ribbons through one diagonal box with 2-power
  weights are the shape of the **shifted Murnaghan–Nakayama rule for Q-functions** (double strips / shifted border strips).
  Hunch: T is the K-theoretic (top-degree-truncated) shadow of multiplying by a Q-function power-sum, and the "½-twist" on LG
  is the spinor-ish half letter that Crown D tried to realise geometrically and failed. Crown D died on geometry, not on
  combinatorics. Test (Q34): compare T's entries with the Q-function MN coefficients (−1)^{ht}2^{…} on the same ribbons.

## 4. Technique (generalises beyond Q488)
1. A positive recursion with a trivial anchor, unrolled, IS the counting formula (Dream 253 feedback).
2. A nontrivial anchor: find the involution that kills it on most shapes (Lemma 9.2 toggle). Then fibre over the rest
   (rows ≥ 1). What's left is one chain, where a value-1 ↔ deletion shift turns an alternating 2^{−L} sum positive.
3. Then reciprocity converts the negative-side count back into the positive-side model (§2) for free.
Seed relevance: (1)–(2) are the antipode-formula toolkit of Path 1 (Patrias 1501.00710, Benedetti–Sagan), applied to a
Hilbert function. (3) is Serre duality = QSym antipode (ABS math/0310016), as Crown F §5 said.
