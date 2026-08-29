"""Appendix F identity — verify at R = 5 and R = 6.

    Q_{2R}(-2, b, c) = c(c-2R) * prod_{k=1}^{2R-1} (c-k)^2      (b-independent)
    Q_{2R}(a, -1, c) = c(c-2R) * prod_{k=1}^{2R-1} (c-k)^2      (a-independent)

Strategy (following Route C / Day 106-107):
  1. For each c in [2R+2, 2R+2 + n_samples], fit Q_{2R}^{(c)}(a, b) as a
     bivariate polynomial via d102.fit_Qk_bivar.
  2. Substitute a = -2 (or b = -1) into that bivariate polynomial. If
     b-independence holds, the resulting polynomial in b is actually a
     constant.
  3. Collect (c, Q(-2, ?, c)) samples, and fit as a polynomial in c.
  4. Also record the b-coefficients to check they all vanish for nonzero
     powers of b.
  5. Compare with the predicted RHS c(c-2R) * prod_{k=1}^{2R-1} (c-k)^2.
"""
import sys
import time
sys.path.insert(0, '/home/agent/projects/code')

from importlib import util
from math import factorial

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


def rising_fact(x, n):
    if n <= 0:
        return 1
    p = 1
    for i in range(n):
        p *= (x + i)
    return p


def predicted_RHS(R):
    """c(c-2R) * prod_{k=1}^{2R-1} (c-k)^2."""
    p = C_SYM * (C_SYM - 2 * R)
    for k in range(1, 2 * R):
        p *= (C_SYM - k) ** 2
    return sp.expand(p)


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


def get_Q_bivar_at_c(R, c_val, tables):
    """Return the bivariate polynomial Q_{2R}^{(c)}(a, b) with the Pochhammer
    prefactor RE-INCORPORATED so we get the true trivariate Q.

    d102.fit_Qk_bivar returns the "normalized" polynomial:
       Q_norm(a,b) := h_k(a,b,c) / [ (a+3)_L * (b+2)_L ]
    where L = c - 1 - k. For k = 2R, this normalization removes the
    Pochhammer prefactor.

    The "Q" in Appendix F is exactly this normalized polynomial (that's
    what h5doubleprime-symbolic.py uses — see sample_Q_at_c which just
    evaluates poly directly). So we return the raw fit_Qk_bivar output.
    """
    k_target = 2 * R
    r = d102.fit_Qk_bivar(c_val, k_target, tables)
    if r is None:
        return None
    poly, D = r
    return sp.expand(poly)


