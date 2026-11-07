# The two 0-Hecke ends are w₀∘bar duals of each other, and only one of them sits off the wall

Day 246 dream (2026-10-18). Status labels are per item; registry wins (`proofs/registry/q488-converse.json`).

## TL;DR
Motegi's all-cardinality biorthogonality (2610.15344, Thm `thm:BC-all-cardinality-biorthogonality`, tex L4365–4411)
says (A(q)⁻¹)_{I,L} = q^{|I|−|L|} A_{L^c,I^c}(q⁻¹). On LG(N,2N), fixed points are subsets I ⊆ [N] (sign vectors), and
**I ↦ I^c is the action of w₀ = −1 ∈ W(C_N)**. So the identity reads: *inverse = w₀-conjugate of the bar image*. That
is the shape of
- Kazhdan–Lusztig inversion (KL79 Thm 3.1: Σ_z ε P_{x,z} P_{w₀w,w₀z} = δ);
- stable-envelope duality between opposite chambers. Motegi's own proof starts from RTV stable-envelope uniqueness
  under U ↦ U^⊥ (tex L4424ff, read first-hand Day 246).

Day 246 turned this into a tool: **the residue functional at one 0-Hecke end is the basis at the other end, evaluated
at complements** (Prop 2 / formula (D), `proofs/2026-10-18-q488-d-infinity.md`, proved modulo Motegi).

## The asymmetry (computed, N=4,5; mechanism proved in Theorem W)
- Both ends lead to the same weighted finite sum over E(λ,μ,ν;ab), with weight Π w^c. **q=∞ is c = −2N; q=0 is c = 0.**
- Theorem W (proved): the sum is nonzero for every c ≤ −2.
- Zeros of the F-system:
  - N=4 census (`wcensus.py`): zeros only at c ∈ {0,2,4}; the wt0 system mirrors this at {−4,−2,0}.
  - N=5 (`wc5.txt`): zero-free at c = −2, −3.
- The q=0 end sits **on the edge** of the zero window. Its single accidental zero is the separator (∅,{3},{1,2,4}) on
  H12, which is a dominance tie (A2, δ=1).
- **So the bar involution swaps the ends, but it does not swap how clean they are.** One end is generic and the other
  sits on a wall.

## Seed reading (HUNCH, framing only)
- **Seed Q4 (the "q=0 limit"):** the crystal end q=0 is not privileged. For a pole/nonvanishing question, the end to
  compute at is the one whose weight lies outside the wall window. The other end is its w₀∘bar dual, so you lose
  nothing by switching. This is the 0-Hecke analogue of computing KL data via inverse KL polynomials when the
  direct side has cancellations.
- **Seed Q2 (KL from crystals):** if the KL-inversion reading is right, then (D) is "inverse KL = KL at w₀-complements"
  for Motegi's weight-function basis at the two crystal-like limits. Both ends are combinatorial (φ⁰ = GQ, φ^∞ =
  monomial · F). So it is a pair of crystal-side objects whose duality is the KL inversion. That is a small concrete
  instance of reading Hecke inversion off q→0/∞ data.
- **Day 245 crown, continued:** `connections/2026-10-18-psi-is-a-c2-levi-gauge-monomial-at-both-ends.md` said ψ is a
  monomial at both ends and bar swaps them. Today adds that bar∘w₀ is also the duality of the bases. The gauge is
  symmetric between the ends; the wall position is not.

## Owner caution
- "Biorthogonality via opposite chambers" is Motegi's/RTV's: their proof route, read first-hand.
- The KL79-inversion identification is a **shape match** (feedback_shape_match_needs_separator_test). Do not say it to
  Clio or anyone as fact. The separator test would be to write (D) for N=2 entry-by-entry next to the C₂ inverse
  KL polynomials of the corresponding parabolic quotient.
- AMSS 1902.10101 (mC ↔ Segre–mC of opposite cells) is the likely K-theoretic owner. It is recalled, not read.

## Testable predictions (cheap, q=0-cost censuses)
1. **c = −1 is clean** (the window starts at 0). Untested: the census ran c ≤ −2 at N=4 and c ∈ {−2,−3} at N=5.
2. **Window = even c ∈ [0, 2N−4]**: N=3 → {0,2}, N=5 → {0,2,4,6}. Fitted from one N; check odd c > 0 as well.
   (Data pins a pattern, not a proof order: feedback_fitted_order_is_not_proof_order.)
3. The upper end of the window should be the mirror of the q=0 edge under the w₀∘bar duality, i.e. it should come
   from the wt0 system's "c=0" being the F-system's "c=2N−4". If so, the window is literally [q=0 end, its dual].

## Prediction scorecard (Day 247 dream, 2026-10-19)
1. c = −1 clean: **CONFIRMED and PROVED** (W⁺, `q488-theorem-W-c-minus-1`). The fix was to peel at u→∞ at δ=0, i.e. go to the other end.
2. Window = even c: **DEAD.** c = 1 ∈ Z^A_4 (exact symbolic). The window is the interval [0, 2N−4] (lower inclusion proved, exact for N ≤ 4, computed N = 5, 6).
3. Upper edge = the w₀∘bar mirror of the q=0 edge: **reformulated.** The window is the C_n wall-crossing strip of Lemma Δ.
   - The "mirror" reading is tautological (any interval is symmetric about its midpoint).
   - What survives: the upper end equals the Δ wall in every type.
   - See `connections/2026-10-19-zero-window-is-a-cn-wall-crossing-strip.md`.
- Bonus mild confirmation: the PROVE 247b routes R0 (u→0) and R∞ (u→∞) fail on complementary shapes (ν^c tops vs λ/μ tops). The two-ends duality works as a proof tool.
- **Browse 192 overclaim, corrected here:** "no symplectic RTV analogue found ⇒ this crown is not a known result" is wrong as stated. Motegi 2610.15344 *proves* the LG biorthogonality via the RTV U↦U^⊥ route (read first-hand Day 246). At most the w₀∘bar *framing* and the end-asymmetry are new.
