"""Shifted Appendix F identity — test the T_1 recursion hypothesis at R=3, R=4.

Given (F): Q_{2R}(-2, b, c) = Q_{2R}(a, -1, c) = P_tilde_R(c) =
             c(c-2R) * prod_{k=1}^{2R-1}(c-k)^2

Define T_1(a, b, c) := ( Q_{2R}(a, b, c) - P_tilde_R(c) ) / ( (a+2)(b+1) )

Hypothesis: T_1(-1, b, c) = T_1(a, 0, c) = P_tilde_R^{(1)}(c)
(depends only on c, both slices equal). Moreover (c-R)^2 divides P_tilde_R^{(1)}(c).

For each R in {3, 4}:
  For c = 2R+2, ..., 2R+2+N-1:
    - fit Q_{2R}^{(c)}(a, b) bivariate polynomial
    - subtract P_tilde_R(c) (a constant at fixed c)
    - divide by (a+2)(b+1) via sympy polynomial division
    - this yields T_1^{(c)}(a, b) as a bivariate polynomial

  Check A: at each c, substitute a = -1 in T_1^{(c)}, verify b-independence
  Check B: at each c, substitute b = 0 in T_1^{(c)}, verify a-independence
  Check C: verify Check A constants equal Check B constants
  Check D: if agree, fit constants as polynomial in c, check (c-R)^2 factor
"""
import sys
import time
sys.path.insert(0, '/home/agent/projects/code')

from importlib import util

import sympy as sp
from sympy import symbols, Matrix, expand, factor, Poly, div, cancel, together

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


A_SYM, B_SYM, C_SYM = sp.symbols('a b c')


def predicted_P_tilde(R):
    """P_tilde_R(c) = c(c-2R) * prod_{k=1}^{2R-1}(c-k)^2."""
    p = C_SYM * (C_SYM - 2 * R)
    for k in range(1, 2 * R):
        p *= (C_SYM - k) ** 2
    return sp.expand(p)


def get_Q_bivar_at_c(R, c_val, tables):
    k_target = 2 * R
    r = d102.fit_Qk_bivar(c_val, k_target, tables)
    if r is None:
        return None
    poly, D = r
    return sp.expand(poly)


def fit_polynomial_1var(samples, deg):
    """Fit samples [(c_i, y_i)] as poly in c of degree deg."""
    N = deg + 1
    if len(samples) < N:
        return None
    c = C_SYM
    rows = []
    yy = []
    for (cv, val) in samples:
        rows.append([cv ** k for k in range(N)])
        yy.append(val)
    A = Matrix(rows)
    y = Matrix(yy)
    aug = A.row_join(y)
    rref, pivots = aug.rref()
    if (aug.cols - 1) in pivots:
        return None
    if len(pivots) < N:
        return None
    sol = [rref[pivots.index(i), aug.cols - 1] for i in range(N)]
    poly = sum(sol[k] * c ** k for k in range(N))
    for (cv, val) in samples:
        if poly.subs(c, cv) != val:
            return None
    return sp.expand(poly)


def divide_bivar_by_ab_factor(P, a_val_root, b_val_root):
    """Divide bivariate poly P(a,b) by (a - a_val_root)(b - b_val_root) exactly.

    Since (a+2) and (b+1) each depend on only one variable, we can divide
    sequentially: first divide by (a - (-2)) treating as poly in a with
    coefficients in b, then divide the result by (b - (-1)).
    """
    # Divide P by (a + 2) as poly in a
    q1, r1 = sp.div(P, A_SYM - a_val_root, A_SYM)
    r1 = sp.expand(r1)
    if r1 != 0:
        raise ValueError(f"P not divisible by (a - {a_val_root}): remainder = {r1}")
    q1 = sp.expand(q1)
    # Now divide q1 by (b + 1) as poly in b
    q2, r2 = sp.div(q1, B_SYM - b_val_root, B_SYM)
    r2 = sp.expand(r2)
    if r2 != 0:
        raise ValueError(f"q1 not divisible by (b - {b_val_root}): remainder = {r2}")
    return sp.expand(q2)


