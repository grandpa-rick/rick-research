"""Finite Coxeter group, KL polynomials, mu, left cells, left-cell modules at v=1.
Computed (numerical + exact integer KL), not proved."""
import numpy as np
from collections import deque

def coxeter_group(M):
    n = len(M)
    B = np.array([[-np.cos(np.pi / M[i][j]) if i != j else 1.0 for j in range(n)] for i in range(n)])
    # simple reflection matrices on V with basis alpha_i: s_i(a_j) = a_j - 2B(i,j) a_i
    S = []
    for i in range(n):
        m = np.eye(n)
        for j in range(n):
            m[i, j] -= 2 * B[i, j]
        S.append(m)
    p = np.linalg.solve(B, np.ones(n))  # B(alpha_i,p)=1>0, generic
    key = lambda v: tuple(np.round(v, 6) + 0.0)
    mats = [np.eye(n)]
    idx = {key(p): 0}
    word = [()]
    length = [0]
    q = deque([0])
    while q:
        w = q.popleft()
        for s in range(n):
            m = S[s] @ mats[w]
            k = key(m @ p)
            if k not in idx:
                idx[k] = len(mats)
                mats.append(m)
                word.append((s,) + word[w])
                length.append(length[w] + 1)
                q.append(idx[k])
    N = len(mats)
    lm = np.zeros((n, N), int)
    rm = np.zeros((n, N), int)
    for w in range(N):
        for s in range(n):
            lm[s, w] = idx[key(S[s] @ mats[w] @ p)]
            rm[s, w] = idx[key(mats[w] @ S[s] @ p)]
    return dict(n=n, N=N, mats=mats, word=word, length=np.array(length), lm=lm, rm=rm)


def kl(G):
    """P[x][w] as integer coefficient arrays in q; mu matrix."""
    N, n, L, lm = G['N'], G['n'], G['length'], G['lm']
    order = np.argsort(L, kind='stable')
    maxdeg = max(L) // 2 + 2
    P = np.zeros((N, N, maxdeg + 1), dtype=np.int64)  # P[x,w,:]
    mu = np.zeros((N, N), dtype=np.int64)
    P[0, 0, 0] = 1
    def ldesc(w, s):
        return L[lm[s, w]] < L[w]
    done = [0]
    for w in order[1:]:
        s = next(s for s in range(n) if ldesc(w, s))
        v = lm[s, w]
        col = np.zeros((N, maxdeg + 1), dtype=np.int64)
        for x in range(N):
            c = 1 if ldesc(x, s) else 0
            sx = lm[s, x]
            # q^{1-c} P_{sx,v} + q^c P_{x,v}
            a = P[sx, v]
            b = P[x, v]
            if c == 0:
                col[x, 1:] += a[:-1]
                col[x] += b
            else:
                col[x] += a
                col[x, 1:] += b[:-1]
        for z in done:
            if mu[z, v] != 0 and ldesc(z, s):
                sh = (L[w] - L[z]) // 2
                col[:, sh:] -= mu[z, v] * P[:, z, :maxdeg + 1 - sh]
        P[:, w, :] = col
        for x in range(N):
            d = L[w] - L[x]
            if d > 0 and d % 2 == 1 and col[x].any():
                mu[x, w] = col[x, (d - 1) // 2]
        done.append(w)
    assert (P >= 0).all()
    musym = mu + mu.T
    return P, musym


def left_descents(G, w):
    return frozenset(s for s in range(G['n']) if G['length'][G['lm'][s, w]] < G['length'][w])


def left_cells(G, mu):
    N, n = G['N'], G['n']
    D = [left_descents(G, w) for w in range(N)]
    # edge w -> z (z <=_L w) if mu(z,w)!=0 and D(z) not subset of D(w)
    adj = [[] for _ in range(N)]
    for w in range(N):
        for z in range(N):
            if mu[z, w] != 0 and not D[z] <= D[w]:
                adj[w].append(z)
    # reachability closure via BFS
    reach = np.zeros((N, N), bool)
    for w in range(N):
        seen = {w}; dq = [w]
        while dq:
            u = dq.pop()
            for z in adj[u]:
                if z not in seen:
                    seen.add(z); dq.append(z)
        reach[w, list(seen)] = True
    cells, assigned = [], set()
    for w in range(N):
        if w in assigned: continue
        c = sorted(z for z in range(N) if reach[w, z] and reach[z, w])
        cells.append(c); assigned |= set(c)
    return cells, D


def cell_module(G, mu, D, cell, conv='Cp'):
    """Matrices A_s of (1+s) in KL basis {c_w: w in cell}; column w = image of c_w."""
    d = len(cell); pos = {w: i for i, w in enumerate(cell)}
    A = []
    for s in range(G['n']):
        m = np.zeros((d, d))
        for w in cell:
            j = pos[w]
            if conv == 'C':  # GW / W-graph sign convention: s e_x = -e_x on descents
                if s not in D[w]:
                    m[j, j] = 2
                    for z in cell:
                        if s in D[z] and mu[z, w] != 0:
                            m[pos[z], j] += mu[z, w]
                continue
            if s in D[w]:
                m[j, j] = 2
            else:
                for z in cell:
                    if s in D[z] and mu[z, w] != 0:
                        m[pos[z], j] += mu[z, w]
        A.append(m)
    return A


def rho_all(G, A):
    """rho(w) for all w using reduced words; rho(s)=A_s - I."""
    I = np.eye(A[0].shape[0])
    R = [None] * G['N']
    R[0] = I
    for w in np.argsort(G['length'], kind='stable')[1:]:
        s = G['word'][w][0]
        R[w] = (A[s] - I) @ R[G['lm'][s, w]]
    return R
