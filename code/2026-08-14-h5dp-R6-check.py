"""Extend Route C to R=6 and R=8 to confirm the pattern.

Also examine:
  Q(R-2, R, c) = c^(R) · P_R(c)
  where P_R(R) = (R+1)! · (2R)! (up to sign).
  And empirically P_R(R) = P_R(R+1).

Check: does P_R(c) itself factor further?
"""
import sys
sys.path.insert(0, '/home/agent/projects/code')
from math import factorial
import sympy as sp
from sympy import symbols, Poly, factor, expand
from importlib import util

spec = util.spec_from_file_location('h5', '/home/agent/projects/code/2026-08-14-h5doubleprime-symbolic.py')
h5 = util.module_from_spec(spec); spec.loader.exec_module(h5)
spec_hk = util.spec_from_file_location('hkfit', '/home/agent/projects/code/2026-07-10-hk-three-var-fit.py')
hkfit = util.module_from_spec(spec_hk); spec_hk.loader.exec_module(hkfit)


def falling_factorial_poly(c_sym, R):
    p = 1
    for i in range(R):
        p *= (c_sym - i)
    return p


def analyze_R_full(R, extra_samples=8):
    print(f"\n{'='*70}")
    print(f"R = {R}")
    print(f"{'='*70}")
    target = factorial(R) * factorial(R + 1) * factorial(2 * R)
    print(f"Target Q_{{{2*R}}}({R-2}, {R}, {R}) = {R}!·{R+1}!·{2*R}! = {target}")

    print(f"\nBuilding M_j tables ...")
    tables = hkfit.build_e2_tables(max_j=2 * R + 2)

    n_samples = 4 * R + 1 + extra_samples
    Qs = []
    c_start = 2 * R + 2
    print(f"Sampling {n_samples} c-values ...")
    for c in range(c_start, c_start + n_samples):
        v = h5.sample_Q_at_c(R, c, tables)
        if v is not None:
            Qs.append((c, v))
        else:
            print(f"  c={c}: None")
    print(f"  Got {len(Qs)} samples.")

    c_sym = symbols('c')
    Q_poly = None; fit_deg = None
    for deg in range(0, len(Qs)):
        p = h5.fit_polynomial_1var(Qs, deg)
        if p is not None:
            Q_poly = p; fit_deg = deg; break
    if Q_poly is None:
        print("  Fit failed."); return
    print(f"Fit degree: {fit_deg}")

    Q_at_R = Q_poly.subs(c_sym, R)
    Q_at_Rp1 = Q_poly.subs(c_sym, R + 1)
    print(f"\nQ({R-2}, {R}, {R})   = {Q_at_R}")
    print(f"Q({R-2}, {R}, {R+1}) = {Q_at_Rp1}")
    print(f"Target ((-1)^R · R!(R+1)!(2R)!) = {(-1)**R * target}")
    print(f"Q(R+1)/Q(R) = {sp.Rational(int(Q_at_Rp1), int(Q_at_R))}")
    # Ratio should be R+1 (from c^(R) factor).

    # Factor out c^(R).
    ff = falling_factorial_poly(c_sym, R)
    Q_p = Poly(expand(Q_poly), c_sym)
    F_p = Poly(expand(ff), c_sym)
    quo, rem = Q_p.div(F_p)
    assert rem.is_zero, f"Q not divisible by c^(R): rem = {rem.as_expr()}"
    P_R = quo.as_expr()
    print(f"\nP_R(c) has degree {Poly(P_R, c_sym).degree()}")
    print(f"P_R({R}) = {P_R.subs(c_sym, R)}")
    print(f"P_R({R+1}) = {P_R.subs(c_sym, R+1)}")
    target_P = factorial(R + 1) * factorial(2 * R)
    print(f"Target P_R(R) = (R+1)!(2R)! = {target_P}")

    # Try to factor P_R.
    print(f"\nFactoring P_R(c) over Q ...")
    P_R_fact = factor(P_R)
    print(f"  {P_R_fact}")

    # Look for symmetry P_R(c) related to P_R(2R-1-c) or similar.
    print(f"\nTesting symmetries:")
    # 1. Does P_R(c) = ±P_R(a - c) for some a?
    for a in range(2 * R - 5, 2 * R + 5):
        p_ac = P_R.subs(c_sym, a - c_sym)
        if expand(p_ac - P_R) == 0:
            print(f"  P_R symmetric: P_R(c) = P_R({a} - c)")
        elif expand(p_ac + P_R) == 0:
            print(f"  P_R antisymmetric: P_R(c) = -P_R({a} - c)")
    # Also: does P_R vanish at some c > R?
    print(f"\nInteger evaluations of P_R for c ∈ [-2, {3*R+2}]:")
    for cv in range(-2, 3 * R + 2):
        val = int(P_R.subs(c_sym, cv))
        marker = "  ← ZERO!" if val == 0 else ""
        print(f"  P_R({cv:3d}) = {val}{marker}")

    return Q_poly, P_R


def main():
    for R in [6]:
        try:
            analyze_R_full(R)
        except Exception as e:
            print(f"R={R} FAILED: {e}")
            import traceback; traceback.print_exc()


if __name__ == "__main__":
    main()
