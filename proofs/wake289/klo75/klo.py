# KLO 2310.20571 modules M_P for P in RSP_n, realised as M_{poset(tau_0)} for a basic skew shape lambda/mu
# (Thm 5.5: M_P depends only on sh(tau_P); Thm 3.9 / Lemma 3.2: Sigma_L(P) = read_tau(SYT(lambda/mu))).
# Basis gamma = read_{tau0}(T), T in SYT; gamma in one-line notation gamma(k) = T(box with tau0-label k).
# Action (2.3): pi_i gamma = gamma if i in Des_L(gamma) (i+1 left of i in one-line);
#               = s_i gamma (swap VALUES i,i+1) if that is in the basis; else 0.
import itertools, random, numpy as np, sympy as sp

# ---------------- shapes ----------------
def connected_shapes(m):
    """basic connected skew shapes with m cells, as tuple of rows (l,r) column intervals, normalised min col 0."""
    out = set()
    def rec(rows, left):
        if left == 0:
            mn = min(l for l, r in rows)
            out.add(tuple((l - mn, r - mn) for l, r in rows)); return
        l, r = rows[-1]
        for r2 in range(l, r + 1):          # r2 >= l (overlap), r2 <= r
            for l2 in range(r2 - left + 1, l + 1):  # l2 <= l, length r2-l2+1 <= left
                rec(rows + [(l2, r2)], left - (r2 - l2 + 1))
    for a in range(1, m + 1):
        rec([(0, a - 1)], m - a)
    return sorted(out)

def cells_of(rows, r0=0, c0=0):
    return [(r0 + i, c0 + c) for i, (l, r) in enumerate(rows) for c in range(l, r + 1)]

def is_ribbon(rows):
    S = set(cells_of(rows))
    return not any((i, j) in S and (i + 1, j) in S and (i, j + 1) in S and (i + 1, j + 1) in S for (i, j) in S)

def star(comps):
    """lambda/mu = comps[0] * comps[1] * ... (comps[0] top-right). Returns sorted cell list."""
    # place bottom-left first: last component at rows bottom, cols left
    cells = []; r0 = 0
    widths = [max(r for l, r in c) + 1 for c in comps]
    total_w = sum(widths)
    c0 = total_w
    for c, w in zip(comps, widths):
        c0 -= w
        cells += cells_of(c, r0, c0)
        r0 += len(c)
    return sorted(cells)

def lam_mu(cells):
    rows = {}
    for i, j in cells: rows.setdefault(i, []).append(j)
    lam = [max(v) + 1 for i, v in sorted(rows.items())]
    mu = [min(v) for i, v in sorted(rows.items())]
    return tuple(lam), tuple(x for x in mu if x > 0)

def compositions(n):
    for k in range(1, n + 1):
        for cuts in itertools.combinations(range(1, n), k - 1):
            b = (0,) + cuts + (n,)
            yield tuple(b[i + 1] - b[i] for i in range(k))

def all_shapes(n, CS):
    """yield list of connected components (each a rows-tuple) for every basic skew shape of size n."""
    for comp in compositions(n):
        for cs in itertools.product(*[CS[m] for m in comp]):
            yield list(cs)

# ---------------- module ----------------
def syt(cells):
    cells = list(cells); S = set(cells); n = len(cells)
    res = []; T = {}
    def rec(k):
        if k > n: res.append(dict(T)); return
        for (i, j) in cells:
            if (i, j) in T: continue
            if (i - 1, j) in S and (i - 1, j) not in T: continue
            if (i, j - 1) in S and (i, j - 1) not in T: continue
            T[(i, j)] = k; rec(k + 1); del T[(i, j)]
    rec(1); return res

def tau0(cells):
    order = sorted(cells, key=lambda c: (c[0], -c[1]))  # top row first, right to left
    return order  # order[k-1] = box with label k

