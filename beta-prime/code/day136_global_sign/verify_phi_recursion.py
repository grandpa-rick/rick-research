"""Day 136 — verify the phi-transformed recursion for P_b := phi(Psi_b).

Test:
    P_{b+1} = [E_2 + (b+1)E_1 + (b+1)^2] * P_b
              + 3b * E_3 * tau(P_{b-1})
              - b(b-1)(E_1 + 2b + 2) * E_3 * tau(P_{b-2})

with tau = phi o sigma o phi:
    tau(E_1) = E_1 + 3
    tau(E_2) = 2 E_1 + E_2 + 3
    tau(E_3) = E_1 + E_2 + E_3 + 1

Also verify that P_b has NONNEGATIVE coefficients (equivalent to sign invariant).
"""

import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day127')
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day128')

from task1_psi_e2_b5_b6 import (
    Psi_direct, sym_to_ebasis_direct, e2_u,
    E1, E2, E3,
)
from sympy import Poly, Integer, expand


def phi(P):
    """Involution E1 -> -E1, E2 -> E2, E3 -> -E3."""
    return expand(P.subs([(E1, -E1), (E2, E2), (E3, -E3)], simultaneous=True))


def tau(P):
    """tau: E1 -> E1+3, E2 -> 2E1+E2+3, E3 -> E1+E2+E3+1."""
    return expand(P.subs([(E1, E1 + 3), (E2, 2*E1 + E2 + 3), (E3, E1 + E2 + E3 + 1)],
                         simultaneous=True))


def sigma(P):
    """sigma: E1 -> E1-3, E2 -> E2-2E1+3, E3 -> E3-E2+E1-1."""
    return expand(P.subs([(E1, E1 - 3), (E2, E2 - 2*E1 + 3), (E3, E3 - E2 + E1 - 1)],
                         simultaneous=True))


def is_nonneg(P):
    """True iff every coefficient of P (in E1,E2,E3) is >= 0."""
    P = expand(P)
    if P == 0:
        return True
    p = Poly(P, E1, E2, E3)
    return all(c >= 0 for c in p.as_dict().values())


def all_nonneg_terms(P):
    P = expand(P)
    if P == 0:
        return True, []
    p = Poly(P, E1, E2, E3)
    bad = [(m, c) for m, c in p.as_dict().items() if c < 0]
    return len(bad) == 0, bad


def main():
    print("Computing Psi_b for b = 0..7 ...", flush=True)
    Psi = {}
    P = {}
    for b in range(0, 8):
        psi_u = Psi_direct(e2_u**b)
        psi_e = sym_to_ebasis_direct(psi_u)
        Psi[b] = expand(psi_e)
        P[b] = phi(Psi[b])
        ok, bad = all_nonneg_terms(P[b])
        print(f"  b={b}: P_b nonneg = {ok}, bad = {bad[:5]}", flush=True)

    print("\nVerify tau = phi o sigma o phi on E_i:", flush=True)
    for g, gname in [(E1, 'E1'), (E2, 'E2'), (E3, 'E3')]:
        lhs = tau(g)
        rhs = phi(sigma(phi(g)))
        print(f"  tau({gname}) = {lhs},  phi.sigma.phi({gname}) = {rhs},  equal = {expand(lhs-rhs) == 0}")

    print("\nVerify recursion (phi-form) for b+1 = 2, 3, 4, 5, 6, 7:", flush=True)
    for bp1 in range(2, 8):
        b = bp1 - 1
        rhs = expand(
            (E_2 := E2) * 0 +  # placeholder
            (E2 + (b+1)*E1 + (b+1)**2) * P[b]
            + 3*b * E3 * tau(P[b-1] if b-1 >= 0 else Integer(0))
            - b*(b-1)*(E1 + 2*b + 2) * E3 * tau(P[b-2] if b-2 >= 0 else Integer(0))
        )
        lhs = P[bp1]
        diff = expand(lhs - rhs)
        print(f"  b+1={bp1}: recursion matches = {diff == 0}")
        if diff != 0:
            print(f"    LHS = {lhs}")
            print(f"    RHS = {rhs}")
            print(f"    Diff = {diff}")

    print("\nVerify original recursion (sanity):")
    for bp1 in range(2, 8):
        b = bp1 - 1
        rhs = expand(
            (E2 - (b+1)*E1 + (b+1)**2) * Psi[b]
            - 3*b * E3 * sigma(Psi[b-1] if b-1 >= 0 else Integer(0))
            - b*(b-1)*(E1 - 2*b - 2) * E3 * sigma(Psi[b-2] if b-2 >= 0 else Integer(0))
        )
        lhs = Psi[bp1]
        diff = expand(lhs - rhs)
        print(f"  b+1={bp1}: original recursion matches = {diff == 0}")


if __name__ == '__main__':
    main()
