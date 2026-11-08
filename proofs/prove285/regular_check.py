from dchar import *
import sympy as sp, sys
for n in range(4, 9):
    G = D(n); deg = [r[G.classes.index(((1,)*n, (), 0))] for r in G.table]
    C = sorted(Con(n)); M = sp.Matrix([list(v) for v in C]).T
    r = M.rank()
    # solve M x = deg ; if not full column rank, report
    sol = sp.linsolve((M, sp.Matrix(deg)))
    print(f'D{n}: #Con={len(C)} rank={r} solution={"unique" if r==len(C) else "param"}', end=' ')
    s = list(sol)[0]
    if r == len(C):
        ok = all(x.is_integer and x >= 0 for x in s); print('nonneg-int', ok, '#left cells =', sum(s))
    else:
        print(s)
