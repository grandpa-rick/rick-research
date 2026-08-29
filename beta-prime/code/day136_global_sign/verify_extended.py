"""Extend empirical verification of P_b, Q_b nonnegativity to b=11, 12."""

import sys
import time
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day127')
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day128')

from task1_psi_e2_b5_b6 import Psi_direct, sym_to_ebasis_direct, e2_u, E1, E2, E3
from sympy import Poly, Integer, expand


def phi(P):
    return expand(P.subs([(E1, -E1), (E2, E2), (E3, -E3)], simultaneous=True))


def tau(P):
    return expand(P.subs([(E1, E1+3), (E2, 2*E1+E2+3), (E3, E1+E2+E3+1)], simultaneous=True))


def is_nonneg(P):
    P = expand(P)
    if P == 0:
        return True
    p = Poly(P, E1, E2, E3)
    return all(c >= 0 for c in p.as_dict().values())


def main():
    B_MAX = 11
    print(f"Computing P_b, Q_b for b = 0..{B_MAX} and verifying nonnegativity + recursions...\n", flush=True)
    P = {}
    Q = {}
    for b in range(0, B_MAX + 1):
        t0 = time.time()
        psi_u = Psi_direct(e2_u**b)
        psi_e = sym_to_ebasis_direct(psi_u)
        P[b] = phi(psi_e)
        t1 = time.time()
        p_nn = is_nonneg(P[b])
        if b >= 1:
            Q[b] = expand(3*tau(P[b-1]) - (b-1)*(E1+2*b+2)*tau(P[b-2] if b-2 >= 0 else Integer(0)))
            q_nn = is_nonneg(Q[b])
        else:
            q_nn = 'n/a'
        t2 = time.time()
        print(f"  b={b:2d}: P nonneg = {p_nn}, Q nonneg = {q_nn}  ({t1-t0:.1f}s + {t2-t1:.1f}s)", flush=True)

    print("\nQ-recursion consistency (b=2..11):")
    all_ok = True
    for b in range(2, B_MAX + 1):
        rhs = expand(((2*b+4)*E1 + 3*E2 + b*b + 3*b + 5) * tau(P[b-2])
                     + 3*(b-2)*(E1+E2+E3+1) * tau(Q[b-2] if (b-2) in Q else Integer(0)))
        ok = (expand(Q[b] - rhs) == 0)
        print(f"  b={b}: Q-recursion holds = {ok}")
        if not ok:
            all_ok = False

    print(f"\n{'ALL PASS' if all_ok else 'FAILURE'}")

if __name__ == '__main__':
    main()
