"""Debug fit failure for h_k^{(13)} k=7..12."""
import sys
import time
from importlib import util

from sympy import Matrix, Rational, symbols

spec = util.spec_from_file_location(
    "hkfit", "/home/agent/projects/code/2026-07-10-hk-three-var-fit.py"
)
mod = util.module_from_spec(spec)
spec.loader.exec_module(mod)
extract_h_k = mod.extract_h_k
build_e2_tables = mod.build_e2_tables


def fit_bivariate_poly_int_debug(samples, deg_bound=16):
    a_s, b_s = symbols('a b')
    for D in range(deg_bound + 1):
        monomials = [(da, db) for da in range(D + 1) for db in range(D + 1 - da)]
        N = len(monomials)
        if len(samples) < N + 3:
            print(f"    D={D}, N={N}: need {N+3}+ samples, have {len(samples)} -- skip", flush=True)
            continue
        t0 = time.time()
        rows = []
        yvals = []
        for (av, bv, yv) in samples:
            rows.append([av ** da * bv ** db for (da, db) in monomials])
            yvals.append(yv)
        M = Matrix(rows)
        y = Matrix(yvals)
        aug = M.row_join(y)
        rref, pivots = aug.rref()
        dt = time.time() - t0
        if (aug.cols - 1) in pivots:
            print(f"    D={D}, N={N}: y-col is pivot -> no consistent solution ({dt:.1f}s)", flush=True)
            continue
        if len(pivots) != N:
            print(f"    D={D}, N={N}: rank {len(pivots)} < N -> under-determined ({dt:.1f}s)", flush=True)
            continue
        sol = [rref[pivots.index(i), aug.cols - 1] for i in range(N)]
        ok_int = True
        for c in sol:
            if not isinstance(c, Rational) or c.q != 1:
                ok_int = False
                break
        if not ok_int:
            print(f"    D={D}, N={N}: solution non-integer ({dt:.1f}s)", flush=True)
            continue
        print(f"    D={D}, N={N}: OK integer solution ({dt:.1f}s)", flush=True)
        return {(da, db): int(c) for (da, db), c in zip(monomials, sol)}, D
    return None, None


def main():
    c_val = 13
    jmax = c_val - 1
    tables = build_e2_tables(max_j=jmax + 2)
    per_k = {k: [] for k in range(jmax + 1)}
    # Broader sample range
    for a in range(c_val, c_val + 18):
        for b in range(c_val, a + 1):
            hks = extract_h_k(a, b, c_val, jmax, tables)
            if hks is None:
                continue
            for k, y in enumerate(hks):
                per_k[k].append((a, b, y))
    print(f"Samples per k: {len(per_k[0])}", flush=True)
    for k in [7, 8, 9, 10, 11, 12]:
        print(f"\nk={k}:", flush=True)
        coeff, D = fit_bivariate_poly_int_debug(per_k[k], deg_bound=16)
        if coeff is None:
            print(f"  FAILED", flush=True)


if __name__ == "__main__":
    main()
