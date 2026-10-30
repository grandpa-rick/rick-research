"""Independent check of Rem 4.21 (rem:LS12) from printed statements.
LS12 (3.6): [L^{-lam}][O_z] = sum_{w>=z} sum_{p in D_{w,z}} (-1)^{l(w)-l(z)} e^{-p(1)} [O_w],
D_{w,z} = {p LS path shape lam : iota(p) <= w W_lam, dn(w,p) = z}.
Thm 4.20: A_{kappa rho} = (-1)^{|theta|} sum_{V-maps g} e^{v_kappa + sum_{g(x)=o} beta(x)}.
Dictionary (Rem 4.21): G/B^- -> G/B, gB^- -> g w0 B; LS X_w <-> closure(B w w0 B/B).
"""
import itertools, sys
from fractions import Fraction as Fr
from collections import Counter

def setup(m):
    # signed permutations: w = tuple of (perm, signs); represent as matrix action on Z^m:
    # w(e_i) = s_i * e_{p(i)}. Store as tuple img where img[i] = (p(i), s_i).
    W = []
    for p in itertools.permutations(range(m)):
        for s in itertools.product((1, -1), repeat=m):
            W.append(tuple(zip(p, s)))
    def act(w, mu):
        out = [0]*m
        for i, (j, s) in enumerate(w):
            out[j] += s*mu[i]
        return tuple(out)
    def mul(u, v):  # (uv)(e_i) = u(v(e_i))
        res = []
        for i in range(m):
            j, s = v[i]
            k, t = u[j]
            res.append((k, s*t))
        return tuple(res)
    # positive roots (as vectors) and coroots
    pos = []
    for i in range(m):
        for k in range(i+1, m):
            r = [0]*m; r[i] = 1; r[k] = -1; pos.append(tuple(r))
            r = [0]*m; r[i] = 1; r[k] = 1; pos.append(tuple(r))
        r = [0]*m; r[i] = 2; pos.append(tuple(r))
    def corootpair(mu, beta):
        # <mu, beta^vee>, beta^vee = 2 beta/(beta,beta)
        bb = sum(x*x for x in beta)
        return Fr(2*sum(a*b for a, b in zip(mu, beta)), bb)
    posset = set(pos)
    def length(w):
        c = 0
        for b in pos:
            wb = act(w, b)
            if wb not in posset:
                c += 1
        return c
    def refl(beta):
        # s_beta as signed perm: s_beta(e_i) = e_i - <e_i, beta^vee> beta
        img = []
        for i in range(m):
            e = [0]*m; e[i] = 1
            c = corootpair(e, beta)
            v = [Fr(e[t]) - c*beta[t] for t in range(m)]
            j = [t for t in range(m) if v[t] != 0]
            assert len(j) == 1
            img.append((j[0], int(v[j[0]])))
        return tuple(img)
    L = {w: length(w) for w in W}
    R = [refl(b) for b in pos]
    # Bruhat order: u < u t with l(ut) > l(u); transitive closure
    up = {w: set() for w in W}
    for w in W:
        for t in R:
            wt = mul(w, t)
            if L[wt] > L[w]:
                up[w].add(wt)
    order = sorted(W, key=lambda w: -L[w])
    above = {}
    for w in order:  # longest first
        s = {w}
        for v in up[w]:
            s |= above[v]
        above[w] = s
    def leq(u, v):
        return v in above[u]
    return dict(W=W, act=act, mul=mul, pos=pos, L=L, leq=leq, refl=refl, R=R, cp=corootpair)

