"""
TEST 1: Sanity check that F = (1 - sqrt(1 + 4A)) / 2 reproduces b_k.
"""
from sympy import Rational, sqrt, series, symbols, Poly, Integer, together, expand, simplify
from sympy import Symbol, sympify

tau = Symbol('tau')

# a_k for k=1..7 (a_0 = 0)
a_vals = [0, -3, -18, -255, -4620, -94500, -2078802, -48005802]
b_expected = [0, 3, 27, 417, 7851, 164124, 3661389, 85384566]

# Build A(τ) as polynomial truncated at order 7
N = 7
A = sum(Rational(a_vals[k]) * tau**k for k in range(N+1))

# Compute (1 + 4A) truncated
one_plus_4A = 1 + 4*A

# Series expansion of sqrt(1 + 4A) around tau=0 up to order N
# Use (1 + x)^(1/2) = sum C(1/2, k) x^k
# But easier: compute using Newton's method or series
sqrt_expr = sqrt(one_plus_4A)
sq_series = series(sqrt_expr, tau, 0, N+1).removeO()

# F = (1 - sqrt) / 2
F = (1 - sq_series) / 2
F_poly = Poly(expand(F), tau)

print("F coefficients (k=0..7):")
for k in range(N+1):
    c = F_poly.nth(k)
    exp = b_expected[k]
    match = "OK" if c == exp else "MISMATCH"
    print(f"  b_{k} = {c}   (expected {exp})  {match}")

# Also verify (1-2F)^2 = 1 + 4A
M = 1 - 2*F
M_sq = expand(M*M)
diff = expand(M_sq - one_plus_4A)
# Truncate to order N
diff_poly = Poly(diff, tau)
truncated_diff = sum(diff_poly.nth(k) * tau**k for k in range(N+1))
print(f"\n(1-2F)^2 - (1+4A) truncated to order {N}: {truncated_diff}")
