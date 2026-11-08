from dchar import *
from itertools import combinations
from math import factorial
import sys
for n in range(2, int(sys.argv[1])+1):
    G = D(n); deg = [r[G.classes.index(((1,)*n,(),0))] for r in G.table]
    bad = 0
    for k in range(n+1):
        for J in combinations(range(1, n+1), k):
            J = frozenset(J); f = fvec(n, J)
            # |W_J|
            if n in J and n-1 not in J: Jp = frozenset(n-1 if j==n else j for j in J)
            else: Jp = J
            ks, m = J_blocks(n, Jp)
            o = D(m).order
            for x in ks: o *= factorial(x)
            if sum(d*x for d, x in zip(deg, f)) * o != G.order: bad += 1
    C = Con(n)
    print(n, 'index-check bad', bad, '#Con', len(C), 'irr', len(G.irr), flush=True)
