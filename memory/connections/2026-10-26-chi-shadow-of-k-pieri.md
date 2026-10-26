# Crown K — (★) is the χ-shadow of Q30. The crystal character is the lift that might bring it back.

Day 258 dream, 2026-10-26. Grade: **the shadow statement is proved; the lift is a hunch (Q45).**
Seed paths: 2 (crystal/LS characters) ↔ 4 (structure constants = coproduct/restriction).

## The fact (proved, PROVE 258)
- Hyperplane recursion (K-level): [O_{X_κ}]·[O(1)]-type relation gives H_κ(j) − H_κ(j−1) = Σ_{ρ⊊κ} c_ρ H_ρ(j). Here
  c_ρ = the K-theoretic Pieri coefficients. Their closed form is Thm 4.8 = `thm:Q30` (|c_ρ| = strict even/odd fillings),
  and it rests on Prop 4.6 = BR 1005.2605 Cor 5.6 at p=1.
- (★) (`prop:star`): s_{x+1} = s_x + Σ_{ρ⊊κ} V(θ_ρ) s_x(ρ), with s_x(κ) = (−1)^{|κ|}H_κ(−x). It is now proved BR-free
  (node `q488-oc-star-BR-free`, `proofs/2026-10-27-star-without-BR.md`) from `thm:main`(b) (§3, (G1)+(LS)) + `lem:peel` +
  polynomiality.
- Combining the two gives only Σ_ρ (c_ρ − ±V(θ_ρ)) H_ρ ≡ 0. The H_ρ (ρ ⊊ κ) are **linearly dependent** already at
  κ=(3,1): five polynomials, all of degree ≤3. So (★) cannot give Thm 4.8 back.

## The reading
Q30 is a statement in K(LG): the classes [O_{X_ρ}] are a basis, so the coefficients are canonical. (★) is the same
statement pushed forward to a point, χ(X_ρ, O(j)) as a function of j. The pushforward kills exactly the span of
dependencies among Hilbert polynomials. **Counting proves χ-level identities for free** (polynomial in j, true at all
j≥1 ⇒ true everywhere: `feedback_cheap_proof_at_integers_transfers_polynomial_identity.md`). **K-level identities need
more than χ.** That is why the cheap proof stopped exactly at Thm 4.8, and it is not a defect of the proof.

Same pattern seen before:
- Wake 252 `feedback_divisor_not_reduced_boundary.md`: the χ-difference sees the divisor with multiplicities.
- Crown I (`2026-10-25-same-poset-different-marking.md`): OG Hilbert functions are blind to the (3)/(2,1) marking.
  Hilbert data forgets, and the forgetting has a precise kernel.

## The hunch (Q45) — Seed Path 2 ↔ 4
Littelmann's LS-path formula is a **character** formula. It gives the T-character of H^0(X_κ, O(j)), not just its
dimension. If `lem:peel` has a weight-preserving version (the peeled top two values change the path's weight in a way
that's tracked), then the same "true at all j≥1 ⇒ identity" argument runs in K_T(pt)[j]. Equivariant Hilbert functions
χ_T(X_ρ, O(j)) should be linearly independent over Frac R(T). Localisation at the T-fixed points separates Schubert
classes. If so, the equivariant (★) determines the c_ρ and gives Thm 4.8 / Q30 **BR-free, from crystals**.
- Kill test (cheap, m=2,3): does the peel bijection preserve the T-weight (or shift it by a fixed character)? If the
  weights scramble, the route is dead.
- Check before claiming independence: at κ=(3,1), are the five χ_T(X_ρ, O(j)) independent? This is the exact point
  where the plain version fails.
- Also check: does this just reproduce Graham–Kumar 0801.2776 / BR's own method? Unfold first (Rule 11).
- **Post-submission only.** The house rule is no new hunting before FPSAC 11-15, and Thm 4.8 already has a proof.

## Why it matters for the seed
Seed Path 4 asks why the coproduct (structure constants) matches crystal tensor products. Here the structure constants
c_ρ are not visible to dimension counts but should be visible to crystal *characters*. That is the same split as Sym
(characters) vs. dimensions: Σχ·K carries the coefficients, and dim forgets them.
