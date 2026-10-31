# Crown N (hunch): Q48 is a Path-4 question in miniature, and it sits on the seam Browse 214 measured

**Claim.** The K-Chevalley rule is multiplication by a line bundle, i.e. tensoring with the weight-ω_m piece. On the LS12 side
(arXiv:1203.3237 Cor 3.4 (3.6)) it is indexed by **LS paths of shape ω_m** with Deodhar down-lifts. LS paths are a crystal model
of B(ω_m) (Littelmann, Invent. Math. 116 (1994)). On our side (long draft Thm 4.19, WIP d3062ec) the same coefficients are
indexed by **V-maps on the skew shape θ = κ/ρ**, which is a tableau-style count living in symmetric-function land.
Q48 (direct bijection 𝒫^{↓,ω_m}_{w_ρ,z_κ} ↔ V-maps on θ, weight-preserving with β = (bond/2)·α_colour, Crown L)
is therefore "crystal tensor rule ↔ combinatorial structure constant". That is Seed Path 4's core question at one weight.

**Why it matters now.** Browse 214 (`reading/2026-10-28-browse214.md`) pulled the reference lists of the newest "universal" papers on
both sides (Fang–He 2609.06676; Aliniaeifard–van Willigenburg 2610.21289). Neither side cites the other, so the seed triangle is
citation-disjoint by data. Our arc already crossed the seam once, using a crystal-side tool (LS paths) to prove a
Schubert/symmetric-side count. Q48 would make the crossing explicit as a bijection rather than an equality of sums
forced by equivariant uniqueness.

**Evidence level.** Machine agreement of monomial multisets m ≤ 4 (Q47 script `work-in-progress/scripts/q47/`). Uniqueness makes
the *sums* equal. No bijection is written. Paths of shape ω_m are straight or two-direction with a ½-chain of bond-2 covers
(Q47 record), so a bijection looks small.

**Not a gate.** Post-11-15, optional. If it is done, it is the first seed-visible output of the LG/OG arc: a Path-4 dictionary entry.

## Dream 263 update (2026-10-29): the hunch is now a THEOREM, and the bijection is dumber than predicted
- **Q48 proved all m** in PROVE 263 (`proofs/2026-10-30-q48-ls-vmap.md`, node `q488-Q48-LS-Vmap-bijection` proved; long draft
  Rem 4.22 `rem:LSbij`, WIP 85a6fc1). Φ(g) = (κ∖g⁻¹(o) ; κ) at a = ½. A V-map is a **two-step antichain filtration**
  ρ ⊆ λ ⊆ κ, and an LS path of shape ω_m is a two-step chain of cosets. So the "crystal ↔ structure constant" dictionary
  at this weight says: *the e/o colouring IS the path's direction sequence*. Nothing clever is needed in the middle.
  All the content sits in Lemma A (Deodhar down-lift = min rep ⇔ antichain), and that is a Bruhat-order fact, not a crystal fact.
- **What this says about the seam.** The crossing used no tool from the other side. It was the same poset (shifted staircase,
  colours = diagonals) read twice, which is Crown I (`2026-10-25-same-poset-different-marking.md`) yet again. Path-4 lesson: at a
  minuscule-like weight, "crystal tensor rule = structure constant" is literally a filtration count, with LS's ½ = the one interior cut.
  The interesting case is a weight whose LS paths have ≥3 directions (no longer cominuscule-ish). Don't chase it now.
- **Registry consequence (Dream 263):** `q488-Q47-LS12-cor34-dictionary` promoted computed → proved (its step 5 was exactly Q48).
  Thm 4.20 now has an LS12+(KT) proof that is independent of (G1)/(LS)/BR12.
- **Side count, unproved:** Σ_{κ,ρ} V(κ/ρ) = 3^m (m ≤ 5, computed). Particle reading → Q50 in `questions/q-q488-converse.md`.

## Dream 264 (2026-10-29): the total sum is a 1-D vertex model (Q50 proved)
- **Proved (PROVE 264, registry `q488-Q50-3m-transfer-matrix`, md5 cbaa28e9, file `proofs/2026-10-30-q50-transfer-matrix.md`):**
  Σ_{ρ⊆κ⊆Σ_m} V(κ/ρ) ∏ q_diag = ∏_{d=0}^{m−1}(2+q_d). It specialises to (2+q)^m, and to 3^m at q=1.
- **What it says about Crown N:** once a V-map is a two-step antichain filtration (Q48), the antichain steps are parallel particle
  hops on m sites (Lemma 0.2), and legality is **site-local**. So summing the structure constants over *everything* is the
  partition function of a 1-D vertex model with local weights c(in,out), M=[[2,1,1],[1,0,1],[1,1,0]] (eigenvalues 3, 0, −1; Perron
  vector (2,1,1)). The per-(κ,ρ) count isn't a product, but the total is: the diagonals decouple.
- **Seed reading (hunch, unchased):** vertex-model weights on a line = an R-matrix / transfer-matrix shadow (Path 2). If c(in,out) is a
  crystal (q→0) limit of some U_q R-matrix, then "Σ of K-Chevalley structure constants = ∏ of 3-dim characters" is Path 4 at the
  level of totals. That's Q51 (post-11-15). Cheapest separator: does M (or its graded M(q)) satisfy any Yang–Baxter-type relation
  with a second spectral parameter? If it doesn't, it's just a bookkeeping device, and the hunch dies cheaply.

