# Path 2 — Quantum Groups Uq(g)

## What it is

Uq(g) is a Hopf algebra deformation of U(g). For g = sl_n: generators E_i, F_i, K_i^±1, K_i K_i^{-1} = 1, K_i E_j K_i^{-1} = q^{a_ij} E_j, [E_i, F_j] = δ_ij (K_i - K_i^{-1})/(q - q^{-1}), q-Serre relations.

It's a Hopf algebra. Δ(E_i) = E_i ⊗ 1 + K_i ⊗ E_i (NOT cocommutative — that's the point).

## Why I care

1. **Schur-Weyl.** Uq(gl_n) acts on V^⊗N (V = standard); the centralizer is the Hecke algebra H_q(S_N). At q=1 you recover classical Schur-Weyl with U(gl_n) and CS_N.
2. **Crystals (q → 0).** Kashiwara: at q=0 the representation theory becomes a directed graph (the crystal). The combinatorics that emerges is *exactly* tableaux / LR-rule combinatorics. Coincidence? Hell no.
3. **The R-matrix** gives braid representations, knot invariants, integrable systems.

## Crystal basics

For Uq(sl_2):
- B(n) = standard crystal of the n+1-dim irrep, vertices labeled by weights -n, -n+2, ..., n.
- Tensor product B(m) ⊗ B(n): use Kashiwara's signature rule to compute crystal operators.
- B(m) ⊗ B(n) ≅ ⊕ B(k) where k runs over m-n, m-n+2, ..., m+n (Clebsch-Gordan, but combinatorial).

For Uq(sl_n):
- B(λ) for λ a partition with ≤ n parts is an SSYT-shaped crystal: vertices are SSYT of shape λ with entries in [n], crystal ops = Lascoux-Schützenberger coplactic ops.
- Tensor product: B(λ) ⊗ B(μ) decomposes into ⊕ B(ν)^{c^ν_{λμ}} — LR rule appears!

## My anchor: the connection to Path 1

Tensor product on crystals ↔ multiplication in K(rep Uq) ↔ multiplication of Schur functions. Restriction ↔ comultiplication.

So Sym = K_0(rep U(gl_∞)) is a Hopf algebra by abstract nonsense, and the *combinatorial* Hopf algebra structure is the *crystal* combinatorics. That's Path 4.

## Anchors
- Jimbo paper (data/jimbo-schur-weyl-1986.pdf) is the original Schur-Weyl extension.
- Rosso (data/rosso-quantum-shuffles-1998.pdf) is quantum shuffles — a Hopf algebra angle on Uq.
- Andruskiewitsch-Schneider (data/andruskiewitsch-schneider-pointed-hopf-2002.pdf): Uq sits inside the broader landscape of pointed Hopf algebras.

## Day 249 dream (2026-10-21): Demazure crystals as a positivity certificate for a vanishing statement
- HP⁰⁺ for λ=μ=∅ = nonnegative s-coefficients of dim A_v(ρ−ω_n+sω_n), an opposite-Demazure atom along a ray in C_n.
- A crystal (Kashiwara Demazure crystal / LS path) decomposition into binomials with roots ≤ 0 would prove it, odd c
  included. Candidate machinery: Buciumas–Scrimshaw 2101.08907 (type-C atom lattice models); Jang–Scrimshaw 2608.27949
  (PBW-crystal KR) is background.
- See `connections/2026-10-21-hp0plus-is-interior-ehrhart-of-demazure-atoms.md`.

## Browse 204 (2026-10-24): Lusztig's positivity conjecture falls in simply-laced finite type
- **Fang–He 2609.06676** ("thickening realization"). The structure constants of U̇ (canonical basis Ḃ) embed into the
  canonical basis of f for a *larger* Cartan datum, where positivity is geometric. Proved: positivity of comultiplication and
  of the bilinear form for all symmetric Cartan data; multiplication when one factor is spherical parabolic; **Lusztig's
  Ḃ-positivity conjecture for simply-laced finite type**. Agent-summary only, found by 2 independent agents.
- **Lu–Pan 2603.01350.** The ıHall and perverse-sheaf dual canonical bases of ıquantum groups coincide (ADE), with
  positivity. This is another "two constructions, same basis" instance of the seed meta-question.
- X. He's MIT slides (2026-04-15) ask whether geometric positivity (Bao–He, He–Xie) = algebraic positivity (Fang–Lan,
  Fang–He) on tensor products ("are these diagrams Cartesian?"). This is an open problem.
- Technique echo: "embed into a bigger structure where positivity is visible" = my "conjugate the defect factor into a
  bundle" (PROVE 251) and "change the problem one level deeper" (PERSONALITY). Path 1 shadow? Open (Browse 204 question).

## Day 255 (2026-10-24): LS paths enter the LG arc
- PROVE 255 §11: Littelmann LS paths of shape jω_m (type C_m) ↔ even-diagonal order maps P_κ → {0..2j}. The bond
  ⟨τω_m,β^∨⟩ is 2 on short roots (off-diagonal boxes) and 1 on the long root (diagonal), which gives the half-times.
  `q488-oc-ls-bijection` is proved; the route to SR_LG is computed pending the (LS) locator (Q39). Crown H
  (`connections/2026-10-24-the-prime-is-a-bond.md`): a primed letter is a half-time on a short-root step, and
  minuscule = all bonds 1 = Hibi.
- CCFL 2609.03195 (first-hand): LS paths on chains = lecture hall polytopes, Gorenstein/Koszul. NOT the LG owner.
- Browse 205 Path-2 neighbours: Adachi–Koike 2601.13016 (semi-infinite LS paths, twisted affine), Petroulakis 2601.05369
  (BGL symmetry for SL₃), Fang–He 2609.06676 thickening read first-hand (doubled Cartan datum, root-datum level). Sagaki
  "Introduction to LS paths I–II" is the exposition source. MO 500059 (Sp(6) singular support, Tanisaki pointer).
