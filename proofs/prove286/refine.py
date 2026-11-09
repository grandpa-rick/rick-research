"""Refine Geck classes by right star operations (x ~_L y => x* ~_L y*), iterate to fixed point."""
import sys
from geck import *
from d8lib import edges
def rstar(w, s, t):
    R = rdes(w)
    if (s in R) == (t in R): return None
    for u in (rmul(w, s), rmul(w, t)):
        Ru = rdes(u)
        if (s in Ru) != (t in Ru): return u
def refine_all(elems, n, key0):
    E = edges(n)
    lab = dict(key0)
    while True:
        ids = {}
        new = {}
        for w in elems:
            sig = (lab[w],) + tuple(lab[v] if (v := rstar(w, s, t)) is not None else None for s, t in E)
            new[w] = ids.setdefault(sig, len(ids))
        nold = len(set(lab.values()))
        lab = new
        if len(ids) == nold: return lab
def validate(n):
    nat = load('D', n)
    ca = {k: components(n, k) for k in range(1, n+1)}
    k0 = {w: full_key(w, n, ca) for w in nat}
    lab = refine_all(list(nat), n, k0)
    from collections import defaultdict
    cls = defaultdict(set); cell = defaultdict(set)
    for w, c in nat.items(): cls[lab[w]].add(w); cell[c].add(w)
    bad = sum(len({lab[w] for w in S}) != 1 for S in cell.values())
    exact = sum(cls[lab[next(iter(S))]] == S for S in cell.values())
    print(f'D{n}: {len(cell)} cells, {len(cls)} refined classes, split {bad}, exact {exact}')
if __name__ == '__main__':
    for n in map(int, sys.argv[1:]): validate(n)
