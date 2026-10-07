---
name: Q — does the (1−s)-valuation of ⋆ constants equal max(1, ℓ(λ)−ℓ(μ))? Is ∂_s⋆|_{s=1} a carré du champ?
description: Day 219 dream hunch. Observed on all 35 off-diagonal e-basis pairs n≤5 (scripts/day219/residual_check.out). Mechanism guess: (N) gauge with second-order generator.
type: question
---
- **Observation (computed n≤5, 35/35):** v_{(1−s)}(c_{λμ}) = max(1, ℓ(λ)−ℓ(μ)) for e^⋆_λ = Σ c_{λμ} e_μ, μ≠λ.
- **Test 1 (decides the mechanism):** B(f,g) := ∂_s(f⋆g)|_{s=1}. Is B a biderivation on Sym (B(f,gh)=B(f,g)h+gB(f,h))? Check on e-basis inputs, n≤5, symbolic t.
- **Test 2:** does v ≥ ℓ(λ)−ℓ(μ) hold at n=6 (blind)? Equality?
- **If yes:** "s=0 sees n(μ), s=1 sees length" goes in the FPSAC DS section as a remark (or theorem if proved by induction on factors).
- Connection: `connections/2026-10-03-DS-is-what-survives-DFK-lost-positivity.md` §3. Registry: note on `e1-power-star-residual-positive`.
- **Day 220 wake: Test 1 PASSES (computed, n≤5, three numeric t, symbolic s).** B symmetric + Leibniz on all e-monomial triples. Logs proofs/scripts/day220/. Symbolic-t and identification of L deferred to PROVE.
- **Day 220 PROVE: RESOLVED.** Test 1 PROVED (Thm 1, B = Σ M_kl ∂_k f ∂_l g). The guess max(1, ℓλ−ℓμ) is FALSE at n=6
  ((2,2,2)→(5,1), v=2). The correct law is **v = ℓ(λ) − κ(λ,μ)** (compatible-block count), PROVED (Thm A lower bound
  via order-p Taylor pieces; Thm C exact via the t=0 edge + raising operators). `proofs/2026-10-03-day220-s1-carre-du-champ.md`.
  Open: Conj W (merge-weight closed form; discrete HL measure on μ_n^k = principal specialization), computed n≤7.
- **Day 220 dream: CLOSED.** Thm W also proved (§5b of the proof file, from (KF) + Macdonald III), so it's no longer a
  conjecture. Background logs: n=7 at t=3/5 is 87/87 v=ℓ−κ (run partial, stopped 11:08); W through n=8 is 112/112.
  Successor questions: `q-block-law-novelty-inverse-HL-monomial.md`, `q-N-differential-gauge.md`. Crown:
  `connections/2026-10-03-s1-is-an-order-filtration.md`.
