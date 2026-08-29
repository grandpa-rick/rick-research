"""Day 138 — Probe P_b = phi(Psi_b) slice by E_3-degree.

Goal:
    - Verify: [E_3^0] P_b = Prod_{k=1..b} (E_2 + k*E_1 + k^2)
    - Compute r_b^{(k)} := [E_3^k] P_b as polynomials in (E_1, E_2)
    - Look for pattern / closed form for r_b^{(k)}.
"""

from sympy import symbols, Poly, Integer, expand, prod, factor, simplify

E1, E2, E3 = symbols('E1 E2 E3')


def sigma(P):
    if P == 0:
        return Integer(0)
    return expand(P.subs(
        [(E1, E1 - 3), (E2, E2 - 2*E1 + 3), (E3, E3 - E2 + E1 - 1)],
        simultaneous=True))


def phi(P):
    if P == 0:
        return Integer(0)
    return expand(P.subs([(E1, -E1), (E3, -E3)], simultaneous=True))


def build_Psi(B_max):
    Psi = {0: Integer(1), 1: E2 - E1 + 1}
    for b in range(1, B_max):
        term1 = (E2 - (b+1)*E1 + (b+1)**2) * Psi[b]
        term2 = 3*b * E3 * sigma(Psi[b-1])
        term3 = b*(b-1)*(E1 - 2*b - 2) * E3 * sigma(Psi[b-2]) if b >= 2 else Integer(0)
        Psi[b+1] = expand(term1 - term2 - term3)
    return Psi


def slice_by_E3(P, kmax):
    """Return list [p_0, p_1, ...] where P = sum p_k(E1,E2) * E3^k."""
    poly = Poly(P, E3)
    d = poly.as_dict()
    result = [Integer(0)] * (kmax + 1)
    for (k,), coef in d.items():
        if k <= kmax:
            result[k] = expand(coef)
    return result


def phi_k(b):
    """(E_2 + k*E_1 + k^2)"""
    return E2 + b*E1 + b*b


def prod_phi(b):
    """prod_{k=1..b} phi_k"""
    p = Integer(1)
    for k in range(1, b+1):
        p *= phi_k(k)
    return expand(p)


def main():
    B_MAX = 10
    print("Building Psi_0 .. Psi_{B_MAX}".format(**{'B_MAX': B_MAX}))
    Psi = build_Psi(B_MAX)
    P = {b: expand(phi(Psi[b])) for b in range(B_MAX + 1)}

    print("=" * 78)
    print("CHECK 1:  [E_3^0] P_b = prod_{k=1..b} (E_2 + k*E_1 + k^2)")
    print("=" * 78)
    for b in range(B_MAX + 1):
        slc = slice_by_E3(P[b], b)
        p0 = slc[0]
        expected = prod_phi(b)
        diff = expand(p0 - expected)
        marker = "OK" if diff == 0 else "FAIL"
        print(f"  b={b:>2}: {marker}   diff = {diff}")

    print()
    print("=" * 78)
    print("CHECK 2:  Print r_b^(k) := [E_3^k] P_b for b = 2..6, k = 0..floor(b/2)")
    print("=" * 78)
    for b in range(2, 7):
        slc = slice_by_E3(P[b], b // 2)
        print(f"\n--- b = {b} ---")
        for k in range(b // 2 + 1):
            print(f"  [E_3^{k}] P_{b} = {slc[k]}")

    print()
    print("=" * 78)
    print("CHECK 3:  For b = 4..8, k = 1:  Look for pattern")
    print("=" * 78)
    for b in range(2, B_MAX + 1):
        slc = slice_by_E3(P[b], 1)
        r1 = slc[1]
        # Try factoring
        try:
            f1 = factor(r1)
        except Exception:
            f1 = r1
        print(f"  b={b}: r_{b}^(1) = {r1}")
        print(f"         factored: {f1}")

    # Also: check p_b as multiplicative structure
    print()
    print("=" * 78)
    print("CHECK 4:  Ratio r_b^(1) / p_{b-2}, r_b^(1) / (b-choose-2 * something)")
    print("=" * 78)
    for b in range(2, B_MAX + 1):
        slc = slice_by_E3(P[b], 1)
        r1 = slc[1]
        # Try r_b^(1) as sum of terms times prod_{k != i, k != j} (E_2 + k E_1 + k^2)
        # If it's of the form: sum_{i<j} c_{i,j}(b) prod_{k not in {i,j}} phi_k
        # then let's just see r_2^(1) = 3, r_3^(1) = 25 E_1 + 9 E_2 + 57
        # Try dividing r_b^(1) by 3 (see if integer)
        print(f"  b={b}: r_b^(1)/3 = {expand(r1/3) if r1 != 0 else 0}")


if __name__ == "__main__":
    main()
