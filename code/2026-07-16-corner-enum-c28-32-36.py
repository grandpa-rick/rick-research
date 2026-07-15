"""Day 98 CODE (2026-07-16) — finish corner enumeration at c ∈ {28, 32, 36}.

Follow-up to the wake sub-agent that only completed c = 24 in the
`2026-07-16-corner-enum-c24-36.py` script. That run showed fits blowing
up at high k (24s at k=19 for c=24), so we cap k ≤ 15 across all c to
fit within budget while still covering the region where the c=20 counter-
example (k=11 interior beat corner by 1) lives.

Crown-jewel prediction: c = 36 has v_2(c - 4) = v_2(32) = 5, versus
c = 20 which has v_2(c - 4) = 4. If the "v_2(c-i) resonance" mechanism
is real, we should see an interior-beats-corner gap ≥ 2 at c = 36 for
some odd k (likely k=11). If we don't, the mechanism is refuted.

Optimisation: build_e2_tables is c-independent, so build once per k_target
(max_j=k_target+2) and reuse across c.
"""

import json
import sys
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


def sample_and_fit_Qk(c_val, k_target, tables, verbose=False):
    """Extract Q_k^{(c)}(a, b) via bivariate fit. Reuses precomputed tables."""
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
                if verbose:
                    print(f"  ! non-integer Q at (a={a}, b={b})")
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
    return v2(h), h


def full_shell_scan(c_val, k_target, Q_ab, T, L):
    a_sym, b_sym = sp.symbols('a b')
    f_Q = sp.lambdify((a_sym, b_sym), Q_ab, modules='math')
    par = c_val % 2
    min_v = None
    argmin = []
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
                argmin = [(a, b, v)]
            elif v == min_v and len(argmin) < 20:
                argmin.append((a, b, v))
    return min_v, argmin


def v2_c_minus_i_table(c_val, imax=5):
    out = {}
    for i in range(1, imax + 1):
        val = c_val - i
        out[i] = {'c_minus_i': val, 'v2': v2(val) if val != 0 else None}
    return out


# ============================================================================
# Budgets
# ============================================================================
PER_C_BUDGET_S = 600      # 10 min per c
OVERALL_BUDGET_S = 1500   # ~25 min total
PER_K_FIT_CUTOFF_S = 90   # if a single fit takes >90s, stop upping k
K_MAX = 15                # per CODE.md option (a): cap k at 15


