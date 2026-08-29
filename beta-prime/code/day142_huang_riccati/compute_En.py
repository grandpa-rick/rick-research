"""Day 142 — Test whether Huang 2608.07599's E_N(t, q) Riccati generating function
matches Rick's U_b(w) polynomial from Day 140/141.

## Huang's definitions (paper 2608.07599, Sec 4.2)

Set
  b_a(t) = C(t+a, 2a),        d_a(t) = C(t+a, 2a+1)
  h_m(t, q) = (1/m!) * prod_{i=1..m_-} (t+i) * prod_{j=0..m_+ - 1} (t + j*q)
  where m_+ = ceil(m/2), m_- = floor(m/2).

Zigzag GFs:
  E_N(t, q) = Z_{delta_{2N}}(t, q)
  O_N(t, q) = Z_{delta_{2N+1}}(t, q)

Recurrences:
  E_N(t, q) = sum_{a=1..N} (-1)^{a+1} h_{2a}(t, q) E_{N-a}(t, q),   E_0 = 1.
  O_N(t, q) = sum_{a=0..N} (-1)^a h_{2a+1}(t, q) E_{N-a}(t, q).

Alternatively:
  sum E_N x^N = 1 / B_{t,q}(-x),   where B_{t,q}(x) = sum_a h_{2a}(t,q) x^a
                                                    = 2F1(t/q, t+1; 1/2; ux/4)  (u = -q substitution)

## Rick's data

P_b = p_b + E_3 * U_b(E_3 + phi_1) with
  p_b = prod_{k=1..b} (E_2 + k*E_1 + k^2),   phi_1 = E_2 + E_1 + 1

Compare with Huang's E_N.
"""

import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day140_interior')
from verify_gf_form import build_P, phi_k, p_b_fn, E1, E2, E3, w

from sympy import (symbols, expand, Poly, Integer, factorial, Rational, factor,
                   div, simplify, ceiling, floor, Symbol, series, together,
                   sqrt, hyper, binomial, S, denom, numer, Function)

t, q = symbols('t q')


def h_m(m, t_val=t, q_val=q):
    """Huang's h_m(t, q) = (1/m!) * prod_{i=1..m_-} (t+i) * prod_{j=0..m_+ - 1} (t + j*q).
    m_+ = ceil(m/2), m_- = floor(m/2).
    """
    m_plus = (m + 1) // 2   # ceil(m/2)
    m_minus = m // 2         # floor(m/2)
    r = Integer(1)
    for i in range(1, m_minus + 1):
        r *= (t_val + i)
    for j in range(0, m_plus):
        r *= (t_val + j * q_val)
    return r / factorial(m)


def E_N(N_max):
    """Compute E_N(t, q) via recurrence for N=0..N_max."""
    E = {0: Integer(1)}
    for N in range(1, N_max + 1):
        val = Integer(0)
        for a in range(1, N + 1):
            val += (-1)**(a + 1) * h_m(2 * a) * E[N - a]
        E[N] = expand(val)
    return E


def O_N(N_max, E):
    O = {}
    for N in range(0, N_max + 1):
        val = Integer(0)
        for a in range(0, N + 1):
            val += (-1)**a * h_m(2 * a + 1) * E[N - a]
        O[N] = expand(val)
    return O


def display_En(E, N_max):
    print("\n" + "=" * 78)
    print("Huang E_N(t, q) explicitly (from recurrence):")
    print("=" * 78)
    for N in range(0, N_max + 1):
        f = factor(E[N])
        print(f"\n  E_{N}(t, q) = {f}")
        # Also show as polynomial in q with t coefficients
        try:
            Eq = Poly(expand(E[N]), q)
            print(f"    degree in q: {Eq.degree()}")
            for d in range(Eq.degree() + 1):
                c = Eq.coeff_monomial(q**d)
                if c != 0:
                    print(f"    [q^{d}]  {factor(c)}")
        except Exception as ex:
            print(f"    (not polynomial in q: {ex})")


def compute_Ub_polys(B_MAX):
    """Compute Rick's U_b(w) polynomial for b=2..B_MAX."""
    print(f"\nBuilding Rick's P_b for b = 0..{B_MAX}")
    P = build_P(B_MAX)
    phi1 = phi_k(1)
    U = {}
    for b in range(2, B_MAX + 1):
        Pshift = expand(P[b].subs(E3, w - phi1))
        numer = expand(Pshift - p_b_fn(b))
        qq, r = div(numer, w - phi1, w)
        qq = expand(qq)
        if r != 0:
            print(f"  b={b}: division fail, remainder = {r}")
            continue
        U[b] = qq
    return U


def display_Ub(U):
    print("\n" + "=" * 78)
    print("Rick's U_b(w) polynomials:")
    print("=" * 78)
    for b in sorted(U):
        Uq = Poly(U[b], w)
        print(f"\n  U_{b}(w), deg in w = {Uq.degree()}:")
        for d in range(Uq.degree() + 1):
            c = Uq.coeff_monomial(w**d)
            if c != 0:
                print(f"    [w^{d}]  {factor(expand(c))}")


