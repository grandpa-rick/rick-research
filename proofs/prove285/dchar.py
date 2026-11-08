"""D_n character machinery: classes, irreducible characters (via B_n bipartition MN + split Delta),
parabolic class fusion, sign-induced multiplicities f(chi,J), a-values from symbols,
constructible characters via truncated (a-)induction from maximal parabolics + (x)sgn.
Node labels: chain 1..n-2, branch n-2, leaves n-1 (swap n-1,n), n (signed swap).
Standard S_n = <s_1..s_{n-1}>. sigma = diagram automorphism swapping n-1,n."""
from fractions import Fraction
from functools import lru_cache
from math import factorial
from itertools import combinations
from collections import Counter
import os
def EPS(nu):
    return (-1)**(sum(nu)-len(nu)) if os.environ.get('EPSCTL') else 1

@lru_cache(None)
def partitions(n, mx=None):
    if mx is None: mx = n
    if n == 0: return ((),)
    out = []
    for k in range(min(n, mx), 0, -1):
        for p in partitions(n - k, k): out.append((k,) + p)
    return tuple(out)

def zee(p):
    c = Counter(p); z = 1
    for r, m in c.items(): z *= r**m * factorial(m)
    return z

def conj(p):
    return tuple(sum(1 for x in p if x > i) for i in range(p[0])) if p else ()

def _hooks(lam, r):
    """all (newlam, sign) from removing an r-rim-hook (beta numbers)."""
    L = len(lam)
    beta = [lam[i] + (L - 1 - i) for i in range(L)]
    S = set(beta); out = []
    for b in beta:
        if b - r >= 0 and (b - r) not in S:
            ht = sum(1 for x in beta if b - r < x < b)
            nb = sorted([x for x in beta if x != b] + [b - r], reverse=True)
            nl = tuple(x - (L - 1 - i) for i, x in enumerate(nb))
            nl = tuple(x for x in nl if x > 0)
            out.append((nl, (-1)**ht))
    return out

@lru_cache(None)
def chiS(lam, rho):
    """S_k character chi^lam at cycle type rho (lam=(k) trivial)."""
    if not rho: return 1 if not lam else 0
    r, rest = rho[0], rho[1:]
    return sum(s * chiS(nl, rest) for nl, s in _hooks(lam, r))

@lru_cache(None)
def chiB(a, b, lam, mu):
    """B_n char chi^{(a,b)} at class (lam positive cycles, mu negative cycles)."""
    if not lam and not mu: return 1 if (not a and not b) else 0
    if lam:
        r, lam2, mu2, neg = lam[0], lam[1:], mu, False
    else:
        r, lam2, mu2, neg = mu[0], lam, mu[1:], True
    t = 0
    for na, s in _hooks(a, r): t += s * chiB(na, b, lam2, mu2)
    for nb, s in _hooks(b, r): t += (-s if neg else s) * chiB(a, nb, lam2, mu2)
    return t

def bipartitions(n):
    return [(a, b) for k in range(n + 1) for a in partitions(k) for b in partitions(n - k)]

