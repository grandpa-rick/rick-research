"""Generic (s,t) Hikita star product. e_k*F = E_k F,
E_k F = sum_{|A|=k} prod_{i in A, j notin A}(x_i - t x_j)/(x_i - x_j) X_A F(X_{A^c}, s X_A).
Matrices of E_k: Lambda^d -> Lambda^{d+k} in Schur basis, N = d+k variables.
V*E_k(s_mu) computed directly (no division) -> Schur coeffs via alternant."""
import sys, itertools, pickle
from sympy.polys.rings import ring
from sympy import ZZ, Symbol
S, T = Symbol('s'), Symbol('t')
def parts(n, m=None):
    if m is None: m = n
    if n == 0: yield (); return
    for k in range(min(n, m), 0, -1):
        for p in parts(n-k, k): yield (k,)+p
RINGS = {}
def R(N):
    if N not in RINGS:
        Rg, *g = ring(['s', 't']+[f'x{i}' for i in range(N)], ZZ)
        RINGS[N] = (Rg, g[0], g[1], g[2:])
    return RINGS[N]
def ssyt(lam, N):
    cells = [(i, j) for i, r in enumerate(lam) for j in range(r)]; Tb = {}
    def rec(c):
        if c == len(cells):
            v = [0]*N
            for x in Tb.values(): v[x] += 1
            yield tuple(v); return
        i, j = cells[c]
        lo = max(Tb[(i, j-1)] if j > 0 else 0, Tb[(i-1, j)]+1 if i > 0 else 0)
        for x in range(lo, N):
            Tb[(i, j)] = x; yield from rec(c+1)
        Tb.pop((i, j), None)
    yield from rec(0)
def schur(lam, N):
    Rg = R(N)[0]; d = {}
    if len(lam) > N: return Rg(0)
    for v in ssyt(lam, N): d[(0, 0)+v] = d.get((0, 0)+v, 0)+1
    return Rg.from_dict(d) if d else Rg(0)
def VEk(k, F, N):  # returns V * E_k F
    Rg, s, t, xs = R(N); tot = Rg(0); Fd = F.to_dict()
    for A in itertools.combinations(range(N), k):
        B = [j for j in range(N) if j not in A]
        sign = (-1)**sum(1 for i in A for j in B if i > j)
        term = Rg(sign)
        for i in range(N):
            for j in range(i+1, N):
                if (i in A) == (j in A): term *= xs[i]-xs[j]
        for i in A:
            term *= xs[i]
            for j in B: term *= xs[i]-t*xs[j]
        Fs = Rg.from_dict({(m[0]+sum(m[2+i] for i in A),)+m[1:]: c for m, c in Fd.items()})
        tot += term*Fs
    return tot
def alt_to_schur(G, N):  # G = V*f ; returns {lam: poly in s,t (sympy ring element in (s,t))}
    d = {}
    for m, c in G.terms():
        lam = [m[2+i]-(N-1-i) for i in range(N)]
        if all(lam[i] > lam[i+1]-1 for i in range(N-1)) and all(lam[i] >= lam[i+1] for i in range(N-1)) and lam[-1] >= 0:
            key = tuple(a for a in lam if a > 0)
            d.setdefault(key, {}); d[key][(m[0], m[1])] = d[key].get((m[0], m[1]), 0)+c
    return {k: {e: c for e, c in v.items() if c} for k, v in d.items() if any(v.values())}
def Ematrix(k, d, N=None):
    if N is None: N = d+k
    return {mu: alt_to_schur(VEk(k, schur(mu, N), N), N) for mu in parts(d)}
if __name__ == '__main__':
    MAXN = int(sys.argv[1])
    mats = {}
    for n in range(1, MAXN+1):
        for k in range(1, n+1):
            d = n-k; mats[(k, d)] = Ematrix(k, d); print('done', k, d, flush=True)
    pickle.dump(mats, open(f'Emats_{MAXN}.pkl', 'wb'))
