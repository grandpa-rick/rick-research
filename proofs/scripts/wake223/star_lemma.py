"""Wake 223b Task 1: star lemma. C = [e_{a+M}] E_a^{(p)}(e_{m_1}...e_{m_p}), E_a^{(p)} = sum_{|A|=a} c_A X_A binom(Delta_A,p),
N = a+M variables, exact symbolic t. Test C / (pref(a;m) prod w(a,m_i)) == const. Grade: computed.
Usage: python star_lemma.py a m1 [m2 [m3]]   (p = number of m's)"""
import sys, itertools, time
from math import comb
from sympy.polys.rings import ring
from sympy import ZZ, symbols, factor, cancel
from bfull import to_e
t = symbols('t')
def esym(Rg, xs, k):
    s = Rg(0)
    for S in itertools.combinations(range(len(xs)), k):
        m = Rg(1)
        for i in S: m *= xs[i]
        s += m
    return s
def apply_op(a, ms, N, p):
    Rg, *g = ring(['t']+[f'x{i}' for i in range(N)], ZZ); T, xs = g[0], g[1:]
    V = Rg(1)
    for i in range(N):
        for j in range(i+1, N): V *= xs[i]-xs[j]
    F = Rg(1)
    for m in ms: F *= esym(Rg, xs, m)
    Fd = F.to_dict(); tot = Rg(0)
    for A in itertools.combinations(range(N), a):
        Bc = [j for j in range(N) if j not in A]
        sign = (-1)**sum(1 for i in A for j in Bc if i > j); term = Rg(sign)
        for i in range(N):
            for j in range(i+1, N):
                if (i in A) == (j in A): term *= xs[i]-xs[j]
        for i in A:
            term *= xs[i]
            for j in Bc: term *= xs[i]-T*xs[j]
        G = Rg.from_dict({mm: c*comb(sum(mm[1+i] for i in A), p) for mm, c in Fd.items() if comb(sum(mm[1+i] for i in A), p)})
        tot += term*G
    q, r = tot.div(V); assert r == 0
    return q
if __name__ == '__main__':
    a = int(sys.argv[1]); ms = [int(x) for x in sys.argv[2:]]; p = len(ms); M = sum(ms); n = a+M
    t0 = time.time()
    q = apply_op(a, ms, n, p); E = to_e(q, n); C = E.get((n,), 0)
    pref = (1-t**n)/(1-t**a)
    for m in ms: pref = pref/(1-t**m)
    W = 1
    for m in ms: W *= (t**(a*m)-1)
    ratio = cancel(C/(pref*W))
    print(f'p={p} a={a} m={tuple(ms)} n={n} [{time.time()-t0:.1f}s]: C={factor(C)}  ratio={ratio}', flush=True)
