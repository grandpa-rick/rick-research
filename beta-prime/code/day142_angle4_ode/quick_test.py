"""Quick test at B_MAX=10 to verify N_1, N_2, N_3 leading coefs = 3/2, 27/5, 417/8."""

import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from compute_P_UV import compute_P_UV, U, V
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day140_interior')
from verify_gf_form import E3
from sympy import (symbols, expand, Integer, Rational, Poly, factorial,
                   rf, factor)

T = symbols('T')

def truncate_T(P, N):
    Pp = Poly(expand(P), T)
    out = Integer(0)
    for d in range(N + 1):
        c = Pp.coeff_monomial(T**d)
        out += c * T**d
    return out

def build_FP(P_UV_dict, B_max):
    F = Integer(0)
    for b in range(B_max + 1):
        F += P_UV_dict[b] * T**b / factorial(b)
    return F

def build_f(B_max):
    F = Integer(0)
    for b in range(B_max + 1):
        F += rf(U, b) * rf(V, b) * T**b / factorial(b)
    return F

def one_over_series(f, N):
    fp = Poly(expand(f), T)
    a = {d: fp.coeff_monomial(T**d) for d in range(N + 1)}
    if a[0] != 1:
        raise ValueError(f"Series does not start with 1: {a[0]}")
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

def series_log_ratio(FP, f, N):
    invf = one_over_series(f, N)
    ratio = truncate_T(expand(FP * invf), N)
    G = expand(ratio - 1)
    logv = Integer(0)
    Gk = Integer(1)
    for k in range(1, N + 1):
        Gk = truncate_T(expand(Gk * G), N)
        if Gk == 0:
            break
        logv = expand(logv + (-1)**(k-1) * Gk / k)
    return truncate_T(logv, N)

def main():
    import time
    t0 = time.time()
    B_MAX = 10
    print(f"Building P_b for b = 0..{B_MAX}")
    P_UV = compute_P_UV(B_MAX)
    print(f"  built in {time.time()-t0:.1f}s")
    t1 = time.time()
    FP = build_FP(P_UV, B_MAX)
    f  = build_f(B_MAX)
    print(f"  FP, f built in {time.time()-t1:.1f}s")
    t2 = time.time()
    L = series_log_ratio(FP, f, B_MAX)
    print(f"  log ratio computed in {time.time()-t2:.1f}s")

    # Extract N_k = [E_3^k] L for k = 1, 2, 3
    Lp = Poly(expand(L), E3)
    for k in [1, 2, 3]:
        Nk = expand(Lp.coeff_monomial(E3**k))
        # Find lowest T degree
        Nkp = Poly(Nk, T)
        for d in range(B_MAX + 1):
            c = Nkp.coeff_monomial(T**d)
            if c != 0:
                print(f"N_{k}[T^{d}] = {expand(c)}  (expected T^{3*k-1})")
                print(f"    at U=V=0: {expand(c.subs([(U,0),(V,0)]))}")
                print(f"    factored: {factor(c)}")
                break
        # Show one more term
        started = False
        for d in range(B_MAX + 1):
            c = Nkp.coeff_monomial(T**d)
            if c != 0:
                if started:
                    print(f"    NEXT: [T^{d}] = {expand(c)}")
                    break
                started = True

if __name__ == '__main__':
    main()