def analyze_slice(R, slice_var, slice_val, tables, num_c_samples):
    """slice_var in {'a', 'b'}. slice_val is the value we specialize to."""
    print(f"\n--- R = {R}, slice {slice_var} = {slice_val} ---", flush=True)

    # Q_{2R} has (a,b)-total degree 2R, so slicing a=-2 leaves a degree-2R
    # polynomial in b. We need to detect b-independence.
    # Sample Q_bivar(a, b, c) at c-values, then substitute.
    c_start = 2 * R + 2
    remaining_var = 'b' if slice_var == 'a' else 'a'
    r_sym = B_SYM if remaining_var == 'b' else A_SYM

    slice_sub_var = A_SYM if slice_var == 'a' else B_SYM

    # For each c: fit Q_bivar, sub in slice, collect remaining polynomial.
    slice_polys = []  # list of (c, poly-in-remaining-var)
    t0 = time.time()
    for i in range(num_c_samples):
        cv = c_start + i
        Q_bivar = get_Q_bivar_at_c(R, cv, tables)
        if Q_bivar is None:
            print(f"  c={cv}: fit_Qk_bivar returned None, skipping")
            continue
        Q_sliced = sp.expand(Q_bivar.subs(slice_sub_var, slice_val))
        slice_polys.append((cv, Q_sliced))
        elapsed = time.time() - t0
        print(f"  c={cv}: bivar fit done ({elapsed:.1f}s cumulative)",
              flush=True)

    # For each c, examine whether Q_sliced depends on remaining_var.
    print(f"\n  b/a-independence check at each c:")
    all_independent = True
    for (cv, ps) in slice_polys:
        ps_poly = Poly(ps, r_sym) if ps != 0 else None
        if ps == 0:
            deg = -1
            const_val = 0
        else:
            deg = ps_poly.degree()
            # coefficients: extract all
            coefs = ps_poly.all_coeffs()  # highest deg first
            const_val = ps_poly.nth(0)
            if deg > 0:
                # print non-zero higher-order coeffs
                nonzero_higher = [(k, c) for k, c in
                                  enumerate(reversed(coefs)) if c != 0 and k > 0]
                if nonzero_higher:
                    all_independent = False
                    print(f"    c={cv}: NOT INDEPENDENT. degree in {remaining_var} = {deg}, nonzero coefs: {nonzero_higher[:5]}")
                    continue
        print(f"    c={cv}: independent (constant = {const_val})")

    print(f"\n  Verdict on {remaining_var}-independence: "
          f"{'YES' if all_independent else 'NO'}")

    # Now fit const_val vs c.
    const_samples = []
    for (cv, ps) in slice_polys:
        if ps == 0:
            const_samples.append((cv, 0))
        else:
            ps_poly = Poly(ps, r_sym)
            const_samples.append((cv, ps_poly.nth(0)))

    # Predicted RHS
    rhs = predicted_RHS(R)
    print(f"\n  Predicted RHS = c(c-{2*R}) * prod_{{k=1}}^{{{2*R-1}}} (c-k)^2")
    # We evaluate the RHS at every sampled c and compare
    all_match = True
    for (cv, val) in const_samples:
        rhs_at_cv = rhs.subs(C_SYM, cv)
        if val != rhs_at_cv:
            all_match = False
            print(f"    c={cv}: Q={val}, RHS={rhs_at_cv} MISMATCH")
        else:
            print(f"    c={cv}: match ({val})")

    print(f"\n  Verdict on RHS equality: "
          f"{'MATCH' if all_match else 'MISMATCH'}")

    # If independent + all c-values match, also do a polynomial fit for the
    # extra confidence.
    fit_deg = 4 * R
    if len(const_samples) >= fit_deg + 1:
        poly = fit_polynomial_1var(const_samples, fit_deg)
        if poly is not None:
            diff = sp.expand(poly - rhs)
            print(f"  Fitted c-polynomial degree {fit_deg}: "
                  f"{'matches RHS' if diff == 0 else 'DIFFERS from RHS'}")
            if diff != 0:
                print(f"    difference = {diff}")
        else:
            print(f"  Could not fit degree-{fit_deg} polynomial in c")

    return {
        'independent': all_independent,
        'matches_rhs': all_match,
        'slice_polys': slice_polys,
        'const_samples': const_samples,
    }


def analyze_R(R, num_c_samples=None):
    print(f"\n{'='*70}")
    print(f"APPENDIX F CHECK, R = {R}")
    print(f"{'='*70}", flush=True)

    if num_c_samples is None:
        # We need at least 4R+1 samples to fit the degree-4R c-polynomial.
        # Use a bit more.
        num_c_samples = 4 * R + 4

    print(f"Building M_j tables up to j = {2*R + 2} ...", flush=True)
    t0 = time.time()
    tables = hkfit.build_e2_tables(max_j=2 * R + 2)
    print(f"  built in {time.time() - t0:.1f}s.", flush=True)

    # a = -2 slice: get Q_bivar, substitute a=-2, examine b-dependence.
    res_a = analyze_slice(R, slice_var='a', slice_val=-2,
                          tables=tables, num_c_samples=num_c_samples)

    # b = -1 slice
    res_b = analyze_slice(R, slice_var='b', slice_val=-1,
                          tables=tables, num_c_samples=num_c_samples)

    return {'a=-2': res_a, 'b=-1': res_b}


def main():
    print("Appendix F verification: Q_{2R}(-2,b,c) and Q_{2R}(a,-1,c) at R=5, R=6")
    print("Predicted: c(c-2R) * prod_{k=1}^{2R-1} (c-k)^2 (b/a-independent)")

    all_results = {}
    for R in [5, 6]:
        try:
            all_results[R] = analyze_R(R)
        except Exception as e:
            print(f"R={R} FAILED: {e}")
            import traceback; traceback.print_exc()
            all_results[R] = None

    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    for R, res in all_results.items():
        print(f"\nR = {R}:")
        if res is None:
            print("  FAILED")
            continue
        for slice_label in ['a=-2', 'b=-1']:
            s = res[slice_label]
            print(f"  slice {slice_label}: "
                  f"independent={s['independent']}, "
                  f"matches RHS={s['matches_rhs']}")


if __name__ == "__main__":
    main()
