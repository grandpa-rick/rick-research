---
name: Route α — τ-degree preservation under Day 118 substitution (STATUS: partial, per-Schur PROVED for ℓ(μ) ≤ 3, Day 127)
description: Day 126 discovery. The (1,1,2)-weight equals τ-degree exactly under u_1 = τ, u_2 = y, u_3 = c (with y + c = s, yc = τ). Day 127: per-Schur equality d_{s*_μ} = d_{s_μ} PROVED for ℓ(μ) ≤ 3. Top-τ Symbol Matching Lemma FALSE as stated (counterexample). Pre-Day-127 empirical Route α results USED BUGGY reduce_y — suspect. Post-fix, per-Schur equality holds but Claim ★ (full weight preservation) requires cancellation propagation, still open.
type: project
---

# Route α — τ-degree preservation

## The setup

Rick's Day 118 substitution: u_1 = τ, u_2 = y, u_3 = c, where (y, c) are the two roots of z² − sz + τ = 0 (so y + c = s and yc = τ). Under this substitution:
- e_1 = u_1 + u_2 + u_3 = τ + s → τ-degree 1
- e_2 = u_1(u_2 + u_3) + u_2 u_3 = τs + τ = τ(s + 1) → τ-degree 1
- e_3 = u_1 u_2 u_3 = τ · τ = τ² → τ-degree 2

**KEY:** the (1,1,2)-weight equals the τ-degree exactly. For an e-monomial e_1^{a_1} e_2^{a_2} e_3^{a_3}:
$$\tau\text{-deg} = a_1 + a_2 + 2a_3 = w.$$

## Claim ★

For any symmetric polynomial P ∈ ℚ[u_1, u_2, u_3]:
$$\tau\text{-deg}\ \Psi(P)(\tau, y, c) = \tau\text{-deg}\ P(\tau, y, c) = w(P).$$

Equivalently, Ψ preserves the (1,1,2)-weight EXACTLY (not just ≤).

This is stronger than Rick's original goal `w(Ψ(e_2^b)) ≤ b`. If Claim ★ holds, everything closes at once.

## Empirical evidence (Route α agent, Day 126, ~200 tests)

**WARNING (Day 127): all these tests used the BUGGY reduce_y function.** The reduce_y bug: it used f_{k-1} where it should use f_k, so y(s-y) reduced to `t-y` instead of `t`. Re-verify with `~/projects/beta-prime/code/day127/lib.py` before citing these numbers.

Original claims (pre-bug-fix):
- 50/50 e-monomials of weight ≤ 6: weight = τ-deg
- 25/25 hand-picked symmetric polys
- 94/94 e-monomials of weight 1..8: Ψ preserves τ-deg
- 164/164 non-symmetric u-monomials: T preserves τ-deg
- Ψ(e_2^b) for b = 1..8: τ-deg = b EXACTLY
- 40/40 s-leading of top-τ preserved by Ψ

**Post-bug-fix status (Day 127):**
- Antisymmetric orbit sums: 20/20 pass (previously reported 0/2 exact match; per-Schur equality only visible with fix).
- Symmetric polynomials with cancellations: 0/30 failures.
- Combinatorial upper bound: verified for all 55 partitions with μ_1 ≤ 5.

Day 124's claim (Ψ preserves (1,1,2)-weight monomially, 147/147) needs re-verification with corrected library.

## Sharper Claim ♦Ψ (from Route α agent)

**Claim ♦.** For every e-monomial f = e_1^{a_1} e_2^{a_2} e_3^{a_3}:
$$\text{top-}\tau(S(f)) = (s+1)^{a_2}.$$
(s-degree = a_2, s-leading = 1, independent of a_1, a_3.)

**Claim ♦Ψ (verified 40/40).** Ψ preserves this top-τ s-leading coefficient exactly:
$$\text{top-}\tau(S(\Psi(f))) = (s+1)^{a_2} + (\text{terms of lower s-degree}).$$

## The residual technical gap — LEMMA FALSE, ROUTE VIA v_d/Q_{m,n} INSTEAD

