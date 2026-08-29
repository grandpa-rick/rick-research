"""Day 101 PROVE — extract clean factorisations of P_hat_k for k = 4, 5, 6.

For k = 4, 5, 6, the polynomial Q_k(a, b, c) has c-linear prefactors listed
in the catalog. After stripping those, we get S_k(a, b, c) which is degree 2
in each of a, b (for k=4, 5) or 3 in each (k=6).

Substituting c = 4m+2 and re-expressing in terms of A := a+2, B := b+1,
we look for the analogue of the P_hat_2 / P_hat_3 clean form.
"""
import sympy as sp
from sympy import symbols, expand, factor, collect, Poly

a, b, c, m, A, B = symbols('a b c m A B')

# From catalog (2026-07-11-Qk-catalog.json):
# Q_4 = c(c-1) * S_4
S_4 = (
    12 * a ** 2 * b ** 2 + 12 * a ** 2 * b + 36 * a * b ** 2
    - 12 * a * b * c ** 3 + 84 * a * b * c ** 2 - 192 * a * b * c + 180 * a * b
    - 12 * a * c ** 3 + 84 * a * c ** 2 - 192 * a * c + 144 * a
    + 24 * b ** 2 - 24 * b * c ** 3 + 168 * b * c ** 2 - 384 * b * c + 312 * b
    + c ** 6 - 15 * c ** 5 + 91 * c ** 4 - 309 * c ** 3 + 652 * c ** 2 - 804 * c + 432
)

# Q_5 = -c(c-3)(c-2)(c-1) * S_5
S_5 = (
    60 * a ** 2 * b ** 2 + 60 * a ** 2 * b + 180 * a * b ** 2
    - 20 * a * b * c ** 3 + 180 * a * b * c ** 2 - 520 * a * b * c + 660 * a * b
    - 20 * a * c ** 3 + 180 * a * c ** 2 - 520 * a * c + 480 * a
    + 120 * b ** 2 - 40 * b * c ** 3 + 360 * b * c ** 2 - 1040 * b * c + 1080 * b
    + c ** 6 - 19 * c ** 5 + 145 * c ** 4 - 605 * c ** 3 + 1534 * c ** 2 - 2256 * c + 1440
)

# Q_6 = -c(c-2)(c-1) * S_6
S_6 = (
    120 * a ** 3 * b ** 3 - 120 * a ** 3 * b + 360 * a ** 2 * b ** 3
    - 180 * a ** 2 * b ** 2 * c ** 3 + 1800 * a ** 2 * b ** 2 * c ** 2 - 5940 * a ** 2 * b ** 2 * c + 6480 * a ** 2 * b ** 2
    - 180 * a ** 2 * b * c ** 3 + 1800 * a ** 2 * b * c ** 2 - 5940 * a ** 2 * b * c + 6120 * a ** 2 * b
    + 240 * a * b ** 3
    - 540 * a * b ** 2 * c ** 3 + 5400 * a * b ** 2 * c ** 2 - 17820 * a * b ** 2 * c + 19440 * a * b ** 2
    + 30 * a * b * c ** 6 - 630 * a * b * c ** 5 + 5430 * a * b * c ** 4 - 25110 * a * b * c ** 3 + 66900 * a * b * c ** 2 - 98460 * a * b * c + 62400 * a * b
    + 30 * a * c ** 6 - 630 * a * c ** 5 + 5430 * a * c ** 4 - 24570 * a * c ** 3 + 61500 * a * c ** 2 - 80640 * a * c + 43200 * a
    - 360 * b ** 2 * c ** 3 + 3600 * b ** 2 * c ** 2 - 11880 * b ** 2 * c + 12960 * b ** 2
    + 60 * b * c ** 6 - 1260 * b * c ** 5 + 10860 * b * c ** 4 - 49500 * b * c ** 3 + 126600 * b * c ** 2 - 173160 * b * c + 99360 * b
    - c ** 9 + 33 * c ** 8 - 474 * c ** 7 + 3942 * c ** 6 - 21189 * c ** 5 + 77157 * c ** 4 - 191456 * c ** 3 + 311988 * c ** 2 - 300960 * c + 129600
)

for k, Sk in [(4, S_4), (5, S_5), (6, S_6)]:
    print("=" * 78)
    print(f"S_{k}(a, b, c) at c = 4m+2")
    print("=" * 78)
    Sk_at = expand(Sk.subs(c, 4 * m + 2))
    # Now express in terms of A = a+2, B = b+1
    Sk_ab = expand(Sk_at.subs([(a, A - 2), (b, B - 1)]))
    print(f"S_{k}(A-2, B-1, 4m+2):")
    poly = Poly(Sk_ab, A, B)
    for mono, coef in sorted(poly.as_dict().items()):
        print(f"   A^{mono[0]} B^{mono[1]}: {expand(coef)}")
    print()
    # Also collect A, B factor
    fac = factor(Sk_ab)
    print(f"  factored: {fac}")
    print()

    # Coefficients of pure-m part (the A=0, B=0 term)
    const_m = poly.as_dict().get((0, 0), 0)
    print(f"  Constant term in (A, B) — call it -T_k(m): {expand(-const_m)}")
    print(f"  v_2 factorization of -const_m: {factor(-const_m)}")
    print()
