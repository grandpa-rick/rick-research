"""Day 112 v2: DIRECT verification of (***) with the CORRECT parameterization.

The right statement of (***):

For fixed (u, v) with u, v >= 0, let C_{u,v}(j) := coef of a^{j-u} b^{j-v} in
S_j(a, b, c) := ds_j(a, b, c) / V(a, b, c). Then C_{u,v}(j) is a polynomial in j
of degree <= u + v.

(In particular, C_{0,0}(j) = 1 for j >= 1, matching u + v = 0 bound.)

Equivalently: shift indices by "displacement from top corner (j, j)". The
"r-shell" of S_j at (a,b)-degree 2j - r corresponds to slots with u + v = r.

This is exactly the (***) statement in the T-verification writeup — where
"r" = displacement from top = u + v.

STRATEGY:
  1. Compute S_j (with c = integer) for j = 1, ..., J.
  2. For each (u, v) with u + v <= R_max, collect samples
        (j, C_{u,v}(j))  for j >= max(u, v)
     and fit as polynomial in j. Report the j-degree; expect <= u + v.

Test up to R_max = 6.
"""
import sys
import time
from collections import defaultdict
from itertools import combinations

import sympy as sp
from sympy import symbols, factor, expand, simplify, Poly, cancel, Integer

a, b, c = symbols('a b c')

OUT = []
def P(*s):
    line = ' '.join(str(x) for x in s)
    print(line, flush=True)
    OUT.append(line)


def fall(x, m):
    if m < 0:
        return Integer(0)
    p = Integer(1)
    for i in range(m):
        p *= (x - i)
    return p


def det3(rows):
    (a11, a12, a13), (a21, a22, a23), (a31, a32, a33) = rows
    return (a11*(a22*a33 - a23*a32)
            - a12*(a21*a33 - a23*a31)
            + a13*(a21*a32 - a22*a31))


def bt(M):
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


def compute_dsV_at_c(J, cv, tables):
    x1, x2, x3 = a + 2, b + 1, Integer(cv)
    xs_cv = (x1, x2, x3)
    # V at cv
    ks0 = [2, 1, 0]
    V_cv = expand(det3([[fall(xs_cv[i], ks0[col]) for col in range(3)] for i in range(3)]))
    P(f"[V] V at c={cv}: {factor(V_cv)}")

    dsV_at_c = {}
    for j in range(J + 1):
        t0 = time.time()
        total = Integer(0)
        for mu, kap in tables[j]:
            ks = [mu[col] + (2 - col) for col in range(3)]
            rows = [[fall(xs_cv[i], ks[col]) for col in range(3)] for i in range(3)]
            total += kap * det3(rows)
        dsj_cv = expand(total)
        if dsj_cv == 0:
            dsV_at_c[j] = Integer(0)
        else:
            q, rr = sp.div(Poly(dsj_cv, [a, b]), Poly(V_cv, [a, b]))
            assert rr.as_expr() == 0, f"ds_{j}/V not divisible at c={cv}"
            dsV_at_c[j] = q.as_expr()
        pab = Poly(dsV_at_c[j], a, b) if dsV_at_c[j] != 0 else None
        tdeg_ab = max((sum(m) for m, cf in pab.terms() if cf != 0), default=0) if pab else 0
        P(f"  j={j}: (a,b)-deg = {tdeg_ab}  ({time.time()-t0:.2f}s)")
    return dsV_at_c


def get_coef_of(H, ai, bk):
    """Coefficient of a^ai b^bk in expression H."""
    if H == 0:
        return Integer(0)
    pab = Poly(H, a, b)
    for monom, cf in pab.terms():
        if monom == (ai, bk):
            return cf
    return Integer(0)


def j_degree_of_samples(samples):
    """Given list of (j_val, y_val), fit polynomial in j and return its degree."""
    if all(s[1] == 0 for s in samples):
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


