"""Day 89 Stage B — extract h_k^{(c=8)}(a, b) for k = 0..15 as sympy polynomials.

Uses the H_c_template pipeline (Sym-side M_j identification, c-uniform)
and Möbius inversion h_k = sum_{j <= k} (-1)^{k-j} C(k,j) H_c(a,b,j).

Fits each h_k as a bivariate integer polynomial of total degree <= 16.
Writes the sympy expressions to a pickle for use by the periodicity check.
"""
import pickle
import time
from importlib import util
from math import factorial

from sympy import Matrix, Rational, expand, factor, symbols

# Load pipeline
spec = util.spec_from_file_location(
    "hkfit", "/home/agent/projects/code/2026-07-10-hk-three-var-fit.py"
)
mod = util.module_from_spec(spec)
spec.loader.exec_module(mod)

extract_h_k = mod.extract_h_k
build_e2_tables = mod.build_e2_tables
H_c_template = mod.H_c_template


def Cn(n, k):
    if k < 0 or k > n:
        return 0
    return factorial(n) // (factorial(k) * factorial(n - k))


def collect_hk_samples_c8(jmax=15, arange=(8, 34)):
    """Return dict {k: [(a, b, y)]} where y = h_k^{(c=8)}(a, b) for a >= b >= 8."""
    c_val = 8
    tables = build_e2_tables(max_j=jmax + 2)
    per_k = {k: [] for k in range(jmax + 1)}
    t0 = time.time()
    n_done = 0
    for a in range(arange[0], arange[1]):
        for b in range(arange[0], a + 1):
            hks = extract_h_k(a, b, c_val, jmax, tables)
            if hks is None:
                continue
            for k, y in enumerate(hks):
                per_k[k].append((a, b, y))
            n_done += 1
    print(f"  {n_done} samples extracted in {time.time() - t0:.1f} sec")
    return per_k


def fit_bivariate_poly(samples, deg_bound=18):
    """Fit y = h_k(a, b) as sum_{da+db<=D} coef * a^da * b^db.
    Returns (poly, deg) or (None, None).
    """
    a_s, b_s = symbols('a b')
    for D in range(deg_bound + 1):
        monomials = [(da, db) for da in range(D + 1) for db in range(D + 1 - da)]
        N = len(monomials)
        if len(samples) < N + 5:
            continue
        # Build system.
        A_rows = []
        y_vals = []
        for (av, bv, yv) in samples:
            row = [av ** da * bv ** db for (da, db) in monomials]
            A_rows.append(row)
            y_vals.append(yv)
        M = Matrix(A_rows)
        y = Matrix(y_vals)
        aug = M.row_join(y)
        rref, pivots = aug.rref()
        if (aug.cols - 1) in pivots:
            continue  # inconsistent -> increase degree
        if len(pivots) != N:
            continue  # under-determined -> more degree
        sol = [rref[pivots.index(i), aug.cols - 1] for i in range(N)]
        # Check all integer
        for c in sol:
            if not isinstance(c, Rational) or c.q != 1:
                # non-integer coef -> false fit shape? try higher degree
                break
        else:
            poly = 0
            for (da, db), c in zip(monomials, sol):
                poly += int(c) * a_s ** da * b_s ** db
            poly = expand(poly)
            # Verify on all samples.
            for (av, bv, yv) in samples:
                got = poly.subs({a_s: av, b_s: bv})
                if got != yv:
                    print(f"    FIT FAIL VERIFY: (a,b)=({av},{bv}) pred={got} actual={yv}")
                    break
            else:
                return poly, D
    return None, None


def main():
    print("=" * 70)
    print("Day 89 Stage B — extract h_k^{(c=8)}(a, b) for k = 0..15")
    print("=" * 70)

    print("\n[1] Collecting samples via H_c_template at c=8 (a in [8,34), b in [8,a+1])...")
    per_k = collect_hk_samples_c8(jmax=15, arange=(8, 34))
    print(f"    Sample counts per k: {[len(per_k[k]) for k in range(16)]}")

    print("\n[2] Fitting h_k^{(c=8)}(a, b) as bivariate poly...")
    h_c8 = {}
    for k in range(16):
        samples = per_k[k]
        if len(samples) < 20:
            print(f"  k={k}: NOT ENOUGH SAMPLES ({len(samples)})")
            continue
        t0 = time.time()
        poly, D = fit_bivariate_poly(samples, deg_bound=18)
        dt = time.time() - t0
        if poly is None:
            print(f"  k={k}: NO FIT within deg <= 18 ({dt:.1f}s)")
        else:
            fpoly = factor(poly)
            print(f"  k={k}: deg <= {D:>2d}  ({dt:>5.1f}s)   fits {len(samples)} samples")
            print(f"        h_{k}^(8) = {fpoly}")
            h_c8[k] = poly

    # Save.
    out = "/home/agent/projects/code/2026-07-11-c8-hk-fits.pkl"
    with open(out, 'wb') as f:
        pickle.dump({k: str(v) for k, v in h_c8.items()}, f)
    print(f"\n    Wrote {out}")

    # Sanity: reconstruct H_8(a, b, j) from h_k^{(c=8)} and cross-check.
    print("\n[3] Sanity: H_8(a,b,j) = sum C(j,k) h_k(a,b) matches pipeline...")
    tables = build_e2_tables(max_j=17)
    a_s, b_s = symbols('a b')
    ok = 0
    fail = 0
    for a in [8, 9, 15, 20]:
        for b in [8, 9]:
            if b > a:
                continue
            for j in [0, 2, 5, 10, 15]:
                H_actual = H_c_template(a, b, 8, j, tables)
                if H_actual is None:
                    continue
                H_pred = 0
                for k in range(min(j, 15) + 1):
                    if k not in h_c8:
                        H_pred = None
                        break
                    H_pred += Cn(j, k) * int(h_c8[k].subs({a_s: a, b_s: b}))
                if H_pred is None:
                    continue
                if H_actual == H_pred:
                    ok += 1
                else:
                    fail += 1
                    if fail <= 3:
                        print(f"  FAIL (a,b,j)=({a},{b},{j}): actual={H_actual} pred={H_pred}")
    print(f"    Sanity: {ok} match, {fail} fail")


if __name__ == "__main__":
    main()