def try_matchings(E, U, N_max):
    """Try various substitutions to see if E_N matches U_b."""
    print("\n" + "=" * 78)
    print("MATCHING TESTS: Huang's E_N vs Rick's U_b")
    print("=" * 78)

    # First, note the degree structures:
    # Rick's U_b(w) has degree ⌊(b-2)/2⌋ in w.
    # So b=2 -> deg 0, b=3 -> deg 0, b=4 -> deg 1, b=5 -> deg 1, ...
    print("\nDegrees in w for U_b:")
    for b in sorted(U):
        Uq = Poly(U[b], w)
        print(f"  U_{b}: deg_w = {Uq.degree()}, expected ⌊(b-2)/2⌋ = {(b-2)//2}")

    # Compute E_N polynomial degrees.
    print("\nE_N degrees in q and t:")
    for N in range(0, N_max + 1):
        EN_expand = expand(E[N])
        Eq = Poly(EN_expand, q, t)
        print(f"  E_{N}(t, q): total degree = {Eq.total_degree()}")
        print(f"    deg in q: {Poly(EN_expand, q).degree() if EN_expand != 0 else 0}")
        print(f"    deg in t: {Poly(EN_expand, t).degree() if EN_expand != 0 else 0}")

    # Note that U_b has coefficients in Q[E_1, E_2]. Rick's U_b has degree in (E_1, E_2)?
    # And w is a separate variable representing E_3 + phi_1.
    # Meanwhile E_N(t, q) has 2 variables. So try:
    # Substitution 1: (t, q) <-> (E_1, E_2)?
    # Substitution 2: (t, q) <-> (u, v)?
    # Substitution 3: (t, q) <-> (U, V) = (u+1, v+1)?
    # Substitution 4: relate w <-> t or q?

    # The paper says E_N(t, q) is a polynomial in t of degree 2N.
    # Rick's U_b(w) with w set to specific value gives poly in (E_1, E_2).

    print("\nAttempting direct comparisons at w=0 (constant term of U_b):")
    for b in sorted(U):
        U_at_0 = expand(U[b].subs(w, 0))
        print(f"  U_{b}(w=0) = {factor(U_at_0)}")

    # Rick's leading motif: 3^k * (2k-1)!! * C(b, 2k)
    # In Huang's Riccati: (1/2)_a appears in denominator of B_{t,q}, giving
    # (1/2)_a = (2a)!/(4^a * a!), which is related to (2a-1)!! by (2a-1)!! = (2a)!/(2^a a!).
    # So (1/2)_a = (2a)! / (4^a a!) = 2^a * a! * (2a-1)!! / (4^a a!) = (2a-1)!! / 2^a.
    # This is where double factorials come in.

    # Try substituting q -> 0 or specific values
    print("\nE_N at q = 0 (limit):")
    for N in range(0, N_max + 1):
        try:
            E_q0 = expand(E[N].subs(q, 0))
            print(f"  E_{N}(t, 0) = {factor(E_q0)}")
        except Exception as ex:
            print(f"  E_{N}(t, 0) = LIMIT ERROR ({ex})")

    print("\nE_N at q = -1 (fence order polynomial):")
    for N in range(0, N_max + 1):
        try:
            E_qm1 = expand(E[N].subs(q, -1))
            print(f"  E_{N}(t, -1) = {factor(E_qm1)}")
        except Exception:
            pass

    print("\nE_N at q = 1:")
    for N in range(0, N_max + 1):
        try:
            E_q1 = expand(E[N].subs(q, 1))
            print(f"  E_{N}(t, 1) = {factor(E_q1)}")
        except Exception:
            pass

    # Try to match degrees:
    # E_N has degree 2N in t. U_b has degree ⌊(b-2)/2⌋ in w. So if we're mapping E_N to U_b:
    # If b = 2N, then U_{2N}(w) has degree N-1 in w. That's different from E_N degree 2N in t.
    # But E_N is a bivariate polynomial! It has degree in q too.

    # Rick's U_b(w) has coefficients that are polynomials in E_1, E_2 of specific degrees.
    # The leading coefficient (in w) is 3^{⌊b/2⌋} (b-1)!! C(b, 2⌊b/2⌋).

    print("\nLEADING coefficient of U_b in w:")
    for b in sorted(U):
        Uq = Poly(U[b], w)
        d = Uq.degree()
        lc = Uq.coeff_monomial(w**d)
        print(f"  [w^{d}] U_{b} = {factor(expand(lc))}")

    print("\nLEADING coefficient of E_N in t:")
    for N in range(0, N_max + 1):
        EN_expand = expand(E[N])
        Et = Poly(EN_expand, t)
        d = Et.degree()
        lc = Et.coeff_monomial(t**d)
        print(f"  [t^{d}] E_{N} = {factor(expand(lc))}")

    print("\nLEADING coefficient of E_N in q:")
    for N in range(0, N_max + 1):
        EN_expand = expand(E[N])
        Eq = Poly(EN_expand, q)
        d = Eq.degree()
        lc = Eq.coeff_monomial(q**d)
        print(f"  [q^{d}] E_{N} = {factor(expand(lc))}")


def main():
    N_MAX = 6
    B_MAX = 8

    # Compute Huang's E_N
    print(f"Computing Huang's E_N(t, q) for N=0..{N_MAX}")
    E = E_N(N_MAX)
    display_En(E, N_MAX)

    # Compute Rick's U_b
    U = compute_Ub_polys(B_MAX)
    display_Ub(U)

    # Compare
    try_matchings(E, U, N_MAX)

    # Print Rick's known LEADING formula for reference
    print("\n" + "=" * 78)
    print("Rick's LEADING closed form (Day 141):")
    print("  [U^{b-2k} V^{b-2k}] r_b^(k) = 3^k * (2k-1)!! * C(b, 2k)")
    print("=" * 78)
    for b in range(2, B_MAX + 1):
        for k in range(1, b // 2 + 1):
            val = 3**k
            for i in range(1, 2*k, 2):
                val *= i
            val *= binomial(b, 2*k)
            print(f"  b={b}, k={k}: 3^{k} * {2*k-1}!! * C({b},{2*k}) = {val}")


if __name__ == "__main__":
    main()
