"""Day 216: structure of Psi_s(b_mu) (normalization of psi.py: Psi(E_lam(1)) = prod t^{-C(lam_i,2)} e_lam).
Expand in (i) HL basis B_nu = t^{-n(nu')} P_{nu'}(x;1/t), (ii) e-basis, (iii) Schur basis (and u=1/t->0 limit)."""
import sys, pickle, itertools, sympy as sp
sys.path.insert(0, '/home/agent/projects/scripts/day214')
from ek_subset_engine import transpose, nstat, parts, dominates
s, t, u, T = sp.symbols('s t u T')
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
    from collections import Counter
    r = 1
    for k, m in Counter(l).items(): r *= k**m*sp.factorial(m)
    return r
BASES = {}
def bases(n):
    if n in BASES: return BASES[n]
    P = list(parts(n)); xs = sp.symbols(f'x1:{n+1}'); idx = {l: i for i, l in enumerate(P)}
    def row(f):
        d = mexp(f, xs); return sp.Matrix([[d.get(l, 0) for l in P]])
    A = sp.Matrix.vstack(*[row(sp.prod([sum(x**k for x in xs) for k in l])) for l in P])  # p in m
    E = sp.Matrix.vstack(*[row(sp.prod([sum(sp.prod(c) for c in itertools.combinations(xs, k)) for k in l])) for l in P])  # e in m
    Ai = A.inv()
    def HL(Tv):  # rows: P_lam(x;Tv) in m-basis, Gram-Schmidt from bottom (dominance total for n<=5)
        D = sp.diag(*[zee(l)*sp.prod([1/(1-Tv**k) for k in l]) for l in P])
        Gm = Ai*D*Ai.T
        ip = lambda a, b: sp.cancel((a*Gm*b.T)[0, 0])
        order = sorted(P, key=lambda l: -sum(1 for m in P if dominates(l, m)))[::-1]  # bottom first
        order = sorted(P, key=lambda l: sum(1 for m in P if dominates(l, m)))
        res = {}
        for l in order:
            v = sp.zeros(1, len(P)); v[idx[l]] = 1
            for m in list(res):
                v = v - sp.cancel(ip(v, res[m])/ip(res[m], res[m]))*res[m]
            res[l] = v.applyfunc(sp.cancel)
        return sp.Matrix.vstack(*[res[l] for l in P])
    HLT = HL(T); S = HLT.subs(T, 0)
    BASES[n] = (P, A, E, HLT, S); return BASES[n]
def coords(vec, M):  # vec row in m; M rows basis in m -> coefficients
    return (vec*M.inv()).applyfunc(lambda c: sp.factor(sp.cancel(c)))

def nn(l): return nstat(l)
def qint(k): return sum(t**i for i in range(k))
def qfac(k): return sp.prod([qint(i) for i in range(1, k+1)])
RES = pickle.load(open('/home/agent/projects/scripts/day216/psi_struct_N5.pkl', 'rb'))
allok = {'a': True, 'b': True, 'c': True, 'deg': True}
for n in range(1, NMAX+1):
    P, A, E, HLT, S = bases(n)
    K = (S*HLT.inv()).applyfunc(sp.cancel)  # s_lam = sum_mu K[lam,mu] P_mu(T): K = Kostka-Foulkes K_{lam mu}(T)
    log(f'#### n={n}')
    for mu in P:
        cB, cE, cS = RES[mu]['B'], RES[mu]['E'], RES[mu]['S']
        # (a) B_(n) coefficient
        pred = s**nn(mu)*qfac(n)/sp.prod([qfac(p) for p in mu])
        oka = sp.cancel(cB[0]-pred) == 0; allok['a'] &= oka
        # (b) t^{n(mu')} Psi -> omega Q'_mu(X;s): coefficient of s_{lam'} equals K_{lam,mu}(s)
        okb = True
        for i, lam in enumerate(P):
            j = P.index(transpose(lam))
            lim = sp.limit(sp.cancel(cS[j]*t**nn(transpose(mu))).subs(t, 1/u), u, 0)
            if sp.cancel(lim - K[i, P.index(mu)].subs(T, s)) != 0: okb = False
        allok['b'] &= okb
        # (c) (1-s)-valuation of e-coefficients vs l(mu)-l(nu); (deg) t-degree of B coeffs
        vals = {}
        for i, nu in enumerate(P):
            c = cE[i]
            if c == 0: continue
            num = sp.numer(sp.cancel(c)); v = 0
            while sp.rem(num, s-1, s) == 0: num = sp.quo(num, s-1, s); v += 1
            vals[nu] = v
            if v != len(mu)-len(nu): allok['c'] = False
        degs = {}
        for i, nu in enumerate(P):
            if cB[i] == 0: continue
            pl = sp.Poly(sp.expand(cB[i]), t); d = pl.degree(); top = sp.factor(pl.coeff_monomial(t**d)); bot = sp.factor(pl.coeff_monomial(1))
            degs[nu] = (d, nn(transpose(nu))-nn(transpose(mu)), top, bot)
            if d != nn(transpose(nu))-nn(transpose(mu)): allok['deg'] = False
        log(f' mu={mu}: (a) B_(n)-coef = s^n(mu)[n]!/prod[mu_i]! : {oka}; (b) t->inf limit = omega Qprime_mu(X;s): {okb}; (c) (1-s)-val of e-coefs {vals}')
        for nu, (d, pd, top, bot) in degs.items(): log(f'     B_{nu}: t-deg {d} (pred n(nu\')-n(mu\')={pd}), top coef {top}, t^0 coef {bot}')
log('ALL:', allok)
