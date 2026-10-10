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
# ---------- Thm 3.8 W_k(J), literal polarization, engine ----------
R = Res("Thm3.8 W_k(J) = lin [..[E_k^(p),e_j1],..](1) = (-1)^p [n]/[k] prod [k]_{t^j}")
Wtab = {}
def W_engine(k, J, tt):
    n = k + sum(J); pP = len(J); ctx = Ctx(1, tt, pP + 1)
    tot = 0
    for T in subsets(J):
        S = [J[i] for i in range(pP) if i not in T]; TT = [J[i] for i in T]
        if S: continue  # lin(e_S * G) = 0 for S nonempty since G has no constant term -- verify below once
        d = EkF(ctx, k, base_eprod(TT), n)
        tot = (tot + (-1) ** (pP - len(T)) * d[(n,)][pP]) % p
    return tot
def W_closed(k, J, tt):
    n = k + sum(J); v = (-1) ** len(J) * tq(n, tt) * inv(tq(k, tt)) % p
    for j in J: v = v * tq(k, tt, j) % p
    return v
for k in range(1, 5):
    for pP in range(1, 4):
        for J in itertools.combinations_with_replacement(range(1, 4), pP):
            if k + sum(J) > 8: continue
            for tt in (t0, 0):
                w = W_engine(k, J, tt); Wtab[(k, J, tt)] = w
                R.chk(w == W_closed(k, J, tt), f"W_{k}{J}")
# verify the 'S nonempty terms vanish under lin' shortcut literally once
ctx = Ctx(1, t0, 3); k, J = 2, (1, 2); n = 5
full = 0
for T in subsets(J):
    S = [J[i] for i in range(2) if i not in T]; TT = [J[i] for i in T]
    d = EkF(ctx, k, base_eprod(TT), n - sum(S))
    # multiply by e_S and take lin: only possible if result is constant (never); compute explicitly
    prod = {}
    for mu, c in d.items():
        kk = srt(mu + tuple(S)); prod[kk] = (prod.get(kk, 0) + c[2]) % p
    full = (full + (-1) ** (2 - len(T)) * prod.get((n,), 0)) % p
R.chk(full == W_closed(2, (1, 2), t0), "literal polarization W_2(1,2)")
print(R)
# ---------- Thm 3.7 histories ----------
def histories(lam, tt):
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
            rec(i - 1, nb, w * W_closed(k, J, tt) % p, m + len(J))
    rec(len(lam) - 1, [], 1, 0); return out
R = Res("Thm3.7 coarsening: val=m, Lead = sum tight histories prod W; Lead(0)=(-1)^m #H")
Rneg = Res("Thm3.7 NEG: process lam_1..lam_l (wrong order) (should FAIL somewhere)")
sk = []
for n in range(2, NMAX + 1):
    for lam in partitions(n):
        if cost(lam) > 4e4: sk.append(lam); continue
        l = len(lam)
        for tt in (t0, 0):
            H = histories(lam, tt); Hrev = None
            for mu in partitions(n):
                if mu == lam or kappa(lam, mu) != len(mu): continue
                m = l - len(mu); c = es(lam, tt, m + 2)[mu]
                R.chk(val(c) == m, f"val {lam}{mu}")
                s_, cnt = H.get(mu, (0, 0))
                R.chk(c[m] == s_, f"Lead {lam}{mu} t={tt}")
                if tt == 0: R.chk(sym(c[m]) == (-1) ** m * cnt and cnt > 0, f"#H {lam}{mu}")
                if tt == t0:
                    if Hrev is None: Hrev = histories(tuple(reversed(lam)), tt)
                    Rneg.chk(c[m] == Hrev.get(mu, (0, 0))[0], "")
print(R, "skipped", sk); print(Rneg, "(expected FAIL)")
# ---------- Lemma 3.9 ----------
R = Res("Lemma3.9 lin T_k f = (-1)^d [n]/[k] f(1,t,..,t^{k-1}) (f=p_rho,e_rho,P_rho)")
Rneg = Res("Lemma3.9 NEG: drop (-1)^d")
for k in range(1, 5):
    for d_ in range(1, 5):
        n = k + d_
        if n > 8: continue
        for rho in partitions(d_):
            for kind in ("p", "e", "P"):
                if kind == "P" and len(rho) > k: continue
                if kind == "e" and rho[0] > k: continue
                g = {"p": lambda Y: pval(Y, rho), "e": lambda Y: eval_e(Y, rho), "P": lambda Y: P_at(rho, Y, t0)}[kind]
                eb = scalar_ebasis(n, n, lambda xb: T_at(k, g, xb, t0))
                pt = np.array([[pow(t0, i, p) for i in range(k)]], dtype=np.int64)
                rhs = (-1) ** d_ * tq(n, t0) * inv(tq(k, t0)) % p * int(g(pt)[0]) % p
                R.chk(eb[(n,)] == rhs, f"{k}{kind}{rho}"); Rneg.chk(eb[(n,)] == rhs * (-1) ** d_ % p, "")
print(R); print(Rneg, "(expected FAIL)")
# ---------- Thm 4.1 / cumulant / Cor 4.2 / separator ----------
t = sp.symbols('t')
def Kpoly(lam):
    l = len(lam); E = list(itertools.combinations(range(l), 2)); tot = 0
    for r in range(l - 1, len(E) + 1):
        for H in itertools.combinations(E, r):
            # connected?
            par = list(range(l))
            def f(x):
                while par[x] != x: x = par[x]
                return x
            for a, b in H: par[f(a)] = f(b)
            if len({f(x) for x in range(l)}) == 1:
                tot += sp.prod([t ** (lam[a] * lam[b]) - 1 for a, b in H])
    return sp.expand(tot)
