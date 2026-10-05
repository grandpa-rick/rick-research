"""
Day 205: fast re-implementation of the Day 198/201 pipeline (build_action in
day198/p2Y_er.py) using python-flint fmpz_mpoly.

Conventions copied VERBATIM from day198/p2Y_er.py:
  T_j F   = t s_j F - (t-1) X_{j+1} (F - s_j F)/(X_j - X_{j+1})
  pi F    = X_1 F(X_2,...,X_m, q^{-1} X_1)
  Y_i     = t^{m-i} T_{i-1}...T_1 pi T_{m-1}^{-1}...T_i^{-1}   (T_i^{-1} applied first)
We absorb t^{m-i} as (t T_j^{-1}) = T_j - (t-1), so everything is polynomial in
s := q^{-1} and t.  Output coefficients are in Z[s,t]; convert with s = 1/q.

p_k(Y).e_r = sum_i Y_i^k e_r(X_1..X_m), homogeneous of degree r+k, symmetric.
e-basis expansion via monomial coefficients + greedy triangular peel.
"""
import flint, sys, time, json
import sympy as sp
from itertools import combinations

q, t = sp.symbols('q t')


def partitions_of(n, maxp=None):
    if maxp is None:
        maxp = n
    if n == 0:
        yield ()
        return
    for p in range(min(n, maxp), 0, -1):
        for rest in partitions_of(n - p, p):
            yield (p,) + rest


def conj(lam):
    return tuple(sum(1 for x in lam if x > i) for i in range(lam[0])) if lam else ()


class AHA:
    def __init__(self, m):
        self.m = m
        names = [f'X{i}' for i in range(1, m + 1)] + ['s', 't']
        self.ctx = flint.fmpz_mpoly_ctx.get(names)
        g = self.ctx.gens()
        self.X = g[:m]
        self.s = g[m]
        self.t = g[m + 1]
        # swap maps
        self._swap = []
        for j in range(m - 1):
            args = list(g)
            args[j], args[j + 1] = g[j + 1], g[j]
            self._swap.append(args)
        args = list(g)
        for j in range(m - 1):
            args[j] = g[j + 1]
        args[m - 1] = self.s * g[0]
        self._pi = args

    def T(self, F, j):  # j is 1-based, 1..m-1
        sF = F.compose(*self._swap[j - 1])
        d = F - sF
        if d.is_zero():
            return self.t * sF
        quot = d / (self.X[j - 1] - self.X[j])  # exact
        return self.t * sF - (self.t - 1) * self.X[j] * quot

    def tTinv(self, F, j):
        return self.T(F, j) - (self.t - 1) * F

    def pi(self, F):
        return self.X[0] * F.compose(*self._pi)

    def Y(self, F, i):
        G = F
        for j in range(i, self.m):
            G = self.tTinv(G, j)
        G = self.pi(G)
        for j in range(1, i):
            G = self.T(G, j)
        return G

    def e(self, r):
        tot = self.ctx.from_dict({}) if False else 0 * self.X[0]
        for c in combinations(range(self.m), r):
            mon = 1 + 0 * self.X[0]
            for v in c:
                mon = mon * self.X[v]
            tot = tot + mon
        return tot


def e_expansion(A, F, n):
    """F symmetric homogeneous deg n in m>=n vars. Returns {lam: coeff(fmpz_mpoly in s,t)}."""
    m = A.m
    assert m >= n
    parts = list(partitions_of(n))
    d = F.to_dict()
    zero_st = 0 * A.s

    def key(lam):
        return tuple(list(lam) + [0] * (m - len(lam))) + (None,)

    # monomial coefficient a_lam (a polynomial in s,t): collect terms with X-exponent = lam
    a = {lam: 0 * A.s for lam in parts}
    lamset = {tuple(list(lam) + [0] * (m - len(lam))): lam for lam in parts}
    for mon, c in d.items():
        xe = tuple(mon[:m])
        if xe in lamset:
            a[lamset[xe]] = a[lamset[xe]] + c * A.s ** mon[m] * A.t ** mon[m + 1]
    # e_mu monomial coefficients (integers) at x^lam
    ectx = flint.fmpz_mpoly_ctx.get([f'Z{i}' for i in range(1, m + 1)])
    Z = ectx.gens()
    ecache = {}

    def e_poly(k):
        if k not in ecache:
            tot = 0 * Z[0]
            for c in combinations(range(m), k):
                mon = 1 + 0 * Z[0]
                for v in c:
                    mon = mon * Z[v]
                tot = tot + mon
            ecache[k] = tot
        return ecache[k]

    def e_mon_coeffs(mu):
        P = 1 + 0 * Z[0]
        for k in mu:
            P = P * e_poly(k)
        dd = P.to_dict()
        return {lam: int(dd.get(tuple(list(lam) + [0] * (m - len(lam))), 0)) for lam in parts}

    # greedy peel: lex-largest lam with nonzero a_lam -> coefficient of e_{lam'}
    res = {}
    parts_sorted = sorted(parts, reverse=True)  # lex decreasing
    for lam in parts_sorted:
        c = a[lam]
        if c.is_zero():
            continue
        mu = conj(lam)
        res[mu] = c
        emc = e_mon_coeffs(mu)
        assert emc[lam] == 1
        for nu in parts:
            if emc[nu]:
                a[nu] = a[nu] - emc[nu] * c
    return res


def to_sympy(A, c):
    """fmpz_mpoly in (X..., s, t) with no X -> sympy expr in q,t, s=1/q."""
    m = A.m
    expr = sp.Integer(0)
    for mon, co in c.to_dict().items():
        assert all(e == 0 for e in mon[:m])
        expr += sp.Integer(int(co)) * q ** (-mon[m]) * t ** mon[m + 1]
    return expr


def compute(k, r, m, verbose=True):
    A = AHA(m)
    t0 = time.time()
    er = A.e(r)
    tot = 0 * A.s
    for i in range(1, m + 1):
        v = er
        for _ in range(k):
            v = A.Y(v, i)
        tot = tot + v
        if verbose:
            print(f'   i={i} done  {time.time()-t0:.1f}s  terms={len(tot)}', flush=True)
    exp = e_expansion(A, tot, r + k)
    return {lam: to_sympy(A, c) for lam, c in exp.items()}, time.time() - t0


if __name__ == '__main__':
    k, r, m = map(int, sys.argv[1:4])
    exp, dt = compute(k, r, m)
    print(f'k={k} r={r} m={m} time={dt:.1f}s')
    out = {str(lam): str(sp.factor(c)) for lam, c in exp.items()}
    for lam in sorted(exp, reverse=True):
        print(f'  e_{lam}: {sp.factor(exp[lam])}')
    with open(f'/home/agent/projects/proofs/scripts/day205/k{k}_r{r}_m{m}.json', 'w') as f:
        json.dump(out, f, indent=1)
