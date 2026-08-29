"""Day 136 — Verify the Q-recursion.

Q_b := 3*tau(P_{b-1}) - (b-1)(E_1+2b+2)*tau(P_{b-2})   (definition, valid for b >= 1)

Claim: For b >= 2,
    Q_b = [(2b+4)E_1 + 3E_2 + b^2 + 3b + 5] * tau(P_{b-2})
         + 3(b-2)(E_1+E_2+E_3+1) * tau(Q_{b-2})

Derivation: Apply P-recursion  P_{c+1} = [E_2+(c+1)E_1+(c+1)^2]*P_c + c*E_3*Q_c
at c = b-2, then apply tau (ring hom, and tau(E_3) = E_1+E_2+E_3+1).

Both sides should agree as polynomials in E1,E2,E3.
"""

import sys
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
    print("Computing P_b for b = 0..8 ...", flush=True)
    P = {}
    for b in range(0, 9):
        psi_u = Psi_direct(e2_u**b)
        psi_e = sym_to_ebasis_direct(psi_u)
        P[b] = phi(psi_e)

    # Compute Q_b directly from definition
    Q = {}
    for b in range(1, 9):
        Pbm1 = P[b-1] if b-1 >= 0 else Integer(0)
        Pbm2 = P[b-2] if b-2 >= 0 else Integer(0)
        Q[b] = expand(3*tau(Pbm1) - (b-1)*(E1 + 2*b + 2)*tau(Pbm2))

    print("\nQ-recursion test:")
    print("  Q_b =? [(2b+4)E_1 + 3E_2 + b^2+3b+5] * tau(P_{b-2}) + 3(b-2)(E_1+E_2+E_3+1) * tau(Q_{b-2})")
    print()
    all_pass = True
    for b in range(2, 9):
        Pbm2 = P[b-2] if b-2 >= 0 else Integer(0)
        Qbm2 = Q[b-2] if (b-2) in Q else Integer(0)
        rhs = expand(((2*b+4)*E1 + 3*E2 + b*b + 3*b + 5) * tau(Pbm2)
                     + 3*(b-2)*(E1+E2+E3+1) * tau(Qbm2))
        lhs = Q[b]
        diff = expand(lhs - rhs)
        ok = (diff == 0)
        print(f"  b={b}: Q-recursion holds = {ok}")
        if not ok:
            all_pass = False
            print(f"    diff = {diff}")

    print(f"\n{'ALL PASS' if all_pass else 'FAILURE'}")

    # Independent nonneg checks
    print("\nSanity: P_b, Q_b nonneg checks:")
    for b in range(9):
        pnn = is_nonneg(P[b]) if b in P else 'n/a'
        qnn = is_nonneg(Q[b]) if b in Q else 'n/a'
        print(f"  b={b}: P nonneg={pnn}, Q nonneg={qnn}")

if __name__ == '__main__':
    main()
