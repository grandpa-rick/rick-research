"""Day 217 kill test: at t=1/s, is s_lam * s_mu = sum_nu c^nu_{lam,mu} s^{c(nu)-c(lam)-c(mu)} s_nu ?
E_k F = sum_{|A|=k} prod_{i in A, j notin A} (x_i - t x_j)/(x_i - x_j) X_A F(X_{A^c}, s X_A); e_k * F := E_k F.
Schur expansion via alternant: coefficient of x^{lam+delta} in Vandermonde*f."""
import sys, itertools, sympy as sp
from sympy.combinatorics.permutations import Permutation
s = sp.Symbol('s')
t = 1/s   # the specialisation under test
out = open(sys.argv[1], 'w')
def log(*a):
    print(*a, flush=True); print(*a, file=out, flush=True)
DOM = sp.QQ.frac_field(s)
def parts(n, m=None):
    if m is None: m = n
    if n == 0: yield (); return
    for k in range(min(n, m), 0, -1):
        for p in parts(n-k, k): yield (k,)+p
def content(l): return sum(j-i for i, r in enumerate(l) for j in range(r))
def setup(N):
    xs = sp.symbols(f'x1:{N+1}')
    V = sp.Poly(sp.prod([xs[i]-xs[j] for i in range(N) for j in range(i+1, N)]), *xs, domain=DOM)
    return xs, V
def schur(lam, xs, V):
    N = len(xs); lam = list(lam)+[0]*(N-len(lam))
    M = sp.Matrix(N, N, lambda i, j: xs[i]**(lam[j]+N-1-j))
    num = sp.Poly(M.det(method='berkowitz'), *xs, domain=DOM)
    q, r = num.div(V); assert r.is_zero; return q
def to_schur(f, N):  # f Poly (symmetric); returns dict lam->coeff
    g = f*V_[N]; d = {}
    for mon, c in g.terms():
        lam = [mon[i]-(N-1-i) for i in range(N)]
        if all(lam[i] >= lam[i+1] for i in range(N-1)) and lam[-1] >= 0:
            d[tuple(a for a in lam if a > 0)] = sp.factor(DOM.to_sympy(c) if not isinstance(c, sp.Basic) else c)
    return d
def Ek(k, F, xs, V):
    N = len(xs); tot = sp.Poly(0, *xs, domain=DOM)
    for A in itertools.combinations(range(N), k):
        B = [j for j in range(N) if j not in A]
        sign = (-1)**sum(1 for i in A for j in B if i > j)
        rest = sp.prod([xs[i]-xs[j] for i in range(N) for j in range(i+1, N) if (i in A) == (j in A)])
        num = sp.prod([xs[i]-t*xs[j] for i in A for j in B])*sp.prod([xs[i] for i in A])
        sub = {xs[i]: s*xs[i] for i in A}
        Fs = sp.Poly(F.as_expr().subs(sub, simultaneous=True), *xs, domain=DOM)
        tot += sp.Poly(sign*rest*num, *xs, domain=DOM)*Fs
    q, r = tot.div(V); assert r.is_zero, 'E_k F not polynomial'
    return q
V_ = {}
def lr(lam, mu, N, xs):
    return to_schur(schur(lam, xs, V_[N])*schur(mu, xs, V_[N]), N)
def predicted(lam, mu, N, xs):
    return {nu: c*s**(content(nu)-content(lam)-content(mu)) for nu, c in lr(lam, mu, N, xs).items()}
def compare(got, pred):
    keys = set(got) | set(pred); bad = []
    for k in keys:
        if sp.simplify(got.get(k, 0)-pred.get(k, 0)) != 0: bad.append((k, got.get(k, 0), pred.get(k, 0)))
    return bad
# ---- Test 2: Pieri
mode = sys.argv[2] if len(sys.argv) > 2 else 'pieri'
if mode == 'pieri':
    total = ok = 0
    for k in (1, 2):
        for n in range(0, 5):
            N = n+k; xs, V = setup(N); V_[N] = V
            for mu in parts(n):
                got = to_schur(Ek(k, schur(mu, xs, V), xs, V), N)
                pred = predicted((1,)*k, mu, N, xs)
                bad = compare(got, pred); total += 1; ok += (not bad)
                log(f'k={k} mu={mu} N={N}: got={got}')
                log(f'    pred={pred}  {"OK" if not bad else "MISMATCH "+str(bad)}')
                if bad:
                    rat = {nu: sp.factor(got.get(nu, 0)/pred[nu]) if pred.get(nu) else None for nu in set(got)|set(pred)}
                    log('    ratio got/pred:', rat)
    log(f'PIERI SUMMARY: {ok}/{total} OK')
