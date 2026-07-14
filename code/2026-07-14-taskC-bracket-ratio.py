"""Day 96 Task C addendum — bracket ratio B_5/B_3 at universal shell.

Q_3 = c(c-2)(c-1)·B_3(a, b, c)  where B_3 has 4 terms
Q_5 = -c(c-3)(c-2)(c-1)·B_5(a, b, c)  where B_5 has ~30 terms

The 2·v_2(c-4) jump in v_2 must come from B_5/B_3 (adjusted for the extra (c-3) factor
in Q_5 which is odd for c even).

Compute B_5(a, b, c) at (a, b) = (T-2, 0) as a polynomial in c for each T range,
and check for (c-4)^2 factor.
"""
import json
from sympy import symbols, sympify, expand, Poly, factor, gcd

a_s, b_s, c_s = symbols('a b c')

# Extract brackets after factoring out obvious factors.
B3 = 6*a_s*b_s + 6*a_s + 12*b_s - c_s**3 + 6*c_s**2 - 11*c_s + 18
B5 = (60*a_s**2*b_s**2 + 60*a_s**2*b_s + 180*a_s*b_s**2 - 20*a_s*b_s*c_s**3
      + 180*a_s*b_s*c_s**2 - 520*a_s*b_s*c_s + 660*a_s*b_s - 20*a_s*c_s**3
      + 180*a_s*c_s**2 - 520*a_s*c_s + 480*a_s + 120*b_s**2 - 40*b_s*c_s**3
      + 360*b_s*c_s**2 - 1040*b_s*c_s + 1080*b_s + c_s**6 - 19*c_s**5
      + 145*c_s**4 - 605*c_s**3 + 1534*c_s**2 - 2256*c_s + 1440)


def v2(n):
    if n == 0: return float('inf')
    n = abs(int(n))
    v = 0
    while n % 2 == 0:
        n //= 2
        v += 1
    return v


def main():
    print("=" * 76)
    print("Bracket B_3, B_5 analysis at universal shell (T-2, 0)")
    print("=" * 76)

    # For each T (8, 16, 32), substitute a = T-2, b = 0 into B_3 and B_5
    # to get univariate polynomials in c.
    for T in [8, 16, 32]:
        a_val = T - 2
        B3_c = expand(B3.subs({a_s: a_val, b_s: 0}))
        B5_c = expand(B5.subs({a_s: a_val, b_s: 0}))
        print(f"\n{'-' * 76}")
        print(f"T = {T}, a = T-2 = {a_val}, b = 0")
        print(f"{'-' * 76}")
        print(f"  B_3(a={a_val}, 0, c) = {B3_c}")
        print(f"  B_5(a={a_val}, 0, c) = {B5_c}")

        # Factor B_3, B_5 as univariate polys in c.
        print(f"\n  factor(B_3) = {factor(B3_c)}")
        print(f"  factor(B_5) = {factor(B5_c)}")

        # Compute gcd
        g = gcd(B3_c, B5_c)
        print(f"\n  gcd(B_3, B_5) = {g}")
        if g != 1:
            print(f"  B_3 / gcd = {factor(expand(B3_c/g))}")
            print(f"  B_5 / gcd = {factor(expand(B5_c/g))}")

        # Look for (c-4) factor in B_5 - (something) * B_3
        # or in specific evaluations
        print(f"\n  B_3 and B_5 evaluations across c:")
        print(f"  {'c':>3} {'B_3':>15} {'v_2':>4} {'B_5':>20} {'v_2':>4}")
        c_range = ({8: [8], 16: [12, 16], 32: [20, 24, 28, 32]})[T]
        for c_val in c_range:
            b3v = int(B3_c.subs(c_s, c_val))
            b5v = int(B5_c.subs(c_s, c_val))
            print(f"  {c_val:>3} {b3v:>15} {v2(b3v):>4} {b5v:>20} {v2(b5v):>4}")

    # Global picture: at (T-2, 0, c), what's v_2(B_5) - v_2(B_3)?
    print(f"\n{'=' * 76}")
    print("v_2(B_5) - v_2(B_3) at (T-2, 0, c), and v_2(c-4):")
    print(f"{'=' * 76}")
    print(f"  {'c':>3} {'T':>4} {'v_2(B_3)':>8} {'v_2(B_5)':>8} {'diff':>4} "
          f"{'v_2(c-4)':>8} {'2v_2(c-4)':>10}")
    T_of = lambda c: (1 << max(1, (c-1).bit_length())) if c > 2 else 4
    for c_val in [8, 12, 16, 20, 24, 28, 32]:
        # Recompute T
        T = 1
        while T <= c_val - 2:
            T *= 2
        a_val = T - 2
        b3v = int(B3.subs({a_s: a_val, b_s: 0, c_s: c_val}))
        b5v = int(B5.subs({a_s: a_val, b_s: 0, c_s: c_val}))
        v_b3, v_b5 = v2(b3v), v2(b5v)
        v_cm4 = v2(c_val - 4)
        print(f"  {c_val:>3} {T:>4} {v_b3:>8} {v_b5:>8} {v_b5 - v_b3:>4} "
              f"{v_cm4:>8} {2*v_cm4:>10}")

    # For c ∈ {20, 24, 28, 32}, T = 32, a = 30. B_5(30, 0, c) is a polynomial
    # in c. Does it have (c-4)^2 as a factor? Check symbolically.
    print(f"\n{'=' * 76}")
    print("Symbolic check: does B_5(30, 0, c) have (c-4)^r factor?")
    print(f"{'=' * 76}")
    B5_30 = expand(B5.subs({a_s: 30, b_s: 0}))
    B3_30 = expand(B3.subs({a_s: 30, b_s: 0}))
    print(f"  B_3(30, 0, c) = {factor(B3_30)}")
    print(f"  B_5(30, 0, c) = {factor(B5_30)}")

    # Try (c-4) substitution
    from sympy import Symbol
    d = Symbol('d')  # d = c - 4
    B3_d = expand(B3_30.subs(c_s, d + 4))
    B5_d = expand(B5_30.subs(c_s, d + 4))
    print(f"\n  In terms of d = c - 4:")
    print(f"  B_3 = {B3_d}")
    print(f"  B_5 = {B5_d}")

    # v_2 of constant term (d = 0, c = 4)
    p3 = Poly(B3_d, d)
    p5 = Poly(B5_d, d)
    print(f"\n  B_3 as poly in d: {p3.all_coeffs()}")
    print(f"  B_5 as poly in d: {p5.all_coeffs()}")
    print(f"  const B_3 = {p3.all_coeffs()[-1]} = {int(p3.all_coeffs()[-1])}, "
          f"v_2 = {v2(int(p3.all_coeffs()[-1]))}")
    print(f"  const B_5 = {p5.all_coeffs()[-1]} = {int(p5.all_coeffs()[-1])}, "
          f"v_2 = {v2(int(p5.all_coeffs()[-1]))}")

    # Save
    out = {'note': 'B_3, B_5 bracket analysis for PROVE.'}
    with open('/home/agent/projects/code/2026-07-14-taskC-bracket-ratio.json', 'w') as f:
        json.dump(out, f, indent=2)


if __name__ == '__main__':
    main()
