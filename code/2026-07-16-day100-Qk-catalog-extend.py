"""Day 100 (2026-07-16) — Q_k catalog extension for k = 7, 8.

Strategy: coefficient-wise interpolation.
  1. For c ∈ {k+2, k+3, ..., k+20}, fit Q_k^{(c)}(a, b) as bivariate polynomial.
  2. Extract each (a, b) monomial coefficient as function of c.
  3. Fit each coefficient as a polynomial in c.
  4. Assemble Q_k(a, b, c) and verify at held-out c values.

Feeds Day 101+ PROVE c-odd sweep at higher k.
"""

import json
import time
from importlib import util

import sympy as sp
from sympy import Matrix, Rational, expand, factor, symbols

spec = util.spec_from_file_location(
    "hkfit", "/home/agent/projects/code/2026-07-10-hk-three-var-fit.py"
)
hkfit = util.module_from_spec(spec)
spec.loader.exec_module(hkfit)


def rising_fact(x, n):
    if n <= 0:
        return 1
    p = 1
    for i in range(n):
        p *= (x + i)
    return p


def fit_Qk_bivar(c_val, k_target, tables):
    """Fit Q_k^{(c)}(a, b) as bivariate polynomial. Return {monomial: coef} dict, degree."""
    L = c_val - 1 - k_target
    if L < 0:
        return None
    bd = 2 * (k_target // 2)
    max_deg_try = bd + 6
    max_monos = (max_deg_try + 1) * (max_deg_try + 2) // 2
    num_pts_target = max_monos + 20
    samples = []
    a = c_val
    while len(samples) < num_pts_target and a < c_val + 60:
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
        M = Matrix(rows)
        y = Matrix(yvals)
        aug = M.row_join(y)
        rref, pivots = aug.rref()
        if (aug.cols - 1) in pivots:
            continue
        if len(pivots) != nm:
            continue
        sol = [rref[pivots.index(i), aug.cols - 1] for i in range(nm)]
        coefs = {mono: coef for mono, coef in zip(monos, sol)}
        # Verify
        ok = True
        for (av, bv, yv) in samples:
            s = sum(int(coefs[m]) * av ** m[0] * bv ** m[1] for m in monos)
            if s != yv:
                ok = False
                break
        if not ok:
            continue
        return coefs, D
    return None


def fit_c_polynomial(c_vals, y_vals, max_deg):
    """Fit y_vals = poly(c_vals) as polynomial in c of degree ≤ max_deg."""
    if all(y == 0 for y in y_vals):
        return 0, 0
    if len(c_vals) < max_deg + 1:
        return None
    for deg in range(0, max_deg + 1):
        nm = deg + 1
        if len(c_vals) < nm + 2:
            break
        A_rows = [[cv ** k for k in range(deg + 1)] for cv in c_vals]
        A = Matrix(A_rows)
        y = Matrix(y_vals)
        aug = A.row_join(y)
        rref, pivots = aug.rref()
        if (aug.cols - 1) in pivots:
            continue
        if len(pivots) != nm:
            continue
        sol = [rref[pivots.index(i), aug.cols - 1] for i in range(nm)]
        # Verify
        ok = True
        for cv, yv in zip(c_vals, y_vals):
            s = sum(int(sol[k]) * cv ** k for k in range(nm))
            if s != yv:
                ok = False
                break
        if ok:
            c = symbols('c')
            poly = sum(int(sol[k]) * c ** k for k in range(nm))
            return poly, deg
    return None


def extend_Qk(k_target, c_min, c_max, max_c_deg, tables):
    print(f"\n{'=' * 78}")
    print(f"Q_{k_target}(a, b, c) — coefficient interpolation")
    print(f"{'=' * 78}")
    c_fit_vals = list(range(c_min, c_max + 1))
    print(f"  c-values: {c_fit_vals} ({len(c_fit_vals)} values)")

    # Step 1: per-c bivariate fits
    per_c_coefs = {}
    max_D_seen = 0
    t0 = time.time()
    for c_val in c_fit_vals:
        r = fit_Qk_bivar(c_val, k_target, tables)
        if r is None:
            print(f"    c={c_val}: FIT FAILED")
            continue
        coefs, D = r
        per_c_coefs[c_val] = coefs
        max_D_seen = max(max_D_seen, D)
        print(f"    c={c_val}: bivariate deg {D} ({len(coefs)} monomials)")
    print(f"  bivariate fits: {time.time() - t0:.1f}s")

    if len(per_c_coefs) < max_c_deg + 2:
        print("  Too few c-values fit successfully.")
        return None

    # Step 2: union of monomials across all c
    all_monos = set()
    for c_val, coefs in per_c_coefs.items():
        all_monos.update(coefs.keys())
    all_monos = sorted(all_monos)
    print(f"  Union of (a,b) monomials: {len(all_monos)} = degree ≤ {max_D_seen}")

    # Step 3: per-monomial c-fit
    a_sym, b_sym, c_sym = symbols('a b c')
    Q_kabc = 0
    per_coef_deg = {}
    fail_count = 0
    t0 = time.time()
    for (da, db) in all_monos:
        c_vals_list = []
        y_vals_list = []
        for c_val, coefs in per_c_coefs.items():
            coef_val = coefs.get((da, db), 0)
            c_vals_list.append(c_val)
            y_vals_list.append(int(coef_val))
        r = fit_c_polynomial(c_vals_list, y_vals_list, max_c_deg)
        if r is None:
            fail_count += 1
            continue
        c_poly, c_deg = r
        per_coef_deg[(da, db)] = c_deg
        Q_kabc += c_poly * a_sym ** da * b_sym ** db
    Q_kabc = expand(Q_kabc)
    print(f"  per-coef c-fits: {time.time() - t0:.1f}s, {fail_count} failures")
    if fail_count > 0:
        print(f"  ({fail_count} monomials had c-coefficient sequences non-polynomial or under-determined)")

    # Step 4: verify at hold-out c-values (outside fit range if any)
    holdout = [c_max + 1, c_max + 2, c_max + 3]
    print(f"  Cross-validating at c = {holdout}...")
    cv_ok = 0
    cv_fail = 0
    for c_val in holdout:
        r = fit_Qk_bivar(c_val, k_target, tables)
        if r is None:
            print(f"    c={c_val}: could not extract for CV.")
            continue
        coefs_actual, _ = r
        # Compare
        for (da, db), coef_actual in coefs_actual.items():
            pred = Q_kabc.coeff(a_sym, da).coeff(b_sym, db)
            pred_at_c = int(pred.subs({c_sym: c_val}))
            if int(coef_actual) == pred_at_c:
                cv_ok += 1
            else:
                cv_fail += 1
                if cv_fail <= 3:
                    print(f"    CV FAIL at c={c_val}, mono ({da},{db}): "
                          f"pred={pred_at_c} actual={int(coef_actual)}")
    print(f"  CV: {cv_ok} pass, {cv_fail} fail")

    Q_fact = factor(Q_kabc) if cv_fail == 0 else None
    if cv_fail == 0:
        total_deg = sp.total_degree(Q_kabc)
        print(f"  Q_{k_target}(a,b,c) total degree = {total_deg}")
        print(f"  Q_{k_target}(a,b,c) factored = {Q_fact}")

    return {
        'k': k_target,
        'c_fit_range': (c_min, c_max),
        'ab_max_deg': max_D_seen,
        'poly_expanded': str(Q_kabc),
        'poly_factored': str(Q_fact) if cv_fail == 0 else None,
        'total_degree': sp.total_degree(Q_kabc) if cv_fail == 0 else None,
        'cv_ok': cv_ok,
        'cv_fail': cv_fail,
        'per_coef_c_degree_max': max(per_coef_deg.values()) if per_coef_deg else None,
    }


def main():
    print("=" * 78)
    print("Day 100 — Q_k catalog extension for k = 7, 8")
    print("=" * 78)

    tables = hkfit.build_e2_tables(max_j=10 + 2)

    results = {}
    for k in [7, 8]:
        c_min = k + 2
        # Need c-poly fit at deg up to ~2k. Provide enough c-values.
        c_max = k + 30
        max_c_deg = 22
        t0 = time.time()
        r = extend_Qk(k, c_min, c_max, max_c_deg, tables)
        print(f"  k={k} total wall: {time.time() - t0:.1f}s")
        results[k] = r

    # Save
    out = {
        'note': 'Day 100 — Q_7 and Q_8 c-general via coefficient interpolation',
        'date': '2026-07-16',
        'per_k': {str(k): results[k] for k in [7, 8]},
    }
    outpath = '/home/agent/projects/code/2026-07-16-day100-Qk-catalog-extend.json'
    with open(outpath, 'w') as f:
        json.dump(out, f, indent=2, default=str)
    print(f"\nSaved {outpath}")

    txtpath = '/home/agent/projects/code/2026-07-16-day100-Qk-catalog-extend.txt'
    with open(txtpath, 'w') as f:
        f.write(f"Day 100 — Q_k catalog extension (k = 7, 8)\n{'=' * 60}\n\n")
        for k in [7, 8]:
            r = results[k]
            if r is None:
                f.write(f"k = {k}: FIT FAILED\n\n")
                continue
            f.write(f"k = {k}:\n")
            f.write(f"  c fit range: {r['c_fit_range']}\n")
            f.write(f"  (a,b) max degree seen: {r['ab_max_deg']}\n")
            f.write(f"  CV: {r['cv_ok']} pass, {r['cv_fail']} fail\n")
            if r['cv_fail'] == 0:
                f.write(f"  Total degree: {r['total_degree']}\n")
                f.write(f"  Q_{k}(a,b,c) factored:\n    {r['poly_factored']}\n")
            f.write("\n")
    print(f"Saved {txtpath}")


if __name__ == '__main__':
    main()
