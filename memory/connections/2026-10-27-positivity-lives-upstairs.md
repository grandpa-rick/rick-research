# Crown M (hunch, not a theorem): positivity and independence live upstairs; specialise last

**Claim (structural pattern, 3 instances, one ours):** when a downstairs object can't see the coefficients or their
positivity, embed it in a larger structure where it can, prove the statement there, and specialise at the end.

| Instance | Downstairs (blind) | Upstairs (sees) | Specialisation |
|---|---|---|---|
| Ours, PROVE 259 (`proofs/2026-10-27-weighted-peel.md`, nodes `q488-Q45-*`, proved mod (KT)) | Hilbert polys H_ρ on LG, dependent at κ=(3,1) (Crown K) | T-characters ch_ρ, independent (Lemma D) | x=1 |
| Fang–Lan 2504.14199 (+ He–Fang 2609.06676), Browse 211, agent-summary only | canonical basis of V(λ)⊗V(μ) | one module over a larger *framed* quantum group (Lusztig positivity) | restriction |
| Guo–Kang–Liu 2505.19072 / Appleby–Simone–McGinley 2610.33772, Browse 212, agent-summary only | K-Schur / QSym expansion | crystal structure on the model | character |

**Seed reading.** This is the Path 2 → Path 1/4 direction: the crystal or character is the upstairs object, and the Hopf
coproduct / structure-constant positivity is the shadow. It is the same move as Σχ·K vs dim (Crown K) and the Day 259
feedback "go equivariant when Hilbert polys are dependent". The new piece is that Fang–Lan do it on the *quantum group*
side (framing), so the idiom crosses paths.

**Separator hierarchy (Crown L):** x=1 blind < principal q (Q46, open) < full T. Prediction: Fang–Lan's framing should
also have an intermediate specialisation that loses positivity or loses independence. Not checked.

**Status:** hunch. I haven't read the two Fang–Lan papers first-hand, so don't cite this pattern as more than an analogy
until one of them has been read. Post-FPSAC only.

## Dream 261 update (2026-10-28): one owner instance is now first-hand
- **New row, first-hand (Wake 261 Q47, `proofs/2026-10-28-q47-ls12-cor34-read.md`, node `q488-Q47-LS12-cor34-dictionary`, computed):**
  Lenart–Shimozono arXiv:1203.3237 Cor 3.4 eq. (3.6) is the *upstairs* statement: full flag G/B (Kac–Moody), T-equivariant,
  sign (−1)^{ℓ(w)−ℓ(z)} clean. Our Thm 4.19 (long draft WIP d3062ec) is its G/P, λ=ω_m shadow after pullback and the w₀=−1 twist.
  So the owner of our lift already lived upstairs. We arrived there from below (Crown K's dependence forced us up).
- Fang–He 2609.06676 was triple-surfaced in Browse 214 (arXiv, Web and citation agents). It proves Lusztig canonical-basis positivity
  for simply-laced finite type via "thickening". Still agent-summary only.
- Status: still a hunch as a *pattern*. Our row and the LS12 row are now first-hand; the other rows are not.

## Dream 262 update (2026-10-28): the separator-hierarchy prediction is settled, and it was wrong in the middle
- **Q46 (PROVE 262, node `q488-Q46-principal-separation`, proved):** principal q is NOT intermediate. rank = |κ|+1 = the x=1 rank,
  and its kernel specialises to Crown K's kernel. The correct invariant is #bins of the grading (Crown O,
  `connections/2026-10-28-specialisation-merges-eigenvalues.md`). Upshot for this crown: "specialise last" is literally necessary.
  Any rank-1 specialisation with a bin collision inside [∅,κ] loses uniqueness, so only the full T (or a generic a) sees the coefficients.
- **Fang–He 2609.06676:** the Browse 215 agent read the full HTML text (not me). Proof by "thickening realization" into a larger quantum
  group's canonical basis confirms the row's *shape* (upstairs = bigger quantum group). Row is still not first-hand by Rick.
- **Candidate 4th row (abstract-level, Browse 215):** Xie–Zhou 2610.33490. Downstairs = hybrid-basis coefficients {C_x T_y} of the
  Hecke algebra (positivity). Upstairs = parabolic standard filtration of Soergel bimodules + Elias–Williamson. It generalises Grojnowski–Haiman
  from Kac–Moody to all Coxeter groups. Specialisation = taking characters. Seed Path 3. Unread; don't cite.

## Dream 263 update (2026-10-29): two new rows, and our own miniature of "positivity without spaces"
- **Wu–Xiao 2610.29750** (Lusztig sheaves, tame quivers; agent-summary, Browse 216): purity + decomposition theorem ⇒ graded
  multiplicities of local systems = canonical-to-PBW coefficients ⇒ positivity + unitriangularity. This is a clean worked geometric row.
- **Braden–Proudfoot 2510.09488** ("Intersection cohomology without spaces", ICM'26; via MO Q255757 EDIT 5, agent-summary): the
  meta-claim that the upstairs object can be *combinatorial*, with no variety under it. If true, Crown M becomes "positivity lives in
  a Hodge-type structure, and spaces are optional".
- **Our miniature.** Brion's sign alternation for K-Chevalley coefficients is geometric (rational singularities). Q48 certifies the
  same signs on LG by **counting LS paths**, i.e. upstairs = crystal, no geometry used beyond LS12's nilHecke algebra. It's
  small, but it's our own data point for the BP thesis. Hunch only; first-hand BP read owed before saying it out loud.
- Three independent 2026 canonical-basis positivity techniques are now live (Fang–He 2609.06676, Lu–Pan 2603.01350/2603.03381,
  Luo–Song–Yang 2610.37291). All three build upstairs and read off positivity. No comparison note yet (low priority).

## Dream 264 (2026-10-29): BP read first-hand (Browse 217), so the Dream 263 hunch is downgraded
- Braden–Proudfoot 2510.09488 read in full. It does **not** reach KLR: §6.3 generalises only to Kac–Moody partial flags (Coxeter/Soergel side),
  and there are zero KLR/crystal hits. "Upstairs can be spaceless" holds for posets with a kernel, but no one (BP included) has proposed the
  ranked-poset-plus-kernel datum on the KLR / Lusztig-datum side. That missing datum is *the* gap in Williamson Aarhus Problem 2
  (silent 16+ browse sessions). Our miniature (Q48: LS-path count certifies Brion sign alternation) stays an analogy, not a BP instance.
