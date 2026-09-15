"""
Day 180 — Stronger tests.

Discovery: T_S(u_S) = 0 identically for |S| >= 4 (when m = 1)!

Test:
1. |S| = 6, 7 confirm the pattern.
2. Test T_S^{(r)}(u_S) := sum_{ij subset S} (u_i+u_j+1)(u_i+u_j)^r prod Delta.
   These arise when m contains E_2 or E_3 (which shift with u_i+u_j).
3. Test T_S^{[r,s]}(u_S) := sum ... (u_i+u_j+1)(u_i+u_j)^r (u_i^2+u_j^2)^s prod Delta.
"""

import sympy as sp
from itertools import combinations

def delta(u, i, j, l):
    return 1/(u[i]-u[l]) + 1/(u[j]-u[l]) + 1/((u[i]-u[l])*(u[j]-u[l]))

def T_S_weighted(u, S, weight_fn):
    """Sum over pairs of weight_fn(u_i, u_j) * prod Delta."""
    total = sp.Integer(0)
    for (i, j) in combinations(S, 2):
        L = [l for l in S if l != i and l != j]
        prod = sp.Integer(1)
        for l in L:
            prod *= delta(u, i, j, l)
        weight = (u[i] + u[j] + 1) * weight_fn(u[i], u[j])
        total += weight * prod
    return sp.simplify(sp.together(total))

# Test |S| = 6
print("|S| = 6, m = 1")
n = 6
u = sp.symbols(f'u0:{n}')
val = T_S_weighted(u, list(range(n)), lambda x, y: 1)
print(f"  T_S = {val}")
print()

# Test T_S^{(r)} for various r at |S| = 4
print("|S| = 4, various weight functions")
n = 4
u = sp.symbols(f'v0:{n}')

# (u_i + u_j) weighted
val1 = T_S_weighted(u, list(range(n)), lambda x, y: x + y)
val1_expand = sp.expand(val1)
print(f"  T_S^{{(1)}} = sum (u_i+u_j+1)(u_i+u_j) prod Delta")
print(f"    = {val1_expand}")
print()

# (u_i + u_j)^2 weighted
val2 = T_S_weighted(u, list(range(n)), lambda x, y: (x + y)**2)
val2_expand = sp.expand(val2)
print(f"  T_S^{{(2)}} = sum (u_i+u_j+1)(u_i+u_j)^2 prod Delta")
print(f"    = {val2_expand}")
print()

# u_i^2 + u_j^2 weighted (relevant for E_3 shift)
val3 = T_S_weighted(u, list(range(n)), lambda x, y: x**2 + y**2)
val3_expand = sp.expand(val3)
print(f"  T_S^{{(2,sq)}} = sum (u_i+u_j+1)(u_i^2+u_j^2) prod Delta")
print(f"    = {val3_expand}")
print()

# Verify T_S^{(1)} at |S| = 5
print("|S| = 5, weight (u_i + u_j)")
n = 5
u = sp.symbols(f'w0:{n}')
val = T_S_weighted(u, list(range(n)), lambda x, y: x + y)
val_expand = sp.expand(val)
print(f"  T_S^{{(1)}} = {val_expand}")
print()

# Test m|_{ij} = u_i * u_j (a polynomial in the shift, one term in E_2)
print("|S| = 4, weight u_i * u_j")
n = 4
u = sp.symbols(f'x0:{n}')
val = T_S_weighted(u, list(range(n)), lambda x, y: x * y)
val_expand = sp.expand(val)
print(f"  T_S^{{p}} = sum (u_i+u_j+1)(u_i u_j) prod Delta")
print(f"    = {val_expand}")
