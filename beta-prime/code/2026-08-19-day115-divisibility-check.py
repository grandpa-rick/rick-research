"""Day 115: verify the divisibility reduction.

Claim: A_p(b, c, j) is divisible by Pi := (sigma - 2p - 1)^{↓(j-2p)} = (b+c-2p)^{↓(j-2p)}
       as a polynomial in b, c.

Furthermore, given this divisibility + the empirical degree bounds
  (i) deg_b A_p <= j
  (ii) pi-degree of A_p in (pi, sigma) is <= p
then Q := A_p / Pi has:
  (D2) deg_b Q <= 2p (equivalently, sigma-degree of the pi^k coefficient is <= 2p - k)
  (D3) pi-degree Q <= p

Test both divisibility and (D2), (D3) computationally.
"""

from collections import defaultdict
from itertools import combinations

import sympy as sp
from sympy import symbols, expand, Poly, Integer, Rational, factor

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


def divides(A, D, vars_):
    """Check if D divides A. Returns quotient or None."""
    if D == 0:
        return None
    q, r = sp.div(sp.Poly(A, *vars_), sp.Poly(D, *vars_))
    if r.as_expr() == 0:
        return q.as_expr()
    return None


def main():
    J = 12
    print(f"Building shifted-Schur tables & ds_j/V up to j = {J} ...")
    tables = bt(J)
    dsV = dsV_all(J, tables)
    print("done.\n")

    print("=" * 78)
    print(" DIVISIBILITY CHECK: A_p / (b + c - 2p)^{↓(j-2p)}")
    print("=" * 78)

    all_ok = True
    for p in range(1, 6):
        for jj in range(2 * p, min(J + 1, 13)):
            A = extract_A_p(jj, p, dsV)
            if A == 0:
                continue
            # Build Pi
            Pi = Integer(1)
            for i in range(jj - 2 * p):
                Pi *= (b + c - 2 * p - i)
            Pi = sp.expand(Pi)
            # Divide
            Q = divides(A, Pi, (b, c))
            if Q is None:
                print(f"  p = {p}, j = {jj}: NOT DIVISIBLE — FAIL")
                all_ok = False
                continue
            # Check Q degrees
            db = sp.Poly(Q, b, c).degree(b) if Q != 0 else -1
            dc = sp.Poly(Q, b, c).degree(c) if Q != 0 else -1
            dt = sp.Poly(Q, b, c).total_degree() if Q != 0 else -1
            Q_ps = to_pi_sigma_shifted(Q)
            deg_pi = sp.Poly(Q_ps, pi_v, sig).degree(pi_v) if Q_ps != 0 else -1
            deg_sig = sp.Poly(Q_ps, pi_v, sig).degree(sig) if Q_ps != 0 else -1
            check_b = "OK" if db <= 2 * p else "FAIL"
            check_pi = "OK" if deg_pi <= p else "FAIL"
            check_t = "OK" if dt <= 3 * p else "FAIL"
            if check_b == "FAIL" or check_pi == "FAIL" or check_t == "FAIL":
                all_ok = False
            print(f"  p = {p}, j = {jj:2d}: Q has deg_b={db} [<={2*p} {check_b}], "
                  f"deg_pi={deg_pi} [<={p} {check_pi}], "
                  f"total_deg={dt} [<={3*p} {check_t}], deg_sig={deg_sig}")

            # More: check the (k, d) support of Q_ps: does deg_sigma of pi^k coef <= 2p - k?
            Q_poly = sp.Poly(Q_ps, pi_v, sig)
            bad = []
            for k in range(deg_pi + 1):
                # coefficient of pi^k as polynomial in sigma
                coef_k = Integer(0)
                for monom, cf in Q_poly.terms():
                    if monom[0] == k:
                        coef_k += cf * sig ** monom[1]
                coef_k = sp.expand(coef_k)
                d = sp.Poly(coef_k, sig).degree() if coef_k != 0 else -1
                if d > 2 * p - k:
                    bad.append((k, d, 2*p - k))
            if bad:
                print(f"        SIGMA-DEG VIOLATIONS: {bad}")
                all_ok = False

    print(f"\n{'=' * 78}")
    print(f"ALL DIVISIBILITY + DEGREE BOUNDS: {'PASS' if all_ok else 'FAIL'}")
    print(f"{'=' * 78}")

    # Bonus: check the degree bounds ON A_p that our reduction assumes.
    print("\n" + "=" * 78)
    print(" INPUT DEGREE BOUND VERIFICATION: deg_b A_p <= j, pi-degree A_p <= p")
    print("=" * 78)

    all_deg_ok = True
    for p in range(1, 6):
        for jj in range(2 * p, min(J + 1, 13)):
            A = extract_A_p(jj, p, dsV)
            if A == 0:
                continue
            db = sp.Poly(A, b, c).degree(b) if A != 0 else -1
            dc = sp.Poly(A, b, c).degree(c) if A != 0 else -1
            dt = sp.Poly(A, b, c).total_degree() if A != 0 else -1
            A_ps = to_pi_sigma_shifted(A)
            deg_pi = sp.Poly(A_ps, pi_v, sig).degree(pi_v) if A_ps != 0 else -1
            check_b = "OK" if db <= jj else "FAIL"
            check_pi = "OK" if deg_pi <= p else "FAIL"
            check_t = "OK" if dt <= jj + p else "FAIL"
            if check_b == "FAIL" or check_pi == "FAIL" or check_t == "FAIL":
                all_deg_ok = False
            print(f"  p = {p}, j = {jj:2d}: A has deg_b={db} [<={jj} {check_b}], "
                  f"deg_pi={deg_pi} [<={p} {check_pi}], "
                  f"total={dt} [<={jj + p} {check_t}]")

    print(f"\nDEGREE BOUNDS ON A_p: {'PASS' if all_deg_ok else 'FAIL'}")


if __name__ == "__main__":
    main()
