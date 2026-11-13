"""Independent exact (over Q, python-flint fmpz_mat) check on the FULL tensor space V^{(x)N}
(no reduction to W, no BFS-hom construction).  conv 'I': pi_i idempotent sort-up; conv 'II': Jung-Oh sign T_i^2=-T_i."""
import itertools, sys, math
import numpy as np
from flint import fmpz_mat

def ops(n, N, conv):
    W = list(itertools.product(range(n), repeat=N)); idx = {w: k for k, w in enumerate(W)}; d = len(W); Ts = []
    for i in range(N - 1):
        M = np.zeros((d, d), dtype=np.int64)
        for w in W:
            a, b = w[i], w[i + 1]; s = list(w); s[i], s[i + 1] = b, a; s = idx[tuple(s)]; k = idx[w]
            if conv == 'I':
                if a < b: M[s, k] = 1
                else: M[k, k] = 1
            else:
                if a < b: M[s, k] = 1
                elif a > b: M[k, k] = -1
        Ts.append(M)
    return W, Ts

def null(A):
    A = fmpz_mat([[int(x) for x in r] for r in A])
    X, k = A.nullspace()
    return np.array([[int(X[r, c]) for c in range(k)] for r in range(A.ncols())], dtype=object).reshape(A.ncols(), k)

def rank(A):
    return fmpz_mat([[int(x) for x in r] for r in A]).rank()

def run(n, N, conv):
    W, Ts = ops(n, N, conv)
    # weight blocks
    wts = {}
    for k, w in enumerate(W):
        wts.setdefault(tuple(w.count(j) for j in range(n)), []).append(k)
    blocks = list(wts.values())
    # A = span of all products of T's (closure)
    d = len(W); I = np.eye(d, dtype=np.int64)
    basis = [I]; frontier = [I]
    while frontier:
        new = []
        for X in frontier:
            for T in Ts:
                Y = X @ T
                if rank([b.ravel() for b in basis] + [Y.ravel()]) > len(basis):
                    basis.append(Y); new.append(Y)
        frontier = new
    dimA = len(basis)
    # S blockwise: phi: V_mu -> V_nu with phi T|mu = T|nu phi
    Sb = []  # (mu index, nu index, matrix)
    for i, bm in enumerate(blocks):
        for j, bn in enumerate(blocks):
            dm, dn = len(bm), len(bn)
            rows = []
            for T in Ts:
                Tm = T[np.ix_(bm, bm)]; Tn = T[np.ix_(bn, bn)]
                # vec row-major phi (dn x dm): phi Tm - Tn phi
                E = np.kron(np.eye(dn, dtype=np.int64), Tm.T) - np.kron(Tn, np.eye(dm, dtype=np.int64))
                rows += E.tolist()
            K = null(rows)
            for c in range(K.shape[1]):
                Sb.append((i, j, np.array(K[:, c], dtype=object).reshape(dn, dm)))
    dimS = len(Sb)
    # B: unknown b_i (d_i x d_i) per block; b_j phi - phi b_i = 0 for phi: i->j
    off = []; tot = 0
    for bm in blocks:
        off.append(tot); tot += len(bm) ** 2
    rows = []
    for (i, j, phi) in Sb:
        di, dj = len(blocks[i]), len(blocks[j])
        Ej = np.kron(np.eye(dj, dtype=object), phi.T)      # vec(b_j phi)
        Ei = np.kron(phi, np.eye(di, dtype=object))         # vec(phi b_i)
        E = np.zeros((dj * di, tot), dtype=object)
        E[:, off[j]:off[j] + dj * dj] += Ej
        E[:, off[i]:off[i] + di * di] -= Ei
        rows += E.tolist()
    dimB = null(rows).shape[1] if rows else tot
    print(dict(n=n, N=N, conv=conv, dimA=dimA, dimS=dimS, schur=math.comb(n*n+N-1, N), dimB=dimB), flush=True)

if __name__ == '__main__':
    for arg in sys.argv[1:]:
        n, N, conv = arg.split(',')
        run(int(n), int(N), conv)
