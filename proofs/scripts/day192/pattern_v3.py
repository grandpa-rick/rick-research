"""Verify conjectured formulas for c_1(r), c_0(r), c_2(r), c_3(r) in e_3 ⋆ e_r."""

import sympy as sp

q, t = sp.symbols('q t')


def qint(n):
    if n <= 0:
        return sp.Integer(0)
    return sum(t**i for i in range(n))


# Actual data
data = {
    (1, 0): (q - 1)*(t + 1)*(t**2 + 1)/q,
    (1, 1): sp.Rational(1)/q,
    (2, 0): (q - 1)*(q*t**2 + q - t)*(t**4 + t**3 + t**2 + t + 1)/q**2,
    (2, 1): (q - 1)*(t**2 + t + 1)/q**2,
    (2, 2): sp.Rational(1)/q**2,
    (3, 0): (q - 1)*(t + 1)*(t**2 - t + 1)*(q**2*t**6 + q**2*t**5 + 2*q**2*t**4 + 2*q**2*t**3 + 2*q**2*t**2 + q**2*t + q**2 - q*t**5 - 2*q*t**4 - 2*q*t**3 - 2*q*t**2 - q*t + t**3)/q**3,
    (3, 1): (q - 1)*(t**2 + 1)*(q*t**2 + q*t + q - t)/q**3,
    (3, 2): (q - 1)*(t + 1)/q**3,
    (3, 3): sp.Rational(1)/q**3,
    (4, 0): (q - 1)*(t**6 + t**5 + t**4 + t**3 + t**2 + t + 1)*(q**2*t**6 + q**2*t**4 + q**2*t**3 + q**2*t**2 + q**2 - q*t**5 - q*t**4 - q*t**3 - q*t**2 - q*t + t**3)/q**3,
    (4, 1): (q - 1)*(q*t**2 + q - t)*(t**4 + t**3 + t**2 + t + 1)/q**3,
    (4, 2): (q - 1)*(t**2 + t + 1)/q**3,
    (4, 3): sp.Rational(1)/q**3,
    (5, 0): (q - 1)*(t + 1)*(t**2 + 1)*(t**4 + 1)*(q**2*t**8 + q**2*t**6 + q**2*t**5 + q**2*t**4 + q**2*t**3 + q**2*t**2 + q**2 - q*t**7 - q*t**6 - q*t**5 - 2*q*t**4 - q*t**3 - q*t**2 - q*t + t**5 + t**3)/q**3,
    (5, 1): (q - 1)*(t**2 - t + 1)*(t**2 + t + 1)*(q*t**4 + q*t**3 + q*t**2 + q*t + q - t**3 - t**2 - t)/q**3,
    (5, 2): (q - 1)*(t + 1)*(t**2 + 1)*sp.Rational(1)/q**3,
    (5, 3): sp.Rational(1)/q**3,
}


def check(name, r, k, guess):
    if (r, k) not in data:
        print(f"  {name} r={r} k={k}: no data")
        return
    diff = sp.simplify(data[(r, k)] - guess)
    status = "PASS" if diff == 0 else "FAIL"
    print(f"  {name} r={r} k={k}: diff = {diff}   [{status}]")


print("=" * 72)
print("Conjectured formulas for e_3 ⋆ e_r  (r >= 3)")
print("=" * 72)

# c_3(r) = q^{-3}
print("\nc_3(r) = q^{-3}:")
for r in [3, 4, 5]:
    check("c_3", r, 3, 1 / q**3)

# c_2(r) = (q-1) [r-1]_t / q^3
print("\nc_2(r) = (q-1) [r-1]_t / q^3:")
for r in [3, 4, 5]:
    check("c_2", r, 2, (q - 1) * qint(r - 1) / q**3)

# c_1(r) = (q-1) [r+1]_t [r+2]_t (q [r]_t - t [r-2]_t) / (q^3 [2]_t [r]_t)
print("\nc_1(r) = (q-1) · [r+1]_t · [r+2]_t · (q[r]_t - t[r-2]_t) / (q^3 · [2]_t · [r]_t):")
for r in [3, 4, 5]:
    guess = (q - 1) * qint(r + 1) * qint(r + 2) * (q * qint(r) - t * qint(r - 2)) / (q**3 * qint(2) * qint(r))
    check("c_1", r, 1, guess)

# Extension to r=2:
# For e_2 ⋆ e_r we had c_2 = q^{-2}. For a=3, the k=2 slot only becomes "middle" for r >= 3.
# But maybe the c_0 formula holds for all r >= 1 with appropriate conventions.

# c_0(r) = coefficient of e_{r+3}: we need to guess based on r=3, 4, 5.
# Structure: (q-1)/q^3 · P(q, t; r) where P is polynomial of degree 2 in q.
# Let's extract q^0, q^1, q^2 parts of d_0(r) = c_0(r) * q^3 / (q-1).
print("\n" + "=" * 72)
print("Analyzing c_0(r):")
print("=" * 72)
for r in [3, 4, 5]:
    d = sp.expand(data[(r, 0)] * q**3 / (q - 1))
    dp = sp.Poly(d, q)
    print(f"\nr={r}: d_0(r) = c_0(r) · q^3/(q-1), degree in q = {dp.degree()}:")
    for k in range(dp.degree() + 1):
        c = dp.nth(k)
        print(f"  q^{k}: {sp.factor(c)}")
