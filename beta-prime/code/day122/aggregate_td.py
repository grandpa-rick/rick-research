"""Experiment 3: [t^d] S_j as polynomial in s := y+c, via (A, B) machinery.

Key convention: in the AB recursion, the symbol `j` is actually `y + c`,
which Rick has been calling `s` since Day 120. The `j` in Kostka's
K_{mu', (2^j)} is the FIXED integer determined by |mu| = 2j.

So we build A_a(s, t), B_a(s, t), form F_mu(s, t), and Kostka's are
fixed integers. Then S_{j_int}(s, t) is a polynomial in s, t with
integer coefficients, and [t^d] S_{j_int} is a polynomial in s.

The Day 120 discovery: [t^d] S_{j_int}(s) = 0 as a polynomial in s
for j_int + 1 <= d <= d_max(j_int).

Compute for j = 3..7, print each [t^d] S_j(s) explicitly.
"""

import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day119')
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day122')

import sympy as sp
from sympy import symbols, expand, Integer, Poly, factor

from kostka import kostka_mu_prime_2j, d_mu, all_mu_3parts

# NEW convention: `s` plays the role of `y + c` in the (A,B) recursion.
s, t = symbols('s t')


def build_AB_in_s(N=20):
    """Build A_a(s, t), B_a(s, t) using s in place of j."""
    A = [Integer(0)]
    B = [Integer(1)]
    for a in range(N):
        A_next = expand((s - a) * A[a] + B[a])
        B_next = expand(-t * A[a] - a * B[a])
        A.append(A_next)
        B.append(B_next)
    return A, B


def fall_t(m):
    """Falling factorial t*(t-1)*...*(t-m+1)."""
    p = Integer(1)
    for i in range(m):
        p *= (t - i)
    return p


def W_ab(A, B, a, b):
    return expand(A[a] * B[b] - A[b] * B[a])


def N_mu(mu, A, B):
    mu_p = list(mu) + [0] * (3 - len(mu))
    k1 = mu_p[0] + 2
    k2 = mu_p[1] + 1
    k3 = mu_p[2]
    N = (fall_t(k1) * W_ab(A, B, k2, k3)
         - fall_t(k2) * W_ab(A, B, k1, k3)
         + fall_t(k3) * W_ab(A, B, k1, k2))
    return expand(N)


def F_mu(mu, A, B):
    """F_mu(s, t) := N_mu / (t (t - s + 1))."""
    N = N_mu(mu, A, B)
    denom = t * (t - s + 1)
    # divide in Q(s)[t]
    q, r = sp.div(sp.Poly(N, t), sp.Poly(denom, t))
    if expand(r.as_expr()) != 0:
        q2, r2 = sp.div(sp.Poly(N, s, t), sp.Poly(denom, s, t))
        if expand(r2.as_expr()) != 0:
            raise ValueError(f"N_mu not divisible for mu={mu}: rem={expand(r.as_expr())}")
        return expand(q2.as_expr())
    return expand(q.as_expr())


def d_max(jval):
    return jval + jval // 2


def get_t_coefficient(expr, d):
    """Return [t^d] expr as a polynomial in s."""
    p = Poly(expr, t, s)
    out = Integer(0)
    for (dt, ds), coef in p.terms():
        if dt == d:
            out += coef * s**ds
    return expand(out)


def compute_Sj(jval, A, B, verbose=False):
    """Compute S_j(s, t) = sum_mu K_mu * F_mu(s, t) for fixed integer jval."""
    twoj = 2 * jval
    contributions = []
    S = Integer(0)
    for mu in all_mu_3parts(twoj):
        K = kostka_mu_prime_2j(mu)
        if K == 0:
            continue
        F = F_mu(mu, A, B)  # in s, t
        contribution = expand(K * F)
        S = expand(S + contribution)
        contributions.append((mu, K, F))
    return S, contributions


def main():
    A, B = build_AB_in_s(20)

    print("Sanity: verify F_mu convention by evaluating [t^d_mu] F_mu at s=j for spine")
    print("(should reproduce Day 121 result (-1)^m delta_{m,l} for mu=(2l+1, l+1+m, l-m))")
    for l in [1, 2, 3]:
        j_int = 2 * l + 1
        for m in range(l + 1):
            mu = (2*l + 1, l + 1 + m, l - m)
            d = d_mu(mu)
            F = F_mu(mu, A, B)
            cd = get_t_coefficient(F, d)
            val_at_j = expand(cd.subs(s, j_int))
            expected = (-1) ** m if m == l else 0
            marker = "OK" if val_at_j == expected else "!!! MISMATCH"
            print(f"  l={l}, m={m}, mu={mu}: [t^{d}] F_mu|s={j_int} = {val_at_j} (exp {expected}) {marker}")
    print()

    for jval in [3, 4, 5, 6, 7]:
        print("=" * 70)
        print(f"j = {jval}, d_max = {d_max(jval)}")
        print("=" * 70)
        S, contribs = compute_Sj(jval, A, B)
        # deg_t
        max_dt = Poly(S, t).degree()
        print(f"  deg_t S_j = {max_dt} (target: <= {jval})")

        for d in range(jval + 1, max(max_dt, d_max(jval)) + 1):
            coef_d = get_t_coefficient(S, d)
            status = "OK" if coef_d == 0 else "!!! NONZERO"
            print(f"  [t^{d}] S_j(s) = {coef_d}  {status}")

        # Also print [t^d] S_j FACTORED for d <= j (informational — these are nonzero)
        if jval <= 5:
            print(f"\n  Informational: [t^d] S_j(s) for d <= j (should be nonzero):")
            for d in range(0, jval + 1):
                coef_d = get_t_coefficient(S, d)
                fac = factor(coef_d) if coef_d != 0 else 0
                print(f"    [t^{d}] S_j(s) = {coef_d}     = {fac}")

        # Coupling breakdown for j <= 5
        if jval <= 5:
            print(f"\n  Per-mu contributions to [t^d] S_j for d > j:")
            for d in range(jval + 1, d_max(jval) + 1):
                nonzero = []
                for mu, K, F in contribs:
                    cd = get_t_coefficient(F, d)
                    if cd != 0:
                        nonzero.append((mu, K, cd))
                subtotal = sum(K * cd for mu, K, cd in nonzero)
                subtotal = expand(subtotal)
                print(f"    d={d}: {len(nonzero)} mu contribute, sum = {subtotal}")
                for mu, K, cd in nonzero:
                    dmu = d_mu(mu)
                    delta = dmu - d
                    parity = (mu[1] - mu[2]) % 2
                    print(f"      mu={mu} K={K} d_mu={dmu} delta={delta} parity={parity}: [t^{d}]F_mu = {cd}")
        print()


if __name__ == "__main__":
    main()
