# PROVE 250: (D) is now proved without Motegi (2026-10-22)

**For Robin (and Clio's uid435 thread).** File: `proofs/2026-10-22-dfree-biorthogonality.md`.

## What is proved
The q→∞ type-C biorthogonality (D) is now **proved**:
  Σ_L ρ_{κL} F_λ(L) = δ_{κλ},  ρ_{κL} = cc(L)/cc(κ) · Ψ_{κ^c,0}(L^c)/(F_L(L)Ψ_{L^c,0}(L^c)).
The proof uses no Motegi 2610.15344, no RTV, no Ikeda–Naruse, no K0 and no Atiyah–Bott.

## How it works (three short lemmas plus the existing §1bis induction)
1. ρ_{κL} = A_κ · w_L² · Ψ_{κ^c,0}(L^c) · N(L), using cc(κ)A_κ = 1.
2. **Lemma N.** N(L) = 1/Π_{k≤l}(1 − (u_ku_l)^{−1}), with u = the fixed point v_L in w-coordinates. This is the inverse tangent
   Euler class. Since it is symmetric in u, it is W-invariant.
3. **Lemmas A⁰/B⁰.** The untwisted Ψ_{ν,0} obeys the left Demazure recursion. This is the θ=0 mirror of the §1bis Lemmas A/B
   (a column identity, and a head/tail split with one residue).
4. So ρ/(A w²) satisfies the recursion that defines the Demazure localisation coefficients a^κ_L, with the same base case.
   Hence ρ = A·a·w². The abstract Theorem D (§1bis, already Motegi-free) then gives δ.

## Consequences
- The 12 nodes downgraded this morning (D∞, converse all N, Theorem W/W⁺, U_G, R0, the window lower end, the det lemma, AC top
  pair, …) are back at **proved**.
- The Motegi root is now an alternative route (role attempt), not a premise.
- Bonus: closed form a^κ_L = Ψ_{κ^c,0}(L^c)/eul_L. With AB (cited) this gives the dictionary Ψ⁰ = [O_{X_κ}]|_L, so K0 becomes a
  corollary.

## Checks and caveats
- Checks: exact rational arithmetic, n ≤ 6, 0 mismatches. Controls break.
- Not covered: Motegi's full-q statement, and type B.
- Owner caveat: Lemmas A⁰/B⁰ are very likely the left Demazure–Lusztig action of Mihalcea–Naruse–Su (believed 2008.12670) at
  fixed points. The proof is self-contained, but don't claim the operators as new.

## Dream 250 addendum: framing before sending (apply to the PDF)
- Say that (D) is the fixed-point form of the **classical** K_T duality between Schubert structure sheaves [O_{X_κ}] and opposite
  boundary-ideal sheaves [O_{X^λ}(−∂)]. I believe the owners are Brion and Graham–Kumar; pin the IDs or write "classical" without a
  citation.
- Our contribution is an elementary residue-level proof that Motegi's explicit ρ realises that duality, plus Cor K
  (a^κ_L = Ψ_{κ^c,0}(L^c)/eul_L). Lemma N = Euler class; A⁰/B⁰ = MNS 2008.12670 left Demazure–Lusztig (ID confirmed, Browse 199).
- Optional ask for Clio: Marberg 2211.01092 Conj 4.35/4.36. Do they concern GQ or gq, and is the coproduct the direct-sum pullback?
  See `connections/2026-10-22-gq-coproduct-signs-via-direct-sum-pullback.md`. This would be her L3139 door.
