"""Extended verification of (⋆⋆-a'') for p = 1.

Statement:  Q_j(b) * A_1(b, c, j) = (b+2)_{c-3} * R_1(b, c, j)
where Q_j(b) = (b+2)_{c-1-j},  A_1(b, c, j) = [a^{j-1}] S_j(a, b, c),
and R_1(b, c, j) is a polynomial with per-b-slot j-degree <= 2.

Verifies for c in {6, 8, 10, 12, 15, 20}, j = 1, ..., min(c-1, 9).

Also EXPLICITLY extracts A_1 formula and R_1 formula for small j to look for
a pattern.
"""

import sys
import time
from collections import defaultdict
from itertools import combinations
from math import comb

import sympy as sp
from sympy import symbols, factor, expand, simplify, Poly, cancel, binomial, Integer

a, b, c = symbols('a b c')
j_sym = symbols('j')
x1, x2, x3 = a + 2, b + 1, c

OUT = []
def P(*s):
    line = ' '.join(str(x) for x in s)
    print(line, flush=True)
    OUT.append(line)


def fall(x, m):
    p = Integer(1)
    for i in range(m):
        p *= (x - i)
    return p


def rise(x, L):
    p = Integer(1)
    for i in range(L):
        p *= (x + i)
    return p


def det3(rows):
    (a11, a12, a13), (a21, a22, a23), (a31, a32, a33) = rows
    return (a11*(a22*a33 - a23*a32)
            - a12*(a21*a33 - a23*a31)
            + a13*(a21*a32 - a22*a31))


def bt(M):
    """Build partition tables via successive vertical-2-strip additions."""
    def vs(mu):
        L = len(mu) + 2
        bb = list(mu) + [0] * (L - len(mu))
        r = []
        for p in combinations(range(L), 2):
            n = bb.copy()
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


def ds_symbolic(j, tables):
    xs = (x1, x2, x3)
    total = Integer(0)
    for mu, kap in tables[j]:
        ks = [mu[col] + (2 - col) for col in range(3)]
        rows = [[fall(xs[i], ks[col]) for col in range(3)] for i in range(3)]
        total += kap * det3(rows)
    return expand(total)


def compute_dsV_symbolic(J, tables):
    V = ds_symbolic(0, tables)
    cache = {}
    for j in range(J + 1):
        dsj = ds_symbolic(j, tables)
        q, r = sp.div(Poly(dsj, [a, b, c]), Poly(V, [a, b, c]))
        assert r.as_expr() == 0, f"V does not divide ds_{j}"
        cache[j] = q.as_expr()
    return cache


def extract_A_p(j, p, dsV_cache):
    """A_p(b, c, j) = [a^{j-p}] S_j(a, b, c), as polynomial in (b, c)."""
    S = dsV_cache[j]
    if j - p < 0:
        return Integer(0)
    pab = Poly(S, a, b, c)
    result = Integer(0)
    for monom, cf in pab.terms():
        da, db, dc = monom
        if da == j - p:
            result += cf * b**db * c**dc
    return expand(result)


def j_degree_of_samples(samples):
    """Fit polynomial to (j, value) samples in the j-variable; return degree
    (returns -1 if all zero, None if not polynomial). Note: uses rational lin. alg."""
    all_zero = all(sp.simplify(s[1]) == 0 for s in samples)
    if all_zero:
        return -1
    n = len(samples)
    for D in range(n):
        rows = []
        yy = []
        for (jv, yv) in samples[:D + 1]:
            rows.append([jv ** i for i in range(D + 1)])
            yy.append(yv)
        M = sp.Matrix(rows)
        y = sp.Matrix(yy)
        try:
            sol = M.solve(y)
        except Exception:
            continue
        ok = True
        for (jv, yv) in samples[D + 1:]:
            pred = sum(sol[i] * jv ** i for i in range(D + 1))
            if sp.simplify(pred - yv) != 0:
                ok = False
                break
        if ok:
            if D == 0 or sp.simplify(sol[D]) != 0:
                return D
    return None


