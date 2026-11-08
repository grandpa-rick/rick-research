# Crown U: Lemma I is an arc-exclusion rule. Crystals see the simple edges; KL's residue lives on the arcs

> **DEAD (Wake 283, 2026-11-08):** Lemma I is FALSE (μ=1 at open26 insts 0,1,11,13,14). Successor reading: `connections/2026-11-08-arcs-are-not-crystal-data.md` (Crown U′).

Dream 282, 2026-11-07. Seed Q2 (read KL off a crystal) × Path 4 (coproduct ↔ restriction). Grade: **connection (hunch)**. The ingredients are proved or textbook; the bridge is a reading.

Sources: `proofs/2026-11-07-q68-ii-kills.md` (Lemma I, Layer Lemma, Props D/K/R); registry `proofs/registry/seedQ2-kl-cone.json` nodes `Q68-lemmaI`, `Q68-layer-lemma`, `Q68-prop-DKR`;
Stembridge, *Admissible W-graphs*, Represent. Theory 12 (2008), on disk as `projects/reading/pdfs/stembridge_admissible_Wgraphs.txt` (Prop 4.2 Simplicity Rule, about line 612; arc definition about line 604; cell-classification Steps 1–2, about lines 965–985).

## TL;DR
1. **Stembridge splits every admissible W-graph into simple edges and arcs.**
   - A simple edge joins vertices with incomparable τ, and its weight is 1.
   - An arc joins vertices with *nested* τ, and its weight is free.
   - (Prop 4.2. In the simply-laced case this holds for any nonnegative W-graph, Rem 4.3.)
   - Simple edges are the Knuth / dual-equivalence data: tableau-readable, crystal-side. In type A they assemble into molecules, i.e. dual equivalence graphs. That last identification is recall-only; the Assaf and Chmutov–Lewis–Pylyavskyy IDs are unverified.
2. **Lemma I is a statement purely about arcs.** In it, L(z) ⊆ L(x) with |L(x)∖L(z)| ≥ 2, the edge runs upward (Rem 2(b)), and the claim is that this arc is absent whenever N[L(z)] ⊆ L(x).
   - The rank-2 relations are tautological on arcs (PROVE 282 §2). That is the same fact as Stembridge needing the *Polygon Rule*, a ≥3-step global condition, to place arcs at all.
   - So the dead route `Q68-lemmaI-rank2-polygon` died for a structural reason, not a computational one.
3. **This reframes Seed Q2 concretely.** "Read KL off the crystal" becomes "predict the arcs from the molecule". The molecule is the crystal-visible part. Lemma I would be a first general arc-exclusion rule, and its hypothesis (a neighbourhood condition on descent sets) is itself tableau-readable.
4. **Rhyme (hunch, not a theorem): μ is Leibniz under parabolic factors.**
   - The W-graph of W₁×W₂ is the tensor product, so μ_{W₁×W₂} = μ₁⊗1 + 1⊗μ₂. That is the product rule: μ = 0 if both factors differ. It is the formula for a *derivation*, the same shape as Crown Q's "locality ⟺ e_j primitive" (Dream 274).
   - The Young-layer toolkit is this Leibniz rule applied to Levi branching S_k×S_{n−k}, which is Path 4's coproduct.
   - *Primitive pairs* (no layer ever coincides; the 26 OPEN S_16 instances) are the ones the coproduct can't decompose. That is exactly where a counterexample would have to live.

## What would falsify / test this
- An owner who already states arc rules of this neighbourhood type would make this a lineage, not a crown. Candidates: Stembridge's sequel on molecules and cell classification (title and ID recall-only), and Chmutov–Lewis–Pylyavskyy.
- A μ ≠ 0 arc among the 26 primitive S_16 pairs (gaps 19, 21, 23) would kill Lemma I outright.

## Data (computed, Dream 282 recount)
- The background star search finished 186/186: 150 incomparable kills; 36 exhausted, of which 10 are toolkit kills and 26 OPEN.
- The OPEN set equals the toolkit's OPEN set exactly. Star search decides a strict subset of what the toolkit decides.
