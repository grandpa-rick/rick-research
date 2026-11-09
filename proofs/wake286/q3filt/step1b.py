import json, time, numpy as np
from core import *
from span_modp import algebra_span_modp
from flint import fmpz_mat, nmod_mat
from math import comb
def classes_by(W, key):
    cl = {}
    for k, w in enumerate(W): cl.setdefault(key(w), []).append(k)
    return list(cl.values())
def np_of(M): return np.array([[int(M[r,c]) for c in range(M.ncols())] for r in range(M.nrows())], dtype=np.int64)

def commutant_dim(gens, classes, d, cross, exact=True):
    """X with X[b,a]=0 unless (a,b) allowed: cross=True: any pair of classes (gens preserve classes) solved blockwise;
    cross=False: X block-diag over classes, gens arbitrary, solved globally."""
    if cross:
        tot = 0
        for a in classes:
            for b in classes:
                na, nb = len(a), len(b); rows = []
                for g in gens:
                    ga = g[np.ix_(a, a)]; gb = g[np.ix_(b, b)]
                    for r in range(nb):
                        for c in range(na):
                            row = np.zeros(na*nb, dtype=np.int64)
                            row[np.arange(nb)*na + c] += gb[r, :]
                            row[r*na + np.arange(na)] -= ga[:, c]
                            if row.any(): rows.append([int(x) for x in row])
                tot += na*nb - (fmpz_mat(rows).rank() if rows else 0)
        return tot
    off = {}; nv = 0; pos = {}
    for ci, c in enumerate(classes):
        off[ci] = nv
        for r, w in enumerate(c): pos[w] = (ci, r)
        nv += len(c)**2
    def var(i, j):  # X[i,j], i,j same class
        ci, r = pos[i]; cj, s = pos[j]
        if ci != cj: return None
        return off[ci] + r*len(classes[ci]) + s
    rows = []
    for g in gens:
        nzr = [np.nonzero(g[r, :])[0] for r in range(d)]; nzc = [np.nonzero(g[:, c])[0] for c in range(d)]
        for i in range(d):
            for j in range(d):
                row = {}
                for k in nzr[i]:   # (gX)[i,j] = g[i,k] X[k,j]
                    v = var(k, j)
                    if v is not None: row[v] = row.get(v, 0) + int(g[i, k])
                for k in nzc[j]:   # (Xg)[i,j] = X[i,k] g[k,j]
                    v = var(i, k)
                    if v is not None: row[v] = row.get(v, 0) - int(g[k, j])
                row = {k: v for k, v in row.items() if v}
                if row:
                    rr = [0]*nv
                    for k, v in row.items(): rr[k] = v
                    rows.append(rr)
    if exact: rk = fmpz_mat(rows).rank()
    else: rk = nmod_mat(rows, 2147483629).rank()
    return nv - rk

out = {}
for (n, N) in [(2,2),(2,3),(3,3),(2,4),(3,4)]:
    t0 = time.time(); W, idx, d = setup(n, N)
    Ts = [np_of(T) for T in T_ops(n, N)]; U = {k: np_of(v) for k, v in U0_ops(n, N).items()}
    AH = algebra_span_modp(Ts, d); AU = algebra_span_modp(list(U.values()), d)
    # certify independence over Q
    rkH = fmpz_mat([[int(x) for x in M.ravel()] for M in AH]).rank()
    rkU = fmpz_mat([[int(x) for x in M.ravel()] for M in AU]).rank()
    wcl = classes_by(W, lambda w: tuple(w.count(i) for i in range(n)))
    scl = classes_by(W, lambda w: frozenset(w))
    dimS = commutant_dim(Ts, wcl, d, cross=True)
    dUc = commutant_dim([U[k] for k in U if k[0] != 'k'], scl, d, cross=False, exact=(d < 81))
    res = dict(n=n, N=N, dimH_image=len(AH), H_indepQ=(rkH == len(AH)), dimS0=dimS, classical=comb(n*n+N-1, N),
               dimU0_image=len(AU), U0_indepQ=(rkU == len(AU)), dim_commutant_U0=dUc, commU0_exact=(d < 81), t=round(time.time()-t0, 1))
    print(res, flush=True); out[f"{n},{N}"] = res
json.dump(out, open('step1b.json', 'w'), indent=1)
