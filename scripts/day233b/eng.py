# Day 233b FPSAC printed sweep -- fresh engine. Prop 2.1 subset formula, mod p, series in eps = s - s0.
# Points carry (base value, s-exponent) so pairs scaled equally cancel exactly (works at s0=0 too).
import numpy as np, itertools, math, random
from functools import lru_cache
p = 1073741789
rng = np.random.default_rng(12345)

def mpow(a, e):
    a = np.asarray(a, dtype=np.int64) % p; r = np.ones_like(a)
    while e:
        if e & 1: r = r * a % p
        a = a * a % p; e >>= 1
    return r
def minv(a): return mpow(a, p - 2)

def smul(a, b):
    K = a.shape[-1]; out = np.zeros(np.broadcast(a, b).shape, dtype=np.int64)
    for i in range(K):
        for j in range(K - i):
            out[..., i + j] = (out[..., i + j] + a[..., i] * b[..., j] % p) % p
    return out
def sinv(a):
    K = a.shape[-1]; b = np.zeros_like(a); i0 = minv(a[..., 0]); b[..., 0] = i0
    for k in range(1, K):
        acc = np.zeros(a.shape[:-1], dtype=np.int64)
        for i in range(1, k + 1): acc = (acc + a[..., i] * b[..., k - i] % p) % p
        b[..., k] = (-acc * i0) % p
    return b

class Ctx:
    def __init__(s, s0, t, K, maxe=12):
        s.s0, s.t, s.K = int(s0) % p, int(t) % p, K
        # table S[e] = series of s^e = (s0+eps)^e
        S = np.zeros((maxe + 1, K), dtype=np.int64)
        for e in range(maxe + 1):
            for k in range(min(e, K - 1) + 1):
                S[e, k] = math.comb(e, k) * pow(s.s0, e - k, p) % p
        s.S = S
    def const(s, v, shape):
        a = np.zeros(shape + (s.K,), dtype=np.int64); a[..., 0] = np.asarray(v) % p; return a
    def coords(s, xb, m):  # series values of points
        return (xb[..., None] % p) * s.S[m] % p

def cA(ctx, xb, m, A, N):
    """c_A at points (xb,m): prod_{i in A, j notin A} (x'_i - t x'_j)/(x'_i - x'_j), equal s-powers cancelled."""
    t = ctx.t; P = xb.shape[0]
    num = ctx.const(1, (P,)); den = ctx.const(1, (P,))
    for i in A:
        for j in range(N):
            if j in A: continue
            d = m[:, i] - m[:, j]
            ei = np.maximum(d, 0); ej = np.maximum(-d, 0)
            xi = (xb[:, i][:, None] % p) * ctx.S[ei] % p
            xj = (xb[:, j][:, None] % p) * ctx.S[ej] % p
            num = smul(num, (xi - t * xj) % p); den = smul(den, (xi - xj) % p)
    return smul(num, sinv(den))

def esym(ctx, X, k):  # e_k of series coordinates X (P,N,K)
    P, N, K = X.shape
    E = [ctx.const(1, (P,))] + [ctx.const(0, (P,)) for _ in range(k)]
    for i in range(N):
        for r in range(k, 0, -1):
            E[r] = (E[r] + smul(E[r - 1], X[:, i])) % p
    return E[k]

def evalE(ctx, seq, xb, m, base):
    """value of E_{seq[0]}...E_{seq[-1]} (base) at points; base(ctx,xb,m)->(P,K)."""
    if not seq: return base(ctx, xb, m)
    k = seq[0]; P, N = xb.shape
    subs = list(itertools.combinations(range(N), k)); C = len(subs)
    xb2 = np.repeat(xb, C, axis=0); m2 = np.repeat(m, C, axis=0).copy()
    for ci, A in enumerate(subs):
        m2[ci::C][:, list(A)] += 1
    inner = evalE(ctx, seq[1:], xb2, m2, base).reshape(P, C, ctx.K)
    tot = ctx.const(0, (P,))
    for ci, A in enumerate(subs):
        c = cA(ctx, xb, m, A, N)
        pr = np.ones(P, dtype=np.int64)
        for i in A: pr = pr * (xb[:, i] % p) % p
        XA = ctx.const(pr, (P,))
        # X_A at current points = prod x_i s^{m_i} (unscaled by this step)
        XA = smul(XA, ctx.S[m[:, list(A)].sum(axis=1)])
        tot = (tot + smul(smul(c, XA), inner[:, ci])) % p
    return tot

