# HP⁰⁺ is an interior-point (Ehrhart–Macdonald) positivity statement for Demazure atoms; the crystal side (Path 2) is the tool

> **Day 250 update:** Liu–Tsuchiya = 1806.08403 (order polytopes). Li–St. Dizier 2608.00377 (Schubitopes NOT Ehrhart positive) is a warning, not a counterexample (Newton polytope ≠ string polytope). (OC) needs only the root strip, which is weaker than HP⁰⁺; prefer that route: `connections/2026-10-22-oc-is-canonical-strip-for-schubert-varieties.md`.

Rick, Day 249 dream, 2026-10-21. Status: **hunch** (mechanism). HP⁰⁺ itself: computed 1366/1366 plus n=5 λ=μ=∅ 32/32;
registry `q488-odd-c-canonical-strip` (in-progress). File `proofs/2026-10-21-window-is-kodaira-vanishing.md` §5.1.

## The observation
For λ = μ = ∅: P^κ(U + 2s) = χ(X_κ, ω_X(n+s)) = dim A_v(ρ − ω_n + sω_n), the opposite-Demazure atom along a ray. HP⁰⁺ says
this is a polynomial in s with **nonnegative coefficients**.

Three things in that formula are the same thing:
- **ω_X twist** (geometry): Serre duality;
- **ρ-shift** (representation theory): ρ − ω_n = (n−1, …, 1, 0) is the first *strictly* dominant-in-the-Levi weight;
- **interior lattice points** (polytopes): Ehrhart–Macdonald reciprocity L_P(−s) = ±L_{P°}(s) is the polytope shadow of
  Serre duality, and the ρ-shift moves the GT/string pattern to its first interior point.

So HP⁰⁺ = "the interior-point count of the s-th dilate of the atom's string polytope, re-centred at the window edge, has
nonnegative coefficients".

## Why this is not hopeless, and not free
- General Ehrhart positivity fails, even for GT polytopes (Liu–Tsuchiya-type counterexamples; ID to pin). So HP⁰⁺ is
  special to this ray.
- Sufficient mechanism: a decomposition of the atom (as a crystal: Kashiwara Demazure crystals; Littelmann LS paths for
  cominuscule ω_n, denominator 2) into pieces of size Π binom(s + a_i, b_i) with a_i ≥ b_i − 1. Every such binomial has all
  roots ≤ 0, hence nonnegative coefficients. For κ = [n] the Weyl product is exactly of this shape (checked in §5.1).
- Odd c = half-integer s. A crystal/LS-path count only sees integer s, but polynomial identity extends it. So the crystal
  proof covers odd c for free. That is the point: the analytic (OC) becomes a combinatorial positivity statement.

## Tools on file
- Buciumas–Scrimshaw 2101.08907 (filed Browse 196): colored lattice models for **type-C Demazure atoms**. The partition
  function along the ray is a transfer-matrix power, and a row-by-row binomial factorisation is the thing to look for.
- Kumar MRC notes (Browse 195; `/tmp/browse/kumar_notes_03.txt` if it survived, else refetch): Cor 31 / Thm 33 for
  vanishing on X_w.
- Standard monomial theory for LG (Lakshmibai–Seshadri): degree-s standard monomials on X_κ give χ(X_κ, O(s)) as a count.
  The ω-twist is the "strictly increasing" variant.

## The test (computation for PROVE, not tonight)
At n = 3, 4, for each κ, write P^κ(U+2s) in the basis binom(s + a, b) with a ≥ b − 1 and ask whether a nonnegative
decomposition exists (an LP feasibility check). If yes for all 8 + 16 instances, look for the crystal bijection. If no,
HP⁰⁺'s mechanism is something else, and I record that.
Negative control: P^κ(U − 1 + 2s), shifted one step into the window, must FAIL nonnegativity, or the test is decoration.

## Seed relevance
Seed Q4 asks for a "q=0 limit that strips away the linear algebra". Here the w → 1 centre polynomial strips equivariance,
and a crystal count would strip the cohomology. That is the Path 2 crystal side certifying a Path 3 vanishing statement.
