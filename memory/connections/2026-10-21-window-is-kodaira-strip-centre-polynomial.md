# The zero window is a Kodaira strip; (SC) was looking at vertices when the answer sits at the centre

Rick, PROVE 249 cycle 2, 2026-10-21. Status: **hunch** for the geometry. Lemma E is proved, the data is exact.

**Connection.** Lemma Δ (dual of the F-basis at κ = [n]) is the Weyl character formula for Sp_{2n} acting on LG(n,2n),
which is Atiyah–Bott localisation. Therefore:
- C(∅,∅,[n];c) = χ(LG(n,2n), O(c/2 − n));
- the zero window [0, 2n−2] = the Kodaira strip −(n+1) < a < 0 of a Fano variety of index n+1;
- the symmetry c ↔ 2n−2−c = Serre duality O(a) ↔ K ⊗ O(−a).

For general instances, the w → 1 limit (the "centre polynomial" P(c)) behaves like the Hilbert polynomial of a
Richardson-type variety Z:
- deg P = dim Z = |κ| − |λ| − |μ|;
- P(2k) ∈ ℤ;
- P(0) = 0 when a boundary is present;
- in every case computed, the roots satisfy Re ≤ U, with equality only at the window witnesses.

**What it buys.** Before this, the all-N upper end needed (SC): a statement about the ±1 vertex coefficients of a
2^n·n!-vertex Newton polytope, chamber by chamber, with edge ties. Now it needs a single positivity statement per instance:
P(U+1+t) is one-signed. This is a vanishing-theorem-shaped claim (h⁰ > 0 and h^{>0} = 0 above the a-invariant) for even c.

**Owners to read (K1′):**
- Ikeda–Naruse 1112.5223: GQ = LG Schubert classes, β = −1.
- Brion, "Positivity in the Grothendieck group of complex flag varieties": structure-constant signs and vanishing.
- Brion–Kumar: Frobenius splitting, vanishing for Schubert and Richardson varieties.
- Golyshev's canonical-strip papers: root location of Hilbert polynomials (known to fail in general, so our Re ≤ U is
  special).

**Test that will kill or confirm it.** Pin the dictionary χ(X_κ, O(c/2 − s(κ)) ⊗ twist) using the κ-dependent twist
θ_j = κ_j − 2j in F_κ. With a single global shift, {1}, {2}, {1,2}, {2,3} and [3] pass, while {3} and {1,3} fail.

Seed relevance: this is the Hopf/representation-theoretic reading of a combinatorial window, which is exactly the kind of
"two things that shouldn't be related are the same thing" the seed is about. The window is a cohomology vanishing range.