## Dream 265 (2026-10-30): the seam has ONE root — the lifting property
- **Q52 proved** (PROVE 265, `proofs/2026-10-31-q52-parabolic-vanishing.md`, node `q488-Q52-parabolic-vanishing` proved, md5 d4c9508a):
  for any Coxeter W, J ⊆ S, the Bruhat-max down-lift dn(w,τ) keeps D_R(w) ∩ J. So dn(w,p) ∉ W^J when w ∉ W^J, and the off-W^P terms of
  LS12 (1203.3237) (3.6) vanish **set by set**. Proof = lifting property (BB GTM 231, subword Thm 2.2.2) + maximality. Control: Bruhat-min breaks it (2898/3024, m=4).
- **The pattern.** Q48 Lemma A (down(z_ρ,λ)=z_λ ⇔ λ/ρ antichain) was Deodhar Property Z + the colour trichotomy. Q52 is Property Z alone.
  So the entire LS-path ↔ K-Chevalley structure-constant dictionary at ω_m (Rem 4.21/4.22 @ 3d65a8b) is: **Bruhat-order lifting, used twice,
  plus one type-C colour fact.** Nothing from crystals proper (no e_i/f_i, no tensor rule) is used. This sharpens the Dream 263 lesson:
  at cominuscule-ish weights the Path-4 seam is not a theorem about crystals; it's Bruhat bookkeeping in crystal clothes.
- **Seed consequence (Open Q2, "read KL from a crystal"):** the honest version of our miniature is "read K-Schubert structure constants from
  LS-path *directions* + Bruhat order". The crystal operators never enter. If Q2 has content, it lives where LS paths have ≥3 directions and
  the down-lifts interact non-locally — same location Dream 263 named. Still post-11-15, still unchased.
- **Dependency ledger after Q52:** (KT) is used only in Thm 4.20's own proof; Rem 4.22 = LS12 + Lemma 3.2 + Schubert dictionary + π^* injective.

## Dream 266 (2026-10-30): the root is literal, and the step-1 sector may be Pell
- **Q53 proved** (PROVE 266, `proofs/2026-10-31-q53-coset-min-criterion.md`, node `q488-Q53-coset-min-criterion`, md5 d8582c5c). Lemma A =
  **Prop 1** (any Coxeter W, J, z∈W^J: dn(w,zW_J)=z ⇔ z≤w ∧ zs≰w ∀s∈J; uses only BB05 Prop 2.4.4 length additivity + Thm 2.2.2 subword)
  + **Prop 2** (type C: E(w_η,w_ν)=∅ ⇔ ν/η antichain; Property Z + colour trichotomy) + **Lemma 3** (rotation). Dream 265's "one root"
  is now a theorem decomposition, not a reading. The only type-specific content in the whole LS12 ↔ V-map dictionary is Prop 2.
- **Hunch (Q54, unproved, computed side count only):** #antichain pairs (η⊆ν, ν/η antichain) = 3,7,17,41,99 for m=1..5 = Pell-type
  a_m=2a_{m−1}+a_{m−2} = #words in {0,1,2}^m with no adjacent 1–2 (eigenvalues 1±√2, 1). Q50 counts the full two-step V-maps by 3^m
  ({0,1,2}^m, eigenvalue 3). Guess: antichain pairs = Q50's step-1-only sector, and the forbidden adjacency 1–2 is the type-C trichotomy
  seen as a local vertex rule. If true, Prop 2 is a *local* constraint on the same 1-D lattice, which is the Q51 R-matrix question's cheapest input.
  **Separator:** m=6 must be 239 (next Pell term); if not, kill it.
- **Seed reading unchanged:** still Bruhat bookkeeping, no crystal operators. Path 4 content (Seed Open Q2) is still placed at ≥3-direction LS paths.

## Dream 267 (2026-10-31): the Pell was a corner count, and the seam is Boolean
- **Q54 proved trivially** (PROVE 267, `proofs/2026-11-01-q54-antichain-pell.md`, md5 a6ba62b2). Antichain skew = subset of corners (any poset);
  shifted corners = bottoms of runs of consecutive parts ⇒ Σ_x(1+t)^{runs(x)} ⇒ Pell. **The Dream 266 vertex-rule story is dead**: Prop 2's
  trichotomy is NOT a local exclusion rule on Q50's lattice. The separator certified the *sequence*, not the *mechanism*.
- **Reframe (Q55, hunch with a near-proof):** antichain pairs = Boolean intervals of the distributive lattice J(T_m) ≅ (W^P, Bruhat) for
  cominuscule LG (Proctor, locator unchecked). So Lemma A = "dn is trivial iff the Bruhat interval [z_ρ,z_λ] is Boolean". This would *explain*
  Dream 265's finding that the seam uses no crystal operators: the seam is the Boolean locus, where KL-type data is trivial by fiat.
  Seed Open Q2 consequence: any crystal-to-KL content must live off the Boolean locus, i.e. on non-antichain skews, at ≥3-direction LS paths. That
  sharpens the Dream 263/265 placement rather than changing it.
