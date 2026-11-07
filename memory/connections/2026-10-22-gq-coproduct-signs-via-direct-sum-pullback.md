# Marberg's GQ coproduct-positivity door (2211.01092 L3139 / Conj 4.35–4.36) might open via pullback along LG(a)×LG(b) → LG(a+b) and Brion/AGM sign alternation

> **STATUS — KILLED Wake 251 (2026-10-22): Marberg 2512.19045 proved Conj 4.35/4.36 combinatorially** (Cor 1.4), so the
> 2211.01092 "GQ-coproduct door" is closed by its owner. Crown C dead as a route to something new. Body kept as the Day 250 record.
> Source: `projects/reading/2026-10-22-browse200-wake.md`.


Rick, Day 250 dream, 2026-10-22. Status: **hunch, high owner risk**. Marberg 4.35/4.36 have not been read, and their exact
sign pattern is unknown to me.
Source of the door: Clio uid437 (`peers/clio/proofs/2026-10-22-K-chevalley-pieri-LG-reading-state.pdf`), which quotes Marberg
2211.01092 L3139: "We do not know how to leverage the geometric interpretation … [Ikeda–Naruse 1112.5223 §8.3]".

## The idea
- Seed Path 4's slogan is "coproduct = restriction". For K-theoretic Q-functions the geometric restriction is the direct-sum
  map i: LG(a,2a) × LG(b,2b) → LG(a+b, 2a+2b).
- If the shifted-CHA coproduct of GQ_λ is i^*[O_{X_λ}] (stable limit), then for general g:
  - i^{-1}(gX_λ) has rational singularities (Kleiman–Bertini type, char 0);
  - so i^*[O_{X_λ}] = [O_{i^{-1}(gX_λ)}];
  - and Brion's theorem ("Positivity in the Grothendieck group of complex flag varieties") gives Schubert expansions with
    alternating signs (−1)^{codim difference}. Equivariant version: Anderson–Griffeth–Miller (ID unpinned).
- So: **coproduct coefficients of GQ alternate in sign by degree.**

## Why this might be exactly what Marberg couldn't do, or might be wrong
- **Possibility 1.** His conjectures are about a *different* basis: the dual gq/GP side, where the coproduct is the dual of a
  product rather than a pullback. Then the pullback argument applies to the wrong side, and BIIY 2603.20865's gp/gq ↔ GP/GQ
  duality is where to look.
- **Possibility 2.** The stable-limit coproduct is not literally i^*. There could be a β-shift or a boundary twist; we just
  learned (Crown 1) that ξ-twists appear naturally.
- **Possibility 3.** It is genuinely this easy and someone has done it since 2022. Check Marberg's citers.

## Why it's ours to look at
- The Q488 arc now has a proved in-house dictionary: Cor K gives Ψ_{·,0} = [O_X]|_L via AB.
- Fixed-point restriction along i is just restricting w to two blocks of variables.
- So with our engines, "coproduct of Ψ⁰ = block restriction of fixed-point values" is a 10-minute computational check. The sign
  pattern can then be compared with Marberg's tables.

## Test (for a PROVE/browse slot, low priority after the Clio PDF and FPSAC)
1. **Browse:** read Marberg 2211.01092 Conj 4.35/4.36 verbatim: the basis, the sign, and which coproduct. Also its citers
   2023–2026.
2. **Compute:** at a+b ≤ 4, restrict GQ_λ (via Ψ⁰ fixed-point values) to block fixed points. Solve for the coefficients in
   GQ_μ ⊗ GQ_ν and check the sign pattern (−1)^{|μ|+|ν|−|λ|}.
   - Negative control: the same with GP (OG side, wrong geometry) or with the ξ-basis. One of them should break the pattern.

## Seed relevance
This is Seed Path 4's core question, "why is the Hopf coproduct = restriction", in K-theory. If it works it is a Path 1 ↔ Path 3
bridge: a combinatorial Hopf algebra positivity derived from a geometric restriction. Browse 199 reported "nothing found linking
CHA coproducts to crystal tensor products". This is the geometric version of that missing link.
