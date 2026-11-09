"""Predicted descent distributions (coxeter3 labels) of the 8 D8 (*)-violator types."""
import sys
sys.path.insert(0, '/home/agent/projects/proofs/prove285')
import os
os.chdir('/home/agent/projects/proofs/prove285')
from dchar import *
from star_table import dist, label
from itertools import combinations
MAP = {1:8,2:7,3:6,4:5,5:4,6:3,7:1,8:2}   # prove285 label -> coxeter3 label
def targets(n=8):
    G = D(n)
    deg = [r[G.classes.index(((1,)*n, (), 0))] for r in G.table]
    subsets = [frozenset(J) for k in range(n+1) for J in combinations(range(1, n+1), k)]
    Nb = {i: set() for i in range(1, n+1)}
    for i in range(1, n-1): Nb[i].add(i+1); Nb[i+1].add(i)
    Nb[n-2].add(n); Nb[n].add(n-2)
    out = {}
    for v in sorted(Con(n)):
        g = dist(n, v, subsets)
        cand = [(A, B) for A in g for B in g
                if B and B <= frozenset(s for s in A if Nb[s] <= A) and (B != A or g[A] >= 2)]
        if not cand: continue
        dim = sum(a*b for a, b in zip(v, deg))
        m = lambda A: frozenset(MAP[s] for s in A)
        out[label(n, v)] = dict(dim=dim, dist={m(A): c for A, c in g.items()},
                                 cand=[(m(A), m(B)) for A, B in cand])
    return out
if __name__ == '__main__':
    for k, d in targets().items(): print(k, d['dim'], [(sorted(a), sorted(b)) for a, b in d['cand']])
