"""Investigate the e-basis expansion of individual s^*_mu and of e_2^j sum.

For the lift theorem to give (StructB), we want:
    sum_{|mu|=2j, ell<=3} K_{mu', (2^j)} s^*_mu   has e-wdeg <= j,
where e-wdeg(e_1^i1 e_2^i2 e_3^i3) = i_1 + i_2 + 2 i_3.

We know:
  (1) Top-degree part of sum = e_2^j (proved from Kostka).
  (2) e_2^j has e-wdeg exactly j (just j copies of e_2).

So the claim is that all LOWER-ORDER corrections also fit in e-wdeg <= j.

This script:
  A. Computes s^*_mu's e-basis expansion for each mu appearing (individually).
  B. Shows individual s^*_mu can violate the bound.
  C. Verifies cancellation across the sum brings us back to e-wdeg <= j.
  D. Investigates the structure of shifted-Schur -> ordinary-Schur triangular change.
"""

from collections import defaultdict
from itertools import combinations

import sympy as sp
from sympy import symbols, expand, Poly, Integer


u_var, y_var, c = symbols('u y c')
e1_v, e2_v, e3_v = symbols('e1 e2 e3')


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


def V_uyc():
    return (u_var - y_var) * (u_var - c) * (y_var - c)


def factorial_schur(mu):
    """s^*_mu(u, y, c). mu a 3-tuple."""
    xs = (u_var, y_var, c)
    ks = [mu[col] + (2 - col) for col in range(3)]
    rows = [[fall(xs[i], ks[col]) for col in range(3)] for i in range(3)]
    num = det3(rows)
    V = V_uyc()
    q, r = sp.div(Poly(num, u_var, y_var, c), Poly(V, u_var, y_var, c))
    assert r.as_expr() == 0
    return q.as_expr()


def ord_schur(mu):
    n = 3
    xs = (u_var, y_var, c)
    rows = [[xs[i]**(mu[col] + n - 1 - col) for col in range(n)]
            for i in range(n)]
    num = det3(rows)
    V = V_uyc()
    q, r = sp.div(Poly(num, u_var, y_var, c), Poly(V, u_var, y_var, c))
    assert r.as_expr() == 0
    return q.as_expr()


def to_elem_uyc(F):
    """Rewrite symmetric F(u, y, c) in (e1, e2, e3)."""
    F = expand(F)
    result = Integer(0)
    while True:
        F = expand(F)
        P = Poly(F, u_var, y_var, c)
        if P.total_degree() < 0 or P.as_expr() == 0:
            break
        terms = sorted(P.terms(), reverse=True)
        (dm, cf) = terms[0]
        du, dy, dc = dm
        if not (du >= dy >= dc):
            return None
        result += cf * e1_v ** (du - dy) * e2_v ** (dy - dc) * e3_v ** dc
        sub = cf * (u_var + y_var + c) ** (du - dy) * (
            u_var * y_var + u_var * c + y_var * c) ** (dy - dc) * (
            u_var * y_var * c) ** dc
        F = expand(F - sub)
    return result


def ewdeg(F_e):
    """Max e-wdeg (weights 1, 1, 2) of poly in (e1, e2, e3)."""
    if F_e == 0:
        return -1
    P = Poly(F_e, e1_v, e2_v, e3_v)
    m = -1
    for mo, cf in P.terms():
        if cf == 0:
            continue
        i1, i2, i3 = mo
        w = i1 + i2 + 2 * i3
        if w > m:
            m = w
    return m


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


def s_star_to_s(mu):
    """Expand s^*_mu in ORDINARY Schurs (in 3 vars) by leading-monomial peel.
    Returns dict lam -> coefficient.
    """
    F = factorial_schur(mu)
    expansion = {}
    while True:
        F = expand(F)
        if F == 0:
            break
        P = Poly(F, u_var, y_var, c)
        if P.total_degree() < 0:
            break
        leading = sorted(P.terms(), reverse=True)[0]
        monom, cf = leading
        lam = tuple(monom)
        if not (lam[0] >= lam[1] >= lam[2]):
            return None
        s_lam = ord_schur(lam)
        expansion[lam] = cf
        F = expand(F - cf * s_lam)
    return expansion


