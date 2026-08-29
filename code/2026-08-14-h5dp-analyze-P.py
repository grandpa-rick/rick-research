"""Analyze P_R(c) = Q_{2R}(R-2, R, c) / c^(R) for structural patterns.

We already know:
  Q_{2R}(R-2, R, c) = c^(R) · P_R(c)      (R = 2, 3, 4, 5 verified)
  P_R(R) = (-1)^R · (R+1)! · (2R)!

Look for:
  1. Other roots of P_R (at negative c, or complex).
  2. Whether P_R has a nice closed form (e.g., Selberg, hook-content).
  3. Whether P_R(-c) or P_R(c + something) has recognisable structure.
  4. Whether Q(R-2, R, c) admits a formula like c! * (2c)! / (nice denom) — i.e., a
     Selberg integral / MacMahon box formula.
  5. Whether the coefficients c_k have known OEIS entries.
"""
import sys
sys.path.insert(0, '/home/agent/projects/code')
from math import factorial
import sympy as sp
from sympy import symbols, Poly, factor, expand, Rational
from importlib import util

spec = util.spec_from_file_location(
    "h5", "/home/agent/projects/code/2026-08-14-h5doubleprime-symbolic.py"
)
h5 = util.module_from_spec(spec)
spec.loader.exec_module(h5)


def falling_factorial_poly(c_sym, R):
    p = 1
    for i in range(R):
        p *= (c_sym - i)
    return p


def compute_P_R(R):
    """Return P_R(c) polynomial (via sample + fit)."""
    from importlib import util as u
    spec = u.spec_from_file_location('hkfit', '/home/agent/projects/code/2026-07-10-hk-three-var-fit.py')
    hkfit = u.module_from_spec(spec); spec.loader.exec_module(hkfit)
    tables = hkfit.build_e2_tables(max_j=2 * R + 2)
    Qs = []
    c_start = 2 * R + 2
    for c in range(c_start, c_start + 4 * R + 8):
        v = h5.sample_Q_at_c(R, c, tables)
        if v is not None:
            Qs.append((c, v))
    c_sym = symbols('c')
    Q_poly = None
    for deg in range(0, len(Qs)):
        p = h5.fit_polynomial_1var(Qs, deg)
        if p is not None:
            Q_poly = p; fit_deg = deg; break
    ff = falling_factorial_poly(c_sym, R)
    Q_p = Poly(expand(Q_poly), c_sym)
    F_p = Poly(expand(ff), c_sym)
    quo, rem = Q_p.div(F_p)
    assert rem.is_zero
    P_R = quo.as_expr()
    return P_R, Q_poly


def analyze(R):
    print(f"\n{'='*70}")
    print(f"R = {R}: Analyzing P_R(c) = Q_{{{2*R}}}({R-2}, {R}, c) / c^({R})")
    print(f"{'='*70}")
    P_R, Q_poly = compute_P_R(R)
    c = symbols('c')
    print(f"\nP_R(c) as polynomial (degree {Poly(P_R, c).degree()}):")
    print(f"  {expand(P_R)}")

    # Values at small c.
    print(f"\nP_R at small c:")
    for cv in range(0, 3 * R + 2):
        val = P_R.subs(c, cv)
        # Factor into primes
        v = int(val)
        f = sp.factorint(abs(v)) if v != 0 else {}
        sign = '' if v >= 0 else '-'
        print(f"  P_{R}({cv:3d}) = {sign}{f}   [={val}]")

    # Check: does P_R have integer roots?
    print(f"\nInteger roots of P_R (in range [-5, {2*R+5}])?")
    for cv in range(-5, 2 * R + 5):
        if P_R.subs(c, cv) == 0:
            print(f"  root at c = {cv}")

    # Look at the sequence P_R(R), P_R(R+1), P_R(R+2), ...
    print(f"\nP_R(R + k) sequence:")
    for k in range(0, 4):
        cv = R + k
        val = P_R.subs(c, cv)
        # Compare to nice formulas.
        # For P_R(R) = (R+1)!(2R)! · (-1)^R
        # Try (R+1)!(2R+2k)! / (something)?
        candidate_1 = factorial(R + 1) * factorial(2 * R)
        if k == 0:
            ratio = Rational(int(val), candidate_1)
            print(f"  P_{R}({cv}) = {val}, ratio to (R+1)!(2R)! = {ratio}")
        else:
            # Try (R+1+k)!(2R+2k)!
            cand = factorial(R + 1 + k) * factorial(2 * R + 2 * k)
            if cand > 0:
                ratio = Rational(int(val), cand) if val != 0 else 0
                print(f"  P_{R}({cv}) = {val}, ratio to (R+1+k)!(2R+2k)! = {ratio}")

    # Try: maybe P_R(c) / [(2c)! stuff] is nice?
    # Or P_R(c) = alternating hook-length count?

    # Also: expand Q_poly = c^(R) * P_R around c=R.
    # We want to see the "why" of P_R(R) = (R+1)!(2R)!.
    print(f"\nExpansion of Q around c=R (first 3 terms):")
    c_sym = c
    from sympy import series
    ser = series(Q_poly, c_sym, R, 4).removeO()
    print(f"  {ser}")


def main():
    for R in [2, 3, 4, 5]:
        analyze(R)


if __name__ == "__main__":
    main()