def verify_p1_at_c(cv, dsV_cache, max_j=None):
    """For each j, verify (b+2)_{cv-1-j} * A_1(b, cv, j) is divisible by
    (b+2)_{cv-3}, and check the residual R_1 has j-degree <= 2 per b-slot.
    Returns dict {j: R_1(b) as polynomial in b}.
    """
    if max_j is None:
        max_j = min(cv - 1, 9)

    R1_by_j = {}
    non_div_flags = []
    for j in range(1, max_j + 1):
        A1 = extract_A_p(j, 1, dsV_cache).subs(c, cv)
        L = cv - 1 - j
        if L < 0:
            continue
        Qj = Integer(1)
        for i in range(L):
            Qj *= (b + 2 + i)
        prod = expand(Qj * A1)
        divlen = cv - 3
        if divlen < 0:
            continue
        Q_targ = Integer(1)
        for i in range(divlen):
            Q_targ *= (b + 2 + i)
        quot, rem = sp.div(Poly(prod, b), Poly(Q_targ, b))
        if rem != 0:
            R1_by_j[j] = None
            non_div_flags.append(j)
        else:
            R1_by_j[j] = quot.as_expr()
    return R1_by_j, non_div_flags


def measure_j_degrees(R1_by_j, twoP_expected=2):
    """Given R_1 as functions of b indexed by j, extract per-b-slot j-degree."""
    all_bs = set()
    for jv, R in R1_by_j.items():
        if R is None or R == 0:
            continue
        pbR = Poly(R, b)
        for (db,), cf in pbR.terms():
            all_bs.add(db)
    per_slot = []
    max_jd = -1
    for bs in sorted(all_bs):
        samples = []
        for jv in sorted(R1_by_j.keys()):
            R = R1_by_j[jv]
            if R is None:
                continue
            if R == 0:
                samples.append((jv, Integer(0)))
                continue
            pbR = Poly(R, b)
            cf = Integer(0)
            for (db,), c_ in pbR.terms():
                if db == bs:
                    cf = c_
                    break
            samples.append((jv, cf))
        jd = j_degree_of_samples(samples)
        per_slot.append((bs, jd))
        if jd is not None and jd > max_jd:
            max_jd = jd
    return max_jd, per_slot


def dump_A1_small_j(dsV_cache, max_j=6):
    """Extract A_1 explicitly for small j and factor/print it.
    Look for a closed form.
    """
    P("\n" + "=" * 72)
    P("EXPLICIT A_1(b, c, j) for small j")
    P("=" * 72)
    for j in range(1, max_j + 1):
        A1 = extract_A_p(j, 1, dsV_cache)
        A1_f = sp.factor(A1)
        P(f"\n  j = {j}:")
        P(f"    A_1 = {A1_f}")


def dump_R1_pattern(dsV_cache, cv=15, max_j=8):
    """For fixed c = cv, print R_1(b, cv, j) explicitly and try to factor."""
    P("\n" + "=" * 72)
    P(f"R_1(b, c, j) pattern at c = {cv}")
    P("=" * 72)
    R1_by_j, non_div = verify_p1_at_c(cv, dsV_cache, max_j=min(cv - 1, max_j))
    P(f"  Non-div j values (should be empty): {non_div}")
    for jv in sorted(R1_by_j.keys()):
        R = R1_by_j[jv]
        if R is None:
            continue
        R_f = sp.factor(R)
        deg_b = sp.Poly(R, b).degree() if R != 0 else -1
        P(f"    j = {jv}: R_1 = {R_f}  (b-degree {deg_b})")


