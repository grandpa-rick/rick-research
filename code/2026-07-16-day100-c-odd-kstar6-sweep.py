"""Day 100 (2026-07-16) — c-odd k*=6 persistence sweep at c ∈ {15, 17, 19}.

Prior data (Day 99):
  c = 11: anchor at (1, 2, j=6, k=6), β'(11) = 12.
  c = 13: anchor at (7, 0, j=6, k=6), β'(13) = 16.

Method:
  For each c ∈ {15, 17, 19}:
    For each k in [0, min(10, c-1)]:
      Fit Q_k^{(c)}(a, b) via bivariate polynomial fit (like crown-jewel).
    For each (a, b, j) in the sweep grid:
      Compute h_k^{(c)}(a, b) = (a+3)_L * (b+2)_L * Q_k^{(c)}(a, b), L = c-1-k.
      Compute H_c(a, b, j) = sum_{k=0}^{j} C(j, k) h_k^{(c)}(a, b).
      Record v_2(H_c(a, b, j)).
  Report the argmin family and check k*=6 uniqueness.
"""

import json
import time
from importlib import util
from math import comb

import sympy as sp

spec = util.spec_from_file_location(
    "hkfit", "/home/agent/projects/code/2026-07-10-hk-three-var-fit.py"
)
hkfit = util.module_from_spec(spec)
spec.loader.exec_module(hkfit)


def v2(n):
    if n == 0:
        return None
    n = abs(int(n))
    v = 0
    while (n & 1) == 0:
        n >>= 1
        v += 1
    return v


def s2(n):
    n = abs(int(n))
    v = 0
    while n:
        v += n & 1
        n >>= 1
    return v


def beta(c):
    return 2 * (c - 1) - s2(c - 1)


def rising_fact(x, n):
    if n <= 0:
        return 1
    p = 1
    for i in range(n):
        p *= (x + i)
    return p


