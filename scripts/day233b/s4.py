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
# ---- stability of T_a g in N (n vs n+1 vars) ----
R = Res("T_a g stable in N (n vs n+1 variables)")
for a, rho in ((2, (2, 1)), (3, (1, 1)), (1, (3,))):
    n = a + sum(rho); g = lambda Y: pval(Y, rho)
    e1 = scalar_ebasis(n, n, lambda xb: T_at(a, g, xb, t0)); e2 = scalar_ebasis(n, n + 1, lambda xb: T_at(a, g, xb, t0))
    R.chk(e1 == e2, f"{a}{rho}")
print(R)
# ---- <G,p_x p_y> = (-1)^n (m_xy [e_x e_y]G + lin G) ----
R = Res("Thm6.6 proof identity <G,p_xp_y> = (-1)^n (m_xy[e_xe_y]G + lin G)")
for n in range(2, 9):
    G = {mu: int(rng.integers(0, p)) for mu in partitions(n)}; Gp = ebasis_to_p(G)
    for y in range(1, n // 2 + 1):
        x = n - y
        R.chk(hall_pair_p(Gp, (x, y)) == (-1) ** n * (mxy(x, y) * G[srt((x, y))] + G[(n,)]) % p, f"{n}{x}{y}")
print(R)
# ---- Thm 6.2 constant-term adjoint formula ----
z = sp.symbols('z1:5'); ts = sp.Integer(t0)
def laurent_mul(A, B):
    out = {}
    for ea, ca in A.items():
        for eb, cb in B.items():
            k = tuple(i + j for i, j in zip(ea, eb)); out[k] = (out.get(k, 0) + ca * cb) % p
    return out
def poly_to_dict(expr, a):
    P_ = sp.Poly(sp.expand(expr), *z[:a]); out = {}
    for mon, c in P_.terms():
        num, den = sp.fraction(sp.Rational(c)) if c.is_Rational else (None, None)
        out[mon] = int(num) % p * inv(int(den)) % p
    return out
def gpoly(kind, rho, a, tt):
    if kind == "p": return sp.prod([sum(zi ** r for zi in z[:a]) for r in rho])
    if kind == "e": return sp.prod([sp.polys.specialpolys.symmetric_poly(r, *z[:a]) for r in rho])
    lam = tuple(rho) + (0,) * (a - len(rho)); tot = 0
    for w in itertools.permutations(range(a)):
        y = [z[i] for i in w]
        tot += sp.prod([y[i] ** lam[i] for i in range(a)]) * sp.prod([(y[i] - tt * y[j]) / (y[i] - y[j]) for i in range(a) for j in range(i + 1, a)])
    vl = 1
    for k, m in Counter(lam).items():
        for j in range(1, m + 1): vl *= (1 - tt ** j) / (1 - tt)
    return sp.cancel(sp.together(tot / vl))
R = Res("Thm6.2 phi_a <T_a g,F>_t = CT[Z g(z) F(1/z) Omega], Omega expanded in z_i/z_j (i<j)")
Rneg = Res("Thm6.2 NEG: expand Omega in z_j/z_i instead")
tsmall = 3  # exact small t for sympy P-polys; reduce mod p
for a in (1, 2, 3):
    for d_ in range(0, 4):
        n = a + d_
        for rho in (list(partitions(d_)) if d_ else [()]):
            for kind in ("p", "e", "P"):
                if kind == "P" and len(rho) > a: continue
                if kind == "e" and rho and rho[0] > a: continue
                if kind != "p" and not rho: continue
                eb, Gp = Tp(a, kind, rho, tsmall) if rho else (None, None)
                if not rho:  # g = 1
                    eb = scalar_ebasis(n, n, lambda xb: T_at(a, lambda Y: np.ones(Y.shape[0], dtype=np.int64), xb, tsmall)); Gp = ebasis_to_p(eb)
                gz = poly_to_dict(sp.prod(z[:a]) * gpoly(kind, rho, a, sp.Integer(tsmall)), a) if rho else poly_to_dict(sp.prod(z[:a]), a)
                for F in partitions(n):
                    Fp = {F: 1}
                    lhs = hl_pair_pp(Gp, Fp, tsmall)
                    for i in range(1, a + 1): lhs = lhs * (1 - pow(tsmall, i, p)) % p
                    # F(1/z) for p_F
                    Fz = {(0,) * a: 1}
                    for r in F:
                        Fz = laurent_mul(Fz, {tuple(-r if q == i else 0 for q in range(a)): 1 for i in range(a)})
                    prod = laurent_mul(gz, Fz)
                    for rev in (False, True):
                        B = n
                        Om = {(0,) * a: 1}
                        for i in range(a):
                            for j in range(i + 1, a):
                                fac = {}
                                for m_ in range(0, B + 1):
                                    w = 1 if m_ == 0 else (pow(tsmall, m_, p) - pow(tsmall, m_ - 1, p)) % p
                                    if rev: w = inv(tsmall) if m_ == 0 else (inv(pow(tsmall, m_ + 1, p)) - inv(pow(tsmall, m_, p))) % p
                                    e = [0] * a
                                    if not rev: e[i] += m_; e[j] -= m_
                                    else: e[i] -= m_; e[j] += m_
                                    fac[tuple(e)] = w
                                Om = laurent_mul(Om, fac)
                        ct = 0
                        for e, c in prod.items():
                            ct = (ct + c * Om.get(tuple(-x for x in e), 0)) % p
                        (Rneg if rev else R).chk(ct == lhs, f"a={a} {kind}{rho} F=p{F}")
print(R); print(Rneg, "(expected FAIL for a>=2)")
# ---- Thm 6.3 two-point formula ----
def Gcoef(kind, rho, A, Bv, tt):
    """coefficients of G_A(w) = g(1,t,..,t^{A-1}, w, wt, .., wt^{B-1}) via interpolation in w"""
    d_ = sum(rho); ws = [int(rng.integers(2, p)) for _ in range(d_ + 1)]
    pts = np.array([[pow(tt, i, p) for i in range(A)] + [w * pow(tt, i, p) % p for i in range(Bv)] for w in ws], dtype=np.int64)
    vals = {"p": lambda Y: pval(Y, rho), "e": lambda Y: eval_e(Y, rho), "P": lambda Y: P_at(rho, Y, tt)}[kind](pts)
    V = np.array([[pow(w, k, p) for k in range(d_ + 1)] for w in ws], dtype=np.int64)
    sol = solve_mod(V, vals.reshape(-1, 1)); return [s_[0] for s_ in sol]
def twopoint(kind, rho, a, x, y, tt):
    d_ = sum(rho); tot = 0
    for A in range(1, a):
        Bv = a - A; Gc = Gcoef(kind, rho, A, Bv, tt)
        G = lambda k: Gc[k] if 0 <= k < len(Gc) else 0
        term = G(y - Bv) * inv((1 - pow(tt, A, p)) * (1 - pow(tt, Bv, p))) % p
        sm = 0
        for m_ in range(1, y + 1):
            sm = (sm + (inv(pow(tt, A * m_, p)) - pow(tt, Bv * m_, p)) * G(y - Bv - m_)) % p
        term = (term + inv(1 - pow(tt, a, p)) * sm) % p
        tot = (tot + inv(pow(tt, A * Bv, p)) * term) % p
    pt = np.array([[pow(tt, i, p) for i in range(a)]], dtype=np.int64)
    gp = int({"p": lambda Y: pval(Y, rho), "e": lambda Y: eval_e(Y, rho), "P": lambda Y: P_at(rho, Y, tt)}[kind](pt)[0])
    tail = gp * inv(1 - pow(tt, a, p)) % p * sum(inv(pow(tt, j * y, p)) for j in range(a)) % p
    return (-1) ** a * (1 - pow(tt, x, p)) * (1 - pow(tt, y, p)) % p * ((tot - tail) % p) % p
R = Res("Thm6.3 two-point formula vs <T_a g, p_x p_y> (Hall), g=p,e,P")
Rneg = Res("Thm6.3 NEG: use <.,.>_t instead of Hall pairing")
for a in range(1, 5):
    for d_ in range(1, 5):
        n = a + d_
        if n > 8: continue
        for rho in partitions(d_):
            for kind in ("p", "e", "P"):
                if kind == "P" and len(rho) > a: continue
                if kind == "e" and rho[0] > a: continue
                eb, Gp = Tp(a, kind, rho)
                for y in range(1, n):
                    x = n - y
                    lhs = hall_pair_p(Gp, (x, y))
                    R.chk(lhs == twopoint(kind, rho, a, x, y, t0), f"a={a} {kind}{rho} ({x},{y})")
                    Rneg.chk(hl_pair_pp(Gp, {srt((x, y)): 1}, t0) == twopoint(kind, rho, a, x, y, t0), "")
print(R); print(Rneg, "(expected FAIL)")
# ---- Green dictionary remark ----
R = Res("Rem Green: Phi_a(P_rho;x,y) = (1-t^x)(1-t^y) X^lam_(x,y)/b_lam, lam=rho+1^a")
def Xgreen(lam, mu, tt, N):
    n = sum(lam); kap = [k for k in partitions(n) if len(k) <= N]; Pn = len(kap) + 2
    xb = rng.integers(1, p, size=(Pn, N)).astype(np.int64)
    sol = solve_mod(np.array([P_at(k, xb, tt) for k in kap]).T, pval(xb, mu).reshape(-1, 1))
    return {k: sol[i][0] for i, k in enumerate(kap)}[srt(lam)]
def phi(m, tt):
    v = 1
    for i in range(1, m + 1): v = v * (1 - pow(tt, i, p)) % p
    return v
def b(lam, tt):
    v = 1
    for k, m in Counter(lam).items(): v = v * phi(m, tt) % p
    return v
for a in range(1, 4):
    for d_ in range(0, 5):
        n = a + d_
        if n > 7: continue
        for rho in (list(partitions(d_)) if d_ else [()]):
            if len(rho) > a: continue
            lam = tuple(r + 1 for r in tuple(rho) + (0,) * (a - len(rho)))
            if rho: eb, Gp = Tp(a, "P", rho)
            else:
                eb = scalar_ebasis(n, n, lambda xb: T_at(a, lambda Y: np.ones(Y.shape[0], dtype=np.int64), xb, t0)); Gp = ebasis_to_p(eb)
            for y in range(1, n):
                x = n - y
                X = Xgreen(lam, srt((x, y)), t0, a)
                R.chk(hall_pair_p(Gp, (x, y)) == (1 - pow(t0, x, p)) * (1 - pow(t0, y, p)) % p * X % p * inv(b(lam, t0)) % p, f"{rho}->{lam} ({x},{y})")
print(R)
# ---- Example 6.4 two rows ----
R = Res("Ex6.4: G_1(w) formula; two-row X piecewise (|lam|<=10); JL Thm 2.6 all classes (n<=9); diagonal values")
for rho in [(2, 0), (3, 1), (4, 1), (2, 2), (5, 2), (1, 0)]:
    r = rho[0] - rho[1]
    for w in (int(rng.integers(2, p)),):
        lhs = int(P_at(rho, np.array([[1, w]], dtype=np.int64), t0)[0])
        if r == 0: rhs = pow(w, rho[1], p)
        else: rhs = pow(w, rho[1], p) * ((1 - t0 * w) - pow(w, r, p) * (w - t0)) % p * inv(1 - w) % p
        R.chk(lhs == rhs, f"G1 {rho}")
for n in range(2, 11):
    for l2 in range(1, n // 2 + 1):
        lam = (n - l2, l2)
        for y in range(1, n // 2 + 1):
            x = n - y; X = Xgreen(lam, srt((x, y)), t0, 2)
            if y < l2: pred = (t0 - 1) * pow(t0, l2 - 1 - y, p) * (1 + pow(t0, y, p)) % p
            elif y == l2: pred = (mxy(x, y) - (1 - t0) * pow(t0, l2 - 1, p)) % p
            else: pred = (t0 - 1) * pow(t0, l2 - 1, p) % p
            R.chk(X == pred, f"two-row {lam} ({x},{y})")
for n in range(2, 10):
    for k in range(0, n // 2 + 1):
        lam = srt((n - k, k))
        for rho in partitions(n):
            pis = [sum(1 for S in subsets(rho) if sum(rho[i] for i in S) == j) for j in range(k + 1)]
            pred = (pis[k] + (t0 - 1) * sum(pow(t0, k - 1 - j, p) * pis[j] for j in range(k))) % p
            R.chk(Xgreen(lam, rho, t0, 2) == pred, f"JL {lam} {rho}")
T = sp.symbols('T')
for l2 in (3, 5, 7):
    for m in (1, 2):
        v = T ** l2 - T ** (l2 - 1) + m
        if m == 1: R.chk(v.subs(T, -1) == -1 and v.subs(T, 0) == 1, f"diag {l2}")
print(R)
# ---- Gamma_a identity and Prop 6.1 ----
R = Res("Gamma_a two forms equal; Prop6.1 [(s-1)^2]c = [e_mu](Gamma_a(e_b,e_c)+D_aD_b(e_c)) all orderings, kappa=1")
ctx2 = Ctx(1, t0, 3)
def EkFd(k, js, n): return EkF(ctx2, k, base_eprod(list(js)), n)
def addto(D, src, c=1, idx=None, extra=()):
    for mu, v in src.items():
        x = v if idx is None else v[idx]
        kk = srt(mu + tuple(extra)); D[kk] = (D.get(kk, 0) + c * x) % p
for n in range(3, min(NMAX, 8) + 1):
    for lam in partitions(n):
        if len(lam) != 3: continue
        mus = [mu for mu in partitions(n) if kappa(lam, mu) == 1]
        if not mus: continue
        full = es(lam, t0, 3)
        for (a, b_, c) in set(itertools.permutations(lam)):
            G1 = {}
            addto(G1, EkFd(a, (b_, c), n), 1, 2)
            addto(G1, EkFd(a, (c,), a + c), -1, 2, (b_,))
            addto(G1, EkFd(a, (b_,), a + b_), -1, 2, (c,))
            G2 = {}
            for r in range(1, b_ + 1):
                for q in range(1, c + 1):
                    eb, _ = Tp(a, "p", srt((r, q)))
                    addto(G2, eb, (-1) ** (r + q), None, tuple(v for v in (b_ - r, c - q) if v))
            R.chk(all(G1.get(mu, 0) == G2.get(mu, 0) for mu in set(G1) | set(G2)), f"Gamma {a},{b_},{c}")
            Mbc = {mu: v[1] for mu, v in EkFd(b_, (c,), b_ + c).items()}
            DD = {}
            for nu, cf in Mbc.items():
                if cf: addto(DD, {mu: v[1] for mu, v in EkFd(a, nu, n).items()}, cf)
            for mu in mus:
                R.chk(full[mu][2] == (G1.get(mu, 0) + DD.get(mu, 0)) % p, f"Prop6.1 {lam} order {(a,b_,c)} mu={mu}")
print(R)
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
# ---- Example 6.8 ----
R = Res("Ex6.8 (3,3,3)->(7,2) and (4,4,2)->(7,3) printed leads; kappa=1")
for lam, mu, poly in (((3, 3, 3), (7, 2), lambda t: 2*t**13+3*t**12+3*t**11+6*t**10+6*t**9+6*t**8+9*t**7+6*t**6+3*t**5+9*t**4+6*t**3+3*t+4),
                      ((4, 4, 2), (7, 3), lambda t: (t+1)*(t**2+1)*(2*t**8+t**7+t**6+3*t**4+t**3+t**2-t+2))):
    R.chk(kappa(lam, mu) == 1, "kappa")
    for tt in (t0, int(rng.integers(2, p)), 0):
        c = es(lam, tt, 3)[mu]; R.chk(val(c) == 2 and c[2] == poly(tt) % p, f"{lam}{mu} t={tt}")
    R.chk(thm66(*lam, *mu, t0) == poly(t0) % p, f"thm66 formula {lam}")
print(R)
# ---- Open problems numerics ----
R = Res("Open2: t=-2, n=6: exactly 7 pairs with val > l-kappa; Lead_{111,3}=[3](2+t)")
cnt = 0
for lam in partitions(6):
    d = es(lam, -2, len(lam) + 2)
    for mu in partitions(6):
        if mu == lam or not dom(mu, lam): continue
        if val(d[mu]) > len(lam) - kappa(lam, mu): cnt += 1
R.chk(cnt == 7, f"count={cnt}")
print(R)
R = Res("Open3: l=3, mu=(n-1,1), kappa=1: Lead(1) = 2n^2-6n+3")
for n in range(4, NMAX + 1):
    for lam in partitions(n):
        if len(lam) != 3 or kappa(lam, (n - 1, 1)) != 1 or cost(lam) > 2e4: continue
        c = es(lam, 1, 3)[(n - 1, 1)]
        R.chk(val(c) == 2 and c[2] == (2 * n * n - 6 * n + 3) % p, f"{lam} {sym(c[2])}")
print(R)
