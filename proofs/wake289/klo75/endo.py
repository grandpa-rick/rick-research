# End_{H_n(0)}(X_{lam/mu}) over GF(P) via Frobenius reciprocity from the Young-block subspace W.
import numpy as np, flint, itertools
import scipy.sparse as sp
from collections import deque
from shapes import *
P = 1000003

def check_relations(acts, m):
    n1 = len(acts)
    def app(f, vec):  # vec: array of basis indices (or -1)
        out = vec.copy(); ok = vec >= 0; out[ok] = np.asarray(f)[vec[ok]]; return out
    base = np.arange(m)
    for i in acts:
        f = np.asarray(acts[i])
        a = app(f, base); assert (app(f, a) == a).all(), ('pi^2', i)
        if i+1 in acts:
            g = np.asarray(acts[i+1])
            assert (app(f, app(g, app(f, base))) == app(g, app(f, app(g, base)))).all(), ('braid', i)
        for j in acts:
            if j >= i+2:
                g = np.asarray(acts[j]); assert (app(f, app(g, base)) == app(g, app(f, base))).all(), ('comm', i, j)

class Solver:
    """nullspace of sparse linear system mod P: weighted union-find for <=2-term rows, dense flint for the rest."""
    def __init__(self, V):
        self.par = list(range(V)); self.sc = [1]*V   # x = sc * par (to root), root zero flag
        self.zero = [False]*V; self.big = []
    def find(self, x):
        s = 1
        path = []
        while self.par[x] != x:
            path.append((x, s)); s = s*self.sc[x] % P; x = self.par[x]
        # compress
        acc = 1
        for (y, sy) in reversed(path): pass
        r = x
        # recompute scales relative to root
        for y, _ in path:
            pass
        return r, s
    def reduce(self, row):
        d = {}
        for x, c in row.items():
            r, s = self.find(x)
            if self.zero[r]: continue
            d[r] = (d.get(r, 0) + c*s) % P
        return {k: v for k, v in d.items() if v}
    def add(self, row):
        d = self.reduce(row)
        if len(d) == 0: return
        if len(d) == 1:
            (r, _), = d.items(); self.zero[r] = True; return
        if len(d) == 2:
            (r1, c1), (r2, c2) = d.items()
            # c1 r1 + c2 r2 = 0 -> r1 = -c2/c1 r2
            self.par[r1] = r2; self.sc[r1] = (-c2*pow(c1, P-2, P)) % P; return
        self.big.append(d)
    def nullspace(self, V):
        changed = True
        while changed:
            changed = False; old = self.big; self.big = []
            for d in old:
                nb = len(self.big); self.add(d)
                if len(self.big) == nb: changed = True
        roots = [x for x in range(V) if self.find(x)[0] == x and not self.zero[x]]
        ridx = {r: k for k, r in enumerate(roots)}
        R = len(roots)
        rows = [self.reduce(d) for d in self.big]; rows = [d for d in rows if d]
        if rows and R:
            # incremental rref in chunks to bound memory
            M = None; CH = max(200, 2000000 // max(R, 1))
            for c0 in range(0, len(rows), CH):
                chunk = rows[c0:c0+CH]
                base = 0 if M is None else M.nrows()
                N = flint.nmod_mat(base + len(chunk), R, P)
                if M is not None:
                    for a in range(base):
                        for b in range(R):
                            v = M[a, b]
                            if int(v): N[a, b] = v
                for a, d in enumerate(chunk):
                    for r, c in d.items(): N[base + a, ridx[r]] = c
                Rr, rank = N.rref()
                M = flint.nmod_mat(rank, R, P)
                for a in range(rank):
                    for b in range(R):
                        v = Rr[a, b]
                        if int(v): M[a, b] = v
            Rr, rank = M, M.nrows()
            # nullspace of R x R from rref
            piv = []
            for a in range(rank):
                for b in range(R):
                    if int(Rr[a, b]) != 0: piv.append(b); break
            free = [b for b in range(R) if b not in set(piv)]
            basis_roots = []
            for fcol in free:
                v = [0]*R; v[fcol] = 1
                for a, pc in enumerate(piv): v[pc] = (-int(Rr[a, fcol])) % P
                basis_roots.append(v)
        else:
            basis_roots = [[1 if k == j else 0 for k in range(R)] for j in range(R)]
        # expand to all vars
        out = []
        rs = [self.find(x) for x in range(V)]
        for v in basis_roots:
            w = np.zeros(V, dtype=np.int64)
            for x in range(V):
                r, s = rs[x]
                if self.zero[r]: continue
                w[x] = s*v[ridx[r]] % P
            out.append(w)
        return out

def apply_f(f, col):
    """apply monomial operator f (array, -1 = kills) to a coefficient vector col."""
    m = len(col); out = np.zeros(m, dtype=np.int64); ok = f >= 0
    np.add.at(out, f[ok], col[ok]); return out % P

def apply_f_map(f, g):
    """compose: g maps unknown-slot S -> basis index (or -1); returns f o g."""
    out = g.copy(); ok = g >= 0; out[ok] = f[g[ok]]; return out

def endo(lam, mu, verbose=False):
    comps, rib, lab = classify(lam, mu)
    B, acts = action(lam, mu); m = len(B); n = sum(lam)-sum(mu)
    check_relations(acts, m)
    F = {i: np.asarray(acts[i]) for i in acts}
    # Young blocks: component k (top to bottom) gets the k-th block of consecutive entries
    rowcomp = {}
    for k, rows in enumerate(comps):
        for r in rows: rowcomp[r] = k
    sizes = [sum(lam[r]-mu[r] for r in rows) for rows in comps]
    bounds = np.cumsum([0]+sizes)
    blk = lambda e: int(np.searchsorted(bounds, e, side='right')-1)  # entry e (0-based) -> block
    Wset = [t for t, b in enumerate(B) if all(rowcomp[b[e][0]] == blk(e) for e in range(n))]
    cut = set(int(x) for x in bounds[1:-1])   # generator pi_a with a = boundary (1-based a = bounds) excluded
    Hp = [i for i in F if i not in cut]
    # dimension check: multinomial * prod f
    # spanning check + BFS forest of X from W
    inW = set(Wset)
    # sources of W under H'
    hasin = set()
    for i in Hp:
        for t in Wset:
            s = F[i][t]
            if s >= 0 and s != t: hasin.add(int(s))
    srcW = [t for t in Wset if t not in hasin]
    # forest of W from sources (H' moves), and of X from W-sources (all moves)
    def forest(starts, gens, allowed=None):
        par = {t: None for t in starts}; order = list(starts); dq = deque(starts)
        while dq:
            t = dq.popleft()
            for i in gens:
                s = int(F[i][t])
                if s >= 0 and s not in par and (allowed is None or s in allowed):
                    par[s] = (t, i); order.append(s); dq.append(s)
        return par, order
    parW, ordW = forest(srcW, Hp, inW)
    assert len(ordW) == len(Wset), 'W not generated by its sources'
    parX, ordX = forest(srcW, list(F))
    iso = (len(ordX) == m)
    assert iso, 'W does not generate X'
    # unknowns: v_j in K^m for each W-source j; slot index j*m+S
    s = len(srcW); V = s*m
    # g_t: map slot S (of source j(t)) -> basis index of A_{w_t} e_S
    g = {}; jt = {}
    for j, t0 in enumerate(srcW): g[t0] = np.arange(m); jt[t0] = j
    for t in ordW:
        if parW[t] is None: continue
        p, i = parW[t]; g[t] = apply_f_map(F[i], g[p]); jt[t] = jt[p]
    S = Solver(V)
    Rs, Vs, Cs = [], [], []; rowbase = 0
    for t in Wset:
        for i in Hp:
            t2 = int(F[i][t])
            if t2 >= 0 and t2 != t and parW.get(t2) == (t, i): continue
            lhs = apply_f_map(F[i], g[t]); ok = lhs >= 0
            Rs.append(rowbase + lhs[ok]); Vs.append(jt[t]*m + np.nonzero(ok)[0]); Cs.append(np.ones(ok.sum(), dtype=np.int64))
            if t2 >= 0:
                ok2 = g[t2] >= 0
                Rs.append(rowbase + g[t2][ok2]); Vs.append(jt[t2]*m + np.nonzero(ok2)[0]); Cs.append(-np.ones(ok2.sum(), dtype=np.int64))
            rowbase += m
    if Rs:
        Rr = np.concatenate(Rs); Vv = np.concatenate(Vs); Cc = np.concatenate(Cs)
        key = Rr.astype(np.int64)*V + Vv
        uk, inv = np.unique(key, return_inverse=True)
        coef = np.bincount(inv, weights=Cc, minlength=len(uk)).astype(np.int64) % P
        nz = coef != 0; uk = uk[nz]; coef = coef[nz]
        rid = uk // V; var = uk % V
        # group by row
        bnd = np.flatnonzero(np.diff(rid)) + 1
        starts = np.concatenate([[0], bnd]); ends = np.concatenate([bnd, [len(rid)]])
        # dedupe identical rows cheaply: process 1-term rows first, then 2-term, then rest
        ln = ends - starts
        order = np.argsort(ln, kind='stable')
        seen = set()
        for k in order:
            st, en = starts[k], ends[k]
            sig = (tuple(var[st:en].tolist()), tuple(coef[st:en].tolist()))
            if sig in seen: continue
            seen.add(sig)
            S.add(dict(zip(sig[0], sig[1])))
    basis = S.nullspace(V)
    d = len(basis)
    # full matrices of End basis elements (columns indexed by X basis)
    Asp = {}
    for i in F:
        ok = F[i] >= 0
        Asp[i] = sp.csr_matrix((np.ones(ok.sum(), dtype=np.int64), (F[i][ok], np.nonzero(ok)[0])), shape=(m, m))
    # path tables: G[:, T] = g_T, the partial map S -> A_{path T} e_S (monomial!), path from W-source j(T)
    depth = {}
    for t in ordX:
        depth[t] = 0 if parX[t] is None else depth[parX[t][0]] + 1
    groups = {}
    for t in ordX:
        if parX[t] is None: continue
        p, i = parX[t]; groups.setdefault((depth[t], i), ([], []))
        groups[(depth[t], i)][0].append(t); groups[(depth[t], i)][1].append(p)
    G = np.full((m, m), -1, dtype=np.int32)
    jX = np.zeros(m, dtype=np.int64)
    for j, t0 in enumerate(srcW): G[:, t0] = np.arange(m); jX[t0] = j
    for (dp, i), (ch, pa) in sorted(groups.items()):
        ch = np.array(ch); pa = np.array(pa); old = G[:, pa]; new = np.full_like(old, -1)
        ok = old >= 0; new[ok] = F[i][old[ok]]; G[:, ch] = new; jX[ch] = jX[pa]
    d = len(basis)
    BN = np.array(basis, dtype=np.int64).reshape(d, s, m)   # BN[a, j, S] = v^a_j[S]
    cen = lambda A: np.where(A > P//2, A - P, A)
    # randomized commutation check on a random combination x of the basis: A_i M_x r = M_x A_i r
    rng = np.random.default_rng(1)
    def Mx_apply(v, r):  # v: (s, m) source vectors, r: vector on X; returns M_x r
        out = np.zeros(m, dtype=np.float64)
        for j in range(s):
            cols = np.nonzero(jX == j)[0]
            Gs = G[:, cols]; ok = Gs >= 0
            w = (cen(v[j])[:, None].astype(np.float64) * cen(r[cols])[None, :].astype(np.float64))
            # values up to (P/2)^2 ~ 2.5e11, sums over <= m^2 terms: reduce mod P per column block to stay exact
            w = np.mod(w, P)
            out += np.bincount(Gs[ok], weights=w[ok], minlength=m)
        return np.mod(np.rint(out).astype(np.int64), P)
    xc = np.mod(rng.integers(0, P, size=d) @ BN.reshape(d, s*m), P).reshape(s, m) if d else None
    Asp = {}
    for i in F:
        ok = F[i] >= 0
        Asp[i] = sp.csr_matrix((np.ones(ok.sum(), dtype=np.int64), (F[i][ok], np.nonzero(ok)[0])), shape=(m, m))
    if d and m <= 7000:
        r = rng.integers(0, P, size=m)
        Mr = Mx_apply(xc, r)
        for i in F:
            assert (np.mod(Asp[i].dot(Mr), P) == Mx_apply(xc, np.mod(Asp[i].dot(r), P))).all(), ('not commuting', i)
    # trace functionals: tau_j[S] = #{T : j(T)=j, g_T(S) = T}
    tau = np.zeros((s, m), dtype=np.int64)
    for j in range(s):
        cols = np.nonzero(jX == j)[0]
        hit = (G[:, cols] == cols[None, :])
        tau[j] = hit.sum(axis=1)
    # Gram_ab = tr(x_a x_b) = sum_j sum_T v^b_j[T] sum_S v^a_{j(T)}[S] tau_j[g_T(S)]
    Gram = np.zeros((d, d), dtype=np.int64)
    for j in range(s):
        tj = np.concatenate([tau[j], [0]])
        Q = tj[G].astype(np.float64)             # Q[S,T] = tau_j[g_T(S)], (G=-1 -> index m -> 0)
        Z = np.zeros((d, m), dtype=np.float64)
        for jp in range(s):
            cols = np.nonzero(jX == jp)[0]
            Z[:, cols] = cen(BN[:, jp, :]).astype(np.float64) @ Q[:, cols]   # |entries| < P/2 * m * m: exact? see note
        Z = np.mod(np.rint(Z).astype(np.int64), P)
        Gram = np.mod(Gram + np.mod(np.rint(cen(Z).astype(np.float64) @ cen(BN[:, j, :]).T.astype(np.float64)).astype(np.int64), P), P)
    rkG = flint.nmod_mat([[int(x) for x in row] for row in Gram], P).rank() if d else 0
    # identity check: the identity endomorphism has source vectors e_{t_j}; tr(1)=m
    assert int(tau[np.arange(s), np.array(srcW)].sum()) == m, 'trace of identity != m'
    return dict(lam=lam, mu=mu, comps=comps, rib=rib, lab=lab, m=m, s=s, dimEnd=d, dimEndJ=rkG, dimJ=d-rkG, basis=basis, srcW=srcW, Gram=Gram, G=None)
