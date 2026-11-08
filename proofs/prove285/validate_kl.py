"""Validate Con(D_n) descent distributions against actual KL left cells (coxkl), n=4,5."""
import sys; sys.path.insert(0, '../wake279')
from coxkl import coxeter_group, kl, left_cells
from dchar import *
from itertools import combinations
from collections import Counter

def coxD(n):
    M = [[2]*n for _ in range(n)]
    for i in range(n): M[i][i] = 1
    def e(a, b): M[a-1][b-1] = M[b-1][a-1] = 3
    for i in range(1, n-1): e(i, i+1)
    e(n-2, n)
    return M

def dist_from_vec(n, v):
    f = {}
    subsets = [frozenset(J) for k in range(n+1) for J in combinations(range(1, n+1), k)]
    for J in subsets: f[J] = sum(a*b for a, b in zip(v, fvec(n, J)))
    g = {}
    for A in subsets:
        t = sum((-1)**(len(K)-len(A)) * f[K] for K in subsets if A <= K)
        assert t >= 0
        if t: g[A] = t
    return frozenset(g.items())

n = int(sys.argv[1])
G = coxeter_group(coxD(n)); P, mu = kl(G)
cells, Ds = left_cells(G, mu)
actual = Counter()
for c in cells:
    cnt = Counter(frozenset(s+1 for s in Ds[w]) for w in c)
    actual[frozenset(cnt.items())] += 1
pred = {dist_from_vec(n, v): v for v in Con(n)}
print('cells', len(cells), 'distinct actual dists', len(actual), 'distinct predicted', len(pred))
print('actual subset of predicted:', set(actual) <= set(pred), ' equal:', set(actual) == set(pred))
for d in set(actual) - set(pred): print('UNPREDICTED', sorted((tuple(sorted(a)), b) for a, b in d))
for d in set(pred) - set(actual): print('UNREALISED', pred[d])