def analyze_R(R, log_lines, num_c_samples=None):
    def out(s=""):
        print(s, flush=True)
        log_lines.append(s)

    out(f"\n{'='*70}")
    out(f"SHIFTED-F (T_1) TEST, R = {R}")
    out(f"{'='*70}")

    if num_c_samples is None:
        # Q_{2R}(a,b,c) has c-degree 4R. After subtracting P_tilde_R (deg 4R
        # in c) and dividing by (a+2)(b+1) (independent of c), T_1 slices
        # have c-degree at most 4R. Sample 4R+4 points for a safety margin.
        num_c_samples = 4 * R + 4

    c_start = 2 * R + 2
    P_tilde = predicted_P_tilde(R)
    out(f"P_tilde_R(c) = {sp.factor(P_tilde)}")

    out(f"\nBuilding M_j tables up to j = {2*R + 2} ...")
    t0 = time.time()
    tables = hkfit.build_e2_tables(max_j=2 * R + 2)
    out(f"  built in {time.time() - t0:.2f}s.")

    T1_at_c = []  # list of (c, T_1(a,b))
    t0 = time.time()
    out(f"\nFitting Q_{{{2*R}}}(a,b,c) at c = {c_start} .. {c_start + num_c_samples - 1}")
    for i in range(num_c_samples):
        cv = c_start + i
        Q_bivar = get_Q_bivar_at_c(R, cv, tables)
        if Q_bivar is None:
            out(f"  c={cv}: fit_Qk_bivar returned None, skipping")
            continue
        P_at_c = P_tilde.subs(C_SYM, cv)
        num = sp.expand(Q_bivar - P_at_c)
        # Divide by (a+2)(b+1)
        try:
            T1 = divide_bivar_by_ab_factor(num, -2, -1)
        except ValueError as e:
            out(f"  c={cv}: DIVISION FAILED: {e}")
            continue
        T1_at_c.append((cv, T1))
        elapsed = time.time() - t0
        out(f"  c={cv}: T_1 computed ({elapsed:.1f}s cumulative)")

    # Check A: T_1(-1, b, c) — substitute a=-1, examine b-dependence
    out(f"\n--- Check A: T_1(a=-1, b, c) — b-independence? ---")
    A_indep = True
    A_consts = []
    for (cv, T1) in T1_at_c:
        Ts = sp.expand(T1.subs(A_SYM, -1))
        if Ts == 0:
            deg = -1
            const_val = 0
        else:
            ps = Poly(Ts, B_SYM)
            deg = ps.degree()
            const_val = ps.nth(0)
            if deg > 0:
                coefs = ps.all_coeffs()
                nonzero_higher = [(k, c) for k, c in
                                  enumerate(reversed(coefs)) if c != 0 and k > 0]
                if nonzero_higher:
                    A_indep = False
                    out(f"    c={cv}: NOT INDEPENDENT. deg in b = {deg}, "
                        f"nonzero higher coefs: {nonzero_higher[:5]}")
                    A_consts.append((cv, None))
                    continue
        out(f"    c={cv}: b-independent, const = {const_val}")
        A_consts.append((cv, const_val))
    out(f"  Verdict: {'YES (b-independent)' if A_indep else 'NO'}")

    # Check B: T_1(a, 0, c) — substitute b=0, examine a-dependence
    out(f"\n--- Check B: T_1(a, b=0, c) — a-independence? ---")
    B_indep = True
    B_consts = []
    for (cv, T1) in T1_at_c:
        Ts = sp.expand(T1.subs(B_SYM, 0))
        if Ts == 0:
            deg = -1
            const_val = 0
        else:
            ps = Poly(Ts, A_SYM)
            deg = ps.degree()
            const_val = ps.nth(0)
            if deg > 0:
                coefs = ps.all_coeffs()
                nonzero_higher = [(k, c) for k, c in
                                  enumerate(reversed(coefs)) if c != 0 and k > 0]
                if nonzero_higher:
                    B_indep = False
                    out(f"    c={cv}: NOT INDEPENDENT. deg in a = {deg}, "
                        f"nonzero higher coefs: {nonzero_higher[:5]}")
                    B_consts.append((cv, None))
                    continue
        out(f"    c={cv}: a-independent, const = {const_val}")
        B_consts.append((cv, const_val))
    out(f"  Verdict: {'YES (a-independent)' if B_indep else 'NO'}")

    # Check C: A and B constants agree?
    out(f"\n--- Check C: A-consts vs B-consts equality ---")
    C_agree = True
    for (cv_a, va), (cv_b, vb) in zip(A_consts, B_consts):
        assert cv_a == cv_b
        if va != vb:
            C_agree = False
            out(f"    c={cv_a}: A={va}, B={vb} DISAGREE")
        else:
            out(f"    c={cv_a}: A=B={va}")
    out(f"  Verdict: {'AGREE' if C_agree else 'DISAGREE'}")

    # Check D: fit as polynomial in c, check (c-R)^2 factor
    if A_indep and B_indep and C_agree:
        out(f"\n--- Check D: fit P_tilde_R^{{(1)}}(c) as polynomial in c ---")
        samples = [(cv, v) for (cv, v) in A_consts if v is not None]
        # Try fitting at degrees from 0 to 4R+2
        max_deg = 4 * R + 2
        fitted = None
        fitted_deg = None
        for d in range(0, max_deg + 1):
            if len(samples) < d + 1:
                break
            # Use first d+1 samples for fit; verify on the rest
            fit_samples = samples[:d + 1]
            check_samples = samples[d + 1:]
            poly = fit_polynomial_1var(fit_samples, d)
            if poly is None:
                continue
            ok = True
            for (cv, v) in check_samples:
                if poly.subs(C_SYM, cv) != v:
                    ok = False
                    break
            if ok and len(check_samples) > 0:
                fitted = poly
                fitted_deg = d
                break

        if fitted is None:
            out(f"  Could not fit polynomial up to degree {max_deg}.")
        else:
            out(f"  Fitted degree = {fitted_deg}")
            out(f"  P_tilde_R^{{(1)}}(c) = {sp.expand(fitted)}")
            fac = sp.factor(fitted)
            out(f"  Factored:              {fac}")
            # Check (c - R)^2 divides fitted
            q, r = sp.div(fitted, (C_SYM - R) ** 2, C_SYM)
            r_exp = sp.expand(r)
            if r_exp == 0:
                out(f"  (c - {R})^2 IS a factor.")
                out(f"  Quotient P_tilde_R^{{(1)}}(c) / (c-{R})^2 = "
                    f"{sp.factor(q)}")
            else:
                out(f"  (c - {R})^2 is NOT a factor; remainder = {r_exp}")
            # Also check (c-R) factor at least
            q1, r1 = sp.div(fitted, (C_SYM - R), C_SYM)
            r1_exp = sp.expand(r1)
            if r1_exp == 0:
                # Compute multiplicity of (c-R) root
                mult = 0
                cur = fitted
                while True:
                    qq, rr = sp.div(cur, (C_SYM - R), C_SYM)
                    if sp.expand(rr) != 0:
                        break
                    mult += 1
                    cur = qq
                out(f"  Multiplicity of (c-{R}) root = {mult}")
            else:
                out(f"  (c - {R}) is NOT a factor of P_tilde_R^{{(1)}}(c)")

            return {
                'A_indep': A_indep, 'B_indep': B_indep, 'C_agree': C_agree,
                'fitted': fitted, 'fitted_deg': fitted_deg,
            }
    return {
        'A_indep': A_indep, 'B_indep': B_indep, 'C_agree': C_agree,
        'fitted': None,
    }


