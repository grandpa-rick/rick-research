import sys, json, time, itertools, numpy as np
from core import setup, T_ops, U0_ops
from lin import *
from flint import fmpz_mat, fmpq_mat

def np_of(M): return np.array([[int(M[r,c]) for c in range(M.ncols())] for r in range(M.nrows())], dtype=object)
def length(w): return sum(1 for i in range(len(w)) for j in range(i+1, len(w)) if w[i] > w[j])
def comp_of(D, N):
    pts = [0] + sorted(D) + [N]; return tuple(pts[k+1]-pts[k] for k in range(len(pts)-1))
def des_of(J): return frozenset(itertools.accumulate(J[:-1]))

def hecke(N):
    perms = list(itertools.permutations(range(N))); pid = {p: k for k, p in enumerate(perms)}; m = len(perms)
    def rmul_i(p, i):  # p*s_i : swap positions i,i+1 (one-line)
        q = list(p); q[i], q[i+1] = q[i+1], q[i]; return tuple(q)
    def lmul_i(p, i):  # s_i*p : swap values i,i+1
        return tuple(i+1 if x == i else i if x == i+1 else x for x in p)
    R = []; L = []
    for i in range(N-1):
        Ri = np.zeros((m, m), dtype=object); Li = np.zeros((m, m), dtype=object)
        for p in perms:
            q = rmul_i(p, i)
            if length(q) > length(p): Ri[pid[q], pid[p]] = 1
            else: Ri[pid[p], pid[p]] = -1
            q = lmul_i(p, i)
            if length(q) > length(p): Li[pid[q], pid[p]] = 1
            else: Li[pid[p], pid[p]] = -1
        R.append(Ri); L.append(Li)
    # reduced words
    red = {}
    for p in perms:
        w = list(p); word = []
        # bubble sort from the right: p = s_{i1}...s_{ik} as right products from identity
        q = list(p); seq = []
        while True:
            for i in range(N-1):
                if q[i] > q[i+1]: q[i], q[i+1] = q[i+1], q[i]; seq.append(i); break
            else: break
        red[p] = list(reversed(seq))  # id * s_{seq reversed} = p
    return perms, pid, R, L, red

