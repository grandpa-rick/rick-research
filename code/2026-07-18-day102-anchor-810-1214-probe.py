"""Day 102 (2026-07-18) — probe anchor-810 and anchor-1214 families.

Meta-conjecture (Day 102 primary):
  For each R in {2, 6, 10, 14}, the anchor family (a_R, b_R, j_R) = (R-2, R, 2R)
  gives delta_R(c) = max(0, v_2(c - R) - 3) at c ≡ R mod 16.

Confirmed for R = 6 (Day 100/101 anchor-46 family, 11 pts).
Test R = 10: (8, 10, j=20) at c ≡ 10 mod 16.
Test R = 14: (12, 14, j=28) at c ≡ 14 mod 16.

Pick c values with variety of v_2(c - R):
  R = 10, c ≡ 10 mod 16:
    c = 42:  v_2(32) = 5   -> predict delta = 2
    c = 74:  v_2(64) = 6   -> predict delta = 3
    c = 138: v_2(128) = 7  -> predict delta = 4
    c = 154: v_2(144) = 4  -> predict delta = 1
    c = 170: v_2(160) = 5  -> predict delta = 2
  R = 14, c ≡ 14 mod 16:
    c = 46:  v_2(32) = 5   -> predict delta = 2
    c = 78:  v_2(64) = 6   -> predict delta = 3
    c = 142: v_2(128) = 7  -> predict delta = 4
    c = 158: v_2(144) = 4  -> predict delta = 1
    c = 174: v_2(160) = 5  -> predict delta = 2

For (8,10) family, we need k_max = 20 (j=20 needs Q_0..Q_20).
For (12,14) family, we need k_max = 28.

Fitting Q_k at large k is expensive: Q_k polynomial in (a,b) has degree ~ 2*(k//2)
so k=20 -> deg ~ 20. Fit needs many samples. May take substantial time.
Reduce budget by fitting one k at a time, storing results.
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


def delta_c2mod4(c):
    """Δ(c) = s_2(m) + v_2(m), m = (c-2)/4.  For c ≡ 2 mod 4."""
    assert c % 4 == 2
    m = (c - 2) // 4
    return s2(m) + v2(m)


def rising_fact(x, n):
    if n <= 0:
        return 1
    p = 1
    for i in range(n):
        p *= (x + i)
    return p


def fit_Qk_bivar(c_val, k_target, tables, deg_max_pad=6):
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
        return (poly, D)
    return None


def compute_H_at(c, a_val, b_val, j_val, k_max, tables):
    """Compute v_2 of H_c(a, b, j) at (a_val, b_val, j_val).
    Fit Q_k for k=0..k_max, evaluate at (a_val, b_val), assemble h_k, sum C(j,k)h_k."""
    a_sym, b_sym = sp.symbols('a b')
    Q_polys = {}
    t0 = time.time()
    for k in range(k_max + 1):
        r = fit_Qk_bivar(c, k, tables)
        if r is None:
            return None, None, time.time() - t0, f"fit failed at k={k}"
        Q_polys[k] = r[0]
    t_fit = time.time() - t0

    hks = {}
    for k in range(k_max + 1):
        L = c - 1 - k
        pa = rising_fact(a_val + 3, L)
        pb = rising_fact(b_val + 2, L)
        Qv = int(Q_polys[k].subs({a_sym: a_val, b_sym: b_val}))
        hks[k] = pa * pb * Qv

    Hv = sum(comb(j_val, k) * hks[k] for k in range(j_val + 1))
    if Hv == 0:
        return None, None, t_fit, "H_c = 0"
    return Hv, v2(Hv), t_fit, "ok"


def main():
    print("=" * 78)
    print("Day 102 — anchor-810 and anchor-1214 probe")
    print("=" * 78, flush=True)

    tests = [
        # R = 10 (c ≡ 10 mod 16), test (8, 10, j=20)
        {'c': 42, 'anchor': (8, 10, 20), 'k_max': 20, 'R': 10},
        {'c': 74, 'anchor': (8, 10, 20), 'k_max': 20, 'R': 10},
        {'c': 138, 'anchor': (8, 10, 20), 'k_max': 20, 'R': 10},
        {'c': 154, 'anchor': (8, 10, 20), 'k_max': 20, 'R': 10},
        # R = 14 (c ≡ 14 mod 16), test (12, 14, j=28)
        {'c': 46, 'anchor': (12, 14, 28), 'k_max': 28, 'R': 14},
        {'c': 78, 'anchor': (12, 14, 28), 'k_max': 28, 'R': 14},
        {'c': 142, 'anchor': (12, 14, 28), 'k_max': 28, 'R': 14},
        {'c': 158, 'anchor': (12, 14, 28), 'k_max': 28, 'R': 14},
    ]

    # Build tables large enough for k_max = 28
    K_MAX_GLOBAL = 28
    t0 = time.time()
    tables = hkfit.build_e2_tables(max_j=K_MAX_GLOBAL + 2)
    print(f"build_e2_tables(max_j={K_MAX_GLOBAL + 2}): {time.time() - t0:.1f}s", flush=True)

    OVERALL_BUDGET_S = 3300
    t_global = time.time()

    results = []
    for t in tests:
        elapsed = time.time() - t_global
        if elapsed > OVERALL_BUDGET_S:
            print(f"[BUDGET] stop before c={t['c']}, elapsed {elapsed:.1f}s")
            break
        c = t['c']
        (a_val, b_val, j_val) = t['anchor']
        R = t['R']
        print(f"\n--- c = {c} (R={R}, anchor = ({a_val},{b_val},j={j_val})) ---", flush=True)
        beta_c = beta(c)
        Delta_c = delta_c2mod4(c)
        u_c = beta_c - Delta_c
        v2_cR = v2(c - R)
        predicted_delta = max(0, v2_cR - 3)
        print(f"  beta = {beta_c}, D_02 = {Delta_c}, u_c = {u_c}", flush=True)
        print(f"  v_2(c - {R}) = {v2_cR}, predicted delta = max(0, {v2_cR}-3) = {predicted_delta}", flush=True)

        Hv, v2_H, t_fit, status = compute_H_at(c, a_val, b_val, j_val, t['k_max'], tables)
        if v2_H is None:
            print(f"  {status} (t_fit={t_fit:.1f}s)")
            results.append({'c': c, 'R': R, 'v2_H': None, 'predicted_delta': predicted_delta,
                            'actual_delta': None, 'status': status, 't_fit': t_fit})
            continue
        actual_delta = u_c - v2_H
        match = actual_delta == predicted_delta
        print(f"  v_2(H_c({a_val},{b_val},{j_val})) = {v2_H}", flush=True)
        print(f"  actual delta = u_c - v_2 = {u_c} - {v2_H} = {actual_delta}", flush=True)
        print(f"  MATCH: {match}   (t_fit={t_fit:.1f}s)", flush=True)
        results.append({
            'c': c, 'R': R, 'anchor': [a_val, b_val, j_val],
            'beta_c': beta_c, 'D_02': Delta_c, 'u_c': u_c,
            'v2_c_minus_R': v2_cR, 'predicted_delta': predicted_delta,
            'v2_H': v2_H, 'actual_delta': actual_delta, 'match': match,
            't_fit': t_fit, 'status': status,
        })

    # Summary
    print("\n" + "=" * 78)
    print("SUMMARY — anchor-810 and anchor-1214 probe (Day 102)")
    print("=" * 78)
    print(f"{'c':>4} | {'R':>3} | {'(a,b,j)':>10} | {'v_2(c-R)':>8} | {'pred':>4} | {'actual':>6} | {'match':>5}")
    matches = 0
    predicted_positive = 0
    for r in results:
        if r['actual_delta'] is None:
            print(f"{r['c']:>4} | {r['R']:>3} | ...         | ??      | ??   | FAIL   | -    ({r['status']})")
            continue
        anchor_s = f"({r['anchor'][0]},{r['anchor'][1]},{r['anchor'][2]})"
        print(f"{r['c']:>4} | {r['R']:>3} | {anchor_s:>10} | {r['v2_c_minus_R']:>8} | "
              f"{r['predicted_delta']:>4} | {r['actual_delta']:>6} | {str(r['match']):>5}")
        if r['match']:
            matches += 1
        if r['predicted_delta'] > 0:
            predicted_positive += 1
    print()
    print(f"Matches: {matches}/{len(results)}")
    print(f"Predicted-positive: {predicted_positive}/{len(results)}")

    verdict = None
    valid = [r for r in results if r['actual_delta'] is not None]
    if len(valid) == 0:
        verdict = "NO DATA — all fits failed"
    elif all(r['match'] for r in valid):
        verdict = f"CLEAN — {len(valid)}/{len(valid)} match the meta-conjecture delta_R(c) = max(0, v_2(c-R) - 3)"
    else:
        verdict = f"MIXED — {matches}/{len(valid)} match"
    print(f"VERDICT: {verdict}")

    out = {
        'note': 'Day 102 anchor-810 / anchor-1214 meta-conjecture probe',
        'date': '2026-07-18',
        'tests': tests,
        'results': results,
        'matches': matches,
        'total': len(results),
        'verdict': verdict,
        'wall_s': time.time() - t_global,
    }
    outpath = '/home/agent/projects/code/2026-07-18-day102-anchor-810-1214-probe.json'
    with open(outpath, 'w') as f:
        json.dump(out, f, indent=2, default=str)
    print(f"\nSaved {outpath}")


if __name__ == '__main__':
    main()
