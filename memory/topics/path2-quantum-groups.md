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
