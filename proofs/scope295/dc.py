"""Double centraliser census for the 0-Hecke action on V^{(x)N}, dim V = n.
Convention (I) (verified): v_k.pi_i = v_{k s_i} if k_i<k_{i+1}; v_k otherwise (k_i>=k_{i+1}).  pi_i^2=pi_i, braid, far-commute.
Reduction: V_mu (weight space) depends up to H-iso only on alpha = mu with zeros deleted, V_mu ~= M_alpha;
A, B are insensitive to multiplicities, so we work on W = (+)_{alpha |= N, l(alpha)<=n} M_alpha.
dim S is recovered with multiplicities C(n,l(alpha)).  All linear algebra mod P (python-flint nmod_mat).
"""
import itertools, sys, time, math
import numpy as np
from flint import nmod_mat

P = 1000003

def comps(N, maxp):
    out = []
    def rec(rem, cur):
        if rem == 0:
            out.append(tuple(cur)); return
        if len(cur) == maxp: return
        for a in range(1, rem + 1):
            rec(rem - a, cur + [a])
    rec(N, []); return out

def module(alpha):
    N = sum(alpha)
    u = tuple(j for j, a in enumerate(alpha) for _ in range(a))
    W = sorted(set(itertools.permutations(u)))
    idx = {w: k for k, w in enumerate(W)}
    ops = []  # ops[i][k] = image index, or -1 for zero
    for i in range(N - 1):
        f = np.empty(len(W), dtype=np.int64)
        for k, w in enumerate(W):
            a, b = w[i], w[i + 1]
            if a < b:
                x = list(w); x[i], x[i + 1] = b, a; f[k] = idx[tuple(x)]
            elif a == b: f[k] = k
            else: f[k] = k   # convention (I): a>b fixed
        ops.append(f)
    return W, idx, u, ops

def opmat(f):
    d = len(f); M = np.zeros((d, d), dtype=np.int64)
    for k in range(d):
        if f[k] >= 0: M[f[k], k] = 1
    return M

def mm(A, B):
    """exact (A@B) mod P via float64 BLAS; exact while inner*(P-1)^2 < 2^53."""
    assert A.shape[-1] * (P - 1) ** 2 < 2 ** 53
    C = np.matmul(np.asarray(A, dtype=np.float64), np.asarray(B, dtype=np.float64))
    return np.rint(C).astype(np.int64) % P

def tomat(A):
    A = np.asarray(A) % P
    return nmod_mat(A.shape[0], A.shape[1], [int(x) for x in A.ravel()], P)

def nullspace(A):
    """columns basis of right nullspace of numpy matrix A mod P (returns ncols x k)."""
    if A.shape[0] == 0: return np.eye(A.shape[1], dtype=np.int64)
    return _null(tomat(A), A.shape[1])

def _null(M, nc):
    X, k = M.nullspace()
    return np.array(X.entries(), dtype=np.int64).reshape(nc, nc)[:, :k].copy()

def null_sparse_comm(phi):
    """nullspace of X -> X phi - phi X (row-major vec), built sparsely."""
    dd = phi.shape[0]; M = nmod_mat(dd * dd, dd * dd, P)
    nz = np.argwhere(phi % P)
    acc = {}
    for (k, c) in nz:   # (X phi)_{rc} += X_{rk} phi_{kc}
        v = int(phi[k, c])
        for r in range(dd):
            key = (r * dd + c, r * dd + k); acc[key] = (acc.get(key, 0) + v) % P
    for (r, k) in nz:   # (phi X)_{rc} = sum_k phi_{rk} X_{kc}
        v = int(phi[r, k])
        for c in range(dd):
            key = (r * dd + c, k * dd + c); acc[key] = (acc.get(key, 0) - v) % P
    for (i, j), v in acc.items():
        if v: M[i, j] = v
    return _null(M, dd * dd)

