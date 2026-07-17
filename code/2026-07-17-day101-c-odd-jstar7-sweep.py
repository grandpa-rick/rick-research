"""Day 101 (2026-07-17) — c-odd j* = 7 verification sweep.

Day 99 found that at c-odd (c ∈ {11, 13, 15}), the argmin j often was j=7.
Day 100's β'(15) truncation-artefact fix: extend catalog and j up to at
least 7 to catch the true minimum. Register `c-odd-jstar-7` hunch.

This cycle: sweep c ∈ {21, 23, 25, 27, 29}, (a, b) ∈ [0, min(15, c-1)]^2,
j ∈ [0, min(12, c-1)], k ∈ [0, min(10, c-1)].

For each c:
  1. Fit Q_k^{(c)}(a, b) for k = 0..k_max.
  2. Compute h_k(a, b) = (a+3)_L (b+2)_L Q_k(a, b).
  3. H_c(a, b, j) = sum_{k=0}^j C(j, k) h_k(a, b).
  4. Report β'(c) = min v_2(H_c(a, b, j)) and argmin (a*, b*, j*).
Question: is j = 7 in the argmin set for every c odd ≥ 15?
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


def fit_Qk_bivar(c_val, k_target, tables, deg_max_pad=6):
    L = c_val - 1 - k_target
    if L < 0:
        return None
    bd = 2 * (k_target // 2)
    max_deg_try = bd + deg_max_pad
    max_monos = (max_deg_try + 1) * (max_deg_try + 2) // 2
    num_pts_target = max_monos + 20
    samples = []
    a = c_val
    while len(samples) < num_pts_target and a < c_val + 80:
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
        return poly
    return None


def process_c(c, ab_max, j_max, k_max, tables):
    a_sym, b_sym = sp.symbols('a b')
    print(f"\n{'-' * 78}\nc = {c}  β(c) = {beta(c)}", flush=True)
    parity = c % 2

    t0 = time.time()
    Q_polys = {}
    for k in range(k_max + 1):
        r = fit_Qk_bivar(c, k, tables)
        Q_polys[k] = r
    t_fit = time.time() - t0
    print(f"  Fit Q_k for k=0..{k_max}: {t_fit:.1f}s  (available: "
          f"{[k for k in Q_polys if Q_polys[k] is not None]})", flush=True)

    # Precompute h_k for all (a, b) in the box
    ab_max_eff = min(ab_max, c - 1) if c > 0 else ab_max
    j_max_eff = min(j_max, c - 1)

    # For each (a, b), for each k, compute h_k(a, b)
    hks_lookup = {}
    for a_val in range(ab_max_eff + 1):
        for b_val in range(ab_max_eff + 1):
            if (a_val + b_val) % 2 != parity:
                continue
            hk_arr = []
            for k in range(k_max + 1):
                if Q_polys[k] is None:
                    hk_arr.append(None)
                    continue
                L = c - 1 - k
                if L < 0:
                    hk_arr.append(0)
                    continue
                pa = rising_fact(a_val + 3, L)
                pb = rising_fact(b_val + 2, L)
                Qv = int(Q_polys[k].subs({a_sym: a_val, b_sym: b_val}))
                hk_arr.append(pa * pb * Qv)
            hks_lookup[(a_val, b_val)] = hk_arr

    # For each (a, b, j), compute H_c and v_2
    records = []
    for (a_val, b_val), hk_arr in hks_lookup.items():
        for j in range(j_max_eff + 1):
            if j > k_max:
                break
            if any(hk_arr[k] is None for k in range(j + 1)):
                continue
            Hv = sum(comb(j, k) * hk_arr[k] for k in range(j + 1))
            if Hv == 0:
                continue
            records.append({'a': a_val, 'b': b_val, 'j': j, 'v2': v2(Hv)})

    # Global min
    if not records:
        return {'c': c, 'no_data': True}
    min_v = min(r['v2'] for r in records)
    argmins = [r for r in records if r['v2'] == min_v]
    j_set = sorted(set(r['j'] for r in argmins))

    # Per j min
    per_j_min = {}
    for j in range(j_max_eff + 1):
        by_j = [r for r in records if r['j'] == j]
        if not by_j:
            continue
        m = min(r['v2'] for r in by_j)
        per_j_min[j] = m

    print(f"  β'(c) = {min_v}  (β(c) - β' = {beta(c) - min_v})", flush=True)
    print(f"  Argmin j-set: {j_set}", flush=True)
    print(f"  First 10 argmins:", flush=True)
    for r in sorted(argmins, key=lambda r: (r['j'], r['a'], r['b']))[:10]:
        print(f"    (a={r['a']:>2}, b={r['b']:>2}, j={r['j']}, v_2={r['v2']})", flush=True)
    print(f"  Per-j min:", flush=True)
    for j in sorted(per_j_min):
        marker = ' <-- global min' if per_j_min[j] == min_v else ''
        print(f"    j={j:>2}: min v_2 = {per_j_min[j]}{marker}", flush=True)

    return {
        'c': c,
        'beta_c': beta(c),
        'beta_prime': min_v,
        'argmin_j_set': j_set,
        'argmin_count': len(argmins),
        'argmins_first_10': [(r['a'], r['b'], r['j'], r['v2']) for r in
                             sorted(argmins, key=lambda r: (r['j'], r['a'], r['b']))[:10]],
        'per_j_min': per_j_min,
        'j_7_in_argmin_set': 7 in j_set,
        'fit_time_s': t_fit,
    }


def main():
    print("=" * 78)
    print("Day 101 — c-odd j* = 7 verification sweep")
    print("=" * 78, flush=True)

    c_vals = [21, 23, 25, 27, 29]
    ab_max = 15
    j_max = 12
    k_max = 12

    t0 = time.time()
    tables = hkfit.build_e2_tables(max_j=k_max + 2)
    print(f"build_e2_tables(max_j={k_max + 2}): {time.time() - t0:.1f}s", flush=True)

    all_records = []
    t_global = time.time()
    for c in c_vals:
        try:
            rec = process_c(c, ab_max, j_max, k_max, tables)
            all_records.append(rec)
        except Exception as e:
            print(f"  ERROR at c={c}: {e}")

    # Summary
    print("\n" + "=" * 78)
    print("SUMMARY — c-odd j* verification")
    print("=" * 78)
    print(f"{'c':>4} | {'β(c)':>5} | {'bprime':>7} | {'j-set':>15} | {'j=7?':>5}")

    j7_count = 0
    exceptions = []
    for r in all_records:
        if r.get('no_data'):
            print(f"{r['c']:>4} | (no data)")
            continue
        j_set_str = str(r['argmin_j_set'])
        j7_marker = 'YES' if r['j_7_in_argmin_set'] else 'NO'
        if r['j_7_in_argmin_set']:
            j7_count += 1
        else:
            exceptions.append((r['c'], r['argmin_j_set']))
        print(f"{r['c']:>4} | {r['beta_c']:>5} | {r['beta_prime']:>7} | {j_set_str:>15} | {j7_marker:>5}")

    # Prior data from Day 99, 100 registry mentions
    prior = [
        {'c': 15, 'j7_in_argmin': True, 'note': 'Day 100 β\'(15) = 19 at j=7'},
        {'c': 17, 'j7_in_argmin': None, 'note': 'TBD from registry check'},
        {'c': 19, 'j7_in_argmin': None, 'note': 'TBD'},
    ]
    print(f"\nJ=7 confirmations this cycle: {j7_count}/{len(all_records)}")
    if exceptions:
        print(f"EXCEPTIONS: {exceptions}")

    out = {
        'note': 'Day 101 c-odd j*=7 verification sweep',
        'date': '2026-07-17',
        'c_vals': c_vals,
        'ab_max': ab_max,
        'j_max': j_max,
        'k_max': k_max,
        'per_c': all_records,
        'j7_count': j7_count,
        'exceptions': exceptions,
        'prior_from_day99_100': prior,
    }
    with open('/home/agent/projects/code/2026-07-17-day101-c-odd-jstar7-sweep.json', 'w') as f:
        json.dump(out, f, indent=2, default=str)
    print("\nSaved.")


if __name__ == '__main__':
    main()
