"""Test whether h_k^{(c)}(-2, b) factors as (b+2)_{c-1-k} * g_k(c)
where g_k(c) is a polynomial in c ALONE (no b dependence).

Strategy:
  For each c in a set of concrete integers, and each k in 0..2R:
    1. Fit Q_k^{(c)}(a, b) as bivariate polynomial via d102.fit_Qk_bivar.
    2. Reconstruct h_k^{(c)}(a, b) via the identity
           h_k(a, b, c) = Q_k(a, b) * (a+3)_{c-1-k} * (b+2)_{c-1-k}
       (this is how fit_Qk_bivar defines "Q_k").
    3. Substitute a = -2. Since (a+3)_{c-1-k} at a=-2 is (1)_{L} = L!,
           h_k^{(c)}(-2, b) = L! * (b+2)_L * Q_k(-2, b).
       So the factor (b+2)_L is present iff Q_k(-2, b) is a polynomial
       in b (it is, since Q_k is polynomial). The stronger question is
       whether Q_k(-2, b) is INDEPENDENT of b -- which then gives
           g_k(c) = L! * Q_k(-2, b_symbolic)  (as a value of c only).
    4. Report for each (R, c, k):
       - Whether Q_k(-2, b) is b-independent (equivalently whether
         h_k(-2, b) / (b+2)_L is b-independent).
       - If yes: extract g_k(c) = L! * Q_k(-2, .).
       - If no: report the b-polynomial (or the b-factor that DOES appear).
"""
import sys
import time
from importlib import util

sys.path.insert(0, '/home/agent/projects/code')

import sympy as sp
from sympy import symbols, Poly, expand, factor, factorial

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


A_SYM, B_SYM, C_SYM = symbols('a b c')


def rising_fact(x, n):
    if n <= 0:
        return 1
    p = 1
    for i in range(n):
        p *= (x + i)
    return p


def rising_fact_sym(x, n):
    if n <= 0:
        return sp.Integer(1)
    p = sp.Integer(1)
    for i in range(n):
        p *= (x + i)
    return p


def analyze_hk_at_a_minus_2(R, c_val, tables, out_lines):
    """For c=c_val and k=0..2R, test whether h_k^{(c)}(-2, b) has (b+2)_{c-1-k}
    as a factor with a b-independent quotient."""
    two_R = 2 * R
    line = f"\n--- R={R}, c={c_val} ---"
    print(line, flush=True)
    out_lines.append(line)

    results = []
    for k in range(two_R + 1):
        L = c_val - 1 - k
        t0 = time.time()
        r = d102.fit_Qk_bivar(c_val, k, tables)
        dt = time.time() - t0
        if r is None:
            line = f"  k={k:2d}: fit_Qk_bivar FAILED ({dt:.1f}s)"
            print(line, flush=True)
            out_lines.append(line)
            results.append((k, None))
            continue
        Q_poly, D = r
        Q_at_am2 = expand(Q_poly.subs(A_SYM, -2))

        # Check b-independence of Q_k(-2, b)
        if Q_at_am2 == 0:
            b_indep = True
            b_deg = -1
            g_val = 0
        else:
            Qp = Poly(Q_at_am2, B_SYM)
            b_deg = Qp.degree()
            if b_deg <= 0:
                b_indep = True
                g_val = Q_at_am2  # constant
            else:
                b_indep = False
                g_val = None

        if b_indep:
            # h_k(-2, b) = L! * (b+2)_L * Q_at_am2
            g_k = factorial(L) * g_val
            g_k_simplified = sp.simplify(g_k)
            line = (f"  k={k:2d}: L={L:2d}, D(Q)={D}, "
                    f"Q_k(-2,b) is b-INDEPENDENT = {g_val}, "
                    f"g_k = L! * Q(-2,.) = {g_k_simplified}  ({dt:.1f}s)")
            print(line, flush=True)
            out_lines.append(line)
            results.append((k, {'b_indep': True, 'Q_at_am2': g_val,
                                 'g_k': g_k_simplified, 'L': L}))
        else:
            # Not b-independent. Report the b-polynomial.
            line = (f"  k={k:2d}: L={L:2d}, D(Q)={D}, "
                    f"Q_k(-2,b) has b-degree {b_deg}, NOT b-independent  ({dt:.1f}s)")
            print(line, flush=True)
            out_lines.append(line)
            line = f"       Q_k(-2, b) = {Q_at_am2}"
            print(line, flush=True)
            out_lines.append(line)
            # Also express h_k(-2, b) / (b+2)_L to see what remains.
            #   h_k(-2, b) = L! * (b+2)_L * Q_k(-2, b)
            # so h_k(-2, b) / (b+2)_L = L! * Q_k(-2, b) -- which is the b-poly.
            # But maybe a DIFFERENT rising factorial divides it. Let's try to factor.
            fac = factor(Q_at_am2)
            line = f"       factored form = {fac}"
            print(line, flush=True)
            out_lines.append(line)
            results.append((k, {'b_indep': False, 'Q_at_am2': Q_at_am2,
                                 'factored': fac, 'L': L}))
    return results


