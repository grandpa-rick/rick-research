"""Test key divisibility: (b+c-2)^{↓(j-2)} | [s*_{(j+1,0)}(y_2, y_3) - B].

If yes, this reduces Lemma 1 to a simple identity:
  A_1 / (b+c-2)^{↓(j-2)} = alpha*(b+c)(b+c-1) - [s*_{(j+1,0)} - B]/(b+c-2)^{↓(j-2)} = P_j

Where B is now computed via my derived ballot formula for kappa.
"""

import time
from collections import defaultdict
from itertools import combinations
from math import comb

import sympy as sp
from sympy import symbols, factor, expand, Poly, Integer, Rational, simplify

a, b, c = symbols('a b c')
y2, y3 = b + 1, c


def fall(x, m):
    p = Integer(1)
    for i in range(m):
        p *= (x - i)
    return p


def s_star_two_var(a_p, b_p):
    """s*_{(a_p, b_p)}(y2, y3) for a_p >= b_p >= 0."""
    if a_p < b_p:
        return Integer(0)
    num = fall(y2, a_p + 1) * fall(y3, b_p) - fall(y3, a_p + 1) * fall(y2, b_p)
    denom = y2 - y3
    q, r = sp.div(Poly(num, [b, c]), Poly(denom, [b, c]))
    assert r.as_expr() == 0
    return q.as_expr()


def kappa_new(j, m2, m3):
    """kappa for mu = (j-1, m2, m3), via my derived formula."""
    # (m3-1)*(m2-m3)/m2 * C(j, m3) + C(j, m2+1)
    return Rational((m3 - 1) * (m2 - m3), m2) * comb(j, m3) + comb(j, m2 + 1)


def compute_B_via_formula(jj):
    """B from my derived formula."""
    result = Integer(0)
    # m2 + m3 = j+1, m2 <= j-1, m2 >= m3 >= 2.
    for m3 in range(2, (jj + 1) // 2 + 1):
        m2 = jj + 1 - m3
        if m2 > jj - 1:
            continue
        if m2 < m3:
            continue
        k = kappa_new(jj, m2, m3)
        result += k * s_star_two_var(m2, m3)
    return expand(result)


def main():
    print("Testing:  (b+c-2)^{↓(j-2)}  divides  [B - s*_{(j+1,0)}(y2, y3)]  ?")
    print("Also computing the quotient and comparing to expected form.")
    print("=" * 72)

    m = b + c
    j_max = 10

    for jj in range(2, j_max + 1):
        B_formula = compute_B_via_formula(jj)
        U = s_star_two_var(jj + 1, 0)
        diff = expand(B_formula - U)

        # Divide by (b+c-2)^{↓(j-2)}
        if jj == 2:
            # (b+c-2)^{↓0} = 1
            div = Integer(1)
        else:
            div = Integer(1)
            for i in range(jj - 2):
                div *= (m - 2 - i)

        # Compute quotient using polynomial division (in b, c)
        try:
            q_poly = Poly(expand(diff), b, c)
            div_poly = Poly(expand(div), b, c)
            qq, rr = sp.div(q_poly, div_poly)
            if rr.as_expr() == 0:
                quot = qq.as_expr()
                status = "OK"
            else:
                quot = None
                status = f"NON-ZERO REMAINDER"
        except Exception as e:
            quot = None
            status = f"error: {e}"

        print(f"\n  j = {jj}: divisibility: {status}")
        if quot is not None:
            # Now compute the expected: alpha*(b+c)(b+c-1) - quot = P_j
            alpha = m - comb(jj, 2)
            # A_1 = alpha*A_0 - s*_{(j+1,0)} + B, so
            # A_1/div = alpha*(b+c)(b+c-1) + (B - s*_{(j+1,0)})/div = alpha*(b+c)(b+c-1) + quot
            pred = expand(alpha * m * (m - 1) + quot)
            # Compare to P_j formula
            Pj_expected = jj * (
                2*b**2*c - b**2*jj + 3*b**2
                + 2*b*c**2 - 4*b*c*jj + 8*b*c + b*jj - 3*b
                - c**2*jj + 5*c**2 - c*jj - 3*c
            )
            Pj_expected = expand(Rational(1, 2) * Pj_expected)
            diff2 = expand(pred - Pj_expected)
            match = "MATCH" if diff2 == 0 else f"MISMATCH: diff = {sp.factor(diff2)}"
            print(f"    P_j (my formula) matches expected? {match}")
            print(f"    quot = [B - s*_{{(j+1,0)}}] / (b+c-2)^{{↓(j-2)}} = {sp.factor(quot)}")


if __name__ == "__main__":
    main()
