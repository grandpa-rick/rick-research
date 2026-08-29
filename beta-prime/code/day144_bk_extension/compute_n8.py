"""Independent cross-check of b_8: directly compute n_8 = N_8[T^{23}] at (U,V)=(0,0).

b_8 = (3*8 - 1) * n_8 = 23 * n_8.

Requires B_MAX = 24 to reach T^{23}.
"""
import sys, os, time
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day140_interior')
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day142_angle4_ode')
from compute_P_fast import compute_P_at
from verify_gf_form import E3
from sympy import (symbols, expand, Integer, Rational, Poly, factorial, factorint)

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


K_MAX_TARGET = 8
B_MAX = 3 * K_MAX_TARGET  # T^{23} needed, but build FP up to T^24 to be safe (T^{3k-1} for k=8 is T^23)
t0 = time.time()
print(f"Building P at (U,V)=(0,0) up to b={B_MAX}...")
P = compute_P_at(0, 0, B_MAX)
print(f"  built in {time.time()-t0:.1f}s")

FP = build_FP(P, B_MAX)
t0 = time.time()
L0 = series_log(FP, B_MAX)
print(f"  log(FP) built in {time.time()-t0:.1f}s")

Lp = Poly(expand(L0), E3)

print("\n=== N_k[T^{3k-1}] at (U,V)=(0,0) ===")
n_dict = {}
for k in range(1, K_MAX_TARGET + 1):
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

print("\n=== CROSS-CHECK ===")
b_known = {1: 3, 2: 27, 3: 417, 4: 7851, 5: 164124, 6: 3661389, 7: 85384566}
try:
    with open('/home/agent/projects/beta-prime/code/day144_bk_extension/a8_b8.txt') as f:
        for line in f:
            if line.startswith('b_8'):
                b_known[8] = int(line.split('=')[1].strip())
except FileNotFoundError:
    pass

for k in sorted(n_dict):
    b_computed = (3*k - 1) * n_dict[k]
    b_ref = b_known.get(k, "n/a")
    match = "MATCH" if b_computed == b_ref else "MISMATCH"
    print(f"  k={k}: b_computed = {b_computed}, expected = {b_ref}   [{match}]")