def rank(A):
    if A.shape[0] == 0 or A.shape[1] == 0: return 0
    return tomat(A).rank()

def homs(Ma, Mb, alpha):
    """basis of Hom_H(M_alpha, M_beta) as d_b x d_a matrices (column convention)."""
    Wa, ia, ua, opa = Ma; Wb, ib, ub, opb = Mb
    db = len(Wb)
    J = []; pos = 0
    for a in alpha:
        J += list(range(pos, pos + a - 1)); pos += a
    rows = []
    for i in J:
        Mi = opmat(opb[i]) - np.eye(db, dtype=np.int64)
        rows.append(Mi)
    K = nullspace(np.vstack(rows)) if rows else np.eye(db, dtype=np.int64)
    # BFS from ua in M_alpha
    da = len(Wa); start = ia[ua]
    par = {start: None}; order = [start]; q = [start]
    while q:
        nq = []
        for k in q:
            for i, f in enumerate(opa):
                t = int(f[k])
                if t >= 0 and t not in par:
                    par[t] = (k, i); order.append(t); nq.append(t)
        q = nq
    assert len(order) == da
    Pb = [opmat(f) for f in opb]
    res = []
    for c in range(K.shape[1]):
        phi = np.zeros((db, da), dtype=np.int64)
        phi[:, start] = K[:, c]
        for t in order[1:]:
            k, i = par[t]
            phi[:, t] = Pb[i] @ phi[:, k] % P
        res.append(phi)
    # sanity: intertwiner
    Pa = [opmat(f) for f in opa]
    for phi in res:
        for i in range(len(Pa)):
            assert not ((phi @ Pa[i] - Pb[i] @ phi) % P).any()
    return res

def comm_eqs(phi, dX, dY):
    """phi: dY x dX. returns (EY, EX) with  vec(Y phi - phi X) = EY vec(Y) + EX vec(X), row-major vec."""
    # (Y phi)_{rc} = sum_k Y_{rk} phi_{kc} -> kron(I_dY, phi^T)
    EY = np.kron(np.eye(dY, dtype=np.int64), phi.T)
    EX = -np.kron(phi, np.eye(dX, dtype=np.int64))
    return EY % P, EX % P