def s_to_elem(lam):
    """Expand ordinary Schur s_lam(u,y,c) in (e_1, e_2, e_3)."""
    return to_elem_uyc(ord_schur(lam))


def main():
    J_MAX = 5
    tables = bt(J_MAX)

    print("=" * 78)
    print("PART A: Per-term s^*_mu e-wdeg for each mu in bt(j) tables (j <= 5)")
    print("=" * 78)
    for jj in range(J_MAX + 1):
        print(f"\n  j = {jj}:")
        for mu, kap in tables[jj]:
            s_star = factorial_schur(mu)
            e_expr = to_elem_uyc(s_star)
            w = ewdeg(e_expr)
            over_j = "VIOLATES" if w > jj else "ok"
            print(f"    mu={mu} kap={kap}: e-wdeg s^*_mu = {w}  [target <= {jj}: {over_j}]")

    print("\n" + "=" * 78)
    print("PART B: Ordinary Schur s_lam e-wdeg (should be exact for ordinary Schurs).")
    print("=" * 78)
    for jj in range(J_MAX + 1):
        print(f"\n  Looking at ordinary Schurs s_lam for |lam| <= 2j={2*jj}, ell<=3.")
        # For each mu in bt(j), also test ORDINARY s_mu
        seen = set()
        for mu, kap in tables[jj]:
            if mu in seen:
                continue
            seen.add(mu)
            e_expr = s_to_elem(mu)
            w = ewdeg(e_expr)
            # For s_mu of total degree d = |mu|, the e-wdeg with weights (1,1,2):
            # If lam has 3 parts (a,b,c), s_lam has an e_3^c factor... actually
            # s_lam in 3 variables: s_lam = e_1^? ... let's just print.
            print(f"    lam={mu}: ordinary s_lam e-wdeg = {w}   (|lam|={sum(mu)})")

    print("\n" + "=" * 78)
    print("PART C: The lower-triangular change from s^*_mu to s_lam.")
    print("        We express each s^*_mu = sum_lam c^mu_lam s_lam (|lam| <= |mu|).")
    print("=" * 78)
    for jj in range(J_MAX + 1):
        print(f"\n  j = {jj}:")
        for mu, kap in tables[jj]:
            exp = s_star_to_s(mu)
            print(f"    s^*_{mu}: {sorted(exp.items(), reverse=True)}")

    print("\n" + "=" * 78)
    print("PART D: Structural check — does s_lam(u, y, c) always have e-wdeg <= |lam|/2 + ...?")
    print("        We check: for lam with |lam| <= 2j and ell<=3,")
    print("        what is the e-wdeg of s_lam?")
    print("        For lam = (a, b, c) descending: leading e-monomial is")
    print("        e_1^{a-b} e_2^{b-c} e_3^c, with wdeg = (a-b) + (b-c) + 2c = a + c.")
    print("        Hmm. So e-wdeg of s_lam is a + c = lam_1 + lam_3.")
    print("        For lam = (j,j,0): e-wdeg = j + 0 = j.  ok.")
    print("        For lam = (2j, 0, 0): e-wdeg = 2j. TOO BIG (only appears if j <= 1).")
    print("=" * 78)
    for jj in range(J_MAX + 1):
        max_over_bt = -1
        for mu, kap in tables[jj]:
            a1, b1, c1 = mu
            claimed = a1 + c1
            actual = ewdeg(s_to_elem(mu))
            match = (claimed == actual)
            if actual > jj:
                max_over_bt = max(max_over_bt, actual)
            print(f"    lam={mu}: claimed e-wdeg = a+c = {claimed}, actual = {actual}, match={match}")
        print(f"  j={jj}: max s_lam e-wdeg among bt(j) = {max([ewdeg(s_to_elem(mu)) for mu, _ in tables[jj]])}, need <= {jj}")


if __name__ == "__main__":
    main()
