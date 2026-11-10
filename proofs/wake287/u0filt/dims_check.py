"""Exact dims: rho(U0), S_0=End_H(V) (commutant), and locality of End_H(P_(a,b)) for n=2 summands."""
import sys, flint, sympy as sp
from core import setup, T_ops, U0_ops, algebra_span
def commutant_dim(gens, d):
    rows = []
    for g in gens:
        G = [[int(g[r, c]) for c in range(d)] for r in range(d)]
        # X g - g X = 0 ; X as d*d unknowns x[r*d+c]
        for r in range(d):
            for c in range(d):
                row = [0]*(d*d)
                for k in range(d):
                    if G[k][c]: row[r*d+k] += G[k][c]
                    if G[r][k]: row[k*d+c] -= G[r][k]
                rows.append(row)
    return d*d - flint.fmpz_mat(rows).rank()
for (n, N) in [(2, 3), (2, 4), (3, 3)]:
    W, idx, d = setup(n, N)
    print((n, N), 'dim rho(U0) =', len(algebra_span(list(U0_ops(n, N).values()), d)), ' dim S_0 = dim End_H(V) =', commutant_dim(T_ops(n, N), d))
