"""
h(τ) = 3 + 9τ + (58/3)τ² + (322/9)τ³ + (1639/27)τ⁴ + (7879/81)τ⁵ + (36376/243)τ⁶

Numerators of c_i (multiplied by 3^i): 3, 27, 174, 966, 4917, 23637, 109128

Try: substitute σ = 3τ. Then h(σ/3) = c_0 + (c_1/3)σ + (c_2/9)σ² + ...
     coefficients become 3, 3, 58/9, 322/81, ... nope not obviously nicer.

Try: hat_h(τ) := h(τ)/3, and consider (h(τ)/3)^n
     hat_c_i = 1, 3, 58/9, 322/27, 1639/81, ...

Numerators of hat_c_i · 3^i = 3, 9, 58, 322/... wait these ARE the same as c_i but /3.

Let me look at OEIS. Numerators: 1, 3, 58, 322, 1639, 7879, 36376 (of c_i/3 · 3^i)
Actually: hat_c_i = c_i/3, and 3^i · hat_c_i = 3^{i-1} · (numerator of c_i · 3^i)
 -- getting confused. Just work with 3^i · c_i integers: 3, 27, 174, 966, 4917, 23637, 109128.
"""
from sympy import Rational, Symbol, Poly, expand, series, factor, apart, together, gcd, sqrt, factorint

tau = Symbol('tau')

# Full sequence
d = [3, 27, 174, 966, 4917, 23637, 109128]

# Try to see if this is C-finite (linear recurrence with constant coefficients)
# Test recurrence of order 2, 3, 4
print("Testing linear recurrences (constant coefficient) on d_i = 3^i · c_i:")
for order in range(2, 5):
    # d_{n} = a_1 d_{n-1} + ... + a_order d_{n-order}
    # Use `order` equations to fit coefficients from d_0..d_{2·order-1}
    if 2*order > len(d):
        continue
    from sympy import Matrix
    M = Matrix([[d[i+j] for j in range(order)] for i in range(order)])
    b_vec = Matrix([d[order+i] for i in range(order)])
    try:
        sol = M.solve(b_vec)
        # verify with remaining terms
        coefs = list(sol)
        ok = True
        for n in range(2*order, len(d)):
            pred = sum(coefs[j] * d[n-order+j] for j in range(order))
            if pred != d[n]:
                ok = False
                break
        print(f"  order {order}: {coefs}  {'MATCH' if ok else 'no fit'}")
    except Exception as e:
        print(f"  order {order}: no solution ({e})")

# Now, maybe try substitution τ → some other variable.
# Let ψ(τ) = τ · h(τ). Compute its inverse.
# Or maybe better: A(τ) has a natural gen fn interpretation via geode.

# Rick's context: (1-2F)² = 1 + 4A, which is a GEODE identity per NT.
# In the NT setup, (1 - 2xg)² = 1 - 4x  for g the Catalan gen fn.
# Here 1 + 4A takes the role of "1 - 4x". So A(τ) is like -x, i.e. maybe
# 4A(τ) = -4·(some series).

# Let φ(τ) := -A(τ). Then (1-2F)² = 1 - 4φ.  In Catalan world, g = (1-sqrt(1-4x))/(2x).
# So F = xg with x → the "parameter."  But F is a series in τ.
# Compare with Catalan: g(x) = sum C_n x^n = 1 + x + 2x² + 5x³ + ... , and 1 - 2xg(x) = sqrt(1-4x).
# So x·g(x) plays role of F. Here F(τ) with b_1=3, so if τ = 3x_true + ... , we could match.

# Let's try: what if b_k = something · Catalan · something?
# Or F(τ) = τ · G(A(τ)) for some G Catalan-like?

# Simplest: does F relate to A by F = τ + (some series in A)?
# Since (1-2F)² = 1 - 4·(-A), and (-A)(τ) = 3τ + 18τ² + ... ,
# formally F = (1 - sqrt(1 - 4(-A)))/2. So if we let u = -A(τ), then F = (1-sqrt(1-4u))/2 = u · Catalan(u).

# So F(τ) = (-A(τ)) · C(-A(τ)) where C(z) = Catalan gen fn = sum C_n z^n.
# Therefore b_k = coefficient of τ^k in u·C(u), u = -A(τ).

# But this doesn't directly give a Lagrange inversion form for F in terms of τ alone
# unless -A(τ) itself has a Lagrange form.

# Let's check the "inverse" structure differently:
# The Lagrange ansatz b_k = (1/k)[τ^{k-1}] h(τ)^k means F = τ · [ something inverse ].
# Equivalently, F is the compositional inverse of G(x) = x/h(x).
# We computed G(τ) = τ·(1/3 - τ + (23/27)τ² - (7/81)τ³ - (4/81)τ⁴ - (20/729)τ⁵ - (32/2187)τ⁶ + ...)
# so h(τ) = τ/G(τ). The h(τ) coefficients are NOT integer, they're not obviously nice.

# Test: maybe h(τ) is not the right ansatz — maybe F is Lagrange inverse of a *rational* function
# that isn't τ/h with polynomial h.

# What if τ/G(τ) equals a specific algebraic function?
# G(τ)/τ = 1/3 - τ + (23/27)τ² - (7/81)τ³ - (4/81)τ⁴ - (20/729)τ⁵ - (32/2187)τ⁶
# Multiply by 3: 3·G(τ)/τ = 1 - 3τ + (23/9)τ² - (7/27)τ³ - (4/27)τ⁴ - (20/243)τ⁵ - (32/729)τ⁶
# Numerators: 1, -3, 23/9? No.

# Try σ = τ/3 substitution in G:
# G(3σ)/σ = 1/3 · (1/3 - 3σ + (23/27)·9σ² - (7/81)·27σ³ - ...)
# Hmm.

# Substitute σ = 3τ. Then G(σ/3) = (σ/9) - σ²/9 + (23/27·9)σ³ - ...
# G(σ/3)/(σ/3) = 1/3 - σ/3 + (23/243)σ² · ... — getting messy.

# Try another substitution: what if τ = t/3? Then in variable t, F(t/3) = 3·(t/3) + 27·(t/3)² + ...
# = t + 3t² + (417/27)t³ + ... = t + 3t² + (139/9)t³ + ...
# Not nicer.

# Try τ = 3t? F(3t) = 9t + 27·9 t² + 417·27 t³ + ... too big.

# Now check: is there any simple closed form for A(τ)?
# a_k = -3, -18, -255, -4620, -94500, -2078802, -48005802
# a_k / (-3) = 1, 6, 85, 1540, 31500, 692934, 16001934
print()
print("a_k / (-3): 1, 6, 85, 1540, 31500, 692934, 16001934")
avals = [1, 6, 85, 1540, 31500, 692934, 16001934]
# Ratios
for i in range(len(avals)-1):
    r = Rational(avals[i+1], avals[i])
    print(f"  ratio {i+1}/{i}: {r} ≈ {float(r):.6f}")

# Look at b_k factorization:
b_vals = [3, 27, 417, 7851, 164124, 3661389, 85384566]
print("\nFactorizations of b_k:")
for bv in b_vals:
    print(f"  {bv} = {factorint(bv)}")

# Factorizations of a_k (absolute):
avals_abs = [3, 18, 255, 4620, 94500, 2078802, 48005802]
print("\nFactorizations of |a_k|:")
for av in avals_abs:
    print(f"  {av} = {factorint(av)}")
