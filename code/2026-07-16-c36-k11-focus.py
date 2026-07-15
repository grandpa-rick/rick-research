"""Day 98 CODE Task 2 — focused c = 36, k = 11 interior-argmin probe.

Rationale: the c = 20 counter-example had (2, 4) interior beating every
corner by v_2 = 1 for k = 11. Prediction from Day 97: c = 36 with
v_2(c - 4) = v_2(32) = 5 (one more bit than c = 20) should show an
interior win by ≥ 2 at k = 11.

Deliverable: v_2(h_11^{(36)}(a, b)) at
  (T-2, 0), (0, T-2), (T-2, T-2), (0, 0),   # corners
  (2, 4), (2, 8), (4, 8), (2, 0),           # small-i witnesses
  plus a full shell scan for the true argmin.
"""

import json
import time
from importlib import util

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
    while n & 1 == 0:
        n >>= 1
        v += 1
    return v


def T_of(c):
    T = 1
    while T <= c - 2:
        T *= 2
    return T


def rising_fact(x, n):
    if n <= 0:
        return 1
    p = 1
    for i in range(n):
        p *= (x + i)
    return p


def sample_and_fit_Qk(c_val, k_target, tables):
    L = c_val - 1 - k_target
    if L < 0:
        return None
    bd = 2 * (k_target // 2)
    max_deg_try = bd + 4
    max_monos = (max_deg_try + 1) * (max_deg_try + 2) // 2
    num_pts_target = max_monos + 20
    samples = []
    a = c_val
    while len(samples) < num_pts_target and a < c_val + 50:
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
    for D in range(bd + 4 + 1):
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


def v2_hk_from_Q(a_val, b_val, c_val, k_target, Q_ab, L):
    a_sym, b_sym = sp.symbols('a b')
    Qv = int(Q_ab.subs({a_sym: a_val, b_sym: b_val}))
    poch_a = rising_fact(a_val + 3, L)
    poch_b = rising_fact(b_val + 2, L)
    h = poch_a * poch_b * Qv
    return v2(h), h, Qv


def main():
    print("=" * 78)
    print("Day 98 (2026-07-16) — c = 36, k = 11 focus scan")
    print("=" * 78)

    c_val = 36
    k_target = 11
    T = T_of(c_val)
    L = c_val - 1 - k_target
    print(f"c = {c_val}, k = {k_target}, T = {T}, L = {L}")
    print(f"v_2(c-i) i=1..5: {[v2(c_val - i) for i in range(1, 6)]}")
    print(f"  (compare c=20: {[v2(20 - i) for i in range(1, 6)]})")

    t0 = time.time()
    tables = hkfit.build_e2_tables(max_j=k_target + 2)
    print(f"\nbuild_e2_tables: {time.time() - t0:.1f}s")

    t0 = time.time()
    Q_ab = sample_and_fit_Qk(c_val, k_target, tables)
    t_fit = time.time() - t0
    print(f"Fit Q_11^(36)(a,b): {t_fit:.1f}s")
    if Q_ab is None:
        print("FIT FAILED — aborting")
        return

    # Witness points to probe
    witnesses_named = [
        ('C1_(T-2, 0)', (T - 2, 0)),
        ('C2_(0, T-2)', (0, T - 2)),
        ('C3_(T-2, T-2)', (T - 2, T - 2)),
        ('C4_(0, 0)', (0, 0)),
        ('mirror_c20_(2, 4)', (2, 4)),
        ('interior_(2, 8)', (2, 8)),
        ('interior_(4, 8)', (4, 8)),
        ('interior_(2, 0)', (2, 0)),
        ('interior_(4, 4)', (4, 4)),
        ('interior_(4, 0)', (4, 0)),
        ('interior_(0, 4)', (0, 4)),
        ('interior_(6, 4)', (6, 4)),
        ('interior_(2, 2)', (2, 2)),
        ('interior_(4, 2)', (4, 2)),
    ]
    print("\n--- Witness v_2 values ---")
    print(f"{'name':>26} {'(a,b)':>10} {'parity':>6} {'v_2':>6}  {'Q_11':>12}")
    witness_results = []
    for (name, (a_val, b_val)) in witnesses_named:
        par = (a_val + b_val) % 2
        if par != c_val % 2:
            print(f"{name:>26} {str((a_val, b_val)):>10} {par:>6} {'skip':>6}")
            witness_results.append({'name': name, 'ab': (a_val, b_val), 'v2': None, 'skipped_parity': True})
            continue
        v, h, Q = v2_hk_from_Q(a_val, b_val, c_val, k_target, Q_ab, L)
        print(f"{name:>26} {str((a_val, b_val)):>10} {par:>6} {v:>6}  {str(Q)[:12]:>12}")
        witness_results.append({'name': name, 'ab': (a_val, b_val), 'v2': v, 'h': str(h), 'Q': str(Q)})

    # Full shell scan for true argmin
    print("\n--- Full shell scan (0..2T, parity matched) ---")
    a_sym, b_sym = sp.symbols('a b')
    f_Q = sp.lambdify((a_sym, b_sym), Q_ab, modules='math')
    par = c_val % 2
    min_v = None
    argmin_list = []
    t_scan_start = time.time()
    for a in range(0, 2 * T + 1):
        pa = rising_fact(a + 3, L)
        for b in range(0, 2 * T + 1):
            if (a + b) % 2 != par:
                continue
            pb = rising_fact(b + 2, L)
            try:
                Qv = int(f_Q(a, b))
            except (ValueError, OverflowError):
                Qv = int(Q_ab.subs({a_sym: a, b_sym: b}))
            h = pa * pb * Qv
            if h == 0:
                continue
            v = v2(h)
            if min_v is None or v < min_v:
                min_v = v
                argmin_list = [(a, b, v)]
            elif v == min_v:
                argmin_list.append((a, b, v))
    t_scan = time.time() - t_scan_start
    print(f"Full shell scan: {t_scan:.1f}s")
    print(f"true min v_2 = {min_v}")
    print(f"argmin count = {len(argmin_list)}")
    print("First 30 argmin coords:")
    for entry in argmin_list[:30]:
        print(f"  {entry}")

    # Compare corner min vs true min
    corner_v2s = [r['v2'] for r in witness_results[:4] if r['v2'] is not None]
    min_corner_v2 = min(corner_v2s) if corner_v2s else None
    gap = (min_corner_v2 - min_v) if (min_corner_v2 is not None and min_v is not None) else None
    print(f"\nmin_corner_v2 = {min_corner_v2}, true_min = {min_v}, GAP = {gap}")

    # Small-i witnesses (a small)
    small_i_wins = [(name, r['ab'], r['v2']) for (name, r) in
                    zip([n for n, _ in witnesses_named[4:]], witness_results[4:])
                    if r['v2'] is not None and r['v2'] == min_v]
    print(f"Small-i witnesses achieving true min: {small_i_wins}")

    # Diagnostic: is the argmin near the (small-a, small-b) corner?
    small_argmins = [x for x in argmin_list if x[0] <= 8 and x[1] <= 8]
    print(f"argmins with a<=8 and b<=8: {small_argmins}")

    verdict_lines = []
    if gap is None:
        verdict_lines.append("no data")
    elif gap == 0:
        verdict_lines.append("REFUTED — c=36 k=11 shows gap = 0; interior does not beat corner")
    elif gap == 1:
        verdict_lines.append("PARTIAL — c=36 k=11 shows gap = 1 (same as c=20 k=11 baseline)")
    elif gap >= 2:
        verdict_lines.append(f"CONFIRMED — c=36 k=11 shows gap = {gap} (≥ 2): mechanism amplifies with v_2(c-4)")
    if small_i_wins:
        wa, wb = small_i_wins[0][1]
        verdict_lines.append(f"Winner near small (a,b) = ({wa},{wb})")

    print("\n" + "=" * 78)
    print("VERDICT")
    print("=" * 78)
    for line in verdict_lines:
        print(" • " + line)

    out = {
        'note': 'Day 98 c=36 k=11 focused scan',
        'date': '2026-07-16',
        'c': c_val,
        'k': k_target,
        'T': T,
        'L': L,
        'v2_c_minus_i': {i: v2(c_val - i) for i in range(1, 6)},
        'witnesses': [{'name': n, 'ab': list(r['ab']), 'v2': r['v2']}
                      for (n, r) in zip([w[0] for w in witnesses_named], witness_results)],
        'true_min_v2': min_v,
        'argmin_count': len(argmin_list),
        'argmin_first_30': [list(x) for x in argmin_list[:30]],
        'small_argmins': [list(x) for x in small_argmins],
        'min_corner_v2': min_corner_v2,
        'gap_corner_minus_interior': gap,
        'small_i_wins': [(n, list(ab), v) for (n, ab, v) in small_i_wins],
        'verdict': verdict_lines,
        'fit_time_s': t_fit,
        'scan_time_s': t_scan,
    }
    outpath = '/home/agent/projects/code/2026-07-16-c36-k11-focus.json'
    with open(outpath, 'w') as f:
        json.dump(out, f, indent=2, default=str)
    print(f"\nSaved {outpath}")


if __name__ == "__main__":
    main()