def base_one(ctx, xb, m): return ctx.const(1, (xb.shape[0],))
def base_eprod(js):
    def f(ctx, xb, m):
        X = ctx.coords(xb, m); v = ctx.const(1, (xb.shape[0],))
        for j in js: v = smul(v, esym(ctx, X, j))
        return v
    return f
def base_pprod(js):
    def f(ctx, xb, m):
        X = ctx.coords(xb, m); v = ctx.const(1, (xb.shape[0],))
        for j in js:
            pj = ctx.const(0, (xb.shape[0],)); Xj = X.copy(); acc = X.copy()
            for _ in range(j - 1): acc = smul(acc, X)
            v = smul(v, acc.sum(axis=1) % p)
        return v
    return f

def partitions(n, mx=None):
    if mx is None: mx = n
    if n == 0: yield (); return
    for k in range(min(n, mx), 0, -1):
        for r in partitions(n - k, k): yield (k,) + r

def e_scalar(xb, k):
    P, N = xb.shape; E = [np.ones(P, dtype=np.int64)] + [np.zeros(P, dtype=np.int64)] * k
    E = [e.copy() for e in E]
    for i in range(N):
        for r in range(k, 0, -1): E[r] = (E[r] + E[r - 1] * (xb[:, i] % p)) % p
    return E[k]

def solve_mod(A, B):
    """A (P x q) full column rank, B (P x K): least squares exact solve mod p via Gaussian elimination; returns q x K, raises if inconsistent."""
    A = [list(map(int, r)) for r in A]; B = [list(map(int, r)) for r in B]
    P, q = len(A), len(A[0]); M = [A[i] + B[i] for i in range(P)]
    row = 0; piv = []
    for col in range(q):
        r = next((i for i in range(row, P) if M[i][col] % p), None)
        if r is None: raise ValueError("rank")
        M[row], M[r] = M[r], M[row]; iv = pow(M[row][col], p - 2, p)
        M[row] = [v * iv % p for v in M[row]]
        for i in range(P):
            if i != row and M[i][col]:
                f = M[i][col]; M[i] = [(a - f * b) % p for a, b in zip(M[i], M[row])]
        piv.append(col); row += 1
    for i in range(row, P):
        if any(M[i][q:]): raise ValueError("inconsistent: not in span")
    return [M[i][q:] for i in range(q)]

def to_ebasis(ctx, n, N, valfun, extra=3):
    """valfun(xb,m)->(P,K) for a degree-n symmetric poly in N vars; returns {mu: series(list K)} over mu|-n with mu1<=N."""
    mus = [mu for mu in partitions(n) if mu[0] <= N]
    P = len(mus) + extra
    xb = rng.integers(1, p, size=(P, N)).astype(np.int64); m = np.zeros((P, N), dtype=np.int64)
    A = np.array([[int(np.prod([1] + [0]) ) for _ in mus] for _ in range(P)], dtype=object)
    cols = []
    for mu in mus:
        v = np.ones(P, dtype=np.int64)
        for k in mu: v = v * e_scalar(xb, k) % p
        cols.append(v)
    A = np.array(cols).T
    B = valfun(xb, m)
    sol = solve_mod(A, B)
    return {mu: sol[i] for i, mu in enumerate(mus)}

def estar(ctx, lam, N=None):
    """e*_lambda in e-basis, as series in eps. Uses E_last(1)=e_last (checked in C0)."""
    lam = tuple(lam); n = sum(lam)
    if N is None: N = n
    if not lam: return {(): [1] + [0] * (ctx.K - 1)}
    order = sorted(lam)  # outer small, innermost largest -> cheapest
    seq, last = order[:-1], order[-1]
    return to_ebasis(ctx, n, N, lambda xb, m: evalE(ctx, seq, xb, m, base_eprod([last])))

def EkF(ctx, k, base, n, N=None):
    if N is None: N = n
    return to_ebasis(ctx, n, N, lambda xb, m: evalE(ctx, [k], xb, m, base))

def sym(v): return v if v <= p // 2 else v - p
