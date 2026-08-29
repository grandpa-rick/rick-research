"""Day 136 — Test Magnitude Lemma.

Conjecture: For all b >= 1,
    3 * tau(P_{b-1}) - (b-1)(E_1 + 2b + 2) * tau(P_{b-2})
has NONNEGATIVE coefficients.

If true, the phi-recursion rewrites as
    P_{b+1} = [E_2 + (b+1)E_1 + (b+1)^2] * P_b
              + b * E_3 * [3*tau(P_{b-1}) - (b-1)(E_1+2b+2)*tau(P_{b-2})]
where every factor except P_b is manifestly nonneg by hypothesis.
Combined with induction on b, we'd get P_b nonneg for all b.
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


def nonneg_check(P):
    """Return (is_nonneg, list_of_neg_terms)."""
    P = expand(P)
    if P == 0:
        return True, []
    p = Poly(P, E1, E2, E3)
    bad = [(m, c) for m, c in p.as_dict().items() if c < 0]
    return len(bad) == 0, bad


def main():
    print("Computing P_b for b = 0..8 ...", flush=True)
    P = {}
    for b in range(0, 9):
        psi_u = Psi_direct(e2_u**b)
        psi_e = sym_to_ebasis_direct(psi_u)
        P[b] = phi(psi_e)

    print("\nMagnitude Lemma test:")
    print("Q_b := 3*tau(P_{b-1}) - (b-1)(E_1+2b+2)*tau(P_{b-2})")
    print("Is Q_b nonneg for each b >= 1?\n")

    all_pass = True
    for b in range(1, 9):
        Pbm1 = P[b-1] if b-1 >= 0 else Integer(0)
        Pbm2 = P[b-2] if b-2 >= 0 else Integer(0)
        Q = expand(3*tau(Pbm1) - (b-1)*(E1 + 2*b + 2)*tau(Pbm2))
        ok, bad = nonneg_check(Q)
        status = "OK" if ok else "FAIL"
        print(f"  b={b}: Q_b nonneg = {ok}  [{status}]")
        if not ok:
            all_pass = False
            print(f"    NEGATIVE terms in Q_b: {bad[:10]}")
            # Show Q_b
            print(f"    Q_b = {Q}")

    print(f"\n{'ALL PASS' if all_pass else 'FAILURE'}")

    # Also verify: reconstruction works
    print("\nReconstruction check: P_{b+1} = [E_2 + (b+1)E_1 + (b+1)^2] P_b + b*E_3*Q_{b+1}?")
    # Note: The Q_b above was defined for the recursion "b -> b+1", i.e. RHS uses P_{b-1}, P_{b-2}.
    # In the original phi-recursion (indexed by b+1 on LHS), it's 3b*tau(P_{b-1}) - b(b-1)(E_1+2b+2)*tau(P_{b-2}),
    # which factors as b*[3*tau(P_{b-1}) - (b-1)(E_1+2b+2)*tau(P_{b-2})] = b*Q where Q is our lemma statement at "b"
    for bp1 in range(2, 9):
        b = bp1 - 1
        Q = expand(3*tau(P[b-1]) - (b-1)*(E1+2*b+2)*tau(P[b-2] if b >= 2 else Integer(0)))
        rhs = expand((E2 + (b+1)*E1 + (b+1)**2)*P[b] + b*E3*Q)
        lhs = P[bp1]
        print(f"  b+1={bp1}: reconstruction matches = {expand(lhs-rhs) == 0}")


if __name__ == '__main__':
    main()
