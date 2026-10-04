"""Wake 221: cross-validate symbolic history leads against the direct subset-formula star engine (Day 220 val_n6.py
engine, s symbolic, t=3/5), n<=5, all coarsening pairs. fast.py itself is hardwired to t=1/s, so we use its general-t twin."""
import sys, itertools, functools, pickle
from sympy.polys.rings import ring
from sympy import QQ, Matrix, Symbol, Rational, expand, Poly, cancel, symbols
T = Rational(3, 5); S = Symbol('s'); tt = symbols('t')
res = pickle.load(open('leads_n8.pkl', 'rb'))
def parts(n, m=None):
    if m is None: m = n
    if n == 0: yield (); return
    for k in range(min(n, m), 0, -1):
        for p in parts(n-k, k): yield (k,)+p
tot = ok = 0
for n in range(2, 6):
    N = n
    Rg, *g = ring(['s']+[f'x{i}' for i in range(N)], QQ); s, xs = g[0], g[1:]
    V = Rg(1)
    for i in range(N):
        for j in range(i+1, N): V *= xs[i]-xs[j]
    def Ek(k, F):
        tot_ = Rg(0); Fd = F.to_dict()
        for A in itertools.combinations(range(N), k):
            B = [j for j in range(N) if j not in A]
            sign = (-1)**sum(1 for i in A for j in B if i > j); term = Rg(sign)
            for i in range(N):
                for j in range(i+1, N):
                    if (i in A) == (j in A): term *= xs[i]-xs[j]
            for i in A:
                term *= xs[i]
                for j in B: term *= xs[i]-T*xs[j]
            Fs = Rg.from_dict({(m[0]+sum(m[1+i] for i in A),)+m[1:]: c for m, c in Fd.items()})
            tot_ += term*Fs
        q, r = tot_.div(V); assert r == 0
        return q
    P = list(parts(n))
    def ek(k): return sum((functools.reduce(lambda a, b: a*b, [xs[i] for i in A], Rg(1)) for A in itertools.combinations(range(N), k)), Rg(0))
    def epoly(mu): return functools.reduce(lambda a, b: a*b, [ek(k) for k in mu], Rg(1))
    M = Matrix(len(P), len(P), lambda i, j: 0)
    for i, mu in enumerate(P):
        d = epoly(mu).to_dict()
        for j, lam in enumerate(P): M[i, j] = d.get((0,)+tuple(lam)+(0,)*(N-len(lam)), 0)
    Minv = M.inv()
    for lam in P:
        F = Rg(1)
        for k in reversed(lam): F = Ek(k, F)
        d = F.to_dict(); mvec = []
        for mu in P:
            key = tuple(mu)+(0,)*(N-len(mu))
            mvec.append(sum(QQ.to_sympy(v)*S**m[0] for m, v in d.items() if m[1:] == key))
        for i, mu in enumerate(P):
            if mu == lam or (lam, mu) not in res: continue
            c = expand(sum(mvec[j]*Minv[j, i] for j in range(len(P))))
            m = len(lam)-len(mu)
            coef = Poly(expand(c.subs(S, S+1)), S).coeff_monomial(S**m)
            low = [Poly(expand(c.subs(S, S+1)), S).coeff_monomial(S**j) for j in range(m)]
            H = res[(lam, mu)][0].subs(tt, T)
            good = coef == H and all(v == 0 for v in low); tot += 1; ok += good
            print(f'{lam} -> {mu}: engine [(s-1)^{m}] = {coef}, history = {H}, lower coeffs zero={all(v==0 for v in low)} {"OK" if good else "MISMATCH"}', flush=True)
print(f'ENGINE CHECK t=3/5 n<=5: {ok}/{tot}')