def LeadG(lam):
    n = sum(lam); return (1 - t ** n) / sp.prod([1 - t ** x for x in lam]) * Kpoly(lam)
def ev(expr, tt):
    num, den = sp.fraction(sp.together(expr))
    return int(sp.Poly(num, t).eval(tt)) % p * inv(int(sp.Poly(den, t).eval(tt)) % p) % p
R = Res("Thm4.1 Lead_{lam,(n)} = (1-t^n)/prod(1-t^li) K_lam  & K = joint cumulant of t^{e2}")
Rneg = Res("Thm4.1 NEG: K over all graphs (not only connected)")
for n in range(2, NMAX + 1):
    for lam in partitions(n):
        if len(lam) < 2 or cost(lam) > 4e4: continue
        G = LeadG(lam)
        for tt in (t0, int(rng.integers(2, p))):
            R.chk(Lead(lam, (n,), tt) == ev(G, tt), f"{lam}")
        l = len(lam)
        allg = sp.prod([1 + (t ** (lam[a] * lam[b]) - 1) for a, b in itertools.combinations(range(l), 2)])
        Rneg.chk(Lead(lam, (n,), t0) == ev((1 - t ** n) / sp.prod([1 - t ** x for x in lam]) * allg, t0), "")
        # cumulant: sum_pi mu(pi) prod_B m(B), m(B)=t^{sum_{i<j in B} li lj}
        cum = 0
        for pi in setparts(list(range(l))):
            k_ = len(pi); mob = (-1) ** (k_ - 1) * math.factorial(k_ - 1)
            cum += mob * sp.prod([t ** sum(lam[a] * lam[b] for a, b in itertools.combinations(B, 2)) for B in pi])
        R.chk(sp.expand(cum - Kpoly(lam)) == 0, f"cumulant {lam}")
print(R); print(Rneg, "(expected FAIL)")
R = Res("Cor4.2 (a) 1^n: (-1)^{n-1}[n] I_n  (b) t=0 (-1)^{l-1}(l-1)!  (c) t->1 (-1)^{l-1} n^{l-1}  (d) sign")
def In(nn):  # Mallows-Riordan: trees on [nn] rooted at 1, inversions = pairs i<j with j ancestor of i
    tot = 0
    for par in itertools.product(range(nn), repeat=nn - 1):  # parent of vertices 1..nn-1 (0-indexed root 0)
        P_ = (None,) + par; ok = True
        for v in range(1, nn):
            seen = set(); x = v
            while x != 0:
                if x in seen: ok = False; break
                seen.add(x); x = P_[x]
            if not ok: break
        if not ok: continue
        inv_ = 0
        for v in range(1, nn):
            x = P_[v]
            while x is not None and x != 0:
                if x > v: inv_ += 1
                x = P_[x]
        tot += t ** inv_
    return sp.expand(tot)
for nn in range(2, 7):
    lam = (1,) * nn
    R.chk(sp.simplify(LeadG(lam) - (-1) ** (nn - 1) * sum(t ** i for i in range(nn)) * In(nn)) == 0, f"(a) n={nn}")
    R.chk(In(nn).subs(t, 1) == nn ** (nn - 2), "Cayley")
for n in range(2, 8):
    for lam in partitions(n):
        l = len(lam)
        if l < 2: continue
        G = sp.cancel(LeadG(lam))
        R.chk(G.subs(t, 0) == (-1) ** (l - 1) * math.factorial(l - 1), f"(b){lam}")
        R.chk(sp.limit(G, t, 1) == (-1) ** (l - 1) * n ** (l - 1), f"(c){lam}")
        R.chk(all(sp.sign(G.subs(t, sp.Rational(v))) == (-1) ** (l - 1) for v in ("1/3", "7/10", "2", "5")), f"(d){lam}")
        if cost(lam) <= 4e4: R.chk(Lead(lam, (n,), 1) == (-1) ** (l - 1) * n ** (l - 1) % p, f"(c) engine t=1 {lam}")
print(R)
J = sp.cancel(LeadG((1, 1, 1, 1)) * LeadG((2, 2)) / LeadG((2, 1, 1)) ** 2)
Jp = (t ** 2 + 1) * (t ** 3 + 3 * t ** 2 + 6 * t + 6) / ((t + 1) * (t ** 2 + t + 2) ** 2)
print(f"[{'PASS' if sp.simplify(J-Jp)==0 and J.subs(t,0)==sp.Rational(3,2) and sp.limit(J,t,1)==1 else 'FAIL'}] Rem4.3 separator J printed formula, J(0)=3/2, J(1)=1")
Jht = sp.cancel(sp.prod([t**nfun(conj(l_))*(t-1)**(1-len(l_))*Kpoly(l_) for l_ in [(1,1,1,1),(2,2)]])/(t**nfun(conj((2,1,1)))*(t-1)**(-2)*Kpoly((2,1,1)))**2)
print(f"[{'PASS' if sp.simplify(Jht-Jp)==0 else 'FAIL'}] Rem4.3 HT-gauge J (t^n(l') (t-1)^(1-l) K) equals J_star")
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
                seen[srt(tuple(srt(tuple(lam[i] for i in B)) for B in pi))] = v
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
