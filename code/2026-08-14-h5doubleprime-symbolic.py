"""Day 106 Route C: Symbolic Q_{2R}(R-2, R, c) via Rick's fit_Qk_bivar pipeline.

Approach: for each c in a range c ≥ 2R+2, use fit_Qk_bivar to fit Q_{2R} as a
polynomial in (a, b) (which requires samples with a >= b >= c), then evaluate
at (a, b) = (R-2, R). This gives Q_{2R}(R-2, R, c) as an integer for each c.

Then fit Q_{2R}(R-2, R, c) as a polynomial in c, symbolically evaluate at
c = R, and compare to R!(R+1)!(2R)!.

We also inspect the structure of Q_{2R}(R-2, R, c) as a polynomial in c to
find the STRUCTURAL REASON the identity holds.
"""
import sys
sys.path.insert(0, '/home/agent/projects/code')

from fractions import Fraction
from math import factorial
from importlib import util

import sympy as sp
from sympy import (Matrix, expand, factor, symbols, Rational, Poly, simplify,
                   together, cancel, series, limit)

# Load the hkfit module.
spec = util.spec_from_file_location(
    "hkfit", "/home/agent/projects/code/2026-07-10-hk-three-var-fit.py"
)
hkfit = util.module_from_spec(spec)
spec.loader.exec_module(hkfit)

spec2 = util.spec_from_file_location(
    "d102", "/home/agent/projects/code/2026-07-18-day102-anchor-810-1214-probe.py"
)
d102 = util.module_from_spec(spec2)
spec2.loader.exec_module(d102)


def sample_Q_at_c(R, c, tables):
    """Fit Q_{2R}^{(c)}(a, b) and evaluate at (a, b) = (R-2, R)."""
    k_target = 2 * R
    r = d102.fit_Qk_bivar(c, k_target, tables)
    if r is None:
        return None
    poly, D = r
    a_sym, b_sym = sp.symbols('a b')
    val = poly.subs({a_sym: R - 2, b_sym: R})
    if not val.is_Integer:
        return None
    return int(val)


def fit_polynomial_1var(samples, deg):
    """Fit samples [(c_i, y_i)] as poly in c of degree deg. Use first (deg+1) samples,
    verify against the rest.
    """
    N = deg + 1
    if len(samples) < N:
        return None
    c = symbols('c')
    A_rows = []
    yy = []
    for (cv, val) in samples:
        row = [cv ** k for k in range(N)]
        A_rows.append(row)
        yy.append(val)
    A = Matrix(A_rows)
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
    return poly


def falling_factorial_poly(c_sym, R):
    """c^(R) = c(c-1)...(c-R+1)."""
    p = 1
    for i in range(R):
        p *= (c_sym - i)
    return p


def analyze_R(R, num_c_samples=None):
    print(f"\n{'=' * 70}")
    print(f"R = {R}")
    print(f"{'=' * 70}")
    target = factorial(R) * factorial(R + 1) * factorial(2 * R)
    print(f"Target Q_{{{2*R}}}({R-2}, {R}, {R}) = {R}!·{R+1}!·{2*R}! = {target}")

    if num_c_samples is None:
        num_c_samples = 4 * R + 8

    print(f"\nBuilding M_j tables up to j = {2*R + 2} ...")
    tables = hkfit.build_e2_tables(max_j=2 * R + 2)
    print("  done.")

    # Sample Q(R-2, R, c) at c = 2R+2, ..., 2R+2+num-1
    print(f"\nSampling Q_{{{2*R}}}({R-2}, {R}, c) at {num_c_samples} c-values ...")
    Qs = []
    c_start = 2 * R + 2
    for c in range(c_start, c_start + num_c_samples):
        v = sample_Q_at_c(R, c, tables)
        print(f"  c={c}: Q = {v}")
        if v is not None:
            Qs.append((c, v))
    print(f"  Total: {len(Qs)} samples.")

    if len(Qs) < 2 * R + 1:
        print(f"  Not enough samples; need at least {2*R + 1}.")
        return

    c_sym = symbols('c')
    Q_poly = None
    fit_deg = None
    for deg in range(0, len(Qs)):
        p = fit_polynomial_1var(Qs, deg)
        if p is not None:
            Q_poly = p
            fit_deg = deg
            break
    if Q_poly is None:
        print(f"  Could not fit polynomial with {len(Qs)} samples.")
        return
    print(f"\nQ_{{{2*R}}}({R-2}, {R}, c) fits as polynomial of degree {fit_deg}.")

    # Evaluate at c = R.
    Q_at_R = Q_poly.subs(c_sym, R)
    print(f"\nQ_{{{2*R}}}({R-2}, {R}, {R}) = {Q_at_R}")
    print(f"Target                    = {target}")
    if Q_at_R == target:
        print(f"MATCH! H5'' verified symbolically at R = {R}.")
    else:
        if target != 0 and Q_at_R != 0:
            print(f"Ratio: {Rational(Q_at_R, target)}")
        else:
            print(f"target={target}, Q_at_R={Q_at_R}")

    # Check divisibility by c^(R).
    print(f"\nChecking factorization Q(c) = c^(R) · P_R(c) where c^(R) = c(c-1)...(c-R+1)")
    ff = falling_factorial_poly(c_sym, R)
    Q_p = Poly(expand(Q_poly), c_sym)
    F_p = Poly(expand(ff), c_sym)
    quo, rem = Q_p.div(F_p)
    if rem.is_zero:
        print(f"  Yes, Q is divisible by c^(R).")
        P_R = quo.as_expr()
        print(f"  P_R(c) has degree {Poly(P_R, c_sym).degree()}")
        P_R_at_R = P_R.subs(c_sym, R)
        print(f"  P_R({R}) = {P_R_at_R}")
        target_P = factorial(R + 1) * factorial(2 * R)
        print(f"  Target P_R(R) = (R+1)! · (2R)! = {target_P}")
        if P_R_at_R == target_P:
            print(f"  MATCH!")
        # Try to factor P_R.
        P_R_fact = factor(P_R)
        print(f"  P_R(c) factored: {P_R_fact}")
    else:
        print(f"  NOT divisible by c^(R). Remainder = {rem.as_expr()}")

    # Also try to factor Q_poly.
    print(f"\nFactoring Q_{{{2*R}}}({R-2}, {R}, c) ...")
    Q_fact = factor(Q_poly)
    print(f"  {Q_fact}")

    # Return Q_poly for further analysis.
    return Q_poly, fit_deg


def main():
    results = {}
    for R in [2, 3, 4]:
        try:
            r = analyze_R(R)
            if r is not None:
                results[R] = r
        except Exception as e:
            print(f"R = {R} failed: {e}")
            import traceback
            traceback.print_exc()

    # Cross-inspection.
    print("\n" + "=" * 78)
    print("SUMMARY")
    print("=" * 78)
    for R, (poly, deg) in results.items():
        target = factorial(R) * factorial(R + 1) * factorial(2 * R)
        print(f"R={R}: deg={deg}, Q(R)={poly.subs(symbols('c'), R)}, target={target}")


if __name__ == "__main__":
    main()
