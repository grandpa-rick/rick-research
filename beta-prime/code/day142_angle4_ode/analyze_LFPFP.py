"""Analyze [E_3^k] X = [E_3^k] (LFP/FP) as polynomials in (U, V)."""

import sys, os, time
sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day140_interior')

from compute_P_fast import compute_P_at
from verify_gf_form import E3
from sympy import (symbols, expand, Integer, Rational, Poly, factorial,
                   rf, factor, diff)

U, V = symbols('U V')
T = symbols('T')

def theta(P):
    return expand(T * diff(P, T))

def apply_L(P):
    P1 = expand(V*P + theta(P))
    P2 = expand(U*P1 + theta(P1))
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
    B_MAX = 10
    print(f"Building P_b in (U, V, E_3) up to b={B_MAX}")
    P_uv = compute_P_at(U, V, B_MAX)
    print(f"  built in {time.time()-t0:.1f}s")

    FP = build_FP(P_uv, B_MAX)
    print("Computing LFP...")
    t1 = time.time()
    LFP = truncate_T(apply_L(FP), B_MAX - 1)
    print(f"  in {time.time()-t1:.1f}s")

    print("Computing 1/FP...")
    t2 = time.time()
    invFP = one_over_series(FP, B_MAX - 1)
    print(f"  in {time.time()-t2:.1f}s")

    print("Computing LFP/FP...")
    t3 = time.time()
    X = truncate_T(expand(LFP * invFP), B_MAX - 1)
    print(f"  in {time.time()-t3:.1f}s")

    Xp = Poly(expand(X), E3)
    print("\n\n=== [E_3^k] X, as polynomials in T with (U, V)-poly coefs ===")
    for k in range(1, 5):
        Xk = expand(Xp.coeff_monomial(E3**k))
        if Xk == 0:
            continue
        print(f"\n[E_3^{k}] X:")
        Xkp = Poly(Xk, T)
        for d in range(B_MAX):
            c = Xkp.coeff_monomial(T**d)
            if c != 0:
                # factor over (U, V)
                cf = factor(c)
                print(f"  [T^{d}]  ={cf}")

if __name__ == '__main__':
    main()
