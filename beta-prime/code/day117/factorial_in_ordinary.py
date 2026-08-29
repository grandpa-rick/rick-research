"""Day 117 — Expand s^*_mu in the ordinary Schur basis, and check
that all appearing s_lambda satisfy (u,pi)-degree(s_lambda) <= (u,pi)-degree(s_mu).

If TRUE for all mu, then deg_{u,pi}(s^*_mu) <= deg_{u,pi}(s_mu), and
S_j = sum K_{mu', (2^j)} s^*_mu = sum_lambda (sum_mu K_{mu', (2^j)} coeff) s_lambda,
and all s_lambda appearing have deg_{u,pi} <= max_mu appearing deg_{u,pi}(s_mu),
which equals ... hmm not quite the bound we want.

Actually the SUM formula: sum_mu K_{mu', (2^j)} s_mu = e_2^j (proved).
So the TOP polynomial-degree part of S_j is e_2^j. But e_2^j has (u,pi)-deg = j.
The LOWER polynomial-degree parts of S_j come from lower parts of s^*_mu's.
If those lower parts also have (u,pi)-deg <= j, we're done.

Let's test:
  (a) does s^*_mu = sum_lambda c^mu_lambda s_lambda with (u,pi)-deg(s_lambda) <= (u,pi)-deg(s_mu)?
  (b) how does the sum sum_mu K_{mu', (2^j)} s^*_mu decompose in ordinary Schur basis?
"""
from ordinary_schur_deg import (
    ord_schur, factorial_schur, all_partitions_len_le_3, V_expr,
)
from route_v_probe import (
    substitute_sigma_pi, joint_u_pi_deg, fall, det3, bt_tables,
)
from sympy import symbols, expand, Integer, Poly

u, y, c = symbols('u y c')


def expand_in_ordinary_schur(f, xs, max_size):
    """Given a symmetric polynomial f(u, y, c), expand in ordinary Schur basis
    {s_lambda: |lambda| <= max_size, ell(lambda) <= 3}."""
    basis = {}
    for N in range(max_size + 1):
        for lam in all_partitions_len_le_3(N):
            basis[lam] = expand(ord_schur(lam, xs))
    all_monomials = set()
    for f_expr in list(basis.values()) + [f]:
        if f_expr == 0:
            continue
        p = Poly(f_expr, u, y, c)
        for mono, _ in p.terms():
            all_monomials.add(mono)
    all_monomials = sorted(all_monomials)
    from sympy import zeros
    key_list = sorted(basis.keys(), key=lambda lam: (sum(lam), lam), reverse=True)
    M = zeros(len(all_monomials), len(key_list))
    b_vec = zeros(len(all_monomials), 1)
    for i, mono in enumerate(all_monomials):
        for j_, mu in enumerate(key_list):
            p = Poly(basis[mu], u, y, c)
            M[i, j_] = p.coeff_monomial(mono)
        p = Poly(f, u, y, c)
        b_vec[i, 0] = p.coeff_monomial(mono)
    sol = M.solve(b_vec)
    coeffs = {mu: sol[j, 0] for j, mu in enumerate(key_list) if sol[j, 0] != 0}
    return coeffs


def upi_deg(mu, xs):
    s = ord_schur(mu, xs)
    return joint_u_pi_deg(substitute_sigma_pi(s))


if __name__ == "__main__":
    xs = (u, y, c)
    # First: test claim (a) for small mu.
    print("(a) Testing: s^*_mu = sum_lambda c^mu_lambda s_lambda with (u,pi)-deg(s_lambda) <= (u,pi)-deg(s_mu)")
    print()
    print(f"{'mu':>15} {'d_mu':>5} {'lambda':>15} {'d_lam':>5} {'c^mu_lambda':>12} {'flag':>5}")
    print('-' * 60)
    all_ok = True
    max_size_to_test = 6
    for N in range(max_size_to_test + 1):
        for mu in all_partitions_len_le_3(N):
            if mu == (0, 0, 0):
                continue
            s_star = factorial_schur(mu, xs)
            coeffs = expand_in_ordinary_schur(s_star, xs, max_size=N)
            d_mu = upi_deg(mu, xs)
            for lam, cval in sorted(coeffs.items(), key=lambda kv: (sum(kv[0]), kv[0]), reverse=True):
                d_lam = upi_deg(lam, xs)
                ok = "OK" if d_lam <= d_mu else "FAIL"
                if d_lam > d_mu:
                    all_ok = False
                print(f"{str(mu):>15} {d_mu:>5} {str(lam):>15} {d_lam:>5} {str(cval):>12} {ok:>5}")
    print()
    print(f"All (a) OK: {all_ok}")
    print()

    # (b) Decompose S_j = sum K_{mu', (2^j)} s^*_mu in ordinary Schur basis and check.
    print()
    print("(b) Decomposing S_j in ordinary Schur basis:")
    T = bt_tables(4)
    for j in range(1, 5):
        Sj = Integer(0)
        for mu, kap in T[j]:
            Sj += kap * factorial_schur(mu, xs)
        Sj = expand(Sj)
        coeffs = expand_in_ordinary_schur(Sj, xs, max_size=2 * j)
        print(f"j={j}: S_{j} in ordinary Schur basis:")
        max_d = 0
        for lam, cval in sorted(coeffs.items(), key=lambda kv: (sum(kv[0]), kv[0]), reverse=True):
            d_lam = upi_deg(lam, xs)
            print(f"    {str(cval):>10} * s_{lam}   (d={d_lam})")
            max_d = max(max_d, d_lam)
        print(f"    max d_lambda appearing: {max_d}, bound j = {j}")
        print()
