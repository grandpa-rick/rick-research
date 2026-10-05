"""Wake 223: B(e_a,e_b) = D_a(e_b) (Day 220 Thm 1(c): M_{ab} = D_a(e_b), D_k = sum_{|A|=k} c_A X_A Delta_A),
exact symbolic t, N = a+b variables, expanded fully in the e-basis. Grade: computed."""
import sys, itertools, pickle, time
from sympy.polys.rings import ring
from sympy import ZZ, QQ, Matrix, symbols, factor, cancel, Poly
t = symbols('t')
def parts(n, m=None):
    if m is None: m = n
    if n == 0: yield (); return
    for k in range(min(n, m), 0, -1):
        for p in parts(n-k, k): yield (k,)+p
def Dk_el(k, l):
    N = k+l
    Rg, *g = ring(['t']+[f'x{i}' for i in range(N)], ZZ); T, xs = g[0], g[1:]
    V = Rg(1)
    for i in range(N):
        for j in range(i+1, N): V *= xs[i]-xs[j]
    # Delta_A e_l = sum_{|S|=l} |A cap S| X_S
    subsetsl = list(itertools.combinations(range(N), l))
    tot = Rg(0)
    for A in itertools.combinations(range(N), k):
        Bc = [j for j in range(N) if j not in A]
        sign = (-1)**sum(1 for i in A for j in Bc if i > j); term = Rg(sign)
        for i in range(N):
            for j in range(i+1, N):
                if (i in A) == (j in A): term *= xs[i]-xs[j]
        for i in A:
            term *= xs[i]
            for j in Bc: term *= xs[i]-T*xs[j]
        As = set(A); F = Rg(0)
        for S in subsetsl:
            c = len(As.intersection(S))
            if c:
                m = Rg(c)
                for i in S: m *= xs[i]
                F += m
        tot += term*F
    q, r = tot.div(V); assert r == 0
    return q, N
def to_e(q, n):
    P = list(parts(n)); N = n
    # e_mu -> m_lam matrix (integers): coefficient of x^lam in e_mu
    from itertools import combinations
    def ecoef(mu, lam):  # number of 0-1 matrices with row sums mu col sums lam
        from functools import lru_cache
        lam = tuple(lam)+(0,)*(N-len(lam))
        @lru_cache(None)
        def go(i, rem):
            if i == len(mu): return 1 if all(r == 0 for r in rem) else 0
            s = 0
            for S in combinations(range(N), mu[i]):
                if all(rem[j] > 0 for j in S):
                    r = list(rem)
                    for j in S: r[j] -= 1
                    s += go(i+1, tuple(r))
            return s
        return go(0, lam)
    M = Matrix(len(P), len(P), lambda i, j: ecoef(P[i], P[j]))  # rows e_mu, cols m_lam
    Minv = M.inv()
    d = q.to_dict(); mvec = []
    for lam in P:
        key = tuple(lam)+(0,)*(N-len(lam)); c = 0
        for m, v in d.items():
            if m[1:] == key: c += int(v)*t**m[0]
        mvec.append(c)
    out = {}
    for i, mu in enumerate(P):
        c = cancel(sum(mvec[j]*Minv[j, i] for j in range(len(P))))
        if c != 0: out[mu] = c
    return out
if __name__ == '__main__':
    nmax = int(sys.argv[1]); res = {}
    for n in range(2, nmax+1):
        for b in range(1, n//2+1):
            a = n-b; t0 = time.time()
            q, N = Dk_el(a, b); E = to_e(q, n); res[(a, b)] = E
            print(f'B(e{a},e{b}) [{time.time()-t0:.1f}s]:', flush=True)
            for mu, c in E.items(): print(f'   e{mu}: {factor(c)}', flush=True)
    pickle.dump(res, open(f'bfull_n{nmax}.pkl', 'wb')); print('DONE')
