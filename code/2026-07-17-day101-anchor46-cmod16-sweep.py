"""Day 101 (2026-07-17) — anchor-46 c ≡ 6 mod 16 growth sweep.

Goal: grow `anchor-46-beats-02-at-c-mod-16-eq-6` from 5 → ≥ 8 data points.

Prior data (Day 100 anchor-neighbourhood sweep, c ∈ {134, 150, 166, 182, 198}):
  All show (4, 6, j=12) v_2 < u(c) = β(c) − Δ(c), delta 1..4.

This cycle: c ∈ {118, 214, 230, 246, 262, 278}.
  All c ≡ 6 mod 16.
  c = 262 has v_2(c - 6) = v_2(256) = 8 (ANOMALOUS v_2 — good anomaly sample!).

For each c:
  1. Compute u(c) = β(c) − Δ(c), Δ(c) = s_2(m) + v_2(m), m = (c-2)/4.
  2. Sweep (a, b) ∈ {(4, 6), (5, 5), (5, 7), (6, 6)}, j ∈ [8, 16].
  3. Report v_2(H_c(a, b, j)) and delta = u(c) − v_2.
  4. Compute v_2(c - i) for i ∈ {2, 4, 6, 8, 10, 12} — anomaly signal.

If 3/3 new anchor-violation confirmations at (4, 6, j=12):
  hunch 5/10 → 8/10.
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
    """Fit Q_k^{(c)}(a, b) as bivariate polynomial. Returns sympy poly or None."""
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


def process_c(c, ab_targets, j_range, k_max, tables):
    """For each (a, b) target, compute v_2(H_c(a, b, j)) for j in j_range."""
    a_sym, b_sym = sp.symbols('a b')
    print(f"\n{'-' * 78}\nc = {c}", flush=True)
    assert c % 16 == 6, f"c={c} must be ≡ 6 mod 16"

    beta_c = beta(c)
    Delta_c = delta_c2mod4(c)
    u_c = beta_c - Delta_c
    print(f"  β(c) = {beta_c}, Δ(c) = {Delta_c}, u(c) = {u_c} (anchor (0, 2) UB)", flush=True)

    v2_c_minus = {i: v2(c - i) for i in range(1, 15)}
    print(f"  v_2(c - i) i=1..14: {v2_c_minus}", flush=True)

    t0 = time.time()
    Q_polys = {}
    for k in range(k_max + 1):
        r = fit_Qk_bivar(c, k, tables)
        Q_polys[k] = r[0] if r is not None else None
    t_fit = time.time() - t0
    print(f"  Fit Q_k for k=0..{k_max}: {t_fit:.1f}s", flush=True)

    # Precompute h_k^{(c)}(a, b) = pa * pb * Q_k(a, b) for each (a, b) target
    ab_records = []
    for (a_val, b_val) in ab_targets:
        if (a_val + b_val) % 2 != c % 2:
            print(f"    ({a_val},{b_val}) parity mismatch — skip")
            continue
        hks = {}
        for k in range(k_max + 1):
            if Q_polys[k] is None:
                hks[k] = None
                continue
            L = c - 1 - k
            pa = rising_fact(a_val + 3, L)
            pb = rising_fact(b_val + 2, L)
            Qv = int(Q_polys[k].subs({a_sym: a_val, b_sym: b_val}))
            hks[k] = pa * pb * Qv

        # Compute H_c(a, b, j) for j in j_range
        j_vals = []
        for j in j_range:
            if j > k_max:
                break
            if any(hks[k] is None for k in range(j + 1)):
                j_vals.append((j, None, None))
                continue
            Hv = sum(comb(j, k) * hks[k] for k in range(j + 1))
            if Hv == 0:
                j_vals.append((j, 0, None))
                continue
            j_vals.append((j, Hv, v2(Hv)))

        # Min over j_range
        valid = [(j, vv) for (j, _, vv) in j_vals if vv is not None]
        if valid:
            best_j, best_v = min(valid, key=lambda x: x[1])
            delta = u_c - best_v
        else:
            best_j, best_v, delta = None, None, None

        ab_records.append({
            'a': a_val,
            'b': b_val,
            'j_vals': [(j, str(vv)) for (j, _, vv) in j_vals],
            'best_j': best_j,
            'best_v2': best_v,
            'delta': delta,
        })
        print(f"    (a, b) = ({a_val:>2},{b_val:>2}):  best_j = {best_j}, "
              f"v_2 = {best_v}, delta = {delta}", flush=True)

    # Focus on (4, 6) at j=12 specifically
    r46 = None
    for r in ab_records:
        if (r['a'], r['b']) == (4, 6):
            for (j, vv) in r['j_vals']:
                if j == 12:
                    r46 = {'j': j, 'v2': vv, 'delta': u_c - int(vv) if vv != 'None' and vv is not None else None}
                    break
    print(f"  (4, 6, j=12): {r46}", flush=True)

    return {
        'c': c,
        'beta_c': beta_c,
        'Delta_c': Delta_c,
        'u_c': u_c,
        'v2_c_minus_i': v2_c_minus,
        'ab_records': ab_records,
        'r46_j12': r46,
        'fit_time_s': t_fit,
    }


def main():
    print("=" * 78)
    print("Day 101 — anchor-46 c ≡ 6 mod 16 growth sweep")
    print("=" * 78, flush=True)

    c_vals = [118, 214, 230, 246, 262, 278]
    for c in c_vals:
        assert c % 16 == 6, f"c = {c} not ≡ 6 mod 16"

    ab_targets = [(4, 6), (5, 5), (5, 7), (6, 6)]
    j_range = list(range(8, 17))
    k_max = 16  # need up to k = 16 (max j)

    t0 = time.time()
    tables = hkfit.build_e2_tables(max_j=k_max + 2)
    print(f"build_e2_tables(max_j={k_max + 2}): {time.time() - t0:.1f}s", flush=True)

    OVERALL_BUDGET_S = 2400
    t_global = time.time()

    all_records = []
    for c in c_vals:
        if time.time() - t_global > OVERALL_BUDGET_S:
            print(f"[BUDGET] stop before c={c}")
            break
        try:
            rec = process_c(c, ab_targets, j_range, k_max, tables)
            all_records.append(rec)
        except Exception as e:
            print(f"  ERROR at c={c}: {e}")

    print("\n" + "=" * 78)
    print("SUMMARY — anchor-46 c ≡ 6 mod 16 (4, 6, j=12) vs (0, 2) anchor")
    print("=" * 78)
    print(f"{'c':>4} | {'u(c)':>5} | {'(4,6,12).v_2':>12} | {'delta':>5} | {'v_2(c-6)':>8}")

    confirmations = 0
    exceptions = []
    per_c_summary = []
    for r in all_records:
        r46 = r['r46_j12']
        v2c6 = r['v2_c_minus_i'].get(6, None)
        if r46 and r46['delta'] is not None:
            v46 = r46['v2']
            delta = r46['delta']
            if delta > 0:
                confirmations += 1
                status = 'CONFIRM'
            else:
                exceptions.append((r['c'], delta))
                status = 'EXCEPTION'
        else:
            v46, delta, status = None, None, 'NO DATA'
        print(f"{r['c']:>4} | {r['u_c']:>5} | {str(v46):>12} | {str(delta):>5} | {str(v2c6):>8}  {status}")
        per_c_summary.append({
            'c': r['c'], 'u_c': r['u_c'],
            'v46_j12': v46, 'delta': delta,
            'v2_c_minus_6': v2c6,
            'status': status,
        })

    print(f"\nConfirmations: {confirmations}/{len(all_records)}")
    if exceptions:
        print(f"EXCEPTIONS: {exceptions}")

    # Cross-c pattern: does delta scale with v_2(c - i) for some i?
    print(f"\nAnomaly signal — v_2(c - i) at each c (i=2..12):")
    print(f"{'c':>4} | " + " | ".join(f'i={i:>2}' for i in range(2, 13)))
    for r in all_records:
        row = [f"{r['v2_c_minus_i'].get(i, '-'):>3}" for i in range(2, 13)]
        print(f"{r['c']:>4} | " + " | ".join(row))

    prior_data = [
        {'c': 134, 'v46_j12': 257, 'u_c': 261, 'delta': 4},
        {'c': 150, 'v46_j12': 290, 'u_c': 291, 'delta': 1},
        {'c': 166, 'v46_j12': 321, 'u_c': 323, 'delta': 2},
        {'c': 182, 'v46_j12': 352, 'u_c': 353, 'delta': 1},
        {'c': 198, 'v46_j12': 384, 'u_c': 387, 'delta': 3},
    ]
    total_confirmations = confirmations + len(prior_data)

    verdict_lines = []
    if confirmations == len(all_records):
        verdict_lines.append(f'CLEAN — {confirmations}/{len(all_records)} new c-values confirm (4,6,j=12) beats (0,2)')
        verdict_lines.append(f'Total confirmations (prior + new): {total_confirmations}')
    else:
        verdict_lines.append(f'MIXED — {confirmations}/{len(all_records)} confirmations; {len(exceptions)} exceptions')

    for line in verdict_lines:
        print(line)

    out = {
        'note': 'Day 101 anchor-46 c ≡ 6 mod 16 growth sweep',
        'date': '2026-07-17',
        'c_vals': c_vals,
        'ab_targets': [list(t) for t in ab_targets],
        'j_range': j_range,
        'per_c_full': all_records,
        'per_c_summary': per_c_summary,
        'prior_data_from_day100': prior_data,
        'confirmations_this_cycle': confirmations,
        'total_confirmations_all_cycles': total_confirmations,
        'exceptions': exceptions,
        'verdict': verdict_lines,
        'total_wall_s': time.time() - t_global,
    }
    outpath = '/home/agent/projects/code/2026-07-17-day101-anchor46-cmod16-sweep.json'
    with open(outpath, 'w') as f:
        json.dump(out, f, indent=2, default=str)
    print(f"\nSaved {outpath}")

    txtpath = '/home/agent/projects/code/2026-07-17-day101-anchor46-cmod16-sweep.txt'
    with open(txtpath, 'w') as f:
        f.write("Day 101 — anchor-46 c ≡ 6 mod 16 growth sweep\n")
        f.write("=" * 60 + "\n\n")
        f.write(f"c_vals (new): {c_vals}\n")
        f.write(f"(a, b) targets: {ab_targets}\n")
        f.write(f"j_range: {j_range}\n\n")
        f.write(f"{'c':>4} | {'u(c)':>5} | {'(4,6,12).v_2':>12} | {'delta':>5} | {'v_2(c-6)':>8}  status\n")
        for s in per_c_summary:
            f.write(f"{s['c']:>4} | {s['u_c']:>5} | {str(s['v46_j12']):>12} | "
                    f"{str(s['delta']):>5} | {str(s['v2_c_minus_6']):>8}  {s['status']}\n")
        f.write(f"\nConfirmations this cycle: {confirmations}/{len(all_records)}\n")
        f.write(f"Total confirmations (prior + this): {total_confirmations}\n")
        f.write("\nPrior Day 100 data:\n")
        for p in prior_data:
            f.write(f"  c={p['c']}: v_2=(4,6,12)={p['v46_j12']}, u(c)={p['u_c']}, delta={p['delta']}\n")
        for line in verdict_lines:
            f.write(f"\n{line}")
    print(f"Saved {txtpath}")


if __name__ == '__main__':
    main()
