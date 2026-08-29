"""Day 127 — Antisymmetric Top-τ Symbol Matching.

Test: for antisymmetric orbit sums a_α (α_1 > α_2 > α_3 distinct),
does τ-deg(T(a_α)) = τ-deg(a_α)?

Compute S(a_α) and S(T(a_α)) fully reduced mod y²-sy+τ,
compare top-τ symbols.
"""
from sympy import symbols, expand, Poly, S, factor, simplify, sympify
from itertools import permutations

s, y, t = symbols('s y t')

def reduce_y(P):
    """Reduce P mod y²-sy+τ where t = τ. Return polynomial with y-degree ≤ 1."""
    P = expand(P)
    poly = Poly(P, y, s, t)
    result = S.Zero
    for monom, coef in poly.as_dict().items():
        yk, sm, tn = monom
        # reduce y^yk
        if yk == 0:
            f, g = 1, 0
        elif yk == 1:
            f, g = 0, 1
        else:
            f, g = 1, 0
            fk, gk = 0, 1
            for _ in range(yk - 1):
                fk_new = -t * gk
                gk_new = f + s * gk
                f, g = fk, gk
                fk, gk = fk_new, gk_new
            f, g = fk, gk
        result += coef * (s**sm) * (t**tn) * (f + g*y)
    return expand(result)

def falling(x, n):
    p = S.One
    for i in range(n):
        p *= (x - i)
    return expand(p)

def apply_S(P_u):
    """Apply substitution u_1→τ, u_2→y, u_3→s-y."""
    u1, u2, u3 = symbols('u1 u2 u3')
    return P_u.subs({u1: t, u2: y, u3: s - y})

def apply_T_then_S(P_u):
    """Apply T (monomial-by-monomial, u^β → ∏ [u_i]_{β_i}), then S."""
    u1, u2, u3 = symbols('u1 u2 u3')
    P_u = expand(P_u)
    poly = Poly(P_u, u1, u2, u3)
    result = S.Zero
    for monom, coef in poly.as_dict().items():
        a, b, c = monom
        # T(u^β) = [u_1]_a [u_2]_b [u_3]_c
        Tm = falling(t, a) * falling(y, b) * falling(s - y, c)
        result += coef * Tm
    return expand(result)

def antisym_orbit(alpha):
    """Return the antisymmetric orbit sum Σ_σ sgn(σ) u^{σ(α)}."""
    u1, u2, u3 = symbols('u1 u2 u3')
    us = (u1, u2, u3)
    result = S.Zero
    for perm in permutations(range(3)):
        # sign
        sign = 1
        for i in range(3):
            for j in range(i+1, 3):
                if perm[i] > perm[j]:
                    sign *= -1
        term = 1
        for i, p in enumerate(perm):
            term *= us[i]**alpha[p]
        result += sign * term
    return expand(result)

def tau_deg(P):
    """τ-degree of P (reduced form)."""
    P = expand(P)
    if P == 0:
        return -1
    return Poly(P, t).degree()

def top_tau(P):
    """Return coefficient of highest τ-power in reduced P."""
    d = tau_deg(P)
    if d < 0:
        return S.Zero
    return Poly(P, t).coeff_monomial(t**d)

print("Testing antisymmetric orbit sums a_α, α_1 > α_2 > α_3 distinct.")
print("Comparing τ-deg and top-τ symbols of a_α vs T(a_α).\n")
print(f"{'α':>15} | {'τ-deg(g)':>8} | {'τ-deg(T(g))':>11} | {'top-τ match':>11} | {'diff τ-deg':>10}")
print("-" * 80)

fails = 0
tests = 0
for A in range(6):
    for B in range(A):
        for C in range(B):
            alpha = (A, B, C)
            g_u = antisym_orbit(alpha)
            Sg = reduce_y(apply_S(g_u))
            STg = reduce_y(apply_T_then_S(g_u))
            d_g = tau_deg(Sg)
            d_Tg = tau_deg(STg)
            diff = reduce_y(STg - Sg)
            d_diff = tau_deg(diff)
            tt_g = top_tau(Sg)
            tt_Tg = top_tau(STg)
            match = (tt_g == tt_Tg) and (d_g == d_Tg)
            symbol = "YES" if match else "NO"
            print(f"{str(alpha):>15} | {d_g:>8} | {d_Tg:>11} | {symbol:>11} | {d_diff:>10}")
            tests += 1
            if not match:
                fails += 1
                print(f"    top-τ(g)  = {tt_g}")
                print(f"    top-τ(Tg) = {tt_Tg}")
                print(f"    diff      = {factor(diff)}")

print(f"\nTotal: {tests} tests, {fails} failures.")
