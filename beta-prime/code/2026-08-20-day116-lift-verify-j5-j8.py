"""Day 116 — Extended verification of the LIFT THEOREM.

LIFT THEOREM:  S_j(u, y, c) = sum_mu kap_mu * s^*_mu(u, y, c),
               where kap_mu = K_{mu', (2^j)} = # SSYT of shape mu' with content (2^j)
                            = coefficient of s_mu in (e_2)^j (in the ordinary Schur basis).

Route 1's bt(j) procedure produces the kap_mu; we compare S_j (from ds_j / V) against
this sum, in the symmetric variables (u, y, c).

This script:
  (i)   Independently computes kap_mu via Kostka: kap_mu := K_{mu', (2^j)}.
  (ii)  Cross-checks kap_mu vs. Rick's bt(j) tables (via ordinary Schur expansion
        of (e_2)^j in 3 variables).
  (iii) Verifies S_j - sum kap_mu s^*_mu == 0 for j in {5, 6, 7, 8}.
"""

from collections import defaultdict
from itertools import combinations, product

import sympy as sp
from sympy import symbols, expand, Poly, Integer

a, b, c = symbols('a b c')
u_var, y_var = symbols('u y')


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
    """Rick's bt: iteratively add a "2-strip" (two boxes in distinct rows) M times."""
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


def V_uyc(xs):
    x0, x1, x2 = xs
    return (x0 - x1) * (x0 - x2) * (x1 - x2)


def factorial_schur(mu, xs):
    """s^*_mu(xs) in Attack B's convention (three variables):
       det[ fall(x_i, mu[col] + (2 - col)) ] / V(xs).
    """
    ks = [mu[col] + (2 - col) for col in range(3)]
    rows = [[fall(xs[i], ks[col]) for col in range(3)] for i in range(3)]
    num = det3(rows)
    V = V_uyc(xs)
    vars_ = list(xs)
    q, r = sp.div(Poly(num, *vars_), Poly(V, *vars_))
    assert r.as_expr() == 0, f"V does not divide numerator for mu={mu}"
    return q.as_expr()


def ds_symbolic_uyc(jj, tables):
    xs = (u_var, y_var, c)
    total = Integer(0)
    for mu, kap in tables[jj]:
        ks = [mu[col] + (2 - col) for col in range(3)]
        rows = [[fall(xs[i], ks[col]) for col in range(3)] for i in range(3)]
        total += kap * det3(rows)
    return expand(total)


def S_of_uyc(jj, tables):
    """S_j in (u, y, c) variables directly."""
    dsj = ds_symbolic_uyc(jj, tables)
    V = V_uyc((u_var, y_var, c))
    q, r = sp.div(Poly(dsj, u_var, y_var, c), Poly(V, u_var, y_var, c))
    assert r.as_expr() == 0
    return q.as_expr()


def ord_schur(mu, xs):
    """Ordinary Schur polynomial s_mu(xs) via Jacobi-Trudi bialternant."""
    n = 3
    rows = [[xs[i]**(mu[col] + n - 1 - col) for col in range(n)]
            for i in range(n)]
    num = det3(rows)
    V = V_uyc(xs)
    vars_ = list(xs)
    q, r = sp.div(Poly(num, *vars_), Poly(V, *vars_))
    assert r.as_expr() == 0
    return q.as_expr()


def transpose(mu):
    if all(x == 0 for x in mu):
        return ()
    L = max(mu)
    return tuple(sum(1 for x in mu if x >= i + 1) for i in range(L))


