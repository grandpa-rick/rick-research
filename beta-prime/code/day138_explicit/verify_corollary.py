"""Day 138 — Verify Corollary 2.1 formula against direct computation.

N(b; x_1, x_2, 0) = sum_{U subset [b], |U| = b - x_2} (prod_U k) * e_{b - x_1 - x_2}(U)

Compare with direct computation of P_b at (x_1, x_2, 0).
"""

from sympy import symbols, Poly, Integer, expand
from itertools import combinations

E1, E2, E3 = symbols('E1 E2 E3')


def sigma(P):
    if P == 0:
        return Integer(0)
    return expand(P.subs(
        [(E1, E1 - 3), (E2, E2 - 2*E1 + 3), (E3, E3 - E2 + E1 - 1)],
        simultaneous=True))


def phi_map(P):
    if P == 0:
        return Integer(0)
    return expand(P.subs([(E1, -E1), (E3, -E3)], simultaneous=True))


def build_P(B_max):
    Psi = {0: Integer(1), 1: E2 - E1 + 1}
    for b in range(1, B_max):
        term1 = (E2 - (b+1)*E1 + (b+1)**2) * Psi[b]
        term2 = 3*b * E3 * sigma(Psi[b-1])
        term3 = b*(b-1)*(E1 - 2*b - 2) * E3 * sigma(Psi[b-2]) if b >= 2 else Integer(0)
        Psi[b+1] = expand(term1 - term2 - term3)
    return {b: expand(phi_map(Psi[b])) for b in range(B_max + 1)}


def elem_sym(elts, j):
    """j-th elementary symmetric polynomial of a list of numbers."""
    if j == 0:
        return Integer(1)
    if j > len(elts):
        return Integer(0)
    total = Integer(0)
    for combo in combinations(elts, j):
        prod = Integer(1)
        for x in combo:
            prod *= x
        total += prod
    return total


def N_formula(b, x1, x2):
    """N(b; x1, x2, 0) = sum_{U subset [b], |U| = b - x2} (prod_U k) * e_{b-x1-x2}(U)."""
    if x1 + x2 > b:
        return Integer(0)
    U_size = b - x2
    total = Integer(0)
    for U in combinations(range(1, b + 1), U_size):
        prod_U = Integer(1)
        for k in U:
            prod_U *= k
        total += prod_U * elem_sym(list(U), b - x1 - x2)
    return total


def main():
    B_MAX = 8
    P = build_P(B_MAX)

    all_pass = True
    for b in range(0, B_MAX + 1):
        # Extract P_b at E_3 = 0, then dict of (x1, x2) coefficients
        Pb_e30 = expand(P[b].subs(E3, 0))
        d = Poly(Pb_e30, E1, E2).as_dict()
        for x1 in range(b + 1):
            for x2 in range(b - x1 + 1):
                # d.get((x1, x2), 0) is direct coefficient
                direct = d.get((x1, x2), Integer(0))
                formula = N_formula(b, x1, x2)
                if direct != formula:
                    print(f"MISMATCH b={b}, x1={x1}, x2={x2}: direct={direct}, formula={formula}")
                    all_pass = False
    if all_pass:
        print(f"PASSED: N(b; x1, x2, 0) formula matches direct P_b|_E3=0 for ALL b <= {B_MAX} and (x1, x2).")


if __name__ == "__main__":
    main()
