"""Iterated recursion levels for Q_{2R} — Day 108 continuation.

Level 0 base identity (Appendix F, verified R=2..6):
    Q_{2R}(-2, b, c) = Q_{2R}(a, -1, c) = P_tilde_R^{(0)}(c)
        = c(c-2R) * prod_{k=1}^{2R-1}(c-k)^2

Level k recursion (hypothesis):
    T_{k}(a, b, c) := ( T_{k-1}(a, b, c) - P_tilde_R^{(k-1)}(c) ) / ( (a + 2 - (k-1)) * (b + 1 - (k-1)) )
                    = ( T_{k-1}(a, b, c) - P_tilde_R^{(k-1)}(c) ) / ( (a + 3 - k) * (b + 2 - k) )
    where T_0 := Q_{2R}.

At level k, the residual after subtraction should have (a + 3 - k)(b + 2 - k) as a
factor, and the resulting T_k should satisfy:
    T_k(a = k - 2, b, c) = T_k(a, b = k - 1, c) = P_tilde_R^{(k)}(c)
i.e. slicing at a = k-2 or b = k-1 gives a polynomial depending only on c.

  Level 0: peel (a+2)(b+1), slice a=-2 or b=-1.
  Level 1: peel (a+1)(b+0), slice a=-1 or b= 0.
  Level 2: peel (a+0)(b-1), slice a= 0 or b= 1.
  Level 3: peel (a-1)(b-2), slice a= 1 or b= 2.
  Level R: T_R(a, b, c) evaluated at c = R should be (-1)^R (2R)!.

For R=3: run levels 0..3.
For R=4: run levels 0..4.
"""
import sys
import time
sys.path.insert(0, '/home/agent/projects/code')

from importlib import util

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


A_SYM, B_SYM, C_SYM = sp.symbols('a b c')


def predicted_P_tilde_0(R):
    """P_tilde_R^{(0)}(c) = c(c-2R) * prod_{k=1}^{2R-1}(c-k)^2."""
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


def fit_1var_with_verify(samples, max_deg):
    """Try fitting samples as poly in c, degrees 0..max_deg. Verify on holdout."""
    for d in range(0, max_deg + 1):
        if len(samples) < d + 2:  # need at least one holdout
            break
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
        if ok:
            return poly, d
    return None, None


def divide_bivar_by_ab_factor(P, a_val_root, b_val_root):
    """Divide bivariate poly P(a,b) by (a - a_val_root)(b - b_val_root) exactly.
    Returns quotient or raises ValueError if not divisible.
    """
    q1, r1 = sp.div(P, A_SYM - a_val_root, A_SYM)
    r1 = sp.expand(r1)
    if r1 != 0:
        raise ValueError(f"P not divisible by (a - {a_val_root}): remainder = {r1}")
    q1 = sp.expand(q1)
    q2, r2 = sp.div(q1, B_SYM - b_val_root, B_SYM)
    r2 = sp.expand(r2)
    if r2 != 0:
        raise ValueError(f"q1 not divisible by (b - {b_val_root}): remainder = {r2}")
    return sp.expand(q2)


def slice_and_verify_independence(T_at_c, slice_var, slice_val, indep_var, out):
    """For each (c, T(a,b)) in T_at_c, substitute slice_var=slice_val, verify
    T is independent of indep_var, and return list of (c, const_value)."""
    consts = []
    all_indep = True
    for (cv, T) in T_at_c:
        Ts = sp.expand(T.subs(slice_var, slice_val))
        if Ts == 0:
            consts.append((cv, 0))
            continue
        ps = Poly(Ts, indep_var)
        deg = ps.degree()
        const_val = ps.nth(0)
        if deg > 0:
            coefs = ps.all_coeffs()
            nonzero_higher = [(k, c) for k, c in
                              enumerate(reversed(coefs)) if c != 0 and k > 0]
            if nonzero_higher:
                all_indep = False
                out(f"    c={cv}: NOT INDEPENDENT of {indep_var}. deg={deg}, "
                    f"nonzero higher coefs: {nonzero_higher[:5]}")
                consts.append((cv, None))
                continue
        consts.append((cv, const_val))
    return all_indep, consts


def leading_coef(poly):
    """Leading coefficient of a polynomial in c."""
    if poly == 0:
        return 0
    p = Poly(poly, C_SYM)
    return p.LC()


def check_cR_squared(fitted, R, out):
    """Check that (c-R)^2 divides fitted; report multiplicity of (c-R) root."""
    q, r = sp.div(fitted, (C_SYM - R) ** 2, C_SYM)
    r_exp = sp.expand(r)
    if r_exp == 0:
        out(f"  (c - {R})^2 IS a factor.")
        # Report multiplicity
        mult = 0
        cur = fitted
        while True:
            qq, rr = sp.div(cur, (C_SYM - R), C_SYM)
            if sp.expand(rr) != 0:
                break
            mult += 1
            cur = qq
        out(f"  Multiplicity of (c-{R}) root = {mult}")
        return True
    else:
        out(f"  (c - {R})^2 is NOT a factor; remainder = {r_exp}")
        # Try (c-R)
        q1, r1 = sp.div(fitted, (C_SYM - R), C_SYM)
        r1_exp = sp.expand(r1)
        if r1_exp == 0:
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
            out(f"  (c - {R}) is NOT a factor.")
        return False


