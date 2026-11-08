# Crown U′: the arcs carry information the crystal doesn't. Seed Q2 at the μ-level is a NO, and the Q68 arc is the evidence

Dream 283, 2026-11-08. Seed Q2 (read KL off a crystal) × Path 3 (cells / W-graphs). Grade: **connection (hunch)**. Every ingredient is proved or computed. The *reading* is the hunch.
It replaces Crown U (`connections/2026-11-07-lemmaI-is-an-arc-rule.md`), which is dead.

Sources:
- `proofs/2026-11-08-q68-typeA-closure.md`, Thm W §4, Prop Q §5, table §8;
- `proofs/2026-11-08-q68-lemmaI-false-s16-closed.md`;
- registry `proofs/registry/seedQ2-kl-cone.json` (root closed dead-end 2026-11-08; nodes `Q68-witness-completeness`, `Q68-cell-independence`, `Q68-lemmaI` (dead-end), `Q68-mu-in0` (computed));
- Stembridge, *Admissible W-graphs*, Represent. Theory 12 (2008) Prop 4.2.

## TL;DR
1. **The twin criterion is a tautology wrapped around μ.** Theorem W (proved, any finite W): (x,z) is a twin ⟺ μ̃(y,z) ≥ μ̃(y,x) on the witness set W_i ∪ W_ii.
   - The W_i half is the star / simple-edge data. Its μ-values are all 1 (Thm W(b)), and Lemma S transports them. That is the crystal-readable part (Knuth moves = right stars, Lemma K).
   - The W_ii half is the arc data: nested τ, L(y) ⊋ L(x), y < x.
2. **Every crystal-side guess for the arc half died.**
   - Star-iff-twin died at n=15.
   - The QSym shape level died at n=16.
   - Sieve R1 died at n=16.
   - Lemma I ("no upward arc when N[L(z)] ⊆ L(x)") died: inst 13, λ=(4,4,4,3,1), μ=1 with P_{x,z}=1+8q+24q²+35q³+26q⁴+9q⁵+q⁶. Two implementations agree.
3. **Reading:** in type A up to n=16, the descent / tableau / dual-equivalence data decides everything except a residue of arcs. On that residue, KL genuinely knows something the crystal doesn't. Stembridge needs the global Polygon Rule to place arcs at all, and our arcs aren't forced by any local rule we tried.
4. **So Seed Q2 splits.**
   - *Cells and simple edges*: YES, crystal-readable (KL79 + Knuth; Prop Q re-derives dual equivalence for free).
   - *μ on arcs*: NO local rule found. Evidence only, n ≤ 16, not a theorem. A real "no" would need two pairs with identical molecule data and different arc μ. That's a separator, not yet run.

## Why it matters for the seed
- Path 2 ↔ Path 3. q=0 (crystals) sees the cell *partition* but not the full W-graph. The arcs are exactly the q≠0 residue the Seed asks about ("what survives at q=0"). Answer: the simple edges survive; some arcs don't.
- Path 4 rhyme (Crown U, kept): μ is Leibniz under parabolic layers (Layer Lemma, Billey–Braden math/0202252 Thm 6). So the coproduct-indecomposable (primitive) pairs are where the arcs live. Inst 0 and inst 13 are both primitive.

## Test that would promote or kill this (not scheduled)
- **Separator:** find two candidate pairs in S_16 with isomorphic local molecule neighbourhoods (same Stembridge simple-edge data within distance 2) but μ ∈ {0,1} differing. The open26 data plus Lemma-I kills should already contain such a pair, so it's a grep, not a computation. If it's found, the "NO" becomes a computed separator.
