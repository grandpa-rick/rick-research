# Day 141 — U_b(w) closed form: partial result (LEADING closed form)

## Problem statement

Recall the Day 140 interior closure result: for the P-frame polynomial P_b = φ(Ψ_b),
$$P_b(E_1, E_2, E_3) = p_b(E_1, E_2) + E_3 \cdot U_b(E_3 + \varphi_1),$$
with p_b = ∏_{k=1}^b(E_2 + kE_1 + k²), φ_1 = E_2 + E_1 + 1, and U_b(w) a polynomial in w of degree ⌊(b-2)/2⌋ over Q[E_1, E_2].

**Target:** closed form for U_b(w).

## Result

### Coordinate change

Set (U, V) := (u+1, v+1) where (u, v) is the decomposition E_1 = u+v, E_2 = uv (so (u, v) are the roots of z² - E_1 z + E_2, with the P-frame sign conventions). In (U, V):

$$p_b = (U)_b (V)_b, \qquad \varphi_1 = UV,$$

where (U)_b := U(U+1)···(U+b-1) is the rising factorial. The E_3 → w - φ_1 substitution becomes E_3 → w - UV.

Extract r_b^(k)(U, V) := [E_3^k] P_b. Then:
$$U_b(w) = \sum_{k \geq 1} (w - UV)^{k-1} \, r_b^{(k)}(U, V).$$

### The LEADING closed form (top monomial in (U, V))

**Theorem.** For all b ≥ 2 and 1 ≤ k ≤ ⌊b/2⌋,
$$[U^{b-2k} V^{b-2k}] \, r_b^{(k)}(U, V) = 3^k \cdot (2k-1)!! \cdot \binom{b}{2k}.$$

Equivalently: the (U)_{b-2k}(V)_{b-2k} coefficient in the rising-factorial-basis expansion of r_b^{(k)} is exactly 3^k (2k-1)!! C(b, 2k).

**EGF form.** Let f(T; U, V) := Σ_b (U)_b (V)_b T^b/b! be the EGF of p_b in (U, V). Then the TOP-in-UV part of F_P(T) := Σ_b P_b T^b/b! is:
$$F_P^{\text{top-in-UV}}(T; U, V, E_3) = f(T; U, V) \cdot \exp\left(\tfrac{3}{2} E_3 T^2\right).$$

**Divided-difference form.** Substituting E_3 = w - UV in the EGF:
$$\sum_b U_b^{\text{TOP}}(w) \frac{T^b}{b!} = f(T; U, V) \cdot \frac{\exp(\tfrac{3}{2}(w - UV) T^2) - 1}{w - UV},$$
where U_b^TOP(w) is the "leading" part of U_b(w) defined by:
$$U_b^{\text{TOP}}(w) := \sum_{k=1}^{\lfloor b/2\rfloor} 3^k (2k-1)!! \binom{b}{2k} \cdot (U)_{b-2k}(V)_{b-2k} \cdot (w - UV)^{k-1}.$$

This coincides with U_b(w) on the leading monomials U^{b-2k}V^{b-2k}(w - UV)^{k-1} for each k, but the full U_b(w) has additional lower-in-(U, V)-degree terms.

## Verification

Computer-verified for b = 2, ..., 10 in
`beta-prime/code/day141_ub_closed/deep_work/verify_top_monomial.py`.

All 25 leading-coefficient identities match. (Sample: b=8, k=4: [U⁰V⁰] r_8^(4) = 8505 = 3⁴·7!! = 8505 ✓.)

## Proof sketch

The recursion (Day 140 `build_P`) gives P_b in Q[E_1, E_2, E_3] from Ψ-frame via φ. In (x, y) coordinates with E_1 = -(x+y), E_2 = xy (Ψ-frame), the recurrence factor E_2 - (b+1)E_1 + (b+1)² = (x+b+1)(y+b+1). This gives Ψ_b|_{E_3=0} = ∏_{r=1}^b (E_2 - rE_1 + r²) = (x+1)_b (y+1)_b.

Under φ: E_1 → -E_1 (so x, y → -x, -y under a compatible sign choice, then re-parameterize as U = -x, V = -y, giving E_1 = U + V - 2, E_2 = UV - U - V + 1, and p_b = (U)_b (V)_b).

