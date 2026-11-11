# intrinsic test: R_k(X): X | Ind_{H_{a-k} x H_k}(Res X [x] C_[k-1]);  L_k(Y): Y | Ind(C_[k-1] [x] Res^{right} Y)
import sys, pickle, numpy as np
sys.path.insert(0, '/home/agent/projects/proofs/wake289/klo75'); sys.path.insert(0, '/home/agent/projects/proofs/prove290')
from indmodel import induce
from klo import rref_null
from gstar import module_from_set
P = 32003; rng = np.random.default_rng(5)

def dense(B):
    B, act = module_from_set(B); d = len(B); n = len(B[0]); G = {}
    for i in range(1, n):
        M = np.zeros((d, d), dtype=np.int64)
        for k in range(d):
            if act[i][k] >= 0: M[act[i][k], k] = 1
        G[i] = M
    return G, n, d

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

def hom(GA, GB, dA, dB, n):
    rows = [(np.kron(np.eye(dA, dtype=np.int64), GB[i]) - np.kron(GA[i].T, np.eye(dB, dtype=np.int64))) % P for i in range(1, n)]
    if not rows: return [np.eye(dA*dB, dtype=np.int64)[c].reshape(dB, dA, order='F') for c in range(dA*dB)]
    return [v.reshape(dB, dA, order='F') for v in rref_null(np.vstack(rows), P)]

def summand(GX, dX, GL, dL, n, tries=3):
    F = hom(GX, GL, dX, dL, n); Gs = hom(GL, GX, dL, dX, n)
    if not F or not Gs: return False
    for _ in range(tries):
        f = sum(int(rng.integers(P)) * v for v in F) % P; g = sum(int(rng.integers(P)) * v for v in Gs) % P
        if rank(g @ f % P) == dX: return True
    return False

C1 = lambda k: ({i: np.ones((1, 1), dtype=np.int64) for i in range(1, k)}, 1)

def R(G, n, d):
    out = []
    for k in range(1, n + 1):
        GR = {i: G[i] for i in range(1, n - k)}; GC, _ = C1(k)
        GL, dL = induce(GR, n - k, d, GC, k, 1)
        if summand(G, d, GL, dL, n): out.append(k)
    return out

def L(G, n, d):
    out = []
    for k in range(1, n + 1):
        GR = {i: G[i + k] for i in range(1, n - k)}; GC, _ = C1(k)
        GL, dL = induce(GC, k, 1, GR, n - k, d)
        if summand(G, d, GL, dL, n): out.append(k)
    return out

if __name__ == '__main__':
    mods = pickle.load(open(sys.argv[1], 'rb')); mmax = int(sys.argv[2])
    res = {}
    for m in mods:
        if m > mmax: continue
        for j, x in enumerate(mods[m]):
            G, n, d = dense(x[2]); r = R(G, n, d); l = L(G, n, d)
            res[(m, j)] = (r, l)
            print(m, x[0], x[1], 'd', d, 'proj', x[3], 'R', r, 'L', l, flush=True)
    pickle.dump(res, open(f'rl{mmax}.pkl', 'wb'))
