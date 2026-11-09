"""PROVE 286: decide D8 (*)-violator types.  usage: decide.py TYPE seed maxseeds
1. seed x with L(x)=A (candidate set of TYPE), F2-piece dist <= target;
2. U(x) = Geck+right-star upper bound (union of left cells) ; want |U|=dim, dist(U)=target;
3. kill every candidate pair (x,z) of U with an F2-certified W_i witness y (mu~(y,z)=0)."""
import sys, pickle, random, time, itertools, json
sys.path.insert(0, '/home/agent/projects/proofs/prove286'); sys.path.insert(0, '/home/agent/projects/proofs/wake285')
from d8class import *
from d8lib import Cox, mu_from, f2_closure, ldes, rdes, lmul, length, word, nbrs
from collections import Counter
n = 8
C8 = pickle.load(open('/home/agent/projects/proofs/prove286/cons8.pkl', 'rb'))
NB = nbrs(n)
def interior(A): return frozenset(s for s in A if NB[s] <= A)
def dist(S): return Counter(ldes(u) for u in S)
def leq(d, t): return all(t.get(A, 0) >= c for A, c in d.items())

def decomposable(T, dim):
    """Can T be written as a sum of >=2 constructible dists?"""
    items = [(k, Counter(v['dist']), v['dim']) for k, v in C8.items() if v['dim'] < dim and leq(v['dist'], T)]
    T = Counter(T)
    def dfs(rem, start, cnt):
        if not +rem: return cnt >= 2
        for i in range(start, len(items)):
            k, d, _ = items[i]
            if all(rem[A] >= c for A, c in d.items()):
                r2 = rem.copy(); r2.subtract(d)
                if dfs(r2, i, cnt+1): return True
        return False
    return dfs(T, 0, 0)

class MU:
    def __init__(self):
        self.cox = Cox('D', 8); self.c = {}
    def mu(self, a, b):
        la, lb = length(a), length(b)
        if la == lb or (la - lb) % 2 == 0: return 0
        if la > lb: a, b, la, lb = b, a, lb, la
        k = (a, b)
        if k not in self.c:
            P = self.cox.pol(word(a), word(b)) if la else self.cox.pol('', word(b))
            self.c[k] = mu_from(P, la, lb)
        return self.c[k]

def f2_witnesses(x):
    Lx = ldes(x); out = []
    for r in range(1, n+1):
        y = lmul(r, x); Ly = ldes(y)
        if not (Lx <= Ly) and not (Ly <= Lx): out.append((r, y))
    return out

def kill_pairs(U, M, log):
    Ls = {u: ldes(u) for u in U}
    pairs = [(x, z) for x in U for z in U if z != x and Ls[z] and Ls[z] <= interior(Ls[x])]
    log(f'  candidate pairs in U: {len(pairs)}  shapes {sorted(Counter((tuple(sorted(Ls[x])), tuple(sorted(Ls[z]))) for x, z in pairs).items())}')
    res = []
    for x, z in pairs:
        W = f2_witnesses(x)
        assert W
        if (length(x) - length(z)) % 2:
            res.append(dict(x=word(x), z=word(z), A=sorted(Ls[x]), B=sorted(Ls[z]), verdict='NO', why='parity',
                            y=word(W[0][1]), r=W[0][0])); continue
        k = None
        for r, y in W:
            if M.mu(y, z) == 0: k = (r, y); break
        if k: res.append(dict(x=word(x), z=word(z), A=sorted(Ls[x]), B=sorted(Ls[z]), verdict='NO', why='W_i F2 witness mu=0',
                              y=word(k[1]), r=k[0]))
        else: res.append(dict(x=word(x), z=word(z), A=sorted(Ls[x]), B=sorted(Ls[z]), verdict='SURVIVES F2 witnesses',
                              mus=[(r, M.mu(y, z)) for r, y in W]))
    return res

if __name__ == '__main__':
    K = sys.argv[1]; random.seed(int(sys.argv[2])); maxs = int(sys.argv[3])
    T = C8[K]; tgt = T['dist']; dim = T['dim']
    logf = open(f'/home/agent/projects/proofs/prove286/out_{K.replace("[","").replace("]","").replace(".","_").replace("+","P")}.txt', 'a')
    def log(s): print(s, flush=True); logf.write(s + '\n'); logf.flush()
    log(f'=== {K} dim {dim} seed {sys.argv[2]} decomposable target? {decomposable(tgt, dim)}')
    As = sorted({A for A, B in pickle.load(open('/home/agent/projects/proofs/wake285/targets8.pkl', 'rb'))[K]['cand']}, key=sorted)
    A = As[0]
    # all x with L(x)=A : x^{-1} has R = A
    xs = [inverse(u) for u in same_R(n, A)]
    random.shuffle(xs)
    log(f'  |{{x: L(x)={sorted(A)}}}| = {len(xs)}')
    B = Bounder(n); pools = {}; seen = set(); tried = 0
    for x in xs:
        if x in seen: continue
        P = f2_closure(x, n, cap=3000)
        if P is None: continue
        seen |= P
        if len(P) > dim or not leq(dist(P), tgt): continue
        tried += 1
        if tried > maxs: break
        R = rdes(x)
        if R not in pools:
            t0 = time.time(); pools[R] = same_R(n, R); log(f'  pool R={sorted(R)} {len(pools[R])} ({time.time()-t0:.0f}s)')
        t0 = time.time()
        U = bound(x, B, pools[R], log=lambda s: None)
        dU = dist(U)
        log(f'  seed {word(x)} piece {len(P)} -> U {len(U)} ({time.time()-t0:.0f}s) dist==target {dict(dU)==tgt}')
        if len(U) == dim and dict(dU) == tgt:
            log(f'  REP CELL FOUND: seed {word(x)}  R={sorted(R)}  |U|={len(U)}')
            pickle.dump(dict(K=K, x=x, U=U), open(f'/home/agent/projects/proofs/prove286/rep_{abs(hash(K))%10**6}.pkl', 'wb'))
            M = MU()
            res = kill_pairs(U, M, log)
            for r in res: log('  ' + json.dumps(r))
            log(f'  verdicts {Counter(r["verdict"] for r in res)}  pol calls {M.cox.ncalls}')
            M.cox.close()
            break
