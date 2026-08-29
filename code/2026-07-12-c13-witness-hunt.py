"""Day 91 — Witness hunt at c=13. D2' predicts beta'(13) = 18.

We look for a distinct-min witness (a*, b*, k*) with v_2(H_13) = 18 (or less).
If found at 18, that's beta'(13) <= 18, consistent with D2'.
If found at some v_2 < 18, that MISMATCHES D2'.

Cannot prove beta'(13) >= 18 without a T=18 periodicity check (2^35 residues,
infeasible on this box). Just a witness pass for now.
"""
import sys
import time
from importlib import util
from math import factorial

from sympy import symbols, Matrix, Rational, expand, lambdify

spec = util.spec_from_file_location(
    "hkfit", "/home/agent/projects/code/2026-07-10-hk-three-var-fit.py"
)
mod = util.module_from_spec(spec)
spec.loader.exec_module(mod)
extract_h_k = mod.extract_h_k
build_e2_tables = mod.build_e2_tables


def v2(n):
    if n == 0:
        return float('inf')
    v = 0
    while n % 2 == 0:
        n //= 2
        v += 1
    return v


def Cn(n, k):
    if k < 0 or k > n:
        return 0
    return factorial(n) // (factorial(k) * factorial(n - k))


def fit_bivariate_poly(samples, deg_bound=30):
    a_s, b_s = symbols('a b')
    for D in range(deg_bound + 1):
        monomials = [(da, db) for da in range(D + 1) for db in range(D + 1 - da)]
        N = len(monomials)
        if len(samples) < N + 3:
            continue
        rows = []
        yvals = []
        for (av, bv, yv) in samples:
            rows.append([av ** da * bv ** db for (da, db) in monomials])
            yvals.append(yv)
        M = Matrix(rows)
        y = Matrix(yvals)
        aug = M.row_join(y)
        rref, pivots = aug.rref()
        if (aug.cols - 1) in pivots:
            continue
        if len(pivots) != N:
            continue
        sol = [rref[pivots.index(i), aug.cols - 1] for i in range(N)]
        ok = True
        for c in sol:
            if not isinstance(c, Rational) or c.q != 1:
                ok = False
                break
        if not ok:
            continue
        poly = 0
        for (da, db), coef in zip(monomials, sol):
            poly += int(coef) * a_s ** da * b_s ** db
        poly = expand(poly)
        for (av, bv, yv) in samples:
            got = poly.subs({a_s: av, b_s: bv})
            if got != yv:
                poly = None
                break
        if poly is not None:
            return poly, D
    return None, None


def main():
    print("=" * 80)
    print(f"Day 91 — c=13 witness hunt (D2' predicts beta'(13) = 18)")
    print("=" * 80)

    c_val = 13
    jmax = 12
    print()
    print(f"Extracting h_k^{{(13)}} for k = 0..{jmax}")
    tables = build_e2_tables(max_j=jmax + 2)
    per_k = {k: [] for k in range(jmax + 1)}
    # top-degree h_0 is deg 2*(c-1) = 24. Need >~ 325 samples.
    t0 = time.time()
    n = 0
    for a in range(13, 40):
        for b in range(13, a + 1):
            hks = extract_h_k(a, b, c_val, jmax, tables)
            if hks is None:
                continue
            for k, y in enumerate(hks):
                per_k[k].append((a, b, y))
            n += 1
    print(f"           {n} samples in {time.time() - t0:.1f}s")

    hk_polys = {}
    for k in range(jmax + 1):
        poly, D = fit_bivariate_poly(per_k[k])
        if poly is None:
            print(f"  k={k}: FIT FAILED")
            continue
        hk_polys[k] = poly
        print(f"  k={k}: deg <= {D}, ok")

    # Scan [0, 64)^2 shell a+b odd for min v_2 per k
    print()
    print(f"Scanning [0, 64)^2 shell a+b odd for min v_2 per k")
    a_s, b_s = symbols('a b')
    per_k_min = {}
    for k, poly in hk_polys.items():
        f = lambdify((a_s, b_s), poly, "math")
        min_v = float('inf')
        achievers = []
        for a in range(64):
            for b in range(64):
                if (a + b) % 2 != 1:
                    continue
                try:
                    val = int(f(a, b))
                except OverflowError:
                    val = int(poly.subs({a_s: a, b_s: b}))
                if val == 0:
                    continue
                v = v2(val)
                if v < min_v:
                    min_v = v
                    achievers = [(a, b, val)]
                elif v == min_v and len(achievers) < 8:
                    achievers.append((a, b, val))
        per_k_min[k] = (min_v, achievers)

    print()
    for k in sorted(per_k_min.keys()):
        m, ach = per_k_min[k]
        print(f"  k={k:>2d}: min v_2 = {m}   achievers (first 2): {[(a, b) for a, b, _ in ach[:2]]}")

    kmin_v = min(m for m, _ in per_k_min.values())
    k_star = min(k for k, (m, _) in per_k_min.items() if m == kmin_v)
    print()
    print(f"argmin: k* = {k_star}, min v_2 = {kmin_v}")

    # Try distinct-min witness at k*
    _, achievers = per_k_min[k_star]
    print()
    print(f"Testing distinct-min witnesses at k* = {k_star}:")
    for (a_star, b_star, _) in achievers[:6]:
        summands = []
        total = 0
        for j in range(k_star + 1):
            if j not in hk_polys:
                summands.append(None)
                continue
            val = int(hk_polys[j].subs({a_s: a_star, b_s: b_star}))
            C = Cn(k_star, j)
            contrib = C * val
            total += contrib
            summands.append((j, val, C, contrib, v2(contrib) if contrib else float('inf')))
        v_total = v2(total) if total else float('inf')
        carrier_v = summands[k_star][4]
        others = [s[4] for i, s in enumerate(summands) if s is not None and i != k_star]
        ok = all(v > carrier_v for v in others) if others else False
        note = "OK distinct-min" if ok else "NOT distinct-min"
        print(f"  (a*, b*) = ({a_star}, {b_star})  H_13 = {total}  v_2 = {v_total}  carrier v_2 = {carrier_v}  {note}")
        if ok:
            print(f"     Per-j v_2: {[s[4] for s in summands if s is not None]}")
            break

    print()
    print("=" * 80)
    print("Interpretation")
    print("=" * 80)
    print(f"  D2' predicts beta'(13) = 18.")
    print(f"  Min scan v_2 = {kmin_v}.  Best witness v_2 = {v_total}.")
    if v_total == 18:
        print(f"  MATCH — beta'(13) <= 18, consistent with D2'.")
    elif v_total < 18:
        print(f"  beta'(13) <= {v_total} < 18 — MISMATCH with D2', check.")
    else:
        print(f"  beta'(13) upper bound = {v_total} > 18 — check tighter witness needed.")


if __name__ == "__main__":
    sys.exit(main())
