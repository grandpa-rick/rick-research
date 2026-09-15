"""Try to fit c_0(r) closed form for e_3 ⋆ e_r.

Guess motivated by Day 191:
   c_0^{a=2}(r) = (q-1)/q · ([r+2]_t/[2]_t) · ([r+1]_t - t/q · [r-1]_t)

Analog for a=3:
   c_0^{a=3}(r) = (q-1)/q · f(r,t) · g(r, t, 1/q)
where f encodes the "q-Gaussian" leading behavior and g is a polynomial in 1/q of degree 2.

From analysis:
   d_0(r) = c_0(r) · q^3/(q-1) has degree 2 in q.
   d_0(r) = A_2(r) q^2 + A_1(r) q + A_0(r)
   A_2(r) = [r+1]_t [r+2]_t [r+3]_t / ([2]_t [3]_t)

Write d_0(r) = q-Gaussian · (Q_2 q^2 + Q_1 q + Q_0) where Q_i are simpler.

Let's parametrize: divide by q-Gaussian G(r) = [r+1]_t[r+2]_t[r+3]_t/([2]_t[3]_t):
   d_0(r) / G(r) = q^2 + (A_1/G) q + (A_0/G)
   Need A_1/G and A_0/G to be Laurent polynomials in t.
"""

import sympy as sp

q, t = sp.symbols('q t')


def qint(n):
    if n <= 0:
        return sp.Integer(0)
    return sum(t**i for i in range(n))


data_c0 = {
    3: (q - 1)*(t + 1)*(t**2 - t + 1)*(q**2*t**6 + q**2*t**5 + 2*q**2*t**4 + 2*q**2*t**3 + 2*q**2*t**2 + q**2*t + q**2 - q*t**5 - 2*q*t**4 - 2*q*t**3 - 2*q*t**2 - q*t + t**3)/q**3,
    4: (q - 1)*(t**6 + t**5 + t**4 + t**3 + t**2 + t + 1)*(q**2*t**6 + q**2*t**4 + q**2*t**3 + q**2*t**2 + q**2 - q*t**5 - q*t**4 - q*t**3 - q*t**2 - q*t + t**3)/q**3,
    5: (q - 1)*(t + 1)*(t**2 + 1)*(t**4 + 1)*(q**2*t**8 + q**2*t**6 + q**2*t**5 + q**2*t**4 + q**2*t**3 + q**2*t**2 + q**2 - q*t**7 - q*t**6 - q*t**5 - 2*q*t**4 - q*t**3 - q*t**2 - q*t + t**5 + t**3)/q**3,
}


for r in [3, 4, 5]:
    c0 = data_c0[r]
    d = sp.expand(c0 * q**3 / (q - 1))
    dp = sp.Poly(d, q)
    A2, A1, A0 = dp.nth(2), dp.nth(1), dp.nth(0)
    G = qint(r + 1) * qint(r + 2) * qint(r + 3) / (qint(2) * qint(3))
    ratio_1 = sp.simplify(A1 / G)
    ratio_0 = sp.simplify(A0 / G)
    print(f"r={r}:")
    print(f"  A_2 = G(r), A_1/G = {sp.factor(ratio_1)}, A_0/G = {sp.factor(ratio_0)}")

# The ratio_1 / (-t) should tell us the "q^1 twist".
print()
for r in [3, 4, 5]:
    c0 = data_c0[r]
    d = sp.expand(c0 * q**3 / (q - 1))
    dp = sp.Poly(d, q)
    A2, A1, A0 = dp.nth(2), dp.nth(1), dp.nth(0)
    G = qint(r + 1) * qint(r + 2) * qint(r + 3) / (qint(2) * qint(3))
    print(f"r={r}:")
    print(f"  -A_1/(t·G) = {sp.factor(sp.simplify(-A1 / (t * G)))}")
    print(f"   A_0/(t^3·G) = {sp.factor(sp.simplify(A0 / (t**3 * G)))}")

# Now let's guess. -A_1/(t G) is a polynomial "P_1(r,t)". A_0/(t^3 G) is a polynomial "P_0(r,t)".
# Look for pattern.
