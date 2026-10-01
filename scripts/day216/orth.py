"""Day 216: is {Psi(b_mu)} orthogonal for some multiplicative power-sum inner product <p_l,p_m> = delta z_l prod a_{l_i}?
(Triangular + orthogonal => Macdonald-type (VI.1/VI.4); for a_k=(1-q^k)/(1-u^k) it is P(q,u).) a_1=1 WLOG."""
import sys, pickle, itertools, sympy as sp
sys.path.insert(0, '/home/agent/projects/scripts/day214')
from ek_subset_engine import transpose, parts
from collections import Counter
s, t = sp.symbols('s t'); N = int(sys.argv[1]); out = open(sys.argv[2], 'w')
def log(*a):
    print(*a, flush=True); print(*a, file=out, flush=True)
PSI = pickle.load(open('/home/agent/projects/scripts/day216/psi_N5.pkl', 'rb'))
a = {1: sp.Integer(1)}; A = sp.symbols('a1:10')
def p_in_m(lam, n):  # p_lam = sum_nu X[lam,nu] m_nu, via n variables
    xs = sp.symbols(f'x1:{n+1}'); f = sp.Poly(sp.prod([sum(x**k for x in xs) for k in lam]), *xs); d = {}
    for mon, c in f.terms():
        if list(mon) == sorted(mon, reverse=True): d[tuple(x for x in mon if x > 0)] = c
    return d
def z(lam):
    c = Counter(lam); return sp.prod([k**v*sp.factorial(v) for k, v in c.items()])
for n in range(2, N+1):
    P = list(parts(n)); X = sp.Matrix([[p_in_m(l, n).get(nu, 0) for nu in P] for l in P])
    Xi = X.inv()  # m_nu = sum_l Xi[nu,l] p_l
    ak = {**a, n: A[n-1]}
    Z = sp.diag(*[z(l)*sp.prod([ak[k] for k in l]) for l in P])
    vecs = [sp.Matrix([[PSI[mu].get(nu, 0) for nu in P]]) * Xi for mu in P]  # p-coords (row)
    eqs = []
    for i in range(len(P)):
        for j in range(i+1, len(P)):
            eqs.append(sp.factor(sp.together((vecs[i]*Z*vecs[j].T)[0, 0])))
    sol = sp.solve(eqs[0] if n == 2 else eqs, A[n-1], dict=True)
    log(f'n={n}: #orthogonality equations {len(eqs)}, unknown a_{n}; solutions: {sol}')
    if not sol:
        # show the individual solutions per equation
        for i, eq in enumerate(eqs):
            log('   eq', i, 'alone gives a_n =', [sp.factor(x) for x in sp.solve(eq, A[n-1])])
        break
    a[n] = sp.factor(sol[0][A[n-1]])
    q, u = sp.symbols('q u')
    log(f'   a_{n} = {a[n]}')
