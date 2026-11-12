# Independent model: iterated induction product X_1 [x] X_2 [x] ... of connected-component modules.
# Ind_{H_a x H_b}^{H_{a+b}}(A (x) B): basis T_w (x) e_x (x) f_y, w minimal left coset rep (increasing on [1,a],[a+1,a+b]).
# pi_i T_w = T_w if s_i w < w; = T_w pi_p if s_i w = w s_p (p in [1,a-1] -> A, p in [a+1,a+b-1] -> B as pi_{p-a}); else T_{s_i w}.
import itertools, numpy as np
from klo import *

def dense(act, d):
    G = {}
    for i, a in act.items():
        M = np.zeros((d, d), dtype=np.int64)
        for k in range(d):
            if a[k] >= 0: M[a[k], k] = 1
        G[i] = M
    return G

def induce(GA, a, dA, GB, b, dB):
    N = a + b
    reps = [w for w in itertools.permutations(range(1, N + 1))
            if all(w[j] < w[j + 1] for j in range(a - 1)) and all(w[j] < w[j + 1] for j in range(a, N - 1))]
    ridx = {w: k for k, w in enumerate(reps)}
    D = len(reps) * dA * dB
    IA, IB = np.eye(dA, dtype=np.int64), np.eye(dB, dtype=np.int64)
    G = {}
    for i in range(1, N):
        M = np.zeros((D, D), dtype=np.int64)
        for w, k in ridx.items():
            pos = {v: p for p, v in enumerate(w, 1)}
            x, y = pos[i], pos[i + 1]
            blk = slice(k * dA * dB, (k + 1) * dA * dB)
            if x > y:
                M[blk, blk] = np.eye(dA * dB, dtype=np.int64)
            elif y == x + 1 and x != a:
                op = np.kron(GA[x], IB) if x < a else np.kron(IA, GB[x - a])
                M[blk, blk] = op
            else:
                u = tuple(i + 1 if v == i else i if v == i + 1 else v for v in w)
                k2 = ridx[u]
                M[k2 * dA * dB:(k2 + 1) * dA * dB, blk] = np.eye(dA * dB, dtype=np.int64)
        G[i] = M
    return G, D

def ind_product(comps):
    G, n, d = None, 0, 1
    for c in comps:
        cells = cells_of(c); B, act, s = build_module(cells); m = len(cells)
        Gc = dense(act, len(B))
        if G is None: G, n, d = Gc, m, len(B)
        else: G, d = induce(G, n, d, Gc, m, len(B)); n += m
    return G, n, d

def char_dense(G, n, d):
    # composition factors via traces of pi_{w0(S)} + Mobius (as in wake288 ind.py)
    from itertools import combinations
    def w0word(S):
        w = []; S = sorted(S); runs = []
        for s_ in S:
            if runs and s_ == runs[-1][-1] + 1: runs[-1].append(s_)
            else: runs.append([s_])
        for r in runs:
            a, b = r[0], r[-1] + 1
            for top_ in range(b - 1, a - 1, -1): w += list(range(a, top_ + 1))
        return w
    tr = {}
    for r in range(n):
        for S in combinations(range(1, n), r):
            Pm = np.eye(d, dtype=np.int64)
            for i in w0word(S): Pm = G[i] @ Pm
            tr[S] = int(np.trace(Pm))
    ch = {}
    for K in tr:
        m = sum((-1) ** (len(S) - len(K)) * tr[S] for S in tr if set(K) <= set(S))
        if m: ch[comp_of(set(range(1, n)) - set(K), n)] = m
    return ch

def hom_space(GA, GB, dA, dB, p):
    # F: A -> B with F GA_i = GB_i F ; vec column-major
    rows = [ (np.kron(np.eye(dA, dtype=np.int64), GB[i]) - np.kron(GA[i].T, np.eye(dB, dtype=np.int64))) % p for i in GA]
    N = rref_null(np.vstack(rows), p)
    return [v.reshape(dB, dA, order='F') for v in N]

def is_iso(GA, GB, d, p=32003, seed=0):
    H = hom_space(GA, GB, d, d, p)
    if not H: return False
    rng = np.random.default_rng(seed)
    F = sum(int(rng.integers(p)) * h for h in H) % p
    # rank mod p
    return len(rref_null(F, p)) == 0
