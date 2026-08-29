"""Compute n_7 = N_7[T^20] directly at (U,V)=(0,0) to verify predicted b_7 = 85384566."""
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
        c = Pp.coeff_monomial(T**d)
        out += c * T**d
    return out


def build_FP(P_dict, B_max):
    F = Integer(0)
    for b in range(B_max + 1):
        F += P_dict[b] * T**b / factorial(b)
    return F


def series_log(FP_series, N):
    """log(FP_series) where [T^0]FP_series = 1."""
    G = expand(FP_series - 1)
    logv = Integer(0)
    Gk = Integer(1)
    for k in range(1, N + 1):
        Gk = truncate_T(expand(Gk * G), N)
        if Gk == 0:
            break
        logv = expand(logv + (-1)**(k - 1) * Gk / k)
    return truncate_T(logv, N)


B_MAX = 21  # Need T^20 for N_7[T^20]
t0 = time.time()
print(f"Building P at (U,V)=(0,0) up to b={B_MAX}...")
P = compute_P_at(0, 0, B_MAX)
print(f"  built in {time.time()-t0:.1f}s")

FP = build_FP(P, B_MAX)
t0 = time.time()
L0 = series_log(FP, B_MAX)
print(f"  log(FP) built in {time.time()-t0:.1f}s")

Lp = Poly(expand(L0), E3)

# Extract n_k = N_k[T^{3k-1}] for k = 1..7
print("\n=== N_k[T^{3k-1}] at (U,V)=(0,0) ===")
n_dict = {}
for k in range(1, 8):
    Nk = expand(Lp.coeff_monomial(E3**k))
    if Nk == 0:
        print(f"  k={k}: N_k = 0")
        continue
    Nkp = Poly(Nk, T)
    coeff = Nkp.coeff_monomial(T**(3*k - 1))
    n_dict[k] = coeff
    b_k = (3*k - 1) * coeff
    print(f"  k={k}: n_{k} = N_{k}[T^{3*k-1}] = {coeff} = {Rational(coeff)}")
    print(f"         b_{k} = (3k-1)·n_k = {b_k}")

print("\n=== PREDICTION CHECK ===")
if 7 in n_dict:
    b7_computed = (3*7 - 1) * n_dict[7]
    b7_predicted = 85384566
    print(f"  Computed b_7 = {b7_computed}")
    print(f"  Predicted b_7 (from a_7 = -48005802 via a_k = -b_k + Σ b_i b_j) = {b7_predicted}")
    if b7_computed == b7_predicted:
        print("  ✓ MATCH! Identity verified for k=7.")
    else:
        print(f"  ✗ MISMATCH. Diff = {b7_computed - b7_predicted}")
