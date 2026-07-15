"""Day 97 Task A — Master Formula (M) verification at m ∈ {4, 5}.

Goal: verify Q_{2m+1}(a, 0, c) matches the Master Formula prediction
    Q_{2m+1}(a, 0, c) = c(c-1)(c-2m) · Π_{i=2}^{2m-1}(c-i)^2
                        · [2m(2m+1)(a+2) − (c-1)(c-2m)(c-2m-1)]
for m ∈ {4, 5}, i.e. k ∈ {9, 11}, across c ∈ {12, 16, 20, 24, 28, 32}
and a ∈ {0, 1, 2, 3, 4, 5}.

Method: for each (c, k), extract h_k^{(c)}(a, b) samples via the standard
pipeline (a ≥ b ≥ c), normalise by the Pochhammer factors to get integer
samples of Q_k^{(c)}(a, b), fit as a bivariate polynomial of low total
degree in (a, b), then substitute b = 0 and evaluate at the six a-values.
Compare directly to the Master Formula prediction.
"""

import json
import sys
import time
from importlib import util
from fractions import Fraction

import sympy as sp

# Pipeline for h_k extraction.
spec = util.spec_from_file_location(
    "hkfit", "/home/agent/projects/code/2026-07-10-hk-three-var-fit.py"
)
hkfit = util.module_from_spec(spec)
spec.loader.exec_module(hkfit)


def rising_fact(x, n):
    if n <= 0:
        return 1
    p = 1
    for i in range(n):
        p *= (x + i)
    return p


def master_odd(m, c_val, a_val):
    """Master Formula prediction Q_{2m+1}(a, 0, c) as an integer."""
    if m == 0:
        return -c_val * (c_val - 1)
    prefactor = c_val * (c_val - 1) * (c_val - 2 * m)
    for i in range(2, 2 * m):
        prefactor *= (c_val - i) ** 2
    bracket = 2 * m * (2 * m + 1) * (a_val + 2) - (c_val - 1) * (c_val - 2 * m) * (c_val - 2 * m - 1)
    return prefactor * bracket