def verify_A1_closed_form(dsV_cache, max_j=10):
    """Verify A_1(b, c, j) = (b+c-2)^↓(j-2) * P_j(b, c) with the fitted P_j
    for integer j >= 2, and also for j = 1 via the extension P_1 / (b+c-1).

    P_j(b, c, j) = (j/2)*[(b+c)(2bc + 3b + 5c - 3) - j*(b² + 4bc + c² - b + c)]
    """
    P("\n" + "=" * 72)
    P(f"VERIFY CLOSED FORM: A_1(b, c, j) = (b+c-2)^↓(j-2) * P_j(b, c)")
    P("=" * 72)
    all_ok = True
    for jv in range(1, max_j + 1):
        A1 = extract_A_p(jv, 1, dsV_cache)
        Pj = (Integer(1) * jv * (
            2*b**2*c - b**2*jv + 3*b**2
            + 2*b*c**2 - 4*b*c*jv + 8*b*c + b*jv - 3*b
            - c**2*jv + 5*c**2 - c*jv - 3*c
        )) / 2
        prefactor = Integer(1)
        for k in range(jv - 2):
            prefactor *= (b + c - 2 - k)
        if jv == 1:
            # (b+c-2)^↓-1 formally = 1/(b+c-1)
            pred = sp.cancel(Pj / (b + c - 1))
        else:
            pred = expand(prefactor * Pj)
        diff = expand(A1 - pred)
        status = "OK" if diff == 0 else f"!!DIFF={diff}"
        if diff != 0:
            all_ok = False
        P(f"    j = {jv}: {status}")
    return all_ok


def main():
    P("=" * 72)
    P("Day 112 — Verification of (⋆⋆-a'')_{p=1}")
    P("=" * 72)

    C_VALS = [6, 8, 10, 12, 15, 20]
    C_MAX = max(C_VALS)
    J_MAX = 10  # need j up to ~10 to compute A_1 for c up to 20 comfortably.

    P(f"Building partition tables up to j = {J_MAX}...")
    t0 = time.time()
    tables = bt(J_MAX)
    P(f"  built in {time.time() - t0:.2f}s")

    P(f"Computing ds_j/V symbolically in (a, b, c), j = 0..{J_MAX}...")
    dsV_cache = compute_dsV_symbolic(J_MAX, tables)
    P(f"  done in {time.time() - t0:.2f}s total.")

    dump_A1_small_j(dsV_cache, max_j=5)

    all_ok = True
    P("\n" + "=" * 72)
    P("Divisibility + j-degree bound check")
    P("=" * 72)
    for cv in C_VALS:
        P(f"\n c = {cv}:")
        max_j_here = min(cv - 1, 9)
        R1_by_j, non_div = verify_p1_at_c(cv, dsV_cache, max_j=max_j_here)
        if non_div:
            P(f"    !! Non-divisibility at j = {non_div}")
            all_ok = False
        max_jd, per_slot = measure_j_degrees(R1_by_j)
        status = "OK" if max_jd <= 2 else "!!VIOLATION!!"
        if max_jd > 2:
            all_ok = False
        P(f"    j range: 1..{max_j_here}, num samples = {len(R1_by_j)}")
        P(f"    R_1 max per-b-slot j-degree = {max_jd} (expect <= 2) [{status}]")
        P(f"    Per-b-slot: {per_slot}")

    dump_R1_pattern(dsV_cache, cv=15, max_j=8)

    cf_ok = verify_A1_closed_form(dsV_cache, max_j=10)

    P("\n" + "=" * 72)
    P(f"SUMMARY: (⋆⋆-a'')_{{p=1}} verification: {'PASS' if all_ok else 'FAIL'}")
    P(f"          A_1 closed form (Lemma 1): {'PASS' if cf_ok else 'FAIL'}")
    P("=" * 72)

    out_path = "/home/agent/projects/beta-prime/code/2026-08-19-star2a-p1-verify.txt"
    with open(out_path, 'w') as f:
        f.write('\n'.join(OUT))
    P(f"\nSaved log to {out_path}")


if __name__ == "__main__":
    main()