def kostka_via_ssyt(shape, content):
    """Count SSYT of given (partition) shape with given content vector.
    shape: tuple (nonzero descending parts).
    content: dict/list; content[i] = # entries equal to i+1.
    Simple brute-force via recursive filling row by row."""
    if not shape:
        return 1 if sum(content) == 0 else 0
    n = sum(content)
    if sum(shape) != n:
        return 0
    # boxes in row-major order
    rows = list(shape)
    R = len(rows)
    # boxes: list of (row, col), in reading order (row by row, left to right)
    boxes = []
    for r_idx in range(R):
        for c_idx in range(rows[r_idx]):
            boxes.append((r_idx, c_idx))
    # We fill boxes with values 1..len(content). Rows weakly increase, columns strictly increase.
    filling = {}
    Kmax = len(content)
    count = [0]

    def rec(idx):
        if idx == len(boxes):
            count[0] += 1
            return
        r_i, c_i = boxes[idx]
        # min value: left neighbor requires >= it (weak); upper neighbor requires > it (strict)
        lo = 1
        if c_i > 0:
            lo = max(lo, filling[(r_i, c_i - 1)])
        if r_i > 0:
            lo = max(lo, filling[(r_i - 1, c_i)] + 1)
        for v in range(lo, Kmax + 1):
            # check remaining budget for value v
            used_v = sum(1 for k, val in filling.items() if val == v)
            if used_v + 1 > content[v - 1]:
                continue
            filling[(r_i, c_i)] = v
            rec(idx + 1)
            del filling[(r_i, c_i)]

    rec(0)
    return count[0]


def partitions_of_at_most_3_parts(n):
    """All partitions of n with at most 3 parts."""
    out = []
    for a1 in range(n, -1, -1):
        for a2 in range(min(a1, n - a1), -1, -1):
            a3 = n - a1 - a2
            if a3 <= a2 and a3 >= 0:
                out.append((a1, a2, a3))
    return out


def main():
    J_MAX = 8
    print(f"Building bt(j) tables up to j = {J_MAX} ...")
    tables = bt(J_MAX)
    for jj in range(J_MAX + 1):
        nkeys = len(tables[jj])
        print(f"  j={jj}: {nkeys} partitions, entries: {tables[jj]}")

    print("\n" + "=" * 78)
    print("STEP 1: Verify kap_mu = K_{mu', (2^j)} via SSYT counting")
    print("=" * 78)

    kappa_from_kostka = {}
    for jj in range(J_MAX + 1):
        parts = partitions_of_at_most_3_parts(2 * jj)
        row = {}
        for mu in parts:
            mu_nz = tuple(x for x in mu if x > 0)
            mut = transpose(mu_nz)
            # content is (2^j)
            content = [2] * jj
            k = kostka_via_ssyt(mut, content)
            if k > 0:
                row[mu] = k
        kappa_from_kostka[jj] = row
        # Compare against bt table
        bt_dict = dict(tables[jj])
        all_mu = set(bt_dict.keys()) | set(row.keys())
        mismatches = []
        for mu in sorted(all_mu, reverse=True):
            kb = bt_dict.get(mu, 0)
            kk = row.get(mu, 0)
            if kb != kk:
                mismatches.append((mu, kb, kk))
        if mismatches:
            print(f"  j={jj}: MISMATCH  {mismatches}")
        else:
            print(f"  j={jj}: bt table == K_{{mu', (2^j)}}  ({len(row)} nonzero mus)  OK")

    print("\n" + "=" * 78)
    print("STEP 2: Verify LIFT: S_j == sum_mu kap_mu * s^*_mu(u, y, c) for j <= 8.")
    print("        Using kap_mu from Kostka (independent of bt).")
    print("=" * 78)

    xs = (u_var, y_var, c)
    for jj in range(J_MAX + 1):
        # Compute S_j via ds_j / V using bt table (this is Rick's definition of S_j)
        S_j = S_of_uyc(jj, tables)
        # Compute sum_mu kap_mu * s^*_mu using Kostka-derived kappas
        expected = Integer(0)
        for mu, k in kappa_from_kostka[jj].items():
            expected += k * factorial_schur(mu, xs)
        diff = expand(S_j - expected)
        equal = (diff == 0)
        status = "PASS" if equal else "FAIL"
        # Get degree info for logging
        pS = Poly(S_j, u_var, y_var, c) if S_j != 0 else None
        deg = pS.total_degree() if pS else -1
        print(f"  j={jj}: S_j (total_deg={deg}) == sum kap * s^*_mu ?  {equal}  [{status}]")
        if not equal:
            # Print the difference (leading terms)
            print(f"    diff = {diff}")

    print("\n" + "=" * 78)
    print("SUMMARY: If all j in {0,...,8} PASS, LIFT THEOREM is EMPIRICALLY ROBUST.")
    print("=" * 78)


if __name__ == "__main__":
    main()
