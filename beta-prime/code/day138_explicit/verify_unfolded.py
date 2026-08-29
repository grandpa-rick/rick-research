"""Day 138 — Verify the P-only unfolded recursion and derive full closed form.

Master unfolded identity:
    P_{b+1} = A_b P_b + 3b E_3 tau(P_{b-1}) - b(b-1)(E_1+2b+2) E_3 tau(P_{b-2})
    ⇒ P_b = p_b + sum_{j=1}^{b-1} (p_b / p_{j+1}) · Delta_j
    where Delta_j = 3j E_3 tau(P_{j-1}) - j(j-1)(E_1+2j+2) E_3 tau(P_{j-2}).

Verify empirically for b ≤ 8.

Then extract [E_3^k] to give closed form for each E_3-slice.
"""

from sympy import symbols, Poly, Integer, expand, simplify

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


def tau(P):
    return phi_map(sigma(phi_map(P)))


def build_P(B_max):
    Psi = {0: Integer(1), 1: E2 - E1 + 1}
    for b in range(1, B_max):
        term1 = (E2 - (b+1)*E1 + (b+1)**2) * Psi[b]
        term2 = 3*b * E3 * sigma(Psi[b-1])
        term3 = b*(b-1)*(E1 - 2*b - 2) * E3 * sigma(Psi[b-2]) if b >= 2 else Integer(0)
        Psi[b+1] = expand(term1 - term2 - term3)
    return {b: expand(phi_map(Psi[b])) for b in range(B_max + 1)}


def phi_k(k):
    return E2 + k*E1 + k*k


def p_b(b):
    result = Integer(1)
    for k in range(1, b + 1):
        result *= phi_k(k)
    return expand(result)


def main():
    B_MAX = 8
    P = build_P(B_MAX)

    print("=" * 78)
    print("CHECK: P-only recursion (no Q!)")
    print("   P_{b+1} = A_b P_b + 3b E_3 tau(P_{b-1}) - b(b-1)(E_1+2b+2) E_3 tau(P_{b-2})")
    print("=" * 78)
    for b in range(0, B_MAX):
        A_b = E2 + (b+1)*E1 + (b+1)**2
        term1 = A_b * P[b]
        term2 = 3*b * E3 * tau(P[b-1]) if b >= 1 else Integer(0)
        term3 = b*(b-1)*(E1 + 2*b + 2) * E3 * tau(P[b-2]) if b >= 2 else Integer(0)
        rhs = expand(term1 + term2 - term3)
        lhs = P[b+1]
        diff = expand(lhs - rhs)
        marker = "OK" if diff == 0 else f"FAIL diff={diff}"
        print(f"  b={b}: {marker}")

    print()
    print("=" * 78)
    print("CHECK: Master unfolded formula P_b = p_b + sum (p_b/p_{j+1}) · Delta_j")
    print("=" * 78)
    for b in range(0, B_MAX + 1):
        pb = p_b(b)
        summ = Integer(0)
        for j in range(1, b):
            # Delta_j = 3j E_3 tau(P_{j-1}) - j(j-1)(E_1+2j+2) E_3 tau(P_{j-2})
            Delta_j = 3*j*E3 * tau(P[j-1])
            if j >= 2:
                Delta_j = Delta_j - j*(j-1)*(E1 + 2*j + 2) * E3 * tau(P[j-2])
            # Multiply by p_b / p_{j+1} = phi_{j+2}...phi_b
            factor = Integer(1)
            for k in range(j+2, b+1):
                factor *= phi_k(k)
            summ += factor * Delta_j
        predicted = expand(pb + summ)
        diff = expand(P[b] - predicted)
        marker = "OK" if diff == 0 else f"FAIL diff={diff}"
        print(f"  b={b}: {marker}")

    print()
    print("=" * 78)
    print("CHECK: Formula for [E_3^1] P_b")
    print("     r_b^(1) = sum_{j=1}^{b-1} (p_b/p_{j+1}) [3j taǔ(P_{j-1}) - j(j-1)(E_1+2j+2) taǔ(P_{j-2})]")
    print("     where taǔ = tau with E_3 → E_1+E_2+1")
    print("=" * 78)
    for b in range(2, B_MAX + 1):
        summ = Integer(0)
        for j in range(1, b):
            # taǔ(P_{j-1}) = tau(P_{j-1}) with E_3 set to 0
            tau_check_Pjm1 = expand(tau(P[j-1]).subs(E3, 0))
            tau_check_Pjm2 = expand(tau(P[j-2] if j >= 2 else Integer(1)).subs(E3, 0)) if j >= 2 else Integer(0)
            inner = 3*j * tau_check_Pjm1
            if j >= 2:
                inner = inner - j*(j-1)*(E1 + 2*j + 2) * tau_check_Pjm2
            factor = Integer(1)
            for k in range(j+2, b+1):
                factor *= phi_k(k)
            summ += factor * inner
        predicted = expand(summ)
        # extract [E_3^1] P_b
        actual = Poly(P[b], E3).as_dict().get((1,), Integer(0))
        actual = expand(actual)
        diff = expand(predicted - actual)
        marker = "OK" if diff == 0 else f"FAIL diff={diff}"
        print(f"  b={b}: {marker}")


if __name__ == "__main__":
    main()
