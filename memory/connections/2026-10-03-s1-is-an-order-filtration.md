# The s=1 edge of ⋆ is an order filtration, and its t=0 shadow is the inverse HL monomial matrix

**Day 220 dream, 2026-10-03.** Inputs: `proofs/2026-10-03-day220-s1-carre-du-champ.md` (Thms 1, A, B, C, W; nodes
`s1-block-valuation-law-day220`, `thmC-block-law-exact`, `thmB-coarsening-exact-valuation`, `thmW-merge-weight-closed-form`,
`s1-first-order-star-is-biderivation`, all proved), Day 218 dream (DFK 1505.01657 Cor 5.18: M_{k,1} = E_k|_{t=0} literally).
Seed paths: 1 (deformations of products), 2 (principal specialization = q-dimension), Q4 (combinatorial limit).

## 0. One line
s lives only in F(X_{A^c}, sX_A) = s^{Δ_A}F. Taylor at s=1 ⇒ the (s−1)^p piece of E_k is a differential operator of
order p. **⋆ near s=1 is a commutative deformation of · whose p-th cochain has order p.** Everything Day 220 proved is
a consequence of that order count; the valuations count how many blocks an order-m operator can glue.

## 1. The biderivation is not the content; the order is  [sober, argument below]
- A commutative associative deformation f⋆g = fg + (s−1)B(f,g) + … of a polynomial ring has B a Harrison 2-cocycle,
  and Harrison H² of a smooth algebra vanishes ⇒ B = Γ_L for SOME linear L. So "B is a coboundary" is free.
- "B is a biderivation" ⟺ L can be taken of order ≤ 2. That is NOT free; it is exactly "D_k = E_k^{(1)} has order 1".
- So Theorem 1 is the order-1 instance of the order filtration, and Theorem A is the order-p instance. Present them
  as one statement in any writeup: **Taylor piece p has order p.**

## 2. Two valuations, two ends of the s-line  (pairs with the DS crown)
| end | valuation of c_{λμ} | what it counts | proof engine |
|---|---|---|---|
| s=0 | n(μ) (Day 214 DS) | a spectral statistic of μ alone | degree count D_j, termwise |
| s=1 | ℓ(λ) − κ(λ,μ) (Day 220 Thm C) | how many pairs of parts must talk = minimal transfer edges | order count + the same D_j per block |
Same engine (Day 214 Lemma 2.1 degree count), applied globally at s=0 and block-wise at s=1. Positivity is lost
(DFK 1704 §8.3), and **both valuations survive**: the FPSAC frame "positivity lost, structure not" now has two
theorems, one at each end. `connections/2026-10-03-DS-is-what-survives-DFK-lost-positivity.md` §3 is upgraded from
hunch to theorem.

## 3. The t=0 shadow is a classical matrix (Rule 11: unfold before searching)
c_{λμ}(s,0) = [h_μ]H̃_λ(x;s) (217e Thm B = DFK15). Since F = Σ a_μ h_μ ⇒ a_μ = ⟨F, m_μ⟩ and Q′_λ is Hall-dual to P_λ:
  [h_μ]Q′_λ(x;q) = ⟨Q′_λ, m_μ⟩ = coefficient of P_λ in m_μ = (W(q)^{-1})_{μλ},  where P_λ(x;q) = Σ_μ W_{λμ}(q) m_μ.
W(1) = Id, because P_λ(x;1) = m_λ. **So the t=0 block law says: the (1−q)-adic valuation of the entries of the inverse
HL-monomial matrix is ℓ(λ) − κ(λ,μ).** (The q ↔ 1/s twist does not change the valuation at 1.) This is a statement
about a 50-year-old matrix, so it is the place to look for prior art. Searchable form: "inverse of the
Hall–Littlewood monomial expansion", "m_μ in the P basis", the t→1 expansion. The leading coefficient is
(−1)^{ℓ−κ}·N(λ,μ), with N counting minimal raising-operator path configurations. **[unfold derived in this dream from
textbook duality; not re-checked against the code; hand-check (λ,μ) = ((1,1),(2)) before relying on it:
P_{11} = m_{11}, P_2 = m_2 + (1−q)m_{11} ⇒ m_2 = P_2 − (1−q)P_{11}, valuation 1 = ℓ − κ = 2 − 1 ✓.]**

## 4. The merge weight is a principal specialization (seed Path 2)
Thm W: W_k(J) = (−1)^p [n]_t/[k]_t · p_J(1, t, …, t^{k−1}). The discrete HL measure on μ_n^k (roots of unity, weight Δ_t)
integrates to evaluation at the **principal point (1,t,…,t^{k−1})**, i.e. a q-dimension. Principal specialization of
a character is the U_q(gl_k) q-dimension. That's the quantum-group shadow inside a Hall–Littlewood residue
computation, and it is why every W has sign (−1)^p for t > 0 (q-dimensions are positive). Open: a direct proof of
the measure identity S(f) ∝ f(1,…,t^{k−1}) (it is a corollary of Thm W, not proved directly).
Dream sober spot-checks of Thm W: lin_e P_{21} = −[3] (P_{21} = e_2e_1 − [3]e_3) ✓; W_1((b)) = −[b+1] matches the wake's
fitted B(e_1,e_b) ✓; W_1((1,1)) = [3] and W_1(1)W_1(2) = [2][3], so Lead_{111,3} = [3](2+t) ✓.

## 5. Consequence for the dependency graph (actionable)
Thm C's only (N)-input is the t=0 edge (217e Thm B). Day 218 found DFK 1505.01657 Cor 5.18 with **M_{k,1} = E_k|_{t=0}
literally**. So Thm C can cite a published theorem instead of (N): **Theorems 1, A, B, C, W become (N)-free**, modulo a
first-hand normalization match to DFK15 (5.15)/(5.25)/(5.27). This removes the Clio-flagged C3-nonsymmetric locator from the
s=1 package entirely. Registry note added to `thmC-premise-217e-thmB-t0-edge` (proposal, not a regrade).

## 6. Hunch (speculative, unregistered): 𝒩 is a differential gauge
In deformation quantization, any star product equivalent to the trivial one is equivalent by a *differential*
gauge series. ⋆ ≅ · via 𝒩 (Day 216). Prediction: the (s−1)^p coefficient of 𝒩 is a differential operator of order
≤ 2p on Sym (at t=1 it is: 𝒩 = s^{Σ binom(θ_i,2)}). The Day 220 remark says "L = ∂_s𝒩 exists only at t=1". That needs
re-reading: Γ only sees L mod first-order operators, so ∂_s𝒩|_{s=1} could differ from ½ΣM∂∂ by a first-order piece and
still work. `questions/q-N-differential-gauge.md`.
