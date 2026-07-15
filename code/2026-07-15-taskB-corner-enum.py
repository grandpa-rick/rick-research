"""Day 97 Task B — Corner enumeration table for h_k^{(c)}(a, b).

For each c ∈ {8, 12, 16, 20} and each odd k ∈ [1, c-3], compute
v_2(h_k^{(c)}(a, b)) at the four corners:
  C1: (T-2, 0)
  C2: (0, T-2)
  C3: (T-2, T-2)
  C4: (0, 0)
where T = smallest power of 2 > c-2.

Then scan the full parity shell a, b ∈ [0, 2T] with (a+b) ≡ c (mod 2)
to find the true argmin of v_2(h_k). Report which corner ties (if any).

Uses Q_k^{(c)}(a, b) extracted via bivariate polynomial fit from the
h_k pipeline; then h_k(a, b) = (a+3)_L · (b+2)_L · Q_k^{(c)}(a, b) for
integer (a, b).
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
        return None  # ∞, treat as "no valid v_2 here"
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


def v2_rising(x, n):
    """v_2( (x)_n ) — assumes x integer >=0 or so."""
    p = rising_fact(x, n)
    return v2(p)


def sample_and_fit_Qk(c_val, k_target, verbose=False):
    """Extract Q_k^{(c)}(a, b) via bivariate fit. Returns sympy poly in (a, b)."""
    L = c_val - 1 - k_target
    if L < 0:
        return None
    tables = hkfit.build_e2_tables(max_j=k_target + 2)
    # sample enough points; bivariate degree of Q_k bound = 2·floor(k/2)
    bd = 2 * (k_target // 2)
    max_deg_try = bd + 4
    max_monos = (max_deg_try + 1) * (max_deg_try + 2) // 2
    num_pts_target = max_monos + 20
    # sample (a, b) with a >= b >= c
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
        # verify
        ok = True
        for (av, bv, yv) in samples:
            if poly.subs({a_sym: av, b_sym: bv}) != yv:
                ok = False
                break
        if not ok:
            continue
        return poly
    return None


def v2_hk(a_val, b_val, c_val, k_target, Q_ab, L):
    """v_2 of h_k^{(c)}(a, b) = (a+3)_L·(b+2)_L·Q_k^{(c)}(a, b) for integer (a, b)."""
    a_sym, b_sym = sp.symbols('a b')
    Qv = int(Q_ab.subs({a_sym: a_val, b_sym: b_val}))
    poch_a = rising_fact(a_val + 3, L)
    poch_b = rising_fact(b_val + 2, L)
    h = poch_a * poch_b * Qv
    return v2(h), h


def full_shell_scan(c_val, k_target, Q_ab, T, L):
    """Scan a, b ∈ [0, 2T] with (a+b) ≡ c (mod 2), find argmin v_2(h_k)."""
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


def main():
    print("=" * 78)
    print("Day 97 Task B — Corner enumeration for h_k^{(c)}(a, b)")
    print("=" * 78)

    c_vals = [8, 12, 16, 20]
    corners_named = ['C1_(T-2,0)', 'C2_(0,T-2)', 'C3_(T-2,T-2)', 'C4_(0,0)']

    all_records = []
    for c_val in c_vals:
        T = T_of(c_val)
        print(f"\nc = {c_val}, T = {T}")
        k_vals = list(range(1, c_val - 2, 2))  # odd k ∈ [1, c-3]
        for k_target in k_vals:
            L = c_val - 1 - k_target
            t0 = time.time()
            Q_ab = sample_and_fit_Qk(c_val, k_target)
            if Q_ab is None:
                print(f"  k={k_target}: EXTRACT FAILED")
                continue
            t_fit = time.time() - t0

            # Corner values
            corners_coords = [(T - 2, 0), (0, T - 2), (T - 2, T - 2), (0, 0)]
            corner_v2s = []
            corner_h = []
            for (a_val, b_val) in corners_coords:
                # parity check
                if (a_val + b_val) % 2 != c_val % 2:
                    corner_v2s.append(None)
                    corner_h.append(None)
                    continue
                v, h = v2_hk(a_val, b_val, c_val, k_target, Q_ab, L)
                corner_v2s.append(v)
                corner_h.append(h)

            # Shell scan
            t1 = time.time()
            min_v, argmin = full_shell_scan(c_val, k_target, Q_ab, T, L)
            t_scan = time.time() - t1

            # Which corners tie
            tie_corners = []
            for i, cv in enumerate(corner_v2s):
                if cv is not None and cv == min_v:
                    tie_corners.append(corners_named[i])

            interior_wins = (len(tie_corners) == 0)

            print(f"  k={k_target:>2}: L={L:>2}   fit {t_fit:.1f}s   scan {t_scan:.1f}s")
            print(f"    corners v_2 [C1,C2,C3,C4] = {corner_v2s}")
            print(f"    true min v_2 = {min_v}, "
                  f"argmin size = {len(argmin)}, "
                  f"argmin[0] = {argmin[0] if argmin else None}")
            if tie_corners:
                print(f"    corners tying: {tie_corners}")
            else:
                print(f"    INTERIOR WINS at {[a[:2] for a in argmin[:5]]}")

            all_records.append({
                'c': c_val,
                'k': k_target,
                'T': T,
                'L': L,
                'corner_v2': corner_v2s,
                'corner_coords': corners_coords,
                'min_v2': min_v,
                'argmin_size': len(argmin),
                'argmin_first5': argmin[:5],
                'tie_corners': tie_corners,
                'interior_wins': interior_wins,
                'fit_time_s': t_fit,
                'scan_time_s': t_scan,
            })

    print("\n" + "=" * 78)
    print("SUMMARY TABLE — corner enumeration")
    print("=" * 78)
    print(f"{'c':>3} {'T':>3} {'k':>3} {'L':>2} "
          f"{'C1':>4} {'C2':>4} {'C3':>4} {'C4':>4} {'true_min':>8} "
          f"{'ties':>16} {'interior':>10}")
    for r in all_records:
        cv = r['corner_v2']

        def fmt(x): return str(x) if x is not None else '-'
        ties = ",".join(t.replace("_", "") for t in r['tie_corners']) or 'NONE'
        print(f"{r['c']:>3} {r['T']:>3} {r['k']:>3} {r['L']:>2} "
              f"{fmt(cv[0]):>4} {fmt(cv[1]):>4} {fmt(cv[2]):>4} {fmt(cv[3]):>4} "
              f"{r['min_v2']:>8} {ties:>16} {'YES' if r['interior_wins'] else 'no':>10}")

    print("\n" + "=" * 78)
    print("MOD-4 PATTERN by (c mod 4, which corner wins)")
    print("=" * 78)
    for c_val in c_vals:
        rows = [r for r in all_records if r['c'] == c_val]
        winners = [(r['k'], r['tie_corners']) for r in rows]
        print(f"c={c_val} (c mod 4 = {c_val % 4}): {winners}")

    out = {
        'note': 'Day 97 Task B: corner enumeration for h_k^{(c)}(a, b)',
        'c_vals': c_vals,
        'records': all_records,
    }
    outpath = '/home/agent/projects/code/2026-07-15-taskB-corner-enum.json'
    with open(outpath, 'w') as f:
        json.dump(out, f, indent=2, default=str)
    print(f"\nSaved {outpath}")


if __name__ == "__main__":
    main()
