"""
Day 142 Attack B v2 — ODE ansatz, faster version.

Test L·F_P / F_P (as a series in T with coefs in E_3) at specific (U, V) values.
If the ratio has a nice closed form, we win.
"""

import sys, os, time
sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day140_interior')

from compute_P_fast import compute_P_at
from verify_gf_form import E3
from sympy import (symbols, expand, Integer, Rational, Poly, factorial,
                   rf, factor, diff)

T = symbols('T')

def theta(P):
    return expand(T * diff(P, T))

def apply_L(P, U_val, V_val):
    """L = T(U_val + θ)(V_val + θ) - θ."""
    P1 = expand(V_val*P + theta(P))
    P2 = expand(U_val*P1 + theta(P1))
    P3 = expand(T * P2)
    return expand(P3 - theta(P))

def truncate_T(P, N):
    Pp = Poly(expand(P), T)
    out = Integer(0)
    for d in range(N + 1):
        c = Pp.coeff_monomial(T**d)
        out += c * T**d
    return out

def build_FP(P_dict, B_max):
    F = Integer(0)
    for b in range(B_max + 1):
        F += P_dict[b] * T**b / factorial(b)
    return F

def one_over_series(f, N):
    fp = Poly(expand(f), T)
    a = {d: fp.coeff_monomial(T**d) for d in range(N + 1)}
    if a[0] != 1:
        raise ValueError(f"Series const term = {a[0]}")
    b = {0: Integer(1)}
    for n in range(1, N + 1):
        s = Integer(0)
        for k in range(1, n + 1):
            s += a[k] * b[n - k]
        b[n] = expand(-s)
    out = Integer(0)
    for d in range(N + 1):
        out += b[d] * T**d
    return out

def main():
    t0 = time.time()
    B_MAX = 15
    for (Uv, Vv) in [(0, 0), (1, 1), (2, 3)]:
        print(f"\n=== (U,V) = ({Uv}, {Vv}) ===")
        t1 = time.time()
        P_uv = compute_P_at(Uv, Vv, B_MAX)
        FP = build_FP(P_uv, B_MAX)
        # Apply L
        LFP = apply_L(FP, Uv, Vv)
        LFP = truncate_T(LFP, B_MAX - 1)
        print(f"  L·F_P computed in {time.time()-t1:.1f}s")

        # LFP / F_P
        invFP = one_over_series(FP, B_MAX - 1)
        ratio = truncate_T(expand(LFP * invFP), B_MAX - 1)
        rp = Poly(expand(ratio), T)
        print(f"  LFP / F_P as series in T (coefs in E_3):")
        for d in range(B_MAX):
            c = expand(rp.coeff_monomial(T**d))
            if c != 0:
                print(f"    [T^{d}]  {c}")

if __name__ == '__main__':
    main()