def analyze_R_recursion(R, log_lines):
    """Run iterated recursion at R, levels 0..R."""
    def out(s=""):
        print(s, flush=True)
        log_lines.append(s)

    out(f"\n{'='*72}")
    out(f"RECURSION LEVELS TEST, R = {R}, running levels 0..{R}")
    out(f"{'='*72}")

    num_c_samples = 4 * R + 4
    c_start = 2 * R + 2

    out(f"Building M_j tables up to j = {2*R + 2} ...")
    t0 = time.time()
    tables = hkfit.build_e2_tables(max_j=2 * R + 2)
    out(f"  built in {time.time() - t0:.2f}s.")

    # Fit Q_{2R}(a,b,c) at c=c_start..c_start+num_c_samples-1
    out(f"\nFitting Q_{{{2*R}}}(a,b,c) at c = {c_start} .. {c_start + num_c_samples - 1}")
    t0 = time.time()
    Q_at_c = []
    for i in range(num_c_samples):
        cv = c_start + i
        Q_bivar = get_Q_bivar_at_c(R, cv, tables)
        if Q_bivar is None:
            out(f"  c={cv}: fit_Qk_bivar returned None, skipping")
            continue
        Q_at_c.append((cv, Q_bivar))
    out(f"  fit {len(Q_at_c)} c-values in {time.time() - t0:.1f}s")

    # T_0 = Q_{2R}
    T_at_c = Q_at_c[:]  # (cv, bivar poly in a,b)

    # P_tilde^{(0)}
    P_tilde_0 = predicted_P_tilde_0(R)
    out(f"\nP_tilde_R^(0)(c) = {sp.factor(P_tilde_0)}")
    out(f"  Leading coef: {leading_coef(P_tilde_0)}")

    P_tildes = [P_tilde_0]  # index: level k
    leading_coefs = [leading_coef(P_tilde_0)]

    max_deg_fit = 4 * R + 2

    # Perform level 1, 2, ..., R
    for k in range(1, R + 1):
        out(f"\n{'-'*70}")
        out(f"LEVEL {k}:  peeling (a + {3-k})(b + {2-k})  from T_{k-1} - P_tilde^({k-1})")
        out(f"{'-'*70}")

        a_root = -(3 - k)  # subtract (a - a_root), factor = (a - a_root) = (a + 3 - k)
        b_root = -(2 - k)  # factor (b - b_root) = (b + 2 - k)
        # Sanity: at level 1, a_root = -2, b_root = -1. Good.
        # At level 2, a_root = -1, b_root = 0. Good.
        # At level 3, a_root = 0, b_root = 1. Good.

        P_prev = P_tildes[k - 1]
        T_next_at_c = []
        for (cv, Tprev) in T_at_c:
            P_val = P_prev.subs(C_SYM, cv)
            num = sp.expand(Tprev - P_val)
            try:
                Tnew = divide_bivar_by_ab_factor(num, a_root, b_root)
            except ValueError as e:
                out(f"  c={cv}: DIVISION FAILED at level {k}: {e}")
                # Try to give diagnostic: what's the residual at a=a_root, b=b_root?
                out(f"    num at a={a_root}: {sp.expand(num.subs(A_SYM, a_root))}")
                out(f"    num at b={b_root}: {sp.expand(num.subs(B_SYM, b_root))}")
                return {'levels_done': k - 1, 'P_tildes': P_tildes,
                        'leading_coefs': leading_coefs, 'T_final': None}
            T_next_at_c.append((cv, Tnew))
        out(f"  Division by (a - {a_root})(b - {b_root}) succeeded for all c.")

        # Slice-check: T_k(a = k-2, b, c) — should be b-independent
        slice_a = k - 2  # slice a = k-2
        slice_b = k - 1  # slice b = k-1
        out(f"\n  Check A: T_{k}(a = {slice_a}, b, c) — b-independence?")
        A_indep, A_consts = slice_and_verify_independence(
            T_next_at_c, A_SYM, slice_a, B_SYM, out)
        out(f"    Verdict A: {'YES (b-indep)' if A_indep else 'NO'}")

        out(f"  Check B: T_{k}(a, b = {slice_b}, c) — a-independence?")
        B_indep, B_consts = slice_and_verify_independence(
            T_next_at_c, B_SYM, slice_b, A_SYM, out)
        out(f"    Verdict B: {'YES (a-indep)' if B_indep else 'NO'}")

        # Check C: A_consts == B_consts
        C_agree = True
        for (cva, va), (cvb, vb) in zip(A_consts, B_consts):
            assert cva == cvb
            if va != vb:
                C_agree = False
                out(f"    c={cva}: A={va} B={vb} DISAGREE")
        out(f"    Verdict C (A==B): {'AGREE' if C_agree else 'DISAGREE'}")

        # Fit polynomial in c
        samples = [(cv, v) for (cv, v) in A_consts if v is not None]
        # For level k, the c-degree could be lower — we've divided by
        # nothing that depends on c so it's still bounded by 4R.
        fitted, fitted_deg = fit_1var_with_verify(samples, max_deg_fit)
        if fitted is None:
            out(f"    Could not fit P_tilde_R^{{({k})}}(c) as polynomial in c.")
            return {'levels_done': k - 1, 'P_tildes': P_tildes,
                    'leading_coefs': leading_coefs, 'T_final': None}
        out(f"    Fitted degree = {fitted_deg}")
        out(f"    P_tilde_R^({k})(c) = {sp.expand(fitted)}")
        out(f"    Factored:            {sp.factor(fitted)}")
        lc = leading_coef(fitted)
        out(f"    Leading coefficient: {lc}")

        # Check (c - R)^2 factor
        if k >= 1 and k < R:
            check_cR_squared(fitted, R, out)

        P_tildes.append(fitted)
        leading_coefs.append(lc)
        T_at_c = T_next_at_c

        if k == R:
            # Terminal: T_R(a, b, c). At c = R, expect (-1)^R (2R)!.
            out(f"\n  TERMINAL LEVEL k = R = {R}:")
            out(f"  T_R at c = R = {R}: expect (-1)^{R} * (2R)! = "
                f"{((-1)**R) * sp.factorial(2*R)}")
            # Do we have c = R in our fits? c_start = 2R+2 > R, so no.
            # Instead, use the fitted polynomial: P_tilde_R^{(R)}(c) at c = R.
            val_at_R = fitted.subs(C_SYM, R)
            expected = ((-1) ** R) * sp.factorial(2 * R)
            out(f"    P_tilde_R^({R})(c={R}) = {val_at_R}")
            out(f"    Expected (-1)^{R} * ({2*R})! = {expected}")
            out(f"    Match: {val_at_R == expected}")

            # Also: T_R(a,b,c) is a bivariate poly in (a,b) at each c. Print
            # it at a few c values to see whether it's a constant in (a, b).
            out(f"\n  T_R(a,b,c) shape at each c (should perhaps be a constant "
                f"in a,b at c = R, but generally a polynomial):")
            for (cv, T) in T_at_c[:5]:
                pT = Poly(T, A_SYM, B_SYM)
                out(f"    c={cv}: total_deg={pT.total_degree()}, "
                    f"T={sp.expand(T)[:200] if len(str(sp.expand(T))) > 200 else sp.expand(T)}"
                    if False else f"    c={cv}: total_deg={pT.total_degree()}")
            # Just print the first one in full:
            if T_at_c:
                cv0, T0 = T_at_c[0]
                out(f"    Full T_R at c={cv0}:")
                out(f"      {sp.expand(T0)}")

    out(f"\n{'-'*70}")
    out(f"SUMMARY for R = {R}")
    out(f"{'-'*70}")
    for k, (P, lc) in enumerate(zip(P_tildes, leading_coefs)):
        out(f"  Level {k}: P_tilde_R^({k})(c) = {sp.factor(P)}")
        out(f"           Leading coef: {lc}")

    return {'levels_done': R, 'P_tildes': P_tildes,
            'leading_coefs': leading_coefs, 'T_final': T_at_c}


