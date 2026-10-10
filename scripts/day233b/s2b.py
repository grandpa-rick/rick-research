from util import *
import sys, sympy as sp
NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 7
t0 = int(rng.integers(2, p))
def cost(lam): return math.prod(math.comb(sum(lam), k) for k in sorted(lam)[:-1])
cache = {}
def es(lam, tt, K):
    key = (lam, tt, K)
    if key not in cache: cache[key] = estar(Ctx(1, tt, K, maxe=len(lam) + 1), lam)
    return cache[key]
def Lead(lam, mu, tt):
    l = len(lam); kp = kappa(lam, mu); c = es(lam, tt, l - kp + 1)[mu]; return c[l - kp]
def W_closed(k, J, tt):
    n = k + sum(J); v = (-1) ** len(J) * tq(n, tt) * inv(tq(k, tt)) % p
    for j in J: v = v * tq(k, tt, j) % p
    return v
def histories(lam, tt, Wf=None):
    """process lam_l..lam_1; labeled blocks; returns dict final sorted sizes -> (sum of weights, count, m)"""
    out = {}
    def rec(i, blocks, w, m):
        if i < 0:
            key = srt(blocks); s, c = out.get(key, (0, 0)); out[key] = ((s + w) % p, c + 1); return
        k = lam[i]
        rec(i - 1, blocks + [k], w, m)
        for T in subsets(blocks):
            if not T: continue
            J = tuple(sorted(blocks[x] for x in T))
            nb = [blocks[x] for x in range(len(blocks)) if x not in T] + [k + sum(J)]
            rec(i - 1, nb, w * (Wf or W_closed)(k, J, tt) % p, m + len(J))
    rec(len(lam) - 1, [], 1, 0); return out

def W_nosign(k,J,tt): return W_closed(k,J,tt)*(-1)**len(J)%p
R = Res("Thm3.7 NEG: weights without (-1)^p (should FAIL for odd m)")
for n in range(3, 8):
    for lam in partitions(n):
        if cost(lam) > 4e4: continue
        H = histories(lam, t0, W_nosign)
        for mu in partitions(n):
            if mu == lam or kappa(lam, mu) != len(mu): continue
            m = len(lam)-len(mu); R.chk(es(lam,t0,m+1)[mu][m] == H.get(mu,(0,0))[0], "")
print(R, "(expected FAIL)")
# ---------- Thm 4.4 coarsening factor ----------
R = Res("Thm4.4 Lead = sum over set partitions with block sums = mu of prod connected leads")
Rneg = Res("Thm4.4 NEG: count each distinct block-multiset once (dedupe) (should FAIL where equal parts)")
for n in range(2, NMAX + 1):
    for lam in partitions(n):
        if cost(lam) > 4e4: continue
        l = len(lam)
        for mu in partitions(n):
            if mu == lam or kappa(lam, mu) != len(mu): continue
            tot = 0; seen = {}; 
            for pi in setparts(list(range(l))):
                if srt(tuple(sum(lam[i] for i in B) for B in pi)) != mu: continue
                v = 1
                for B in pi:
                    if len(B) > 1:
                        lb = srt(tuple(lam[i] for i in B)); v = v * Lead(lb, (sum(lb),), t0) % p
                tot = (tot + v) % p
                seen[tuple(sorted(tuple(sorted((lam[i] for i in B),reverse=True)) for B in pi))] = v
            R.chk(Lead(lam, mu, t0) == tot, f"{lam}{mu}")
            Rneg.chk(Lead(lam, mu, t0) == sum(seen.values()) % p, "")
print(R); print(Rneg, "(expected FAIL)")
# ---------- Thm 4.5 block multiplicativity ----------
R = Res("Thm4.5 [(s-1)^m]c = sum_{pi,kappa blocks} sum_{(nu^C)} prod [(s-1)^{|C|-1}]c_{lam_C,nu^C}; factors kappa=1")
Rneg = Res("Thm4.5 NEG: sum over position-assignments of mu (overcount) (should FAIL)")
def subparts(mu, sizes):
    """distinct tuples of partitions (nu^1..nu^r) with |nu^i|=sizes[i], disjoint union = mu (multiset); and position-assignment count"""
    res = Counter()
    def rec(i, rem, acc):
        if i == len(sizes):
            if not rem: res[tuple(acc)] += 1
            return
        for T in subsets(rem):
            if not T: continue
            nu = srt(tuple(rem[x] for x in T))
            if sum(nu) != sizes[i]: continue
            rec(i + 1, tuple(rem[x] for x in range(len(rem)) if x not in T), acc + [nu])
    rec(0, tuple(mu), []); return res
for n in range(2, NMAX + 1):
    for lam in partitions(n):
        if cost(lam) > 4e4: continue
        l = len(lam)
        for mu in partitions(n):
            kp = kappa(lam, mu)
            if kp < 1: continue
            m = l - kp; lhs = es(lam, t0, m + 1)[mu][m]; tot = 0; tot2 = 0
            for pi in setparts(list(range(l))):
                if len(pi) != kp: continue
                lC = [srt(tuple(lam[i] for i in B)) for B in pi]
                for tup, mult in subparts(mu, [sum(x) for x in lC]).items():
                    if not all(dom(nu, lc) for nu, lc in zip(tup, lC)): continue
                    v = 1
                    for nu, lc, B in zip(tup, lC, pi):
                        R.chk(kappa(lc, nu) == 1, f"factor kappa {lc}{nu}")
                        v = v * es(lc, t0, len(B))[nu][len(B) - 1] % p
                    tot = (tot + v) % p; tot2 = (tot2 + mult * v) % p
            R.chk(lhs == tot, f"{lam}{mu}"); Rneg.chk(lhs == tot2, "")
print(R); print(Rneg, "(expected FAIL)")
