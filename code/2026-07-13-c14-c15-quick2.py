"""Timing test for extract+fit at c=14, jmax=8."""
import sys
import time
from importlib import util
from math import factorial

from sympy import symbols, Matrix, Rational, expand

spec = util.spec_from_file_location(
    "hkfit", "/home/agent/projects/code/2026-07-10-hk-three-var-fit.py"
)
mod = util.module_from_spec(spec)
spec.loader.exec_module(mod)


def fit_bivariate_poly(samples, deg_bound=32):
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
        for (da, db), c in zip(monomials, sol):
            poly += int(c) * a_s ** da * b_s ** db
        poly = expand(poly)
        bad = False
        for (av, bv, yv) in samples:
            got = poly.subs({a_s: av, b_s: bv})
            if got != yv:
                bad = True
                break
        if bad:
            continue
        return poly, D
    return None, None


c_val = 14
jmax = 8
print(f"Sampling c={c_val}, jmax={jmax}...", flush=True)
t0 = time.time()
tables = mod.build_e2_tables(max_j=jmax + 2)
print(f"  tables in {time.time()-t0:.1f}s", flush=True)

per_k = {k: [] for k in range(jmax + 1)}
t0 = time.time()
n_ok = 0
arange = (14, 36)
for a in range(arange[0], arange[1]):
    for b in range(c_val, a + 1):
        hks = mod.extract_h_k(a, b, c_val, jmax, tables)
        if hks is None:
            continue
        for k, y in enumerate(hks):
            per_k[k].append((a, b, y))
        n_ok += 1
print(f"  {n_ok} samples in {time.time()-t0:.1f}s", flush=True)

for k in range(jmax + 1):
    samples = per_k[k]
    print(f"\nFitting k={k}, {len(samples)} samples...", flush=True)
    t0 = time.time()
    poly, D = fit_bivariate_poly(samples, deg_bound=32)
    dt = time.time() - t0
    print(f"  k={k}: deg={D}, fit time = {dt:.1f}s", flush=True)
    if poly is None:
        print(f"    NO FIT!", flush=True)