def verify(R_max, dsV_at_c, J_max):
    """For each (u, v) with u + v <= R_max, compute C_{u,v}(j) as function of j
    and report j-degree.
    """
    P("\n" + "=" * 72)
    P(f"(***) DIRECT verify at slot (a^{{j-u}} b^{{j-v}}), R_max = {R_max}")
    P("Claim: j-degree of C_{u,v}(j) <= u + v")
    P("=" * 72)

    results = {}
    for r in range(R_max + 1):
        max_uv_deg = -1
        for u in range(r + 1):
            v = r - u
            samples = []
            for jv in range(1, J_max + 1):
                if jv - u < 0 or jv - v < 0:
                    continue
                cf = get_coef_of(dsV_at_c[jv], jv - u, jv - v)
                samples.append((jv, cf))
            if len(samples) < r + 3:
                P(f"  (u={u}, v={v}, r={u+v}): too few samples ({len(samples)}), skip.")
                continue
            jd = j_degree_of_samples(samples)
            results[(u, v)] = jd
            if jd is not None and jd > max_uv_deg:
                max_uv_deg = jd
            status = "OK" if (jd is not None and jd <= u + v) else "!!"
            P(f"  (u={u}, v={v}): C_{{u,v}}(j) sample count = {len(samples)}, j-deg = {jd}"
              f" (bound = {u+v}) [{status}]")
        stat_r = "OK" if max_uv_deg <= r else "!!"
        P(f"  ==> r = {r}: max j-deg = {max_uv_deg} (bound = {r}) [{stat_r}]")
    return results


def show_a0(R_max, dsV_at_c, J_max):
    """Also show the u=0 (a=constant, i.e., top a) slots specifically."""
    P("\n" + "=" * 72)
    P("Table of C_{u,v}(j) values (small u, v)")
    P("=" * 72)
    for u in range(4):
        for v in range(u, 4):  # by symmetry only need v >= u
            P(f"\n  (u, v) = ({u}, {v}):")
            for jv in range(max(u, v), J_max + 1):
                cf = get_coef_of(dsV_at_c[jv], jv - u, jv - v)
                P(f"    j = {jv}: C = {cf}")


def kappa_polydeg(J_max, tables):
    """For each fixed (r, s) shape (mu_3 = r, mu_2 = r + s, mu_1 = 2j - 2r - s),
    fit kappa_mu as polynomial in j and report j-degree."""
    P("\n" + "=" * 72)
    P("kappa_{(mu_1, mu_2, r)} j-degree analysis")
    P("Shape: (r, s) where mu_3 = r, mu_2 = r + s, mu_1 = 2j - 2r - s")
    P("Conjecture: j-degree of kappa is <= r")
    P("=" * 72)
    for r in range(7):
        max_jd = -1
        for s in range(6):
            samples = []
            for j in range(1, J_max + 1):
                for mu, kap in tables[j]:
                    if mu == (2*j - 2*r - s, r + s, r) and mu[0] >= mu[1]:
                        samples.append((j, kap))
                        break
            if len(samples) < r + 3:
                continue
            jd = j_degree_of_samples(samples)
            if jd is not None and jd > max_jd:
                max_jd = jd
            status = "OK" if (jd is not None and jd <= r) else "!!"
            P(f"  r = {r}, s = {s}: samples = {len(samples)}, j-deg = {jd} [{status}]"
              f"  data first 5: {samples[:5]}")
        stat = "OK" if max_jd <= r else ("empty" if max_jd == -1 else "!!")
        P(f"  ==> r = {r}: max j-deg (over shapes) = {max_jd} [{stat}]")


def main():
    P("=" * 72)
    P("Day 112 v2: DIRECT (***) verification with correct parameterization")
    P("=" * 72)

    C_VAL = 25
    J_MAX = 16

    P(f"[bt] Building partition tables up to j = {J_MAX}...")
    t0 = time.time()
    tables = bt(J_MAX)
    P(f"[bt] done in {time.time() - t0:.2f}s")

    P(f"[ds] Computing ds_j/V at c = {C_VAL}...")
    dsV_at_c = compute_dsV_at_c(J_MAX, C_VAL, tables)

    verify(6, dsV_at_c, J_MAX)

    show_a0(6, dsV_at_c, J_MAX)

    kappa_polydeg(J_MAX, tables)

    out_path = "/home/agent/projects/beta-prime/code/2026-08-19-star-star-star-verify-v2.txt"
    with open(out_path, 'w') as f:
        f.write('\n'.join(OUT))
    P(f"\nSaved log to {out_path}")


if __name__ == "__main__":
    main()