class Dgroup:
    def __init__(self, n):
        self.n = n
        self.order = 2**(n - 1) * factorial(n) if n >= 1 else 1
        if n <= 1:
            self.classes = [((1,) * n, (), 0)]; self.csize = [1]
            self.irr = [('triv',)]; self.table = [[1]]; self.a = [0]
            return
        cl, cs = [], []
        BN = 2**n * factorial(n)
        for k in range(n + 1):
            for lam in partitions(k):
                for mu in partitions(n - k):
                    if len(mu) % 2: continue
                    bsize = BN // (zee(lam) * zee(mu) * 2**(len(lam) + len(mu)))
                    if not mu and all(x % 2 == 0 for x in lam):
                        for sg in (1, -1): cl.append((lam, mu, sg)); cs.append(bsize // 2)
                    else:
                        cl.append((lam, mu, 0)); cs.append(bsize)
        self.classes, self.csize = cl, cs
        self.cidx = {c: i for i, c in enumerate(cl)}
        irr, tab = [], []
        seen = set()
        for a, b in bipartitions(n):
            key = tuple(sorted([a, b]))
            if key in seen: continue
            seen.add(key)
            if a != b:
                irr.append((key[0], key[1], 0))
                tab.append([chiB(a, b, l, m) for (l, m, s) in cl])
            else:
                for e in (1, -1):
                    row = []
                    for (l, m, s) in cl:
                        v = chiB(a, a, l, m)
                        dl = 0
                        if s != 0:
                            nu = tuple(x // 2 for x in l)
                            dl = e * s * 2**len(nu) * chiS(a, nu) * (EPS(nu))
                        v = Fraction(v + dl, 2)
                        assert v.denominator == 1; v = int(v)
                        row.append(v)
                    irr.append((a, a, e)); tab.append(row)
        self.irr, self.table = irr, tab
        self.a = [self.avalue(x) for x in irr]

    def inner(self, f, g):
        return Fraction(sum(c * x * y for c, x, y in zip(self.csize, f, g)), self.order)

    def avalue(self, x):
        if len(x) == 1: return 0
        a, b = x[0], x[1]
        M = max(len(a), len(b)) + 1
        def ent(p):
            p = list(p) + [0] * (M - len(p)); p = p[::-1]
            return [p[i] + i for i in range(M)]
        def smin(E): return sum(min(u, v) for u, v in combinations(E, 2))
        return smin(ent(a) + ent(b)) - smin(ent((self.n,)) + ent(()))

    def sigma_irr(self, i):
        a, b, e = self.irr[i]
        return self.irr.index((a, b, -e)) if e else i

    def sgn(self):
        return [(-1)**(self.n - len(l) - len(m)) for (l, m, s) in self.classes]

@lru_cache(None)
def D(n): return Dgroup(n)

def parabolic(n, ks, m):
    """W' = S_{k1} x ... x D_m on coords (blocks first, D_m last). Returns list of
    (size, Dn-class-index, list of W'-class labels) -- labels used to evaluate W' chars."""
    G = D(n); Dm = D(m)
    out = []
    def rec(i, acc):
        if i == len(ks):
            for ci, (lc, mc, sc) in enumerate(Dm.classes):
                lam = tuple(sorted([x for r in acc for x in r] + list(lc), reverse=True))
                mu = tuple(mc)
                split = (not mu) and all(x % 2 == 0 for x in lam)
                sg = (sc if m >= 2 else 1) if split else 0
                size = Dm.csize[ci]
                for r in acc: size *= factorial(sum(r)) // zee(r)
                out.append((size, G.cidx[(lam, mu, sg)], (tuple(acc), ci)))
            return
        for r in partitions(ks[i]): rec(i + 1, acc + [r])
    rec(0, [])
    return out

def J_blocks(n, J):
    """J subset of {1..n}, not (n in J and n-1 not in J). Return (ks, m)."""
    J = set(J)
    if n in J:
        assert n - 1 in J
        c = n - 1
        while c - 1 >= 1 and (c - 1) in J and c - 1 <= n - 2: c -= 1
        # coords c..n if chain nodes c..n-2 in J; c here is smallest coordinate index
        if n - 2 in J:
            c = n - 2
            while c - 1 >= 1 and (c - 1) in J: c -= 1
        else:
            c = n - 1
        m = n - c + 1; top = c - 1  # coords 1..c-1 for A blocks, nodes 1..c-2
    else:
        m = 0; top = n
    ks, cur = [], 1
    for i in range(1, top):
        if i in J: cur += 1
        else: ks.append(cur); cur = 1
    if top >= 1: ks.append(cur)
    return ks, m

@lru_cache(None)
def fvec(n, J):
    """f(chi_i, J) = <chi_i, Ind_{W_J} sgn> for all irreps i of D_n. J frozenset."""
    G = D(n)
    if n in J and (n - 1) not in J:
        sJ = frozenset((n - 1 if j == n else j) for j in J)
        v = fvec(n, sJ)
        return tuple(v[G.sigma_irr(i)] for i in range(len(G.irr)))
    ks, m = J_blocks(n, J)
    P = parabolic(n, ks, m)
    order = sum(s for s, _, _ in P)
    sg = G.sgn()
    res = []
    for row in G.table:
        t = sum(s * sg[ci] * row[ci] for s, ci, _ in P)
        q = Fraction(t, order); assert q.denominator == 1 and q >= 0, (n, J, q)
        res.append(int(q))
    return tuple(res)

def Wprime_irreps(ks, m):
    Dm = D(m)
    out = [[]]
    for k in ks: out = [o + [lam] for o in out for lam in partitions(k)]
    return [(tuple(o), j) for o in out for j in range(len(Dm.irr))]

def Wprime_char(ks, m, E, label):
    lams, j = E; rhos, ci = label
    v = D(m).table[j][ci]
    for lam, rho in zip(lams, rhos): v *= chiS(lam, rho)
    return v

def Wprime_a(ks, m, E):
    lams, j = E
    return sum(sum(i * x for i, x in enumerate(lam)) for lam in lams) + D(m).a[j]

def induce(n, ks, m, E):
    G = D(n); P = parabolic(n, ks, m)
    order = sum(s for s, _, _ in P)
    vals = [(s, ci, Wprime_char(ks, m, E, lab)) for s, ci, lab in P]
    res = []
    for row in G.table:
        q = Fraction(sum(s * v * row[ci] for s, ci, v in vals), order)
        assert q.denominator == 1 and q >= 0; res.append(int(q))
    return res

def Jind(n, ks, m, Evec_list):
    """Evec_list: list of (coef, W'-irrep). returns truncated-induction vector."""
    G = D(n)
    aE = {Wprime_a(ks, m, E) for c, E in Evec_list}
    assert len(aE) == 1; aE = aE.pop()
    tot = [0] * len(G.irr)
    for c, E in Evec_list:
        v = induce(n, ks, m, E)
        tot = [x + c * y for x, y in zip(tot, v)]
    for i, x in enumerate(tot):
        if x: assert G.a[i] >= aE, ("a-violation", n, ks, m, G.irr[i], G.a[i], aE)
    return tuple(x if G.a[i] == aE else 0 for i, x in enumerate(tot))

def tensor_sgn(n, v):
    G = D(n); sg = G.sgn()
    out = [0] * len(G.irr)
    for i, x in enumerate(v):
        if not x: continue
        row = [a * b for a, b in zip(G.table[i], sg)]
        j = G.table.index(row); out[j] += x
    return tuple(out)

@lru_cache(None)
def Con(n):
    """constructible characters of D_n, as tuples of multiplicities over D(n).irr."""
    G = D(n)
    if n <= 1: return frozenset({(1,)})
    res = set()
    maxpar = [([k], n - k) for k in range(1, n - 1)] + [([n], 0)]
    for ks, m in maxpar:
        # Con(W') = products: S_k irreps (type A: Con = Irr) x Con(D_m)
        conm = Con(m) if m >= 2 else [(1,)]
        Dm = D(m)
        for cm in conm:
            for lams in [[]] if not ks else None or _prodparts(ks):
                lst = [(c, (tuple(lams), j)) for j, c in enumerate(cm) if c]
                # truncated induction is linear on a-homogeneous constructibles
                v = Jind(n, ks, m, lst)
                res.add(v)
                if ks == [n] and m == 0:
                    res.add(tuple(v[G.sigma_irr(i)] for i in range(len(G.irr))))
    res |= {tensor_sgn(n, v) for v in res}
    return frozenset(res)

def _prodparts(ks):
    out = [[]]
    for k in ks: out = [o + [lam] for o in out for lam in partitions(k)]
    return out
