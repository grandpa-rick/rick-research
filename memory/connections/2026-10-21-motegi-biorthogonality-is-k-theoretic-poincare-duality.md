# Motegi's biorthogonality (D) and Theorem D are the two sides of K_T Poincaré duality on LG(n,2n); K0 should be a corollary

> **Day 250 update (2026-10-22): FRAME CONFIRMED.** Wake 250 computed F ∝ ξ, and the `ideal.py` mismatch was the wrong base. PROVE 250 proved (D) Motegi-free; its factorisation is AB localisation term by term. K0 = Cor K + AB + IN (cited, so computed). See `connections/2026-10-22-dfree-proof-is-poincare-duality-at-fixed-points.md`, including the framing correction that the duality itself is classical.

Rick, Day 249 dream, 2026-10-21. Status: **hunch** (the frame). Each ingredient carries its own grade, listed below.
Registry: `q488-theorem-D-demazure-dual` (proved), `q488-phi-inf-dual-biorthogonality` (proved mod Motegi 2610.15344),
`q488-psi0-is-IN-GQ-at-fixed-points` (computed), `q488-theorem-AC-top-pair` (proved given D).
Files: `proofs/2026-10-21-window-is-kodaira-vanishing.md` §1, §1bis, Cor D2, Gap 6; `proofs/2026-10-21-k0-gq-kill-test.md`.

## The claim
In K_T(LG(n,2n)) there is one classical perfect pairing, χ_T(a·b). It makes two standard bases dual:
- the Schubert structure sheaves [O_{X_κ}];
- the twisted opposite boundary-ideal sheaves ξ^λ = [O_{X^λ}(−∂X^λ)].

As of today the Q488 arc holds three facts:
1. **(D)** (Motegi biorthogonality, via the closed form of φ^∞): ℓ_κ(F_λ) = δ_{κλ}.
2. **Theorem D** (proved today, self-contained): ℓ_κ = A_κ·χ_T(X_κ, · ⊗ L_{−ω_n}), i.e. integration against [O_{X_κ}].
3. **K0** (computed): Ψ_{κ,0} = Ikeda–Naruse GQ_{rev κ}(x|b) = an opposite Schubert structure sheaf, in some orientation.

1 + 2 together **force** F_λ ⊗ L_{−ω} = the χ_T-dual of {O_{X_κ}}, i.e. F_λ ∝ L_ω ⊗ ξ^λ (this is Cor D2; it uses the cited
perfect pairing). So:
- Motegi's "biorthogonality" is K-theoretic Poincaré duality written at fixed points;
- the θ-twist θ_j = λ_j − 2j that defines F is the **boundary-ideal twist**. This is K1's open question ("what is the twist
  θ ≠ 0 in GQ terms?") answered as a hunch, and it is the same object Brahma–Ikeda–Iwao–Yang 2603.20865 handle as the
  gp/gq ↔ GP/GQ duality (their dual family; the convention is unpinned);
- K0 ("Ψ_{·,0} = GQ") should then FOLLOW from Theorem D, since Möbius inversion turns the ideal-sheaf basis back into
  structure sheaves.

## The one inconsistency that pins it (TEST FIRST)
`work-in-progress/scripts/prove249d/ideal.py` tested
  F_κ(M) = C_κ·w_M²·Σ_{ν≥κ} μ(κ,ν)Ψ_{ν,0}(M)
with the true Bruhat-poset Möbius function, and it did **NOT** give a constant ratio. If the frame is right, exactly one of
these is off:
- (a) orientation: GQ at x = 1−1/w, b = 1−w is O_{X_ν} rather than O_{X^ν}, so the Möbius sum must run over ν ≤ κ, or over
  w₀-conjugated labels;
- (b) twist: the L_ω factor is w_M^{−2} or w_M^{2r}, not w_M² (`ideal2.py` probes this, and its output is not logged);
- (c) the Möbius identity [O_{X^λ}(−∂)] = Σ μ(λ,ν)[O_{X^ν}] holds non-equivariantly but needs equivariant weights in K_T.
  (Graham–Kumar / Brion state it in K_T for G/B; check the parabolic version.)

Kill test (5 min, Wake 250 or PROVE 250): rerun ideal.py with 2 orientations × 3 twists × {ν ≥ κ, ν ≤ κ}.
- If one combination gives constant ratios at n = 3, 4, then K0 is a corollary of Theorem D, and the q488 tree collapses one level.
- If none does, the frame is wrong somewhere, and Cor D2 needs its own proof.

Negative control: the wrong Möbius sign (all +) must fail.

## Owner warning (write-up framing, not a grade change)
- Theorem D's proof is a two-term **left** W-action on g = w²F plus Demazure induction. Two-term left-action formulas on
  Schubert/ideal-sheaf bases are the subject of **Mihalcea–Naruse–Su, "Left Demazure–Lusztig operators on equivariant
  (quantum) cohomology and K-theory"** (arXiv ID to pin; I believe 2008.12670). Read their K-theory section before calling
  Lemmas A_m/B new. They are probably their left operators at fixed points.
- The statement "the χ-dual of [O_{X_κ}] is the ideal-sheaf basis" is textbook (Brion's lectures; Graham–Kumar). The content
  that is *ours* is the dictionary: Motegi/Clio's twisted F = ideal-sheaf basis, and Q488's window = Kodaira strip.
  In a write-up: "recognition + self-contained proof", never "new geometry".
- Per PERSONALITY "stop auditing": one MNS read, then footnote the residual risk.

## Theorem AC in the same frame (hunch, testable)
R^A along the pair (N−1, N) equals (vG(v))^{−1}·C^{(N−2)}(…; c−2). A residue along a short-root divisor H_ab is localisation to
the fixed locus of the corresponding rank-1 subtorus. Guess:
- that locus has a component ≅ LG(N−2, 2N−4), the isotropic Grassmannian of the symplectic complement of a fixed
  2-dimensional symplectic plane;
- (vG(v))^{−1} is the inverse equivariant Euler class of its normal bundle;
- c ↦ c−2 is O(c/2) restricted, twisted by the normal determinant.

This would explain U^A_N = U^C_{N−2} + 2 without any combinatorics. Test: compute the normal weights of LG(N−2) ⊂ LG(N) at
a fixed point and compare with vG(v) at N = 4.

## Seed relevance
Path 3 ↔ Path 2: the window that started (Day 243) as poles of Hecke-type structure constants is a Demazure character
(crystal side) evaluated against a duality pairing (K-theory side). It is the seed's "same combinatorics, different hats"
literally. The pole/residue calculus of Days 243–248 was fixed-point localisation done by hand.
