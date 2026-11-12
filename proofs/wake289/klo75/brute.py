# Independent check: End as full commutant {X : A_i X = X A_i} by dense linear algebra over Q (sympy-free: flint fmpq_mat).
import numpy as np, flint
from shapes import *
def mats(lam, mu):
    B, acts = action(lam, mu); m = len(B); A = {}
    for i, f in acts.items():
        M = np.zeros((m, m), dtype=np.int64)
        for t, s in enumerate(f):
            if s >= 0: M[s, t] = 1
        A[i] = M
    return A, m
def brute(lam, mu):
    A, m = mats(lam, mu)
    rows = []
    I = np.eye(m, dtype=np.int64)
    for M in A.values():  # vec(AX - XA) = (I kron A - A^T kron I) vec X (column-major)
        rows.append(np.kron(I, M) - np.kron(M.T, I))
    K = np.vstack(rows) if rows else np.zeros((1, m*m), dtype=np.int64)
    Q = flint.fmpq_mat(K.shape[0], K.shape[1], [int(x) for x in K.flatten()])
    d = m*m - Q.rank()
    # basis of End over Q
    R, rk = Q.rref()
    piv = []
    for a in range(rk):
        for b in range(m*m):
            if R[a, b] != 0: piv.append(b); break
    free = [b for b in range(m*m) if b not in set(piv)]
    basis = []
    for fc in free:
        v = [flint.fmpq(0)]*(m*m); v[fc] = flint.fmpq(1)
        for a, pc in enumerate(piv): v[pc] = -R[a, fc]
        basis.append(flint.fmpq_mat(m, m, [v[c*m + r] for r in range(m) for c in range(m)]))  # column-major unvec
    # trace form rank over Q: express products; use regular trace via left mult on End (coords by least squares through rref)
    Bm = flint.fmpq_mat(len(basis), m*m, [x for b in basis for x in [b[r, c] for c in range(m) for r in range(m)]])
    def coords(X):
        vec = [X[r, c] for c in range(m) for r in range(m)]
        return [vec[fc] for fc in free]   # free coordinates determine element
    dd = len(basis)
    C = [[coords(basis[a]*basis[b]) for b in range(dd)] for a in range(dd)]
    trL = [sum(C[c][b][b] for b in range(dd)) for c in range(dd)]
    G = flint.fmpq_mat(dd, dd, [sum(C[a][b][c]*trL[c] for c in range(dd)) for a in range(dd) for b in range(dd)])
    return m, dd, G.rank()
