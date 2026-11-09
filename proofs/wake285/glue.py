"""Glue F2-pieces into a candidate D8 left cell for a target type; certify with a reverse mu-edge."""
import pickle, random, sys, time
from collections import Counter
from d8lib import *
n = 8
T = pickle.load(open('targets8.pkl', 'rb'))
key = sys.argv[1]; random.seed(int(sys.argv[2])); tmax = float(sys.argv[3])
tgt = T[key]['dist']; dim = T[key]['dim']
def dist(P): return Counter(ldes(u) for u in P)
def rand_elt():
    p = list(range(1, n+1)); random.shuffle(p)
    sg = [random.choice((1, -1)) for _ in range(n)]
    if sg.count(-1) % 2: sg[0] *= -1
    return tuple(a*b for a, b in zip(p, sg))
def sub(d, t): return all(t.get(A, 0) >= c for A, c in d.items())
t0 = time.time(); seen = set(); tries = 0
while time.time() - t0 < tmax:
    w = rand_elt()
    if w in seen or ldes(w) not in tgt: continue
    P1 = f2_closure(w, n, cap=dim)
    if P1 is None: continue
    seen |= P1; tries += 1
    d1 = dist(P1)
    if not sub(d1, tgt) or len(P1) == dim: continue
    R = rdes(w)
    # local neighbours u -> r u with L(ru) strictly comparable to L(u), same right descent set
    nb = set()
    for u in P1:
        for r in range(1, n+1):
            v = lmul(r, u)
            if v not in P1 and rdes(v) == R: nb.add(v)
    pieces = []; covered = set()
    for v in nb:
        if v in covered: continue
        P2 = f2_closure(v, n, cap=dim)
        if P2 is None: continue
        covered |= P2
        d2 = dist(P2)
        if len(P1) + len(P2) == dim and dict(d1 + d2) == tgt: pieces.append(P2)
    if pieces:
        print(f'P1 size {len(P1)}; {len(nb)} local nbrs; matching pieces: {[len(p) for p in pieces]}  ({time.time()-t0:.1f}s, tries {tries})')
        pickle.dump(dict(key=key, P1=P1, P2s=pieces, w=w), open(f'cell_{abs(hash(key))%10**6}.pkl', 'wb'))
        print('saved', f'cell_{abs(hash(key))%10**6}.pkl'); break
else:
    print('no glue found', tries)
