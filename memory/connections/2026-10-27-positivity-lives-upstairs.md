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
