# Fast mod-p re-implementation of the PRINTED subset formula (longversion (2.x) E_k, Lemma 2.8 stability:
# e*_lam in m variables = sum_mu c_{lam,mu} e_mu(x_1..x_m), e_mu=0 if mu_1>m). Exact over F_p, p=2^61-1.
import itertools, random, sys
from functools import lru_cache
P = (1 << 61) - 1
inv = lambda a: pow(a % P, P - 2, P)
rng = random.Random(232)
def partitions(n, maxp=None):
    if maxp is None: maxp = n
    if n == 0: yield (); return
    for p in range(min(n, maxp), 0, -1):
        for q in partitions(n - p, p): yield (p,) + q
def esym(xs, r):
    e = [1] + [0] * len(xs)
    for x in xs:
        for j in range(len(xs), 0, -1): e[j] = (e[j] + e[j - 1] * x) % P
    return e[r] if 0 <= r <= len(xs) else 0
def estar(lam, x, s, t):
    if not lam: return 1
    k = lam[0]; m = len(x); tot = 0
    for A in itertools.combinations(range(m), k):
        As = set(A); c = 1
        for i in A:
            c = c * x[i] % P
            for j in range(m):
                if j not in As: c = c * (x[i] - t * x[j]) % P * inv(x[i] - x[j]) % P
        y = [s * x[i] % P if i in As else x[i] for i in range(m)]
        tot = (tot + c * estar(lam[1:], y, s, t)) % P
    return tot
def solve(M, b):
    n = len(M); cols = len(M[0]); A = [row[:] + [bb] for row, bb in zip(M, b)]; r = 0
    for c in range(cols):
        pr = next((i for i in range(r, n) if A[i][c] % P), None)
        assert pr is not None, 'singular'
        A[r], A[pr] = A[pr], A[r]; iv = inv(A[r][c]); A[r] = [a * iv % P for a in A[r]]
        for i in range(n):
            if i != r and A[i][c]:
                f = A[i][c]; A[i] = [(a - f * bb) % P for a, bb in zip(A[i], A[r])]
        r += 1
    for i in range(r, n): assert A[i][-1] % P == 0, 'inconsistent'
    return [A[i][-1] for i in range(cols)]
def nfun(lam): return sum(i * p for i, p in enumerate(lam))
@lru_cache(None)
def hexp(lam, t, m):
    """{mu: [coef of (s-1)^j]} for mu_1<=m, in m variables. s-degree <= n(lam) (each E_k step rescales a
    homogeneous function of degree = remaining size), interpolate on n(lam)+3 nodes and verify the top 2 vanish."""
    n = sum(lam); mus = [mu for mu in partitions(n) if mu[0] <= m]
    D = nfun(lam) + 3
    hs = list(range(2, 2 + D))
    pts = []
    while len(pts) < len(mus) + 3:
        p = [rng.randrange(1, P) for _ in range(m)]
        if len(set(p)) == m: pts.append(p)
    M = [[1] * len(mus) for _ in pts]
    for a, p in enumerate(pts):
        es = [esym(p, r) for r in range(m + 1)]
        for b, mu in enumerate(mus):
            v = 1
            for r in mu: v = v * es[r] % P
            M[a][b] = v
    cols = []
    for h in hs:
        b = [estar(lam, p, (1 + h) % P, t) for p in pts]
        cols.append(solve(M, b))
    out = {}
    for j, mu in enumerate(mus):
        ys = [c[j] for c in cols]
        co = interp(hs, ys)
        assert co[-1] == 0 and co[-2] == 0, ('degree bound violated', lam, mu)
        out[mu] = co
    return out
def interp(xs, ys):
    n = len(xs); coef = [0] * n
    for i in range(n):
        num = [1]; den = 1
        for j in range(n):
            if j == i: continue
            num = [((num[k - 1] if k > 0 else 0) - xs[j] * (num[k] if k < len(num) else 0)) % P for k in range(len(num) + 1)]
            den = den * (xs[i] - xs[j]) % P
        di = inv(den)
        for k in range(len(num)): coef[k] = (coef[k] + ys[i] * num[k] % P * di) % P
    return coef
def frac_to_p(fr): return fr.numerator % P * inv(fr.denominator) % P
