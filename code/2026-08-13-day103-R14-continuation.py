"""Day 103 (2026-08-13) — continuation of Day 102 R=14 probe + R=6 sanity check.

Context: Day 102 c=46 fit (R=14, k_max=28) took 10573s (~3 hours).
Budget for this run: ~4 hours total wall-time.

Plan:
  1. Fast R=6 sanity control: c = 294 (v_2(288) = 5, predicted δ = 2 for ε_6=3).
     Should take ~40s per Day 101 timings.
  2. R=14 continuation: c = 78 (v_2(64) = 6). Under ε_14 = 4 (current hypothesis),
     predicted δ = 2. Under ε_14 = 5 (H1), predicted δ = 1. Discriminates ε_14
     between 4 and 5.
  3. If time budget allows (>1.5h remaining after c=78), also attempt c = 158
     (v_2(144) = 4). Under ε_14=4, predicted δ = 0. Under ε_14=3, predicted δ=1.

Writes results incrementally to JSON after each c-value in case of budget stop.
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


def compute_H_at(c, a_val, b_val, j_val, k_max, tables, verbose=True):
    a_sym, b_sym = sp.symbols('a b')
    Q_polys = {}
    t0 = time.time()
    for k in range(k_max + 1):
        tk = time.time()
        r = fit_Qk_bivar(c, k, tables)
        if r is None:
            return None, None, time.time() - t0, f"fit failed at k={k}", {}
        Q_polys[k] = r[0]
        if verbose:
            print(f"    Q_{k} fit deg={r[1]} in {time.time()-tk:.1f}s (cum {time.time()-t0:.1f}s)", flush=True)
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
        return None, None, t_fit, "H_c = 0", hks
    return Hv, v2(Hv), t_fit, "ok", hks


OUT_PATH = '/home/agent/projects/code/2026-08-13-day103-R14-continuation.json'


def save_incremental(state):
    with open(OUT_PATH, 'w') as f:
        json.dump(state, f, indent=2, default=str)


def main():
    print("=" * 78)
    print("Day 103 — R=14 continuation + R=6 sanity check")
    print("=" * 78, flush=True)

    # Sequence: fast sanity first, then the expensive R=14 probe.
    tests = [
        {'c': 294, 'anchor': (4, 6, 12),   'k_max': 12, 'R': 6,  'label': 'R6-sanity'},
        {'c': 78,  'anchor': (12, 14, 28), 'k_max': 28, 'R': 14, 'label': 'R14-probe-1'},
        {'c': 158, 'anchor': (12, 14, 28), 'k_max': 28, 'R': 14, 'label': 'R14-probe-2'},
    ]

    K_MAX_GLOBAL = 28
    t0 = time.time()
    tables = hkfit.build_e2_tables(max_j=K_MAX_GLOBAL + 2)
    print(f"build_e2_tables(max_j={K_MAX_GLOBAL + 2}): {time.time() - t0:.1f}s", flush=True)

    OVERALL_BUDGET_S = 3.5 * 3600  # 3.5 hours, leaves 30min buffer
    t_global = time.time()

    state = {
        'note': 'Day 103 R=14 continuation + R=6 sanity check',
        'date': '2026-08-13',
        'budget_s': OVERALL_BUDGET_S,
        'tests_planned': tests,
        'results': [],
        'status': 'running',
        'started': time.strftime('%Y-%m-%d %H:%M:%S'),
    }
    save_incremental(state)

    for t in tests:
        elapsed = time.time() - t_global
        remaining = OVERALL_BUDGET_S - elapsed
        c = t['c']
        # R=14 costs ~3h. Skip if remaining < 3.2h.
        if t['R'] == 14 and remaining < 3.2 * 3600:
            print(f"[BUDGET] skip c={c} (R=14) — need ~3.2h, have {remaining/3600:.2f}h")
            state['results'].append({'c': c, 'R': t['R'], 'skipped': True,
                                     'reason': f'budget: {remaining/3600:.2f}h remaining'})
            save_incremental(state)
            continue
        if remaining < 60:
            print(f"[BUDGET] stop before c={c}, elapsed {elapsed:.1f}s")
            break
        (a_val, b_val, j_val) = t['anchor']
        R = t['R']
        print(f"\n--- c={c} (R={R}, anchor=({a_val},{b_val},{j_val}), k_max={t['k_max']}) [{t['label']}] ---", flush=True)
        beta_c = beta(c)
        Delta_c = delta_c2mod4(c)
        u_c = beta_c - Delta_c
        v2_cR = v2(c - R)
        print(f"  beta={beta_c}, D_02={Delta_c}, u_c={u_c}, v_2(c-{R})={v2_cR}", flush=True)

        t_start = time.time()
        Hv, v2_H, t_fit, status, hks = compute_H_at(c, a_val, b_val, j_val, t['k_max'], tables,
                                                    verbose=(t['R'] == 14))
        t_c = time.time() - t_start
        result = {
            'c': c, 'R': R, 'anchor': [a_val, b_val, j_val], 'label': t['label'],
            'beta_c': beta_c, 'D_02': Delta_c, 'u_c': u_c,
            'v2_c_minus_R': v2_cR,
            't_fit_s': t_fit, 't_total_s': t_c, 'status': status,
        }
        if v2_H is None:
            print(f"  FAIL: {status} (t={t_c:.1f}s)", flush=True)
            result['v2_H'] = None
            result['actual_delta'] = None
        else:
            actual_delta = u_c - v2_H
            # Compute inferred epsilon: if delta = max(0, v2_cR - eps), and delta>0,
            # then eps = v2_cR - actual_delta.
            if actual_delta > 0:
                inferred_eps = v2_cR - actual_delta
            elif v2_cR is None:
                inferred_eps = None
            else:
                # delta=0 means eps >= v2_cR (only a lower bound)
                inferred_eps = f">={v2_cR}"
            print(f"  v_2(H)={v2_H}, actual_delta={actual_delta}, inferred_eps={inferred_eps} (t={t_c:.1f}s)", flush=True)
            result['v2_H'] = v2_H
            result['actual_delta'] = actual_delta
            result['inferred_eps'] = inferred_eps

        state['results'].append(result)
        save_incremental(state)

    state['status'] = 'done'
    state['finished'] = time.strftime('%Y-%m-%d %H:%M:%S')
    state['wall_s'] = time.time() - t_global
    save_incremental(state)

    print("\n" + "=" * 78)
    print("SUMMARY")
    print("=" * 78)
    for r in state['results']:
        if r.get('skipped'):
            print(f"  c={r['c']} R={r['R']}: SKIPPED ({r['reason']})")
            continue
        if r.get('v2_H') is None:
            print(f"  c={r['c']} R={r['R']}: FAIL ({r['status']})")
            continue
        print(f"  c={r['c']} R={r['R']}: v_2(c-R)={r['v2_c_minus_R']}, "
              f"delta={r['actual_delta']}, eps={r['inferred_eps']} "
              f"(t={r['t_total_s']:.0f}s)")
    print(f"\nTotal wall: {state['wall_s']:.0f}s")
    print(f"Saved {OUT_PATH}")


if __name__ == '__main__':
    main()
