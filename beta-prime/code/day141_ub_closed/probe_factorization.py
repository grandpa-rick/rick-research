"""Probe: does F_140(T) factor as G(T,E3) with SOME nice form?

Options to test:
  (a) F_140 = H(T) · N(T, E3) where N is a specific function.
  (b) log(F_140/H) is polynomial in E3 of some low degree (Day 140-like).
  (c) F_140 = H(T) · Ξ(E3 T, T, E1, E2) — some product with a specific shape.
  (d) Perhaps F is a triangular product involving log(1-E1 T) but with E3-dependent exponent.

Start by computing log F_140 to E3-degree 2 or 3.
"""

import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day140_interior')
from verify_gf_form import build_P, phi_k, p_b_fn, E1, E2, E3

from sympy import symbols, expand, Poly, Integer, factorial, Rational, factor, log, series, Symbol, cancel

T = symbols('T')

def truncate_T(expr, order):
    p = Poly(expr, T)
    out = Integer(0)
    for deg, coef in p.as_dict().items():
        if deg[0] <= order:
            out += coef * T**deg[0]
    return out

def main():
    B_MAX = 6
    P = build_P(B_MAX)

    # Build F_140(T) as truncated series in T with coeffs in E1,E2,E3
    F = Integer(0)
    for b in range(B_MAX+1):
        F += P[b] * T**b / factorial(b)
    F = expand(F)

    ORDER = B_MAX

    # log F = log(1 + (F-1)) truncated
    Fm1 = expand(F - 1)
    logF = Integer(0)
    current = Integer(1)
    for k in range(1, ORDER+1):
        current = truncate_T(expand(current * Fm1), ORDER)
        logF += (-1)**(k-1) * current / k
    logF = expand(logF)

    # Look at coefficients of T^n in log F
    print("log F_140(T), coef of T^n as polynomial in E3:")
    for n in range(ORDER+1):
        c = Poly(logF, T).as_dict().get((n,), Integer(0))
        c = expand(c)
        print(f"\n  T^{n}:")
        # Split by E3 degree
        cP = Poly(c, E3) if c != 0 else None
        if cP is None:
            print("    0")
            continue
        for d in range(cP.degree()+1):
            ck = cP.coeff_monomial(E3**d)
            if ck != 0:
                print(f"    [E3^{d}]  {factor(expand(ck))}")


if __name__ == '__main__':
    main()
