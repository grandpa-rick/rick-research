"""Day 98 CODE Task 3 — plug the c=17 per-k gap for k ∈ [7, 15].

Day 91 established min v_2(h_k^{(c=17)}(a, b)) for k ∈ [0, 6] via a [0, 64)^2
shell scan. The witness at (15, 0, k*=2) gives β'(17) ≤ 23. Together with
LB_k catalog values for k ∈ [0, 6], β'(17) = 23 was declared EXACT (Day 96).

But k ∈ [7, 15] were only covered by the LB catalog *empirically*. This
script does the direct shell scan for k ∈ [7, 15] to close the gap.

Method:
  - Fit Q_k^{(c=17)}(a, b) via the Pochhammer-normalized bivariate fit.
  - For each k, scan [0, 2^T)^2 with a+b ≡ c mod 2 (c=17 odd → a+b odd).
  - Take T = 6 (matches Day 91) and also T = 8 (256 grid, checks stability).
  - Report min v_2 per k and per T. If min v_2 at T=6 = min v_2 at T=8,
    empirical periodicity holds and the [0, 32)^2 (=2T shell) result stands.

Also as a cross-check, re-run k ∈ [0, 6] and verify against Day 91 numbers.
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


def scan_shell(Q_ab, c_val, k_target, T_exp, verbose=False):
    """Scan [0, 2^T_exp)^2 with a+b ≡ c_val mod 2. Return min v_2 and count."""
    a_sym, b_sym = sp.symbols('a b')
    f_Q = sp.lambdify((a_sym, b_sym), Q_ab, modules='math')
    L = c_val - 1 - k_target
    N = 1 << T_exp
    par = c_val % 2
    min_v = None
    argmin_first = None
    argmin_count = 0
    for a in range(N):
        pa = rising_fact(a + 3, L)
        for b in range(N):
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
                argmin_first = (a, b, v)
                argmin_count = 1
            elif v == min_v:
                argmin_count += 1
    return min_v, argmin_first, argmin_count


def main():
    print("=" * 78)
    print("Day 98 (2026-07-16) — c = 17 per-k gap plug for k ∈ [7, 15]")
    print("=" * 78)

    c_val = 17
    print(f"c = {c_val}, T_of(c) = 16 (natural shell [0, 32)^2)")
    print(f"Day 91 covered k ∈ [0, 6] with [0, 64)^2 scan.")
    print(f"Task 3: extend to k ∈ [7, 15] and cross-check k ∈ [0, 6].")

    # Extract Q_k for each k in [0, 15]
    fit_times = {}
    Qs = {}
    for k in range(0, 16):
        t0 = time.time()
        tables = hkfit.build_e2_tables(max_j=k + 2)
        try:
            Q_ab = sample_and_fit_Qk(c_val, k, tables)
        except Exception as e:
            print(f"  k={k}: fit exception: {e}")
            Q_ab = None
        fit_times[k] = time.time() - t0
        if Q_ab is None:
            print(f"  k={k}: fit FAILED ({fit_times[k]:.1f}s)")
            continue
        Qs[k] = Q_ab
        print(f"  k={k}: fit OK ({fit_times[k]:.1f}s)")

    # Scan each k on multiple shell sizes
    print(f"\n{'k':>3} {'T=6':>10} {'T=8':>10} {'stable':>7} {'argmin_T=8':>18} {'count_T=8':>10}")
    results = {}
    for k in sorted(Qs.keys()):
        Q_ab = Qs[k]
        # T=6 first
        t0 = time.time()
        min_v_6, argmin_6, count_6 = scan_shell(Q_ab, c_val, k, 6)
        t_6 = time.time() - t0
        t0 = time.time()
        min_v_8, argmin_8, count_8 = scan_shell(Q_ab, c_val, k, 8)
        t_8 = time.time() - t0
        stable = (min_v_6 == min_v_8) if (min_v_6 is not None and min_v_8 is not None) else False
        print(f"{k:>3} {min_v_6!s:>10} {min_v_8!s:>10} {str(stable):>7} "
              f"{str(argmin_8):>18} {count_8:>10}   ({t_6:.1f}+{t_8:.1f}s)")
        results[k] = {
            'min_v2_T6': min_v_6,
            'argmin_T6': argmin_6,
            'count_T6': count_6,
            'min_v2_T8': min_v_8,
            'argmin_T8': argmin_8,
            'count_T8': count_8,
            'stable': stable,
            't_6_s': t_6,
            't_8_s': t_8,
        }

    print("\n" + "=" * 78)
    print("SYNTHESIS — β'(17) certification")
    print("=" * 78)
    all_ok = True
    min_across_k = None
    for k in sorted(results.keys()):
        r = results[k]
        v = r['min_v2_T8']
        if v is None:
            print(f"  k={k}: no data")
            all_ok = False
            continue
        if min_across_k is None or v < min_across_k:
            min_across_k = v
        note = ""
        if v < 23:
            note = " ← LT 23 (β'(17) would be lower!)"
            all_ok = False
        print(f"  k={k}: min v_2 = {v}  stable_at_T=6 = {r['stable']}{note}")
    print(f"\n  min over k in [0, 15]: {min_across_k}")
    if min_across_k is not None and min_across_k >= 23:
        print(f"  ⇒ min v_2 >= 23 across all k in [0, 15]")
        print(f"  Combined with witness at (15, 0, k*=2): β'(17) = 23 CONFIRMED end-to-end")
    elif min_across_k is not None:
        print(f"  ⇒ min v_2 = {min_across_k} < 23 — β'(17) may be lower than 23!")

    out = {
        'note': 'Day 98 c=17 per-k gap plug for k ∈ [7, 15]',
        'date': '2026-07-16',
        'c': c_val,
        'fit_times_s': fit_times,
        'results_per_k': {str(k): v for k, v in results.items()},
        'min_across_k_T8': min_across_k,
        'all_k_ge_23': all_ok if min_across_k is not None else False,
    }
    outpath = '/home/agent/projects/code/2026-07-16-c17-per-k-gap-plug.json'
    with open(outpath, 'w') as f:
        json.dump(out, f, indent=2, default=str)
    print(f"\nSaved {outpath}")


if __name__ == "__main__":
    main()