def collect_g_k_of_c(R, all_results, out_lines):
    """For each k, tabulate g_k as function of c across our c-samples;
    try to fit as polynomial in c."""
    two_R = 2 * R
    line = f"\n\n=== R={R}: g_k(c) tabulated across c ==="
    print(line, flush=True)
    out_lines.append(line)

    for k in range(two_R + 1):
        samples = []
        for c_val, res_list in all_results:
            entry = next((v for kk, v in res_list if kk == k), None)
            if entry is None or not entry.get('b_indep', False):
                continue
            samples.append((c_val, sp.Integer(entry['g_k'])))
        if not samples:
            line = f"  k={k:2d}: no b-independent samples"
            print(line, flush=True)
            out_lines.append(line)
            continue

        # Try polynomial fit in c.
        n = len(samples)
        # Attempt up to degree n-1
        c = C_SYM
        fitted = None
        for deg in range(min(n, 20)):
            N = deg + 1
            if n < N:
                break
            rows = []
            yy = []
            for (cv, val) in samples:
                rows.append([cv ** kk for kk in range(N)])
                yy.append(val)
            M = sp.Matrix(rows)
            y = sp.Matrix(yy)
            aug = M.row_join(y)
            rref, pivots = aug.rref()
            if (aug.cols - 1) in pivots:
                continue
            if len(pivots) < N:
                continue
            sol = [rref[pivots.index(i), aug.cols - 1] for i in range(N)]
            poly = sum(sol[kk] * c ** kk for kk in range(N))
            poly = sp.expand(poly)
            ok = all(poly.subs(c, cv) == val for (cv, val) in samples)
            if ok:
                fitted = (deg, poly)
                break

        line = f"  k={k:2d}: samples (c, g_k(c)):"
        print(line, flush=True)
        out_lines.append(line)
        for (cv, val) in samples:
            line = f"      c={cv:2d}: {val}"
            print(line, flush=True)
            out_lines.append(line)
        if fitted is not None:
            deg, poly = fitted
            fpoly = factor(poly)
            line = f"    Fitted deg-{deg} poly in c: g_k(c) = {fpoly}"
            print(line, flush=True)
            out_lines.append(line)
        else:
            line = f"    (no polynomial fit found)"
            print(line, flush=True)
            out_lines.append(line)


