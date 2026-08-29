"""Day 138 — Probe pattern in r_b^{(k)} and q_b^{(0)}.

Ansatz to test: is P_b a sum over set-partitions/matchings of [b] with
each pair (i, j) contributing an "E_3-carrying weight" g_{ij} and each
singleton k contributing phi_k = E_2 + k E_1 + k^2?

Also: probe q_b^{(0)}, the E_3=0 part of Q_b.
"""
from sympy import symbols, Poly, Integer, expand, factor, simplify, Rational, cancel
from itertools import combinations
from functools import lru_cache

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
    """tau = phi sigma phi"""
    return phi_map(sigma(phi_map(P)))


def build_P_Q(B_max):
    """Return P and Q up to B_max."""
    Psi = {0: Integer(1), 1: E2 - E1 + 1}
    for b in range(1, B_max):
        term1 = (E2 - (b+1)*E1 + (b+1)**2) * Psi[b]
        term2 = 3*b * E3 * sigma(Psi[b-1])
        term3 = b*(b-1)*(E1 - 2*b - 2) * E3 * sigma(Psi[b-2]) if b >= 2 else Integer(0)
        Psi[b+1] = expand(term1 - term2 - term3)
    P = {b: expand(phi_map(Psi[b])) for b in range(B_max + 1)}
    # Q_b defined via Q_b = 3 tau(P_{b-1}) - (b-1)(E_1 + 2b + 2) tau(P_{b-2})
    # for b >= 1.  Q_0 is not used.  Base: Q_1 = 3 tau(P_0) - 0 = 3.
    Q = {}
    for b in range(1, B_max + 1):
        term1 = 3 * tau(P[b-1])
        term2 = (b-1) * (E1 + 2*b + 2) * tau(P[b-2]) if b >= 2 else Integer(0)
        Q[b] = expand(term1 - term2)
    return P, Q


def slice_by_E3(P, kmax=None):
    poly = Poly(P, E3)
    d = poly.as_dict()
    result = {}
    for (k,), coef in d.items():
        result[k] = expand(coef)
    return result


def phi_k(k):
    return E2 + k*E1 + k*k


def prod_phi_over_set(S):
    """product of phi_k for k in S"""
    p = Integer(1)
    for k in S:
        p *= phi_k(k)
    return expand(p)


