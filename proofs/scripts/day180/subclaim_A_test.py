"""
Day 180 — Test Sub-claim A: for |S| >= 4, T_S(u_S) vanishes at u_l = 0 for any l in S.

Where T_S = sum over pairs {i,j} in S of (u_i+u_j+1) * prod_{l in S\{i,j}} Delta_ij(l).

For m=1. This is the base case for Lemma 2-A at k>=2.
"""

import sympy as sp
from itertools import combinations

def delta(u, i, j, l):
    return 1/(u[i]-u[l]) + 1/(u[j]-u[l]) + 1/((u[i]-u[l])*(u[j]-u[l]))

def T_S(u, S):
    """T_S(m=1) for subset S (list of indices into u)"""
    total = sp.Integer(0)
    for (i, j) in combinations(S, 2):
        L = [l for l in S if l != i and l != j]
        prod = sp.Integer(1)
        for l in L:
            prod *= delta(u, i, j, l)
        weight = u[i] + u[j] + 1
        total += weight * prod
    return sp.simplify(total)

# --- Test |S| = 4 ---
print("=" * 60)
print("Test |S| = 4: does T_S vanish at u_l = 0 for l in S?")
print("=" * 60)

n = 4
u = sp.symbols(f'u0:{n}')
S = list(range(n))

TS = T_S(u, S)
TS_simplified = sp.simplify(sp.together(TS))
print(f"T_S as symbolic:")
print(f"  simplified = {TS_simplified}")
print()

for l in S:
    val = sp.simplify(TS_simplified.subs(u[l], 0))
    print(f"  T_S|_{{u_{l}=0}} = {val}")

print()

# --- Test |S| = 5 ---
print("=" * 60)
print("Test |S| = 5: does T_S vanish at u_l = 0 for l in S?")
print("=" * 60)

n = 5
u = sp.symbols(f'v0:{n}')
S = list(range(n))

TS = T_S(u, S)
print("Simplifying T_S for |S|=5...")
TS_simplified = sp.simplify(sp.together(TS))
print(f"T_S expression length: {len(str(TS_simplified))}")

for l in S:
    val = sp.simplify(TS_simplified.subs(u[l], 0))
    print(f"  T_S|_{{v_{l}=0}} = {val}")

print()

# --- Test |S| = 3 for sanity (should NOT vanish) ---
print("=" * 60)
print("Sanity: T_S for |S| = 3 (should be 3, not vanish)")
print("=" * 60)

n = 3
u = sp.symbols(f'w0:{n}')
S = list(range(n))
TS = T_S(u, S)
TS_simplified = sp.simplify(sp.together(TS))
print(f"T_S = {TS_simplified}")
for l in S:
    val = sp.simplify(TS_simplified.subs(u[l], 0))
    print(f"  T_S|_{{w_{l}=0}} = {val}")
