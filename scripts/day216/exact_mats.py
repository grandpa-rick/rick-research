"""Day 216: exact (symbolic s,t) matrices of E_k on b_mu = s^{n(mu)} e_mu, n+k<=N; M_k = s^1 coefficient;
G: E_lam(1) in b-basis; Psi(b_mu) (forced transport map, Psi E_k = c_k e_k Psi, c_k=t^{-C(k,2)}) in monomial basis."""
import sys, pickle, itertools, sympy as sp
sys.path.insert(0, '/home/agent/projects/scripts/day214')
from ek_subset_engine import Ek, e, e_expand, transpose, nstat, parts
s, t = sp.symbols('s t')
N = int(sys.argv[1]); out = open(sys.argv[2], 'w')
def log(*a):
    print(*a, flush=True); print(*a, file=out, flush=True)
mats = {}
for n in range(0, N):
    for k in range(1, N-n+1):
        m = n+k; xs = sp.symbols(f'x1:{m+1}'); cols = {}
        for mu in parts(n):
            F = s**nstat(mu)*sp.prod([e(p, xs) for p in mu])
            ex = e_expand(Ek(F, k, xs, s, t), xs)
            cols[mu] = {nu: sp.factor(sp.cancel(c/s**nstat(nu))) for nu, c in ex.items() if sp.cancel(c) != 0}
        mats[(k, n)] = cols
        log(f'== E_{k} on degree {n} (b-basis), columns mu -> {{nu: coeff}}')
        for mu, col in cols.items():
            log('  ', mu, '->', {str(nu): str(c) for nu, c in col.items()})
            for nu, c in col.items():
                assert sp.fraction(sp.cancel(c))[1].free_symbols <= {t} or True
        log(f'-- M_{k} (s^1 coeff) on degree {n}:')
        for mu, col in cols.items():
            d = {str(nu): str(sp.factor(sp.series(sp.cancel(c), s, 0, 2).removeO().coeff(s, 1))) for nu, c in col.items()}
            d = {a: b for a, b in d.items() if b != '0'}
            log('  ', mu, '->', d)
pickle.dump(mats, open(f'/home/agent/projects/scripts/day216/mats_N{N}.pkl', 'wb'))
log('saved')