def main():
    B_MAX = 8
    P, Q = build_P_Q(B_MAX)

    print("=" * 78)
    print("q_b^{(0)} = [E_3^0] Q_b for b = 1..7")
    print("=" * 78)
    q0 = {}
    for b in range(1, B_MAX + 1):
        q0[b] = slice_by_E3(Q[b]).get(0, Integer(0))
        print(f"  b={b}: q_{b}^(0) = {q0[b]}")

    print()
    print("=" * 78)
    print("Try Ansatz: q_b^{(0)} = 3 * prod_{k=1..b-1} phi_k evaluated at shift + ...")
    print("=" * 78)
    for b in range(1, B_MAX + 1):
        # tau(p_{b-1}): tau applied to prod_{k=1..b-1} phi_k
        p_bm1 = prod_phi_over_set(range(1, b))  # empty product for b=1
        # This is p_{b-1} = P_{b-1}|_{E_3=0}
        # Note q_b^{(0)} at leading order (E_3 in Q's τ maps) comes from 3 τ(P_{b-1})|_{E_3=0}
        # But that's involved.
        pass

    # Let me try: q_b^{(0)} =? 3 * tau(p_{b-1})|_{E_3->0} + correction
    print("Try: 3 * (tau applied to prod_{k=1..b-1} phi_k) with E_3->0")
    for b in range(1, B_MAX + 1):
        p_bm1 = prod_phi_over_set(range(1, b))
        t_p = tau(p_bm1).subs(E3, 0)
        # Actually tau(p_bm1) is already E_3-free since p_bm1 is E_3-free... no wait
        # tau sends E_1 → E_1+3, E_2 → 2E_1+E_2+3, E_3 → E_1+E_2+E_3+1
        # So tau(polynomial in E_1, E_2) is polynomial in E_1, E_2 (E_3 not involved
        # since p_bm1 has no E_3).
        # So tau(p_bm1) is E_3-free.
        term1 = 3 * expand(t_p)
        # tau(P_{b-2}) — but tau(P_{b-2})|_{E_3=0} = τ̌(P_{b-2})
        tau_Pbm2 = tau(P[b-2] if b >= 2 else Integer(1))
        tau_Pbm2_e3_0 = expand(tau_Pbm2.subs(E3, 0))
        term2 = (b-1) * (E1 + 2*b + 2) * tau_Pbm2_e3_0 if b >= 2 else Integer(0)
        result = expand(term1 - term2)
        # compare to q_b^{(0)}
        diff = expand(result - q0[b])
        print(f"  b={b}: predicted q_{b}^(0) - actual = {diff}")

    print()
    print("=" * 78)
    print("PROBE: q_b^{(0)} - 3 * tau(p_{b-1}) : should factor via (b-1)")
    print("=" * 78)
    # q_b^{(0)} - 3 tau(p_{b-1}) should be (b-1)(E_1 + 2b+2) * something
    # since q_b^{(0)} = 3 taǔ(P_{b-1}) - (b-1)(E_1 + 2b+2) taǔ(P_{b-2})
    # and taǔ(P) is the same as tau applied to P then E_3 set to 0.
    for b in range(1, B_MAX + 1):
        # Actually q_b^{(0)} directly = 3 τ̌(P_{b-1}) - (b-1)(E_1+2b+2) τ̌(P_{b-2})
        # Note: P_{b-1} = p_{b-1} + E_3 · (stuff). τ maps E_3 to E_1+E_2+E_3+1.
        # After τ then set E_3=0: E_3 → E_1+E_2+1.
        # So τ̌(P_{b-1}) = τ'(p_{b-1}) + (E_1+E_2+1)·τ'([E_3^1]P_{b-1}) + ...
        # where τ' is τ restricted to E_1, E_2 substitution.
        # For b-1 ≤ 1, [E_3^k]P_{b-1} = 0 for k ≥ 1, so τ̌(P_{b-1}) = τ'(p_{b-1}).
        # For b-1 = 2: [E_3^1]P_2 = 3, so τ̌(P_2) = τ'(p_2) + 3(E_1+E_2+1) = τ'(p_2)+3P_1.

        # For simplicity, just check q_b^{(0)} directly:
        # q_b^{(0)} - 3 * tau(P_{b-1}).subs(E_3, 0) should equal
        #   -(b-1)(E_1+2b+2) * tau(P_{b-2}).subs(E_3, 0)
        tau_Pbm1_e3_0 = expand(tau(P[b-1]).subs(E3, 0)) if b >= 1 else Integer(0)
        expected_diff = -( (b-1) * (E1 + 2*b + 2) * expand(tau(P[b-2] if b >= 2 else Integer(1)).subs(E3, 0))) if b >= 2 else Integer(0)
        actual_diff = expand(q0[b] - 3 * tau_Pbm1_e3_0)
        diff = expand(actual_diff - expected_diff)
        print(f"  b={b}: q_{b}^(0) - 3*τ(P_{b-1})|_E3=0 - [-(b-1)(E_1+2b+2)τ(P_{b-2})|_E3=0] = {diff}")

    # Show what τ(P_b)|_{E_3=0} looks like for small b
    print()
    print("=" * 78)
    print("τ(P_b) with E_3 → 0:  τ shifted P_b evaluated at E_3=0")
    print("=" * 78)
    for b in range(0, B_MAX + 1):
        val = expand(tau(P[b]).subs(E3, 0))
        print(f"  b={b}: τ(P_{b})|_E3=0 = {val}")

    # Special: τ(p_b) = ?
    print()
    print("Same thing but only applying τ to p_b (E_3-free part):")
    for b in range(0, B_MAX + 1):
        pb = prod_phi_over_set(range(1, b + 1))
        val = expand(tau(pb).subs(E3, 0))
        # Also try to factor as prod of (E_2 + k E_1 + k^2) shifted
        # τ(E_2 + k E_1 + k^2) = (2E_1+E_2+3) + k(E_1+3) + k^2 = E_2 + (k+2)E_1 + k^2+3k+3
        # = E_2 + (k+2)E_1 + (k+1)^2 + k + 2? Let's see: (k+1)^2 = k^2+2k+1, so k^2 + 3k+3 = (k+1)^2 + k+2. Not clean.
        # Better: E_2 + (k+2)E_1 + (k+2)^2 - k - 1 = E_2 + (k+2)E_1 + k^2+4k+4-k-1 = E_2 + (k+2)E_1 + k^2+3k+3 ✓
        # So τ(φ_k) = φ_{k+2} - (k+1).
        print(f"  b={b}: τ(p_{b})|_E3=0 = {val}")

    # Verify τ(φ_k) = φ_{k+2} - (k+1)
    print()
    print("Check: τ(φ_k) = φ_{k+2} - (k+1)?")
    for k in range(0, 5):
        lhs = expand(tau(phi_k(k)))
        rhs = expand(phi_k(k+2) - (k+1))
        print(f"  k={k}: τ(φ_{k}) - (φ_{k+2} - (k+1)) = {expand(lhs - rhs)}")


if __name__ == "__main__":
    main()
