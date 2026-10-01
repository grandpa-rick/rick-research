"""Day 216: allow the full transport freedom theta_gamma: e_k -> g_k e_k (Psi unique up to this; c_k normalization).
Ask: exist g_k, a_k with {theta Psi(b_mu)}_{mu |- n} pairwise orthogonal under <p_l,p_m> = delta z_l prod a_{l_i}, for n=2..4?
Any P/Q/J (any q,u), H~ (= p-rescaled J), omega-twists, indexed by mu or mu', are orthogonal for SOME multiplicative a,
and p-rescalings preserve 'orthogonal for some multiplicative a'. Done at fixed rational (s,t) (a kill at a generic point kills the family)."""
import sys, pickle, itertools, sympy as sp
sys.path.insert(0, '/home/agent/projects/scripts/day214')
from ek_subset_engine import transpose, parts, e
from collections import Counter
s, t = sp.symbols('s t'); out = open(sys.argv[2], 'w'); NMAX = int(sys.argv[1])
S0, T0 = sp.Rational(sys.argv[3]), sp.Rational(sys.argv[4])
def log(*a):
    print(*a, flush=True); print(*a, file=out, flush=True)
PSI = pickle.load(open('/home/agent/projects/scripts/day216/psi_N5.pkl', 'rb'))
g = sp.symbols('g1:7'); a = sp.symbols('a1:7')
def mon_in(f, n, keys):
    xs = sp.symbols(f'x1:{n+1}'); P = sp.Poly(sp.expand(f), *xs); d = {}
    for mon, c in P.terms():
        if list(mon) == sorted(mon, reverse=True): d[tuple(x for x in mon if x > 0)] = c
    return [d.get(k, 0) for k in keys]
def z(lam):
    c = Counter(lam); return sp.prod([k**v*sp.factorial(v) for k, v in c.items()])
eqs = []
for n in range(2, NMAX+1):
    P = list(parts(n)); xs = sp.symbols(f'x1:{n+1}')
    pm = sp.Matrix([mon_in(sp.prod([sum(x**k for x in xs) for k in l]), n, P) for l in P])  # p in m
    em = sp.Matrix([mon_in(sp.prod([e(k, xs) for k in l]), n, P) for l in P])           # e in m
    E2P = em*pm.inv()   # e_l = sum E2P[l,j] p_j
    M2E = em.inv()      # m_nu = sum M2E[nu,l] e_l
    Z = sp.diag(*[z(l)*sp.prod([a[k-1] for k in l]) for l in P])
    vecs = []
    for mu in P:
        mrow = sp.Matrix([[sp.sympify(PSI[mu].get(nu, 0)).subs({s: S0, t: T0}) for nu in P]])
        erow = mrow*M2E
        erow = sp.Matrix([[erow[0, i]*sp.prod([g[k-1] for k in l]) for i, l in enumerate(P)]])
        vecs.append(erow*E2P)
    for i in range(len(P)):
        for j in range(i+1, len(P)):
            eqs.append(sp.expand((vecs[i]*Z*vecs[j].T)[0, 0]))
    unk = [g[k] for k in range(1, n)] + [a[k] for k in range(1, n)]
    E = [x.subs({g[0]: 1, a[0]: 1}) for x in eqs]
    # require nonzero g's and a's: saturate by adding w*prod(unk)-1
    w = sp.Symbol('w'); E2 = E + [w*sp.prod(unk) - 1]
    G = sp.groebner(E2, *unk, w, order='grevlex')
    log(f'(s,t)=({S0},{T0}) n<= {n}: #eqs {len(E)}, unknowns {unk}; Groebner basis == [1]? {list(G.exprs) == [1]}; size {len(G.exprs)}')
    if list(G.exprs) == [1]: break
    if n == 2 or len(G.exprs) < 8: log('   GB:', G.exprs)
