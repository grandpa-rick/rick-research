"""Day 216b: check (N): E_k P_nu = t^{-C(k,2)} sum_lam c_{lam/nu} (T_lam/T_nu) P_lam,
P = Macdonald P(x; q=s, tau=1/t) in m variables (D_1 eigenvectors), T_lam = t^{n(lam)} s^{n(lam')},
c from e_k P_nu = sum c P_lam.  Exact rationals, numeric s,t.  usage: N_check.py s t N"""
import sys, itertools, sympy as sp
sys.path.insert(0, '/home/agent/projects/scripts/day214')
from ek_subset_engine import Ek, e, parts, transpose, nstat
s = sp.Rational(sys.argv[1]); t = sp.Rational(sys.argv[2]); N = int(sys.argv[3])
tau = 1/t
def mono(kap, xs):
    kap = list(kap)+[0]*(len(xs)-len(kap))
    return sum(sp.prod([x**a for x, a in zip(xs, p)]) for p in set(itertools.permutations(kap)))
def mcoeffs(f, xs):
    P = sp.Poly(sp.expand(f), *xs); d = {}
    for mon, c in P.terms():
        if list(mon) == sorted(mon, reverse=True): d[tuple(a for a in mon if a > 0)] = c
    return d
def D1(f, xs):
    m = len(xs); r = 0
    for i in range(m):
        A = sp.prod([(tau*xs[i]-xs[j])/(xs[i]-xs[j]) for j in range(m) if j != i])
        r += A*f.subs(xs[i], s*xs[i])
    return sp.expand(sp.cancel(sp.together(r)))
def dominates(a, b):
    sa = sb = 0
    for i in range(max(len(a), len(b))):
        sa += a[i] if i < len(a) else 0; sb += b[i] if i < len(b) else 0
        if sa < sb: return False
    return True
Pcache = {}
def macP(nu, xs):
    key = (nu, len(xs))
    if key in Pcache: return Pcache[key]
    if not nu: return sp.Integer(1)
    m = len(xs); n = sum(nu)
    lows = [k for k in parts(n) if len(k) <= m and dominates(nu, k) and k != nu]
    cs = sp.symbols(f'c0:{len(lows)+1}')
    f = mono(nu, xs)+sum(c*mono(k, xs) for c, k in zip(cs, lows))
    ev = sum(s**(nu[i] if i < len(nu) else 0)*tau**(m-1-i) for i in range(m))
    g = sp.expand(D1(f, xs)-ev*f)
    eqs = list(mcoeffs(g, xs).values())
    sol = sp.solve(eqs, cs[:len(lows)], dict=True)[0] if lows else {}
    r = sp.expand(f.subs(sol)); Pcache[key] = r; return r
def expandP(f, xs):
    out = {}; f = sp.expand(f)
    while f != 0:
        d = mcoeffs(f, xs); lead = max(d); c = d[lead]
        out[lead] = c; f = sp.expand(f-c*macP(lead, xs))
    return out
T = lambda l: t**nstat(l)*s**nstat(transpose(l)) if l else 1
bad = 0
for n in range(0, N):
    for k in range(1, N-n+1):
        m = n+k; xs = sp.symbols(f'x1:{m+1}')
        for nu in parts(n):
            Pn = macP(nu, xs)
            lhs = expandP(Ek(Pn, k, xs, s, t), xs)
            ek = expandP(sp.expand(e(k, xs)*Pn), xs)
            pred = {l: t**(-sp.binomial(k, 2))*c*T(l)/T(nu) for l, c in ek.items()}
            ok = all(sp.simplify(lhs.get(l, 0)-pred.get(l, 0)) == 0 for l in set(lhs) | set(pred))
            if not ok: bad += 1
            print(n, k, nu, 'OK' if ok else 'FAIL', flush=True)
print('bad', bad)
