"""Wake 287: Q71 U0-variant. Does V^{(x)N} (V=Q^2) admit a chain of (rho(U_0),H_N(0))-sub-bimodules with
H-projective isotypic layers (weak form) / layers L (x) M_I, each I once (strong form)?
Exact over Q (sympy). Action: core.py = Jung-Oh 2509.26194 (4.5) [pibar^2=-pibar] and Def 4.2 coproduct
  Delta(e)=1(x)e + e(x)k_i, Delta(f)=k_{i+1}(x)f + f(x)1, Delta(k)=k(x)k, rho_V(k_i)=sum_{j!=i}E_jj.
Method (n=2): V = T (+) Y, T = V.eps (eps = pi_{w0}, pi_i=1+pibar_i, central idempotent of the trivial block,
M_(N)=C_empty simple projective) and Y = V.(1-eps) = (+)_{a=1}^{N-1} P_(a,N-a), P_(a,N-a) = Y cap weight(a,N-a).
Both A-stable (A = <rho(U0),rho(H)>), so chains decouple.  In Y each type occurs once, End P = Q, so any H-summand
of type P_i is a graph x -> x + phi(x), phi in Hom_H(P_i, rest).  Search: bottom layer = A-stable graph of a
single P_i (solve quadratic system g21 + g22 phi = phi(g11 + g12 phi) for all generators g), pass to quotient
(g' = g22 - phi g12), recurse."""
import sys, itertools, json
import sympy as sp
from core import setup, T_ops, U0_ops, algebra_span

def tosp(M): return sp.Matrix(M.nrows(), M.ncols(), lambda r, c: int(M[r, c]))

def colspace_basis(M):
    return sp.Matrix.hstack(*M.columnspace()) if M.rank() else None

def coords(B, X):
    """B (d x r) full col rank, X (d x s) with columns in colspan B: return C with B C = X."""
    C = (B.T*B).inv()*B.T*X
    assert B*C == X
    return C