def build_module(cells):
    n = len(cells); boxes = tau0(cells)
    basis = [tuple(T[b] for b in boxes) for T in syt(cells)]
    idx = {g: k for k, g in enumerate(basis)}
    d = len(basis); act = {}
    for i in range(1, n):
        a = np.empty(d, dtype=np.int64)
        for k, g in enumerate(basis):
            pi_, pj = g.index(i), g.index(i + 1)
            if pj < pi_: a[k] = k
            else:
                h = tuple(i + 1 if v == i else i if v == i + 1 else v for v in g)
                a[k] = idx.get(h, -1)
        act[i] = a
    # sigma = read_tau0(T_{lambda/mu}) (row reading)
    Trow = {c: k + 1 for k, c in enumerate(sorted(cells))}
    sigma = tuple(Trow[b] for b in boxes)
    return basis, act, idx[sigma]

def check_relations(act, n):
    def comp(*fs):  # apply right-to-left
        d = len(fs[0]); x = np.arange(d)
        for f in reversed(fs):
            y = np.where(x >= 0, f[np.maximum(x, 0)], -1); x = y
        return x
    for i in range(1, n):
        assert (comp(act[i], act[i]) == act[i]).all()
        if i + 1 < n: assert (comp(act[i], act[i+1], act[i]) == comp(act[i+1], act[i], act[i+1])).all()
        for j in range(i + 2, n): assert (comp(act[i], act[j]) == comp(act[j], act[i])).all()

def desL(g):
    return frozenset(i for i in range(1, len(g)) if g.index(i + 1) < g.index(i))

def apply(a, v, p):
    w = np.zeros_like(v); m = a >= 0
    np.add.at(w, a[m], v[m]); return w % p

def apply_cols(a, M, p):  # pi_i @ M (rows)
    W = np.zeros_like(M); m = a >= 0
    np.add.at(W, a[m], M[m]); return W % p

def mat_right(M, a, p):  # M @ pi_i : column k of result = M[:, a[k]] (or 0)
    W = np.zeros_like(M); m = a >= 0
    W[:, m] = M[:, a[m]]; return W % p

# ---------------- linear algebra mod p ----------------
def rref_null(A, p):
    A = A.copy() % p; m, n = A.shape; piv = []; r = 0
    for c in range(n):
        if r >= m: break
        nz = np.nonzero(A[r:, c])[0]
        if len(nz) == 0: continue
        k = r + nz[0]
        if k != r: A[[r, k]] = A[[k, r]]
        A[r] = (A[r] * pow(int(A[r, c]), p - 2, p)) % p
        col = A[:, c].copy(); col[r] = 0
        nzr = np.nonzero(col)[0]
        if len(nzr): A[nzr] = (A[nzr] - np.outer(col[nzr], A[r])) % p
        piv.append(c); r += 1
    free = [c for c in range(n) if c not in piv]; basis = []
    for f in free:
        v = np.zeros(n, dtype=np.int64); v[f] = 1
        for i, c in enumerate(piv): v[c] = (-A[i, f]) % p
        basis.append(v)
    return basis

# ---------------- End via cyclic generator sigma ----------------
def end_algebra(basis, act, s, p=32003, seed=0, nrand=2):
    n = len(basis[0]); d = len(basis)
    # BFS predecessor tree from sigma
    pred = {s: None}; order = [s]; q = [s]
    while q:
        k = q.pop(0)
        for i in range(1, n):
            t = act[i][k]
            if t >= 0 and t != k and t not in pred: pred[t] = (k, i); order.append(t); q.append(t)
    assert len(pred) == d, "sigma does not generate"
    Ds = desL(basis[s])
    supp = [k for k, g in enumerate(basis) if Ds <= desL(g)]
    exits = [i for i in range(1, n) if act[i][s] == -1]
    # V0 = {v supported on supp, pi_i v = 0 for exit i}
    if exits:
        rows = []
        for i in exits:
            Mi = np.zeros((d, len(supp)), dtype=np.int64)
            for c, k in enumerate(supp):
                if act[i][k] >= 0: Mi[act[i][k], c] += 1
            rows.append(Mi)
        V0c = rref_null(np.vstack(rows), p)
    else:
        V0c = [np.eye(len(supp), dtype=np.int64)[c] for c in range(len(supp))]
    V0 = []
    for c in V0c:
        v = np.zeros(d, dtype=np.int64); v[supp] = c; V0.append(v)
    def F_of(v):
        F = np.zeros((d, d), dtype=np.int64); F[:, s] = v % p
        for t in order[1:]:
            k, i = pred[t]; F[:, t] = apply(act[i], F[:, k], p)
        return F
    rng = np.random.default_rng(seed)
    U = rng.integers(0, p, size=(d, nrand))
    PU = {i: apply_cols(act[i], U, p) for i in act}
    cols = []
    for v in V0:
        F = F_of(v).astype(np.float64)
        res = []
        FU = np.mod(F @ U, p).astype(np.int64)
        for i in act:
            r1 = apply_cols(act[i], FU, p)
            r2 = np.mod(F @ PU[i], p).astype(np.int64)
            res.append((r1 - r2) % p)
        cols.append(np.concatenate([x.ravel() for x in res]))
    k0 = len(V0)
    A = np.stack(cols, axis=1)
    A = A[np.any(A != 0, axis=1)]
    if A.shape[0] == 0: C = [np.eye(k0, dtype=np.int64)[j] for j in range(k0)]
    else: C = rref_null(A, p)
    E = [sum(int(c[j]) * V0[j] for j in range(k0)) % p for c in C]
    # exact verification of every End basis element
    for v in E:
        F = F_of(v)
        for i in act:
            assert ((apply_cols(act[i], F, p) - mat_right(F, act[i], p)) % p == 0).all(), "verification failed"
    return E, F_of, order, pred

