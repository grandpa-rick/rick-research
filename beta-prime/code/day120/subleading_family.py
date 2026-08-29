"""Day 120 — Look for closed forms in the subleading expansion of s*_mu.

Focus on families that appear "generic" (large a, small b, c):
  (a, 0, 0), (a, 1, 0), (a, 1, 1), (a, 2, 0), (a, 2, 1), (a, 2, 2)

We conjecture that for fixed (b, c), the subleading polynomial
  [t^{d_mu - k}] s*_mu(t, s, t)
becomes eventually polynomial in a (for a large enough).

Check: is [t^{d-1}] s*_{(a, 0, 0)} = s - T_a where T_a = (a+1)(a+2)/2 - 3 or similar?
"""

import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day117')
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day119')

from kostka import d_mu
from compute_bar_s import s_star_mu
from route_v_probe import substitute_sigma_pi, sig, pi
from sympy import expand, Integer, symbols, Poly, factor

u, y, c = symbols('u y c')
t, s = symbols('t s')


def eval_ts(mu):
    f = s_star_mu(mu)
    fsub = substitute_sigma_pi(f)
    return expand(fsub.subs({u: t, sig: s, pi: t}))


def sub_coef(mu, k):
    """[t^{d_mu - k}] eval_ts(mu) as poly in s."""
    d = d_mu(mu)
    expr = eval_ts(mu)
    p = Poly(expr, t, s)
    out = Integer(0)
    for (dt, ds), coef in p.terms():
        if dt == d - k:
            out += coef * s**ds
    return expand(out)


def show_family(bc, k, a_range):
    """Show sub_coef((a, b, c), k) for varying a."""
    b, cc = bc
    print(f"\n[t^{{d-{k}}}] s*_{{(a, {b}, {cc})}} for a = {list(a_range)}:")
    print(f"  T_a values (constant term):")
    for a in a_range:
        if a < b:
            continue
        mu = (a, b, cc)
        coef = sub_coef(mu, k)
        print(f"    a={a}: {coef}   (factored: {factor(coef) if coef != 0 else '0'})")


def show_family_diffs(bc, k, a_range):
    """Look at differences to detect polynomial-in-a behavior."""
    b, cc = bc
    print(f"\nDifferences of [t^{{d-{k}}}] s*_{{(a,{b},{cc})}} across a:")
    prev = None
    for a in a_range:
        if a < b:
            continue
        mu = (a, b, cc)
        coef = sub_coef(mu, k)
        if prev is not None:
            diff = expand(coef - prev)
            print(f"  a={a}: coef = {coef};  Delta = {factor(diff) if diff != 0 else '0'}")
        else:
            print(f"  a={a}: coef = {coef}")
        prev = coef


if __name__ == "__main__":
    # Family (a, 0, 0)
    print("=" * 70)
    print("FAMILY: mu = (a, 0, 0)  --  parity even")
    print("=" * 70)
    show_family_diffs((0, 0), 1, range(1, 10))
    show_family_diffs((0, 0), 2, range(2, 10))
    show_family_diffs((0, 0), 3, range(3, 10))

    print("\n" + "=" * 70)
    print("FAMILY: mu = (a, 1, 1)  --  parity even  (d_mu = a + 1)")
    print("=" * 70)
    show_family_diffs((1, 1), 1, range(1, 10))
    show_family_diffs((1, 1), 2, range(2, 10))

    print("\n" + "=" * 70)
    print("FAMILY: mu = (a, 1, 0)  --  parity odd")
    print("=" * 70)
    show_family_diffs((1, 0), 1, range(1, 10))
    show_family_diffs((1, 0), 2, range(2, 10))

    print("\n" + "=" * 70)
    print("FAMILY: mu = (a, 2, 0)  --  parity even (d_mu = a + 1)")
    print("=" * 70)
    show_family_diffs((2, 0), 1, range(2, 10))

    print("\n" + "=" * 70)
    print("FAMILY: mu = (a, 2, 2)  --  parity even (d_mu = a + 2)")
    print("=" * 70)
    show_family_diffs((2, 2), 1, range(2, 10))