def run(n, N, verbose=True):
    W, idx, d = setup(n, N)
    T = [tosp(t) for t in T_ops(n, N)]        # column convention: T_i v = v.pibar_i
    U = U0_ops(n, N); Ug = {k: tosp(v) for k, v in U.items()}
    out = {'n': n, 'N': N, 'd': d}
    # dims
    AH = algebra_span(list(T_ops(n, N)), d); AU = algebra_span(list(U.values()), d)
    out['dim_rhoH'] = len(AH); out['dim_rhoU0'] = len(AU)
    # check commutation
    assert all(t*u == u*t for t in T for u in Ug.values())
    # eps = pi_{w0}: right action v.(pi_{i1}...pi_{ik}) = P_ik ... P_i1 v, P_i = I + T_i
    I = sp.eye(d); P = [I + t for t in T]
    w0 = [i for k in range(N-1) for i in range(N-1-k)]   # bubble-sort reduced word of w0 (length N(N-1)/2)
    assert len(w0) == N*(N-1)//2
    E = I
    for i in w0: E = P[i]*E
    assert E*E == E and all(t*E == sp.zeros(d) for t in T) and all(E*t == sp.zeros(d) for t in T)
    out['dim_trivial_block'] = E.rank()
    # trivial block: check U0 acts irreducibly (algebra = full matrix algebra) on it
    Bt = colspace_basis(E)
    gens_t = [coords(Bt, g*Bt) for g in Ug.values()]
    r = Bt.shape[1]
    # algebra span on block
    basis = [sp.eye(r)]; vecs = [list(sp.eye(r))]; frontier = [sp.eye(r)]
    while frontier:
        new = []
        for X in frontier:
            for g in gens_t:
                Yv = g*X
                if sp.Matrix(vecs + [list(Yv)]).rank() > len(vecs):
                    vecs.append(list(Yv)); new.append(Yv)
        frontier = new
    out['dim_U0_on_trivial_block'] = len(vecs); out['trivial_block_simple_U0'] = (len(vecs) == r*r)
    # Y summands by weight
    Ey = I - E
    summ = []
    for a in range(1, N):
        cols = [idx[w] for w in W if w.count(0) == a] if n == 2 else None
        sub = Ey[:, cols]
        if sub.rank() == 0: continue
        summ.append(((a, N-a), colspace_basis(sub)))
    out['summands'] = {str(k): b.shape[1] for k, b in summ}
    By = sp.Matrix.hstack(*[b for _, b in summ])
    sizes = [b.shape[1] for _, b in summ]; labels = [k for k, _ in summ]
    off = [sum(sizes[:k]) for k in range(len(sizes)+1)]
    Hy = [coords(By, t*By) for t in T]
    Gy = {k: coords(By, g*By) for k, g in Ug.items()}
    # structure of rho(U0) restricted to Y in block-matrix terms
    for k, g in Gy.items():
        nz = [(labels[i], labels[j]) for i in range(len(sizes)) for j in range(len(sizes))
              if g[off[i]:off[i+1], off[j]:off[j+1]] != sp.zeros(sizes[i], sizes[j])]
        out.setdefault('U0_gen_blocks(target<-source)', {})[k] = [f'{a}<-{b}' for a, b in nz]
    # Hom_H between summands (dims)
    def hom_basis(i, j):
        """basis of Hom_H(P_i -> P_j) as matrices sizes[j] x sizes[i]."""
        si, sj = sizes[i], sizes[j]
        xs = sp.symbols(f'x0:{si*sj}'); X = sp.Matrix(sj, si, xs)
        eqs = []
        for h in Hy:
            hi = h[off[i]:off[i+1], off[i]:off[i+1]]; hj = h[off[j]:off[j+1], off[j]:off[j+1]]
            eqs += list(hj*X - X*hi)
        A, _ = sp.linear_eq_to_matrix(eqs, xs)
        return [sp.Matrix(sj, si, list(v)) for v in A.nullspace()]
    homdim = {f'{labels[i]}->{labels[j]}': len(hom_basis(i, j)) for i in range(len(sizes)) for j in range(len(sizes))}
    out['dim_Hom_H'] = homdim
    # rho(A) restricted to Y: dims of U0 image vs End_H(Y)
    Uy = []
    for X in AU:
        Xs = tosp(X); Uy.append(list(coords(By, Xs*By)))
    out['dim_U0_on_Y'] = sp.Matrix(Uy).rank(); out['dim_End_H(Y)'] = sum(homdim.values())
    # recursive search. state: list of remaining summand indices; ops (U gens, as matrices on current coords)
    chains = []; attempts = []
    path_labels = lambda path: [labels.index(p[0]) for p in path]
    def search(rem, G, path):
        if not rem:
            chains.append(path); return
        sz = [sizes[i] for i in rem]; o = [sum(sz[:k]) for k in range(len(sz)+1)]
        for pos, i in enumerate(rem):
            others = [j for j in rem if j != i]
            # reorder coords: i first
            perm = list(range(o[pos], o[pos+1])) + [c for q in range(len(rem)) if q != pos for c in range(o[q], o[q+1])]
            Gp = {k: g.extract(perm, perm) for k, g in G.items()}
            si = sizes[i]; so = sum(sizes[j] for j in others)
            # phi in Hom_H(P_i, (+)others)
            hb = []
            for qq, j in enumerate(others):
                for Bm in hom_basis(i, j):
                    full = sp.zeros(so, si); oo = sum(sizes[jj] for jj in others[:qq])
                    full[oo:oo+sizes[j], :] = Bm; hb.append(full)
            cs = sp.symbols(f'c0:{len(hb)}') if hb else ()
            phi = sum((c*Bm for c, Bm in zip(cs, hb)), sp.zeros(so, si))
            eqs = []
            for g in Gp.values():
                g11, g12, g21, g22 = g[:si, :si], g[:si, si:], g[si:, :si], g[si:, si:]
                eqs += [sp.expand(e) for e in (g21 + g22*phi - phi*(g11 + g12*phi))]
            eqs = [e for e in eqs if e != 0]
            sols = sp.solve(eqs, cs, dict=True) if eqs else [dict()]
            attempts.append((tuple(labels[j] for j in path_labels(path)), labels[i], len(sols), [ [str(c) for c in cs if c not in so] for so in sols]))
            for sol in sols:
                free = [c for c in cs if c not in sol]
                if free:
                    # positive-dimensional family: record, specialise free params to 0 for recursion
                    sol = dict(sol); [sol.setdefault(c, 0) for c in free]
                phis = phi.subs(sol)
                Gq = {k: (g[si:, si:] - phis*g[:si, si:]) for k, g in Gp.items()}
                search(others, Gq, path + [(labels[i], {str(k): str(v) for k, v in sol.items()}, [str(c) for c in free])])
    search(list(range(len(sizes))), Gy, [])
    out['chains_in_Y'] = chains
    out['bottom_attempts(prefix,type,#solutions,free_params)'] = attempts
    out['any_free_family_in_failed_search'] = (not chains) and any(any(f) for a in attempts for f in a[3])
    out['answer_weak'] = bool(chains) and True
    out['answer_strong'] = bool(chains) and out['trivial_block_simple_U0']
    if verbose:
        for k, v in out.items(): print(k, ':', v)
    return out

if __name__ == '__main__':
    n, N = int(sys.argv[1]), int(sys.argv[2])
    res = run(n, N)
    json.dump(res, open(f'res_{n}{N}.json', 'w'), indent=1, default=str)
