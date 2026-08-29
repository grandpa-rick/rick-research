"""Test Central Lemma:
  s*_{(j+1, 0)}(y_2, y_3) - B_j = (b+c)^{↓(j+1)} - j*pi*(b+c-2)^{↓(j-1)}
where sigma = b+c+1, pi = (b+1)*c.

This is a compact reformulation. If true, combined with A_0 = (b+c)^{↓j},
proves Lemma 1.
"""

from collections import defaultdict
from itertools import combinations
from math import comb

import sympy as sp
from sympy import symbols, factor, expand, Poly, Integer, Rational

b, c = symbols('b c')
y2, y3 = b + 1, c


def fall(x, m):
    p = Integer(1)
    for i in range(m):
        p *= (x - i)
    return p


def s_star_two_var(a_p, b_p):
    if a_p < b_p:
        return Integer(0)
    num = fall(y2, a_p + 1) * fall(y3, b_p) - fall(y3, a_p + 1) * fall(y2, b_p)
    denom = y2 - y3
    q, r = sp.div(Poly(num, [b, c]), Poly(denom, [b, c]))
    assert r.as_expr() == 0
    return q.as_expr()


def kappa_new(j, m2, m3):
    return Rational((m3 - 1) * (m2 - m3), m2) * comb(j, m3) + comb(j, m2 + 1)


def compute_B(jj):
    result = Integer(0)
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
    print("Central Lemma test: s*_{(j+1,0)} - B_j = (b+c)^{↓(j+1)} - j*pi*(b+c-2)^{↓(j-1)}")
    print("=" * 72)

    pi_expr = (b + 1) * c

    all_ok = True
    for jj in range(2, 13):
        B = compute_B(jj)
        s_star = s_star_two_var(jj + 1, 0)
        LHS = expand(s_star - B)

        bc_fall_j1 = fall(b + c, jj + 1)
        bc_fall_jm1 = fall(b + c - 2, jj - 1)
        RHS = expand(bc_fall_j1 - jj * pi_expr * bc_fall_jm1)

        diff = expand(LHS - RHS)
        status = "OK" if diff == 0 else f"FAIL diff = {sp.factor(diff)}"
        print(f"  j = {jj}: {status}")
        if diff != 0:
            all_ok = False

    print()
    print(f"Central Lemma: {'PASS' if all_ok else 'FAIL'} for j = 2..12")


if __name__ == "__main__":
    main()
