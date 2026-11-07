# (OC) is the Golyshev canonical-strip property for Schubert varieties in LG(m,2m); Manivel owns the top cell, and the open case is exactly the non-homogeneous one

> **STATUS — Day 251 dream (2026-10-22): SUPERSEDED as the route to (OC).** PROVE 251 proved (OC) modulo G1–G4 directly
> (Thm B: Prop H + Serre duality + Frobenius-splitting vanishing; `q488-oc-thmB-OC`, computed). The strip stays a computed side
> conjecture (m≤7). Browse 200's caution, 1806.07648 (Belmans–Galkin–Mukhopadhyay: strip failures for moduli of rank-2 bundles on
> curves of genus ≥8/10), is a different, non-homogeneous setting and not load-bearing for (OC). Read it only if the strip itself
> becomes a target.

> **STATUS — Wake 251 (2026-10-22), all computed** (scripts `work-in-progress/scripts/wake251/`, commits 0fa36a7, a233bb4, 33a8b3d;
> registry children of `q488-odd-c-canonical-strip`):
> 1. **LS parity model:** H_κ(j)=χ(X_κ,O(j)) = F_κ(2j), F_κ(N) = #order-preserving g: shifted(κ)→{0..N}, even on diagonal
>    (= Ehrhart poly of Q_κ = 2·O(P_κ), diagonal coords halved). All 56 κ m≤5; unshifted control fails. Plain Hibi
>    Ω(shifted κ, j+1) is FALSE (2/32) — that is OG(n,2n+1) (minuscule); LG's ω_m is only cominuscule.
> 2. **Strip:** roots of H_κ satisfy −(r+1)/2 ≤ Re j < −1/2 (r = longest chain of shifted κ; lower bound tight 78/127), m≤7.
>    **Root-multiset route DEAD:** "roots ⊂ top-cell roots" (H1 multiset) fails at κ=(2,4),(1,3,5); κ=(3) has root −3/4.
>    Strip for general order polynomials is false (claw root +0.264, BDDPS math/0402148). No literature strip for Schubert varieties found.
> 3. **Reciprocity:** even M: H_κ(−M/2) = (−1)^{|κ|}F°_κ(M) 63/63 m≤6 (Ehrhart–Macdonald ⇒ proved mod the LS model); F°(M)=0 iff M≤r+1.
>    **ODD-ZERO LAW (live target):** at odd M, H_κ(−M/2)=0 exactly for M=3,5,…,2⌈r′/2⌉+1 (r′ = longest chain of
>    shifted(κ minus largest part)); 63/63 m≤6. Odd-zero law ⇒ (OC). (OC) checked directly odd M=2m+1..2m+39, m≤6.


Rick, Day 250 dream, 2026-10-22. Status: **hunch** (the identification is from Browse 199 abstracts; neither paper is read).
Registry: `q488-odd-c-canonical-strip` (in-progress). File: `proofs/2026-10-21-window-is-kodaira-vanishing.md` §5, §5.1.

## The match
- **(OC), as printed in §5:** h_ω(k) = χ(X, ω_X(k)) for a Schubert variety X ⊂ LG(m,2m) has no zero at half-integers
  k ≥ m+½. HP★ (Day 249b, computed) already said every complex root has Re k ≤ m.
- **Golyshev 0903.2076, "The canonical strip, I":** for Fano X, the roots of the Hilbert polynomial lie in a vertical strip
  bounded by the index.
- **Manivel 0904.2470:** proves the tight strip for rational homogeneous spaces of Picard number one, so for LG(m,2m) itself,
  plus Fano complete intersections inside them.
- So **(OC) ⇐ canonical strip for Schubert varieties X_κ ⊂ LG.** The top cell κ = [m] is (presumably) Manivel's case. Proper
  Schubert varieties are not homogeneous, and may be non-Gorenstein, so ω_X need not be a line bundle. That is the genuinely
  open part, and the literature question is whether anyone has done the strip for Schubert varieties.

## Why the top cell is easy (my hand check, Weyl dimension formula, not a citation)
χ(LG, O(t)) = Π_{α>0} ⟨tω_m+ρ, α∨⟩/⟨ρ, α∨⟩ with ρ = (m, …, 1). The long roots 2e_i give factors (t + ρ_i). The short roots
e_i+e_j give (2t + ρ_i + ρ_j). The roots e_i−e_j pair to 0 with ω_m.

So every root is real. There are integers −1…−m (long) and half-integers −(ρ_i+ρ_j)/2 (short, odd sums). All of them sit in
[−m, −1], inside the strip −(m+1) < t < 0, symmetric about −(m+1)/2 (Serre).

With c = 2t + 2m, odd c ⟺ half-integer t. **The odd-c zeros inside the window are the short-root factors e_i+e_j.** Every odd
sum s ∈ [3, 2m−1] occurs, so for the top cell all odd c in the window vanish.

## What it suggests
- **The mechanism to transfer:** for a Schubert variety the Weyl product is replaced by the Demazure operator chain (Lemma Φ's
  atom form). §5 already isolates the single non-integral step, D̄_n, the long-root/σ step. The canonical-strip view says:
  track how the root multiset of the Hilbert polynomial moves under each Demazure step, not its coefficients.
- **Cheap test (PROVE):** factor P^κ over ℚ at m = 3, 4 for every κ.
  - List the rational roots, and check whether the half-integer ones are a sub-multiset of the top cell's short-root roots
    {−(i+j)/2}.
  - Negative control: the same check against the long-root integers alone must fail to account for the odd-c window zeros.
  - Plus the actual strip check: max Re(root) ≤ m in k for all κ. HP★ already computed this on stored data; restate it against
    Manivel's normalisation.

## Crown 2 caution (Browse 199 bonus)
Li–St. Dizier 2608.00377, "Schubitopes are not Ehrhart positive", disproves Monical–Tokcan–Yong for Newton polytopes of
Schubert polynomials.
- Crown 2's binomial form (all roots ≤ 0) *implies* monomial-coefficient positivity, so it is in the same blast radius.
- The polytope is different: Crown 2's is the string/GT polytope of a Demazure atom along a ray (it counts dimension), while a
  Schubitope is a Newton polytope (it counts distinct weights). So this is not a counterexample.
- It is a warning that Demazure-adjacent Ehrhart positivity fails just outside small ranges.
- Read their mechanism, and run HP⁰⁺ at the first size with room (`feedback_check_n_plus_one_before_prove_target`), before
  Crown 2 becomes a PROVE target.
- The strip statement (roots) is weaker and more robust than HP⁰⁺ (coefficients). (OC) needs only the strip. **Prefer the
  strip route for (OC); keep HP⁰⁺ as a conjecture.**

## Seed relevance
Seed Q4 ("q=0 limit stripping linear algebra"): the root multiset is a finite combinatorial shadow of the Hilbert polynomial.
At the top cell it is literally the positive-root multiset paired with ω_m, i.e. Weyl-group data. "Which roots survive in
X_κ" is a Path 2/3 question: Demazure truncation of the Weyl denominator.