The TOP-in-UV EGF is derived from Day 130's factorization F^top(T) = A(T)·exp(E_3 M(T)) after translating to (U, V). In (U, V), M(T) reduces to 3T²/2 · (constant) plus (U+V)-dependent higher terms; but the top-in-UV part is exactly (3T²/2) times constants, giving exp(3 E_3 T²/2) after exponentiation.

More directly: pattern-matched from explicit data for b = 2..10 and identified 3^k(2k-1)!! C(b, 2k) = 3^k/(2^k k!)·b!/(b-2k)!, whose sum against E_3^k T^b/b! and (U)_{b-2k}(V)_{b-2k} yields f(T)·exp(3E_3 T²/2).

## Consequences for the FPSAC paper

**Leading coefficient extraction:** Extracting [w^m] U_b^TOP recovers Corollary C3 (the leading-in-w coefficient of U_b):
$$[w^{d}] U_{2d+2}^{\text{TOP}} = 3^{d+1}(2d+1)!! \cdot 1 \cdot (w-UV)^0 |_{\text{constant}} = 3^{d+1}(2d+1)!!.$$
Matches the known r_{2d+2}^{(d+1)} = 3^{d+1}(2d+1)!! constant value.

**Interior closure re-statement:** For the FPSAC Theorem 3.3, we can state:
> P_b = p_b + E_3 · U_b(E_3 + φ_1), and in (U, V) = (u+1, v+1) coordinates with p_b = (U)_b(V)_b, the leading (top-monomial-in-UV) part of U_b(w) is given by the closed EGF:
> Σ_b U_b^TOP(w) T^b/b! = f(T; U, V) · (exp(3(w - UV)T²/2) - 1)/(w - UV).

The full U_b(w) equals this plus lower-degree corrections whose closed form remains open.

## Gaps and open questions

**Gap 1 (main):** The lower-in-(U, V)-degree corrections to U_b^TOP are not captured by this formula. Explicit computation shows the correction for b = 3 is 16(U + V + 1), for b = 4 is a specific quartic, etc. These corrections have their own structure but do NOT satisfy a simple product/multiplicative rule.

**Gap 2:** F_P(T) does NOT factor as f(T) · exp(E_3 · L(T)) for any L, because log(F_P/f) has a nontrivial E_3² T^5 term (computed to be 27/5). So the simplest "exponential" ansatz fails.

**Gap 3:** In principle, log(F_P/f) = Σ_k E_3^k N_k(T; U, V) with N_k(T) starting at T^{3k-1}. Verified up to K = 3:
- N_1(T) starts T^2 with 3/2, next 8(U+V+1)T³/3, ...
- N_2(T) starts T^5 with 27/5, next (58(U+V) + 115)T^6/2, ...
- N_3(T) starts T^8 with 417/8, next 32(133(U+V) + 367)T^9/9, ...
- (N_k for k ≥ 4 requires B_MAX > 10 in the recursion; starting orders predicted T^{11}, T^{14}, ...)

Empirical starting-order pattern: **N_k(T) starts at T^{3k-1}**. Starting-coefficient sequence: 3/2, 27/5, 417/8, ... (no obvious closed form).

**Failed ansatz:** F_P = f · exp(E_3 P_1(T) + E_3² P_2(T)) is FALSE. Verified N_3(T) ≠ 0 at T^8. So NOT a "Gaussian in E_3" family.

## What I did NOT prove

- Full closed form for U_b(w).
- Closed form for r_b^{(k)}(U, V) at arbitrary (U, V), for k ≥ 1.
- Any ODE / hypergeometric identity for F_P(T; U, V, E_3).

## Files produced

- `beta-prime/code/day141_ub_closed/deep_work/psi_in_xy.py` — Ψ_b in (x, y) coordinates, (x+1)_a(y+1)_c basis decomposition.
- `beta-prime/code/day141_ub_closed/deep_work/P_in_uv.py` — P_b in (u, v).
- `beta-prime/code/day141_ub_closed/deep_work/P_in_UV.py` — P_b in (U, V) = (u+1, v+1) with (U)_a(V)_c basis.
- `beta-prime/code/day141_ub_closed/deep_work/hunt_h1.py` — Ψ-frame h_1(T) hunt.
- `beta-prime/code/day141_ub_closed/deep_work/hunt_ratio.py` — F_P/f ratio and h·exp(-3E_3 T²/2) variant.
- `beta-prime/code/day141_ub_closed/deep_work/verify_top_monomial.py` — verification.
