"""
The 'SOLUTION FOUND' results in test6 have ugly rationals — likely just fitting noise.
Genuine test: predict c_7 (and hence b_8) from fitted h and see if it agrees with
b_8 computed directly from the sqrt formula.
"""
from sympy import Rational, Symbol, series, sqrt, Poly, expand

tau = Symbol('tau')

# Compute more coefficients of A first — need a_8, need to know if Rick's data extends.
# Rick gave a_1..a_7 only. Since b_k determines a_k via (1-2F)² = 1+4A,
# but a_k determines b_k, we can only extrapolate if we assume the ansatz.
# So: test if the h = 3 + 9τ + ... polynomial (deg 6) predicts b_8 that satisfies
# any consistent extension.

# Actually the ansatz b_k = (1/k)[τ^{k-1}] h^k is a definition of {b_k} once h is chosen.
# We fit c_0..c_6 to match b_1..b_7. This is a system of 7 equations in 7 unknowns — a
# tautological fit. It says NOTHING about whether the ansatz is 'correct'.

# The right test: fit c_0..c_5 (from b_1..b_6), then PREDICT b_7. If prediction matches
# 85384566, the ansatz has explanatory power.

b_expected = [None, 3, 27, 417, 7851, 164124, 3661389, 85384566]

# Refit c_0..c_5 from b_1..b_6, get h_5(τ) = c_0 + ... + c_5 τ^5
c = [Symbol(f'c{i}') for i in range(7)]
h = sum(c[i]*tau**i for i in range(6))  # degree 5

from sympy import solve
values = {}
values[c[0]] = Rational(b_expected[1])
for k in range(2, 7):  # fit through b_6, using c_0..c_5
    h_sub = h.subs(values)
    hk = expand(h_sub**k)
    coef = Poly(hk, tau).nth(k-1)
    eq = coef - k * b_expected[k]
    sol = solve(eq, c[k-1])
    values[c[k-1]] = sol[0]

# Now compute predicted b_7 = (1/7) [τ^6] h^7
h_final = sum(values[c[i]] * tau**i for i in range(6))
h7 = expand(h_final**7)
pred_b7 = Rational(Poly(h7, tau).nth(6), 7)
print(f"c_0..c_5 fit from b_1..b_6:")
for i in range(6):
    print(f"  c_{i} = {values[c[i]]}")
print(f"\nPredicted b_7 = {pred_b7}")
print(f"Actual b_7    = {b_expected[7]}")
print(f"Match? {pred_b7 == b_expected[7]}")

# If they don't match, the h series is deeper — c_6 exists but nonzero, needed to fit b_7.
# We already saw c_6 = 36376/243 nonzero, so no truncation.

# Alternative test: fit c_0..c_4 from b_1..b_5, predict b_6 AND b_7.
values2 = {}
values2[c[0]] = Rational(b_expected[1])
h2 = sum(c[i]*tau**i for i in range(5))
for k in range(2, 6):
    h_sub = h2.subs(values2)
    hk = expand(h_sub**k)
    coef = Poly(hk, tau).nth(k-1)
    eq = coef - k * b_expected[k]
    sol = solve(eq, c[k-1])
    values2[c[k-1]] = sol[0]
h_final2 = sum(values2[c[i]] * tau**i for i in range(5))
h6 = expand(h_final2**6)
pred_b6 = Rational(Poly(h6, tau).nth(5), 6)
h7 = expand(h_final2**7)
pred_b7_from5 = Rational(Poly(h7, tau).nth(6), 7)
print(f"\nUsing degree-4 h (from b_1..b_5):")
for i in range(5):
    print(f"  c_{i} = {values2[c[i]]}")
print(f"  Predicted b_6 = {pred_b6}, actual = {b_expected[6]}, match={pred_b6==b_expected[6]}")
print(f"  Predicted b_7 = {pred_b7_from5}, actual = {b_expected[7]}, match={pred_b7_from5==b_expected[7]}")

# Conclusion: the ansatz b_k = (1/k)[τ^{k-1}] h(τ)^k is trivially fittable for ANY sequence.
# It has no predictive power. The question is whether h has a CLOSED FORM.
