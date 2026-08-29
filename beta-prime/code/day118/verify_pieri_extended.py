"""Day 118 — Extended numerical verification of the STRONG per-term shifted-Pieri
claim (**):

  In s^*_{(1,1)} * s^*_mu = sum_{lambda/mu vert 2-strip} s^*_lambda
                          + sum_{lower lambda} c^lambda_mu s^*_lambda,
  every "lower" lambda that appears (with |lambda| < |mu|+2 OR lambda not a
  vert 2-strip of mu) satisfies d_lambda <= d_mu + 1.

We push |mu| up to 8 or 10, depending on computational tractability.

Note: The 3-variable shifted Schur s*_lambda in 3 variables is nonzero iff
ell(lambda) <= 3. Since (1,1) has length 2, all lambda in
supp(s*_{(1,1)} * s*_mu) also have ell <= 3 as long as ell(mu) <= 3 (because
in 3 vars everything longer vanishes).

This adds one box or two boxes to mu, so support is:
  { lambda : mu ⊆ lambda ⊆ (mu+row+col additions), |lambda| ∈ {|mu|, |mu|+1, |mu|+2} }.

Since we work in 3 variables, we ALSO get any lambda with ell(lambda) <= 3.
Actually s*_{(1,1)} · s*_mu in 3 vars gives ONLY 3-variable-supported lambda,
because outside terms vanish under evaluation at just 3 vars. So the "shifted
Pieri" we observe empirically is the *truncation* of the full shifted Pieri to
3 variables.
"""
import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day117')

from ordinary_schur_deg import factorial_schur, all_partitions_len_le_3
from route_v_probe import substitute_sigma_pi, joint_u_pi_deg
from eprime_filtration import vert_2_strips_from
from sympy import symbols, expand, Integer, Poly
from itertools import combinations
import time

u, y, c = symbols('u y c')


def upi_deg(expr):
    return joint_u_pi_deg(substitute_sigma_pi(expr))


# Cache for basis
_basis_cache = {}
def get_factorial_schur(mu, xs=(u, y, c)):
    if mu not in _basis_cache:
        _basis_cache[mu] = expand(factorial_schur(mu, xs))
    return _basis_cache[mu]


# Cache for d_mu
_d_cache = {}
def get_d(mu):
    if mu not in _d_cache:
        _d_cache[mu] = upi_deg(get_factorial_schur(mu))
    return _d_cache[mu]


def support_of_s11_product(mu):
    """Return all partitions lambda (as length-3 tuples) that can appear in
    supp(s*_{(1,1)} · s*_mu). By Molev-Sagan, |lambda|-|mu| in {0, 1, 2} and
    mu ⊆ lambda. We restrict ell(lambda) <= 3 (needed for 3-variable Schurs).
    """
    result = set()
    mu = tuple(mu)
    while len(mu) < 3:
        mu = mu + (0,)
    # |lambda| = |mu|: only lambda = mu
    result.add(mu)
    # |lambda| = |mu| + 1: add one box to some row i
    for i in range(3):
        nu = list(mu)
        nu[i] += 1
        if all(nu[j] >= nu[j+1] for j in range(2)):
            result.add(tuple(nu))
    # |lambda| = |mu| + 2: add two boxes
    #   (a) two in same row (horizontal 2-strip in one row):
    for i in range(3):
        nu = list(mu)
        nu[i] += 2
        if all(nu[j] >= nu[j+1] for j in range(2)):
            result.add(tuple(nu))
    #   (b) two in different rows (vertical 2-strip):
    for i, j in combinations(range(3), 2):
        nu = list(mu)
        nu[i] += 1
        nu[j] += 1
        if all(nu[k] >= nu[k+1] for k in range(2)):
            result.add(tuple(nu))
    return sorted(result, key=lambda x: (sum(x), x), reverse=True)


