"""Day 216: test Psi_s(b_mu) ∝ omega( P_mu(X; q=A, t=B)[X (1-C)/(1-D)] ) for a grid of (A,B,C,D).
Psi normalization as psi.py. Macdonald P via Gram-Schmidt (dominance total for n<=5)."""
import sys, pickle, itertools, sympy as sp
sys.path.insert(0, '/home/agent/projects/scripts/day214')
from ek_subset_engine import transpose, nstat, parts, dominates
from collections import Counter
s, t, q, T = sp.symbols('s t q T'); u = 1/t
NMAX = int(sys.argv[1]); out = open(sys.argv[2], 'w')
def log(*a):
    print(*a, flush=True); print(*a, file=out, flush=True)
PSI = pickle.load(open('/home/agent/projects/scripts/day216/psi_N5.pkl', 'rb'))
def mexp(f, xs):
    Pl = sp.Poly(sp.expand(f), *xs); d = {}
    for mon, c in Pl.terms():
        if list(mon) == sorted(mon, reverse=True): d[tuple(a for a in mon if a > 0)] = c
    return d
def zee(l):
    r = 1
    for k, m in Counter(l).items(): r *= k**m*sp.factorial(m)
    return r
cands = {'s': s, 'u': u, 't': t, '0': sp.Integer(0), 'su': s*u, 'st': s*t, '1/s': 1/s}
grid = []
for A in ['u', 's', 't', '0', 'su', 'st', '1/s']:
    for B in ['s', 'u', 't', '0', 'su', 'st', '1/s']:
        if A == B: continue
        for C in ['0', 's', 'u', 't', 'su', 'st']:
            for D in ['0', 's', 'u', 't', 'su', 'st']:
                if C == D and C != '0': continue
                grid.append((A, B, C, D))
alive = set(grid)
for n in range(2, NMAX+1):
    P = list(parts(n)); xs = sp.symbols(f'x1:{n+1}'); idx = {l: i for i, l in enumerate(P)}
    Amat = sp.Matrix([[mexp(sp.prod([sum(x**k for x in xs) for k in l]), xs).get(m, 0) for m in P] for l in P])  # p in m
    Ai = Amat.inv()
    D = sp.diag(*[zee(l)*sp.prod([(1-q**k)/(1-T**k) for k in l]) for l in P])
    Gm = Ai*D*Ai.T
    ip = lambda a, b: sp.cancel((a*Gm*b.T)[0, 0])
    order = sorted(P, key=lambda l: sum(1 for m in P if dominates(l, m)))
    res = {}
    for l in order:
        v = sp.zeros(1, len(P)); v[idx[l]] = 1
        for m in list(res): v = v - sp.cancel(ip(v, res[m])/ip(res[m], res[m]))*res[m]
        res[l] = v.applyfunc(sp.cancel)
    log(f'n={n}: Macdonald P computed')
    Pp = {l: (res[l]*Ai).applyfunc(sp.cancel) for l in P}  # p-coords
    psip = {mu: (sp.Matrix([[PSI[mu].get(m, 0) for m in P]])*Ai).applyfunc(sp.cancel) for mu in P}
    for g in sorted(alive):
        A, B, C, Dd = [cands[x] for x in g]; ok = True
        for mu in P:
            v = Pp[mu].subs({q: A, T: B}, simultaneous=True)
            w = [sp.cancel(v[i]*(-1)**(n-len(l))*sp.prod([(1-C**k)/(1-Dd**k) for k in l])) for i, l in enumerate(P)]
            ps = psip[mu]
            # ratio constant?
            ratios = set()
            for i in range(len(P)):
                if w[i] == 0 and ps[i] == 0: continue
                if w[i] == 0 or ps[i] == 0: ok = False; break
                ratios.add(sp.cancel(ps[i]/w[i]))
                if len(ratios) > 1: ok = False; break
            if not ok: break
        if not ok: alive.discard(g)
    log(f'  survivors after n={n}: {len(alive)}', sorted(alive)[:40])
