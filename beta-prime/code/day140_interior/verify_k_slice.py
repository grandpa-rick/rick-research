"""Day 140 — Verify the general k-slice formula

    r_b^{(k)} = Σ_{m ≥ k-1} C(m, k-1) · φ_1^{m-k+1} · T[r^{(m)}_·]_b,
    r^{(0)} := p.

Derivation (Rick):
  r_{b+1}^{(k)} = φ_{b+1} · r_b^{(k)} + b · q_b^{(k-1)}
=> r_b^{(k)} = Σ_{j=1}^{b-1} (p_b/p_{j+1}) · j · q_j^{(k-1)}

  Q_j = 3 τ(P_{j-1}) - (j-1)(E_1+2j+2) τ(P_{j-2})
  τ(P_{j-1}) = Σ_m τ̌₀(r_{j-1}^{(m)}) · (E_3 + φ_1)^m
  [E_3^{k-1}](E_3+φ_1)^m = C(m, k-1) φ_1^{m-k+1}
=> q_j^{(k-1)} = Σ_{m≥k-1} C(m, k-1) φ_1^{m-k+1} · [3τ̌₀(r_{j-1}^{(m)}) - (j-1)(E_1+2j+2)τ̌₀(r_{j-2}^{(m)})]
=> r_b^{(k)} = Σ_{m≥k-1} C(m, k-1) φ_1^{m-k+1} T[r^{(m)}]_b.

For k=1: r_b^{(1)} = Σ_{m≥0} φ_1^m T[r^{(m)}]_b (Day 139).
For k=2: r_b^{(2)} = Σ_{m≥1} m · φ_1^{m-1} T[r^{(m)}]_b.
For k=3: r_b^{(3)} = Σ_{m≥2} C(m,2) · φ_1^{m-2} T[r^{(m)}]_b.
For k=4: r_b^{(4)} = Σ_{m≥3} C(m,3) · φ_1^{m-3} T[r^{(m)}]_b.
"""

from sympy import symbols, Poly, Integer, expand, binomial

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

    # Precompute all r_j^{(m)} and p_j sequences we'll need
    K_MAX = B_MAX // 2 + 2
    r_seq = {}
    r_seq[0] = {b: p_b_fn(b) for b in range(0, B_MAX + 1)}
    for m in range(1, K_MAX + 1):
        r_seq[m] = {b: r_k_extract(P[b], m) for b in range(0, B_MAX + 1)}

    # Check r^{(m)}_j = 0 for j < 2m
    print("\nSupport check: r^{(m)}_j = 0 for j < 2m?")
    for m in range(1, K_MAX + 1):
        for j in range(0, min(2*m, B_MAX + 1)):
            if r_seq[m][j] != 0:
                print(f"  UNEXPECTED: r^{{({m})}}_{j} = {r_seq[m][j]}")
        print(f"  m={m}: r^{{({m})}}_j = 0 for j < min({2*m}, {B_MAX+1}): OK")

    # Test formula for k = 1, 2, 3, 4
    for k in range(1, 5):
        print("\n" + "=" * 78)
        print(f"TESTING k = {k}:  r_b^{{({k})}} = Σ_{{m≥{k-1}}} C(m,{k-1}) φ_1^{{m-{k-1}}} T[r^{{(m)}}]_b")
        print("=" * 78)
        for b in range(2, B_MAX + 1):
            if k > b // 2:
                # r_b^{(k)} must be 0
                actual = r_k_extract(P[b], k)
                if actual == 0:
                    print(f"  b={b}: r_b^{{({k})}} = 0 (empty support), skip")
                else:
                    print(f"  b={b}: r_b^{{({k})}} nonzero but expected zero! Actual={actual}")
                continue
            actual = r_k_extract(P[b], k)
            predicted = Integer(0)
            for m in range(k-1, K_MAX + 1):
                coeff = binomial(m, k-1)
                predicted += coeff * phi1**(m - k + 1) * T_op(r_seq[m], b)
            predicted = expand(predicted)
            diff = expand(actual - predicted)
            status = "OK" if diff == 0 else f"FAIL diff={diff}"
            print(f"  b={b}: {status}")

    # Print r_b^{(2)} table too — this is the Day 140 primary target
    print("\n" + "=" * 78)
    print("r_b^{(2)} EMPIRICAL POLYNOMIALS for b = 4..10 (support: x_1+x_2+4 <= b)")
    print("=" * 78)
    for b in range(4, B_MAX + 1):
        r2 = r_k_extract(P[b], 2)
        print(f"\n  b={b}: r_b^{{(2)}} = {r2}")
        # Numeric at (0,0)
        n00 = int(r2.subs([(E1,0),(E2,0)]))
        print(f"  r_b^{{(2)}}(0,0) = {n00}")

    # Diagonal r_b^{(2)}(0,0) for OEIS
    print("\n" + "=" * 78)
    print("Diagonal r_b^{(2)}(0,0) for b=4..10:")
    seq = [int(r_k_extract(P[b], 2).subs([(E1,0),(E2,0)])) for b in range(4, B_MAX + 1)]
    print(f"  {seq}")


if __name__ == "__main__":
    main()