def process_c(c_val, global_start, table_cache):
    T = T_of(c_val)
    print(f"\n{'=' * 78}")
    print(f"c = {c_val}, T = {T}")
    v2ci = v2_c_minus_i_table(c_val)
    print(f"  v_2(c-i) table:")
    for i in range(1, 6):
        e = v2ci[i]
        print(f"    i={i}: c-i={e['c_minus_i']}, v_2 = {e['v2']}")

    k_vals = [k for k in range(1, min(K_MAX, c_val - 3) + 1, 2)]
    records = []
    c_start = time.time()
    truncated = False
    truncated_at_k = None
    for k_target in k_vals:
        if time.time() - global_start > OVERALL_BUDGET_S:
            print(f"  [OVERALL TIMEOUT] stopping at k={k_target}")
            truncated = True
            truncated_at_k = k_target
            break
        if time.time() - c_start > PER_C_BUDGET_S:
            print(f"  [PER-C TIMEOUT] stopping at k={k_target}")
            truncated = True
            truncated_at_k = k_target
            break

        # Reuse tables across c for a given k_target.
        if k_target not in table_cache:
            table_cache[k_target] = hkfit.build_e2_tables(max_j=k_target + 2)
        tables = table_cache[k_target]

        L = c_val - 1 - k_target
        t0 = time.time()
        try:
            Q_ab = sample_and_fit_Qk(c_val, k_target, tables)
        except Exception as e:
            print(f"  k={k_target}: EXCEPTION during fit: {e}")
            Q_ab = None
        t_fit = time.time() - t0

        if Q_ab is None:
            print(f"  k={k_target}: EXTRACT FAILED ({t_fit:.1f}s)")
            continue

        corners_coords = [(T - 2, 0), (0, T - 2), (T - 2, T - 2), (0, 0)]
        corner_v2s = []
        corner_h = []
        for (a_val, b_val) in corners_coords:
            if (a_val + b_val) % 2 != c_val % 2:
                corner_v2s.append(None)
                corner_h.append(None)
                continue
            v, h = v2_hk_from_Q(a_val, b_val, c_val, k_target, Q_ab, L)
            corner_v2s.append(v)
            corner_h.append(h)

        t1 = time.time()
        try:
            min_v, argmin = full_shell_scan(c_val, k_target, Q_ab, T, L)
        except Exception as e:
            print(f"  k={k_target}: EXCEPTION during scan: {e}")
            continue
        t_scan = time.time() - t1

        corners_named = ['C1_(T-2,0)', 'C2_(0,T-2)', 'C3_(T-2,T-2)', 'C4_(0,0)']
        tie_corners = []
        for i, cv in enumerate(corner_v2s):
            if cv is not None and cv == min_v:
                tie_corners.append(corners_named[i])
        interior_wins = (len(tie_corners) == 0)
        valid_corners = [c for c in corner_v2s if c is not None]
        min_corner_v2 = min(valid_corners) if valid_corners else None
        gap = (min_corner_v2 - min_v) if (min_corner_v2 is not None and min_v is not None) else None

        print(f"  k={k_target:>2}: L={L:>2}  fit {t_fit:.1f}s  scan {t_scan:.1f}s")
        print(f"    corners v_2 [C1,C2,C3,C4] = {corner_v2s}  (min corner = {min_corner_v2})")
        print(f"    true min v_2 = {min_v}, argmin[0..4] = {argmin[:5]}")
        if interior_wins:
            print(f"    ==> INTERIOR WINS, gap = {gap}")
        else:
            print(f"    corners tying: {tie_corners}  (gap = {gap})")

        records.append({
            'c': c_val,
            'k': k_target,
            'T': T,
            'L': L,
            'corner_v2': corner_v2s,
            'corner_coords': corners_coords,
            'min_corner_v2': min_corner_v2,
            'min_v2': min_v,
            'gap_corner_minus_interior': gap,
            'argmin_size': len(argmin),
            'argmin_first5': argmin[:5],
            'tie_corners': tie_corners,
            'interior_wins': interior_wins,
            'fit_time_s': t_fit,
            'scan_time_s': t_scan,
        })

        if t_fit > PER_K_FIT_CUTOFF_S:
            print(f"  [FIT CUTOFF] k={k_target} took {t_fit:.1f}s; truncating higher k")
            truncated = True
            truncated_at_k = k_target
            break

    return {
        'c': c_val,
        'T': T,
        'v2_c_minus_i': v2ci,
        'records': records,
        'truncated': truncated,
        'truncated_at_k': truncated_at_k,
        'wall_s': time.time() - c_start,
    }


