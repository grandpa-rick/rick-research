from eng import *
from fractions import Fraction
from functools import lru_cache
from collections import Counter

def nfun(lam): return sum(i * x for i, x in enumerate(lam))
def conj(lam):
    return tuple(sum(1 for x in lam if x > i) for i in range(lam[0])) if lam else ()
def dom(mu, lam):  # mu >= lam (same size)
    if sum(mu) != sum(lam): return False
    a = b = 0
    for i in range(max(len(mu), len(lam))):
        a += mu[i] if i < len(mu) else 0; b += lam[i] if i < len(lam) else 0
        if a < b: return False
    return True
def srt(x): return tuple(sorted((v for v in x if v > 0), reverse=True))

def subsets(seq):
    for r in range(len(seq) + 1):
        for c in itertools.combinations(range(len(seq)), r): yield c

@lru_cache(None)
def kappa(lam, mu):
    """printed def: largest r with lam, mu split into r nonempty blocks (as multisets), mu^i dom lam^i."""
    lam, mu = srt(lam), srt(mu)
    if not lam and not mu: return 0
    if not lam or not mu: return -10**9
    best = -10**9
    rest = lam[1:]
    for S in subsets(rest):
        LS = srt((lam[0],) + tuple(rest[i] for i in S)); w = sum(LS)
        Lrest = srt(tuple(rest[i] for i in range(len(rest)) if i not in S))
        seen = set()
        for T in subsets(mu):
            if not T: continue
            MT = srt(tuple(mu[i] for i in T))
            if sum(MT) != w or MT in seen: continue
            seen.add(MT)
            if not dom(MT, LS): continue
            Mrest = srt(tuple(mu[i] for i in range(len(mu)) if i not in T))
            r = kappa(Lrest, Mrest)
            if r >= 0: best = max(best, 1 + r)
    return best

def setparts(lst):
    if not lst: yield []; return
    f, rest = lst[0], lst[1:]
    for sp in setparts(rest):
        for i in range(len(sp)): yield sp[:i] + [[f] + sp[i]] + sp[i + 1:]
        yield [[f]] + sp

def tq(m, t, r=1):  # [m]_{t^r} mod p
    tr = pow(int(t) % p, r, p); return sum(pow(tr, i, p) for i in range(m)) % p
def inv(a): return pow(int(a) % p, p - 2, p)

def zee(lam):
    z = 1
    for k, m in Counter(lam).items(): z *= k ** m * math.factorial(m)
    return z
def eps_(lam): return (-1) ** (sum(lam) - len(lam))

# e -> p expansion mod p (exact rationals reduced mod p)
@lru_cache(None)
def e_in_p(n):  # dict rho -> coef
    return {rho: eps_(rho) * inv(zee(rho)) % p for rho in partitions(n)}
def pmul(A, B):
    out = {}
    for a, x in A.items():
        for b, y in B.items():
            k = srt(a + b); out[k] = (out.get(k, 0) + x * y) % p
    return out
def ebasis_to_p(d):  # d: mu -> scalar
    out = {}
    for mu, c in d.items():
        if not c % p: continue
        v = {(): 1}
        for k in mu: v = pmul(v, e_in_p(k))
        for r, x in v.items(): out[r] = (out.get(r, 0) + c * x) % p
    return out
def hall_pair_p(Gp, rho):  # <G, p_rho> Hall
    return Gp.get(srt(rho), 0) * zee(srt(rho)) % p
def hl_pair_pp(Gp, Fp, t):
    s = 0
    for r, x in Gp.items():
        if r in Fp:
            w = zee(r)
            for k in r: w = w * inv(1 - pow(t, k, p)) % p
            s = (s + x * Fp[r] * w) % p
    return s

def lead(series, v):
    return series[v] if v < len(series) else None
def val(series):
    for i, x in enumerate(series):
        if x % p: return i
    return len(series)  # means >= K

# HL P_lambda at scalar points via symmetrisation (Macdonald III (2.2)), N vars, param t
def P_at(lam, xb, t):
    P_, N = xb.shape; lam = tuple(lam) + (0,) * (N - len(lam))
    t = int(t) % p; tot = np.zeros(P_, dtype=np.int64)
    for w in itertools.permutations(range(N)):
        y = xb[:, list(w)] % p
        v = np.ones(P_, dtype=np.int64)
        for i in range(N):
            if lam[i]: v = v * mpow(y[:, i], lam[i]) % p
            for j in range(i + 1, N):
                v = v * ((y[:, i] - t * y[:, j]) % p) % p * minv((y[:, i] - y[:, j]) % p) % p
        tot = (tot + v) % p
    vl = 1
    for k, m in Counter(lam).items():
        for j in range(1, m + 1): vl = vl * (1 - pow(t, j, p)) % p * inv(1 - t) % p
    return tot * inv(vl) % p

def T_at(k, g, xb, t):
    """T_k g := sum_{|A|=k} c_A X_A g(X_A), scalar points, g: function (P,k)->(P,)"""
    P_, N = xb.shape; t = int(t) % p; tot = np.zeros(P_, dtype=np.int64)
    for A in itertools.combinations(range(N), k):
        v = np.ones(P_, dtype=np.int64)
        for i in A:
            v = v * (xb[:, i] % p) % p
            for j in range(N):
                if j in A: continue
                v = v * ((xb[:, i] - t * xb[:, j]) % p) % p * minv((xb[:, i] - xb[:, j]) % p) % p
        tot = (tot + v * g(xb[:, list(A)]) % p) % p
    return tot

def scalar_ebasis(n, N, f, extra=3):
    mus = [mu for mu in partitions(n) if mu[0] <= N]
    P_ = len(mus) + extra
    xb = rng.integers(1, p, size=(P_, N)).astype(np.int64)
    cols = []
    for mu in mus:
        v = np.ones(P_, dtype=np.int64)
        for k in mu: v = v * e_scalar(xb, k) % p
        cols.append(v)
    sol = solve_mod(np.array(cols).T, f(xb).reshape(-1, 1))
    return {mu: sol[i][0] for i, mu in enumerate(mus)}

def pval(xb, js):  # product of power sums at scalar points
    v = np.ones(xb.shape[0], dtype=np.int64)
    for j in js: v = v * (mpow(xb, j).sum(axis=1) % p) % p
    return v
def eval_e(xb, js):
    v = np.ones(xb.shape[0], dtype=np.int64)
    for j in js: v = v * e_scalar(xb, j) % p
    return v

class Res:
    def __init__(s, name): s.name, s.ok, s.bad, s.notes = name, 0, 0, []
    def chk(s, cond, msg=""):
        if cond: s.ok += 1
        else:
            s.bad += 1
            if len(s.notes) < 8: s.notes.append(msg)
    def __str__(s): return f"[{'PASS' if s.bad == 0 and s.ok > 0 else 'FAIL'}] {s.name}: {s.ok} ok, {s.bad} bad {s.notes if s.bad else ''}"
