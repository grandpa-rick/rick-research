"""Day 117 — Compute (u, pi)-degree of ordinary Schur polynomials s_lambda,
and expand S_j in the ordinary Schur basis to see the (u,pi)-degree structure.
"""
from route_v_probe import (
    bt_tables, ds_uyc, divide, substitute_sigma_pi, joint_u_pi_deg,
    fall, det3,
)
from sympy import symbols, expand, Integer, Poly

u, y, c = symbols('u y c')


def V_expr(xs):
    return (xs[0] - xs[1]) * (xs[0] - xs[2]) * (xs[1] - xs[2])


def factorial_schur(mu, xs):
    ks = [mu[col] + (2 - col) for col in range(3)]
    rows = [[fall(xs[i], ks[col]) for col in range(3)] for i in range(3)]
    num = det3(rows)
    V = V_expr(xs)
    q, r = Poly(num, *xs).div(Poly(V, *xs))
    assert r.as_expr() == 0
    return q.as_expr()


def ord_schur(mu, xs):
    ks = [mu[col] + (2 - col) for col in range(3)]
    rows = [[xs[i] ** ks[col] for col in range(3)] for i in range(3)]
    num = det3(rows)
    V = V_expr(xs)
    q, r = Poly(num, *xs).div(Poly(V, *xs))
    assert r.as_expr() == 0
    return q.as_expr()


def all_partitions_len_le_3(N):
    result = []
    for a in range(N, -1, -1):
        for b in range(min(a, N - a), -1, -1):
            for cc in range(min(b, N - a - b), -1, -1):
                if a + b + cc == N:
                    result.append((a, b, cc))
    return result


if __name__ == "__main__":
    xs = (u, y, c)
    print("=== (u, pi)-degrees of ordinary Schur polynomials s_lambda ===")
    print("(joint (u, pi)-degree with sigma = y + c, pi = y*c)")
    print()
    print(f"{'|lambda|':>10} {'lambda':>15} {'(u,pi)-deg':>12}")
    for N in range(0, 7):
        for lam in all_partitions_len_le_3(N):
            s = ord_schur(lam, xs)
            s_sigpi = substitute_sigma_pi(s)
            d = joint_u_pi_deg(s_sigpi)
            print(f"{N:>10} {str(lam):>15} {d:>12}")
    print()

    print("=== (u, pi)-degrees of factorial Schur polynomials s*_mu ===")
    print(f"{'|mu|':>10} {'mu':>15} {'(u,pi)-deg':>12}")
    for N in range(0, 7):
        for mu in all_partitions_len_le_3(N):
            s = factorial_schur(mu, xs)
            s_sigpi = substitute_sigma_pi(s)
            d = joint_u_pi_deg(s_sigpi)
            print(f"{N:>10} {str(mu):>15} {d:>12}")
