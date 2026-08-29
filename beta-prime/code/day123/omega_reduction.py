"""Day 123: Reduce E_j mod Omega = e_3(e_1+1)^2 - (e_2+e_3)^2.

Under specialization Sigma: e_1 -> t+j, e_2 -> t(j+1), e_3 -> t^2:
  Omega maps to 0 (it's the syzygy).

So ker Sigma = (Omega). We can reduce E_j modulo Omega:
  E_j = f_j(e_1, e_2) + g_j(e_1, e_2) * e_3 + (Omega multiple)
Under Sigma: E_j|_spec = f_j(t+j, t(j+1)) + g_j(t+j, t(j+1)) * t^2.
  deg_t <= max(deg f_j, deg g_j + 2)
  where deg here means total degree in (e_1, e_2), which corresponds to deg_t.

Goal: verify deg f_j <= j and deg g_j <= j - 2.

Reduction rule: e_3^2 = (e_1^2 + 2 e_1 - 2 e_2 + 1) e_3 - e_2^2  (mod Omega)
"""

import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day123')

import sympy as sp
from sympy import symbols, expand, Poly, Integer

from e_basis_check import check_conjecture

e1, e2, e3 = symbols('e1 e2 e3')


def reduce_mod_omega(f):
    """Reduce polynomial in e1, e2, e3 modulo Omega = e_3(e_1+1)^2 - (e_2+e_3)^2.
    Rewrite e_3^2 -> (e_1^2 + 2 e_1 - 2 e_2 + 1) e_3 - e_2^2 iteratively.
    Returns (f0, f1) where f = f0 + f1 * e_3 (mod Omega).
    """
    P = e1**2 + 2*e1 - 2*e2 + 1
    Q = e2**2
    f = expand(f)
    # iteratively replace e_3^k for k >= 2 by lower powers
    while True:
        p = Poly(f, e3)
        deg = p.degree()
        if deg <= 1:
            break
        # highest power in e_3: replace one factor of e_3^2 with P e_3 - Q
        # Only replace top term
        top_coef = p.nth(deg)
        # subtract top_coef * e_3^deg, add top_coef * e_3^(deg - 2) * (P * e_3 - Q)
        f = expand(f - top_coef * e3**deg + top_coef * e3**(deg - 2) * (P * e3 - Q))
    # Now f is linear in e_3: f = f0 + f1 * e_3
    p = Poly(f, e3)
    f0 = expand(p.nth(0))
    f1 = expand(p.nth(1)) if p.degree() >= 1 else Integer(0)
    return f0, f1


def total_deg_e12(f):
    """Total degree of polynomial f(e_1, e_2)."""
    if f == 0:
        return -1
    p = Poly(f, e1, e2)
    max_d = -1
    for (a, b), _ in p.terms():
        max_d = max(max_d, a + b)
    return max_d


def main():
    print('Reduce E_j mod Omega and check degree bounds:')
    print('=' * 70)

    all_ok = True
    for j_val in range(1, 9):
        _, _, E_e = check_conjecture(j_val)
        f0, f1 = reduce_mod_omega(E_e)
        d0 = total_deg_e12(f0)
        d1 = total_deg_e12(f1)
        ok = (d0 <= j_val) and (d1 <= j_val - 2)
        if not ok:
            all_ok = False
        print(f'j = {j_val}:')
        print(f'  f_j deg = {d0} (target <= {j_val})')
        print(f'  g_j deg = {d1} (target <= {j_val - 2})')
        print(f'  Verdict: {"OK" if ok else "FAIL"}')

        # Verify reduction is correct: substitute
        Omega = e3 * (e1 + 1)**2 - (e2 + e3)**2
        recon = expand(f0 + f1 * e3)
        diff = expand(E_e - recon)
        # Should be divisible by Omega
        q, r = sp.div(sp.Poly(diff, e3), sp.Poly(Omega, e3))
        if expand(r.as_expr()) != 0:
            print(f'  *** REDUCTION ERROR: remainder = {expand(r.as_expr())}')
            all_ok = False

    print()
    print(f'ALL cases OK: {all_ok}')


if __name__ == '__main__':
    main()