def run(n, N):
    t0 = time.time(); W, idx, d = setup(n, N)
    rho = [np_of(T) for T in T_ops(n, N)]
    perms, pid, Rr, Ll, red = hecke(N); m = len(perms)
    # check reduced words: right-multiplying identity
    for p in perms:
        v = np.zeros(m, dtype=object); v[pid[tuple(range(N))]] = 1
        for i in red[p]: v = Rr[i] @ v
        assert v[pid[p]] == 1 and sum(abs(x) for x in v) == 1
    I = np.eye(d, dtype=object)
    rhow = {}
    for p in perms:
        M = I.copy()
        for i in red[p]: M = rho[i] @ M   # v.(pi_{i1}...pi_{ik}) = rho_ik ... rho_i1 v
        rhow[p] = M
    def rho_of(h): 
        M = np.zeros((d, d), dtype=object)
        for k, c in enumerate(h):
            if c: M = M + c * rhow[perms[k]]
        return M
    # left regular matrices of basis elements: L_{pi_w} = prod of L_i in order (pi_w = pi_i1..pi_ik, left mult by pi_w = L_i1 ... L_ik)
    Lw = {}
    for p in perms:
        M = np.eye(m, dtype=object)
        for i in red[p]: M = M @ Ll[i]
        Lw[p] = M
    G = [[int(np.trace(Lw[a] @ Lw[b])) for b in perms] for a in perms]
    JH = nullspace(G, m)   # radical of H (char 0 trace criterion on faithful left regular rep)
    def Rmat(h):  # right multiplication by h on H (x -> x h)
        M = np.zeros((m, m), dtype=object)
        for k, c in enumerate(h):
            if c:
                Mk = np.eye(m, dtype=object)
                for i in red[perms[k]]: Mk = Rr[i] @ Mk
                M = M + c * Mk
        return M
    # soc(H) right socle = {x : x j = 0 for j in J}
    rows = []
    for j in JH:
        rows += [list(r) for r in Rmat(j)]
    socH = nullspace(rows, m)
    def Lmat(h):
        M = np.zeros((m, m), dtype=object)
        for k, c in enumerate(h):
            if c: M = M + c * Lw[perms[k]]
        return M
    subsets = [frozenset(s) for r in range(N) for s in itertools.combinations(range(1, N), r)]  # D subset of {1..N-1}; pi_i index i-1
    def chi(D, i): return -1 if (i+1) in D else 0
    # pairs (left char a, right char b) in soc(H)
    nu = {}
    for a in subsets:
        for b in subsets:
            ops = [Ll[i] - chi(a, i)*np.eye(m, dtype=object) for i in range(N-1)] + [Rr[i] - chi(b, i)*np.eye(m, dtype=object) for i in range(N-1)]
            rows2 = []
            # v in socH span with ops v = 0
            B = socH
            cols = np.array(B, dtype=object).T if B else np.zeros((m, 0), dtype=object)
            for op in ops: rows2 += [list(r) for r in (op @ cols)]
            k = len(B) - (fmpz_mat([list(map(int, r)) for r in rows2]).rank() if B else 0)
            if k: nu.setdefault(a, []).append((b, k))
    # ---- S basis (blockwise commutant)
    wts = {}
    for k, w in enumerate(W): wts.setdefault(tuple(w.count(i) for i in range(n)), []).append(k)
    wl = list(wts.items())
    Sbasis = []
    for mu, a in wl:
        for nu_, b in wl:
            na, nb = len(a), len(b); rows3 = []
            for g in rho:
                ga = g[np.ix_(a, a)]; gb = g[np.ix_(b, b)]
                for r in range(nb):
                    for c in range(na):
                        row = [0]*(na*nb)
                        for k in range(nb):
                            if gb[r, k]: row[k*na+c] += int(gb[r, k])
                        for k in range(na):
                            if ga[k, c]: row[r*na+k] -= int(ga[k, c])
                        rows3.append(row)
            for v in nullspace(rows3, na*nb):
                X = np.zeros((d, d), dtype=object)
                for r in range(nb):
                    for c in range(na): X[b[r], a[c]] = v[r*na+c]
                Sbasis.append((mu, nu_, X))
    sdim = len(Sbasis)
    # trace-form radical of S (blocks: tr(XY) nonzero only if X: mu->nu, Y: nu->mu)
    Gs = [[0]*sdim for _ in range(sdim)]
    for x, (m1, n1, X) in enumerate(Sbasis):
        for y, (m2, n2, Y) in enumerate(Sbasis):
            if m1 == n2 and n1 == m2: Gs[x][y] = int(np.trace(X @ Y))
    JSc = nullspace(Gs, sdim)
    JS = []
    for c in JSc:
        M = np.zeros((d, d), dtype=object)
        for k, cc in enumerate(c):
            if cc: M = M + cc * Sbasis[k][2]
        JS.append(M)
    JA = [rho_of(j) for j in JH]
    # cross-check J(S) = {X in S : im X in V.J(A)}
    VJ = basis_of([list(M[:, c]) for M in JA for c in range(d)], d)
    ann = nullspace(VJ, d) if VJ else [[int(i == j) for j in range(d)] for i in range(d)]
    rows4 = []
    for a_ in ann:
        a_ = np.array(a_, dtype=object)
        for c in range(d):
            rows4.append([int((a_ @ X)[c]) for (_, _, X) in Sbasis])
    JS2dim = len(nullspace(rows4, sdim))
    # ---- radical series of V as bimodule
    radops = JS + JA
    layers = []; R = [list(r) for r in np.eye(d, dtype=int)]
    series = [R]
    while R:
        newv = []
        for op in radops:
            M = op @ np.array(R, dtype=object).T
            newv += [list(M[:, c]) for c in range(M.shape[1])]
        R2 = basis_of(newv, d)
        series.append(R2); R = R2
    # ---- socle series
    soc = [[]]
    while dim_span(soc[-1]) < d:
        nxt = preimage_in(radops, soc[-1], d); soc.append(nxt)
    # ---- F_J expansion helper
    comps = [J for k in range(1, n+1) for J in itertools.product(range(1, N+1), repeat=k) if sum(J) == N]
    mus = [mu for mu, _ in wl]
    def Smu(mu):
        s = set(); acc = 0
        for x in mu[:-1]:
            acc += x
            if 0 < acc < N: s.add(acc)
        return s
    Fmat = [[1 if des_of(J) <= Smu(mu) else 0 for J in comps] for mu in mus]
    def expandF(charvec):
        A = fmpq_mat(Fmat); bvec = fmpq_mat([[c] for c in charvec])
        x = A.solve(bvec) if len(comps) == len(mus) else None
        if x is None:
            # least squares-free: solve via normal eq exact (A has full column rank)
            At = A.transpose(); x = (At*A).solve(At*bvec)
            assert A*x == bvec, "character not in span of F_J"
        return {comps[k]: int(x[k, 0]) for k in range(len(comps)) if x[k, 0] != 0}
    def layer_decomp(Up, Ud):
        """semisimple bimodule Up/Ud: returns {(J_S, comp_H): mult}."""
        out = {}
        annD = nullspace(Ud, d) if Ud else [[int(i == j) for j in range(d)] for i in range(d)]
        for D in subsets:
            charvec = []
            for mu, a in wl:
                Bm = basis_of([[v[k] if k in set(a) else 0 for k in range(d)] for v in Up], d)
                if not Bm: charvec.append(0); continue
                Bd = [[v[k] if k in set(a) else 0 for k in range(d)] for v in Ud]
                ddim = dim_span(Bd)
                cols = np.array(Bm, dtype=object).T
                rows5 = []
                for i in range(N-1):
                    M = (rho[i] - chi(D, i)*np.eye(d, dtype=object)) @ cols
                    for a_ in annD: rows5.append(list(np.array(a_, dtype=object) @ M))
                k = len(nullspace(rows5, len(Bm)))
                charvec.append(k - ddim)
            if any(charvec):
                for J, c in expandF(charvec).items(): out[(J, comp_of(D, N))] = c
        return out
    radlayers = [layer_decomp(series[k], series[k+1]) for k in range(len(series)-1)]
    soclayers = [layer_decomp(soc[k+1], soc[k]) for k in range(len(soc)-1)]
    # ---- filtration end-tests: bottom sub-bimodule L_I x P_I ; top quotient L_I x P_I
    socHrho = [rho_of(h) for h in socH]
    def times_socH(vecs):
        out = []
        for M in socHrho:
            P = M @ np.array(vecs, dtype=object).T
            out += [list(P[:, c]) for c in range(P.shape[1])]
        return out
    SocS = preimage_in(JS, [], d)   # {v : J(S) v = 0}
    Zb = basis_of(times_socH(SocS), d) if SocS else []
    bottom = layer_decomp(Zb, []) if Zb else {}
    JSV = basis_of([list(M[:, c]) for M in JS for c in range(d)], d)
    Zt = basis_of(JSV + times_socH([list(r) for r in np.eye(d, dtype=int)]), d)
    top = layer_decomp(Zt, JSV)
    nu_c = {comp_of(a, N): [(comp_of(b, N), k) for b, k in v] for a, v in nu.items()}
    res = dict(n=n, N=N, dimJH=len(JH), dimsocH=len(socH), nakayama=nu_c, dimS=sdim, dimJS=len(JSc), dimJS_via_projective_crit=JS2dim,
               radical_dims=[dim_span(s) for s in series], socle_dims=[dim_span(s) for s in soc],
               rad_layers=radlayers, soc_layers=soclayers, bottom_socS_times_socH=bottom, top_quot_times_socH=top, t=round(time.time()-t0, 1))
    return res

if __name__ == '__main__':
    n, N = int(sys.argv[1]), int(sys.argv[2])
    res = run(n, N)
    s = lambda o: {str(k): v for k, v in o.items()} if isinstance(o, dict) else o
    res2 = {k: ([s(x) for x in v] if k.endswith('layers') else s(v)) for k, v in res.items()}
    json.dump(res2, open(f'step2_{n}{N}.json', 'w'), indent=1)
    for k, v in res2.items(): print(k, ':', v)