def sample_Qk_normalized(c_val, k_target, num_pts_target=200):
    """Sample Q_k^{(c)}(a, b) = h_k(a,b) / ((a+3)_L (b+2)_L) at integer (a, b)
    with a >= b >= c. Returns list of (a, b, Q_val_int).

    Fails if any sample is non-integer (which would signal a broken conjecture).
    """
    L = c_val - 1 - k_target
    assert L >= 0, f"L={L} negative for c={c_val}, k={k_target}"
    tables = hkfit.build_e2_tables(max_j=k_target + 2)
    samples = []
    # sweep outward until we have enough samples
    a_hi = c_val
    while len(samples) < num_pts_target and a_hi < c_val + 60:
        a_hi += 1
        for a in range(a_hi - 1, a_hi):
            for b in range(c_val, a + 1):
                hks = hkfit.extract_h_k(a, b, c_val, k_target, tables)
                if hks is None:
                    continue
                if k_target >= len(hks):
                    continue
                y = hks[k_target]
                denom = rising_fact(a + 3, L) * rising_fact(b + 2, L)
                if denom == 0:
                    continue
                if y % denom != 0:
                    print(f"  ! non-integer Q at (a={a}, b={b}, c={c_val}, k={k_target})")
                    return None
                samples.append((a, b, y // denom))
    return samples


def fit_bivariate_poly(samples, max_deg):
    """Fit samples to sum c_{da,db} a^da b^db, total degree <= max_deg.
    Returns sympy polynomial or None."""
    a, b = sp.symbols('a b')
    monomials = [(da, db) for da in range(max_deg + 1)
                 for db in range(max_deg + 1 - da)]
    N = len(monomials)
    if len(samples) < N:
        return None
    rows = []
    yvals = []
    for (av, bv, yv) in samples:
        rows.append([av ** da * bv ** db for (da, db) in monomials])
        yvals.append(yv)
    M = sp.Matrix(rows)
    y = sp.Matrix(yvals)
    aug = M.row_join(y)
    rref, pivots = aug.rref()
    if (aug.cols - 1) in pivots:
        return None
    if len(pivots) != N:
        return None
    sol = [rref[pivots.index(i), aug.cols - 1] for i in range(N)]
    poly = 0
    for (da, db), coef in zip(monomials, sol):
        poly += coef * a ** da * b ** db
    poly = sp.expand(poly)
    # verify on samples
    for (av, bv, yv) in samples:
        if poly.subs({a: av, b: bv}) != yv:
            return None
    return poly


def fit_Qk_c(c_val, k_target, verbose=False):
    """Return sympy poly Q_k^{(c)}(a, b) or None."""
    t0 = time.time()
    # Expected bivariate degree bound = 2*floor(k/2).
    # For safety, sample more than min needed and try increasing degrees.
    bd = 2 * (k_target // 2)
    # +2 slack in case pattern is wrong at higher k
    max_deg_try = bd + 4
    max_monos = (max_deg_try + 1) * (max_deg_try + 2) // 2
    num_pts_target = max_monos + 20
    samples = sample_Qk_normalized(c_val, k_target, num_pts_target=num_pts_target)
    t_sample = time.time() - t0
    if samples is None:
        print(f"  [c={c_val},k={k_target}] non-integer Q, aborting")
        return None, None
    if verbose:
        print(f"  [c={c_val},k={k_target}] sampled {len(samples)} pts in {t_sample:.1f}s")
    for D in range(0, max_deg_try + 1):
        # need at least (D+1)(D+2)/2 samples
        nm = (D + 1) * (D + 2) // 2
        if len(samples) < nm + 3:
            continue
        t1 = time.time()
        poly = fit_bivariate_poly(samples, D)
        t_fit = time.time() - t1
        if poly is not None:
            # extra verification: re-check on independent samples if available
            if verbose:
                print(f"  [c={c_val},k={k_target}] fit at deg={D}, "
                      f"nm={nm}, {t_fit:.1f}s")
            return poly, D
    return None, None


def check_master_formula(c_val, m, poly_Q_ab, sample_a=(0, 1, 2, 3, 4, 5)):
    """Check Q_{2m+1}(a, 0, c) matches Master Formula for sample a-values.
    Returns list of dicts."""
    a, b = sp.symbols('a b')
    poly_at_b0 = sp.expand(poly_Q_ab.subs(b, 0))
    rows = []
    for a_val in sample_a:
        actual = int(poly_at_b0.subs(a, a_val))
        pred = master_odd(m, c_val, a_val)
        rows.append({
            'c': c_val,
            'k': 2 * m + 1,
            'm': m,
            'a': a_val,
            'actual': actual,
            'pred': pred,
            'match': (actual == pred),
        })
    return rows, poly_at_b0


def main():
    print("=" * 78)
    print("Day 97 Task A — Master Formula (M) stress test at m ∈ {4, 5}")
    print("=" * 78)

    c_vals = [12, 16, 20, 24, 28, 32]
    ms = [4, 5]
    a_test = [0, 1, 2, 3, 4, 5]

    all_rows = []
    fit_summary = []

    for m in ms:
        k = 2 * m + 1
        print(f"\n--- m={m} (k={k}) ---")
        for c_val in c_vals:
            print(f"\nc={c_val}, k={k}:")
            t0 = time.time()
            poly_Q, D_fit = fit_Qk_c(c_val, k, verbose=True)
            if poly_Q is None:
                print(f"  FIT FAILED for c={c_val}, k={k}")
                fit_summary.append({
                    'c': c_val, 'k': k, 'fit_ok': False,
                    'time_s': time.time() - t0,
                })
                continue

            rows, poly_b0 = check_master_formula(c_val, m, poly_Q, sample_a=a_test)
            all_rows.extend(rows)
            all_match = all(r['match'] for r in rows)
            print(f"  fit deg={D_fit}, Q_k(a, 0, {c_val}) = {sp.factor(poly_b0)}")
            print(f"  match at a ∈ {a_test}: "
                  f"{'ALL YES' if all_match else 'SOME NO'}")
            for r in rows:
                tag = 'YES' if r['match'] else '*** NO ***'
                print(f"    a={r['a']:>1}: actual={r['actual']}, "
                      f"pred={r['pred']} [{tag}]")
            fit_summary.append({
                'c': c_val, 'k': k, 'fit_ok': True,
                'fit_deg': D_fit,
                'all_match': all_match,
                'time_s': time.time() - t0,
            })

    # Summary table
    print("\n" + "=" * 78)
    print("SUMMARY TABLE")
    print("=" * 78)
    print(f"{'m':>2} {'k':>3} {'c':>3} {'a=0':>7} {'a=1':>7} {'a=2':>7} "
          f"{'a=3':>7} {'a=4':>7} {'a=5':>7}")
    for m in ms:
        k = 2 * m + 1
        for c_val in c_vals:
            marks = []
            for a_val in a_test:
                row = next((r for r in all_rows if r['c'] == c_val
                            and r['k'] == k and r['a'] == a_val), None)
                if row is None:
                    marks.append('?')
                else:
                    marks.append('OK' if row['match'] else 'FAIL')
            print(f"{m:>2} {k:>3} {c_val:>3} "
                  + " ".join(f"{s:>7}" for s in marks))

    n_pass = sum(1 for r in all_rows if r['match'])
    n_total = len(all_rows)
    print(f"\nTotal: {n_pass}/{n_total} match")

    out = {
        'note': 'Day 97 Task A: Master Formula verification at m in {4, 5}',
        'c_vals': c_vals,
        'ms': ms,
        'a_test': a_test,
        'rows': all_rows,
        'fit_summary': fit_summary,
        'n_pass': n_pass,
        'n_total': n_total,
        'all_pass': (n_pass == n_total),
    }
    outpath = '/home/agent/projects/code/2026-07-15-taskA-master-formula.json'
    with open(outpath, 'w') as f:
        json.dump(out, f, indent=2, default=str)
    print(f"\nSaved {outpath}")


if __name__ == "__main__":
    main()
