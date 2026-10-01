"""Day 216: forced transport map Psi (Psi E_k = c_k e_k Psi, c_k = t^{-C(k,2)}): Psi(b_mu) in e- and m-bases;
test triangularity and compare with Macdonald P_{mu'}(x;q,1/t)."""
import sys, pickle, itertools, sympy as sp
sys.path.insert(0, '/home/agent/projects/scripts/day214')
from ek_subset_engine import e, transpose, nstat, parts, dominates
s, t, q = sp.symbols('s t q')
N = int(sys.argv[1]); mats = pickle.load(open('/home/agent/projects/scripts/day216/mats_N5.pkl', 'rb'))
out = open(sys.argv[2], 'w')
def log(*a):
    print(*a, flush=True); print(*a, file=out, flush=True)
def apply(k, vec):  # vec: dict partition->coeff in b-basis, degree n
    res = {}
    for mu, c in vec.items():
        n = sum(mu)
        for nu, d in mats[(k, n)][mu].items(): res[nu] = res.get(nu, 0) + c*d
    return {a: sp.factor(b) for a, b in res.items() if sp.cancel(b) != 0}
def m_expand(f, xs):
    P = sp.Poly(sp.expand(f), *xs); outd = {}
    for mon, c in P.terms():
        if list(mon) == sorted(mon, reverse=True):
            outd[tuple(a for a in mon if a > 0)] = sp.factor(c)
    return outd
PSI = {}
for n in range(1, N+1):
    P = list(parts(n)); xs = sp.symbols(f'x1:{n+1}')
    G = sp.zeros(len(P))
    for i, lam in enumerate(P):
        v = {(): sp.Integer(1)}
        for k in reversed(lam): v = apply(k, v)
        for j, mu in enumerate(P): G[i, j] = v.get(mu, 0)
    Gi = G.inv()  # b_mu = sum_lam Gi[mu,lam] E_lam(1)
    log(f'==== n={n}; det G =', sp.factor(G.det()))
    for j, mu in enumerate(P):
        f = sum(sp.cancel(Gi[j, i])*sp.prod([t**(-sp.binomial(p, 2)) for p in lam])*sp.prod([e(p, xs) for p in lam]) for i, lam in enumerate(P))
        f = sp.together(sp.expand(f))
        md = m_expand(sp.cancel(f*1), xs) if False else None
        num, den = sp.fraction(sp.cancel(f))
        mdn = m_expand(num, xs); mdict = {a: sp.factor(b/den) for a, b in mdn.items()}
        PSI[mu] = mdict
        lead = transpose(mu)
        tri = all(dominates(lead, nu) for nu in mdict)
        log(f' Psi(b_{mu}) in m-basis (expected lead m_{lead}); triangular below {lead}: {tri}')
        for nu, c in sorted(mdict.items(), reverse=True): log('     ', nu, ':', c)
pickle.dump(PSI, open(f'/home/agent/projects/scripts/day216/psi_N{N}.pkl', 'wb'))
