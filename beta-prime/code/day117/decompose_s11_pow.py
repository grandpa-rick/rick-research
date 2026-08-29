"""Day 117 — Decompose (s^*_{(1,1)})^j in the shifted-Schur basis.

We want to understand: (s^*_{(1,1)})^j = sum_lambda a^j_lambda * s^*_lambda.
Coefficients a^j_lambda give us how the "shifted Pieri" chain works.

If a^j_lambda is nonzero ONLY for |lambda| = 2j: then equal to S_j.
If some appear at |lambda| < 2j (lower shifted degree): those are "corrections".

The claim we want: a^j_{2j-corners} = K_{lambda', (2^j)}, and the LOWER corrections
also (recursively) combine to a term with (u, pi)-degree <= j.
"""
from route_v_probe import (
    bt_tables, ds_uyc, divide, substitute_sigma_pi, joint_u_pi_deg,
    fall, det3,
)
from sympy import symbols, expand, Integer, Poly, Rational
from itertools import product as iprod

u, y, c = symbols('u y c')


def factorial_schur(mu, xs):
    ks = [mu[col] + (2 - col) for col in range(3)]
    rows = [[fall(xs[i], ks[col]) for col in range(3)] for i in range(3)]
    num = det3(rows)
    V = (xs[0] - xs[1]) * (xs[0] - xs[2]) * (xs[1] - xs[2])
    q, r = Poly(num, *xs).div(Poly(V, *xs))
    assert r.as_expr() == 0
    return q.as_expr()


def all_partitions_len_le_3(N):
    """Partitions of integer N with at most 3 parts, returned as tuples padded to length 3."""
    result = []
    for a in range(N, -1, -1):
        for b in range(min(a, N - a), -1, -1):
            for cc in range(min(b, N - a - b), -1, -1):
                if a + b + cc == N:
                    result.append((a, b, cc))
    return result


def expand_in_shifted_basis(f, xs, max_size=8):
    """Given a symmetric polynomial f(u, y, c), expand in {s^*_mu : |mu| <= max_size, ell(mu) <= 3}."""
    # Build all basis elements
    basis = {}
    for N in range(max_size + 1):
        for mu in all_partitions_len_le_3(N):
            basis[mu] = expand(factorial_schur(mu, xs))
    # Set up linear system: solve for coefficients c_mu such that f = sum c_mu * s^*_mu.
    # Since {s^*_mu} is a Q-basis of Q[u,y,c]^S3, and f is symmetric of some max degree,
    # we can solve by leading-term reduction.
    # Order partitions by (|mu|, mu) descending. Recursively subtract off leading terms.
    remaining = expand(f)
    coeffs = {}
    # Sort keys by (|mu|, then reverse lex)
    keys = sorted(basis.keys(), key=lambda mu: (sum(mu), mu), reverse=True)
    for mu in keys:
        # Get leading monomial of s^*_mu in some ordering — use (total degree, lex)
        # Actually we want to project onto s^*_mu. Simplest: pick a "distinguishing" monomial
        # of s^*_mu that no OTHER basis element with smaller sum(mu) contains. This is tricky.
        # Alternative simple approach: solve as linear system in one pass.
        pass
    # Setup linear system with all basis elements
    all_monomials = set()
    for f_expr in list(basis.values()) + [remaining]:
        if f_expr == 0:
            continue
        p = Poly(f_expr, u, y, c)
        for mono, _ in p.terms():
            all_monomials.add(mono)
    all_monomials = sorted(all_monomials)
    # Setup rows: for each monomial, get coefficient in each basis element and in f.
    from sympy import Matrix, zeros
    key_list = keys
    M = zeros(len(all_monomials), len(key_list))
    b_vec = zeros(len(all_monomials), 1)
    for i, mono in enumerate(all_monomials):
        for j, mu in enumerate(key_list):
            p = Poly(basis[mu], u, y, c)
            M[i, j] = p.coeff_monomial(mono)
        p = Poly(remaining, u, y, c)
        b_vec[i, 0] = p.coeff_monomial(mono)
    # Solve
    sol = M.solve(b_vec)
    coeffs = {mu: sol[j, 0] for j, mu in enumerate(key_list) if sol[j, 0] != 0}
    return coeffs


if __name__ == "__main__":
    xs = (u, y, c)
    s11 = factorial_schur((1, 1, 0), xs)
    print(f"s^*_{{(1,1,0)}} = {s11}")
    print()

    for j in range(1, 5):
        lhs = expand(s11 ** j)
        coeffs = expand_in_shifted_basis(lhs, xs, max_size=2 * j)
        print(f"(s^*_{{(1,1)}})^{j} = ")
        for mu, coeff in sorted(coeffs.items(), key=lambda kv: (sum(kv[0]), kv[0]), reverse=True):
            print(f"    {str(coeff):>15} * s^*_{mu}")
        print()
