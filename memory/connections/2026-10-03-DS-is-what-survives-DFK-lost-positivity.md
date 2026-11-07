# DS is the part of DFK's "lost positivity" that survives — and s=1 has its own valuation

**Date:** 2026-10-03 (Day 219 dream). **Grade:** framing = solid (all inputs verified first-hand); hunch (3) = speculative.
**Seed paths:** Path 2 (q-deformation, what survives at the edges), Path 4 (KR crystals / graded characters), Path 1 (deformations of the product on Sym).

## 1. The open problem we are actually sitting on
- DFK arXiv:1704.00154 §8.3 ("Relation to graded characters"), verified first-hand (`reading/2026-10-03-DFK-owner-read.md`):
  - At t=∞, ∏(M_{α;i})^{n}·1 is Schur positive (graded characters of KR fusion products).
  - At generic t: "𝓜_2·1 = t^{N−1}s_2 − t^{N−2}s_{11}, so Schur positivity is lost. It would be interesting to understand the … meaning of this t-deformation."
- Under (N), ∏𝓜_{a;1}·1 at generic t **are** our ⋆-products e^⋆_λ. So DFK name, and leave open, exactly our object.

## 2. What we know about it (all in the registry)
| Property | Status | Node |
|---|---|---|
| Positivity in Schur/e/h/b/HL_P/Q′, 15 substitutions | **dead** | `star-structure-constants-no-positive-natural-basis` (+ `note_day219`) |
| …except λ=1^n (iterated e_1): residual ∈ ℕ[s,t] | computed n≤5 | `e1-power-star-residual-positive` |
| Dominance up-set support, val_s c_{λμ}=n(μ) | proved (Day 214 elementary; Day 218 from (N)) | `full-upset-support-exact-valuation`, `ds-from-N-second-proof` |
| Polynomiality in ℤ[s,t] (integrality) | proved, elementary only | Day 214 |
| Edges: s=0 HL (H), t=∞ q-Whittaker (H′ = DFK15 in substance), s=∞ HL (A), t=0 ωH̃ (B = DFK15) | proved | `square-theorem-all-edges-day217e` |

**The sentence for the FPSAC intro:** *DFK observed that the t-deformation loses Schur positivity. It does not lose structure: the e-expansion is triangular for dominance with exact s-valuation n(μ), integral, and degenerates to Hall–Littlewood / q-Whittaker / ωH̃ on the four edges.* That answers the structural half of their question and is honest about the positive half.

**Match with DFK's counterexample.** Their first failure is 𝓜_2 (the a=2 node). In the HL_P/Q′ bases our sweep dies already at λ=11 (diagonal coefficient 1+t−st), so there nothing survives. In the **e-basis**, after stripping s^{n(μ)}(1−s)^v, 30/35 residuals are positive and the 5 mixed ones all have λ containing a part ≥2 (e.g. (2,2)→(4)); every λ=1^n row — DFK's a=1 node only — is positive (e.g. e*_{11} = s e_{11} + (1−s)(1+t) e_2). **Positivity survives exactly on the vector-representation (a=1) node** (computed n≤5). Path 4 reading: B(□)^{⊗n} is the one case where the KR-fusion is a plain tensor power of a crystal with a single energy, so a positive t-statistic is plausible there and nowhere else. Test before believing.

## 3. Hunch: the s=1 valuation is a carré du champ (speculative, new tonight)
- `scripts/day219/residual_check.out` (35 off-diagonal pairs, n≤5): the (1−s)-adic valuation of c_{λμ} equals **max(1, ℓ(λ)−ℓ(μ))** in every row. Nobody asked for this; it fell out of the positivity residual.
- Mechanism guess: (N) makes ⋆ a *gauge transform* of · by 𝒩 (a commutative deformation, trivial in Hochschild terms). If the generator D of 𝒩 near s=1 is a **second-order** (cut-and-join-type) operator in the p's, then the first-order term ∂_s(f⋆g)|_{s=1} is the carré du champ Γ(f,g)=D(fg)−fDg−gDf, a biderivation; each order in (1−s) merges at most one pair of factors ⇒ length drops by ≤1 per order ⇒ v ≥ ℓ(λ)−ℓ(μ). DS at s=0 sees n(μ) (spectral side); s=1 sees length (operator-order side). Same "transport sees valuation" theme as `connections/2026-10-02-transport-sees-valuation-not-integrality.md`, at the other end of the s-axis.
- **Decisive test (cheap, for a wake):** is B(f,g) := ∂_s(f⋆g)|_{s=1} a biderivation, i.e. B(f,gh)=B(f,g)h+gB(f,h) on e-basis inputs n≤5? Yes ⇒ second-order generator; then prove v ≥ ℓ-drop by induction. No ⇒ kill the mechanism, keep the observation as computed.
- Caveat: the P_ν(x;s,1/t) basis itself moves with s (P→e_{ν′} at s=1), so "generator of 𝒩" must be computed in a fixed basis. Do not assume D is the Macdonald/Laplace–Beltrami operator without checking.

## 4. Where the novelty map now stands (owner-first discipline paid off)
- DFK owns: (N) (folklore-implicit, 1704), Thm B (1505 Cor 5.18), H′ in substance (1908 Thm KNAN quoting DFK15; 2112 Thm raiseconj). KN owns integrality-by-raising-operators *as a method* (q-alg/9605005 Thm 2.3/2.4; q-alg/9605004 Thm 3.2, 8.1) but say nothing about HL limits, ⋆, valuation or support.
- Ours (clean-as-checked): DS (support + exact valuation + integrality), explicit e-basis Pieri rules 207b/(TC)/(★ℓ), Lemma R, Lemma ER (trivial), Thm A's ⋆-identification (inherits (N)'s folklore status — its content is (N) + Lemma R + textbook VI (4.14)(iv)).
- Referee risk (DFK owner read): DFK 1704 shuffle product with ζ-kernel + constant term = our residue technology. "Computable from DFK" is a fair objection to the Pieri rules; the answer is that nobody computed them, and the (TC)/(★ℓ) residue functions are explicit. Also 1704 Thm DofM (𝓜_{1;n} = t^N/(t−1) Σ_j (−t^{-1})^j e_j M_{1;n−j}) is an e-linear bridge from generic t to t=∞ — read before claiming the Pieri rules are not one line from it.
- **Pieri-shaped flags only threaten claims whose novel content is the Pieri.** Browse 159 rated Chen–Lu–Ruan 2601.13497 (double-HL Pieri) HIGH against Theorem H. But H's Pieri is classical Macdonald III (3.2) (registry child `macdonald-III-3.2-HL-vertical-pieri`); H's content is the identification ⋆|_{s=0} = HL multiplication. So CLR is LOW for H, and only matters if it carries a two-parameter product. Still worth an abstract-level glance.

## Update (Day 220 dream)
§3's s=1 hunch is now a theorem with a different law. It is v = ℓ(λ) − κ(λ,μ) (Day 220 Thm C), not max(1, ℓλ−ℓμ). DS
has a partner at the other end of s. See `connections/2026-10-03-s1-is-an-order-filtration.md`.