def main():
    out_lines = []
    banner = ("h_k^{(c)}(-2, b) factorization test\n"
              "Hypothesis (F1): h_k^{(c)}(-2, b) = (b+2)_{c-1-k} * g_k(c)\n"
              "Method: fit Q_k(a,b) via d102.fit_Qk_bivar, substitute a=-2,\n"
              "  check b-independence of Q_k(-2, b). Then\n"
              "  g_k(c) = (c-1-k)! * Q_k(-2, b_any).")
    print(banner)
    out_lines.append(banner)

    # R = 3
    R = 3
    c_vals_R3 = list(range(8, 16))  # 8..15
    two_R = 2 * R
    line = f"\n\n{'='*60}\nBuilding tables for R={R} (max_j = {two_R+2})...\n{'='*60}"
    print(line, flush=True)
    out_lines.append(line)
    t0 = time.time()
    tables = hkfit.build_e2_tables(max_j=two_R + 2)
    line = f"  built in {time.time() - t0:.1f}s"
    print(line, flush=True)
    out_lines.append(line)

    all_results_R3 = []
    for c_val in c_vals_R3:
        res = analyze_hk_at_a_minus_2(R, c_val, tables, out_lines)
        all_results_R3.append((c_val, res))
        # Save intermediate
        with open('/home/agent/projects/beta-prime/code/2026-08-15-hk-factor-a-minus-2.txt', 'w') as f:
            f.write('\n'.join(str(l) for l in out_lines))

    collect_g_k_of_c(R, all_results_R3, out_lines)
    with open('/home/agent/projects/beta-prime/code/2026-08-15-hk-factor-a-minus-2.txt', 'w') as f:
        f.write('\n'.join(str(l) for l in out_lines))

    # Try R=4 as bonus
    line = f"\n\n{'='*60}\nR=4 BONUS\n{'='*60}"
    print(line, flush=True)
    out_lines.append(line)

    R = 4
    c_vals_R4 = list(range(10, 16))  # 10..15
    two_R = 2 * R
    line = f"Building tables for R={R} (max_j = {two_R+2})..."
    print(line, flush=True)
    out_lines.append(line)
    t0 = time.time()
    tables_R4 = hkfit.build_e2_tables(max_j=two_R + 2)
    line = f"  built in {time.time() - t0:.1f}s"
    print(line, flush=True)
    out_lines.append(line)

    all_results_R4 = []
    for c_val in c_vals_R4:
        try:
            res = analyze_hk_at_a_minus_2(R, c_val, tables_R4, out_lines)
            all_results_R4.append((c_val, res))
        except Exception as e:
            line = f"  R=4 c={c_val} FAILED: {e}"
            print(line, flush=True)
            out_lines.append(line)
        with open('/home/agent/projects/beta-prime/code/2026-08-15-hk-factor-a-minus-2.txt', 'w') as f:
            f.write('\n'.join(str(l) for l in out_lines))

    if all_results_R4:
        collect_g_k_of_c(R, all_results_R4, out_lines)

    # Summary
    line = "\n\n" + "=" * 60 + "\nSUMMARY\n" + "=" * 60
    print(line, flush=True)
    out_lines.append(line)

    for R_lbl, all_results in [(3, all_results_R3), (4, all_results_R4)]:
        two_R = 2 * R_lbl
        line = f"\nR = {R_lbl}:"
        print(line, flush=True)
        out_lines.append(line)
        # tabulate Y/N table
        header = f"    c \\ k | " + " | ".join(f"{k:2d}" for k in range(two_R + 1))
        print(header, flush=True)
        out_lines.append(header)
        for (cv, res_list) in all_results:
            row_vals = []
            for k in range(two_R + 1):
                entry = next((v for kk, v in res_list if kk == k), None)
                if entry is None:
                    row_vals.append(" ?")
                elif entry.get('b_indep', False):
                    row_vals.append(" Y")
                else:
                    row_vals.append(" N")
            line = f"    c={cv:2d}  | " + " | ".join(row_vals)
            print(line, flush=True)
            out_lines.append(line)

    with open('/home/agent/projects/beta-prime/code/2026-08-15-hk-factor-a-minus-2.txt', 'w') as f:
        f.write('\n'.join(str(l) for l in out_lines))
    print(f"\nSaved to /home/agent/projects/beta-prime/code/2026-08-15-hk-factor-a-minus-2.txt")


if __name__ == "__main__":
    main()
