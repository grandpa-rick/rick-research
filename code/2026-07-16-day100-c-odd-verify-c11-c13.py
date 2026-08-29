"""Day 100 verification — extend c=11, c=13 sweep to j > 6 to confirm
whether Day 99's β' values were also truncation artefacts.

Day 99 said:
  c=11: β'=12 at (1, 2, j=6).
  c=13: β'=16 at (7, 0, j=6).
Does j=7 (or higher) beat this?
"""

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


def fit_Qk_bivar(c_val, k_target, tables):
    L = c_val - 1 - k_target
    if L < 0:
        return None
    bd = 2 * (k_target // 2)
    max_deg_try = bd + 6
    max_monos = (max_deg_try + 1) * (max_deg_try + 2) // 2
    num_pts_target = max_monos + 20
    samples = []
    a = c_val
    while len(samples) < num_pts_target and a < c_val + 80:
        for b in range(c_val, a + 1):
            hks = hkfit.extract_h_k(a, b, c_val, k_target, tables)
            if hks is None or k_target >= len(hks):
                continue
            y = hks[k_target]
            denom = rising_fact(a + 3, L) * rising_fact(b + 2, L)
            if denom == 0 or y % denom != 0:
                continue
            samples.append((a, b, y // denom))
        a += 1

    a_sym, b_sym = sp.symbols('a b')
    for D in range(bd + 7):
        nm = (D + 1) * (D + 2) // 2
        if len(samples) < nm + 3:
            continue
        monos = [(da, db) for da in range(D + 1) for db in range(D + 1 - da)]
        rows = [[av ** da * bv ** db for (da, db) in monos] for (av, bv, yv) in samples]
        yvals = [yv for (av, bv, yv) in samples]
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
        for (da, db), coef in zip(monos, sol):
            poly += coef * a_sym ** da * b_sym ** db
        poly = sp.expand(poly)
        ok = all(poly.subs({a_sym: av, b_sym: bv}) == yv for (av, bv, yv) in samples)
        if not ok:
            continue
        return poly
    return None


def sweep_c_full(c_val, ab_max, k_max, j_max, tables):
    a_sym, b_sym = sp.symbols('a b')
    Q_polys = {}
    for k in range(k_max + 1):
        Q_polys[k] = fit_Qk_bivar(c_val, k, tables)

    records = []
    for a_val in range(0, ab_max + 1):
        for b_val in range(0, ab_max + 1):
            hks = {}
            for k in range(k_max + 1):
                if Q_polys[k] is None:
                    hks[k] = None
                    continue
                L = c_val - 1 - k
                pa = rising_fact(a_val + 3, L)
                pb = rising_fact(b_val + 2, L)
                Qv = int(Q_polys[k].subs({a_sym: a_val, b_sym: b_val}))
                hks[k] = pa * pb * Qv
            for j in range(0, j_max + 1):
                if any(hks[k] is None for k in range(j + 1)):
                    continue
                Hv = sum(comb(j, k) * hks[k] for k in range(j + 1))
                if Hv == 0:
                    continue
                records.append({'a': a_val, 'b': b_val, 'j': j, 'v2': v2(Hv)})
    return records


def summarize(c_val, records):
    print(f"\nc = {c_val}, β(c) = {beta(c_val)}")
    if not records:
        print("  (no records)")
        return
    min_v = min(r['v2'] for r in records)
    argmins = [r for r in records if r['v2'] == min_v]
    js = sorted({r['j'] for r in argmins})
    print(f"  β'(c) = {min_v}, deficit = {beta(c_val) - min_v}")
    print(f"  argmin j-values: {js}")
    print(f"  # argmins: {len(argmins)}")
    for r in sorted(argmins, key=lambda r: (r['j'], r['a'], r['b']))[:10]:
        print(f"    (a={r['a']:>2}, b={r['b']:>2}, j={r['j']:>2}, v_2={r['v2']})")

    # min per j
    for j in sorted({r['j'] for r in records}):
        by_j = [r for r in records if r['j'] == j]
        mn = min(r['v2'] for r in by_j)
        cnt = sum(1 for r in by_j if r['v2'] == mn)
        first = min([r for r in by_j if r['v2'] == mn], key=lambda r: (r['a'], r['b']))
        print(f"    j={j:>2}: min = {mn}, count = {cnt}, first (a,b) = ({first['a']}, {first['b']})")


def main():
    print("=" * 78)
    print("Day 100 verification — extend c=11, c=13 to j ∈ [0, 10]")
    print("=" * 78)
    tables = hkfit.build_e2_tables(max_j=12)
    t0 = time.time()
    for c in [11, 13]:
        print(f"\n{'=' * 60}")
        print(f"Sweeping c = {c}")
        print(f"{'=' * 60}")
        records = sweep_c_full(c, ab_max=15, k_max=10, j_max=10, tables=tables)
        summarize(c, records)
    print(f"\ntotal wall {time.time()-t0:.1f}s")


if __name__ == '__main__':
    main()
