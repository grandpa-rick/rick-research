"""Verify the sub_1 recursion I derived, and compute G(T) via GF.

Recursion:
sub_1[b+1] = (E_2 - (b+1) E_1) sub_1[b] + (b+1)^2 tops[b]
             - 3 b E_3 [D(tops[b-1]) + sigma_top(sub_1[b-1])]
             - b(b-1) E_1 E_3 [D(tops[b-2]) + sigma_top(sub_1[b-2])]
             + 2 b(b-1)(b+1) E_3 sigma_top(tops[b-2])

D(P) = -3 sigma_top(dP/dE1) + 3 sigma_top(dP/dE2) + (E1 - E2) sigma_top(dP/dE3).
sigma_top(E1) = E1, sigma_top(E2) = E2 - 2 E1, sigma_top(E3) = E3.
"""
import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day127')
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day128')

from lib import s, y, t, u1, u2, u3
from task1_psi_e2_b5_b6 import (Psi_direct, sym_to_ebasis_direct,
                                 top_weight_part, e1_u, e2_u, e3_u,
                                 E1, E2, E3, weight_of_e_monom)

from sympy import Poly, Integer, expand, diff, symbols


def sigma_top(P):
    """Apply E2 -> E2 - 2 E1 (leave E1, E3 alone)."""
    return expand(P.subs(E2, E2 - 2*E1))


def D_op(P):
    """The sigma-derivation D: weight-w polynomial to weight-(w-1) part of sigma(P)."""
    P = expand(P)
    d1 = diff(P, E1)
    d2 = diff(P, E2)
    d3 = diff(P, E3)
    return expand(-3 * sigma_top(d1) + 3 * sigma_top(d2) + (E1 - E2) * sigma_top(d3))


def weight_part(P, w):
    P = expand(P)
    if P == 0:
        return Integer(0)
    p = Poly(P, E1, E2, E3)
    out = Integer(0)
    for monom, coeff in p.as_dict().items():
        i, j, k = monom
        if i + j + 2*k == w:
            out += coeff * E1**i * E2**j * E3**k
    return out


# Compute Psi_b for b = 0..8, extract tops[b] = weight-b and sub_1[b] = weight-(b-1)
tops = {}
sub1 = {}
psi = {}

print("Computing Psi_b for b = 0..8...")
for b in range(9):
    if b == 0:
        psi[b] = Integer(1)
    else:
        psi_u = Psi_direct(e2_u**b)
        psi[b] = sym_to_ebasis_direct(psi_u)
    tops[b] = weight_part(psi[b], b)
    sub1[b] = weight_part(psi[b], b - 1) if b >= 1 else Integer(0)
    print(f"  b={b}: computed.")

# Verify sub_1 recursion for b in 0..6 (giving sub_1 for b+1 in 1..7)
print("\n=== Verifying sub_1 recursion ===")
for b in range(7):
    # Compute RHS
    rhs = expand((E2 - (b+1)*E1) * sub1[b] + (b+1)**2 * tops[b])
    if b >= 1:
        rhs = expand(rhs - 3*b * E3 * (D_op(tops[b-1]) + sigma_top(sub1[b-1])))
    if b >= 2:
        rhs = expand(rhs - b*(b-1) * E1 * E3 * (D_op(tops[b-2]) + sigma_top(sub1[b-2])))
        rhs = expand(rhs + 2*b*(b-1)*(b+1) * E3 * sigma_top(tops[b-2]))
    lhs = sub1[b+1]
    diff_ = expand(lhs - rhs)
    if diff_ == 0:
        print(f"  b={b} -> sub_1[{b+1}] recursion MATCHES")
    else:
        print(f"  b={b} -> sub_1[{b+1}] MISMATCH! diff = {diff_}")

print("\nDone.")
