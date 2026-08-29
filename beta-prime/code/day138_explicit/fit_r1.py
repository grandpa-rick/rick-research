"""Day 138 — Fit r_b^{(1)} as a linear combination of products phi_i * phi_j.

r_b^{(1)} has (1,1,2)-weight = b - 2.  Support x_1 + x_2 ≤ b - 2.

Ansatz: r_b^{(1)} = sum_{1 ≤ i < j ≤ b} c_{ij}(b) · phi_i * phi_j
where phi_k = E_2 + k*E_1 + k^2, so phi_i*phi_j has weight 2.

Wait: phi_i * phi_j is a polynomial in E_1, E_2 of top-weight 2 (in E_1, E_2)
but including lower-weight terms. So sum over C(b, 2) pairs gives a polynomial
of weight ≤ 2. But r_b^{(1)} has weight ≤ b - 2, not weight ≤ 2.

For b = 3: r_3^{(1)} has weight ≤ 1. Doesn't fit degree-2 basis unless c's are zero...
Actually r_3^{(1)} = 25 E_1 + 9 E_2 + 57. It's degree 1 in E_1, E_2, so YES it fits
as combo of {1, phi_i} — but then not "phi_i * phi_j". Hmm.

Let me re-index: r_b^{(1)} weight in (1,1,2)-grading of P_b: total weight of E_3 is 2,
so if P_b has weight ≤ b, then r_b^{(1)} has weight ≤ b-2. For b=3, that's ≤ 1.
For b=4, that's ≤ 2. So my ansatz phi_i * phi_j (weight ≤ 2) works only for b=4+.

Let me try a more general ansatz for each b:
r_b^{(1)} = sum over subsets S ⊆ [b] of size b-2 of c_S · prod_{k ∈ S} phi_k

This has C(b, b-2) = C(b, 2) terms, each of weight ≤ b-2. That's a natural basis.

Verify: for b=3, subsets of size 1: {1}, {2}, {3}. r_3^{(1)} = c_1 phi_1 + c_2 phi_2 + c_3 phi_3.
For b=4, subsets of size 2: {1,2}, {1,3}, ..., {3,4} = 6 subsets. r_4^{(1)} = sum c_{ij} phi_i phi_j.

Try this fit for b = 3..8.
"""

from sympy import symbols, Poly, Integer, expand, factor, Rational, Matrix, linsolve
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


def slice_by_E3(P, k):
    poly = Poly(P, E3)
    d = poly.as_dict()
    return expand(d.get((k,), Integer(0)))


def phi_k(k):
    return E2 + k*E1 + k*k


def prod_phi(S):
    p = Integer(1)
    for k in S:
        p *= phi_k(k)
    return expand(p)


def fit_r_bk(rb1, b, k):
    """Fit rb1 = sum_{S ⊆ [b], |S|=b-2k} c_S · prod_{i in S} phi_i.
    Returns dict {S: coefficient}. If no exact fit, return None.
    """
    size = b - 2 * k
    subsets = list(combinations(range(1, b + 1), size))
    # basis
    basis = [prod_phi(S) for S in subsets]
    # We solve linear system: sum c_i · basis_i = rb1
    # Use Poly.as_dict to build matrix
    target_poly = Poly(rb1, E1, E2).as_dict()
    basis_polys = [Poly(bi, E1, E2).as_dict() for bi in basis]

    # collect all monomials appearing
    monoms = set()
    for d in basis_polys:
        monoms.update(d.keys())
    monoms.update(target_poly.keys())
    monoms = sorted(monoms)

    # Set up matrix
    n_eq = len(monoms)
    n_var = len(basis)
    from sympy import symbols as sym
    cs = sym(f'c_0:{n_var}')
    equations = []
    for m in monoms:
        lhs = sum(cs[i] * basis_polys[i].get(m, 0) for i in range(n_var))
        rhs = target_poly.get(m, 0)
        equations.append(lhs - rhs)
    sol = linsolve(equations, cs)
    if not sol:
        return None
    sol_list = list(sol)[0]
    return {subsets[i]: sol_list[i] for i in range(n_var)}


def main():
    B_MAX = 8
    P = build_P(B_MAX)

    for k in [1, 2, 3]:
        print("=" * 78)
        print(f"Fit r_b^{{({k})}} = sum_{{S subset [b], |S|=b-{2*k}}} c_S · prod_{{i in S}} phi_i")
        print("=" * 78)
        for b in range(2*k, B_MAX + 1):
            rb1 = slice_by_E3(P[b], k)
            if rb1 == 0:
                print(f"  b={b}: r_{b}^({k}) = 0")
                continue
            sol = fit_r_bk(rb1, b, k)
            if sol is None:
                print(f"  b={b}: NO fit (basis insufficient)")
                continue
            # See if free parameters
            print(f"  b={b}: r_{b}^({k}) coefficients c_S:")
            for S, c in sorted(sol.items()):
                print(f"     S={S}: c_S = {c}")
        print()


if __name__ == "__main__":
    main()
