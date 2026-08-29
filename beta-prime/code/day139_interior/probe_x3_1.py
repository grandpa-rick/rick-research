"""Day 139 — Interior formula probe for x_3 = 1 slice.

Extract N(b; x_1, x_2, 1) := [E_1^{x_1} E_2^{x_2} E_3^1] P_b
for b = 2..10 and all valid (x_1, x_2) with x_1 + x_2 + 2 <= b.

Then look for structural patterns:
  - Ratios N(b;x_1,x_2,1) / N(b;0,x_2,1) — does x_1-dep factor? (Angle A)
  - Comparison to N(b;x_1,x_2,0) shifted somehow
  - OEIS query on pure sequences (row/column slices, fixed b)

Support: x_1 + x_2 + 2 <= b, i.e. x_1 + x_2 <= b - 2.
"""

from sympy import symbols, Poly, Integer, expand, factor, simplify, sympify
from sympy import Rational, Add, Mul, Pow, gcd

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
    """Return dict {b : P_b} for b in [0, B_max]."""
    Psi = {0: Integer(1), 1: E2 - E1 + 1}
    for b in range(1, B_max):
        term1 = (E2 - (b+1)*E1 + (b+1)**2) * Psi[b]
        term2 = 3*b * E3 * sigma(Psi[b-1])
        term3 = b*(b-1)*(E1 - 2*b - 2) * E3 * sigma(Psi[b-2]) if b >= 2 else Integer(0)
        Psi[b+1] = expand(term1 - term2 - term3)
    return {b: expand(phi_map(Psi[b])) for b in range(B_max + 1)}


def coeff(P_b, x1, x2, x3):
    """Extract N(b; x1, x2, x3) = |[E_1^{x1} E_2^{x2} E_3^{x3}] P_b|."""
    d = Poly(P_b, E1, E2, E3).as_dict()
    return d.get((x1, x2, x3), Integer(0))


def N_boundary(b, x1, x2):
    """Closed form on x_3=0 face: sum over U in [b], |U|=b-x2 of (prod U) * e_{b-x1-x2}(U)."""
    from itertools import combinations
    total = Integer(0)
    for U in combinations(range(1, b+1), b - x2):
        prod_U = Integer(1)
        for k in U:
            prod_U *= k
        # e_{b-x1-x2}(U)
        r = b - x1 - x2
        if r < 0 or r > len(U):
            continue
        e_r = Integer(0)
        for S in combinations(U, r):
            m = Integer(1)
            for k in S:
                m *= k
            e_r += m
        total += prod_U * e_r
    return total


def main():
    B_MAX = 10
    print("Building P_b for b = 0..", B_MAX)
    P = build_P(B_MAX)
    print("Done.\n")

    # ---- Table: N(b; x_1, x_2, 1) ----
    print("=" * 78)
    print("TABLE: N(b; x_1, x_2, 1) for b = 2..%d" % B_MAX)
    print(" (x_1 + x_2 <= b - 2)")
    print("=" * 78)
    for b in range(2, B_MAX + 1):
        print(f"\n--- b = {b} ---")
        # Rows: x_1, Cols: x_2
        max_x1 = b - 2
        header = "x1\\x2 |" + "".join(f"{x2:>9}" for x2 in range(0, b - 1))
        print(header)
        print("-" * len(header))
        for x1 in range(0, max_x1 + 1):
            row = f"{x1:>5} |"
            for x2 in range(0, b - 1):
                if x1 + x2 <= b - 2:
                    N = coeff(P[b], x1, x2, 1)
                    row += f"{int(N):>9}"
                else:
                    row += f"{'.':>9}"
            print(row)

    # ---- Column x_2 = 0, fixed x_3 = 1: sequences by b, x_1 ----
    print()
    print("=" * 78)
    print("COLUMN SEQUENCES: N(b; x_1, 0, 1) — fixed x_1 varies, b increases")
    print("=" * 78)
    for x1 in range(0, 6):
        seq = []
        for b in range(x1 + 2, B_MAX + 1):
            N = coeff(P[b], x1, 0, 1)
            seq.append(int(N))
        print(f"  x_1={x1}: b={x1+2}..{B_MAX}: {seq}")

    print()
    print("=" * 78)
    print("COLUMN SEQUENCES: N(b; 0, x_2, 1) — fixed x_2 varies")
    print("=" * 78)
    for x2 in range(0, 6):
        seq = []
        for b in range(x2 + 2, B_MAX + 1):
            N = coeff(P[b], 0, x2, 1)
            seq.append(int(N))
        print(f"  x_2={x2}: b={x2+2}..{B_MAX}: {seq}")

    # ---- Diagonal x_1 = 0: sequence r_b^{(1)}(0, 0) etc ----
    print()
    print("=" * 78)
    print("DIAGONAL: r_b^{(1)}(0,0) = N(b; 0, 0, 1) — for OEIS lookup")
    print("=" * 78)
    seq = [int(coeff(P[b], 0, 0, 1)) for b in range(2, B_MAX + 1)]
    print(f"  b=2..{B_MAX}: {seq}")

    # ---- Attack angle A: Ratio N(b;x_1,x_2,1) / N(b;0,x_2,1) — does x_1 sep? ----
    print()
    print("=" * 78)
    print("ANGLE A: Ratio N(b; x_1, x_2, 1) / N(b; 0, x_2, 1)")
    print(" If x_1-dep factors, ratio should be independent of x_2")
    print("=" * 78)
    for b in range(4, B_MAX + 1):
        print(f"\n--- b = {b} ---")
        for x2 in range(0, b - 1):
            row = f"  x2={x2}:"
            for x1 in range(0, b - 1 - x2):
                if x1 + x2 <= b - 2:
                    denom = coeff(P[b], 0, x2, 1)
                    if denom == 0:
                        continue
                    ratio = Rational(int(coeff(P[b], x1, x2, 1)), int(denom))
                    row += f" x1={x1}:{ratio}"
            print(row)


if __name__ == "__main__":
    main()
