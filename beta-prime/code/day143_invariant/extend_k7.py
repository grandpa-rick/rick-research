"""Extend to k=7 — need T^20, so B_MAX=21."""
import sys, os, time
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day140_interior')
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day142_angle4_ode')
from compute_P_fast import compute_P_at
from verify_gf_form import E3
from sympy import symbols, expand, Integer, Poly, factorial, diff, factorint

T = symbols('T')


def theta(P):
    return expand(T * diff(P, T))


def apply_L_uv0(P):
    return expand(T * theta(theta(P)) - theta(P))


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
    b = {0: Integer(1)}
    inv_a0 = Integer(1) / a[0]
    for n in range(1, N + 1):
        s = sum(a[k] * b[n - k] for k in range(1, n + 1))
        b[n] = expand(-inv_a0 * s)
    return sum(b[d] * T**d for d in range(N + 1))


K_MAX = 7
B_MAX = 3 * K_MAX  # T^{20}
print(f"[k=7] B_MAX={B_MAX}")
t0 = time.time()
P_dict = compute_P_at(0, 0, B_MAX)
print(f"  P_dict built in {time.time()-t0:.1f}s")
t0 = time.time()
FP = build_FP(P_dict, B_MAX)
LFP = truncate_T(apply_L_uv0(FP), B_MAX - 1)
print(f"  L·F_P built in {time.time()-t0:.1f}s")
t0 = time.time()
invFP = one_over_series(FP, B_MAX - 1)
print(f"  1/F_P built in {time.time()-t0:.1f}s")
t0 = time.time()
X = truncate_T(expand(LFP * invFP), B_MAX - 1)
print(f"  X built in {time.time()-t0:.1f}s")

Xp = Poly(X, T)
print(f"\n=== Invariant sequence at (U,V)=(0,0), k=1..{K_MAX} ===")
for k in range(1, K_MAX + 1):
    b = 3*k - 1
    coeff_Tb = Xp.coeff_monomial(T**b)
    coeff = Poly(coeff_Tb, E3).coeff_monomial(E3**k)
    print(f"  k={k}: [E_3^{k} T^{b}] X = {coeff}    factors = {factorint(abs(int(coeff))) if coeff else '{}'}")
