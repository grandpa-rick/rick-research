"""Day 123: Express E_j in elementary symmetric basis (in 3 variables) and
check t-weighted degree of each monomial.

Under specialization u_1 = t, u_2 + u_3 = j, u_2 u_3 = t:
  e_1(u) = t + j        deg_t = 1
  e_2(u) = t j + t = t(j+1)   deg_t = 1
  e_3(u) = t * yc = t * t = t^2   deg_t = 2

So a monomial e_1^a1 e_2^a2 e_3^a3 has deg_t = a1 + a2 + 2*a3.

CONJECTURE: For E_j = sum_mu K_{mu',(2^j)} s*_mu (in the shifted-symmetric ring, in 3 vars):
  Writing E_j in e-basis: E_j = sum_alpha c_alpha e_1^{a1} e_2^{a2} e_3^{a3},
  we have a1 + a2 + 2*a3 <= j for all alpha with c_alpha != 0.

If true, deg_t phi(e_2^j) = deg_t E_j|_{spec} <= j. DONE.
"""

import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day122')
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day119')

import sympy as sp
from sympy import symbols, expand, Poly, factor, Integer, Rational, prod
from sympy.functions.combinatorial.numbers import stirling
from collections import defaultdict
from itertools import combinations

e1, e2, e3 = symbols('e1 e2 e3')
u1, u2, u3 = symbols('u1 u2 u3')
j_sym, t = symbols('j t')


def kostka_via_e2j(j_val, max_ell=3):
    current = defaultdict(int)
    current[()] = 1

    def e2_action(nu, ell=max_ell):
        nu_padded = list(nu) + [0] * max(0, ell + 1 - len(nu))
        results = []
        for i in range(ell + 2):
            for j2 in range(i + 1, ell + 2):
                new_nu = list(nu_padded)
                while len(new_nu) <= j2:
                    new_nu.append(0)
                new_nu[i] += 1
                new_nu[j2] += 1
                if all(new_nu[k] >= new_nu[k + 1] for k in range(len(new_nu) - 1)):
                    while new_nu and new_nu[-1] == 0:
                        new_nu.pop()
                    if len(new_nu) <= ell:
                        results.append(tuple(new_nu))
        return results

    for _ in range(j_val):
        new_current = defaultdict(int)
        for nu, c in current.items():
            for lam in e2_action(nu):
                new_current[lam] += c
        current = new_current
    out = {}
    for mu, K in current.items():
        mu_padded = list(mu) + [0] * (3 - len(mu))
        out[tuple(mu_padded)] = K
    return out


def s_star_mu(mu):
    """s*_mu(u1, u2, u3) via Weyl formula (falling factorial version)."""
    mu = list(mu) + [0] * (3 - len(mu))
    mu = mu[:3]
    k = [mu[0] + 2, mu[1] + 1, mu[2]]
    xs = [u1, u2, u3]
    from sympy import Integer as SPI

    def fall(x, m):
        p = SPI(1)
        for i in range(m):
            p *= (x - i)
        return p

    # Weyl determinant / V
    rows = [[fall(xs[i], k[l]) for l in range(3)] for i in range(3)]
    numer = (rows[0][0] * (rows[1][1] * rows[2][2] - rows[1][2] * rows[2][1])
             - rows[0][1] * (rows[1][0] * rows[2][2] - rows[1][2] * rows[2][0])
             + rows[0][2] * (rows[1][0] * rows[2][1] - rows[1][1] * rows[2][0]))
    V = (u1 - u2) * (u1 - u3) * (u2 - u3)
    q, r = sp.div(sp.Poly(expand(numer), u1, u2, u3), sp.Poly(expand(V), u1, u2, u3))
    if r.as_expr() != 0:
        raise ValueError(f'Not divisible for mu={mu}')
    return expand(q.as_expr())


def sym_to_e_basis(f):
    """Convert a symmetric polynomial f(u1, u2, u3) to a polynomial in e1, e2, e3.
    Uses the reduction algorithm: repeatedly subtract e_k^? times leading term.
    Actually easier: use sympy's built-in.
    """
    # sympy has poly_ring with symmetric reduction
    # Use elementary symmetric decomposition via sympy
    from sympy.polys.polyfuncs import symmetrize
    result, remainder, formulas = symmetrize(f, [u1, u2, u3], formal=True)
    if remainder != 0:
        raise ValueError(f'Not symmetric: {f}')
    # result is in terms of formal 's1, s2, s3' — replace with e1, e2, e3
    s_syms = [x for (x, _) in formulas]
    e_subs = dict(zip(s_syms, [e1, e2, e3]))
    return expand(result.subs(e_subs))


def check_conjecture(j_val, verbose=False):
    e2j = kostka_via_e2j(j_val, max_ell=3)
    # Compute E_j = sum_mu K * s*_mu, in u1, u2, u3
    E_j = Integer(0)
    for mu, K in e2j.items():
        E_j += K * s_star_mu(mu)
    E_j = expand(E_j)
    # Convert to e-basis
    E_e = sym_to_e_basis(E_j)
    if verbose:
        print(f'  E_{j_val} in e-basis = {E_e}')
    # Iterate monomials: check a1 + a2 + 2*a3 <= j
    poly = Poly(E_e, e1, e2, e3)
    max_deg = 0
    bad = []
    for (a1, a2, a3), coef in poly.terms():
        d = a1 + a2 + 2 * a3
        max_deg = max(max_deg, d)
        if d > j_val:
            bad.append(((a1, a2, a3), coef, d))
    return max_deg, bad, E_e


def main():
    print('Test: E_j in e_1, e_2, e_3 basis. Conjecture: a1 + a2 + 2*a3 <= j.')
    print('=' * 70)
    for j_val in range(1, 8):
        max_deg, bad, E_e = check_conjecture(j_val, verbose=(j_val <= 3))
        status = 'OK' if not bad else f'FAIL (bad: {bad})'
        print(f'j = {j_val}: max (a1 + a2 + 2 a3) = {max_deg} (target <= {j_val}): {status}')
        if j_val <= 4 and not bad:
            print(f'    E_{j_val} = {E_e}')

    # If confirmed, also verify by substitution
    print()
    print('=' * 70)
    print('Verify E_j(t+j, t(j+1), t^2) = S_j = phi(e_2^j) for small j:')
    for j_val in range(1, 5):
        _, _, E_e = check_conjecture(j_val)
        S_via_e = expand(E_e.subs({e1: t + j_sym, e2: t * (j_sym + 1), e3: t ** 2}))
        # Compare with directly computed S_j
        sys.path.insert(0, '/home/agent/projects/beta-prime/code/day123')
        from leibniz_search import phi_e2_nu
        from n_mu_formula import N_mu, F_mu
        from ab_recursion import build_AB
        A, B = build_AB(20)
        # actually easier: use kostka_via_e2j and F
        e2j = kostka_via_e2j(j_val)
        S_direct = Integer(0)
        for mu, K in e2j.items():
            mu3 = list(mu) + [0] * (3 - len(mu))
            F = F_mu(tuple(mu3[:3]), A, B)
            S_direct += K * F
        # F_mu uses (j, t) — replace j -> j_sym
        S_direct_sub = expand(S_direct)
        # F_mu code uses sympy symbol j, we need to match
        from n_mu_formula import j as j_code
        S_direct_sub = S_direct_sub.subs({j_code: j_sym})
        diff = expand(S_via_e - S_direct_sub)
        print(f'  j = {j_val}: E_j|_spec - S_j = {diff}   ({"MATCH" if diff == 0 else "FAIL"})')


if __name__ == '__main__':
    main()
