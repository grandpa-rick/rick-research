"""Day 191 sober recheck of e_2 * e_2 formula.

Independent check via numerical specialization at (q, t) = (5, 3), (2, 7), (7, -1):
compute e_2(Y) . e_2(X) at m=4 with q,t substituted upfront (much faster);
compare to formula evaluated at same point.
"""

import sympy as sp
from itertools import combinations
from fractions import Fraction

def qint(n, t):
    return sum(t**i for i in range(n)) if n > 0 else 0


def build_action_numeric(m, q_val, t_val):
    """Same as build_action but with q, t as numeric Fractions to avoid symbolic blowup."""
    q, t = q_val, t_val
    X = sp.symbols(f'X1:{m+1}')

    def si_apply(F, i):
        subs = {X[i-1]: X[i], X[i]: X[i-1]}
        return sp.expand(F.xreplace(subs))

    def Ti_apply(F, i):
        F = sp.expand(F)
        sF = si_apply(F, i)
        diff = sp.expand(F - sF)
        quot = sp.cancel(diff / (X[i-1] - X[i]))
        return sp.expand(t * sF + (t - 1) * (-X[i]) * quot)

    def Ti_inv_apply(F, i):
        Ti_F = Ti_apply(F, i)
        return sp.expand(Ti_F / t - Fraction(t - 1, t) * F)

    def Pi_apply(F):
        subs = {X[i]: X[i+1] for i in range(m-1)}
        subs[X[m-1]] = Fraction(1, q) * X[0]
        Fshift = sp.expand(F.xreplace(subs))
        return sp.expand(X[0] * Fshift)

    def Y_apply(F, i):
        G = F
        for j in range(i, m):
            G = Ti_inv_apply(G, j)
        G = Pi_apply(G)
        for j in range(1, i):
            G = Ti_apply(G, j)
        return sp.expand(t**(m - i) * G)

    return X, Y_apply


def e_r_X(m, r):
    X = sp.symbols(f'X1:{m+1}')
    if r == 0:
        return sp.Integer(1)
    if r > m:
        return sp.Integer(0)
    result = sp.Integer(0)
    for combo in combinations(X, r):
        term = sp.Integer(1)
        for v in combo:
            term *= v
        result += term
    return sp.expand(result)


def compute_e2_star_e2_numeric(m, q_val, t_val):
    X, Y_apply = build_action_numeric(m, q_val, t_val)
    e2X = e_r_X(m, 2)
    Yj_e2 = {j: Y_apply(e2X, j) for j in range(1, m+1)}
    total = sp.Integer(0)
    for i in range(1, m+1):
        for j in range(i+1, m+1):
            total = sp.expand(total + Y_apply(Yj_e2[j], i))
    return sp.expand(total / t_val)


def formula_e2_star_e2(q_val, t_val):
    """Formula from Day 191: coefficients of e_lambda in e_2 * e_2."""
    q, t = q_val, t_val
    return {
        (4,): Fraction(q-1, q**2) * (t**2 + 1) * (q*t**2 + q*t + q - t),
        (3, 1): Fraction(q-1, q**2) * (t + 1),
        (2, 2): Fraction(1, q**2),
    }


def formula_e2_star_e2_symbolic():
    q, t = sp.symbols('q t')
    return {
        (4,): (q-1)/q**2 * (t**2 + 1) * (q*t**2 + q*t + q - t),
        (3, 1): (q-1)/q**2 * (t + 1),
        (2, 2): 1/q**2,
    }


def polynomial_from_e_basis(m, coeffs):
    """Given {lam: coeff}, return polynomial sum_lam coeff * e_lam(X_1..X_m)."""
    result = sp.Integer(0)
    for lam, c in coeffs.items():
        el = sp.Integer(1)
        for p in lam:
            el *= e_r_X(m, p)
        result += c * el
    return sp.expand(result)


def main():
    print("=" * 70)
    print("Day 191 sober re-check: e_2 * e_2 at numeric (q, t)")
    print("=" * 70)

    for q_val, t_val in [(Fraction(5, 1), Fraction(3, 1)),
                          (Fraction(2, 1), Fraction(7, 1)),
                          (Fraction(7, 1), Fraction(-1, 1))]:
        print(f"\n--- (q, t) = ({q_val}, {t_val}) ---")
        m = 4
        # Compute LHS numerically
        lhs_poly = compute_e2_star_e2_numeric(m, q_val, t_val)
        # Compute RHS from formula
        formula_coeffs = formula_e2_star_e2(q_val, t_val)
        rhs_poly = polynomial_from_e_basis(m, formula_coeffs)
        # Compare
        diff = sp.expand(lhs_poly - rhs_poly)
        print(f"  LHS (direct): degree = {sp.Poly(lhs_poly, *sp.symbols(f'X1:{m+1}')).total_degree()}")
        print(f"  RHS (formula): degree = {sp.Poly(rhs_poly, *sp.symbols(f'X1:{m+1}')).total_degree()}")
        print(f"  Difference: {diff}  (should be 0)")


if __name__ == "__main__":
    main()
