"""Day 116 — Attempt to prove (StructB) structurally.

(StructB): S_j = ds_j / V in Q[e_1, e_2, e_3](u,y,c) satisfies
  every nonzero coefficient c_{i1,i2,i3} has i_1 + i_2 + 2 i_3 <= j.

Setup:
    xs = (u, y, c)
    for each mu in bt(j) with kappa_mu:
      det_mu = det[fall(x_i, k_l)]_{i,l=0..2}, k_l = mu[l] + (2 - l)
    ds_j = sum_mu kappa_mu det_mu
    V = (u-y)(u-c)(y-c) = Vandermonde
    S_j = ds_j / V

Key idea: introduce a "principal grading" wdeg on Q[u, y, c] via
    wdeg_e(u) = wdeg_e(y) = wdeg_e(c) = 1
    but also assign a "shift" grading via u -> u + t etc.
Actually, the cleanest angle: the (e_1, e_2, e_3) grading corresponds to
    wdeg_e(e_1) = 1, wdeg_e(e_2) = 1, wdeg_e(e_3) = 2.
This is DIFFERENT from the ordinary (u, y, c)-degree.

For any monomial u^a y^b c^c' with a + b + c' = d, in the (e_1, e_2, e_3) expansion via
Newton-Girard / Kostka, the wdeg_e is bounded by d/2 + ??? hmm no.

Actually notice: since e_i is degree i in (u, y, c), we have
    ordinary_deg = i_1 + 2 i_2 + 3 i_3.
So the "e-wdeg" i_1 + i_2 + 2 i_3 is NOT the same as ordinary degree.
i_1 + i_2 + 2 i_3 = ord_deg - i_2 - i_3.

Explicitly: for a homogeneous symmetric polynomial of ordinary degree d in (u, y, c),
its e-basis expansion has e-wdeg
    i_1 + i_2 + 2 i_3 = d - i_2 - i_3
which ranges from ceil(d/3) (when i_1=0, i_3=?) up to d.

Actually the maximum e-wdeg is d itself (from the term with all i_1 = d).
The minimum is d/3 (from e_3^{d/3}).

CLAIM refined: For S_j (ordinary degree 2j in (u,y,c)):
    max e-wdeg = 2j - min(i_2 + i_3)  ... hmm.

Wait — I mis-recalled. Let me recompute:
Poly of e_1^i1 e_2^i2 e_3^i3 has ordinary degree i_1 + 2 i_2 + 3 i_3 in (u,y,c).
So a homogeneous poly of ord deg d has i_1 + 2 i_2 + 3 i_3 = d,
i.e., i_1 = d - 2 i_2 - 3 i_3.
Then e-wdeg = i_1 + i_2 + 2 i_3 = d - i_2 - i_3.
Range: i_2, i_3 >= 0 with 2 i_2 + 3 i_3 <= d.

If d = 2j, then e-wdeg range is from (i_2 = j, i_3 = 0, i_1 = 0 -> wdeg = j)
to (i_2 = 0, i_3 = 0, i_1 = 2j -> wdeg = 2j).

So homogeneous of ordinary degree 2j has e-wdeg between j and 2j.
(StructB): S_j has e-wdeg <= j.
Since min e-wdeg for hom deg 2j = j, (StructB) says e-wdeg is MINIMAL,
i.e., only i_1 + i_2 + 2 i_3 = j = d/2 terms appear (in the leading grade piece)?

Wait no — S_j is NOT homogeneous of ord degree 2j.  It has various homogeneous
components.  For each hom component of degree d, e-wdeg is at least d/2 (roughly),
and (StructB) says <= j.

Actually STEP 2 output above showed S_j has total_deg = 2j.  Is S_j homogeneous?
Let's check.

Hmm the output was total_deg = 2j; but does that mean HOMOGENEOUS or just max degree?
Given the shifted-Schur (falling factorial) structure, S_j is NOT homogeneous — it has
mixed-degree contributions.

But WAIT: the ORDINARY-DEGREE-2j PART of S_j has e-wdeg between j and 2j.  If we can show
ONLY the e-wdeg = j part of the ord-deg-2j piece survives, we get big cancellations.
Similarly for lower-ord-deg pieces.

Let me look at the empirical numbers:
  j=4, ord-deg = 2j = 8: all i_1 + 2 i_2 + 3 i_3 = 8 monomials in e-basis with e-wdeg = 4:
    (i_1, i_2, i_3) satisfies i_1 + 2i_2 + 3 i_3 = 8 AND i_1 + i_2 + 2 i_3 = 4.
    Subtract: i_2 + i_3 = 4.  With 2 i_2 + 3 i_3 <= 8 always.  So all (i_2, i_3) with sum 4:
    (0,4): 3*4=12>8, no.  (1,3): 2+9=11>8, no.  (2,2): 4+6=10>8, no.  (3,1): 6+3=9>8, no.
    (4,0): 8. Yes. Also i_1 = 0.
    So the ONLY leading ord-deg-8 wdeg-4 term is (i_1, i_2, i_3) = (0, 4, 0).
Actually check ord-deg-8 terms in j=4 e-table:  none printed with i1+2i2+3i3=8 except (0,4,0)?

Looking at j=4 output:
    (4, 0, 0): ord-deg = 4, e-wdeg = 4
    (3, 1, 0): ord-deg = 5, wdeg = 4
    (2, 2, 0): ord-deg = 6, wdeg = 4
    (2, 0, 1): ord-deg = 5, wdeg = 4
    (1, 3, 0): ord-deg = 7, wdeg = 4
    (1, 1, 1): ord-deg = 6, wdeg = 4
    (0, 4, 0): ord-deg = 8, wdeg = 4
    (0, 2, 1): ord-deg = 7, wdeg = 4
    (0, 0, 2): ord-deg = 6, wdeg = 4

Interesting: e-wdeg = j = 4 pieces cover all ord degrees from 4 to 8. So the e-wdeg
filtration is INDEPENDENT of ord-deg filtration.

Different approach: verify a stronger structural claim.
"""

