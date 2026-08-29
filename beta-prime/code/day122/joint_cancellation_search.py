"""Experiment 4: Structural search for the joint-cancellation mechanism.

For each j, compute the full S_j(s, t) polynomial. Look for structure:
  - deg_t S_j <= j (individual F_mu have deg_t up to d_mu >= j+1;
    the sum SHOULD have deg_t <= j).
  - This is the KEY compression: the sum "loses degree" from ~d_max to j.

Also probe:
  - Does S_j(s, t) factor nicely? Roots in s? Roots in t?
  - Does S_j(s, t) evaluated at "special" values reveal structure?
  - What is the leading-t part [t^j] S_j(s) explicitly?
"""

import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day119')
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day122')

import sympy as sp
from sympy import symbols, expand, Integer, Poly, factor, gcd, roots

from aggregate_td import (build_AB_in_s, F_mu, N_mu, W_ab, fall_t,
                          compute_Sj, get_t_coefficient, d_max, s, t)
from kostka import kostka_mu_prime_2j, d_mu, all_mu_3parts


def analyze_Sj(jval, A, B):
    print("=" * 70)
    print(f"j = {jval}, d_max = {d_max(jval)}")
    print("=" * 70)
    S, contribs = compute_Sj(jval, A, B)

    max_dt = Poly(S, t).degree()
    print(f"  deg_t S_j = {max_dt} (KEY: this IS the vanishing statement)")
    print()

    print("  [t^d] S_j(s) for d = 0, ..., deg_t:")
    for d in range(max_dt + 1):
        coef = get_t_coefficient(S, d)
        fac = factor(coef) if coef != 0 else 0
        print(f"    [t^{d}] = {fac}")

    # Show total factorization?
    print()
    try:
        S_fac = factor(S)
        # Only if reasonably compact
        s_str = str(S_fac)
        if len(s_str) < 400:
            print(f"  factor(S_j) = {S_fac}")
        else:
            print(f"  factor(S_j) — too long to display ({len(s_str)} chars)")
    except Exception as e:
        print(f"  factor failed: {e}")

    # Look for structural roots
    print()
    print("  S_j(s=integer, t) for s=0, 1, ..., j+1:")
    for s_val in range(0, jval + 2):
        S_at_s = expand(S.subs(s, s_val))
        p = Poly(S_at_s, t) if S_at_s != 0 else None
        if p is None:
            print(f"    s={s_val}: S_j = 0 identically")
        else:
            print(f"    s={s_val}: S_j(s,t) = {S_at_s}")

    print()


def main():
    A, B = build_AB_in_s(20)
    for jval in [3, 4, 5, 6, 7]:
        analyze_Sj(jval, A, B)


if __name__ == "__main__":
    main()
