"""Verify the assumption: N_k[T^b] = 0 for 2k ≤ b < 3k-1.
Compute N_k at (U, V) = (0, 0) up to sufficient b, print all nonzero coefficients.
Also check at a NON-degenerate (U, V) point like (1, 1) or (2, 3).
"""
import sys, os, time
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day140_interior')
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day142_angle4_ode')
from compute_P_fast import compute_P_at
from verify_gf_form import E3
from sympy import (symbols, expand, Integer, Rational, Poly, factorial)

T = symbols('T')


def truncate_T(P, N):
    Pp = Poly(expand(P), T)
    out = Integer(0)
    for d in range(N + 1):
        out += Pp.coeff_monomial(T**d) * T**d
    return out


def build_FP(P_dict, B_max):
    F = Integer(0)
    for b in range(B_max + 1):
        F += P_dict[b] * T**b / factorial(b)
    return F


def one_over_series(f, N):
    fp = Poly(expand(f), T)
    a = {d: fp.coeff_monomial(T**d) for d in range(N + 1)}
    if a[0] == 0:
        raise ValueError("Constant coeff is zero")
    b = {0: Integer(1) / a[0]}
    for n in range(1, N + 1):
        s = sum(a[k] * b[n - k] for k in range(1, n + 1))
        b[n] = expand(-s / a[0])
    return sum(b[d] * T**d for d in range(N + 1))


def series_log(G_series, N):
    """log(1 + G) where G_series = 1 + G (i.e., subtract 1 first)."""
    # log series := Σ_{k≥1} (-1)^{k-1} G^k / k
    G = expand(G_series - 1)
    logv = Integer(0)
    Gk = Integer(1)
    for k in range(1, N + 1):
        Gk = truncate_T(expand(Gk * G), N)
        if Gk == 0:
            break
        logv = expand(logv + (-1)**(k - 1) * Gk / k)
    return truncate_T(logv, N)


def check_lowT_Nk_at(U_val, V_val, B_MAX, k_max, label):
    print(f"\n{'='*70}\n Check at (U, V) = {label}   B_MAX = {B_MAX}")
    print("="*70)
    P = compute_P_at(U_val, V_val, B_MAX)
    FP = build_FP(P, B_MAX)
    # f = 2F0(U, V; T) — at (U,V)=(0,0), f = 1. Else compute explicitly.
    from sympy import rf
    f = Integer(0)
    for n in range(B_MAX + 1):
        f += rf(U_val, n) * rf(V_val, n) * T**n / factorial(n)
    f = expand(f)
    inv_f = one_over_series(f, B_MAX)
    ratio = truncate_T(expand(FP * inv_f), B_MAX)
    logratio = series_log(ratio, B_MAX)
    Lp = Poly(expand(logratio), E3)

    for k in range(1, k_max + 1):
        Nk = expand(Lp.coeff_monomial(E3**k))
        if Nk == 0:
            print(f"  N_{k} = 0")
            continue
        Nkp = Poly(Nk, T)
        # Find lowest T degree
        lowest = None
        for d in range(B_MAX + 1):
            if Nkp.coeff_monomial(T**d) != 0:
                lowest = d
                break
        print(f"  N_{k}: lowest T-degree = {lowest}  (expected: {3*k-1})   status = {'OK' if lowest == 3*k-1 else 'DIFFERS'}")
        # Print vanishing check: N_k[T^b] for b < 3k-1 (starting from 2k)
        problems = []
        for b in range(2*k, 3*k - 1):
            c = Nkp.coeff_monomial(T**b)
            if c != 0:
                problems.append((b, c))
        if problems:
            print(f"    VIOLATION: N_k[T^b] != 0 for b in [2k, 3k-2]:")
            for b, c in problems:
                print(f"      N_{k}[T^{b}] = {c}")
        else:
            print(f"    OK: N_{k}[T^b] = 0 for b in [{2*k}, {3*k-2}]")


def main():
    # At (0, 0): fast
    check_lowT_Nk_at(0, 0, 18, 5, "(0, 0)")
    # At (1, 1): non-trivial
    check_lowT_Nk_at(1, 1, 15, 4, "(1, 1)")


if __name__ == '__main__':
    main()
