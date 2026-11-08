from dchar import *
from star_table import dist, nbrs, label
import sympy as sp
from itertools import combinations
n = 8; G = D(n); Nb = nbrs(n)
deg = [r[G.classes.index(((1,)*n, (), 0))] for r in G.table]
C = sorted(Con(n)); M = sp.Matrix([list(v) for v in C]).T
mult = dict(zip(C, list(sp.linsolve((M, sp.Matrix(deg))))[0]))
subsets = [frozenset(J) for k in range(n+1) for J in combinations(range(1, n+1), k)]
tot = 0
for v in C:
    g = dist(n, v, subsets); cand = []
    for A in g:
        intA = frozenset(s for s in A if Nb[s] <= A)
        for B in g:
            if B and B <= intA: cand.append((sorted(A), g[A], sorted(B), g[B]))
    if cand:
        tot += mult[v]
        print(label(n, v), 'a=', {G.a[i] for i, c in enumerate(v) if c}, '#left cells with this char:', mult[v])
        for c in cand: print('    L(x)=', c[0], f'(x{c[1]})', ' L(z)=', c[2], f'(x{c[3]})')
print('total violating left cells in D8:', tot, 'of 11504')
