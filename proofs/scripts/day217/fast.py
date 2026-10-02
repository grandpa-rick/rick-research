"""Day 217 kill test (fast engine). At t = 1/s, test
   s_lam * s_mu =?= sum_nu c^nu_{lam mu} s^{c(nu)-c(lam)-c(mu)} s_nu,   c = sum of contents.
e_k * F := E_k F  (normalisation from Theorem (N): Psi=N^{-1}, Psi E_k = t^{-C(k,2)} e_k Psi, N(e_k)=t^{C(k,2)}e_k  =>  e_k*F = E_k F).
E_k F = sum_A prod_{i in A, j notin A}(x_i - t x_j)/(x_i - x_j) X_A F(X_{A^c}, s X_A).
At t=1/s: (x_i - x_j/s) = s^{-1}(s x_i - x_j); so E_k = s^{-k(N-k)} * [integer poly operator]. Work in ZZ[s, x], track s-power separately.
Schur expansion via alternant coefficients (coefficient of x^{lam+delta} in Vandermonde*f)."""
import sys, itertools
from sympy.polys.rings import ring
from sympy import ZZ, Matrix, Symbol, factor, cancel, Integer
out = open(sys.argv[1], 'w'); MODE = sys.argv[2]
def log(*a):
    print(*a, flush=True); print(*a, file=out, flush=True)
S = Symbol('s')
def parts(n, m=None):
    if m is None: m = n
    if n == 0: yield (); return
    for k in range(min(n, m), 0, -1):
        for p in parts(n-k, k): yield (k,)+p
def content(l): return sum(j-i for i, r in enumerate(l) for j in range(r))
RINGS = {}
def R(N):
    if N not in RINGS:
        Rg, *g = ring(['s']+[f'x{i}' for i in range(N)], ZZ)
        s, xs = g[0], g[1:]
        V = Rg(1)
        for i in range(N):
            for j in range(i+1, N): V *= xs[i]-xs[j]
        RINGS[N] = (Rg, s, xs, V)
    return RINGS[N]
def ssyt(lam, N):
    cells = [(i, j) for i, r in enumerate(lam) for j in range(r)]; T = {}
    def rec(c):
        if c == len(cells):
            v = [0]*N
            for x in T.values(): v[x] += 1
            yield tuple(v); return
        i, j = cells[c]
        lo = max(T[(i, j-1)] if j > 0 else 0, T[(i-1, j)]+1 if i > 0 else 0)
        for x in range(lo, N):
            T[(i, j)] = x; yield from rec(c+1)
        T.pop((i, j), None)
    yield from rec(0)
def schur(lam, N):
    Rg, s, xs, V = R(N); d = {}
    for v in ssyt(lam, N): d[(0,)+v] = d.get((0,)+v, 0)+1
    return Rg.from_dict(d) if d else Rg(0)
def Ek(k, F, N):  # returns poly; true E_k F = poly * s^{-k(N-k)}
    Rg, s, xs, V = R(N); tot = Rg(0)
    Fd = F.to_dict()
    for A in itertools.combinations(range(N), k):
        B = [j for j in range(N) if j not in A]
        sign = (-1)**sum(1 for i in A for j in B if i > j)
        term = Rg(sign)
        for i in range(N):
            for j in range(i+1, N):
                if (i in A) == (j in A): term *= xs[i]-xs[j]
        for i in A:
            term *= xs[i]
            for j in B: term *= s*xs[i]-xs[j]
        Fs = Rg.from_dict({(m[0]+sum(m[1+i] for i in A),)+m[1:]: c for m, c in Fd.items()})
        tot += term*Fs
    q, r = tot.div(V); assert r == 0, 'not polynomial'
    return q
def to_schur(F, e, N):  # F*s^e -> dict lam -> sympy coeff
    Rg, s, xs, V = R(N); g = F*V; d = {}
    for m, c in g.terms():
        lam = [m[1+i]-(N-1-i) for i in range(N)]
        if all(lam[i] >= lam[i+1] for i in range(N-1)) and lam[-1] >= 0:
            key = tuple(a for a in lam if a > 0)
            d[key] = d.get(key, 0) + Integer(c)*S**(m[0]+e)
    return {k: factor(v) for k, v in d.items() if v != 0}
def lr(lam, mu, N): return to_schur(schur(lam, N)*schur(mu, N), 0, N)
def predicted(lam, mu, N): return {nu: c*S**(content(nu)-content(lam)-content(mu)) for nu, c in lr(lam, mu, N).items()}
def compare(got, pred):
    return [(k, got.get(k, 0), pred.get(k, 0)) for k in set(got) | set(pred) if cancel(got.get(k, 0)-pred.get(k, 0)) != 0]
def report(tag, got, pred):
    bad = compare(got, pred)
    log(f'{tag}: got={got}\n    pred={pred}  {"OK" if not bad else "MISMATCH "+str(bad)}')
    if bad: log('    ratio got/pred:', {nu: factor(got.get(nu, 0)/pred[nu]) if pred.get(nu) else ('extra', got.get(nu)) for nu in set(got)|set(pred)})
    return not bad
if MODE == 'pieri':
    tot = ok = 0
    for k in (1, 2, 3):
        for n in range(0, 5 if k < 3 else 4):
            N = n+k
            for mu in parts(n):
                got = to_schur(Ek(k, schur(mu, N), N), -k*(N-k), N)
                tot += 1; ok += report(f'e_{k} * s_{mu} N={N}', got, predicted((1,)*k, mu, N))
    log(f'PIERI SUMMARY: {ok}/{tot} OK')
if MODE == 'star':
    def Erho(rho, F, N):
        e = 0
        for k in reversed(rho): F = Ek(k, F, N); e -= k*(N-k)
        return F, e
    def star_expansion(lam):
        n = sum(lam); P = list(parts(n))
        G = Matrix(len(P), len(P), lambda i, j: 0)
        for i, rho in enumerate(P):
            F, e = Erho(rho, R(n)[0](1), n); d = to_schur(F, e, n)
            for j, nu in enumerate(P): G[i, j] = d.get(nu, 0)
        Gi = G.inv(); j = P.index(lam)
        return {rho: factor(Gi[j, i]) for i, rho in enumerate(P) if Gi[j, i] != 0}
    tot = ok = 0
    for lam, mu in [((2,), (1, 1)), ((1, 1), (2,)), ((2,), (2,)), ((2, 1), (1,)), ((2,), (2, 1)), ((1, 1), (2, 1)),
                    ((3,), (1, 1)), ((2, 1), (2, 1)), ((2, 1), (1, 1, 1)), ((2, 1), (3,))]:
        coeffs = star_expansion(lam); N = sum(lam)+sum(mu)
        log(f'  s_{lam} = sum_rho a_rho E_rho(1): {coeffs}')
        got = {}
        for rho, a in coeffs.items():
            F, e = Erho(rho, schur(mu, N), N)
            for nu, c in to_schur(F, e, N).items(): got[nu] = got.get(nu, 0) + a*c
        got = {k: factor(v) for k, v in got.items() if cancel(v) != 0}
        tot += 1; ok += report(f's_{lam} * s_{mu} N={N}', got, predicted(lam, mu, N))
    log(f'STAR SUMMARY: {ok}/{tot} OK')