def run(n, N, verbose=True):
    t0 = time.time()
    al = comps(N, n)
    Ms = {a: module(a) for a in al}
    d = {a: len(Ms[a][0]) for a in al}
    H = {}
    for a in al:
        for b in al:
            H[(a, b)] = homs(Ms[a], Ms[b], a)
    # dim S with multiplicities
    dimS = sum(math.comb(n, len(a)) * math.comb(n, len(b)) * len(H[(a, b)]) for a in al for b in al)
    print('homs done', time.time()-t0, flush=True)
    # commutant per block (batched: basis matrices X, images X phi - phi X)
    def bas(Kc, dd):  # columns (row-major vec) -> stack (k, dd, dd)
        return Kc.T.reshape(Kc.shape[1], dd, dd)
    K = {}
    for a in al:
        da = d[a]; Ka = None
        rng = np.random.default_rng(1)
        Hs = H[(a, a)]
        if len(Hs) > 1:
            phi0 = sum(int(rng.integers(1, P)) * f for f in Hs) % P
            Ka = null_sparse_comm(phi0)
        for phi in Hs:
            if Ka is None: Ka = np.eye(da * da, dtype=np.int64)
            X = bas(Ka, da)
            E = ((X @ phi - phi @ X) % P).reshape(X.shape[0], -1).T
            if not E.any(): continue
            Ka = mm(Ka, nullspace(E))
        if Ka is None: Ka = np.eye(da * da, dtype=np.int64)
        K[a] = Ka
    print('self-comm done', time.time()-t0, {a:K[a].shape[1] for a in al}, flush=True)
    off = {}; tot = 0
    for a in al:
        off[a] = tot; tot += K[a].shape[1]
    Xs = {a: bas(K[a], d[a]) for a in al}
    G = np.eye(tot, dtype=np.int64)
    for a in al:
        for b in al:
            if a == b: continue
            for phi in H[(a, b)]:
                # b_b phi - phi b_a  ;  phi: d_b x d_a
                Eb = ((Xs[b] @ phi) % P).reshape(K[b].shape[1], -1).T
                Ea = ((-(phi @ Xs[a])) % P).reshape(K[a].shape[1], -1).T
                E = (mm(Eb, G[off[b]:off[b] + K[b].shape[1], :]) + mm(Ea, G[off[a]:off[a] + K[a].shape[1], :])) % P
                if not E.any(): continue
                G = mm(G, nullspace(E))
    print('B done', time.time()-t0, G.shape, flush=True)
    dimB = G.shape[1]
    # A: all pi_w as partial maps on W, via BFS over S_N
    blocks = al
    sizes = [d[a] for a in al]
    ident = tuple(range(N))
    def compose(fw, i):  # pi_w pi_i : apply pi_w then pi_i (right action) -> on each block
        out = []
        for a, f in zip(al, fw):
            g = Ms[a][3][i]
            h = np.where(f >= 0, g[np.maximum(f, 0)], -1)
            out.append(h)
        return out
    idf = [np.arange(d[a], dtype=np.int64) for a in al]
    elems = {ident: idf}; frontier = [ident]
    while frontier:
        nf = []
        for w in frontier:
            for i in range(N - 1):
                if w[i] < w[i + 1]:  # length goes up when right-multiplying by s_i on positions
                    w2 = list(w); w2[i], w2[i + 1] = w2[i + 1], w2[i]; w2 = tuple(w2)
                    if w2 not in elems:
                        elems[w2] = compose(elems[w], i); nf.append(w2)
        frontier = nf
    assert len(elems) == math.factorial(N)
    L = sum(s * s for s in sizes)
    Amat = np.zeros((len(elems), L), dtype=np.int64)
    for r, fw in enumerate(elems.values()):
        o = 0
        for f, s in zip(fw, sizes):
            for k in range(s):
                if f[k] >= 0: Amat[r, o + f[k] * s + k] = 1  # row-major vec of matrix M[f[k],k]
            o += s * s
    rng = np.random.default_rng(7)
    R = rng.integers(0, P, size=(L, len(elems) + 50)).astype(np.float64)
    assert L * P < 2 ** 53
    AR = np.rint(Amat.astype(np.float64) @ R).astype(np.int64) % P   # Amat is 0/1: exact
    dimA = rank(AR)   # rank(A R) = rank(A) w.h.p.; never exceeds it
    # A subset B check: B basis in the global vec coordinates
    Bvec = np.zeros((L, dimB), dtype=np.int64); o = 0
    for a, s in zip(al, sizes):
        Bvec[o:o + s * s, :] = K[a] @ G[off[a]:off[a] + K[a].shape[1], :] % P
        o += s * s
    BR = np.vstack([mm(Bvec.T[i:i+1], R) for i in range(Bvec.shape[1])]) if L * (P-1)**2 >= 2**53 else mm(Bvec.T, R)
    rAB = rank(np.vstack([AR, BR]))  # projected; == dimB certifies A in B only modulo projection (w.h.p.)
    res = dict(n=n, N=N, dimA=dimA, dimS=dimS, schur=math.comb(n * n + N - 1, N), dimB=dimB,
               AinB=(rAB == dimB), ann=math.factorial(N) - dimA, t=time.time() - t0,
               ncomp=len(al), dimW=sum(sizes))
    global LAST; LAST = dict(Amat=Amat, Bvec=Bvec, sizes=sizes, al=al)
    if verbose: print(res, flush=True)
    return res

if __name__ == '__main__':
    for arg in sys.argv[1:]:
        n, N = map(int, arg.split(','))
        run(n, N)