def main():
    print("=" * 78)
    print("Day 98 (2026-07-16) — Corner enum c ∈ {28,32,36}, k ≤ 15")
    print("=" * 78)

    c_vals = [28, 32, 36]
    all_c = []
    table_cache = {}
    global_start = time.time()

    for c_val in c_vals:
        if time.time() - global_start > OVERALL_BUDGET_S:
            print(f"\n[OVERALL TIMEOUT] before c={c_val}: skipping.")
            all_c.append({'c': c_val, 'status': 'skipped_overall_timeout', 'records': []})
            continue
        block = process_c(c_val, global_start, table_cache)
        block['status'] = 'completed_full' if not block['truncated'] else 'completed_truncated'
        all_c.append(block)

    # Summary table
    print("\n" + "=" * 78)
    print("SUMMARY TABLE — corner enumeration c ∈ {28, 32, 36}")
    print("=" * 78)
    print(f"{'c':>3} {'T':>3} {'k':>3} {'L':>2} "
          f"{'C1':>4} {'C2':>4} {'C3':>4} {'C4':>4} {'min_c':>5} {'true_min':>8} "
          f"{'gap':>4} {'interior':>10}")
    for block in all_c:
        for r in block.get('records', []):
            cv = r['corner_v2']
            def fmt(x): return str(x) if x is not None else '-'
            print(f"{r['c']:>3} {r['T']:>3} {r['k']:>3} {r['L']:>2} "
                  f"{fmt(cv[0]):>4} {fmt(cv[1]):>4} {fmt(cv[2]):>4} {fmt(cv[3]):>4} "
                  f"{fmt(r['min_corner_v2']):>5} {r['min_v2']:>8} "
                  f"{fmt(r['gap_corner_minus_interior']):>4} "
                  f"{'YES' if r['interior_wins'] else 'no':>10}")

    # Correlation analysis
    print("\n" + "=" * 78)
    print("CORRELATION: interior-win gap vs v_2(c-i)")
    print("=" * 78)
    for block in all_c:
        if not block.get('records'):
            print(f"c={block['c']}: no records ({block.get('status')})")
            continue
        c_val = block['c']
        v2ci = block['v2_c_minus_i']
        v2c1 = v2ci[1]['v2']
        v2c2 = v2ci[2]['v2']
        v2c3 = v2ci[3]['v2']
        v2c4 = v2ci[4]['v2']
        v2c5 = v2ci[5]['v2']
        gaps = [(r['k'], r['gap_corner_minus_interior'], r['interior_wins'])
                for r in block['records']
                if r['gap_corner_minus_interior'] is not None]
        interior_win_ks = [(r['k'], r['gap_corner_minus_interior']) for r in block['records']
                           if r['interior_wins']]
        max_gap = max((g for (_, g, _) in gaps), default=None)
        argmax_k = None
        for (k, g, _) in gaps:
            if g == max_gap:
                argmax_k = k
                break
        print(f"c={c_val}: v_2(c-i) i=1..5: [{v2c1},{v2c2},{v2c3},{v2c4},{v2c5}]  "
              f"max gap = {max_gap} at k = {argmax_k}, interior-win ks = {interior_win_ks}")

    # Synthesis
    print("\n" + "=" * 78)
    print("SYNTHESIS")
    print("=" * 78)
    for block in all_c:
        if not block.get('records'):
            continue
        c_val = block['c']
        gaps = [(r['k'], r['gap_corner_minus_interior']) for r in block['records']
                if r['gap_corner_minus_interior'] is not None]
        max_gap = max((g for (_, g) in gaps), default=None)
        v2cm4 = block['v2_c_minus_i'][4]['v2']
        print(f"c = {c_val}: v_2(c-4) = {v2cm4}, max gap = {max_gap}")
    print()
    c36_block = next((b for b in all_c if b.get('c') == 36), None)
    if c36_block and c36_block.get('records'):
        gaps36 = [(r['k'], r['gap_corner_minus_interior']) for r in c36_block['records']
                  if r['gap_corner_minus_interior'] is not None]
        max_gap_36 = max((g for (_, g) in gaps36), default=None)
        if max_gap_36 is None:
            verdict = "no data"
        elif max_gap_36 >= 2:
            verdict = f"CONFIRMED — c=36 shows interior-win gap ≥ 2 (max = {max_gap_36})"
        elif max_gap_36 == 1:
            verdict = f"partial — c=36 shows gap = 1 (same as c=20), no amplification"
        else:
            verdict = f"REFUTED — c=36 shows gap = 0, mechanism fails"
        print(f"'v_2(c-i) resonance' prediction: {verdict}")

    out = {
        'note': 'Day 98 corner enum c ∈ {28,32,36}, k ≤ 15',
        'date': '2026-07-16',
        'c_vals': c_vals,
        'k_max': K_MAX,
        'blocks': all_c,
        'total_wall_s': time.time() - global_start,
    }
    outpath_json = '/home/agent/projects/code/2026-07-16-corner-enum-c28-32-36.json'
    with open(outpath_json, 'w') as f:
        json.dump(out, f, indent=2, default=str)
    print(f"\nSaved {outpath_json}")
    print(f"Total wall: {time.time() - global_start:.1f}s")


if __name__ == "__main__":
    main()
