"""
Try LFP / f (with f known to satisfy Lf=0, so this ratio measures deviation).
Also try (LFP - X · FP) / F_P for various X to see if we can zero it out.
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

def build_f_num(U_val, V_val, B_max):
    F = Integer(0)
    for b in range(B_max + 1):
        F += (rf(U_val, b) * rf(V_val, b)) * T**b / factorial(b)
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

def show_LFP_over_f(Uv, Vv, B_MAX):
    print(f"\n=== (U,V) = ({Uv}, {Vv}) ===")
    P_uv = compute_P_at(Uv, Vv, B_MAX)
    FP = build_FP(P_uv, B_MAX)
    f = build_f_num(Uv, Vv, B_MAX)
    LFP = truncate_T(apply_L(FP, Uv, Vv), B_MAX - 1)

    # LFP / f
    invf = one_over_series(f, B_MAX - 1)
    ratio = truncate_T(expand(LFP * invf), B_MAX - 1)
    rp = Poly(expand(ratio), T)
    print(f"  LFP / f as series in T (coefs in E_3):")
    for d in range(B_MAX):
        c = expand(rp.coeff_monomial(T**d))
        if c != 0:
            print(f"    [T^{d}]  {c}")

def try_L_frobenius(Uv, Vv, B_MAX):
    """Try to fit L F_P = X F_P where X is a polynomial in T and E_3 of specific form."""
    P_uv = compute_P_at(Uv, Vv, B_MAX)
    FP = build_FP(P_uv, B_MAX)
    LFP = truncate_T(apply_L(FP, Uv, Vv), B_MAX - 1)
    invFP = one_over_series(FP, B_MAX - 1)
    X = truncate_T(expand(LFP * invFP), B_MAX - 1)

    # Look at X as poly in E_3 with T-poly coefs.
    Xp = Poly(expand(X), E3)
    for k in range(1, 8):
        Xk = expand(Xp.coeff_monomial(E3**k))
        if Xk == 0:
            continue
        Xkp = Poly(Xk, T)
        print(f"  [E_3^{k}] X:")
        for d in range(B_MAX):
            c = Xkp.coeff_monomial(T**d)
            if c != 0:
                print(f"    [T^{d}]  {c}")

def main():
    for (Uv, Vv) in [(0, 0), (1, 1), (2, 3)]:
        show_LFP_over_f(Uv, Vv, 12)

    print("\n\n" + "=" * 60)
    print("Look at X = LFP/FP as poly in E_3 (coefs in T):")
    print("=" * 60)
    for (Uv, Vv) in [(0, 0), (1, 1), (2, 3)]:
        print(f"\n(U,V) = ({Uv}, {Vv}):")
        try_L_frobenius(Uv, Vv, 15)

if __name__ == '__main__':
    main()
