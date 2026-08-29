"""Master identity (M) verification, wide k range.

  (M)  Q_k(-2, b, c) = (-1)^k * c * (c-k) * prod_{j=1}^{k-1} (c-j)^2   for k >= 1
       Q_k(a, -1, c) = same RHS                                        (Appendix F symmetry)

Both sides should be b-independent (resp. a-independent) and match RHS as polys in c.

Strategy per k:
  1. Fit Q_k(a,b) via d102.fit_Qk_bivar at many concrete c-values.
  2. Substitute a=-2 (resp. b=-1). Check remaining var-independence.
  3. Collect (c, const_val) samples. Fit 1-var poly in c (deg = 2k).
  4. Compare to RHS.
"""
import sys
import time
from importlib import util

sys.path.insert(0, '/home/agent/projects/code')

import sympy as sp
from sympy import symbols, Matrix, expand, factor, Poly

spec_hk = util.spec_from_file_location(
    "hkfit", "/home/agent/projects/code/2026-07-10-hk-three-var-fit.py"
)
hkfit = util.module_from_spec(spec_hk)
spec_hk.loader.exec_module(hkfit)

spec_d102 = util.spec_from_file_location(
    "d102", "/home/agent/projects/code/2026-07-18-day102-anchor-810-1214-probe.py"
)
d102 = util.module_from_spec(spec_d102)
spec_d102.loader.exec_module(d102)


A, B, C = symbols('a b c')


def rhs(k):
    p = (-1) ** k * C * (C - k)
    for j in range(1, k):
        p *= (C - j) ** 2
    return sp.expand(p)


def fit_c_poly(samples, deg):
    N = deg + 1
    if len(samples) < N:
        return None
    rows = [[cv ** i for i in range(N)] for (cv, _) in samples]
    yy = [val for (_, val) in samples]
    M = Matrix(rows)
    y = Matrix(yy)
    aug = M.row_join(y)
    rref, piv = aug.rref()
    if (aug.cols - 1) in piv:
        return None
    if len(piv) < N:
        return None
    sol = [rref[piv.index(i), aug.cols - 1] for i in range(N)]
    poly = sum(sol[i] * C ** i for i in range(N))
    for (cv, val) in samples:
        if poly.subs(C, cv) != val:
            return None
    return sp.expand(poly)


def slice_and_extract(k, slice_var, slice_val, tables, c_vals, log):
    """slice_var in {'a','b'}. Return list of (c, const_val), and indep flag."""
    sub_sym = A if slice_var == 'a' else B
    rem_sym = B if slice_var == 'a' else A
    samples = []
    indep = True
    max_bdeg = 0
    for cv in c_vals:
        r = d102.fit_Qk_bivar(cv, k, tables)
        if r is None:
            log.append(f"    k={k} c={cv} slice {slice_var}={slice_val}: fit FAILED")
            continue
        Q = r[0]
        Qs = sp.expand(Q.subs(sub_sym, slice_val))
        if Qs == 0:
            samples.append((cv, 0))
            continue
        Qp = Poly(Qs, rem_sym)
        d = Qp.degree()
        if d > 0:
            indep = False
            max_bdeg = max(max_bdeg, d)
            log.append(f"    k={k} c={cv} slice {slice_var}={slice_val}: NOT INDEPENDENT (deg {d})")
        samples.append((cv, Qp.nth(0)))
    return samples, indep, max_bdeg


