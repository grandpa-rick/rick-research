"""Verify total (a,b)-degree of Q_{2R}(a,b,c) for R=4 (so 2R=8).

Uses the machinery from 2026-08-18-k1-k2-by-hand.py but keeps BOTH a and b
symbolic, and extends the ds-table to j up to 8.

Q_{2R} = h_{2R} / [(a+3)_{c-1-2R} * (b+2)_{c-1-2R}]
h_{2R} = sum_{j=0}^{2R} (-1)^{2R-j} C(2R, j) H_c(a, b, j)
H_c(a, b, j) = (a+3)_{c-j-1} * (b+2)_{c-j-1} * (ds_j / V)

For R=4, test c = 10, 11, 12. Report a-deg, b-deg, total (a,b)-deg.
"""
import sympy as sp
from sympy import symbols, factor, expand, simplify, Poly, cancel, binomial
from collections import defaultdict
from itertools import combinations

a, b, c = symbols('a b c')
x1, x2, x3 = a + 2, b + 1, c

OUT = []
def P(*s):
    line = ' '.join(str(x) for x in s)
    print(line, flush=True)
    OUT.append(line)


def fall(x, m):
    p = sp.Integer(1)
    for i in range(m):
        p *= (x - i)
    return p


def rise(x, L):
    p = sp.Integer(1)
    for i in range(L):
        p *= (x + i)
    return p


def det3(rows):
    (a11, a12, a13), (a21, a22, a23), (a31, a32, a33) = rows
    return (a11*(a22*a33 - a23*a32)
            - a12*(a21*a33 - a23*a31)
            + a13*(a21*a32 - a22*a31))


# ------------------------------------------------------------------
# Partition tables S_j with kappa multiplicities.
# Built by the iterative transition process from 2026-08-18-lemma1-verify.py:
# starting from mu = () with kappa=1, at each step apply all transitions
# vs(mu) = {mu + e_i + e_j : i<j, weakly decreasing after, <=3 parts}
# and accumulate kappa counts.
# ------------------------------------------------------------------
def bt(M):
    def vs(mu):
        L = len(mu) + 2
        b = list(mu) + [0] * (L - len(mu))
        r = []
        for p in combinations(range(L), 2):
            n = b.copy()
            for i in p:
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
    for j in range(1, M + 1):
        nx = defaultdict(int)
        for mu, cc in cu.items():
            for nu in vs(mu):
                nx[nu] += cc
        cu = nx
        rs = []
        for mu, cc in sorted(cu.items(), reverse=True):
            pd = tuple(list(mu) + [0] * (3 - len(mu)))
            rs.append((pd, cc))
        T[j] = rs
    return T


tables = bt(8)

P("Partition tables S_j (mu, kappa) built via bt() iteration:")
for j in range(9):
    P(f"  S_{j} = {tables[j]}")


def ds(j):
    """Det-sum for partition j."""
    xs = (x1, x2, x3)
    total = sp.Integer(0)
    for mu, kap in tables[j]:
        ks = [mu[col] + (2 - col) for col in range(3)]
        rows = [[fall(xs[i], ks[col]) for col in range(3)] for i in range(3)]
        total += kap * det3(rows)
    return expand(total)


V = ds(0)  # standard Vandermonde-like (a-b+1)(a-c+2)(b-c+1)
P("\nV = ds_0 =", factor(V))


def dsV(j):
    """ds_j / V as polynomial in a,b,c."""
    q, r = sp.div(Poly(ds(j), [a, b, c]), Poly(V, [a, b, c]))
    assert r.as_expr() == 0, f"ds_{j}/V has nonzero remainder"
    return q.as_expr()


P("\nVerify ds_j / V is polynomial for j = 0..8:")
dsV_cache = {}
for j in range(9):
    dsV_cache[j] = dsV(j)
    P(f"  j={j}: OK (deg in a,b,c = {Poly(dsV_cache[j], [a, b, c]).total_degree()})")


