"""Just extract and fit h_k^{(13)} polynomials, log progress. Used to
estimate time for the periodicity script."""
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


def fit_bivariate_poly_int(samples, deg_bound=28):
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
        coeff = {}
        for (da, db), c in zip(monomials, sol):
            coeff[(da, db)] = int(c)
        for (av, bv, yv) in samples:
            s = 0
            for (da, db), c in coeff.items():
                s += c * (av ** da) * (bv ** db)
            if s != yv:
                coeff = None
                break
        if coeff is not None:
            return coeff, D
    return None, None


def main():
    c_val = 13
    jmax = c_val - 1
    print(f"[extract] h_k^({c_val}) for k=0..{jmax}", flush=True)
    tables = build_e2_tables(max_j=jmax + 2)
    per_k_samples = {k: [] for k in range(jmax + 1)}
    t0 = time.time()
    n = 0
    for a in range(c_val, c_val + 27):
        for b in range(c_val, a + 1):
            hks = extract_h_k(a, b, c_val, jmax, tables)
            if hks is None:
                continue
            for k, y in enumerate(hks):
                per_k_samples[k].append((a, b, y))
            n += 1
    print(f"  {n} samples in {time.time() - t0:.1f}s", flush=True)

    coeff_by_k = {}
    for k in range(jmax + 1):
        t1 = time.time()
        coeff, D = fit_bivariate_poly_int(per_k_samples[k])
        dt = time.time() - t1
        if coeff is None:
            print(f"  k={k}: FIT FAILED after {dt:.1f}s", flush=True)
            continue
        coeff_by_k[k] = coeff
        print(f"  k={k}: deg <= {D}, ok ({dt:.1f}s, {len(coeff)} monomials)", flush=True)

    # Persist to pickle for reuse
    import pickle
    with open("/home/agent/projects/code/2026-07-12-c13-coeff.pkl", "wb") as f:
        pickle.dump(coeff_by_k, f)
    print(f"Saved coeff_by_k to /home/agent/projects/code/2026-07-12-c13-coeff.pkl", flush=True)


if __name__ == "__main__":
    sys.exit(main())
