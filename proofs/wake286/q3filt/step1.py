import sys, itertools, json, time
from core import *
from flint import fmpz_mat
from math import comb

def classes_by(W, key):
    cl = {}
    for k, w in enumerate(W): cl.setdefault(key(w), []).append(k)
    return list(cl.values())

def commutant_blocks(gens, classes, d):
    """dim of {X : X g = g X} given X is known block-diagonal-compatible: X maps class a -> class b arbitrary,
    and gens preserve classes. Returns basis as dict blocks (a,b)->list of matrices."""
    basis = []
    for a in classes:
        for b in classes:
            # unknown X: |b| x |a| ; equation g_b X = X g_a for each gen
            na, nb = len(a), len(b); nv = na*nb
            rows = []
            for g in gens:
                ga = [[int(g[r, c]) for c in a] for r in a]; gb = [[int(g[r, c]) for c in b] for r in b]
                for r in range(nb):
                    for c in range(na):
                        row = [0]*nv
                        # (g_b X)[r,c] = sum_k gb[r][k] X[k,c]
                        for k in range(nb):
                            if gb[r][k]: row[k*na + c] += gb[r][k]
                        # (X g_a)[r,c] = sum_k X[r,k] ga[k][c]
                        for k in range(na):
                            if ga[k][c]: row[r*na + k] -= ga[k][c]
                        if any(row): rows.append(row)
            for v in nullspace_int(rows, nv):
                basis.append((a, b, v))
    return basis

def to_full(item, d):
    a, b, v = item; na = len(a)
    M = [[0]*d for _ in range(d)]
    for r, br in enumerate(b):
        for c, ac in enumerate(a):
            if v[r*na+c]: M[br][ac] = v[r*na+c]
    return fmpz_mat(M)

out = {}
for (n, N) in [(2,2),(2,3),(3,3),(2,4),(3,4)]:
    t0 = time.time()
    W, idx, d = setup(n, N)
    Ts = T_ops(n, N)
    I = fmpz_mat([[int(r==c) for c in range(d)] for r in range(d)])
    ok_quad = all(T*T == -T for T in Ts)
    ok_braid = all(Ts[i]*Ts[i+1]*Ts[i] == Ts[i+1]*Ts[i]*Ts[i+1] for i in range(N-2))
    ok_comm = all(Ts[i]*Ts[j] == Ts[j]*Ts[i] for i in range(N-1) for j in range(i+2, N-1))
    U = U0_ops(n, N); Ug = list(U.values())
    ok_UT = all(u*T == T*u for u in Ug for T in Ts)
    AH = algebra_span(Ts, d); AU = algebra_span(Ug, d)
    wt = lambda w: tuple(w.count(i) for i in range(n))
    wcl = classes_by(W, wt)
    S = commutant_blocks(Ts, wcl, d)
    # commutant of U0 image: U0 image contains products of k_i -> projections by support set; block by support
    scl = classes_by(W, lambda w: frozenset(w))
    Uc = commutant_blocks(Ug, scl, d)
    # End_S(V): S contains weight projections -> block diagonal in weights
    Sfull = [to_full(s, d) for s in S]
    # equations: Y block-diag (weight) commuting with all of Sfull
    blocks = wcl; off = {}; nv = 0
    for bi, b in enumerate(blocks):
        off[bi] = nv; nv += len(b)**2
    pos = {}
    for bi, b in enumerate(blocks):
        for r, br in enumerate(b): pos[br] = (bi, r)
    rows = []
    for s in S:
        a, b, v = s; na = len(a)
        # s maps a->b with matrix X (|b|x|a|). Need Y_b X = X Y_a
        ba = pos[a[0]][0]; bb = pos[b[0]][0]; nb = len(b)
        X = [[v[r*na+c] for c in range(na)] for r in range(nb)]
        for r in range(nb):
            for c in range(na):
                row = [0]*nv
                for k in range(nb):
                    if X[k][c]: row[off[bb] + r*nb + k] += X[k][c]
                for k in range(na):
                    if X[r][k]: row[off[ba] + k*na + c] -= X[r][k]
                if any(row): rows.append(row)
    dES = len(nullspace_int(rows, nv))
    res = dict(n=n, N=N, d=d, quad=ok_quad, braid=ok_braid, farcomm=ok_comm, U0_commutes_H=ok_UT,
               dimH_image=len(AH), dimS=len(S), schur_classical=comb(n*n+N-1, N), dimEnd_S=dES,
               double_centralizer=(dES == len(AH)), dimU0_image=len(AU), dim_commutant_U0=len(Uc),
               time=round(time.time()-t0,1))
    print(res, flush=True); out[f"{n},{N}"] = res
json.dump(out, open('step1.json','w'), indent=1)
