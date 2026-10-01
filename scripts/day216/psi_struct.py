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
RES = {}
for n in range(1, NMAX+1):
    P, A, E, HLT, S = bases(n)
    log(f'################ n={n}  partitions {P}')
    log('sanity HL P_(n)(x;T) row:', [sp.factor(c) for c in HLT[0, :]])
    B = sp.Matrix.vstack(*[(t**(-nstat(transpose(nu)))*HLT[P.index(transpose(nu)), :].subs(T, 1/t)).applyfunc(sp.cancel) for nu in P])
    for mu in P:
        vec = sp.Matrix([[PSI[mu].get(l, 0) for l in P]])
        cB = coords(vec, B); cE = coords(vec, E); cS = coords(vec, S)
        RES[mu] = dict(B=cB, E=cE, S=cS)
        log(f'== Psi_s(b_{mu})')
        log('  s=0 equals B_mu ?', all(sp.cancel(cB[i].subs(s, 0) - (1 if P[i] == mu else 0)) == 0 for i in range(len(P))))
        log('  (i) HL B_nu coeffs:'); [log('     ', P[i], ':', cB[i]) for i in range(len(P)) if cB[i] != 0]
        log('  (ii) e_nu coeffs:'); [log('     ', P[i], ':', cE[i]) for i in range(len(P)) if cE[i] != 0]
        log('  (iii) Schur coeffs:'); [log('     ', P[i], ':', cS[i]) for i in range(len(P)) if cS[i] != 0]
        lim = [sp.factor(sp.limit(sp.cancel(cS[i].subs(t, 1/u)*u**0), u, 0)) if cS[i] != 0 else 0 for i in range(len(P))]
        log('  (iii\') Schur coeffs at u=1/t->0:', {str(P[i]): str(lim[i]) for i in range(len(P)) if lim[i] != 0})
pickle.dump(RES, open(f'/home/agent/projects/scripts/day216/psi_struct_N{NMAX}.pkl', 'wb'))
