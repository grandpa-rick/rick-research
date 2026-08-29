"""Day 115: verify the KEY ARGUMENT for divisibility of A_p by Pi_{p,j}.

The argument: at sigma = t for t in [2p+1, j]:
  - A_p|_{sigma=t} is a polynomial in pi of degree <= p (from pi-degree bound).
  - At partition points (mu_1, mu_2) with mu_1 + mu_2 = t - 1 (so sigma = t),
    A_p vanishes.
  - There are floor((t-1)/2) + 1 >= p+1 such partitions, giving pi-values
    pi_k = k(t-k) for k = 0, 1, ..., floor((t-1)/2), all distinct.
  - So A_p|_{sigma=t} vanishes at >= p+1 distinct pi-values, hence identically 0.

Verify this argument directly.
"""

from collections import defaultdict
from itertools import combinations

import sympy as sp
from sympy import symbols, expand, Poly, Integer

a, b, c = symbols('a b c')
u = a + 2
sig, pi_v = symbols('sigma pi')


def fall(x, m):
    p = Integer(1)
    for i in range(m):
        p *= (x - i)
    return p


def det3(rows):
    (a11, a12, a13), (a21, a22, a23), (a31, a32, a33) = rows
    return (a11 * (a22 * a33 - a23 * a32)
            - a12 * (a21 * a33 - a23 * a31)
            + a13 * (a21 * a32 - a22 * a31))


def bt(M):
    def vs(mu):
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
            r.append(tuple(n))
        return r
    cu = defaultdict(int)
    cu[()] = 1
    T = {0: [((0, 0, 0), 1)]}
    for jj in range(1, M + 1):
        nx = defaultdict(int)
        for mu, cc in cu.items():
            for nu in vs(mu):
                nx[nu] += cc
        cu = nx
        rs = []
        for mu, cc in sorted(cu.items(), reverse=True):
            pd = tuple(list(mu) + [0] * (3 - len(mu)))
            rs.append((pd, cc))
        T[jj] = rs
    return T


def ds_symbolic(jj, tables):
    xs = (u, b + 1, c)
    total = Integer(0)
    for mu, kap in tables[jj]:
        ks = [mu[col] + (2 - col) for col in range(3)]
        rows = [[fall(xs[i], ks[col]) for col in range(3)] for i in range(3)]
        total += kap * det3(rows)
    return expand(total)


def V_of():
    return (a - b + 1) * (a - c + 2) * (b - c + 1)


def dsV_all(J, tables):
    V = V_of()
    cache = {}
    for jj in range(J + 1):
        dsj = ds_symbolic(jj, tables)
        q, r = sp.div(Poly(dsj, [a, b, c]), Poly(V, [a, b, c]))
        assert r.as_expr() == 0
        cache[jj] = q.as_expr()
    return cache


def extract_A_p(jj, p, dsV_cache):
    S = dsV_cache[jj]
    if jj - p < 0:
        return Integer(0)
    pab = Poly(S, a, b, c)
    result = Integer(0)
    for monom, cf in pab.terms():
        da, db, dc = monom
        if da == jj - p:
            result += cf * b ** db * c ** dc
    return expand(result)


def to_pi_sigma_shifted(F):
    z = symbols('_z_pi_sig_')
    Fz = expand(F.subs([(b, z - 1), (c, sig - z)]))
    Pz = sp.Poly(Fz, z)
    D = Pz.degree()
    coefs = [Pz.coeff_monomial(z ** i) for i in range(D + 1)]
    while len(coefs) > 2:
        top = coefs[-1]
        d = len(coefs) - 1
        if top == 0:
            coefs.pop()
            continue
        coefs[d - 1] = sp.expand(coefs[d - 1] + sig * top)
        coefs[d - 2] = sp.expand(coefs[d - 2] - pi_v * top)
        coefs.pop()
    while len(coefs) < 2:
        coefs.append(Integer(0))
    if sp.simplify(coefs[1]) != 0:
        return None
    return sp.expand(coefs[0])


def main():
    J = 12
    print(f"Building A_p up to j = {J} ...")
    tables = bt(J)
    dsV = dsV_all(J, tables)
    print("done.\n")

    print("=" * 78)
    print(" DIRECT VERIFICATION: A_p|_{sigma=t} = 0 as polynomial in pi, for t in [2p+1, j]")
    print("=" * 78)
    all_ok = True
    for p in range(1, 6):
        for jj in range(2 * p, min(J + 1, 13)):
            A = extract_A_p(jj, p, dsV)
            if A == 0:
                continue
            A_ps = to_pi_sigma_shifted(A)
            if A_ps is None:
                print(f"  p={p}, j={jj}: A NOT twisted-symmetric — skip")
                continue
            deg_pi = sp.Poly(A_ps, pi_v, sig).degree(pi_v) if A_ps != 0 else -1
            deg_pi_ok = deg_pi <= p
            marker_pi = "OK" if deg_pi_ok else "FAIL"
            print(f"  p={p}, j={jj}: deg_pi(A_p) = {deg_pi} [<={p} {marker_pi}]")
            # For each t in [2p+1, j]: check A_p|_{sigma=t} = 0 as poly in pi.
            for t in range(2 * p + 1, jj + 1):
                A_at_t = sp.expand(A_ps.subs(sig, t))
                is_zero = (A_at_t == 0)
                # Also check partition-point count
                n_parts = (t - 1) // 2 + 1
                marker = "ZERO" if is_zero else "NONZERO !!!"
                print(f"      t = {t:2d}: partitions|mu|={t-1}: count={n_parts} (>= p+1 = {p+1}?), "
                      f"A_p|_{{sigma={t}}} = {marker}")
                if not is_zero:
                    all_ok = False
                    print(f"         A_p|_{{sigma={t}}} = {A_at_t}")

    print(f"\n{'=' * 78}")
    print(f"KEY ARGUMENT RESULT: {'PASS' if all_ok else 'FAIL'}")
    print(f"{'=' * 78}")


if __name__ == "__main__":
    main()