def sample_and_fit_Qk_bivar(c_val, k_target, tables, deg_max_pad=6):
    """Fit Q_k^{(c)}(a, b) as bivariate polynomial. Returns (poly, deg) or None."""
    L = c_val - 1 - k_target
    if L < 0:
        return None
    bd = 2 * (k_target // 2)
    max_deg_try = bd + deg_max_pad
    max_monos = (max_deg_try + 1) * (max_deg_try + 2) // 2
    num_pts_target = max_monos + 20
    samples = []
    a = c_val
    while len(samples) < num_pts_target and a < c_val + 60:
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
                return None
            samples.append((a, b, y // denom))
        a += 1

    a_sym, b_sym = sp.symbols('a b')
    for D in range(bd + deg_max_pad + 1):
        nm = (D + 1) * (D + 2) // 2
        if len(samples) < nm + 3:
            continue
        monomials = [(da, db) for da in range(D + 1) for db in range(D + 1 - da)]
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
            continue
        if len(pivots) != nm:
            continue
        sol = [rref[pivots.index(i), aug.cols - 1] for i in range(nm)]
        poly = 0
        for (da, db), coef in zip(monomials, sol):
            poly += coef * a_sym ** da * b_sym ** db
        poly = sp.expand(poly)
        ok = True
        for (av, bv, yv) in samples:
            if poly.subs({a_sym: av, b_sym: bv}) != yv:
                ok = False
                break
        if not ok:
            continue
        return (poly, D)
    return None


def sweep_c(c_val, ab_max, j_max, k_max, tables):
    """Sweep (a, b, j) and compute v_2(H_c(a, b, j)). Returns records."""
    a_max = ab_max
    b_max = ab_max
    j_hi = min(j_max, c_val - 1)
    k_hi = min(k_max, c_val - 1)
    print(f"\n{'=' * 78}")
    print(f"c = {c_val}, β(c) = {beta(c_val)}, sweep (a,b) in [0,{a_max}]^2, j in [0,{j_hi}]")
    print(f"{'=' * 78}")

    # Fit Q_k for k = 0..k_hi
    a_sym, b_sym = sp.symbols('a b')
    Q_polys = {}
    t0 = time.time()
    for k in range(k_hi + 1):
        r = sample_and_fit_Qk_bivar(c_val, k, tables)
        if r is None:
            print(f"    Q_{k}^({c_val}) fit FAILED — skipping")
            Q_polys[k] = None
        else:
            poly, D = r
            Q_polys[k] = poly
            print(f"    Q_{k}^({c_val}) fit at total deg {D}")
    t_fit = time.time() - t0
    print(f"  Fit time: {t_fit:.1f}s")

    # Precompute h_k lambdas
    h_lam = {}
    for k in range(k_hi + 1):
        if Q_polys[k] is None:
            h_lam[k] = None
            continue
        h_lam[k] = sp.lambdify((a_sym, b_sym), Q_polys[k], modules='math')

    # Sweep
    records = []
    t0 = time.time()
    for a_val in range(0, a_max + 1):
        for b_val in range(0, b_max + 1):
            # Compute h_k values
            hks = {}
            for k in range(k_hi + 1):
                if Q_polys[k] is None:
                    hks[k] = None
                    continue
                L = c_val - 1 - k
                pa = rising_fact(a_val + 3, L)
                pb = rising_fact(b_val + 2, L)
                try:
                    Qv = int(h_lam[k](a_val, b_val))
                except (ValueError, OverflowError):
                    Qv = int(Q_polys[k].subs({a_sym: a_val, b_sym: b_val}))
                hks[k] = pa * pb * Qv
            # Compute H_c(a, b, j) for each j
            for j in range(0, j_hi + 1):
                if any(hks[k] is None for k in range(j + 1)):
                    continue
                Hv = sum(comb(j, k) * hks[k] for k in range(j + 1))
                if Hv == 0:
                    continue
                records.append({'a': a_val, 'b': b_val, 'j': j,
                                'v2': v2(Hv)})
    t_sweep = time.time() - t0
    print(f"  Sweep {len(records)} valid points in {t_sweep:.1f}s")

    if not records:
        return {'c': c_val, 'note': 'no valid H_c', 'records': []}

    min_v = min(r['v2'] for r in records if r['v2'] is not None)
    argmins = [r for r in records if r['v2'] == min_v]
    js_achieving_min = sorted({r['j'] for r in argmins})
    kstar_unique_6 = (js_achieving_min == [6])

    print(f"  β'(c) = min v_2 = {min_v}  (β - {beta(c_val) - min_v})")
    print(f"  # argmins: {len(argmins)}")
    print(f"  j-values achieving min: {js_achieving_min}")
    print(f"  k*=6 uniquely argmin? {kstar_unique_6}")

    print(f"\n  All argmins:")
    for r in sorted(argmins, key=lambda r: (r['j'], r['a'], r['b'])):
        print(f"    (a={r['a']:>2}, b={r['b']:>2}, j={r['j']:>2}, v_2={r['v2']})")

    print(f"\n  Min per j:")
    per_j_min = []
    for j in range(j_hi + 1):
        by_j = [r for r in records if r['j'] == j]
        if not by_j:
            continue
        mn = min(r['v2'] for r in by_j if r['v2'] is not None)
        cnt = sum(1 for r in by_j if r['v2'] == mn)
        first = min([r for r in by_j if r['v2'] == mn], key=lambda r: (r['a'], r['b']))
        per_j_min.append({'j': j, 'min': mn, 'count': cnt, 'first_ab': (first['a'], first['b'])})
        print(f"    j={j:>2}: min v_2 = {mn}, count = {cnt}, first (a,b) = ({first['a']}, {first['b']})")

    return {
        'c': c_val,
        'beta': beta(c_val),
        'a_max': a_max, 'b_max': b_max, 'j_max': j_hi, 'k_max': k_hi,
        'sweep_time_s': t_sweep,
        'fit_time_s': t_fit,
        'min_v2': min_v,
        'js_achieving_min': js_achieving_min,
        'kstar_6_unique': kstar_unique_6,
        'argmins': [{'a': r['a'], 'b': r['b'], 'j': r['j'], 'v2': r['v2']}
                    for r in sorted(argmins, key=lambda r: (r['j'], r['a'], r['b']))],
        'per_j_min': per_j_min,
    }


def main():
    print("=" * 78)
    print("Day 100 (2026-07-16) — c-odd k*=6 persistence sweep")
    print("=" * 78)

    c_vals = [15, 17, 19]
    ab_max = 15
    j_max = 10
    k_max = 10
    tables_max_k = k_max + 2
    t0 = time.time()
    tables = hkfit.build_e2_tables(max_j=tables_max_k + 2)
    print(f"build_e2_tables(max_j={tables_max_k + 2}): {time.time() - t0:.1f}s")

    results = {}
    for c in c_vals:
        results[c] = sweep_c(c, ab_max, j_max, k_max, tables)

    # Summary table
    print("\n" + "=" * 78)
    print("SUMMARY TABLE")
    print("=" * 78)
    header = f"{'c':>3} | {'beta':>5} | {'betaP':>5} | {'j-argmins':>16} | {'k*=6 unique?':>12}"
    print(header)
    print("-" * 60)
    for c in c_vals:
        r = results[c]
        js_str = str(r.get('js_achieving_min', 'N/A'))
        print(f"{c:>3} | {r.get('beta', '-'):>5} | {r.get('min_v2', '-'):>5} | {js_str:>16} | "
              f"{str(r.get('kstar_6_unique', 'N/A')):>12}")

    persistent_all = all(results[c].get('kstar_6_unique', False) for c in c_vals)
    print(f"\nk*=6 persistent across c ∈ {{15, 17, 19}}? {persistent_all}")
    if persistent_all:
        print("→ Combined with Day 99 c ∈ {11, 13}: 5 data points.")
        print("  Registry: c-odd-kstar-6-persistent hunch → 5 pts → threshold for computed.")
    else:
        print("→ k*=6 hunch REFUTED at some c. See details.")

    out = {
        'note': 'Day 100 c-odd k*=6 persistence sweep at c ∈ {15, 17, 19}',
        'date': '2026-07-16',
        'j_max': j_max,
        'ab_max': ab_max,
        'k_max': k_max,
        'per_c': {str(c): results[c] for c in c_vals},
        'kstar_6_persistent_all': persistent_all,
        'prior_data': {
            '11': {'anchor': [1, 2, 6, 6], 'beta_prime': 12},
            '13': {'anchor': [7, 0, 6, 6], 'beta_prime': 16},
        },
    }

    outpath = '/home/agent/projects/code/2026-07-16-day100-c-odd-kstar6-sweep.json'
    with open(outpath, 'w') as f:
        json.dump(out, f, indent=2, default=str)
    print(f"\nSaved {outpath}")

    txtpath = '/home/agent/projects/code/2026-07-16-day100-c-odd-kstar6-sweep.txt'
    with open(txtpath, 'w') as f:
        f.write(f"Day 100 — c-odd k*=6 persistence sweep\n{'=' * 60}\n\n")
        f.write(f"c in {{15, 17, 19}}, (a,b) in [0,{ab_max}]^2, j in [0,{j_max}], k in [0,{k_max}]\n\n")
        f.write(f"{'c':>3} | {'beta':>5} | {'betaP':>5} | {'j-argmins':>18} | {'k*=6 unique?':>12}\n")
        f.write("-" * 70 + "\n")
        for c in c_vals:
            r = results[c]
            js_str = str(r.get('js_achieving_min', 'N/A'))
            f.write(f"{c:>3} | {r.get('beta', '-'):>5} | {r.get('min_v2', '-'):>5} | {js_str:>18} | "
                    f"{str(r.get('kstar_6_unique', 'N/A')):>12}\n")
        f.write(f"\nk*=6 persistent across c ∈ {{15, 17, 19}}? {persistent_all}\n")
    print(f"Saved {txtpath}")


if __name__ == '__main__':
    main()
