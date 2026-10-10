from util import *
import sys, sympy as sp
NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 9
t0 = int(rng.integers(2, p))
def cost(lam): return math.prod(math.comb(sum(lam), k) for k in sorted(lam)[:-1])
cache = {}
def es(lam, tt, K):
    key = (lam, tt, K)
    if key not in cache: cache[key] = estar(Ctx(1, tt, K, maxe=len(lam) + 1), lam)
    return cache[key]
Tcache = {}
def Tp(a, kind, rho, tt=t0):
    """T_a g in p-basis, g = p_rho / e_rho / P_rho (in a vars)"""
    key = (a, kind, rho, tt)
    if key not in Tcache:
        n = a + sum(rho)
        g = {"p": lambda Y: pval(Y, rho), "e": lambda Y: eval_e(Y, rho), "P": lambda Y: P_at(rho, Y, tt)}[kind]
        eb = scalar_ebasis(n, n, lambda xb: T_at(a, g, xb, tt))
        Tcache[key] = (eb, ebasis_to_p(eb))
    return Tcache[key]
def mxy(x, y): return 2 if x == y else 1
# ---- Thm 6.6 printed formula ----
def L_(a, b, t): return (1 - pow(t, a + b, p)) * (pow(t, a * b, p) - 1) % p * inv((1 - pow(t, a, p)) * (1 - pow(t, b, p))) % p
def Mcl(k, r, t):
    if k < r: k, r = r, k
    out = {}
    if r == 0: return out
    out[srt((k, r))] = r % p
    for j in range(1, r + 1):
        kk = srt((k + j, r - j)); out[kk] = (out.get(kk, 0) + L_(k - r + j, j, t)) % p
    return out
def Da(a, F, t):  # derivation D_a(e_j)=M_aj on dict F
    out = {}
    for mu, c in F.items():
        for i in range(len(mu)):
            rest = mu[:i] + mu[i + 1:]
            for nu, x in Mcl(a, mu[i], t).items():
                kk = srt(nu + rest); out[kk] = (out.get(kk, 0) + c * x) % p
    return out
def Xi(a, r, q, t): return (-1) ** (r + q) * tq(a + r + q, t) * inv(tq(a, t)) % p * tq(a, t, r) % p * tq(a, t, q) % p
def thm66(a, b_, c, x, y, t, neg=False):
    n = x + y; _, Gp = Tp(a, "p", srt((b_, c)), t)
    U = ((-1) ** n * hall_pair_p(Gp, (x, y)) - Xi(a, b_, c, t)) * inv(1 if neg else mxy(x, y)) % p
    tot = (-1) ** (b_ + c) * U % p
    for r in range(1, b_):
        if sorted((b_ - r, a + r + c)) == sorted((x, y)): tot = (tot + (-1) ** (r + c) * Xi(a, r, c, t)) % p
    for q in range(1, c):
        if sorted((c - q, a + b_ + q)) == sorted((x, y)): tot = (tot + (-1) ** (b_ + q) * Xi(a, b_, q, t)) % p
    tot = (tot + Da(a, Mcl(b_, c, t), t).get(srt((x, y)), 0)) % p
    return tot
R = Res("Thm6.6 printed closed l=3,kappa=1 lead vs engine, all orderings")
Rneg = Res("Thm6.6 NEG: drop the 1/m_xy")
Rx = Res("Thm6.6 Xi_a(r,q) printed = lin T_a(p_r p_q)")
for a in range(1, 4):
    for r in range(1, 4):
        for q in range(1, 4):
            eb, _ = Tp(a, "p", srt((r, q))); Rx.chk(eb[(a + r + q,)] == Xi(a, r, q, t0), f"{a}{r}{q}")
print(Rx)
pairs = 0
for n in range(3, NMAX + 1):
    for lam in partitions(n):
        if len(lam) != 3 or cost(lam) > 2e4: continue
        mus = [mu for mu in partitions(n) if len(mu) == 2 and kappa(lam, mu) == 1]
        if not mus: continue
        full = es(lam, t0, 3)
        for mu in mus:
            pairs += 1
            for (a, b_, c) in set(itertools.permutations(lam)):
                v = thm66(a, b_, c, mu[0], mu[1], t0)
                R.chk(full[mu][2] == v, f"{lam}->{mu} order {(a,b_,c)}")
                if mu[0] == mu[1]: Rneg.chk(full[mu][2] == thm66(a, b_, c, mu[0], mu[1], t0, True), "")
print(R, f"({pairs} pairs)"); print(Rneg, "(expected FAIL)")