from __future__ import annotations
from collections import defaultdict
from itertools import combinations

import sympy as sp
from sympy import expand, Integer, Poly, symbols

u_var, y_var = symbols('u y')
e1_v, e2_v, e3_v = symbols('e1 e2 e3')
c = symbols('c')


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


def to_elem_uyc(F):
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


def S_in_uyc(jj, tables):
    xs = (u_var, y_var, c)
    total = Integer(0)
    for mu, kap in tables[jj]:
        ks = [mu[col] + (2 - col) for col in range(3)]
        rows = [[fall(xs[i], ks[col]) for col in range(3)] for i in range(3)]
        total += kap * det3(rows)
    V_uyc = (u_var - y_var) * (u_var - c) * (y_var - c)
    q, r = sp.div(Poly(total, u_var, y_var, c), Poly(V_uyc, u_var, y_var, c))
    assert r.as_expr() == 0
    return q.as_expr()


def ds_in_uyc(jj, tables):
    xs = (u_var, y_var, c)
    total = Integer(0)
    for mu, kap in tables[jj]:
        ks = [mu[col] + (2 - col) for col in range(3)]
        rows = [[fall(xs[i], ks[col]) for col in range(3)] for i in range(3)]
        total += kap * det3(rows)
    return expand(total)


def to_hom_grades(F):
    """Split F(u,y,c) into homogeneous components by ordinary degree."""
    F = expand(F)
    P = Poly(F, u_var, y_var, c)
    grades = defaultdict(lambda: Integer(0))
    for m, cf in P.terms():
        if cf == 0:
            continue
        d = sum(m)
        grades[d] += cf * u_var ** m[0] * y_var ** m[1] * c ** m[2]
    return dict(grades)


def e_wdeg_of_poly(F_elem):
    P = Poly(F_elem, e1_v, e2_v, e3_v)
    max_w = -1
    for m, cf in P.terms():
        if cf == 0:
            continue
        w = m[0] + m[1] + 2 * m[2]
        if w > max_w:
            max_w = w
    return max_w


def main():
    J_MAX = 6
    tables = bt(J_MAX)

    print("Homogeneous decomposition of S_j and e-wdeg per grade")
    print("=" * 78)
    for jj in range(J_MAX + 1):
        S = S_in_uyc(jj, tables)
        grades = to_hom_grades(S)
        print(f"\n  j = {jj}:  hom-grades of S_j (ord-deg d -> component):")
        for d in sorted(grades.keys()):
            comp = grades[d]
            comp_e = to_elem_uyc(comp)
            w = e_wdeg_of_poly(comp_e)
            # theoretical min-wdeg for hom degree d: min over 2 i_2 + 3 i_3 <= d,
            # i_1 = d - 2 i_2 - 3 i_3, wdeg = d - i_2 - i_3.
            # to minimize wdeg maximize i_2 + i_3, subject to 2 i_2 + 3 i_3 <= d.
            # max i_2 + i_3 = d // 2 (when i_3 = 0, i_2 = d//2), so min wdeg = d - d//2 = ceil(d/2).
            # But d must equal i_1 + 2 i_2 + 3 i_3 so i_1 = d - 2 i_2 (with i_3=0), so d even for i_3=0.
            # min wdeg over hom deg d is: for d even, d/2. For d odd, min needs i_3=1: i_2=(d-3)/2, wdeg = d - (d-3)/2 - 1 = (d+1)/2.
            # So min wdeg = ceil(d/2).
            import math
            th_min = math.ceil(d / 2)
            print(f"    d = {d}: e-wdeg = {w},  theoretical min = {th_min}, target <= j = {jj}")

    # ANALYTIC CLAIM ATTEMPT: For each mu and each hom-grade component of s*_mu(u,y,c),
    # the e-wdeg is close to |mu|/2 = j.
    #
    # But s*_mu VIOLATES (StructB) term-wise (Attack B step 8).  So we need the SUM
    # over mu to bring down e-wdeg.  Let's compute per-mu s*_mu hom-grade e-wdegs.
    print("\n\nPer-mu, per-hom-grade e-wdeg of s*_mu:")
    print("=" * 78)
    for jj in range(min(J_MAX + 1, 4)):
        print(f"\n  j = {jj}:")
        for mu, kap in tables[jj]:
            xs = (u_var, y_var, c)
            ks = [mu[col] + (2 - col) for col in range(3)]
            rows = [[fall(xs[i], ks[col]) for col in range(3)] for i in range(3)]
            num = det3(rows)
            V_uyc = (u_var - y_var) * (u_var - c) * (y_var - c)
            q, r = sp.div(Poly(num, u_var, y_var, c), Poly(V_uyc, u_var, y_var, c))
            assert r.as_expr() == 0
            s_star = q.as_expr()
            grades = to_hom_grades(s_star)
            for d in sorted(grades.keys()):
                comp = grades[d]
                comp_e = to_elem_uyc(comp)
                w = e_wdeg_of_poly(comp_e)
                print(f"    mu={mu}, d={d}: e-wdeg = {w}, kap={kap}")


if __name__ == "__main__":
    main()
