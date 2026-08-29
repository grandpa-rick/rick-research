"""Experiment 5b: q-lift of the FULL [t^d] S_j(s) = 0 vanishing.

Define S_j(s, t; q) := sum_mu K_{mu', (2^j)}(q) * s*_mu specialized(s, t).
Then classically at q=1: [t^d] S_j(s; 1) = 0 for d > j.

Question: does [t^d] S_j(s; q) = 0 for d > j as a polynomial in s, q?
"""

import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day119')
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day122')

from sympy import symbols, expand, Integer, Poly, factor

from aggregate_td import (build_AB_in_s, F_mu, get_t_coefficient, d_max, s, t)
from q_lift_check import kostka_foulkes_mu_prime_2j, q
from kostka import d_mu, all_mu_3parts


def compute_Sj_qlift(jval, A, B):
    """Compute S_j(s, t; q) = sum_mu K_{mu', (2^j)}(q) * F_mu(s, t)."""
    twoj = 2 * jval
    contribs = []
    S = Integer(0)
    for mu in all_mu_3parts(twoj):
        Kq = kostka_foulkes_mu_prime_2j(mu, jval)
        if Kq == 0:
            continue
        F = F_mu(mu, A, B)  # in s, t
        contribution = expand(Kq * F)
        S = expand(S + contribution)
        contribs.append((mu, Kq, F))
    return S, contribs


def get_t_coefficient_qlift(expr, d):
    """[t^d] expr as poly in s and q."""
    p = Poly(expr, t, s, q)
    out = Integer(0)
    for (dt, ds, dq), coef in p.terms():
        if dt == d:
            out += coef * s**ds * q**dq
    return expand(out)


def main():
    A, B = build_AB_in_s(20)

    for jval in [3, 4, 5]:
        print("=" * 70)
        print(f"j = {jval}, d_max = {d_max(jval)}")
        print("=" * 70)
        S, contribs = compute_Sj_qlift(jval, A, B)
        # deg_t
        max_dt = Poly(S, t).degree()
        print(f"  deg_t S_j(s, t; q) = {max_dt}")
        for d in range(jval + 1, max(max_dt, d_max(jval)) + 1):
            coef = get_t_coefficient_qlift(S, d)
            status = "ZERO" if coef == 0 else "NONZERO"
            if coef != 0:
                # Show q-degree pattern
                pcoef = Poly(coef, q)
                print(f"  [t^{d}] S_j(s, q): deg_q = {pcoef.degree()}, "
                      f"leading in q = {pcoef.LC()}, "
                      f"constant in q = {expand(coef.subs(q, 0))}")
                # Compact print of whole coef
                s_str = str(coef)
                if len(s_str) < 200:
                    print(f"    = {coef}")
                else:
                    print(f"    (poly with {len(s_str)} chars)")
            else:
                print(f"  [t^{d}] S_j(s, q) = 0 (ZERO)")
        print()


if __name__ == "__main__":
    main()
