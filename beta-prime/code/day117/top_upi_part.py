"""Day 117 — Test the conjecture:
  Top-(u,pi)-deg-j part of S_j equals (e_2 - e_1)^j.

If true, this gives a CLOSED FORM for the top part of S_j in F^j:
  bar{S_j} = (bar{e_2} - bar{e_1})^j in bar{F}^j.

And it implies bar{E} = mult by g := bar{e_2} - bar{e_1} on bar{Lambda_3}.
Then bar{E}: bar{F}^k -> bar{F}^{k+1} trivially (since g in F^1).
So E: F^k -> F^{k+1}, hence S_j = E^j(1) in F^j.
"""
from ordinary_schur_deg import factorial_schur, all_partitions_len_le_3
from route_v_probe import substitute_sigma_pi, joint_u_pi_deg, bt_tables
from sympy import symbols, expand, Integer, Poly, simplify

u, y, c = symbols('u y c')
e1, e2, e3 = symbols('e_1 e_2 e_3')


def sym_poly_to_e_basis(f, xs):
    """Given a symmetric polynomial f(u, y, c), express as polynomial in e_1, e_2, e_3.
    Uses the fact that Q[u,y,c]^S3 = Q[e_1, e_2, e_3]."""
    # Use Groebner basis / recursion. Simplest: repeatedly extract the "leading monomial"
    # e_1^i1 * e_2^i2 * e_3^i3 (in some order) and subtract.
    # Easier: use sympy's sympify / groebner functionality if available.
    # Actually, use resultant: for a symmetric poly, expand using power sums and Newton.
    # Or: since it's polynomial with rational coeffs, express as poly in u, y, c;
    # substitute u -> e_1 - y - c, then y -> ...; this becomes messy.
    # Cleanest: represent f as sum of monomials, group by S3-orbits (monomial symm funcs),
    # then convert m_lambda to e_1, e_2, e_3.
    p = Poly(expand(f), u, y, c)
    # Monomial symmetric functions in 3 variables
    from collections import defaultdict
    orbits = defaultdict(lambda: Integer(0))
    for mono, coeff in p.terms():
        # sort mono descending to get the "partition"
        part = tuple(sorted(mono, reverse=True))
        orbits[part] += coeff
    # Now express each m_lambda in e-basis via Newton or explicit formula
    # For 3 variables, use:
    #   m_(0) = 1
    #   m_(1) = e_1
    #   m_(2) = e_1^2 - 2 e_2
    #   m_(1,1) = e_2
    #   m_(3) = e_1^3 - 3 e_1 e_2 + 3 e_3
    #   m_(2,1) = e_1 e_2 - 3 e_3
    #   m_(1,1,1) = e_3
    #   etc.
    # We build these iteratively using power-sum -> Newton.
    # Alternative: since f is symmetric, its e-expansion is unique. We compute it
    # by "peeling off": find leading (in some order) e-monomial, subtract, iterate.
    # Order e-monomials by (deg = i1 + 2*i2 + 3*i3, then lex).
    from sympy import sympify
    remaining = expand(f)
    result = Integer(0)
    max_iter = 200
    for _ in range(max_iter):
        if remaining == 0:
            break
        # Get remaining as poly in u, y, c
        p_rem = Poly(remaining, u, y, c)
        # Find "leading" monomial: the one with maximum (u, y, c) in lex order.
        # For symmetric poly, leading term u^a y^b c^d has a >= b >= d.
        leading_mono = None
        leading_coeff = 0
        for mono, coeff in p_rem.terms():
            if leading_mono is None or mono > leading_mono:
                leading_mono = mono
                leading_coeff = coeff
        # Convert to partition (a, b, d), a >= b >= d.
        (a, b, d) = leading_mono
        # e_1^(a-b) * e_2^(b-d) * e_3^d has leading monomial u^a y^b c^d with coefficient 1
        i1 = a - b
        i2 = b - d
        i3 = d
        # e_1 = u + y + c, e_2 = uy + uc + yc, e_3 = uyc
        # e_1^i1 e_2^i2 e_3^i3: symmetric poly, leading u^i1 * u^i2 y^i2 * u^i3 y^i3 c^i3 (leading is u^{i1+i2+i3} y^{i2+i3} c^{i3})
        # Wait more carefully: leading monomial of e_1 is u; of e_2 is u*y; of e_3 is u*y*c.
        # So e_1^i1 e_2^i2 e_3^i3 has leading = u^i1 * (u*y)^i2 * (u*y*c)^i3 = u^{i1+i2+i3} y^{i2+i3} c^{i3}.
        # (a, b, d) = (i1+i2+i3, i2+i3, i3). Yes: a - b = i1, b - d = i2, d = i3.
        # coefficient of leading is 1. So subtract leading_coeff * e_1^i1 e_2^i2 e_3^i3.
        e1_expr = u + y + c
        e2_expr = u*y + u*c + y*c
        e3_expr = u*y*c
        term = leading_coeff * (e1_expr ** i1) * (e2_expr ** i2) * (e3_expr ** i3)
        result += leading_coeff * (e1 ** i1) * (e2 ** i2) * (e3 ** i3)
        remaining = expand(remaining - term)
    else:
        print(f"WARNING: did not converge in {max_iter} iterations, remaining={remaining}")
    return expand(result)


def top_upi_part(f_in_e, k):
    """Given f as polynomial in e_1, e_2, e_3, return the monomials with weighted degree = k."""
    p = Poly(f_in_e, e1, e2, e3)
    top = Integer(0)
    for mono, coeff in p.terms():
        i1, i2, i3 = mono
        if i1 + i2 + 2 * i3 == k:
            top += coeff * e1**i1 * e2**i2 * e3**i3
    return expand(top)


if __name__ == "__main__":
    xs = (u, y, c)
    JMAX = 5
    T = bt_tables(JMAX)
    for j in range(JMAX + 1):
        Sj = Integer(0)
        for mu, kap in T[j]:
            Sj += kap * factorial_schur(mu, xs)
        Sj = expand(Sj)
        # Convert to e-basis
        Sj_e = sym_poly_to_e_basis(Sj, xs)
        # Extract top-(u,pi)-deg-j part
        top = top_upi_part(Sj_e, j)
        # Conjectured: (e_2 - e_1)^j
        conjectured = expand((e2 - e1) ** j)
        diff = expand(top - conjectured)
        status = "MATCH" if diff == 0 else "DIFFER"
        print(f"j={j}: top-(u,pi)-deg-{j} part of S_{j} in e-basis = {top}")
        print(f"      (e_2 - e_1)^{j} = {conjectured}")
        print(f"      -> {status}")
        print()
