# Question — Is A^{(2)} (Nazarov-Sklyanin, Thibon 2608.30791) equal to p_2(Y) in Hikita's level-1 AHA polynomial rep, up to a monomial (q,t)-rescaling?

**Status:** CLOSED — REFUTED Day 200 + Day 201.
- **Vertex A (A^{(2)} = p_2(Y) via Thibon 2608.30791):** REFUTED Day 200 both readings. (a) 𝔮-scaling mismatch (F·1 ≠ 0 while A^{(2)}·1 = 0). (b) Spectral: direct SymPy at m=3 confirms non-equivalence.
- **Vertex B (Jack P_2^{(N)} via Thibon 2609.10284):** REFUTED Day 201 both readings. (a) Degree mismatch: Rick's p_2(Y) is degree +2 on X; Thibon's Δ_2(α) is degree 0 (different graded pieces). (b) Spectral: F(spec_λ)|_{ε¹} is linear in |λ| (m=5 SymPy: F(spec_(2)) = F(spec_(1,1)) at ε¹); Thibon's 2 C_1^{(α)}(λ) is quadratic in λ_i.
- **Vertex C (shuffle Δ_2):** dormant. Same degree-0 signature as Vertex B; likely to die on same obstruction.

**Route R5 essentially exhausted.** New primary analytic route is R6 (Bechtloff-Weising 2310.10249) — see `q-BW-2310-EHA-descent.md`.

**Original priority:** ★★★★ (Day 200 primary target).
**EV assessment (retrospective):** the pre-test 50-60% estimate was too high. Structural mismatch (degree, eigenvalue-polynomial-degree) should have been checked *before* Kostka expansion. New auto-memory template: **operator-shape audit** = (degree on X) × (eigenvalue-polynomial-degree in λ_i) before identification.

## The precise identification

Let $A^{(2)}$ denote the second Nazarov-Sklyanin operator on $\Lambda_{q,t}$, per Thibon 2608.30791. Acts diagonally on Macdonald $P_\lambda$:
$$A^{(2)} \cdot P_\lambda \;=\; t^{-1} \cdot P^*_{(1,1)}(q^{-\lambda}; q^{-1}, t^{-1}) \cdot P_\lambda \;=\; \sum_{\square \in \lambda} c_{q,t}(\square)^2 \cdot P_\lambda,$$
where $c_{q,t}(\square)$ is the $(q,t)$-content of box $\square$ in the Young diagram of $\lambda$.

**The claim to test:**
$$A^{(2)}(F(X)) \;\stackrel{?}{=}\; c_{q,t} \cdot \bigl(p_2(Y) \bullet F(X)\bigr) \qquad \forall F \in \Lambda_{q,t},$$
where $c_{q,t}$ is a monomial in $q, t$ (a global normalization, allowed to be unknown/fitted).

## Why this should be true

Cherednik $Y_i$ acts on the level-1 polynomial rep as (roughly) $q^{-\text{shift}_i} t^{\text{content}_i}$ up to conjugation by $T$-generators. So $Y_i^2$ carries "squared content" structure. $p_2(Y) = \sum_i Y_i^2$ globally sums this, matching $A^{(2)}$'s $\sum_{\square} c(\square)^2$ eigenvalue formula.

**Structural argument.** $A^{(2)}$ is defined so that it commutes with the DAHA action (Nazarov-Sklyanin construction). $p_2(Y)$ lives in the Cherednik commutative subalgebra $\mathbb Q_{q,t}[Y_1, \ldots, Y_m]^{S_m}$ (symmetric functions in $Y$'s), which also commutes with itself. Both are content-symmetric operators.

## Test protocol (SymPy, m=3 or m=4, r=2)

### Setup
1. Compute $p_2(Y) \bullet e_r(X)$ in Hikita's level-1 rep for $r = 2$ at $m = 4$ (already done Day 198; result = Lemma 1 with $\tau_2 = -(q^2-1)(t^2+1)(qt^3-q+t+1)/q^3$).
2. Compute $A^{(2)} \cdot e_r(X)$ via:
   a. Expand $e_r(X) = \sum_\lambda K_{\lambda r}(q,t) P_\lambda(X; q,t)$ using $(q,t)$-Kostka coefficients (finite sum, computable in SymPy via Macdonald polynomial recursion).
   b. Apply $A^{(2)}$ diagonally: $A^{(2)} \cdot P_\lambda = t^{-1} P^*_{(1,1)}(q^{-\lambda}) \cdot P_\lambda$. Explicit eigenvalue = $\sum_{\square \in \lambda} c_{q,t}(\square)^2$.
   c. Transform back to $e$-basis.
3. Compare $A^{(2)} \cdot e_r$ vs $p_2(Y) \bullet e_r$ (Lemma 1) up to a common monomial $(q,t)$-factor.

### Test at r = 2

Partitions of 2: $(2), (1,1)$. Kostka expansion:
$$e_2 \;=\; K_{(2), (1,1)}(q,t) P_{(2)} + K_{(1,1), (1,1)}(q,t) P_{(1,1)}.$$
Content of boxes:
- $\lambda = (2)$: boxes at $(1,1), (1,2)$; contents $0, 1$ (classical) → $q,t$-contents.
- $\lambda = (1,1)$: boxes at $(1,1), (2,1)$; contents $0, -1$.

Apply $A^{(2)}$ eigenvalues; recombine. Should give a 4-term expression in $e$-basis. Compare against Rick's Lemma 1 at r=2.

### Three outcomes

- **YES (probable):** analytic identity $A^{(2)}(F) = c_{q,t} \cdot (p_2(Y) \bullet F)$ holds with computable $c_{q,t}$.
  - Consequence: Lemma 1 becomes `proved` via Thibon 2608.30791 Thm 2.3.
  - DS(r, 1, 1) becomes analytically proved for all r ≥ 2 (Day 198 decomposition + Lemma 1 + Day 191 SP).
  - FPSAC anchor: "new p_2(Y)-Pieri Lemma proved via Nazarov-Sklyanin identification".
- **NO — normalization off:** identify the correct rescaling. Likely fixable (Hikita convention $Y = Y^{DAHA,-1}$ standard mismatch).
- **NO — structural mismatch:** $A^{(2)}$ acts on Macdonald basis differently than $p_2(Y)$ acts on the level-1 polynomial rep. Kill Vertex A; move to Vertex B (Jack) then Vertex C (shuffle).

## Estimated probability of YES

**50-60%** (per Day 199 dream). High structural plausibility. High normalization risk. Content-based eigenvalues match. Basis conversion (e-basis ↔ P-basis via Kostka) may hide subtleties.

## Cost estimate

**1-2 hours** for SymPy protocol. Bottleneck is $(q,t)$-Kostka coefficient computation, which is standard but slow in SymPy for m ≥ 5.

## Fallback: Vertex B check in parallel

If Vertex A takes longer than expected, run Thibon 2609.10284 §7.1 Jack-level $P_2^{(N)} \cdot e_r$ in parallel (~1 hr). Even a shape-match (4 terms, 3 r-independent) at Jack level is strong evidence.

## Cross-references

- `connections/2026-09-16-thibon-triangle-p2Y-candidates.md` — full triangle discussion (Vertex A here).
- `connections/2026-09-16-p2Y-pieri-newton-independent-atom.md` — why $p_2(Y)$ is the canonical missing input.
- `reading/2026-09-16-browse145.md` — Browse 145 with Thibon 2608.30791 resurfacing.
- `proofs/2026-09-17-day198-DS-211-via-p2-pieri.md` — Day 198 writeup with Lemma 1.
