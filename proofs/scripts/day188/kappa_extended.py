#!/usr/bin/env python3
"""
Day 188 - Extend Speicher-Nica free cumulants kappa_k of b_k to k=1..12.

Approach:
  1. Recompute b_k for k=1..12 by Lagrange inversion of F(1-F)^3(3-4F) = t(3-2F)^2.
     (Also sanity-check against the 12-term list in day183 OEIS draft.)
  2. Solve the Nica-Speicher functional equation
        M(z) = 1 + K(z * M(z)),   K(z) = sum_{k>=1} kappa_k z^k, M(z) = sum b_k z^k
     for kappa_1, ..., kappa_12 by matching coefficients mod z^13.
  3. Report divisibility by 3, 9, 27, ...
"""
import sympy as sp

N = 13  # work modulo z^N (compute up to k = N-1 = 12)
z = sp.symbols('z')

# ----------------------------------------------------------------------
# 1. Compute b_k for k=0..12 by series-solving F(1-F)^3(3-4F) = z(3-2F)^2.
# ----------------------------------------------------------------------
b_syms = sp.symbols('b1:13')  # b_1 .. b_12
F = sum(b_syms[i] * z**(i+1) for i in range(12))
lhs = sp.expand(F * (1-F)**3 * (3 - 4*F))
rhs = sp.expand(z * (3 - 2*F)**2)
diff = sp.series(lhs - rhs, z, 0, N).removeO()
diff = sp.expand(diff)

b_vals = {}
for k in range(1, N):
    coeff = sp.Poly(diff, z).coeff_monomial(z**k)
    coeff = coeff.subs(b_vals)
    sol = sp.solve(coeff, b_syms[k-1])
    assert len(sol) == 1
    b_vals[b_syms[k-1]] = sol[0]

b = [1] + [int(b_vals[b_syms[k-1]]) for k in range(1, N)]

expected_b = [1, 3, 27, 417, 7851, 164124, 3661389, 85384566, 2056373739,
              50751637140, 1276862920140, 32626363346505, 844375375808301]
assert b == expected_b, f"b_k mismatch: {b} vs {expected_b}"
print("b_k (k=0..12):")
for k, val in enumerate(b):
    print(f"  b_{k:>2} = {val}")
print()

# ----------------------------------------------------------------------
# 2. Solve for Speicher-Nica free cumulants kappa_1..kappa_12.
#    Functional equation: M(z) = 1 + K(z*M(z))
#    where M(z) = 1 + sum b_k z^k, K(u) = sum kappa_k u^k.
# ----------------------------------------------------------------------
M = sum(b[k] * z**k for k in range(N))          # 1 + b_1 z + b_2 z^2 + ...
k_syms = sp.symbols('k1:13')                    # kappa_1 .. kappa_12
u = sp.Symbol('u')
K_of_u = sum(k_syms[i] * u**(i+1) for i in range(12))
K_sub = K_of_u.subs(u, z * M)
K_ser = sp.series(K_sub, z, 0, N).removeO()
K_poly = sp.expand(K_ser)

# Match [z^k] (1 + K(z*M(z))) = b_k, for k=1..12.
kappa_vals = {}
for k in range(1, N):
    coeff = sp.Poly(K_poly, z).coeff_monomial(z**k)
    coeff = coeff.subs(kappa_vals)
    eqn = sp.Eq(coeff, b[k])
    sol = sp.solve(eqn, k_syms[k-1])
    assert len(sol) == 1
    kappa_vals[k_syms[k-1]] = sol[0]

kappa = [int(kappa_vals[k_syms[i]]) for i in range(12)]

# Sanity: first five match Rick's Day 186 values.
expected_first5 = [3, 18, 228, 3414, 57051]
assert kappa[:5] == expected_first5, f"first5 mismatch: {kappa[:5]} vs {expected_first5}"

print("kappa_k (Speicher-Nica free cumulants of b_k) for k=1..12:")
for k in range(1, 13):
    print(f"  kappa_{k:>2} = {kappa[k-1]}")
print()

# ----------------------------------------------------------------------
# 3. Divisibility by 3, 9, 27, ...
# ----------------------------------------------------------------------
def three_adic_valuation(n):
    n = abs(int(n))
    if n == 0:
        return float('inf')
    v = 0
    while n % 3 == 0:
        n //= 3
        v += 1
    return v

print("3-adic valuations v_3(kappa_k):")
for k in range(1, 13):
    v = three_adic_valuation(kappa[k-1])
    print(f"  v_3(kappa_{k:>2}) = {v}    (kappa_{k}/3 = {kappa[k-1] // 3})")
print()

# Cross-check against comparable transforms.
print("Cross-check: v_3 for b_k, a_k = INVERTi(b_k), kappa_k")
# a_k = INVERTi(b_k)
B_full = sum(b[k] * z**k for k in range(N))
one_over_B = sp.series(1 / B_full, z, 0, N).removeO()
A_series = sp.expand(1 - one_over_B)
a = [int(sp.Poly(A_series, z).coeff_monomial(z**k)) for k in range(1, N)]
print(f"{'k':>3} | {'v3(b_k)':>7} | {'v3(a_k)':>7} | {'v3(kappa)':>9}")
for k in range(1, 13):
    print(f"{k:>3} | {three_adic_valuation(b[k]):>7} | {three_adic_valuation(a[k-1]):>7} | {three_adic_valuation(kappa[k-1]):>9}")
print()

# Print kappa_k / 3 for clarity
print("kappa_k / 3:")
for k in range(1, 13):
    q, r = divmod(kappa[k-1], 3)
    assert r == 0, f"kappa_{k} not divisible by 3"
    print(f"  kappa_{k}/3 = {q}")
