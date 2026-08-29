"""Fast path: build P_b in E_3 only at (U,V) = (0,0). Get N_k leading coefs at U=V=0."""

import sys, os, time
sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day140_interior')

from compute_P_fast import compute_P_at
from verify_gf_form import E3
from sympy import (symbols, expand, Integer, Rational, Poly, factorial, rf, factor)

T = symbols('T')

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
    t0 = time.time()
    B_MAX = 18
    print(f"Building P_b at U=V=0 for b = 0..{B_MAX}")
    P_00 = compute_P_at(0, 0, B_MAX)
    print(f"  built in {time.time()-t0:.1f}s")

    # f at U=V=0: rf(0, b) = 0 for b >= 1, so f = 1.
    FP = build_FP(P_00, B_MAX)
    f = Integer(1)

    t1 = time.time()
    # Since f=1 the log ratio is just log(FP).
    L0 = series_log_ratio(FP, f, B_MAX)
    print(f"  log(FP) at U=V=0 in {time.time()-t1:.1f}s")

    Lp = Poly(expand(L0), E3)
    print("\nN_k(T; 0, 0) — all nonzero T-coefficients:")
    for k in range(1, 7):
        Nk = expand(Lp.coeff_monomial(E3**k))
        if Nk == 0:
            print(f"  N_{k} = 0  (up to T^{B_MAX})")
            continue
        Nkp = Poly(Nk, T)
        print(f"\n  N_{k}(T; U=V=0):")
        for d in range(B_MAX + 1):
            c = Nkp.coeff_monomial(T**d)
            if c != 0:
                print(f"    [T^{d}] = {c}")

    # Also report just the leading (T^{3k-1}) coefficient sequence
    print("\n" + "=" * 60)
    print("LEADING SEQUENCE (numerators / denominators):")
    print("=" * 60)
    for k in range(1, 7):
        Nk = expand(Lp.coeff_monomial(E3**k))
        if Nk == 0:
            print(f"  k={k}: N_k = 0")
            continue
        d0 = 3*k - 1
        c = Poly(Nk, T).coeff_monomial(T**d0)
        print(f"  k={k}: N_k[T^{d0}] = {c}  (as fraction: {Rational(c)})")

if __name__ == '__main__':
    main()
