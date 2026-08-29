"""
Explore patterns in c_i and g_i.
c_i = 3, 9, 58/3, 322/9, 1639/27, 7879/81, 36376/243
g_i = 1/3, -1, 23/27, -7/81, -4/81, -20/729, -32/2187
"""
from sympy import Rational, factorint, gcd, factor

c = [Rational(3), Rational(9), Rational(58,3), Rational(322,9), Rational(1639,27), Rational(7879,81), Rational(36376,243)]

# Scale by 3^i to clear denominators
print("3^i * c_i:")
for i, v in enumerate(c):
    scaled = v * Rational(3)**i
    print(f"  i={i}: {scaled}  (factored: {factorint(int(scaled)) if scaled==int(scaled) else 'non-integer'})")

print()
# Ratios c_{i+1}/c_i
print("Ratios c_{i+1}/c_i:")
for i in range(len(c)-1):
    r = c[i+1]/c[i]
    print(f"  c_{i+1}/c_{i} = {r} ≈ {float(r):.6f}")

# Look at numerators of c after multiplying by 3^i
print("\nNumerators of 3^i · c_i: 3, 27, 174, 966, 4917, 23637, 109128")
nums = [3, 27, 174, 966, 4917, 23637, 109128]
# Try ratios and differences
print("Differences:")
for i in range(len(nums)-1):
    print(f"  {nums[i+1]} - {nums[i]} = {nums[i+1]-nums[i]}")

# Try dividing by 3
print("\nDivided by 3:")
for n in nums:
    print(f"  {n}/3 = {Rational(n,3)}")

# Try c_i · 3
print("\n3·c_i (rescale):")
for v in c:
    print(f"  {3*v}")

# Alternative: search OEIS-like — numerators of 3·c_i minus constant?
# c_0=3, c_1=9, c_2=58/3
# What about h(τ)/(1-τ)^something?
print()

# Try to see if h(τ) has a nice closed form:
# h(0) = 3, h'(0) = 9, h''(0)/2 = 58/3, h'''(0)/6 = 322/9 ...
# So h(τ) = 3 + 9τ + (58/3)τ² + (322/9)τ³ + (1639/27)τ⁴ + (7879/81)τ⁵ + (36376/243)τ⁶ ...
# Let me try h(τ) = 3/(1 - 3τ)^α for various α
# then [τ^k] h = 3 · C(-α, k) · (-3)^k · ??? Hmm, generalized binomial
# [τ^k] (1-3τ)^{-α} = C(α+k-1, k) · 3^k
# So h(τ) = 3(1-3τ)^{-α} gives c_k = 3 · C(α+k-1, k) · 3^k
# c_1/c_0 · 1/3 = 1 → α = 1: then c_1 = 3·1·3 = 9 ✓
# c_2 with α=1: 3 · C(2,2) · 9 = 3·1·9 = 27. But actual c_2 = 58/3. NO.

# Try h = 3(1 + aτ + bτ² + ...) — write out normalized coefficients c_i / 3:
print("c_i / 3:")
for v in c:
    print(f"  {v/3}")

# 1, 3, 58/9, 322/27, 1639/81, ...

# Test: perhaps h(τ)^3 has nicer coefficients?
from sympy import Symbol, Poly, expand
tau = Symbol('tau')
hpoly = sum(c[i]*tau**i for i in range(len(c)))
h3 = expand(hpoly**3)
h3poly = Poly(h3, tau)
print("\nCoefficients of h(τ)^3:")
for k in range(10):
    v = h3poly.nth(k)
    print(f"  [τ^{k}] h^3 = {v}")

# Also compute τ/h(τ) — the function whose comp. inverse is F.
# We already have G(x) = comp. inv. of F. So if F is comp. inv. of x/h(x),
# then G(x) = x/h(x)?  Let me check: F is comp inv of G means F(G(x))=x, G(F(τ))=τ.
# If G(τ) = τ/h(τ), then τ/h(τ) is what we should compare with the computed G.

# G computed: g_1=1/3, g_2=-1, g_3=23/27, g_4=-7/81, g_5=-4/81, g_6=-20/729, g_7=-32/2187
# τ/h(τ) with h(0)=3 means leading term τ/3 = (1/3)τ, matches g_1=1/3.
# Then τ/h(τ) = τ · (1/3) · 1/(1 + 3τ + (58/9)τ² + ...)
# So h(τ) = τ/G(τ). Let's compute.

Gpoly_expr = sum({1: Rational(1,3), 2: Rational(-1), 3: Rational(23,27), 4: Rational(-7,81),
                  5: Rational(-4,81), 6: Rational(-20,729), 7: Rational(-32,2187)}[k] * tau**k
                 for k in range(1,8))
# Now h(τ) = τ / G(τ) — compute series
# G(τ) = (τ/3)(1 - 3τ + (23/9)τ² - (7/27)τ³ - ...)
# G(τ)/τ = 1/3 - τ + (23/27)τ² - ...
Gover_tau = Rational(1,3) - tau + Rational(23,27)*tau**2 - Rational(7,81)*tau**3 - Rational(4,81)*tau**4 - Rational(20,729)*tau**5 - Rational(32,2187)*tau**6

# 1/(G/τ) = h(τ), compute reciprocal series
from sympy import series
h_from_G = series(1/Gover_tau, tau, 0, 8).removeO()
print("\nh(τ) computed via τ/G(τ):")
h_from_G_poly = Poly(expand(h_from_G), tau)
for k in range(7):
    print(f"  [τ^{k}] h = {h_from_G_poly.nth(k)}")
