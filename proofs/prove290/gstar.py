# Test (G*): X, Y indecomposable weak-Bruhat interval modules => X [x] Y indecomposable unless both projective.
# Interval module B(s,r) on [s,r]_L in S_m; product = positions-concatenation, values shuffled (JKLO / KLO A.2(1)).
import sys, itertools, json, numpy as np
sys.path.insert(0, '/home/agent/projects/proofs/wake289/klo75')
from klo import end_algebra, local_test, top, check_relations, desL

P = 32003

def sw(g, i):
    return tuple(i + 1 if v == i else i if v == i + 1 else v for v in g)

def leq_L(s, r):
    # s <=_L r iff POSITION-pair inversion sets nested (left mult swaps values i,i+1 = changes one position pair)
    def inv(g):
        return {(p, q) for p in range(len(g)) for q in range(p + 1, len(g)) if g[p] > g[q]}
    return inv(s) <= inv(r)

def module_from_set(B):
    B = sorted(B); idx = {g: k for k, g in enumerate(B)}; n = len(B[0]); d = len(B)
    act = {}
    for i in range(1, n):
        a = np.empty(d, dtype=np.int64)
        for k, g in enumerate(B):
            if i in desL(g): a[k] = k
            else: a[k] = idx.get(sw(g, i), -1)
        act[i] = a
    return B, act

def interval(s, r):
    n = len(s); out = {s}; q = [s]
    while q:
        g = q.pop()
        for i in range(1, n):
            if i not in desL(g):
                h = sw(g, i)
                if h not in out and leq_L(h, r): out.add(h); q.append(h)
    return out

def product_set(BX, BY):
    a = len(next(iter(BX))); b = len(next(iter(BY))); N = a + b
    out = set()
    for S in itertools.combinations(range(1, N + 1), a):
        Sc = [v for v in range(1, N + 1) if v not in S]
        for x in BX:
            for y in BY:
                out.add(tuple(S[v - 1] for v in x) + tuple(Sc[v - 1] for v in y))
    return out

def analyse(B):
    B, act = module_from_set(B)
    n = len(B[0])
    if n > 1: check_relations(act, n)
    # generator = unique minimal element (min length)
    s = min(range(len(B)), key=lambda k: len([1 for i in range(n) for j in range(i+1, n) if B[k][i] > B[k][j]]))
    if n == 1: return dict(d=1, ind=True, top={(): 1}, nE=1)
    E, F_of, _, _ = end_algebra(B, act, s, p=P)
    nd, loc = local_test(E, F_of, P)
    return dict(d=len(B), ind=loc, nd=nd, nE=len(E), top=top(B, act))

def dimP(D, m):
    return sum(1 for w in itertools.permutations(range(1, m + 1)) if desL(w) == frozenset(D))

if __name__ == '__main__':
    mmax = int(sys.argv[1]); Nmax = int(sys.argv[2]); dcap = int(sys.argv[3])
    mods = {}
    for m in range(1, mmax + 1):
        perms = list(itertools.permutations(range(1, m + 1)))
        seen = set()
        for s in perms:
            for r in perms:
                if leq_L(s, r):
                    B = frozenset(interval(s, r))
                    if B in seen: continue
                    seen.add(B)
                    info = analyse(B)
                    if not info['ind']: continue
                    tp = info['top']
                    proj = (len(tp) == 1 and sum(tp.values()) == 1 and dimP(list(tp)[0], m) == info['d'])
                    mods.setdefault(m, []).append((s, r, B, proj, info['d']))
        print('m', m, 'indec intervals', len(mods[m]), 'proj', sum(x[3] for x in mods[m]), flush=True)
    bad = []; cnt = 0
    for a in range(1, mmax + 1):
        for b in range(1, mmax + 1):
            if a + b > Nmax: continue
            for (s, r, BX, pX, dX) in mods[a]:
                for (s2, r2, BY, pY, dY) in mods[b]:
                    from math import comb
                    if comb(a + b, a) * dX * dY > dcap: continue
                    info = analyse(product_set(BX, BY))
                    cnt += 1
                    exp_dec = pX and pY
                    if info['ind'] == exp_dec:
                        bad.append((s, r, s2, r2, pX, pY, info['ind'], info['nd']))
                        print('VIOLATION', s, r, '|', s2, r2, 'proj', pX, pY, 'ind', info['ind'], 'nd', info['nd'], 'd', info['d'], flush=True)
        print('done a+b..', a, cnt, len(bad), flush=True)
    print('TOTAL', cnt, 'violations', len(bad))
