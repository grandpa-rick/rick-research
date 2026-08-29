"""Verify the KEY IDENTITIES that will drive the structural proof.

(I1)  T(u_i * h) = u_i * T(h) - T(D_i * h)             — proven umbral identity
(I2)  T(e_3 * X) = e_3 * sigma(T(X))                    — from (I1) iterated 3x
                                                          sigma = u_i -> u_i - 1 simultaneously
(I3)  Psi(e_1 * f) = (e_1 - 3) Psi(f) - Psi(E(f))       — derivation using (I1)
(I4)  Psi(e_3 * f) = e_3 * sigma(Psi(f))                — from (I2), since sigma(V)=V

For f = e_2^b (eigenvector of E with eigenvalue 2b):
  Psi(e_1 e_2^b) = (E_1 - 2b - 3) Psi_b
  Psi(e_3 e_2^{b-1}) = E_3 * sigma(Psi_{b-1})

Also key computation:
(K1)  Sigma_i u_i (D_j+D_k)(e_2^b V) = (2b+1) e_1 e_2^b V - b (e_1 e_2 - 3 e_3) e_2^{b-1} V
(K2)  e_2(D)(e_2) = e_2                                 — Sigma_{a<b} D_a D_b(e_2)
(K3)  e_2(D(e_2)) = e_2^2 + e_1 e_3                     — Sigma_{a<b} D_a(e_2) D_b(e_2)
(K4)  e_2(D)(V) = 2 V

Then:
  piece_2 - 2 * piece_3 = (b+1)(E_1 - 2b - 3) Psi_b + 3b E_3 sigma(Psi_{b-1})

which gives us the ADEQUATE reduction of piece_2 to piece_3 + Psi-things.

For piece_3 = T(e_2(D)(e_2^b V))/V, expand e_2(D)(e_2^b V) and reduce.
"""

import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day127')
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day128')

from lib import s, y, t as tau, u1, u2, u3, falling
from task1_psi_e2_b5_b6 import (T_u, e1_u, e2_u, e3_u, V, Psi_direct,
                                 sym_to_ebasis_direct, top_weight_part,
                                 E1, E2, E3, weight_of_e_monom, max_weight)
from sympy import expand, Poly, Integer, factor, simplify, symbols, Rational, diff

D1 = lambda p: expand(u1 * diff(p, u1))
D2 = lambda p: expand(u2 * diff(p, u2))
D3 = lambda p: expand(u3 * diff(p, u3))
E_op = lambda p: expand(D1(p) + D2(p) + D3(p))

def e2_D(p):
    return expand(D1(D2(p)) + D1(D3(p)) + D2(D3(p)))

def sigma(p):
    """Simultaneous shift u_i -> u_i - 1."""
    return expand(p.subs({u1: u1-1, u2: u2-1, u3: u3-1}, simultaneous=True))

# ============================
# Verify (K2): e_2(D)(e_2) = e_2
# ============================
print("K2: e_2(D)(e_2) =", expand(e2_D(e2_u) - e2_u), "-> ", "OK" if expand(e2_D(e2_u) - e2_u) == 0 else "FAIL")

# ============================
# Verify (K3): e_2(D(e_2)) = e_2^2 + e_1 e_3
# ============================
K3_val = expand(
    D1(e2_u) * D2(e2_u) + D1(e2_u) * D3(e2_u) + D2(e2_u) * D3(e2_u)
    - (e2_u**2 + e1_u * e3_u)
)
print(f"K3: e_2(D(e_2)) - (e_2^2 + e_1 e_3) = {K3_val} -> {'OK' if K3_val == 0 else 'FAIL'}")

# ============================
# Verify (K4): e_2(D)(V) = 2 V
# ============================
K4_val = expand(e2_D(V) - 2 * V)
print(f"K4: e_2(D)(V) - 2V = {K4_val} -> {'OK' if K4_val == 0 else 'FAIL'}")

