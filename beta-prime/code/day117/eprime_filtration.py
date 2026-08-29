"""Day 117 — Test whether the shifted-Pieri correction operator E' preserves
the (u,pi)-filtration F^k.

E'(s^*_mu) := s^*_{(1,1)} * s^*_mu - E(s^*_mu),
where E(s^*_mu) = sum_{lambda: lambda/mu vert 2-strip} s^*_lambda.

Claim to test: (u,pi)-deg(E'(s^*_mu)) <= d_mu = (u,pi)-deg(s^*_mu).

If TRUE for all mu with |mu| <= max_size, this gives strong evidence for StructB.
"""
from ordinary_schur_deg import factorial_schur, all_partitions_len_le_3
from route_v_probe import substitute_sigma_pi, joint_u_pi_deg
from decompose_s11_pow import expand_in_shifted_basis
from sympy import symbols, expand, Integer
from itertools import combinations

u, y, c = symbols('u y c')


def upi_deg(expr):
    return joint_u_pi_deg(substitute_sigma_pi(expr))


def vert_2_strips_from(mu):
    """Return all lambda such that lambda/mu is a vertical 2-strip
    (i.e., lambda \\supset mu with 2 boxes added in DIFFERENT rows).
    Restrict ell(lambda) <= 3."""
    L = len(mu) + 2
    bb = list(mu) + [0] * (L - len(mu))
    r = []
    for pp in combinations(range(L), 2):
        n = bb.copy()
        for i in pp:
            n[i] += 1
        ok = True
        for i in range(L - 1):
            if n[i] < n[i + 1]:
                ok = False
                break
        if not ok:
            continue
        while n and n[-1] == 0:
            n.pop()
        if len(n) > 3:
            continue
        # Pad to length 3
        pd = tuple(list(n) + [0] * (3 - len(n)))
        r.append(pd)
    return r


if __name__ == "__main__":
    xs = (u, y, c)
    s11 = factorial_schur((1, 1, 0), xs)

    max_size = 5
    print(f"Testing: (u,pi)-deg(E'(s^*_mu)) <= d_mu?")
    print()
    print(f"{'mu':>15} {'d_mu':>5} {'d(E prime)':>12} {'flag':>10}")
    print('-' * 60)
    all_ok = True
    for N in range(max_size + 1):
        for mu in all_partitions_len_le_3(N):
            s_star_mu = factorial_schur(mu, xs)
            d_mu = upi_deg(s_star_mu)
            product = expand(s11 * s_star_mu)
            # E(s^*_mu) = sum over vert-2-strip lambda of s^*_lambda
            e_part = Integer(0)
            for lam in vert_2_strips_from(mu):
                e_part += factorial_schur(lam, xs)
            e_part = expand(e_part)
            # E'(s^*_mu) = product - e_part
            e_prime = expand(product - e_part)
            d_prime = upi_deg(e_prime) if e_prime != 0 else 0
            flag = "OK" if d_prime <= d_mu else "FAIL"
            if d_prime > d_mu:
                all_ok = False
            print(f"{str(mu):>15} {d_mu:>5} {d_prime:>12} {flag:>10}")
    print()
    print(f"All OK: {all_ok}")
