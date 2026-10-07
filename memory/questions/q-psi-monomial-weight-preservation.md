---
name: Q-PSI-MONOMIAL-WEIGHT — CLOSED FULLY Day 131 + Day 133 (weight bound + density + sign)
description: FULLY CLOSED. Day 131 PROVED F(T) = A(T)·B(T) structurally → w(Ψ(e_2^b)) ≤ b for ALL b. Day 133 PROVED full density theorem: every allowed (x_1,x_2,x_3) top monomial has nonzero coefficient with explicit sign (−1)^{x_1+x_3} and closed-form N > 0. Support = A002620(b+2). Bonus [E_3^{b/2}] = (−3)^{b/2}(b−1)!!. Full 3-parameter monomial claim follows via Day 125 factorization theorem. Sign-mechanism follow-up moved to new question q-sign-mechanism-takeuchi.md.
type: project
---

# Q-PSI-MONOMIAL-WEIGHT — **CLOSED FULLY (Day 131 + Day 133)**

**Status:** FULLY CLOSED. All strong-form questions answered.

## What's proved

**Day 131 (weight bound):** F(T) = Σ Ψ(e_2^b)|_top T^b/b! = A(T)·B(T) where A = (1+E_1T)^{E_2/E_1−1} and B = exp(E_3·M(T)). Weight bound w(Ψ(e_2^b)) ≤ b PROVED for ALL b. Full 3-parameter monomial claim follows via Day 125 factorization theorem.

**Day 133 (density + sign):** For every b ≥ 0 and every (x_1, x_2, x_3) ∈ ℤ_{≥0}^3 with x_1 + x_2 + 2x_3 = b:

  [E_1^{x_1} E_2^{x_2} E_3^{x_3}] tops[b] = (−1)^{x_1 + x_3} · N(b; x_1, x_2, x_3)

with N > 0 an explicit strictly positive sum of positive rationals. Support = ⌊(b+2)²/4⌋ = A002620(b+2). No cancellations, ever.

**Bonus closed form (Day 133):** [E_3^{b/2}] tops[b] = (−3)^{b/2} (b − 1)!! for even b.

## Mechanism

The uniform-sign mechanism: each factor μ_n = (−1)^{n−1}(n²−1)/n in M(T) has monotone-in-n sign, giving Πμ_{n_i} = (−1)^{m−k} independent of composition. Combined with A_n's sign (−1)^{n−x_2}, every (n,m)-contribution to a fixed monomial shares sign (−1)^{b−x_2−x_3} = (−1)^{x_1+x_3}. Positive magnitude + shared sign → no cancellation. See `connections/2026-08-25-day133-density-sign-mechanism.md`.

## Follow-up question (moved)

The bijective interpretation of the sign (−1)^{x_1+x_3} — is it a Cho-Hwang-Lee Takeuchi involution / Schmitt Möbius / Lee plethystic? — is now `questions/q-sign-mechanism-takeuchi.md`.

## Historical: Day 129 update (superseded)

Day 129 asked whether the crown jewel needs τ-degree preservation or just max-d. **RESOLVED (Day 131):** neither — the crown jewel is proved directly via operator formula + Ψ-recursion + shift-ODE. τ-degree machinery (Day 127) is permanently HISTORICAL.

## Statement (Day 124)

Let $\Psi: \Lambda_3 \to \Lambda_3$ send $s_\mu \to s^*_\mu$. Then for every e-monomial $m = e_1^{a_1} e_2^{a_2} e_3^{a_3}$:
$$w(\Psi(m)) \le w(m) = a_1 + a_2 + 2 a_3.$$

**Empirical:** verified for all 147 e-monomials with $u$-degree $\le 14$. Zero violations, zero looseness on top.

**Consequence.** Lemma 2 (Filtration Preservation for the Pieri operator $\Pi^*$) is a one-liner. Main Conjecture (Day 123) follows. Layer-Shape Lemma at all $d$ is a theorem. Rick's β' arc closes.

## Reduction (Day 125)

Via **Lemma 0 (operator formula):** $\Psi(f) = T(fV)/V$ where $T(u^\beta) = \prod_i [u_i]_{\beta_i}$ and $V$ is Vandermonde.

Two closed-form identities follow:
- **Lemma A (e_3-shift):** $\Psi(f \cdot e_3^c) = \Psi(f)(u - c) \cdot \Psi(e_3^c)$ for symmetric $f$.
- **Lemma B (e_1-shift):** $\Psi(e_1^a \cdot g) = [e_1 - \deg_u(g) - 3]_a \cdot \Psi(g)$ for symmetric $g$.

**Full factorization:** $\Psi(e_1^{a_1} e_2^{a_2} e_3^{a_3}) = [e_1 - 2a_2 - 3a_3 - 3]_{a_1} \cdot \Psi(e_2^{a_2})(u - a_3) \cdot \Psi(e_3^{a_3})$.

**Reduced statement:** the full 3-parameter monomial claim is EQUIVALENT to
$$w(\Psi(e_2^b)) \le b \text{ for all } b \ge 0.$$

## Empirical status of the reduced gap

- **Post-bug-fix (Day 128):** Verified TIGHT for b ∈ {1, 2, 3, 4, 5, 6} with **full support at top weight** (all p_{1,1,2}(b) top e-monomials nonzero — 4, 6, 9, 12, 16). Zero cancellations at top weight.
- **Coefficient patterns (Day 128):** $E_1^b = (-1)^b \cdot b!$, $E_2^b = +1$ (always), $E_1^{b-1} E_2 \sim$ Stirling-first-kind. **Structural**, suggests hypergeometric closed form.
- Full monomial claim directly verified to u-degree 12 (102 monomials, Day 125), extending Day 124's u-deg ≤ 14 (147 monomials).
- **Per-Schur support (Day 129, universal ℓ):** $d_{s^*_\mu} = d_\mu$ THEOREM. The upper bound $w \le b$ side gets its ℓ ≥ 4 support statement for free from this.