def main():
    log_lines = []

    def out(s=""):
        print(s, flush=True)
        log_lines.append(s)

    out("Shifted Appendix F (T_1 recursion) test at R = 3 (and R = 4 if time).")
    out("Hypothesis: T_1(-1,b,c) = T_1(a,0,c) = P_tilde_R^{(1)}(c),")
    out("            with (c-R)^2 as a factor.")

    results = {}
    for R in [3, 4]:
        t_start = time.time()
        try:
            results[R] = analyze_R(R, log_lines)
        except Exception as e:
            out(f"R={R} FAILED: {e}")
            import traceback
            tb = traceback.format_exc()
            out(tb)
            results[R] = None
        t_end = time.time()
        out(f"\nR={R} total time: {t_end - t_start:.1f}s")

    out("\n" + "=" * 70)
    out("SUMMARY")
    out("=" * 70)
    for R, res in results.items():
        out(f"\nR = {R}:")
        if res is None:
            out("  FAILED")
            continue
        out(f"  A (b-indep at a=-1): {res['A_indep']}")
        out(f"  B (a-indep at b= 0): {res['B_indep']}")
        out(f"  C (A==B):            {res['C_agree']}")
        if res.get('fitted') is not None:
            out(f"  fitted deg:          {res['fitted_deg']}")
            out(f"  P_tilde^(1):         {sp.factor(res['fitted'])}")

    # Save log
    out_path = "/home/agent/projects/beta-prime/code/2026-08-15-shifted-F-R3-R4.txt"
    with open(out_path, "w") as f:
        f.write("\n".join(log_lines) + "\n")
    print(f"\n[wrote log to {out_path}]", flush=True)


if __name__ == "__main__":
    main()
