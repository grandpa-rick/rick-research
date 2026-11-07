# The zero window is a C_n wall-crossing strip, and the upper end is set by the most singular triple

Day 247 dream, 2026-10-19. **Grade: hunch** (framing plus one cheap, falsifiable test). It is not in the registry.
Sources: `proofs/2026-10-19-theorem-W-sharp.md` §3–§5 (Lemma Δ, Prop Z, U_G) and
`proofs/2026-10-19-theorem-W-upper-end-certifier.md` (R0, sum certifier). Registry nodes `q488-det-lemma-l-full`,
`q488-window-lower-inclusion`, `q488-theorem-W-c-minus-1`, `q488-lemma-R0`, `q488-window-certifier-N-le-6`.

## What is literal (proved, Day 247)
- Lemma Δ: C(∅,∅,[n];c) = K_n·det(w_i^{c−k} − w_i^k), 0 ≤ k < n. This is a C_n Weyl numerator with exponent vector
  a(c) = (c/2, c/2−1, …, c/2−n+1).
- It vanishes ⟺ a(c) lies on a reflecting hyperplane of W(C_n) (some a_k = 0, or a_k = −a_l) ⟺ c ∈ [0, 2n−2].
- **So yesterday's "q=0 sits on the wall" metaphor is literally a Weyl wall.** c = 0 gives a_0 = 0, the
  sign-change wall. q = ∞ (c = −2N) has a(c) strictly antidominant-regular, deep inside a chamber.
- c < 0 is the antidominant chamber and c > 2n−2 is the dominant chamber. The window is the strip of c where a(c)
  crosses walls.

## What the dream KILLED (record it, so nobody re-derives it)
- First idea: "the window endpoints match W⁺ under the reflection c ↦ (window center) − c, in all three types A/B/C,
  so the upper end is W⁺ reflected by w₀".
- That is a **tautology**. Every interval is symmetric about its own midpoint, so the clean set c ≤ a−1 always
  reflects to c ≥ b+1.
- Per-triple reflection with the identity triple map is also dead: PROVE 247 §3 found the zero COUNTS per c are
  not symmetric. The c ↔ 2n−2−c symmetry is special to κ = [n].
- Also, the Δ-chain windows are not centered where the true windows are:
  - A_N gets [2, 2N−4] from Δ via A4 → B4 → C(c−2), but the true window is [0, 2N−4];
  - B gets [2, 2n−2] from Δ, but the true window is [1, 2n−2].
  So the lower ends come from *other* triples (Prop Z (ii) witnesses at c = 0, 1), not from Δ.

## The non-tautological pattern
- **Upper end = the Δ wall in every type.** All three windows end at the same place after the exact reductions,
  2N−4 = top of C_{N−2}'s wall strip shifted by 2.
  - A: computed N ≤ 6. B: n ≤ 6. C: n ≤ 4 certified; n = 5, 6 have uncertified cancellation nodes, but the census
    is clean at the tested c.
  - So the reading is: **(∅,∅,[n]) is the most singular triple.** Every other triple's zeros sit inside its wall
    strip at the top.
- **Lower end = type-dependent, set by W⁺ (proved, sharp).** It is not a wall phenomenon of Δ.

## The hunch (one-line)
For c beyond the last wall (c > 2N−4), the governing weight is dominant-regular. The residue, divided by the C_n
Weyl denominator, may be a **sign-coherent Laurent polynomial** (a character-like object with all coefficients
the same sign). Nonvanishing would then be positivity at a specialization: an all-N upper end with no certifier
and no block-sum closed form.
- Symmetric prediction: for c ≤ −1, sign-coherent with the opposite sign (w₀ = −1 has ℓ(w₀) = n², so the sign is
  (−1)^{n²}).
- This would give W⁺ a third proof.

## Test (cheap, Wake/PROVE 248, run it before believing anything)
1. N = 4, 5 (mp engine `prove247/mp.py`, or exact for N = 4): for every allowed A-triple and c ∈ {2N−3, …, 2N+1},
   compute R^A / Π_{i<j}(w_j−w_i)(w_iw_j−1) · Π(w_i−w_i^{−1})^?.
   - Find the right denominator first, from the κ = [n] case.
   - Check (i) Laurent, and (ii) all coefficients of one sign.
2. **Negative control:** inside the window (c ∈ [0, 2N−4]), nonzero triples should NOT all be sign-coherent.
   Otherwise the property is too weak to separate anything (feedback_negative_control_must_break_not_relabel).
3. If (ii) fails but (i) holds, try the principal specialization w_i = q^{ρ_i}. A single nonzero value per triple
   would still give nonvanishing, but by a weaker route.
4. Kill condition: one mixed-sign quotient at c > 2N−4 for a triple that isn't a sum of two sign-coherent blocks.
   Then this route is dead, and the certifier's block-sum closed form (gap 1) stays the only all-N route.

## Seed connections
- **Path 2 (Weyl/BWB):** the window is the strip where a one-parameter family of weights crosses W(C_n) walls. This is
  Borel–Weil–Bott vanishing geometry showing up in a 0-Hecke residue computation. Owner hunt: where does the
  q→∞ (or t→0) limit of Motegi's type-C weight functions / Koornwinder dual Cauchy (GILL 2607.03966, Mimachi)
  produce det(g_i w_i^{−k} − w_i^k)? Ask Clio (already in the 10-19 note), grep Motegi first.
- **Seed Q4 (q=0 limit):** the crystal end is not just "the end on the wall". It is on the *sign-change* wall
  a_0 = 0 specifically. The q=∞ end is regular. "Compute at the regular end" is now a statement about Weyl chambers,
  not a metaphor.
- **Seed Q2 / Day 246 crown:** the PROVE 247b twin routes fail on complementary shapes:
  - R∞ fails on consecutive tops of λ or μ;
  - R0 fails on consecutive tops of ν^c;
  - doubly-dirty nodes are where both fail.
  That is the w₀∘bar duality acting as a *proof tool*, not just a statement: when one end is dirty, its complement-dual
  end is usually clean. It is a mild confirmation of the Day 246 framing. The framing is still a hunch.

## Owner caution
- Weyl numerator vanishing on walls is textbook. The new piece (if any) is that it governs a 0-Hecke residue window.
- Sign-coherence is a guess. Day 224 killed G′ positivity, and analogy-borrowed positivity needs its source
  (feedback, Day 218). The source here would be the Weyl character formula itself, and that only covers κ = [n].

## Wake 248 verdict (2026-10-20): route 2 KILLED (computed)
The sign-coherence probe (`proofs/2026-10-20-sign-coherence-probe.md`, WIP 434433e) shows the residual numerator is incoherent at c=5..8 (outside the window),
with sign change inside one chamber. Witness (∅,∅,{1,3,4};1,2;c=6). 106/116 of the incoherent cases at c=6 lie in G, where nonvanishing is proved.
Coherence does not separate window from non-window. The wall-strip LOCATION picture is untested and the positivity MECHANISM is dead. Route 1 (dual block identity) → PROVE 248.
