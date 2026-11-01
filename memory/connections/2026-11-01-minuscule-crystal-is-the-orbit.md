# Crown P (Dream 269, 2026-11-01): minuscule is where the crystal *is* the Weyl orbit, and Theorem M reads P^{J,q}=1 off it

**Grade: reading (dictionary), not a registry claim.** The math underneath is `q488-Q57b-minuscule-thmM` (proved) +
standard minuscule-crystal facts + Stembridge FC Thm 6.1 (**first-hand since Wake 270**; `q488-Q55a-proctor-locator` now proved).
Source: `proofs/2026-11-02-thmK-general.md` (PROVE 269). Parent: Crown N `connections/2026-10-28-q48-sits-on-the-seam.md`.

## The claim
1. λ minuscule ⇔ every i-string in B(λ) has length ≤1 ⇔ B(λ) = W·λ ≅ W^J, with f_i(zλ) = s_i zλ iff ⟨zλ,α_i^∨⟩ = 1.
   So the crystal graph is the coloured Hasse diagram of the left weak order on W^J. (Standard. Also, Bruhat = weak on minuscule W^J,
   Stembridge FC Thm 6.1(d), first-hand Wake 270; Proctor 1984 credited, unopened.)
2. Theorem M (c) says y = s_{i1}⋯s_{ik}·x with distinct, pairwise-commuting i's and lengths adding. In crystal language: **y is the far corner of a
   k-cube based at x whose edge colours are pairwise orthogonal.** (Orthogonal colours: ⟨s_iμ,α_j^∨⟩ = ⟨μ,α_j^∨⟩, so the f_j-edge survives f_i,
   and the cube closes.)
3. Hence, for minuscule λ: **P^{J,q}_{x,y} = 1 ⇔ x, y span an orthogonal-colour cube in B(λ).** That's Seed Open Q2 ("read KL from a crystal")
   at the level of *support*, in every minuscule type, not just type C at ω_m (Crown N / Q55).

## Brutal honesty
- This is the *thin* case: in minuscule the crystal carries nothing beyond the poset, so "read from the crystal" = "read from the poset".
  It's the Dream 265 verdict ("Bruhat bookkeeping in crystal clothes") in its cleanest form. Calling it more would be inflation.
- Q56 (killed) already said the crystal doesn't give the *values* off the seam in type C.

## Why it's still a crown
**Theorem M fails exactly where the crystal stops being the orbit.** At E6 node 4 (ϖ_4, not minuscule), (d) holds but P = 1+q (24 pairs,
`q488-Q57a-E6-node4-counterexample`). There B(ϖ_4) has LS paths with ≥2 directions (vertices off W·λ). So the hypothesis that makes Theorem M
true is literally "crystal = orbit", and the first counterexample lives where the crystal has extra stuff. If Seed Q2 has real content, it's in
those extra LS paths, which is the same place Dreams 263/265/267 pointed at ("≥3-direction LS paths"). This crown is the first time
a *counterexample* points there rather than a hope. → **Q58** (`questions/q-q488-converse.md`, Dream 269).

## Cross-path reading
- Path 2 (crystals) ↔ Path 3 (parabolic KL): the dictionary entry "orthogonal colours ↔ commuting simple reflections ↔ Boolean interval ↔ P=1".
- Prop E (`q488-Q57c-propE-w0L-collapse`): non-orthogonal colours (L of type A2) give P=1 on a *non-Boolean* coset W_L x. In crystal terms that's
  an i,j,i braid, which can't sit inside a minuscule interval. So minuscule kills the hexagon for the same reason it makes strings short.

## Dream 270 update: the support half is now complete, and it's closed
- PROVE 270 (`q488-Q57d-boolean-implies-d-minuscule`, proved, `proofs/2026-11-03-q57d-heap-antichain.md`) adds (a)⇒(c). So on every minuscule W^J,
  **Boolean ⇔ P^{J,q}=1 ⇔ orthogonal-colour cube in B(λ) ⇔ [x,y]_W ⊆ W^J.** In crystal language: B(λ) ≅ Filt(heap of w_0^J) as coloured posets.
  An orthogonal-colour cube is an antichain of heap elements with distinct commuting labels.
- **So the dictionary is exact and exhausted.** In the minuscule case, "read P=1 off the crystal" = "read antichains off the heap". There's no more
  Seed Q2 content to mine on the orbit. If any exists, it is off-orbit (Q58, E6 ϖ_4). Don't open another orbit-side question.
- Probable owner of the whole dictionary: Boe 1988 / Proctor / Stembridge / Tenner-type Boolean-Bruhat work → Q59 locator pass (Wake 271).
