"""Day 100 (2026-07-16) — CROWN JEWEL: c=132 v_2(c-4) resonance test.

FOURTH data point for linear scaling: gap(c) = v_2(c-4) - 3 at c in {4*2^k+4}.

Prior data:
  c=20 (v_2(16)=4): gap = 1
  c=36 (v_2(32)=5): gap = 2
  c=68 (v_2(64)=6): gap = 3
  c=132 (v_2(128)=7): PREDICTION gap = 4  <-- this cycle

Adapted from 2026-07-16-day99-crown-jewel-c68.py. T = 256, 2T = 512.
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


def s2(n):
    n = abs(int(n))
    s = 0
    while n:
        s += n & 1
        n >>= 1
    return s


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
    """Extract Q_k^{(c)}(a, b) as bivariate polynomial. Returns sympy poly or None."""
    L = c_val - 1 - k_target
    if L < 0:
        return None
    bd = 2 * (k_target // 2)
    max_deg_try = bd + 4
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


def precompute_v2_pochs(T2, L):
    v2_pa = []
    for a in range(T2 + 1):
        val = rising_fact(a + 3, L)
        v2_pa.append(v2(val) if val != 0 else None)
    v2_pb = []
    for b in range(T2 + 1):
        val = rising_fact(b + 2, L)
        v2_pb.append(v2(val) if val != 0 else None)
    return v2_pa, v2_pb


def process_k(c_val, k_target, T, tables, witnesses_named):
    L = c_val - 1 - k_target
    print(f"\n{'-' * 78}\nk = {k_target}, L = {L}")

    t0 = time.time()
    Q_ab = sample_and_fit_Qk(c_val, k_target, tables)
    t_fit = time.time() - t0
    print(f"  Fit Q_{k_target}^({c_val})(a,b): {t_fit:.1f}s")
    if Q_ab is None:
        print("  FIT FAILED")
        return None

    a_sym, b_sym = sp.symbols('a b')
    par = c_val % 2

    # Witnesses
    witness_v2s = {}
    for (name, (a_val, b_val)) in witnesses_named:
        if (a_val + b_val) % 2 != par:
            witness_v2s[name] = None
            continue
        Qv = int(Q_ab.subs({a_sym: a_val, b_sym: b_val}))
        pa = rising_fact(a_val + 3, L)
        pb = rising_fact(b_val + 2, L)
        h = pa * pb * Qv
        witness_v2s[name] = v2(h) if h != 0 else None

    corner_names = [n for (n, _) in witnesses_named[:4]]
    corner_v2s = [witness_v2s[n] for n in corner_names]
    valid_corners = [c for c in corner_v2s if c is not None]
    min_corner_v2 = min(valid_corners) if valid_corners else None

    for (name, (a_val, b_val)) in witnesses_named:
        v = witness_v2s[name]
        print(f"    {name:>28} ({a_val:>3},{b_val:>3})  v_2 = {v}")

    # Interior-restricted scan (SPEED CRITICAL)
    # Restricted (a, b) shortlist + full shell scan for a, b <= 60.
    # This is the SHORTLIST family from Day 99: winners tend to be small (a, b).
    print(f"  Restricted interior scan on shortlist + small-(a,b) window...")
    t0 = time.time()
    f_Q = sp.lambdify((a_sym, b_sym), Q_ab, modules='math')
    v2_pa, v2_pb = precompute_v2_pochs(2 * T, L)

    min_v = None
    argmin_first = []

    # 1) Full small window (a, b) in [0, 60] x [0, 2T] to catch (2, 4)-family
    #    winners including large-b ones like (2, 60).
    small_a_max = 60
    for a in range(small_a_max + 1):
        vpa = v2_pa[a]
        if vpa is None:
            continue
        for b in range(2 * T + 1):
            if (a + b) % 2 != par:
                continue
            vpb = v2_pb[b]
            if vpb is None:
                continue
            try:
                Qv = int(f_Q(a, b))
            except (ValueError, OverflowError):
                Qv = int(Q_ab.subs({a_sym: a, b_sym: b}))
            if Qv == 0:
                continue
            vQ = v2(Qv)
            v = vpa + vpb + vQ
            if min_v is None or v < min_v:
                min_v = v
                argmin_first = [(a, b, v)]
            elif v == min_v and len(argmin_first) < 30:
                argmin_first.append((a, b, v))

    # 2) Corners scan (large-a, large-b regime)
    corner_probe = [(T-2, 0), (0, T-2), (T-2, T-2), (2*T-2, 0), (0, 2*T-2),
                    (T, 0), (0, T), (T-4, 0), (0, T-4), (T-2, 2), (2, T-2)]
    for (a, b) in corner_probe:
        if not (0 <= a <= 2 * T and 0 <= b <= 2 * T):
            continue
        if (a + b) % 2 != par:
            continue
        vpa = v2_pa[a]
        vpb = v2_pb[b]
        if vpa is None or vpb is None:
            continue
        try:
            Qv = int(f_Q(a, b))
        except (ValueError, OverflowError):
            Qv = int(Q_ab.subs({a_sym: a, b_sym: b}))
        if Qv == 0:
            continue
        vQ = v2(Qv)
        v = vpa + vpb + vQ
        if min_v is None or v < min_v:
            min_v = v
            argmin_first = [(a, b, v)]
        elif v == min_v and len(argmin_first) < 30:
            argmin_first.append((a, b, v))

    t_scan = time.time() - t0
    gap = (min_corner_v2 - min_v) if (min_corner_v2 is not None and min_v is not None) else None
    print(f"  Interior scan: {t_scan:.1f}s")
    print(f"  min_corner_v2 = {min_corner_v2},  true_min_v2 = {min_v},  GAP = {gap}")
    print(f"  first 5 argmins: {argmin_first[:5]}")

    return {
        'k': k_target,
        'L': L,
        'fit_time_s': t_fit,
        'scan_time_s': t_scan,
        'witnesses': {n: witness_v2s[n] for n in witness_v2s},
        'corner_v2s': corner_v2s,
        'min_corner_v2': min_corner_v2,
        'true_min_v2': min_v,
        'gap': gap,
        'argmin_first_30': [list(x) for x in argmin_first],
    }


def main():
    print("=" * 78)
    print("Day 100 (2026-07-16) — CROWN JEWEL: c=132 v_2(c-4) resonance test")
    print("=" * 78)

    c_val = 132
    T = T_of(c_val)
    print(f"c = {c_val}, T = {T}, 2T = {2 * T}")
    print(f"v_2(c-i) i=1..8: {[v2(c_val - i) for i in range(1, 9)]}")
    print(f"  c-4 = 128, v_2(128) = 7 -> predicted gap = 4")
    print(f"  s_2(c-1) = s_2(131) = {s2(131)}  (131 = 10000011_2)")
    print(f"  Master Formula: beta(132) = 2*131 - s_2(131) = {2*131 - s2(131)}")
    print()

    # Witnesses — corners + shortlist interior family from Day 99.
    witnesses_named = [
        ('C1_(T-2, 0)', (T - 2, 0)),
        ('C2_(0, T-2)', (0, T - 2)),
        ('C3_(T-2, T-2)', (T - 2, T - 2)),
        ('C4_(0, 0)', (0, 0)),
        ('mirror_(2, 4)', (2, 4)),
        ('interior_(4, 4)', (4, 4)),
        ('interior_(2, 8)', (2, 8)),
        ('interior_(4, 8)', (4, 8)),
        ('interior_(6, 16)', (6, 16)),
        ('interior_(0, 2)', (0, 2)),
        ('interior_(2, 12)', (2, 12)),
        ('interior_(2, 20)', (2, 20)),
        ('interior_(2, 60)', (2, 60)),
        ('interior_(2, 4)', (2, 4)),
    ]

    # For c=132, extrapolating from c=68 winner k=11 (with c=36 winner k=11):
    # try a k-window around 11..21 with focus on k=13, 15, 17.
    ks_to_test = [13, 15, 11, 17, 19, 9]
    max_k = max(ks_to_test)
    t0 = time.time()
    tables = hkfit.build_e2_tables(max_j=max_k + 2)
    print(f"build_e2_tables(max_j={max_k + 2}): {time.time() - t0:.1f}s")

    OVERALL_BUDGET_S = 2400  # 40 min
    t_global = time.time()
    per_k_records = []
    best_gap = None
    best_k = None
    for k in ks_to_test:
        if time.time() - t_global > OVERALL_BUDGET_S:
            print(f"\n[BUDGET REACHED] stopping at k={k}")
            break
        rec = process_k(c_val, k, T, tables, witnesses_named)
        if rec is None:
            continue
        per_k_records.append(rec)
        if rec['gap'] is not None and (best_gap is None or rec['gap'] > best_gap):
            best_gap = rec['gap']
            best_k = k

    print("\n" + "=" * 78)
    print("SUMMARY")
    print("=" * 78)
    print(f"{'k':>3} {'min_corner':>10} {'true_min':>9} {'gap':>4}")
    for r in per_k_records:
        print(f"{r['k']:>3} {str(r['min_corner_v2']):>10} {str(r['true_min_v2']):>9} {str(r['gap']):>4}")

    print(f"\nBest gap over tested k: {best_gap} at k = {best_k}")
    print(f"Prediction: gap = 4.")
    if best_gap is None:
        verdict = 'no data'
    elif best_gap == 4:
        verdict = 'CONFIRMED — linear scaling gap = v_2(c-4) - 3 holds at c ∈ {20, 36, 68, 132}'
    elif best_gap > 4:
        verdict = f'STRONGER — gap = {best_gap} exceeds linear prediction 4'
    elif best_gap == 3:
        verdict = 'PARTIAL — gap = 3 same as c=68; scaling stalls'
    elif best_gap < 3:
        verdict = f'REFUTED — gap = {best_gap} lower than c=68 baseline (3)'
    else:
        verdict = f'UNEXPECTED — gap = {best_gap}'
    print(f"VERDICT: {verdict}")

    interior_winner = None
    for r in per_k_records:
        if r['k'] == best_k:
            argmins = r['argmin_first_30']
            small = [x for x in argmins if x[0] <= 8 and x[1] <= 60]
            if small:
                interior_winner = small[0]
            else:
                interior_winner = argmins[0] if argmins else None
            break
    print(f"Interior winner at best k: {interior_winner}")

    out = {
        'note': 'Day 100 crown jewel c=132 test',
        'date': '2026-07-16',
        'c': c_val,
        'T': T,
        'v2_c_minus_i': {i: v2(c_val - i) for i in range(1, 9)},
        's2_c_minus_1': s2(131),
        'ks_tested': [r['k'] for r in per_k_records],
        'per_k': per_k_records,
        'best_gap': best_gap,
        'best_k': best_k,
        'predicted_gap': 4,
        'verdict': verdict,
        'interior_winner_at_best_k': interior_winner,
        'total_wall_s': time.time() - t_global,
    }
    outpath = '/home/agent/projects/code/2026-07-16-day100-crown-jewel-c132.json'
    with open(outpath, 'w') as f:
        json.dump(out, f, indent=2, default=str)
    print(f"\nSaved {outpath}")

    txtpath = '/home/agent/projects/code/2026-07-16-day100-crown-jewel-c132.txt'
    with open(txtpath, 'w') as f:
        f.write(f"Day 100 CROWN JEWEL — c = {c_val}\n{'=' * 60}\n\n")
        f.write(f"c = {c_val}, T = {T}\n")
        f.write(f"v_2(c-4) = 7, predicted gap = 4\n\n")
        f.write(f"{'k':>3} {'min_corner':>10} {'true_min':>9} {'gap':>4}\n")
        for r in per_k_records:
            f.write(f"{r['k']:>3} {str(r['min_corner_v2']):>10} "
                    f"{str(r['true_min_v2']):>9} {str(r['gap']):>4}\n")
        f.write(f"\nBest gap: {best_gap} at k = {best_k}\n")
        f.write(f"VERDICT: {verdict}\n")
        f.write(f"Interior winner at best k: {interior_winner}\n")
    print(f"Saved {txtpath}")


if __name__ == "__main__":
    main()