def run(m, variant="printed"):
    S = setup(m)
    W, act, mul, L, leq, cp = S['W'], S['act'], S['mul'], S['L'], S['leq'], S['cp']
    om = tuple([1]*m)
    w0 = tuple((i, -1) for i in range(m))
    # cosets W/W_P by w(omega)
    coset = {}
    for w in W:
        coset.setdefault(act(w, om), []).append(w)
    minrep = {mu: min(ws, key=lambda w: L[w]) for mu, ws in coset.items()}
    maxrep = {mu: max(ws, key=lambda w: L[w]) for mu, ws in coset.items()}
    mus = list(coset)
    # Bruhat order on W/W_P via min reps (LS12 Section 3.1)
    def cleq(a, b):
        return leq(minrep[a], minrep[b])
    # covers in W/W_lambda and bonds, computed from roots
    def cover(sig, tau):  # sig > tau cover
        if not (cleq(tau, sig) and L[minrep[sig]] == L[minrep[tau]] + 1):
            return None
        for b in S['pos']:
            if act(S['refl'](b), tau) == sig:
                return b
        raise RuntimeError
    covers = {}
    for a in mus:
        for b in mus:
            if a != b:
                beta = cover(a, b)
                if beta is not None:
                    covers[(a, b)] = abs(cp(b, beta))  # bond <kappa_k(lam), beta^vee>
    # a-chain existence for (sig, tau), a = 1/2 (only possibility for bonds 1,2 and a in (0,1)): DFS
    def achain(sig, tau, a):
        if sig == tau:
            return True
        for (x, y), bond in covers.items():
            if x == sig and (a*bond).denominator == 1 and cleq(tau, y):
                if achain(y, tau, a):
                    return True
        return False
    # LS paths of shape omega: generic enumeration over sequences with rationals; bonds <=2 => a must have a*b in Z
    # for some cover, so a in {1/2} (a*1 in Z impossible in (0,1)). Hence <=2 directions.
    paths = []
    for t in mus:
        paths.append(((t,), (Fr(1),)))
    for s1 in mus:
        for s2 in mus:
            if s1 != s2 and cleq(s2, s1) and achain(s1, s2, Fr(1, 2)):
                paths.append(((s1, s2), (Fr(1, 2), Fr(1, 2))))
    def endpoint(p):
        dirs, lens = p
        return tuple(sum(l*d[i] for d, l in zip(dirs, lens)) for i in range(m))
    def dn(w, tau):
        cands = [v for v in coset[tau] if leq(v, w)]
        assert cands
        mx = [v for v in cands if all(leq(u, v) for u in cands)]
        assert len(mx) == 1, "Deodhar max fails"
        return mx[0]
    def dnpath(w, p):
        for d in p[0]:
            w = dn(w, d)
        return w
    # (3.6): coefficient of [O_w] in [L^{-om}][O_z]
    def ls36(z):
        coeff = {}
        for w in W:
            if not leq(z, w):
                continue
            for p in paths:
                if cleq(p[0][0], act(w, om)) and dnpath(w, p) == z:
                    sgn = (-1)**(L[w]-L[z])
                    e = tuple(-x for x in endpoint(p))
                    coeff.setdefault(w, Counter())[e] += sgn
        return {w: c for w, c in coeff.items() if any(c.values())}
    # shifted shapes
    def strict_parts():
        res = []
        for r in range(m+1):
            for c in itertools.combinations(range(m, 0, -1), r):
                res.append(tuple(c))
        return res
    parts = strict_parts()
    def D(k):
        return {(a, a+d) for a, ka in enumerate(k) for d in range(ka)}
    def v(k):  # -1 in positions m+1-k (1-based)
        return tuple(-1 if (m - i) in k else 1 for i in range(m))
    def beta(x):
        a, b = x; d = b - a
        e = [0]*m
        if d == 0:
            e[m-1] = 1
        else:
            e[m-d-1] += 1; e[m-d] -= 1
        return tuple(e)
    def le(x, y):
        return x[0] <= y[0] and x[1] <= y[1]
    def A(k, r):
        th = sorted(D(k) - D(r))
        c = Counter()
        for g in itertools.product('eo', repeat=len(th)):
            G = dict(zip(th, g))
            if any(x[0] == x[1] and G[x] != 'e' for x in th):
                continue
            ok = all(not (x != y and le(x, y)) or (G[x] == 'e' and G[y] == 'o') for x in th for y in th)
            if not ok:
                continue
            e = list(map(Fr, v(k)))
            for x in th:
                if G[x] == 'o':
                    e = [e[i] + beta(x)[i] for i in range(m)]
            c[tuple(e)] += (-1)**len(th)
        return c
    # sanity: v_kappa = w_kappa omega with dim |kappa|
    for k in parts:
        assert L[minrep[v(k)]] == sum(k)
    # dictionary
    wP0 = None
    def zof(k):
        if variant == "printed":
            # pullback of X_k = closure B w_k w_{0,P} B/B; LS index w with w w0 = w_k w0P
            z = mul(maxrep[v(k)], w0)
            assert z == minrep[tuple(-x for x in v(k))]
            return z
        elif variant == "notwist":  # z_kappa omega = + v_kappa
            return minrep[v(k)]
    zinv = {zof(k): k for k in parts}
    npass = nfail = 0; monofail = 0; offrep = 0; pairfail = 0
    for k in parts:
        c = ls36(zof(k))
        for w, cw in c.items():
            if w not in zinv:
                offrep += 1
        for r in parts:
            exp = A(k, r) if set(D(r)) <= set(D(k)) else Counter()
            got = c.get(zof(r), Counter())
            got = Counter({kk: vv for kk, vv in got.items() if vv})
            exp = Counter({kk: vv for kk, vv in exp.items() if vv})
            if got == exp:
                npass += 1
            else:
                nfail += 1
                keys = set(got) | set(exp)
                monofail += sum(abs(got.get(x, 0) - exp.get(x, 0)) for x in keys)
    return dict(m=m, W=len(W), paths=len(paths), pairs=npass+nfail, pass_=npass, fail=nfail,
                monomial_diff=monofail, offrep_terms=offrep)

if __name__ == "__main__":
    for m in map(int, sys.argv[1:]):
        for var in ("printed", "notwist"):
            print(var, run(m, var), flush=True)