def coords(E, w, p):
    """solve w = sum x_j E_j (E as d-vectors)"""
    A = np.stack(E + [w], axis=1)
    N = rref_null(A, p)
    assert len(N) >= 1
    for z in N:
        if z[-1] % p:
            inv = pow(int(z[-1]), p - 2, p); return [(-int(z[j]) * inv) % p for j in range(len(E))]
    raise ValueError("not in span")

def local_test(E, F_of, p, seed=1):
    """left-regular matrix of random X in End (coords = f(sigma)); returns (#distinct eigenvalues over closure, local?)"""
    k = len(E)
    if k == 1: return 1, True
    rnd = random.Random(seed)
    x = [rnd.randrange(p) for _ in range(k)]
    X = sum(x[j] * E[j] for j in range(k)) % p
    FX = F_of(X).astype(np.float64)
    L = np.zeros((k, k), dtype=np.int64)
    for j in range(k):
        L[:, j] = coords(E, np.mod(FX @ E[j].astype(np.float64), p).astype(np.int64), p)
    t = sp.symbols('t')
    cp = sp.Poly(sp.Matrix(L.tolist()).charpoly(t).as_expr(), t, modulus=p)
    g = sp.gcd(cp, cp.diff(t))
    nd = sp.quo(cp, g).degree()
    return nd, nd == 1

# ---------------- top via union-find ----------------
def top(basis, act):
    """dim Hom(M, C_alpha) for every alpha (as set S where pi acts by 1). exact (graph problem)."""
    n = len(basis[0]); d = len(basis); out = {}
    for r in range(n):
        for S in itertools.combinations(range(1, n), r):
            S = set(S); par = list(range(d)); zero = [False] * d
            def f(x):
                while par[x] != x: par[x] = par[par[x]]; x = par[x]
                return x
            for i in range(1, n):
                chi = 1 if i in S else 0; a = act[i]
                for g in range(d):
                    t = a[g]
                    if t == g:
                        if chi == 0: zero[f(g)] = True
                    elif t < 0:
                        if chi == 1: zero[f(g)] = True
                    else:
                        if chi == 1:
                            x, y = f(g), f(t)
                            if x != y: par[x] = y; zero[y] = zero[y] or zero[x]
                        else: zero[f(t)] = True
            roots = {f(g) for g in range(d)}
            m = sum(1 for r_ in roots if not zero[r_])
            if m: out[tuple(sorted(S))] = m
    return out

def comp_of(S, n):
    c = []; prev = 0
    for s in sorted(S) + [n]: c.append(s - prev); prev = s
    return tuple(c)

def character(basis, n):
    """ch = sum_gamma F_{comp(Des_L(gamma))^c}  (Lemma 3.2 proof)."""
    ch = {}
    for g in basis:
        S = set(range(1, n)) - desL(g)
        c = comp_of(S, n); ch[c] = ch.get(c, 0) + 1
    return ch
