"""Experiment 2: Numerator formula N_mu(j, t) via (A, B) reduction.

For 3-part mu = (mu_1, mu_2, mu_3), let k = (mu_1+2, mu_2+1, mu_3).
Weyl formula:
  s*_mu(u, y, c) = det([x_i]_{k_l}) / V(u, y, c)
with V = (u-y)(u-c)(y-c).

Under u = t, y+c = j, yc = t:
  (u-y)(u-c) = t^2 - tj + t = t(t - j + 1)
  V / (y - c) = t(t - j + 1)

Expand det along row 1:
  det = [u]_{k_1} M_{k_2,k_3} - [u]_{k_2} M_{k_1,k_3} + [u]_{k_3} M_{k_1,k_2}
where M_{a,b} = [y]_a [c]_b - [y]_b [c]_a = W_{a,b}(t) (y - c).

Hence
  s*_mu specialized = N_mu(j, t) / (t (t - j + 1))
where
  N_mu(j, t) = [t]_{k_1} W_{k_2,k_3} - [t]_{k_2} W_{k_1,k_3} + [t]_{k_3} W_{k_1,k_2}.

Verify against direct sympy computation of s*_mu for several mu of size <= 8.
"""

import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day117')
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day119')

import sympy as sp
from sympy import symbols, expand, Integer, Poly, simplify, factor

from ab_recursion import build_AB

j, t = symbols('j t')
u, y, c = symbols('u y c')
sig, pi_sym = symbols('sigma pi')


def fall_j(x, m):
    """Falling factorial x*(x-1)*...*(x-m+1)."""
    p = Integer(1)
    for i in range(m):
        p *= (x - i)
    return p


def W_ab(A, B, a, b):
    return expand(A[a] * B[b] - A[b] * B[a])


def N_mu(mu, A, B):
    """N_mu(j, t) via the (A,B) closed form.
    k = (mu_1 + 2, mu_2 + 1, mu_3).
    """
    mu_p = list(mu) + [0] * (3 - len(mu))
    k1 = mu_p[0] + 2
    k2 = mu_p[1] + 1
    k3 = mu_p[2]
    N = (fall_j(t, k1) * W_ab(A, B, k2, k3)
         - fall_j(t, k2) * W_ab(A, B, k1, k3)
         + fall_j(t, k3) * W_ab(A, B, k1, k2))
    return expand(N)


def F_mu(mu, A, B):
    """F_mu(j, t) := s*_mu specialized = N_mu / (t (t - j + 1))."""
    N = N_mu(mu, A, B)
    denom = t * (t - j + 1)
    # Divide symbolically in Q(j)[t]
    q, r = sp.div(sp.Poly(N, t), sp.Poly(denom, t))
    if expand(r.as_expr()) != 0:
        # try full poly ring
        q2, r2 = sp.div(sp.Poly(N, j, t), sp.Poly(denom, j, t))
        if expand(r2.as_expr()) != 0:
            raise ValueError(f"N_mu not divisible by t(t-j+1) for mu={mu}: N={N}, remainder={expand(r.as_expr())}")
        return expand(q2.as_expr())
    return expand(q.as_expr())


# --- Direct computation (for verification) ---

def det3(rows):
    (a11, a12, a13), (a21, a22, a23), (a31, a32, a33) = rows
    return (a11 * (a22 * a33 - a23 * a32)
            - a12 * (a21 * a33 - a23 * a31)
            + a13 * (a21 * a32 - a22 * a31))


def fall(x, m):
    p = Integer(1)
    for i in range(m):
        p *= (x - i)
    return p


def s_star_mu_direct(mu):
    """Direct: s*_mu(u, y, c) = det([x_i]_{k_l}) / V(u,y,c)."""
    xs = (u, y, c)
    mu_p = list(mu) + [0] * (3 - len(mu))
    ks = [mu_p[col] + (2 - col) for col in range(3)]
    rows = [[fall(xs[i], ks[col]) for col in range(3)] for i in range(3)]
    numer = det3(rows)
    V = (u - y) * (u - c) * (y - c)
    q, r = sp.div(sp.Poly(expand(numer), u, y, c), sp.Poly(expand(V), u, y, c))
    if r.as_expr() != 0:
        raise ValueError("bad division")
    return expand(q.as_expr())


def F_mu_direct(mu):
    """Directly compute s*_mu(u=t, y+c=j, yc=t) via substitute_sigma_pi."""
    from route_v_probe import substitute_sigma_pi
    f = s_star_mu_direct(mu)
    fs = substitute_sigma_pi(f)  # now in u, sig, pi
    # substitute u=t, sig=j, pi=t
    result = expand(fs.subs({u: t, sig: j, pi_sym: t}))
    return result


def verify_mu(mu, A, B):
    F_AB = F_mu(mu, A, B)
    F_dir = F_mu_direct(mu)
    diff = expand(F_AB - F_dir)
    return diff == 0, F_AB, F_dir


def main():
    A, B = build_AB(20)

    # Test partitions
    test_mus = [
        (3, 2, 1),
        (4, 2, 1),
        (3, 3, 2),
        (2, 1, 0),
        (3, 1, 0),
        (4, 3, 3),
        (5, 3, 2),
        (5, 4, 1),
        (5, 5, 0),
        # spine shapes (2l+1, l+1+m, l-m) for l=2: j=5
        (5, 3, 2),  # l=2, m=0
        (5, 4, 1),  # l=2, m=1
        (5, 5, 0),  # l=2, m=2
        # spine for l=3, j=7
        (7, 4, 3),  # m=0
        (7, 5, 2),  # m=1
        (7, 6, 1),  # m=2
        (7, 7, 0),  # m=3
    ]

    print("=" * 70)
    print("Verify N_mu / (t(t-j+1)) = direct s*_mu specialized")
    print("=" * 70)
    all_ok = True
    for mu in test_mus:
        try:
            ok, FAB, Fdir = verify_mu(mu, A, B)
            marker = "OK" if ok else "!!! MISMATCH"
            if not ok:
                all_ok = False
                print(f"  mu={mu}: {marker}")
                print(f"    F_AB  = {FAB}")
                print(f"    F_dir = {Fdir}")
            else:
                # print short summary
                pAB = Poly(FAB, t, j)
                terms = list(pAB.terms())
                print(f"  mu={mu}: OK  ({len(terms)} monomials, deg_t={Poly(FAB, t).degree()})")
        except Exception as e:
            all_ok = False
            print(f"  mu={mu}: ERROR {e}")

    print(f"\nAll match: {'YES' if all_ok else 'NO'}")

    print()
    print("=" * 70)
    print("Sample N_mu closed forms:")
    print("=" * 70)
    for mu in [(3, 2, 1), (4, 2, 1), (5, 3, 2)]:
        N = N_mu(mu, A, B)
        F = F_mu(mu, A, B)
        print(f"\nmu = {mu}, k = ({mu[0]+2}, {mu[1]+1}, {mu[2]})")
        print(f"  N_mu(j,t) has deg_t = {Poly(N, t).degree()}, deg_j = {Poly(N, j).degree()}")
        print(f"  F_mu(j,t) has deg_t = {Poly(F, t).degree()}, deg_j = {Poly(F, j).degree()}")


if __name__ == "__main__":
    main()
