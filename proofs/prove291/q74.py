# Q74: test (G**'): Ind(X [x] Y) decomposable <=> X ~ Ind(X' [x] P) and Y ~ Ind(Q [x] Y'), P,Q nonzero projective.
import sys, itertools, pickle, os, numpy as np
from math import comb
sys.path.insert(0, '/home/agent/projects/proofs/prove290'); sys.path.insert(0, '/home/agent/projects/proofs/wake289/klo75')
from gstar import leq_L, interval, product_set, dimP, module_from_set
from klo import rref_null, desL, top, end_algebra, local_test
import gstar
def analyse(B):
    B, act = module_from_set(B); n = len(B[0])
    if n == 1: return dict(d=1, ind=True, top={(): 1})
    s = min(range(len(B)), key=lambda k: sum(1 for i in range(n) for j in range(i+1, n) if B[k][i] > B[k][j]))
    try: E, F_of, _, _ = end_algebra(B, act, s, p=P)
    except AssertionError: E, F_of, _, _ = end_algebra(B, act, s, p=P, nrand=len(B) + 2)
    nd, loc = local_test(E, F_of, P)
    return dict(d=len(B), ind=loc, nd=nd, top=top(B, act))
P = 32003
rng = np.random.default_rng(3)

def dense(B):
    B, act = module_from_set(B); d = len(B); n = len(B[0]); G = {}
    for i in range(1, n):
        M = np.zeros((d, d), dtype=np.int64)
        for k in range(d):
            if act[i][k] >= 0: M[act[i][k], k] = 1
        G[i] = M
    return G, n, d, act, B

def rank(M):
    M = M.copy() % P; r = 0; m, n = M.shape
    for c in range(n):
        if r >= m: break
        nz = np.nonzero(M[r:, c])[0]
        if not len(nz): continue
        k = r + nz[0]; M[[r, k]] = M[[k, r]]
        M[r] = M[r] * pow(int(M[r, c]), P - 2, P) % P
        col = M[:, c].copy(); col[r] = 0; nzr = np.nonzero(col)[0]
        if len(nzr): M[nzr] = (M[nzr] - np.outer(col[nzr], M[r])) % P
        r += 1
    return r

def iso(A, Bm):
    GA, n, dA, actA, BA = A; GB, n2, dB, actB, BB = Bm
    if dA != dB or n != n2: return False
    if n == 1: return True
    if top(BA, actA) != top(BB, actB): return False
    rows = [(np.kron(np.eye(dA, dtype=np.int64), GB[i]) - np.kron(GA[i].T, np.eye(dB, dtype=np.int64))) % P for i in range(1, n)]
    N = rref_null(np.vstack(rows), P)
    if not N: return False
    F = sum(int(rng.integers(P)) * v for v in N) % P
    return rank(F.reshape(dB, dA, order='F')) == dA

mmax = int(sys.argv[1]); Nmax = int(sys.argv[2]); dcap = int(sys.argv[3])
cache = f'mods{mmax}.pkl'
if os.path.exists(cache): mods = pickle.load(open(cache, 'rb'))
else:
    mods = {}
    for m in range(1, mmax + 1):
        perms = list(itertools.permutations(range(1, m + 1))); seen = set()
        for s in perms:
            for r in perms:
                if leq_L(s, r):
                    B = frozenset(interval(s, r))
                    if B in seen: continue
                    seen.add(B); info = analyse(B)
                    if not info['ind']: continue
                    tp = info['top']
                    proj = (len(tp) == 1 and sum(tp.values()) == 1 and dimP(list(tp)[0], m) == info['d'])
                    mods.setdefault(m, []).append((s, r, B, proj, info['d']))
        print('m', m, len(mods[m]), 'proj', sum(x[3] for x in mods[m]), flush=True)
    pickle.dump(mods, open(cache, 'wb'))
D = {(m, j): dense(x[2]) for m in mods for j, x in enumerate(mods[m])}

def splits(m, j, side):
    """side='beg': Y ~ Ind(Q [x] Y'); side='end': X ~ Ind(X' [x] P). return list of witnesses (k, idxQ, idxY')"""
    s, r, B, proj, d = mods[m][j]
    if proj: return [('proj',)]
    out = []
    for k in range(1, m):  # k = size of projective piece, rest size m-k >= 1
        for jq, q in enumerate(mods[k]):
            if not q[3]: continue
            for jy, y in enumerate(mods[m - k]):
                if q[4] * y[4] * comb(m, k) != d: continue
                S = product_set(q[2], y[2]) if side == 'beg' else product_set(y[2], q[2])
                if iso(D[(m, j)], dense(S)): out.append((k, q[0], y[0], y[1]))
    return out

BEG = {}; END = {}
for m in mods:
    for j in range(len(mods[m])):
        BEG[(m, j)] = splits(m, j, 'beg'); END[(m, j)] = splits(m, j, 'end')
    print('m', m, 'BEG nonproj', sum(1 for j in range(len(mods[m])) if BEG[(m,j)] and BEG[(m,j)][0] != ('proj',)),
          'END nonproj', sum(1 for j in range(len(mods[m])) if END[(m,j)] and END[(m,j)][0] != ('proj',)), flush=True)
for m in mods:
    for j, x in enumerate(mods[m]):
        if BEG[(m, j)] and not x[3]: print('  BEG', x[0], x[1], 'd', x[4], BEG[(m, j)][:3])
        if END[(m, j)] and not x[3]: print('  END', x[0], x[1], 'd', x[4], END[(m, j)][:3])
cnt = 0; agree = 0; bad = []
for a in mods:
    for b in mods:
        if a + b > Nmax: continue
        for ja, X in enumerate(mods[a]):
            for jb, Y in enumerate(mods[b]):
                if comb(a + b, a) * X[4] * Y[4] > dcap: continue
                ind = analyse(product_set(X[2], Y[2]))['ind']
                pred = bool(END[(a, ja)]) and bool(BEG[(b, jb)])
                cnt += 1
                if pred == (not ind): agree += 1
                else:
                    bad.append((X[:2], Y[:2])); print('MISMATCH', X[0], X[1], '|', Y[0], Y[1], 'ind', ind, 'pred_dec', pred, flush=True)
        print('done', a, b, cnt, agree, flush=True) if False else None
    print('a', a, 'cnt', cnt, 'agree', agree, 'bad', len(bad), flush=True)
print('TOTAL', cnt, 'agree', agree, 'mismatch', len(bad))
