"""Day 140 — Verify the GF-packaged form:

    P_b(E_1, E_2, E_3) = p_b + E_3 · U_b(E_3 + φ_1)

where U_b(w) := Σ_{m≥0} T[r^{(m)}_·]_b · w^m is a polynomial in w of degree ≤ ⌊(b-2)/2⌋.

Equivalently: U_b(w) = (P_b|_{E_3 = w - φ_1} - p_b) / (w - φ_1).

Also verify: T[p]_b = Σ_{n≥1} (-1)^{n-1} φ_1^{n-1} r_b^{(n)}
(from setting w = 0 in the packaged form; a cross-check of the Neumann series).
"""

from sympy import symbols, Poly, Integer, expand, binomial, div

E1, E2, E3, w = symbols('E1 E2 E3 w')


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


def phi_k(k):
    return E2 + k*E1 + k*k


def p_b_fn(b):
    r = Integer(1)
    for k in range(1, b + 1):
        r *= phi_k(k)
    return expand(r)


def tau_check0(f):
    return expand(f.subs([(E1, E1+3), (E2, 2*E1+E2+3)], simultaneous=True))


def T_op(f_seq, b):
    s = Integer(0)
    for j in range(1, b):
        factor_prod = Integer(1)
        for kk in range(j+2, b+1):
            factor_prod *= phi_k(kk)
        f_jm1 = f_seq.get(j-1, Integer(0))
        f_jm2 = f_seq.get(j-2, Integer(0)) if j >= 2 else Integer(0)
        inner = 3 * tau_check0(f_jm1)
        if j >= 2:
            inner -= (j-1)*(E1 + 2*j + 2) * tau_check0(f_jm2)
        s += factor_prod * j * inner
    return expand(s)


def r_k_extract(P_b, k):
    return expand(Poly(P_b, E3).as_dict().get((k,), Integer(0)))


def main():
    B_MAX = 10
    print(f"Building P_b for b = 0..{B_MAX}")
    P = build_P(B_MAX)
    phi1 = phi_k(1)

    # Compute r_seq for m=0..7 (should cover up to b=10)
    K_MAX = B_MAX // 2 + 2
    r_seq = {}
    r_seq[0] = {b: p_b_fn(b) for b in range(0, B_MAX + 1)}
    for m in range(1, K_MAX + 1):
        r_seq[m] = {b: r_k_extract(P[b], m) for b in range(0, B_MAX + 1)}

    # ---- Verify P_b = p_b + E_3 · U_b(E_3 + φ_1) ----
    print("\n" + "=" * 78)
    print("VERIFY: P_b = p_b + E_3 · U_b(E_3 + φ_1)")
    print("        where U_b(w) = Σ_m T[r^{(m)}]_b · w^m")
    print("=" * 78)
    for b in range(1, B_MAX + 1):
        # Compute U_b as polynomial in w
        U_b = Integer(0)
        for m in range(0, K_MAX + 1):
            U_b += T_op(r_seq[m], b) * w**m
        U_b = expand(U_b)
        # Substitute w -> E_3 + φ_1
        U_b_shift = expand(U_b.subs(w, E3 + phi1))
        # Predicted P_b
        predicted = expand(p_b_fn(b) + E3 * U_b_shift)
        actual = P[b]
        diff = expand(actual - predicted)
        status = "OK" if diff == 0 else f"FAIL diff={diff}"
        print(f"  b={b}: U_b degree in w = {Poly(U_b, w).degree() if U_b != 0 else -1}   {status}")

    # ---- Verify equivalent characterization: U_b(w) = (P_b|_{E_3 = w-φ_1} - p_b)/(w-φ_1) ----
    print("\n" + "=" * 78)
    print("VERIFY (equivalent): U_b(w) = (P_b|_{E_3 = w - φ_1} - p_b) / (w - φ_1)")
    print("=" * 78)
    for b in range(1, B_MAX + 1):
        # U_b from Σ_m T[...] · w^m
        U_b_series = Integer(0)
        for m in range(0, K_MAX + 1):
            U_b_series += T_op(r_seq[m], b) * w**m
        U_b_series = expand(U_b_series)
        # U_b from direct substitution
        Pb_shift = expand(P[b].subs(E3, w - phi1))
        pb = p_b_fn(b)
        numer = expand(Pb_shift - pb)
        # divide by (w - φ_1)
        q, r = div(numer, w - phi1, w)
        q, r = expand(q), expand(r)
        if r != 0:
            print(f"  b={b}: FAIL — remainder in division = {r}")
            continue
        diff = expand(U_b_series - q)
        status = "OK" if diff == 0 else f"FAIL diff={diff}"
        print(f"  b={b}: {status}")

    # ---- Verify T[p]_b = Σ_n (-1)^{n-1} φ_1^{n-1} r_b^{(n)} ----
    print("\n" + "=" * 78)
    print("VERIFY: T[p]_b = Σ_{n≥1} (-1)^{n-1} φ_1^{n-1} r_b^{(n)}  (setting w=0)")
    print("=" * 78)
    for b in range(2, B_MAX + 1):
        lhs = T_op(r_seq[0], b)
        rhs = Integer(0)
        for n in range(1, K_MAX + 1):
            rhs += (-1)**(n-1) * phi1**(n-1) * r_seq[n][b]
        rhs = expand(rhs)
        diff = expand(lhs - rhs)
        status = "OK" if diff == 0 else f"FAIL diff={diff}"
        print(f"  b={b}: {status}")

    # ---- k=5 slice — verify formula ----
    print("\n" + "=" * 78)
    print("VERIFY k=5 slice: r_b^{(5)} = Σ_{m≥4} C(m,4) φ_1^{m-4} T[r^{(m)}]_b")
    print("=" * 78)
    for b in range(2, B_MAX + 1):
        actual = r_seq[5][b] if 5 in r_seq else Integer(0)
        if 5 > b // 2:
            if actual != 0:
                print(f"  b={b}: expected r_b^{{(5)}}=0 (b/2={b//2}<5), got {actual}")
            else:
                print(f"  b={b}: r_b^{{(5)}}=0 as expected")
            continue
        predicted = Integer(0)
        for m in range(4, K_MAX + 1):
            predicted += binomial(m, 4) * phi1**(m-4) * T_op(r_seq[m], b)
        predicted = expand(predicted)
        diff = expand(actual - predicted)
        status = "OK" if diff == 0 else f"FAIL diff={diff}"
        print(f"  b={b}: {status}")

    # ---- Show U_b explicitly for b=4,5,6,7 ----
    print("\n" + "=" * 78)
    print("U_b(w) polynomials (in w with coefs in E_1, E_2) — b = 3..8")
    print("=" * 78)
    for b in range(3, 9):
        U_b = Integer(0)
        for m in range(0, K_MAX + 1):
            U_b += T_op(r_seq[m], b) * w**m
        U_b = expand(U_b)
        print(f"\n  U_{b}(w) =")
        # Print each coefficient
        Ub_poly = Poly(U_b, w)
        for deg in range(Ub_poly.degree()+1):
            c = Ub_poly.coeff_monomial(w**deg)
            if c != 0:
                print(f"    [w^{deg}]  {c}")


if __name__ == "__main__":
    main()