def expand_in_shifted_basis_fast(f, mu):
    """Given f = s*_{(1,1)} · s*_mu, decompose into shifted-Schur basis using
    only the a priori possible support (from Molev-Sagan)."""
    from sympy import Matrix, zeros
    xs = (u, y, c)
    supp = support_of_s11_product(mu)
    # Basis of s*_lambda for lambda in supp
    basis_polys = {lam: get_factorial_schur(lam) for lam in supp}
    # Collect all monomials appearing anywhere
    all_monomials = set()
    f_poly = Poly(expand(f), u, y, c)
    for mono, _ in f_poly.terms():
        all_monomials.add(mono)
    for lam, p in basis_polys.items():
        pp = Poly(p, u, y, c)
        for mono, _ in pp.terms():
            all_monomials.add(mono)
    all_monomials = sorted(all_monomials)
    key_list = supp  # ordered by (|lam|, lam) descending
    M = zeros(len(all_monomials), len(key_list))
    b_vec = zeros(len(all_monomials), 1)
    for i, mono in enumerate(all_monomials):
        for j, lam in enumerate(key_list):
            pp = Poly(basis_polys[lam], u, y, c)
            M[i, j] = pp.coeff_monomial(mono)
        b_vec[i, 0] = f_poly.coeff_monomial(mono)
    sol = M.solve(b_vec)
    coeffs = {lam: sol[j, 0] for j, lam in enumerate(key_list) if sol[j, 0] != 0}
    return coeffs


def is_vert_2_strip(mu, lam):
    """Check whether lam/mu is a vertical 2-strip (i.e., 2 boxes added, all in
    distinct rows)."""
    mu_p = tuple(list(mu) + [0] * (3 - len(mu)))
    lam_p = tuple(list(lam) + [0] * (3 - len(lam)))
    diff = [lam_p[i] - mu_p[i] for i in range(3)]
    if sum(diff) != 2:
        return False
    return all(d in (0, 1) for d in diff)


def verify_mu(mu, verbose=False):
    """Verify (**) for a single mu. Returns (ok, d_mu, failures)."""
    xs = (u, y, c)
    s11 = get_factorial_schur((1, 1, 0))
    s_star_mu = get_factorial_schur(mu)
    d_mu = get_d(mu)
    product = expand(s11 * s_star_mu)
    coeffs = expand_in_shifted_basis_fast(product, mu)
    failures = []
    for lam, cv in coeffs.items():
        if is_vert_2_strip(mu, lam):
            continue  # top layer
        d_lam = get_d(lam)
        if d_lam > d_mu + 1:
            failures.append((lam, d_lam, cv))
    return (len(failures) == 0), d_mu, failures, coeffs


if __name__ == "__main__":
    MAX_SIZE = int(sys.argv[1]) if len(sys.argv) > 1 else 8
    print(f"Verifying STRONG per-term shifted-Pieri claim (**) for |mu| <= {MAX_SIZE}")
    print(f"{'mu':>15} {'d_mu':>5} {'time (s)':>10} {'flag':>10}")
    print('-' * 60)
    all_ok = True
    n_cases = 0
    total_time = 0.0
    for N in range(MAX_SIZE + 1):
        for mu in all_partitions_len_le_3(N):
            n_cases += 1
            t0 = time.time()
            ok, d_mu, failures, coeffs = verify_mu(mu)
            dt = time.time() - t0
            total_time += dt
            flag = "OK" if ok else "!!FAIL!!"
            if not ok:
                all_ok = False
            print(f"{str(mu):>15} {d_mu:>5} {dt:>10.2f} {flag:>10}")
            if failures:
                for lam, d, cv in failures:
                    print(f"    FAIL: lambda={lam}, d_lam={d}, d_mu+1={d_mu+1}, coeff={cv}")
    print()
    print(f"Total: {n_cases} cases, {total_time:.2f} s")
    print(f"All strong per-term (**) verified: {all_ok}")