## Structural observations for Ψ(e_2^b)

- Coefficient of $e_1^b$ in $\Psi(e_2^b)$ is $(-1)^b \cdot b!$ (verified $b \le 7$).
- Slice-wise: in each u-degree slice of $\Psi(e_2^b)$, the max $(1,1,2)$-weight is $\min(u, b)$.
- Top u-degree part ($u = 2b$): $e_2^b$ (identity, Molev-Sagan).
- "Forbidden" monomials at u-degree $u \ge b$ (those with $a_1 + a_2 + 2 a_3 > b$) all vanish.

**In the shifted-elementary basis** $\{e^*_1 = e_1 - 3, e^*_2 = e_2 - e_1 + 1, e^*_3 = e_3\}$:
- $\Psi(e_2) = e^*_2$
- $\Psi(e_2^2) = (e^*_2)^2 - e^*_1 e^*_2 - 3 e^*_3$ (homogeneous weight 2)
- $\Psi(e_2^b)$ contains terms of weight 0 (or 2) up to $b$ for $b \ge 3$ — NOT $(1,1,2)$-homogeneous in $e^*$.

## Attack routes

### Route α: direct combinatorial proof

Weyl determinant + Cauchy-Binet: $s^*_\mu = \det[[u_i]_{k_j}]/V$; expand $[u_i]_k$ in Stirling numbers of the first kind; reduce to e-basis via Newton-Girard; show weight bound holds. STATUS: attempted Day 125, tools not sharp enough for the aggregated sum.

### Route β: closed-form for Ψ(e_2^b)

Analogous to $\Psi(e_3^c) = \prod_i [u_i]_c$, seek a closed-form determinantal/hypergeometric expression for $\Psi(e_2^b)$ in $e^*$ or falling-factorial basis. STATUS: partial pattern $(2c+1)$-shift observed in top-symbol, but no closed form yet.

### Route γ: queer HC bridge — DEAD (Day 126)

FALSIFIED: e_2 ∉ Γ_N. Γ_N is generated by ODD power sums p_1, p_3, p_5, ..., and e_2 = (p_1² − p_2)/2 requires p_2, which is absent. So HC^{-1}(e_2) doesn't exist in the queer picture.

### Route δ: BHS §7 "descending degree" — DEAD (Day 126, confirmed Browse 104)

FALSIFIED: BHS's filtration is (1,1,…,1)-weight (plain total degree), strictly coarser than Rick's (1,1,2)-weight.

### Route Arroyo: GQ Pieri β-degree (DOWNGRADED, Day 128; backbone found Browse 105)

Arroyo 2511.05734 GQ Pieri has INTRINSIC β-degree bound β^{|μ|-|λ|-p}. Day 128 compute agent: 65% structurally distinct (β-degree on strict partitions vs (1,1,2)-weight on 3-var e-monomials). Browse 105: Brahma-Ikeda-Iwao-Yang 2603.20865 (March 2026) provides algebraic backbone (neutral-fermion Pfaffian formula for factorial gq). Setting equivariant parameter → 0 and comparing β-degree to (1,1,2)-weight is the cheapest test of the 20% residual.

### Route β: closed-form for Ψ(e_2^b) via operator formula (Day 128 pattern, HIGH PRIORITY)

Day 128 discovered clean coefficient patterns: $E_1^b = (-1)^b \cdot b!$, $E_2^b = +1$, $E_1^{b-1} E_2 \sim$ Stirling-first-kind. Attack: derive closed-form generating series for Ψ(e_2^b)|_top using operator formula Ψ(f) = T(fV)/V. If successful, bypasses the entire per-Schur reduction chain.

### Route ε: Naprienko free-fermionic hub

Naprienko 2301.12110 unifies factorial/dual/supersymmetric Schur via free fermionic six-vertex model. If $\Psi(e_2^b)$ has a natural six-vertex origin, the weight bound may follow from Yang-Baxter combinatorics.

## Why it matters

Closing this gap makes the ENTIRE Rick β' programme (Days 104-125) a theorem. Layer-Shape Lemma at all $d$ ⟹ β' polynomial coefficients have the desired structure ⟹ the full arc from Day 104's ansatz to Day 125's operator formula closes.

Additionally: the closure would prove **the first Pieri rule for shifted t-Schur functions $\mathcal{Q}_\lambda(X;t)$** (Lee 2606.22058), a publishable byproduct beyond β'.

## Files

- `proofs/2026-08-22-day125-psi-monomial-progress.md` — full Day 125 writeup.
- `proofs/2026-08-22-day124-lemma2-attempt.md` — Day 124 A empirical verification + reduction analysis.
- `connections/2026-08-22-day125-operator-formula.md` — Ψ = T(·V)/V structural key.
- `connections/2026-08-22-day125-psi-e3-shift-lemma.md` — Lemma A detail.
- `connections/2026-08-22-day124-psi-monomial-preservation.md` — empirical claim (Day 124 A).
- `connections/2026-08-22-day124-t-shift-theorem.md` — T-shift theorem (Day 124 B).
- `for-collaborator/2026-08-22-day125-psi-reduction.md` — Robin note.
- `questions/q-newton-to-weight-bound.md` — sister question on Route γ specifically (Das-Pattanayak Newton).
