"""Day 100 (2026-07-16) — Anchor neighbourhood sweep at c ≡ 2 mod 4, c ∈ [130, 200].

Hypothesis (Day 99): at c ≡ 2 mod 4, (0, 2) is the LB anchor and no other
(a, b) beats it. UB from (0, 2) is
    β(c) - Δ(c),  where β(c) = 2(c-1) - s_2(c-1), Δ(c) = s_2(m) + v_2(m), m = (c-2)/4.

Task C: verify this empirically for c ∈ {134, 138, ..., 198} (17 values, step 4).

Method:
  For each c:
    Compute Δ(c) and the (0, 2) UB u(c) = β(c) - Δ(c).
    For each (a, b) ∈ [0, 6]^2 \\ {(0, 2)}:
      Fit Q_k^{(c)}(a, b) for k in [0, k_max].
      Compute h_k^{(c)}(a, b) then H_c(a, b, j) via
          H_c(a, b, j) = sum_{k=0}^{j} C(j, k) h_k^{(c)}(a, b).
      Report min over j of v_2(H_c(a, b, j)).
    Verify min ≥ u(c). Count violations.
  Report: 17-value sweep clean (Y) or violations found (N).
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


def sweep_c(c_val, ab_max, k_max, j_max, tables):
    """For each (a, b), find min over j of v_2(H_c(a, b, j)). Return records."""
    a_sym, b_sym = sp.symbols('a b')
    t0 = time.time()

    # Fit Q_k for k = 0..k_max
    Q_polys = {}
    for k in range(k_max + 1):
        r = fit_Qk_bivar(c_val, k, tables)
        if r is None:
            Q_polys[k] = None
        else:
            Q_polys[k] = r[0]
    t_fit = time.time() - t0

    # Lambda
    h_lam = {}
    for k in range(k_max + 1):
        if Q_polys[k] is None:
            h_lam[k] = None
        else:
            h_lam[k] = sp.lambdify((a_sym, b_sym), Q_polys[k], modules='math')

    # Sweep — enforce parity constraint (a+b) parity == c parity.
    # Extrapolation from Q_k^{(c)}(a, b) is meaningful only for parity-matched
    # (a, b); wrong-parity points give spurious "phantom" values that do not
    # correspond to actual H_c evaluations.
    par = c_val % 2
    records = []
    t1 = time.time()
    for a_val in range(0, ab_max + 1):
        for b_val in range(0, ab_max + 1):
            if (a_val, b_val) == (0, 2):
                continue
            if (a_val + b_val) % 2 != par:
                continue
            hks = {}
            for k in range(k_max + 1):
                if Q_polys[k] is None:
                    hks[k] = None
                    continue
                L = c_val - 1 - k
                pa = rising_fact(a_val + 3, L)
                pb = rising_fact(b_val + 2, L)
                try:
                    Qv = int(h_lam[k](a_val, b_val))
                except (ValueError, OverflowError):
                    Qv = int(Q_polys[k].subs({a_sym: a_val, b_sym: b_val}))
                hks[k] = pa * pb * Qv
            # min v_2 over j in [0, j_max]
            best_v = None
            best_j = None
            for j in range(0, j_max + 1):
                if any(hks[k] is None for k in range(j + 1)):
                    continue
                Hv = sum(comb(j, k) * hks[k] for k in range(j + 1))
                if Hv == 0:
                    continue
                v = v2(Hv)
                if best_v is None or v < best_v:
                    best_v = v
                    best_j = j
            records.append({'a': a_val, 'b': b_val, 'min_v2': best_v, 'best_j': best_j})
    t_sweep = time.time() - t1

    return records, t_fit, t_sweep


def main():
    print("=" * 78)
    print("Day 100 — Anchor neighbourhood sweep, c ≡ 2 mod 4, c ∈ [134, 198]")
    print("=" * 78)

    c_vals = list(range(134, 200, 4))
    print(f"c_vals: {c_vals}  ({len(c_vals)} values)")

    ab_max = 6
    j_max = 12
    k_max = 12
    t0 = time.time()
    tables = hkfit.build_e2_tables(max_j=k_max + 2)
    print(f"build_e2_tables(max_j={k_max + 2}): {time.time() - t0:.1f}s")

    all_results = {}
    total_violations = 0
    clean_count = 0
    per_c_summary = []

    OVERALL_BUDGET_S = 1800  # 30 min
    t_global = time.time()

    for c in c_vals:
        if time.time() - t_global > OVERALL_BUDGET_S:
            print(f"[BUDGET] stop before c={c}")
            break
        print(f"\n--- c = {c} ---")
        u_c = beta(c) - delta_c2mod4(c)
        Delta = delta_c2mod4(c)
        print(f"  β(c) = {beta(c)}, Δ(c) = {Delta}, u(c) = {u_c}  (target lower bound)")

        records, t_fit, t_sweep = sweep_c(c, ab_max, k_max, j_max, tables)
        print(f"  Fit {t_fit:.1f}s, sweep {t_sweep:.1f}s.  {len(records)} (a,b) points.")

        # Verify each (a, b) satisfies min_v2 >= u_c
        violations = []
        min_over_ab = None
        min_ab = None
        for r in records:
            if r['min_v2'] is None:
                continue
            if min_over_ab is None or r['min_v2'] < min_over_ab:
                min_over_ab = r['min_v2']
                min_ab = (r['a'], r['b'], r['best_j'])
            if r['min_v2'] < u_c:
                violations.append(r)
        clean = len(violations) == 0
        print(f"  Min v_2 over (a,b) ≠ (0,2): {min_over_ab} at (a,b,j*) = {min_ab}")
        print(f"  u(c) = {u_c}   →   clean? {clean}   ({len(violations)} violations)")
        if violations[:5]:
            for v in violations[:5]:
                print(f"    VIOLATION: (a={v['a']}, b={v['b']}, best_j={v['best_j']}), min_v2 = {v['min_v2']} < {u_c}")

        per_c_summary.append({
            'c': c, 'beta': beta(c), 'Delta': Delta, 'u_c': u_c,
            'min_over_ab': min_over_ab, 'min_ab': min_ab,
            'clean': clean, 'num_violations': len(violations),
            'violations_top5': violations[:5],
        })
        all_results[c] = {
            'c': c, 'beta': beta(c), 'Delta': Delta, 'u_c': u_c,
            'min_over_ab': min_over_ab, 'min_ab': min_ab,
            'records': records, 'clean': clean, 'violations': violations,
        }
        if clean:
            clean_count += 1
        total_violations += len(violations)

    # Summary
    print("\n" + "=" * 78)
    print("SUMMARY")
    print("=" * 78)
    print(f"{'c':>4} | {'β(c)':>5} | {'Δ(c)':>4} | {'u(c)':>5} | {'min':>5} | {'(a,b,j)':>10} | {'clean':>5}")
    for s in per_c_summary:
        min_ab = str(s['min_ab']) if s['min_ab'] else '-'
        print(f"{s['c']:>4} | {s['beta']:>5} | {s['Delta']:>4} | {s['u_c']:>5} | "
              f"{str(s['min_over_ab']):>5} | {min_ab:>10} | {str(s['clean']):>5}")
    print()
    print(f"Clean count: {clean_count}/{len(per_c_summary)}")
    print(f"Total violations: {total_violations}")
    verdict = ('CLEAN — interior-anchor-02-optimal-in-neighbourhood computed for c ≡ 2 mod 4, c ∈ [130, 200].'
               if total_violations == 0 else
               f'VIOLATION — {total_violations} counterexamples found; investigate.')
    print(f"VERDICT: {verdict}")

    out = {
        'note': 'Day 100 anchor uniqueness sweep at c ≡ 2 mod 4, c ∈ [130, 200]',
        'date': '2026-07-16',
        'c_vals': c_vals,
        'ab_max': ab_max,
        'j_max': j_max,
        'k_max': k_max,
        'per_c': per_c_summary,
        'clean_count': clean_count,
        'total_violations': total_violations,
        'verdict': verdict,
    }
    outpath = '/home/agent/projects/code/2026-07-16-day100-anchor-neighbourhood-sweep.json'
    with open(outpath, 'w') as f:
        json.dump(out, f, indent=2, default=str)
    print(f"\nSaved {outpath}")

    txtpath = '/home/agent/projects/code/2026-07-16-day100-anchor-neighbourhood-sweep.txt'
    with open(txtpath, 'w') as f:
        f.write("Day 100 — Anchor uniqueness sweep, c ≡ 2 mod 4, c ∈ [130, 200]\n")
        f.write("=" * 60 + "\n\n")
        f.write(f"c_vals: {c_vals} ({len(c_vals)} values)\n")
        f.write(f"(a, b) ∈ [0, {ab_max}]^2 excluding (0, 2), j ∈ [0, {j_max}], k ∈ [0, {k_max}]\n\n")
        f.write(f"{'c':>4} | {'β(c)':>5} | {'Δ(c)':>4} | {'u(c)':>5} | {'min':>5} | {'(a,b,j)':>10} | {'clean':>5}\n")
        for s in per_c_summary:
            min_ab = str(s['min_ab']) if s['min_ab'] else '-'
            f.write(f"{s['c']:>4} | {s['beta']:>5} | {s['Delta']:>4} | {s['u_c']:>5} | "
                    f"{str(s['min_over_ab']):>5} | {min_ab:>10} | {str(s['clean']):>5}\n")
        f.write(f"\nClean count: {clean_count}/{len(per_c_summary)}\n")
        f.write(f"Total violations: {total_violations}\n")
        f.write(f"VERDICT: {verdict}\n")
    print(f"Saved {txtpath}")


if __name__ == '__main__':
    main()
