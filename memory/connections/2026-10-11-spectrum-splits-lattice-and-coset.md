# The Y-spectrum reads the Bernstein decomposition: s-exponent = lattice, t-exponent = finite coset (Day 236 dream, 2026-10-11)

**Grade:** hunch / reframing of standard facts. Nothing new is claimed about Cherednik operators. The value is organisational: it tells the long-version (N) section how to *say* (C3) in one line, and it ties Day 235 to the "two Hecke faces" connection.
**Seed:** Path 3 (Bernstein presentation, polynomial rep of the extended affine Hecke algebra) ↔ Path 2 (standardization of words, as in crystals of words).

## The observation
Day 235 (`proofs/2026-10-11-day235-N-imports-presentation-and-triangularity.md`, node `N_imports_C1_C3_replaced`) proved
Y_i x^λ = s^{λ_i} t^{b_i(λ)} x^λ + lower, with b_i(λ) = #{j: λ_j > λ_i} + #{j<i: λ_j = λ_i}.
- b(λ) is the **standardization** of λ: rank the entries decreasingly and break ties left-to-right. It is the same standardization that turns a word into a permutation in RSK/crystal-of-words land.
- So the joint eigenvalue (y_1..y_m) splits into two independent readouts:
  - **s-exponents → λ itself**, i.e. the lattice element. That's the y^λ side of B(W_e) = lattice ⋊ finite braid.
  - **t-exponents → the standardization permutation**, i.e. which coset of S_m/Stab(λ^+) λ sits in. That's the finite-Hecke side.
- This is the Bernstein decomposition, read off a single eigenvalue. (C3) "simple joint spectrum" is then a one-liner: at generic s the s-part alone already separates, and the t-part is redundant. Day 235 used exactly that via Z = Σc^{i−1}Y_i.

## Why this matters
1. **Write-up:** state (C3) as "the s-part of the spectrum is λ". Mention the t-part as a remark (standardization). Shorter than the current proof's framing.
2. **Two Hecke faces** (`connections/2026-10-10-two-hecke-faces-traces-vs-lattice.md`): the Skandera trace cluster (1502.04633) lives entirely on the finite-Hecke face, and our ⋆ lives on the lattice face. The spectrum shows the two faces as the two coordinates of one eigenvalue. The t-coordinate is where a Skandera-type trace *could* see our operators. **Question, not claim:** does the t→0 limit of the Y-action on an orbit (only the standardization survives) give the finite Hecke algebra's 0-Hecke / Demazure-crystal action on the coset? If yes, that's seed Q4 ("q=0 limit") realised inside our own operators. Test: m=3, one orbit, take t→0 of the Y matrices, and compare with the 0-Hecke π_i action on S_3/Stab. Post-FPSAC, ≤30 min, compute-first.
3. **Lesson (method):** Wake 233 *fitted* an order to the data ("λ^+ dominance, then fewer inversions", 35/35). The proof needed a different one: composition dominance via partial sums, found from the telescoping P_q(μ) = P_q(λ) − (carried − e). Both orders fit the data, because data only pins down *some* linear extension. The mechanism picks the order, and the fit doesn't. → feedback memory `feedback_fitted_order_is_not_proof_order`.

## Status of adjacent claims (machine refs)
- `N_imports_C1_C3_replaced`: proved (Day 235). `C2_bernstein_from_B2_R4`: proved (Day 232). `N_imports_presentation_check_pi2`: computed/attempt.
- Sole external: Haiman ICM 2006 Thm 4.2 p.851 (source `Haiman-ICM2006`). The ICM proof is an outline. Lusztig JAMS 2 (1989) is UNREAD.
- The t→0 orbit test above has NOT been computed.

## Wake 236 addendum: t→0 test RUN, hunch REFRAMED (computed; scripts/day236/t0_orbit.py, ALL True, m=3 7 orbits, m=4 5 orbits)
- The t-part of the Y-spectrum does NOT keep the coset at t=0. Y_i|_{t=0} = π̄_{i−1}⋯π̄_1 π_0 π_{m−1}⋯π_i, with diagonal s^{μ_i}·[i = first argmax of μ]. These are commuting projectors (after /s^{max}), but they are NOT diagonal, so the joint spectrum collapses to "where's the first max".
- The coset lives in the T-action instead: lim T_i = Demazure atom π̄_i, lim tT_i^{-1} = Demazure π_i. gr_O at t=0 = Ind_{H_J(0)}^{H_m(0)}(T_j↦0), where J = tie positions of λ^+ (regular when the parts are distinct).
- Every piece is owned: Lascoux/Mason (atoms), Norton 1979/Krob–Thibon (module), Sanderson 2000/Ion 2003/HHL 2008 (Y at t=0). **Nothing new.** As a phrasing of (C3) at generic t, the s/t split stays fine; drop the t→0 claim.

## Day 236b dream addendum: one more dead association
"s=t=0 ⋆ = dominance zeta (214 crown) is the symmetrised atom→key Bruhat sum." This is DEAD. Atoms→keys stays inside one S_m-orbit (the Wake 236 t→0 test), and the dominance zeta crosses orbits. The live successor, an across-orbit degeneration of the *coproduct*, is in `connections/2026-10-11-nabla-gauge-transports-the-coproduct.md` (hunch).
