"""Upper bound U(x) ⊇ left cell of x in D_n: Geck keys (all maximal parabolics) refined by depth-d right-star
signatures.  Every depth gives a union of left cells (Geck + KL right-star transport)."""
import sys, itertools, pickle, time
sys.path.insert(0, '/home/agent/projects/proofs/prove286')
from geck import *
from d8lib import edges, f2_closure
from refine import rstar

class Bounder:
    def __init__(self, n):
        self.n = n; self.ca = {k: components(n, k) for k in range(1, n+1)}
        self.E = edges(n); self.kc = {}; self.sc = {}; self.intern = {}
    def key(self, w):
        k = self.kc.get(w)
        if k is None: k = self.kc[w] = full_key(w, self.n, self.ca)
        return k
    def sig(self, w, d):
        m = self.sc.get((w, d))
        if m is None:
            if d == 0: t = self.key(w)
            else:
                t = (self.sig(w, d-1),) + tuple(None if (v := rstar(w, s, u)) is None else self.sig(v, d-1)
                                               for s, u in self.E)
            m = self.sc[(w, d)] = self.intern.setdefault(t, len(self.intern))
        return m

def same_R(n, R):
    out = []
    for p in itertools.permutations(range(1, n+1)):
        for sg in itertools.product((1, -1), repeat=n-1):
            s0 = 1 if sg.count(-1) % 2 == 0 else -1
            u = (p[0]*s0,) + tuple(a*b for a, b in zip(p[1:], sg))
            if rdes(u) == R: out.append(u)
    return out

def bound(x, B, pool, dmax=40, log=print, stable=5):
    S = [v for v in pool if B.key(v) == B.key(x)]
    log(f'  depth0 {len(S)}')
    same = 0
    for d in range(1, dmax+1):
        sx = B.sig(x, d)
        S2 = [v for v in S if B.sig(v, d) == sx]
        log(f'  depth{d} {len(S2)}')
        same = same + 1 if len(S2) == len(S) else 0
        S = S2
        if same >= stable: break
    return set(S)
