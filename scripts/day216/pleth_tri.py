"""Day 216: for plethystic alphabets A = eps*(1-a)/(1-b) (a,b monomials in s,t), test whether the family
G_mu = Psi_s(b_mu)[X A] is m-triangular (support of G_mu in an interval below or above its leading term)
-- necessary condition for 'Psi(b_mu) = HL/Macdonald-type basis after plethysm'."""
import sys, pickle, itertools, sympy as sp
sys.path.insert(0, '/home/agent/projects/scripts/day214')
from ek_subset_engine import transpose, nstat, parts, dominates
from collections import Counter
s, t = sp.symbols('s t'); u = 1/t
NMAX = int(sys.argv[1]); out = open(sys.argv[2], 'w')
def log(*a):
    print(*a, flush=True); print(*a, file=out, flush=True)
PSI = pickle.load(open('/home/agent/projects/scripts/day216/psi_N5.pkl', 'rb'))
def mexp(f, xs):
    Pl = sp.Poly(sp.expand(f), *xs); d = {}
    for mon, c in Pl.terms():
        if list(mon) == sorted(mon, reverse=True): d[tuple(a for a in mon if a > 0)] = c
    return d
mons = {'0': 0, 's': s, 't': t, 'u': u, 'st': s*t, 'su': s*u, 's2': s**2, 't2': t**2, 'u2': u**2, 's2t': s**2*t, 's2u': s**2*u}
alph = [(eps, a, b) for eps in (1, -1) for a in mons for b in mons if a != b]
mats = {}
for n in range(2, NMAX+1):
    P = list(parts(n)); xs = sp.symbols(f'x1:{n+1}')
    Am = sp.Matrix([[mexp(sp.prod([sum(x**k for x in xs) for k in l]), xs).get(m, 0) for m in P] for l in P])
    mats[n] = (P, Am, Am.inv())
alive = set(alph); report = {}
for n in range(2, NMAX+1):
    P, Am, Ai = mats[n]
    psip = {mu: sp.Matrix([[PSI[mu].get(m, 0) for m in P]])*Ai for mu in P}
    for (eps, a, b) in sorted(alive):
        A, B = mons[a], mons[b]
        sup = {}
        for mu in P:
            v = sp.Matrix([[psip[mu][i]*sp.prod([eps**(k-1)*(1-A**k)/(1-B**k) for k in l]) for i, l in enumerate(P)]])
            w = (v*Am).applyfunc(lambda c: sp.cancel(c))
            sup[mu] = [P[i] for i in range(len(P)) if w[i] != 0]
        # triangular: exists ordering where each G_mu has a unique max (or min) in dominance, distinct across mu, all others below (above)
        def tri(direction):
            leads = []
            for mu in P:
                S = sup[mu]
                cand = [l for l in S if all((dominates(l, m) if direction == 'down' else dominates(m, l)) for m in S)]
                if not cand: return False
                leads.append(cand[0])
            return len(set(leads)) == len(P)
        dn, up = tri('down'), tri('up')
        if not (dn or up): alive.discard((eps, a, b))
        else: report[(eps, a, b)] = (dn, up, {str(mu): len(sup[mu]) for mu in P})
    log(f'n={n}: triangular survivors {len(alive)}')
    for g in sorted(alive): log('   ', g, report[g])