**Top-τ Symbol Matching Lemma (Day 126, FALSE as stated).** Counterexample: [y]_1 · [s-y]_2 - y · (s-y)^2 = -τ, τ-degree 1 (not < 1). Discovered Day 127 after bug-fix in reduce_y.

**Correct route (Day 127, PROVED for ℓ(μ) ≤ 3):** the combinatorial upper bound (λ_1 ≤ μ_1, |λ| ≤ |μ|, monotonicity of f(x) = x + ⌊(|μ|-x)/2⌋) + computational lower bound via v_d and Q_{m,n} polynomials. See `connections/2026-08-22-day127-per-schur-tau-equality.md`.

**Full Claim ★ (Ψ preserves τ-degree for arbitrary symmetric f) is STRONGER than per-Schur equality** — it requires cancellations to propagate from ordinary-Schur to shifted-Schur basis. Empirically holds through b ≤ 4 (with corrected reduce_y). Rigorous proof open.

## Why this is the right route

**Advantages over Route γ (queer HC):**
- Route γ requires an INVERSE MAP that doesn't exist (e_2 ∉ Γ_N).
- Route α works directly with Ψ's defining operator formula.
- Route α is purely SYMMETRIC-POLYNOMIAL: no representation theory needed.

**Advantages over Route δ (BHS §7):**
- BHS descends by total polynomial degree (weaker).
- Route α uses the FINER (1,1,2)-weight via τ-substitution — the correct grading.

## Structural insights for the proof

**Insight 1:** V(τ, y, c) = τ(τ - s + 1)(2y - s). Antisymmetric factor (2y - s) has square (s² - 4τ) mod ideal.

**Insight 2:** T(P·V) mod ideal = A(s,τ) + B(s,τ) y with A = -Bs/2 (from antisymmetry). Then Ψ(P)(s,τ) = B(s,τ) / [4τ(τ - s + 1)].

**Insight 3:** Claim ★ ⟺ τ-deg B_P = w(P) + 2, where B_P is the y-coefficient of T(P·V) mod (y² - sy + τ).

**Insight 4 (KEY):** For β ≠ γ (distinct exponents, always the case in antisymmetric fV):
$$[y]_\beta \cdot [c]_\gamma = \prod_{i=0}^{\min(\beta,\gamma)-1} (\tau - is + i^2) \cdot (\text{poly in } y \text{ of degree } |\beta - \gamma|).$$
Paired factors (y-i)(c-i) = τ - is + i² lie in ℚ[s, τ] with τ-degree 1.

**Insight 5 (loose per-monomial bound):** The per-monomial τ-degree bound is α + ⌊(β+γ)/2⌋, which for fV = e_2^b · V gives τ-deg Ψ(f) ≤ 2b+1 (loose by b+1). So CANCELLATION IS ESSENTIAL — the antisymmetric-orbit structure must eliminate high-τ terms.

## Attack strategies

**Approach 1: antisymmetric-orbit cancellation.** Group monomials in fV by S_3 orbits, use pair-wise cancellation to eliminate leading-τ contributions.

**Approach 2: generating function.** Consider Σ_b Ψ(e_2^b) t^b / b!. Look for a master identity that manifests τ-degree preservation.

**Approach 3: leading-term matching.** For each monomial u_1^α u_2^β u_3^γ, both u_1^α u_2^β u_3^γ and [u_1]_α [u_2]_β [u_3]_γ have the same leading TOP monomial u_1^α u_2^β u_3^γ under expansion (Stirling drops are lower). Under substitution mod ideal, the leading-τ contribution should transfer exactly from RAW substitution to T-image, giving τ-degree preservation OF SYMMETRIC POLYNOMIALS via T. Then division by V preserves it too.

## Files

- `/home/agent/state/PROVE.md` — Day 127 seed, targeting Claim ★ or its restriction to e_2^b.
- `/home/agent/projects/beta-prime/notes/2026-08-20-day118-molev-verify-and-proof-attempt.md` — original substitution & d_μ formula.
- `/home/agent/projects/beta-prime/code/day126/route_alpha_tau_degree.py` — empirical test code.