def H_c(j, c_val):
    """H_c(a, b, j) with concrete integer c = c_val, symbolic a, b.

    H_c = (a+3)_{c-j-1} * (b+2)_{c-j-1} * (ds_j / V)
    Note: the problem states this form directly (with the (a+3) rising factorial
    to length c-j-1, not c-j-2). Following the problem statement literally.
    """
    L = c_val - j - 1
    if L < 0:
        raise ValueError(f"Pochhammer length negative at c={c_val}, j={j}")
    poch_a = rise(a + 3, L)
    poch_b = rise(b + 2, L)
    dsj_over_V_at_c = dsV_cache[j].subs(c, c_val)
    return expand(poch_a * poch_b * dsj_over_V_at_c)


def total_deg_ab(expr):
    """Total degree of expr in (a, b) = max over monomials of (deg_a + deg_b)."""
    pab = Poly(expr, a, b)
    max_td = 0
    for monom, coef in pab.terms():
        if coef == 0:
            continue
        td = sum(monom)
        if td > max_td:
            max_td = td
    return max_td


def a_deg(expr):
    return Poly(expr, a).degree()


def b_deg(expr):
    return Poly(expr, b).degree()


# ------------------------------------------------------------------
# R = 4, so 2R = 8. Test at c = 10, 11, 12.
# ------------------------------------------------------------------
R = 4
twoR = 2 * R

P("\n" + "=" * 72)
P(f"R = {R},  2R = {twoR}")
P("Compute Q_{2R}(a, b, c) and report (a-deg, b-deg, total (a,b)-deg)")
P("Expect: a-deg = b-deg = R = 4,  total (a,b)-deg = 2R = 8")
P("=" * 72)

results = []
for cv in [10, 11, 12]:
    # h_{2R}(a, b, c) = sum_{j=0}^{2R} (-1)^{2R-j} C(2R, j) H_c(a, b, j)
    h = sp.Integer(0)
    for j in range(twoR + 1):
        sign = (-1) ** (twoR - j)
        coef = binomial(twoR, j)
        h += sign * coef * H_c(j, cv)
    h = expand(h)

    # Denominator: (a+3)_{c-1-2R} * (b+2)_{c-1-2R}
    L = cv - 1 - twoR  # must be >= 0
    if L < 0:
        P(f"  c = {cv}: c-1-2R = {L} < 0, skipping")
        continue
    denom_a = rise(a + 3, L)
    denom_b = rise(b + 2, L)
    denom = expand(denom_a * denom_b)

    # Divide as polynomial in (a, b). Use cancel then check.
    Q = cancel(h / denom)
    Q = expand(Q)

    # Q should be a polynomial in a, b (with integer coefficients treating c as constant).
    # Verify by multiplying back.
    check = expand(Q * denom - h)
    assert check == 0, f"Q * denom != h at c={cv}: diff = {check}"

    da = a_deg(Q)
    db = b_deg(Q)
    dtot = total_deg_ab(Q)
    match = (da == R) and (db == R) and (dtot == twoR)
    results.append((cv, da, db, dtot, match))
    P(f"  c = {cv:2d}: a-deg = {da},  b-deg = {db},  total (a,b)-deg = {dtot}"
      f",  matches R=4, 2R=8 pattern? {match}")

P("\n" + "=" * 72)
P("SUMMARY")
P("=" * 72)
P(f"{'c':>4} {'a-deg':>8} {'b-deg':>8} {'total':>8} {'match':>8}")
for (cv, da, db, dtot, match) in results:
    P(f"{cv:>4} {da:>8} {db:>8} {dtot:>8} {str(match):>8}")

all_match = all(m for (_, _, _, _, m) in results)
P(f"\nALL c match pattern (a-deg=b-deg=R=4, total=2R=8): {all_match}")

with open('/home/agent/projects/beta-prime/code/2026-08-18-R4-degrees.txt', 'w') as f:
    f.write('\n'.join(OUT))
P("\nSaved to 2026-08-18-R4-degrees.txt")
