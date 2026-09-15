"""
Day 180 — Verify MVL structural claims:
1. Pi_P^{(S)} is a polynomial (no poles), and has expected degree.
2. Verify at multiple |S| and P.
"""

import sympy as sp
from itertools import combinations

def delta(u, i, j, l):
    return 1/(u[i]-u[l]) + 1/(u[j]-u[l]) + 1/((u[i]-u[l])*(u[j]-u[l]))

def Pi_P(u, S, P_fn):
    """Sum over pairs {i,j} in S of (u_i+u_j+1) P(u_i, u_j) * prod Delta."""
    total = sp.Integer(0)
    for (i, j) in combinations(S, 2):
        L = [l for l in S if l != i and l != j]
        prod = sp.Integer(1)
        for l in L:
            prod *= delta(u, i, j, l)
        weight = (u[i] + u[j] + 1) * P_fn(u[i], u[j])
        total += weight * prod
    total = sp.cancel(sp.together(total))
    return sp.expand(total)


def total_degree(expr, vars):
    if expr == 0:
        return -sp.oo
    p = sp.Poly(sp.expand(expr), *vars)
    return p.total_degree()


# Battery of tests
test_cases = [
    # (|S|, degree_P, symbolic P as (x, y) -> expr, name)
    (3, 0, lambda x, y: 1, "1"),
    (3, 1, lambda x, y: x + y, "s"),
    (3, 2, lambda x, y: x*y, "p"),
    (3, 2, lambda x, y: x**2 + y**2, "q"),
    (3, 3, lambda x, y: (x+y)**3, "s^3"),
    (4, 0, lambda x, y: 1, "1"),
    (4, 1, lambda x, y: x + y, "s"),
    (4, 2, lambda x, y: x*y, "p"),
    (4, 2, lambda x, y: x**2 + y**2, "q"),
    (4, 3, lambda x, y: (x+y)**3, "s^3"),
    (4, 3, lambda x, y: x*y*(x+y), "sp"),
    (5, 0, lambda x, y: 1, "1"),
    (5, 1, lambda x, y: x + y, "s"),
    (5, 2, lambda x, y: (x+y)**2, "s^2"),
    (5, 2, lambda x, y: x*y, "p"),
    (5, 3, lambda x, y: (x+y)**3, "s^3"),
]

for size, dP, P_fn, name in test_cases:
    predicted_deg_max = dP - (size - 3)
    n = size
    u = sp.symbols(f'u_{size}_{name.replace("^","").replace("*","")}_0:{n}')
    S = list(range(n))
    val = Pi_P(u, S, P_fn)
    val_expand = sp.expand(val)
    if val_expand == 0:
        actual_deg = -sp.oo
    else:
        actual_deg = total_degree(val_expand, u)
    pass_ = (actual_deg <= predicted_deg_max) if actual_deg != -sp.oo else True
    status = "PASS" if pass_ else "FAIL"
    print(f"|S|={size} P={name} deg={dP}:  predicted deg <= {predicted_deg_max}, actual={actual_deg}  [{status}]")
