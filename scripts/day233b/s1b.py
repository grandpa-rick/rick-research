from util import *
import sys
NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 7
t0 = int(rng.integers(2, p))
def cost(lam): return math.prod(math.comb(sum(lam), k) for k in sorted(lam)[:-1])
# ---------- caches of e*_lam at s0=1 ----------
cache = {}
def es(lam, tt, K):
    key = (lam, tt, K)
    if key not in cache: cache[key] = estar(Ctx(1, tt, K, maxe=len(lam) + 1), lam)
    return cache[key]
def ser(c, k): return c[k] if k < len(c) else 0
# ---------- Prop 3.3 M_kr closed form ----------
def L(a, b, t):
    return (1 - pow(t, a + b, p)) * (pow(t, a * b, p) - 1) % p * inv((1 - pow(t, a, p)) * (1 - pow(t, b, p))) % p
def Mclosed(k, r, t):
    if k < r: k, r = r, k
    out = {}
    if r == 0: return out
    key = srt((k, r)); out[key] = r % p
    for j in range(1, r + 1):
        kk = srt((k + j, r - j)); out[kk] = (out.get(kk, 0) + L(k - r + j, j, t)) % p
    return out
R = Res("Prop3.3 M_kr = B(e_k,e_r) closed form, symmetric (k+r<=9)")
Rneg = Res("Prop3.3 NEG: L(a,b) with a,b swapped to L(j, k-r+j) -- (should FAIL)")
for n in range(2, 10):
    for r in range(1, n // 2 + 1):
        k = n - r
        d = es(srt((k, r)), t0, 2)
        M = Mclosed(k, r, t0)
        for mu, c in d.items(): R.chk(c[1] == M.get(mu, 0), f"M_{k}{r} at {mu}")
        Mbad = {srt((k, r)): r}
        for j in range(1, r + 1): Mbad[srt((k + j, r - j))] = (Mbad.get(srt((k + j, r - j)), 0) + L(j + 1, k - r + j, t0)) % p
        Rneg.chk(all(c[1] == Mbad.get(mu, 0) for mu, c in d.items()), "")
        # D_k(e_r) = [eps]E_k(e_r) both orders (symmetry M_kr = M_rk): E_r(e_k) vs E_k(e_r)
        ctx = Ctx(1, t0, 2)
        if n <= 8:
            d1 = EkF(ctx, k, base_eprod([r]), n); d2 = EkF(ctx, r, base_eprod([k]), n)
            R.chk(all(d1[m][1] == d2[m][1] == M.get(m, 0) for m in d1), f"sym {k}{r}")
print(R); print(Rneg, "(expected FAIL)")
# consequence [(s-1)^1] e*_lam = sum_{i<j} M_{li lj} e_{lam minus}
R = Res("Prop3.3 consequence [(s-1)]e*_lam = sum_{i<j} M e_rest")
for n in range(2, NMAX + 1):
    for lam in partitions(n):
        if cost(lam) > 4e4: continue
        d = es(lam, t0, 2); pred = {}
        for i, j in itertools.combinations(range(len(lam)), 2):
            rest = tuple(lam[x] for x in range(len(lam)) if x not in (i, j))
            for mu, c in Mclosed(lam[i], lam[j], t0).items():
                kk = srt(mu + rest); pred[kk] = (pred.get(kk, 0) + c) % p
        R.chk(all(d[mu][1] == pred.get(mu, 0) for mu in d), f"{lam}")
print(R)
# ---------- Thm 3.2: D_k derivation; B(f,g) formula with f,g e-monomials ----------
R = Res("Thm3.2 D_k derivation & B(f,g)=sum M_kl df/de_k dg/de_l")
ctx = Ctx(1, t0, 2)
for n in range(3, 7):
    for k in range(1, n):
        for rest in partitions(n - k):
            if len(rest) < 2: continue
            d = EkF(ctx, k, base_eprod(list(rest)), n)
            pred = {}
            for i in range(len(rest)):
                oth = rest[:i] + rest[i + 1:]
                for mu, c in Mclosed(k, rest[i], t0).items():
                    kk = srt(mu + oth); pred[kk] = (pred.get(kk, 0) + c) % p
            R.chk(all(d[mu][1] == pred.get(mu, 0) for mu in d), f"D_{k} e_{rest}")
# star product of e-monomials f,g via inverse of C(s) (C(1)=I so C^-1 = I - eps C1)
def Cmat(dg):
    return {lam: es(lam, t0, 2) for lam in partitions(dg)}
def star_eps1(f, g):  # f,g partitions (e-monomials); returns [eps^1] of e_f * e_g (star) as dict
    Cf, Cg = Cmat(sum(f)), Cmat(sum(g))
    # e_f = e*_f - eps * sum_rho C1[f][rho] e*_rho  (mod eps^2)
    out = {}
    def add(d, c):
        for mu, v in d.items(): out[mu] = (out.get(mu, 0) + c * v) % p
    # e*_{f u g} first-order part
    add({mu: c[1] for mu, c in es(srt(f + g), t0, 2).items()}, 1)
    for rho, c in Cf[f].items():
        if c[1]: add({mu: x[0] for mu, x in es(srt(rho + g), t0, 2).items()}, -c[1])
    for rho, c in Cg[g].items():
        if c[1]: add({mu: x[0] for mu, x in es(srt(f + rho), t0, 2).items()}, -c[1])
    return out
def pd(f, k):  # d e_f / d e_k as dict
    out = {}
    for i, x in enumerate(f):
        if x == k:
            r = f[:i] + f[i + 1:]; out[r] = out.get(r, 0) + 1; 
    return {r: c // max(1, 1) for r, c in out.items()}
def pd(f, k):
    c = f.count(k)
    if not c: return {}
    r = list(f); r.remove(k); return {tuple(r): c}
cnt = 0
for nf in range(1, 4):
    for ng in range(1, 4):
        for f in partitions(nf):
            for g in partitions(ng):
                lhs = star_eps1(f, g); pred = {}
                for k in set(f):
                    for l in set(g):
                        for a, x in pd(f, k).items():
                            for b, y in pd(g, l).items():
                                for mu, c in Mclosed(k, l, t0).items():
                                    kk = srt(mu + a + b); pred[kk] = (pred.get(kk, 0) + x * y * c) % p
                R.chk(all(lhs.get(mu, 0) % p == pred.get(mu, 0) for mu in set(lhs) | set(pred)), f"B({f},{g})")
print(R)
# ---------- Thm 3.4 block valuation law ----------
R = Res("Thm3.4 val>=l-kappa all (lam,mu); = for mu>lam generic t and t=0; t=0 lead sign (-1)^(l-k), |.|>=1")
Rneg = Res("Thm3.4 NEG: predict val = l-kappa+1 (should FAIL)")
sk = []
for n in range(2, NMAX + 1):
    for lam in partitions(n):
        if cost(lam) > 4e4: sk.append(lam); continue
        l = len(lam)
        for tt in (t0, 0):
            d = es(lam, tt, l + 2)
            for mu in partitions(n):
                c = d[mu]; kp = kappa(lam, mu)
                if kp < 0: R.chk(not any(c), f"nondom {lam}{mu}"); continue
                R.chk(val(c) >= l - kp, f"lb {lam}{mu}")
                if mu != lam:
                    R.chk(val(c) == l - kp, f"eq {lam}{mu} t={tt} val={val(c)} pred={l-kp}")
                    Rneg.chk(val(c) == l - kp + 1, "")
                    if tt == 0:
                        v = sym(c[l - kp]); R.chk(v * (-1) ** (l - kp) >= 1, f"t0 lead {lam}{mu} {v}")
print(R, "skipped:", sk); print(Rneg, "(expected FAIL)")
