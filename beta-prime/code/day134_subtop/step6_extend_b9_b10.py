"""Extend density + uniform-sign verification to b = 9, 10.
Also verify A_b^{(1)} formula for b = 9, 10 (E_3-free slice).
"""
import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day127')
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day128')

from lib import s, y, t, u1, u2, u3
from task1_psi_e2_b5_b6 import (Psi_direct, sym_to_ebasis_direct, e2_u,
                                 E1, E2, E3, weight_of_e_monom)

from sympy import Poly, Integer, expand
import time


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


def A_n_upper1(n):
    total = Integer(0)
    for r in range(1, n + 1):
        term = Integer(r) ** 2
        for s_ in range(1, n + 1):
            if s_ != r:
                term = expand(term * (E2 - s_ * E1))
        total = expand(total + term)
    return total


def count_p112_at(w):
    c = 0
    for k in range(w // 2 + 1):
        for j in range(w - 2*k + 1):
            i = w - 2*k - j
            if i >= 0:
                c += 1
    return c


for b in [9, 10]:
    t0 = time.time()
    psi_u = Psi_direct(e2_u ** b)
    t1 = time.time()
    psi_e = sym_to_ebasis_direct(psi_u)
    t2 = time.time()

    sub1 = weight_part(psi_e, b - 1)
    p = Poly(sub1, E1, E2, E3)
    nonzero = [(m, c) for m, c in p.as_dict().items() if c != 0]

    print(f"\nb = {b}:  Psi t={t1-t0:.2f}s, sym→E t={t2-t1:.2f}s")
    expected_count = count_p112_at(b - 1)
    print(f"  |support of sub_1[{b}]| = {len(nonzero)}  (predicted A002620({b+1}) = {expected_count})")
    # Uniform sign check
    fails = []
    for (i, j, k), c in nonzero:
        expected_sign = 1 if (i + k) % 2 == 0 else -1
        actual_sign = 1 if c > 0 else -1
        if expected_sign != actual_sign:
            fails.append(((i, j, k), c, expected_sign))
    if fails:
        for f in fails:
            print(f"  SIGN MISMATCH: {f}")
    else:
        print(f"  ✓ Uniform sign (-1)^(x1+x3) confirmed for all {len(nonzero)} monomials.")

    # E_3-free slice matches A_b^{(1)}
    A_up1 = A_n_upper1(b)
    e3_0 = Integer(0)
    for (i, j, k), c in p.as_dict().items():
        if k == 0:
            e3_0 += c * E1**i * E2**j
    e3_0 = expand(e3_0)
    diff = expand(A_up1 - e3_0)
    if diff == 0:
        print(f"  ✓ A_{b}^{{(1)}} = [E_3^0] sub_1[{b}] formula matches.")
    else:
        print(f"  MISMATCH in A_b^(1) formula: diff = {diff}")