# ============================
# Verify (I4): Psi(e_3 * g) = e_3 * sigma(Psi(g))
# ============================
print("\nI4 verification:")
for b in range(0, 5):
    g = expand(e2_u**b)
    lhs = Psi_direct(expand(e3_u * g))
    rhs = expand(e3_u * sigma(Psi_direct(g) if b > 0 else Integer(1)))
    diff_val = expand(lhs - rhs)
    print(f"  b={b}: Psi(e_3 * e_2^{b}) matches e_3 * sigma(Psi(e_2^{b}))? {'YES' if diff_val == 0 else 'NO'}")
    if diff_val != 0:
        print(f"    diff = {diff_val}")

# ============================
# Verify (I3): Psi(e_1 f) = (e_1-3) Psi(f) - Psi(E(f))
# ============================
print("\nI3 verification:")
for b in range(0, 5):
    f = expand(e2_u**b)
    lhs = Psi_direct(expand(e1_u * f))
    rhs = expand((e1_u - 3) * (Psi_direct(f) if b > 0 else Integer(1)) - Psi_direct(E_op(f)))
    diff_val = expand(lhs - rhs)
    print(f"  b={b}: Psi(e_1 e_2^{b}) matches (e_1-3) Psi - Psi(E(f))? {'YES' if diff_val == 0 else 'NO'}")

# ============================
# Verify (K1): Sigma_i u_i (D_j+D_k)(e_2^b V) = (2b+1) e_1 e_2^b V - b (e_1 e_2 - 3 e_3) e_2^{b-1} V
# ============================
print("\nK1 verification:")
for b in range(0, 5):
    g = expand(e2_u**b * V)
    lhs = expand(u1 * (D2(g) + D3(g)) + u2 * (D1(g) + D3(g)) + u3 * (D1(g) + D2(g)))
    rhs = expand((2*b+1) * e1_u * e2_u**b * V - b * (e1_u * e2_u - 3 * e3_u) * e2_u**(b-1) * V if b >= 1
                 else (2*b+1) * e1_u * e2_u**b * V)
    diff_val = expand(lhs - rhs)
    print(f"  b={b}: K1 matches? {'YES' if diff_val == 0 else 'NO'}")
    if diff_val != 0:
        print(f"    diff = {diff_val}")

# ============================
# COMBINE: verify the "piece_2 - 2 piece_3" identity
# ============================
def divV(x):
    x = expand(x)
    q, r = Poly(x, u1, u2, u3).div(Poly(V, u1, u2, u3))
    if r.as_expr() != 0:
        raise ValueError(f"Nonzero remainder: {r.as_expr()}")
    return q.as_expr()

print("\npiece_2 - 2 piece_3 vs (b+1)(E_1-2b-3) Psi_b + 3b E_3 sigma(Psi_{b-1}):")
for b in range(0, 5):
    g = expand(e2_u**b * V)
    # piece_2 = middle
    sum_mid = expand(u1 * T_u(D2(g) + D3(g)) + u2 * T_u(D1(g) + D3(g)) + u3 * T_u(D1(g) + D2(g)))
    piece_2 = divV(sum_mid)
    # piece_3 = N_b
    piece_3 = divV(T_u(e2_D(g)))
    lhs = expand(piece_2 - 2 * piece_3)

    Psi_b = Psi_direct(e2_u**b) if b > 0 else Integer(1)
    Psi_bm1 = Psi_direct(e2_u**(b-1)) if b > 1 else (Integer(1) if b == 1 else Integer(0))
    rhs = expand(
        (b+1) * (e1_u - 2*b - 3) * Psi_b
        + 3 * b * e3_u * sigma(Psi_bm1)
    )
    diff_val = expand(lhs - rhs)
    print(f"  b={b}: matches? {'YES' if diff_val == 0 else 'NO'}")
    if diff_val != 0:
        print(f"    diff = {diff_val}")
