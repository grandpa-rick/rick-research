"""Analyze the invariant sequence: try common normalizations, ratios, D-finite recurrences."""
from sympy import (Rational, Integer, factorial, factorint, symbols, Matrix,
                   solve, simplify, together, expand, nsimplify, gcd, Poly)
from fractions import Fraction

# The universal invariant
a = [Integer(-3), Integer(-18), Integer(-255), Integer(-4620), Integer(-94500),
     Integer(-2078802), Integer(-48005802)]

print("=== Raw sequence ===")
for k, v in enumerate(a, 1):
    print(f"  a_{k} = {v}   |a_k| factors: {factorint(abs(int(v)))}")

print("\n=== Ratios a_{k+1}/a_k ===")
for k in range(len(a) - 1):
    r = Rational(a[k+1], a[k])
    print(f"  a_{k+2}/a_{k+1} = {r} ≈ {float(r):.5f}")

print("\n=== Various normalizations ===")
print("  a_k / (2k-1)!!:")
dbl_fact = [1, 3, 15, 105, 945, 10395, 135135]
for k in range(len(a)):
    r = Rational(a[k], dbl_fact[k])
    print(f"    k={k+1}: {r}")

print("  a_k / (3k-1)!:")
for k in range(len(a)):
    r = Rational(a[k], factorial(3*(k+1)-1))
    print(f"    k={k+1}: {r} (denom factored: {factorint(int(r.q))})")

print("  a_k / (3k)!:")
for k in range(len(a)):
    r = Rational(a[k], factorial(3*(k+1)))
    print(f"    k={k+1}: {r}")

print("  a_k / k!:")
for k in range(len(a)):
    r = Rational(a[k], factorial(k+1))
    print(f"    k={k+1}: {r}")

print("  a_k · k!:")
for k in range(len(a)):
    r = a[k] * factorial(k+1)
    print(f"    k={k+1}: {r}")

print("\n=== Test linear P-recurrence  Σ p_j(k) a_{k-j} = 0 (P-recursive) ===")
# Try order-2 recurrence: p_0(k) a_k + p_1(k) a_{k-1} + p_2(k) a_{k-2} = 0
# where p_j is polynomial in k. Try total degrees up to 3 for each.
def try_precursive(order, deg):
    """
    a_k satisfies Σ_{j=0}^{order} p_j(k) a_{k-j} = 0 where p_j is degree-deg polynomial in k.
    We have 7 values; need enough for identification.
    """
    n = len(a)
    # variables: p_j has coefficients c_{j,0}, ..., c_{j,deg}
    n_vars = (order + 1) * (deg + 1)
    from sympy import symbols
    cs = symbols(f'c0:{n_vars}')
    eqs = []
    for k in range(order, n):  # a_k, a_{k-1}, ..., a_{k-order} known; k is 0-indexed value = actual index k+1
        # Actually, let's use k+1 as the true index
        true_k = k + 1
        eq = 0
        for j in range(order + 1):
            poly_val = sum(cs[j*(deg+1) + d] * true_k**d for d in range(deg + 1))
            eq += poly_val * a[k - j]
        eqs.append(eq)
    sol = solve(eqs, cs, dict=True)
    return sol

# Try order 1, degree 4:
print("  order=1 recurrence:")
for deg in range(0, 6):
    sol = try_precursive(1, deg)
    if sol and any(any(v != 0 for v in s.values()) for s in sol):
        # nontrivial
        print(f"    deg={deg}: NONTRIVIAL SOLUTION")
        for s in sol:
            for k, v in s.items():
                if v != 0:
                    print(f"      {k} = {v}")
        break
    else:
        print(f"    deg={deg}: only trivial")

print("  order=2 recurrence:")
for deg in range(0, 4):
    sol = try_precursive(2, deg)
    if sol and any(any(v != 0 for v in s.values()) for s in sol):
        print(f"    deg={deg}: NONTRIVIAL SOLUTION")
        for s in sol:
            for k, v in s.items():
                if v != 0:
                    print(f"      {k} = {v}")
        break
    else:
        print(f"    deg={deg}: only trivial")

print("  order=3 recurrence:")
for deg in range(0, 3):
    sol = try_precursive(3, deg)
    if sol and any(any(v != 0 for v in s.values()) for s in sol):
        print(f"    deg={deg}: NONTRIVIAL SOLUTION")
        for s in sol:
            for k, v in s.items():
                if v != 0:
                    print(f"      {k} = {v}")
        break
    else:
        print(f"    deg={deg}: only trivial")
