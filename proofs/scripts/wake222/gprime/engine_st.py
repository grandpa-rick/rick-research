"""Wake 222: exact c_{lam mu}(s,t) via the Day 214/220 subset-formula star engine (same Ek as day220/val_n6.py and
wake221/lead/engine_check.py), but with BOTH s and t symbolic (ring QQ[s,t,x_1..x_N]). c_{lam mu} = coefficient of e_mu in
e*_lam = E_{lam_1}...E_{lam_l}(1) (applied with reversed(lam), as in the existing engine). Then Lead_{lam mu}(t) =
[(s-1)^v] c_{lam mu}, v = (s-1)-adic valuation over QQ(t). Saves dict (lam,mu) -> sympy poly c(s,t) to cst_n{n}.pkl.
Grade: computed."""
import sys, itertools, functools, pickle, time
from sympy.polys.rings import ring
from sympy import QQ, Matrix, symbols, expand
n = int(sys.argv[1]); N = n
S, Tt = symbols('s t')
Rg, *g = ring(['s', 't']+[f'x{i}' for i in range(N)], QQ); s, T, xs = g[0], g[1], g[2:]
V = Rg(1)
for i in range(N):
    for j in range(i+1, N): V *= xs[i]-xs[j]
def Ek(k, F):
    tot = Rg(0); Fd = F.to_dict()
    for A in itertools.combinations(range(N), k):
        B = [j for j in range(N) if j not in A]
        sign = (-1)**sum(1 for i in A for j in B if i > j); term = Rg(sign)
        for i in range(N):
            for j in range(i+1, N):
                if (i in A) == (j in A): term *= xs[i]-xs[j]
        for i in A:
            term *= xs[i]
            for j in B: term *= xs[i]-T*xs[j]
        Fs = Rg.from_dict({(m[0]+sum(m[2+i] for i in A),)+m[1:]: c for m, c in Fd.items()})
        tot += term*Fs
    q, r = tot.div(V); assert r == 0
    return q
def parts(n, m=None):
    if m is None: m = n
    if n == 0: yield (); return
    for k in range(min(n, m), 0, -1):
        for p in parts(n-k, k): yield (k,)+p
P = list(parts(n))
def ek(k): return sum((functools.reduce(lambda a, b: a*b, [xs[i] for i in A], Rg(1)) for A in itertools.combinations(range(N), k)), Rg(0))
def epoly(mu): return functools.reduce(lambda a, b: a*b, [ek(k) for k in mu], Rg(1))
M = Matrix(len(P), len(P), lambda i, j: 0)
for i, mu in enumerate(P):
    d = epoly(mu).to_dict()
    for j, lam in enumerate(P): M[i, j] = d.get((0, 0)+tuple(lam)+(0,)*(N-len(lam)), 0)
Minv = M.inv()
res = {}
SKIP1 = len(sys.argv) > 2 and sys.argv[2] == 'skip1n'  # 1^n: every mu is a coarsening (covered by wake221 history data)
for lam in P:
    if SKIP1 and lam == (1,)*n: continue
    t0 = time.time()
    F = Rg(1)
    for k in reversed(lam): F = Ek(k, F)
    d = F.to_dict(); mvec = []
    for mu in P:
        key = tuple(mu)+(0,)*(N-len(mu))
        mvec.append(sum((QQ.to_sympy(v)*S**m[0]*Tt**m[1] for m, v in d.items() if m[2:] == key), 0))
    for i, mu in enumerate(P):
        res[(lam, mu)] = expand(sum(mvec[j]*Minv[j, i] for j in range(len(P))))
    print(f'{lam} done {time.time()-t0:.1f}s', flush=True)
pickle.dump(res, open(f'cst_n{n}{"_skip1n" if SKIP1 else ""}.pkl', 'wb'))
print('DONE')