def main():
    log_lines = []
    def out(s=""):
        print(s, flush=True)
        log_lines.append(s)

    out("Iterated Q_{2R} recursion — levels 0..R at R=3 and R=4.")
    out("Hypothesis at level k:")
    out("  T_k(a, b, c) = ( T_{k-1} - P_tilde^{(k-1)}(c) ) / ( (a + 3 - k)(b + 2 - k) )")
    out("  T_k(a = k-2, b, c) = T_k(a, b = k-1, c) = P_tilde^{(k)}(c),")
    out("  a polynomial in c alone (with (c-R)^2 as a factor for 1 <= k < R).")
    out("At level k=R, expect P_tilde^{(R)}(R) = (-1)^R (2R)!.")

    results = {}
    for R in [3, 4]:
        t0 = time.time()
        try:
            results[R] = analyze_R_recursion(R, log_lines)
        except Exception as e:
            import traceback
            tb = traceback.format_exc()
            out(f"R={R} EXCEPTION: {e}")
            out(tb)
            results[R] = None
        out(f"\nR={R} total time: {time.time() - t0:.1f}s")

    out("\n" + "=" * 72)
    out("OVERALL SUMMARY")
    out("=" * 72)
    for R, res in results.items():
        out(f"\nR = {R}:")
        if res is None:
            out(f"  FAILED with exception.")
            continue
        out(f"  levels completed: 0..{res['levels_done']}")
        for k, lc in enumerate(res['leading_coefs']):
            out(f"    level {k}: leading coef = {lc}")

    out_path = "/home/agent/projects/beta-prime/code/2026-08-15-recursion-levels.txt"
    with open(out_path, "w") as f:
        f.write("\n".join(log_lines) + "\n")
    print(f"\n[wrote log to {out_path}]", flush=True)


if __name__ == "__main__":
    main()
