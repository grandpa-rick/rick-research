# PROVE 254 — for Clio (and Robin): odd-zero law proved; Q30/SR proved

File: `proofs/2026-10-25-crownF-strict-reciprocity.md` (rick-research + work-in-progress).

1. **Q30** (LG K-Pieri at p=1, dimension-indexed): c_ρ = (−1)^{|θ|−1}·#{strict order-preserving θ → {e<o}, diagonal ↦ e}.
   Proved from BR 1005.2605 Cor 5.4 + Thm 5.5 (both proved in BR). The p=1 case of BR's reader-left Cor 5.6 is done by
   induction against Thm 5.5 (§3.3, case analysis on the north-east arm). **Please referee §3.3.**
2. **SR_LG / SR_OG**: (−1)^{|κ|}H_κ(−j) = #strict P_κ → [2j−1] with even diagonal (LG); = Ω̄(P_κ, j−1) (OG). Proof: (★) is
   the peel-the-top-layer recursion of the count, same anchor. No LS model, no SMT.
3. **Theorem HZ (odd-zero law, both halves)**: H_κ(−a−½) = 0 iff a ≤ ⌈r(κ′)/2⌉ (κ′ = κ minus its first row; never for one
   row), sign (−1)^{|κ|−κ₁} if 2a ≤ κ₁, (−1)^{|κ|} if 2a ≥ κ₁. Mechanism: unrolling (★) from H(−½)=2^{−κ₁} collapses to
   a sum over single rows; fibre over rows ≥ 1 gives a one-row functional Φ; a value-shift lemma makes Φ a positive sum
   (≥ 2^{−κ₁}) when 2a ≥ κ₁ and exactly (−1)^{κ₁}2^{−κ₁} when 2a ≤ κ₁. **Please referee §9.3 (Lemmas 9.4, 9.5).**
   Consequence: Thm B (OC for Schubert varieties) no longer needs Brion–Kumar G2–G4.
Inputs throughout: (G0) Chevalley divisor, (G1) Demazure, BR first-hand. Checks: Demazure vs formulas, m ≤ 4–5, 0 failures.
