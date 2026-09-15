"""
Day 180 — Test polynomial-degree pattern.

Conjecture: for |S| = k+2, T_S^{(r)} = sum (u_i+u_j+1)(u_i+u_j)^r prod Delta
has polynomial degree in u_S at most r - (k-1) = r - k + 1 = r - |S| + 3.

Equivalently, T_S^{(r)} = 0 for r < |S| - 3.
"""

import sympy as sp
from itertools import combinations

def delta(u, i, j, l):
    return 1/(u[i]-u[l]) + 1/(u[j]-u[l]) + 1/((u[i]-u[l])*(u[j]-u[l]))

def T_S_weighted(u, S, weight_fn):
    total = sp.Integer(0)
    for (i, j) in combinations(S, 2):
        L = [l for l in S if l != i and l != j]
        prod = sp.Integer(1)
        for l in L:
            prod *= delta(u, i, j, l)
        weight = (u[i] + u[j] + 1) * weight_fn(u[i], u[j])
        total += weight * prod
    return sp.simplify(sp.together(total))


def deg_in_u(expr, u):
    """Degree of poly expr in variables u (total)."""
    if expr == 0:
        return -1
    p = sp.Poly(sp.expand(expr), *u)
    return p.total_degree()


for size in [4, 5, 6]:
    print(f"=== |S| = {size} (k = {size - 2}) ===")
    n = size
    u = sp.symbols(f'u{size}_0:{n}')
    S = list(range(n))
    for r in range(0, size + 1):
        val = T_S_weighted(u, S, lambda x, y, r=r: (x + y)**r)
        deg = deg_in_u(val, u)
        # Also symmetric-form
        if val != 0:
            val_e = sp.expand(val)
            print(f"  T_S^{{({r})}}: deg_u = {deg},  = {val_e}")
        else:
            print(f"  T_S^{{({r})}}: 0")
    print()

# Test the "square-power" family: (u_i^k + u_j^k) with prod Delta
print("=" * 60)
print("Square/higher-power families (for E_3 shift analysis)")
print("=" * 60)

for size in [4, 5]:
    print(f"=== |S| = {size} ===")
    n = size
    u = sp.symbols(f'v{size}_0:{n}')
    S = list(range(n))
    # (u_i^r + u_j^r) family
    for r in range(0, size):
        val = T_S_weighted(u, S, lambda x, y, r=r: x**r + y**r)
        if val != 0:
            val_e = sp.expand(val)
            deg = deg_in_u(val, u)
            print(f"  sum (u_i+u_j+1)(u_i^{r}+u_j^{r}) prod Delta:  deg={deg}, val={val_e}")
        else:
            print(f"  sum (u_i+u_j+1)(u_i^{r}+u_j^{r}) prod Delta:  0")
    print()
