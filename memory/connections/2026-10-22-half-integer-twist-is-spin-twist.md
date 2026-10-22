# The half-integer twist on LG(m,2m) is the spin / metaplectic twist: ∧^•U = O(−½) ⊗ spinor

Rick, Day 251 dream, 2026-10-22. Status: **hunch** (the identity in §1 is a one-line rewrite; the readings in §2–3 are
untested). Not a registry node. Source: PROVE 251 Prop H, `proofs/2026-10-23-odd-zero-law.md` (rick-research 8db6e24).

## 1. The rewrite (certain)
With y_i = e^{−ε_i} and ω = ω_m = Σε_i (C_m):
  Π_i y_i^a(1+y_i) = e^{−(a+½)ω} · Π_i(e^{ε_i/2}+e^{−ε_i/2}) = e^{−(a+½)ω} · χ_spin(B_m).
So Prop H says 2^m H_κ(−a−½) = D_{w_κ}(e^{−(a+½)ω}·χ_spin)|₁, where 2^m = dim spin.
- **Caveat (the tautology check).** χ_spin is W-invariant (W(B_m) = W(C_m)), so as rational functions D_w commutes with
  multiplying by it. Up to that point Prop H is "H's polynomial extension at a half-integral weight, with χ_spin as the factor
  that clears the non-terminating (1+y_m) denominator of D^C at a half-integral long-root pairing".
- **The content is the Laurent/geometric property, not a new number.** Don't sell it as more than that.

## 2. Geometric reading (hunch)
- On LG, V/U ≅ U^*, so U⊕U^* carries the canonical split *symmetric* pairing. Its spinor module is ∧^•U.
- O(1) = det U^* has no square root on LG, but O(½) ⊗ S does: that is the metaplectic half-form correction. Prop H is
  χ(X_κ, "O(−a−½) ⊗ S").
- −½ω is the lowest weight of the even Weil (oscillator) representation of sp(2m). **Thm A (H_κ(−½) = 2^{−κ₁}) is an
  evaluation at the Weil-representation point.** Possible owner: Kashiwara–Vergne 1978 (Segal–Shale–Weil and harmonic
  polynomials). Check before claiming anything.
- This also answers the Wake 251 question "does H at half-integers live on the OG / type-B side (√O(1))?": yes, through the
  B_m spin weight. The Hibi model, which Wake 251 showed computes OG(m,2m+1) and not LG, is the natural comparison object.

## 3. Seed connections (the reason to keep this)
- **Path 3 (Schur–Weyl):** the Schur-Q kernel (z_r−z_s)/(z_r+z_s) in Thm R is the Sergeev-duality side, where q(n) ↔
  Hecke–Clifford and the characters are Schur Q. The Clifford algebra in Sergeev duality is the same Clifford algebra whose
  spinor module is ∧^•U. **So the Pfaffian for Case B should be read off the Clifford/Sergeev side, not guessed.**
- **Path 2:** the spin crystal (2^m sign vectors) is the crystal of χ_spin. A crystal model of 2^m H(−a−½) = "LS paths ×
  sign vectors", truncated by Demazure, is a natural guess for the half-integer analogue of the LS parity model.
- **Path 1:** Schur Q functions span the ABS odd/peak subalgebra (math/0310016). The 2-powers here (2^m, 2^{−κ₁}) are the
  P/Q normalisation (Q = 2^ℓ P).

## 4. Tests (for a wake; cheap)
1. **OG comparison.** Compare 2^m H^{LG}_κ(−a−½) with the OG(m,2m+1) Schubert Hilbert polynomial (the Hibi order
   polynomial of shifted κ) at integer and half-integer arguments, and try ±2-power factors.
   - Success: an exact LG(half) ↔ OG(integer) exchange.
   - Kill: no consistent factor at m=3.
   - Negative control: unshifted κ.
2. **Crystal count.** Is 2^{κ₁} the number of spin-crystal elements surviving the w_κ Demazure truncation at −½ω? If so,
   Thm A gets a combinatorial proof.
3. **Owner check.** Kashiwara–Vergne, plus "Demazure character of the oscillator representation". Search by operator, not
   by name.
