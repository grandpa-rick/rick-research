# Q56 scout (PROVE 269 compute agent, 2026-11-01). Grade: computed (m <= 5). Verdict: KILL for the specialisation hunch.

Script: `q56_scout.py` (run `python3 q56_scout.py M`). Outputs: `q56_scout_m4.out` (m<=4), `q56_scout_m5.out` (m<=5; ~2 s).

## Definitions used
- Pairs: strict ρ ⊆ λ, θ = λ/ρ, θ not an antichain, and D_{z_ρ,z_λ} ≠ ∅ (the (3.6) support of PROVE 268 Prop S).
  Counts: 1, 5, 20, 70 for m = 2..5 (26 pairs for m<=4, 96 for m<=5), matching q55_support.py.
- (3.6) coefficient: from printed Rem 4.20/4.22 (draft main.tex l.1330, 1386), Σ_{p∈D} e^{-p(1)} = (−1)^{|θ|} A_{λρ}.
  Non-equivariant: c = (−1)^{|θ|} N, with N = #D = #{μ : ρ⊆μ⊆λ, μ/ρ antichain, λ/μ antichain without diagonal box}.
  Also V(t) = Σ_μ t^{|λ/μ|}.
- Parabolic KL: Deodhar's R-recursion as in `proofs/prove268/q55.py` (`parKL`, copied as `parKL2` here so it also returns R).
  u=q: fac = −1 in the "stay" case. Cross-checked in q55.py (m<=4, 0 bad) against Σ_{u∈W_J}(−1)^{ℓ(u)} P_{σu,τ}.
  u=−1: fac = q. Cross-checked against P_{σw_J,τw_J}.
  Primary indexing is z: interval [z_λ, z_ρ] (the (3.6) one). w-indexing [w_ρ, w_λ] is reported as a convention control.
  Full-W P_{z_λ,z_ρ} is also reported, for m<=4 only.
- ℓ(z_ρ)−ℓ(z_λ) = |θ| on every row, so "(−1)^{Δℓ}X = c" means the same as "X = N".

## Results
- **N = 2^{#isolated off-diagonal boxes of θ}** on 96/96 pairs. This restates the printed V-map lemma; it is not new.
  N ∈ {1,2}: N = 2 on 1/26 pairs (m<=4) and 10/96 pairs (m<=5). So c = ±1 almost always.
- No candidate matches c on all pairs under c=X, c=−X, c=(−1)^{Δℓ}X or |c|=|X|. Best scores, out of 26 for m<=4 and 96 for m<=5:
  - P^{J,−1}[z](±1): 20/26 and 68/96.
  - P^{J,−1}[w](±1): 23/26 and 74/96.
  - P_full[z](±1): 23/26.
  - P^{J,q}[z](±1): 1/26 and 6/96. P^{J,q}[z] = 0 on most of these pairs, as K0 forces a zero constant term off the seam.
  - R^J (either u, either indexing) at q=±1: 0 matches. In the u=q convention R^J(1) is identically 0 on these pairs.
- Negative control (seeded shuffle of each candidate column) gives the SAME best scores: 20, 23, 74 and 66–78. So the partial
  P^{J,−1} agreement is base rate (|c| = 1 and P^{J,−1}(1) = 1 are both common). It is not signal.
- Polynomial level: V(t) = ±P never holds for P^{J,q}[z], P^{J,−1}[z/w] or P_full. It holds for P^{J,q}[w] on 4/26 and 14/96.
- Concrete mismatches: the N=2 pairs, e.g. m=4, ρ=(3), λ=(4,2), have P^{J,−1} = 1 in both indexings. Many N=1 pairs have
  P^{J,−1}[z] = 1+q, so the value at q=1 is 2. At m=5 one pair has P^{J,−1}[z] = 1+2q+q^2.

## Verdict
The kill criterion is met at m = 4 and confirmed at m = 5. The (3.6) coefficient on non-Boolean pairs is not P^J(±1) or R^J(±1)
in either Deodhar convention or either indexing, up to sign or (−1)^{Δℓ}. It is a count of isolated off-diagonal boxes,
which comes from the V-map description, not from KL. Caveat: this checks only the non-equivariant coefficient. Equivariant
or q-graded versions (for example V(t) against a q-shifted P^J) were tested only as the literal tuple comparison above.