def verify_k(k, k_max_tables, log):
    print(f"\n=== k = {k} ===", flush=True)
    log.append(f"\n=== k = {k} ===")

    # Need at least 2k+1 c-values; add margin. Q_k(-2,b,c) has c-degree 2k.
    n_c = max(2 * k + 5, 8)
    c_start = k + 2  # need L = c-1-k >= 0, so c >= k+1; use k+2 for safety
    c_vals = list(range(c_start, c_start + n_c))

    # a=-2 slice
    t0 = time.time()
    a_samples, a_indep, a_bdeg = slice_and_extract(k, 'a', -2, k_max_tables, c_vals, log)
    t_a = time.time() - t0

    # b=-1 slice
    t0 = time.time()
    b_samples, b_indep, b_bdeg = slice_and_extract(k, 'b', -1, k_max_tables, c_vals, log)
    t_b = time.time() - t0

    R = rhs(k)

    # Fit c-poly for each
    a_poly = fit_c_poly(a_samples, 2 * k) if len(a_samples) >= 2 * k + 1 else None
    b_poly = fit_c_poly(b_samples, 2 * k) if len(b_samples) >= 2 * k + 1 else None

    a_match = (a_poly is not None) and (sp.expand(a_poly - R) == 0)
    b_match = (b_poly is not None) and (sp.expand(b_poly - R) == 0)

    # Per-sample RHS check (belt and braces)
    a_ptwise = all(v == R.subs(C, cv) for (cv, v) in a_samples)
    b_ptwise = all(v == R.subs(C, cv) for (cv, v) in b_samples)

    lines = [
        f"  a=-2 slice: b-indep={'PASS' if a_indep else f'FAIL(bdeg={a_bdeg})'}, "
        f"RHS-match={'PASS' if (a_match and a_ptwise) else 'FAIL'}, "
        f"time={t_a:.1f}s",
        f"  b=-1 slice: a-indep={'PASS' if b_indep else f'FAIL(adeg={b_bdeg})'}, "
        f"RHS-match={'PASS' if (b_match and b_ptwise) else 'FAIL'}, "
        f"time={t_b:.1f}s",
    ]
    for l in lines:
        print(l, flush=True)
        log.append(l)

    if not a_match and a_indep:
        diff = sp.expand((a_poly if a_poly else 0) - R)
        log.append(f"  a-side diff = {diff}")
        print(f"  a-side diff = {diff}", flush=True)
    if not b_match and b_indep:
        diff = sp.expand((b_poly if b_poly else 0) - R)
        log.append(f"  b-side diff = {diff}")
        print(f"  b-side diff = {diff}", flush=True)

    return {
        'k': k,
        'a_indep': a_indep, 'a_match': a_match and a_ptwise,
        'b_indep': b_indep, 'b_match': b_match and b_ptwise,
        't_a': t_a, 't_b': t_b,
        'a_samples': a_samples, 'b_samples': b_samples,
    }


def main():
    log = []
    log.append("Master identity (M) verification, k = 1..K_max")
    log.append("Q_k(-2, b, c) = Q_k(a, -1, c) = (-1)^k * c * (c-k) * prod_{j=1}^{k-1}(c-j)^2")

    K_MAX = 12  # will try to push higher if fast
    K_STRETCH = 15

    t0 = time.time()
    # Need M_j tables up to j = K_STRETCH + 2
    tables = hkfit.build_e2_tables(max_j=K_STRETCH + 2)
    log.append(f"\nbuild_e2_tables(max_j={K_STRETCH + 2}): {time.time() - t0:.1f}s")
    print(log[-1], flush=True)

    results = []
    t_start = time.time()
    BUDGET = 3000  # seconds

    for k in range(1, K_STRETCH + 1):
        if time.time() - t_start > BUDGET:
            log.append(f"\nBUDGET exceeded, stopping before k={k}")
            print(log[-1], flush=True)
            break
        try:
            r = verify_k(k, tables, log)
            results.append(r)
        except Exception as e:
            log.append(f"k={k} EXCEPTION: {e}")
            import traceback
            log.append(traceback.format_exc())
            print(log[-1], flush=True)
            break
        # Save intermediate
        with open('/home/agent/projects/beta-prime/code/2026-08-18-M-identity-verify-wide.txt', 'w') as f:
            f.write('\n'.join(log))

    # Summary table
    log.append("\n" + "=" * 70)
    log.append("SUMMARY")
    log.append("=" * 70)
    log.append(f"{'k':>3} | {'a-indep':>7} | {'a-RHS':>5} | {'b-indep':>7} | {'b-RHS':>5} | {'t_a':>6} | {'t_b':>6}")
    for r in results:
        log.append(
            f"{r['k']:>3} | "
            f"{'PASS' if r['a_indep'] else 'FAIL':>7} | "
            f"{'PASS' if r['a_match'] else 'FAIL':>5} | "
            f"{'PASS' if r['b_indep'] else 'FAIL':>7} | "
            f"{'PASS' if r['b_match'] else 'FAIL':>5} | "
            f"{r['t_a']:>5.1f}s | {r['t_b']:>5.1f}s"
        )
    for l in log[-len(results) - 4:]:
        print(l, flush=True)

    all_pass = all(r['a_indep'] and r['a_match'] and r['b_indep'] and r['b_match'] for r in results)
    verdict = ("ALL PASS through k = " + str(max(r['k'] for r in results))) if all_pass else "FAILURES DETECTED"
    log.append(f"\nVERDICT: {verdict}")
    print(f"\nVERDICT: {verdict}", flush=True)

    with open('/home/agent/projects/beta-prime/code/2026-08-18-M-identity-verify-wide.txt', 'w') as f:
        f.write('\n'.join(log))
    print("Saved.", flush=True)


if __name__ == '__main__':
    main()
