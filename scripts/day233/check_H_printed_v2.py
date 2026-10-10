# Day 233: Thm H (1),(2),(3) + Cor dmatrix (both formulas, N[t], t=1), re-implemented from the
# PRINTED text of longversion §5 (pdftotext), |mu|+k <= NMAX. Independent of lv_engine/check_*_printed:
#  - E_k from the printed subset formula, evaluated pointwise mod p, assembled into e-basis matrices;
#    s-dependence by exact interpolation (deg_s E_k e_mu <= |mu|), then composed as polynomial matrices.
#  - HL P_kappa(x;u) by Gram-Schmidt for <p_l,p_m>_u = delta z_l prod(1-u^{l_i})^{-1}  (Macdonald III (4.11)/(2.11)),
#    NOT via the Pieri rule. Kostka-Foulkes K(u) from s = K(u) P(u) (III (2.6)), interpolated in u, lifted to Z.
# Negative controls at the end must FAIL.
import itertools, random, sys
from functools import lru_cache
P_ = 2**31 - 1
NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 7
random.seed(233)
def inv(a): return pow(a % P_, P_ - 2, P_)

@lru_cache(None)
def parts(n, mx=None):
    if mx is None: mx = n
    if n == 0: return [()]
    out = []
    for f in range(min(n, mx), 0, -1):
        for r in parts(n - f, f): out.append((f,) + r)
    return out
def conj(l):
    return tuple(sum(1 for p in l if p > i) for i in range(l[0])) if l else ()
def nfun(l): return sum(i * p for i, p in enumerate(l))
def dom(a, b):  # a >= b in dominance (same size)
    sa = sb = 0
    for i in range(max(len(a), len(b))):
        sa += a[i] if i < len(a) else 0; sb += b[i] if i < len(b) else 0
        if sa < sb: return False
    return True
def mult(k, v): return sum(1 for p in k if p == v)

# ---------- linear algebra mod p ----------
def solve(M, B):  # M n x n, B n x r ; returns X with M X = B
    n = len(M); A = [list(M[i]) + list(B[i]) for i in range(n)]
    for c in range(n):
        piv = next(r for r in range(c, n) if A[r][c] % P_)
        A[c], A[piv] = A[piv], A[c]
        iv = inv(A[c][c]); A[c] = [x * iv % P_ for x in A[c]]
        for r in range(n):
            if r != c and A[r][c]:
                f = A[r][c]; A[r] = [(x - f * y) % P_ for x, y in zip(A[r], A[c])]
    return [row[n:] for row in A]
def interp(xs, ys):  # coefficients, lowest first
    n = len(xs); M = [[pow(x, j, P_) for j in range(n)] for x in xs]
    return [r[0] for r in solve(M, [[y] for y in ys])]
def lift(c): c %= P_; return c - P_ if c > P_ // 2 else c

# ---------- star side: E_k matrices in the e-basis, printed subset formula ----------
def esyms(xs):
    E = [1] + [0] * len(xs)
    for x in xs:
        for r in range(len(xs), 0, -1): E[r] = (E[r] + x * E[r - 1]) % P_
    return E
def e_at(nu, E):
    v = 1
    for q in nu: v = v * (E[q] if q < len(E) else 0) % P_
    return v
PTS = {}; EVINV = {}
def points(N):
    if N not in PTS:
        while True:
            pts = [[random.randrange(1, P_) for _ in range(N)] for _ in parts(N)]
            M = [[e_at(nu, esyms(x)) for nu in parts(N)] for x in pts]
            try:
                EVINV[N] = solve(M, [[int(i == j) for j in range(len(M))] for i in range(len(M))]); break
            except StopIteration: pass
        PTS[N] = pts
    return PTS[N]
def Ek_on_emu(k, mu, s, t, perturb=None):
    """e-coefficients (dict nu->val) of E_k e_mu in m=N=|mu|+k variables at (s,t), from the printed formula
       E_kF = sum_{|A|=k} c_A x_A F|_{x_i -> s x_i (i in A)},  c_A = prod_{i in A, j notin A} (x_i - t x_j)/(x_i - x_j)."""
    N = sum(mu) + k; pts = points(N); vals = []
    for x in pts:
        tot = 0
        for A in itertools.combinations(range(N), k):
            As = set(A); cA = 1
            for i in A:
                for j in range(N):
                    if j not in As: cA = cA * (x[i] - t * x[j]) % P_ * inv(x[i] - x[j]) % P_
            xA = 1
            for i in A: xA = xA * x[i] % P_
            sc = [s * x[i] % P_ if ((i in As) != (perturb == 'complement')) else x[i] for i in range(N)]
            tot = (tot + cA * xA % P_ * e_at(mu, esyms(sc))) % P_
        vals.append(tot)
    co = [sum(EVINV[N][i][j] * vals[j] for j in range(len(vals))) % P_ for i in range(len(vals))]
    return {nu: c for nu, c in zip(parts(N), co) if c}
SPTS = [random.randrange(1, P_) for _ in range(NMAX + 3)]
def Ek_poly(k, mu, t, perturb=None):
    """nu -> list of s-coefficients (exact mod p), degree <= |mu|; one extra point verifies the degree bound."""
    d = sum(mu); xs = SPTS[:d + 2]
    data = [Ek_on_emu(k, mu, s, t, perturb) for s in xs]
    out = {}
    for nu in parts(sum(mu) + k):
        ys = [D.get(nu, 0) for D in data]
        c = interp(xs[:d + 1], ys[:d + 1])
        assert sum(cc * pow(xs[d + 1], j, P_) for j, cc in enumerate(c)) % P_ == ys[d + 1], ('s-degree', k, mu, nu)
        if any(c): out[nu] = c
    return out
def padd(a, b):
    n = max(len(a), len(b)); return [((a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)) % P_ for i in range(n)]
def pmul(a, b):
    r = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b): r[i + j] = (r[i + j] + x * y) % P_
    return r
def val_s(c):
    for i, x in enumerate(c):
        if x % P_: return i
    return None

# ---------- HL side: P_kappa(x;u) by Gram-Schmidt, Schur by Kostka ----------
@lru_cache(None)
def Rpm(lam, mu):  # coefficient of x^mu in p_lam
    @lru_cache(None)
    def rec(i, rem):
        if i == len(lam): return int(all(r == 0 for r in rem))
        tot = 0
        for j in range(len(rem)):
            if rem[j] >= lam[i]:
                tot += rec(i + 1, rem[:j] + (rem[j] - lam[i],) + rem[j + 1:])
        return tot
    return rec(0, tuple(mu))
from math import factorial
from collections import Counter
def zlam(l):
    z = 1
    for v, m in Counter(l).items(): z *= v ** m * factorial(m)
    return z
def HLP(n, u):
    """dict kappa -> dict mu -> coeff of m_mu in P_kappa(x;u), mod p."""
    Ps = parts(n)[::-1]  # increasing lex order (extends dominance)
    R = [[Rpm(l, m) % P_ for m in Ps] for l in Ps]
    Rinv = solve(R, [[int(i == j) for j in range(len(Ps))] for i in range(len(Ps))])  # m = Rinv-transpose? p = R m => m = R^{-1} p
    # m_a = sum_l Rinv[a][l] p_l  (Rinv = R^{-1}, rows indexed by m, cols by p)
    zt = []
    for l in Ps:
        z = zlam(l) % P_
        for q in l: z = z * inv(1 - pow(u, q, P_)) % P_
        zt.append(z)
    G = [[sum(Rinv[a][l] * Rinv[b][l] % P_ * zt[l] for l in range(len(Ps))) % P_ for b in range(len(Ps))] for a in range(len(Ps))]
    out = {}
    for i, lam in enumerate(Ps):
        # P = m_i + sum_{j<i} a_j m_j, <P, m_r> = 0 for r<i
        if i == 0: out[lam] = {lam: 1}; continue
        M = [[G[j][r] for j in range(i)] for r in range(i)]
        B = [[-G[i][r] % P_] for r in range(i)]
        a = [r[0] for r in solve(M, B)]
        d = {lam: 1}
        for j in range(i):
            if a[j]: d[Ps[j]] = a[j]
        out[lam] = d
    return out
@lru_cache(None)
def kostka(nu, mu):  # SSYT shape nu content mu, via horizontal strips
    def hstrips(lam, r):  # partitions kappa ⊇ lam with kappa/lam horizontal r-strip
        L = list(lam) + [0]
        def rec(i, rem, cur):
            if i == len(L):
                if rem == 0: yield tuple(p for p in cur if p > 0)
                return
            hi = rem if i == 0 else min(rem, L[i - 1] - L[i])
            for a in range(hi + 1): yield from rec(i + 1, rem - a, cur + [L[i] + a])
        yield from rec(0, r, [])
    shapes = {(): 1}
    for r in mu:
        new = Counter()
        for sh, c in shapes.items():
            for k2 in hstrips(sh, r): new[k2] += c
        shapes = new
    return shapes.get(tuple(nu), 0)
def schur_m(nu):
    return {mu: kostka(nu, mu) for mu in parts(sum(nu)) if kostka(nu, mu)}
def m_coeffs_times_ek(F, k, n):
    """F: dict mu->coeff (monomial basis, degree n). Returns e_k * F in monomial basis, degree n+k:
       [x^kappa] e_k F = sum_{S ⊆ supp kappa, |S|=k} [x^{kappa-1_S}] F."""
    out = {}
    for kap in parts(n + k):
        tot = 0
        for S in itertools.combinations(range(len(kap)), k):
            b = list(kap)
            for i in S: b[i] -= 1
            b = tuple(sorted([q for q in b if q > 0], reverse=True))
            tot += F.get(b, 0)
        if tot % P_: out[kap] = tot % P_
    return out

# ---------- printed formulas ----------
def qbin(N, r, t):
    if r < 0 or r > N: return 0
    num = den = 1
    for i in range(r):
        num = num * (1 - pow(t, N - i, P_)) % P_; den = den * (1 - pow(t, i + 1, P_)) % P_
    return num * inv(den) % P_
def printed_3(mu, k, t, reverse=False):
    """Thm H(3): L_k bbar_mu = sum_{kappa/rho vert k-strip} t^{inv} prod_v [m_v(kappa), r_v] bbar_nu, rho=mu', kappa=nu'."""
    rho = conj(mu); out = {}
    for nu in parts(sum(mu) + k):
        kap = conj(nu); rr = list(rho) + [0] * (len(kap) - len(rho))
        if len(rr) > len(kap): continue
        diff = [a - b for a, b in zip(kap, rr)]
        if any(d not in (0, 1) for d in diff) or sum(diff) != k: continue
        r = Counter(kap[i] for i in range(len(kap)) if diff[i] == 1)  # r_v: rows of length v ending in strip box
        vals = set(kap)
        e = sum(r[v] * (mult(kap, w) - r[w]) for v in vals for w in vals if ((v < w) != reverse) and v != w)
        c = pow(t, e, P_)
        for v in vals: c = c * qbin(mult(kap, v), r[v], t) % P_
        if c: out[nu] = c
    return out

# ================= checks =================
log = []
def say(*a):
    s = ' '.join(str(x) for x in a); print(s); log.append(s); sys.stdout.flush()
TS = [random.randrange(2, P_) for _ in range(2)]
ok1 = ok3 = ok2 = True; ncase = 0; NC1 = NC2 = NC4 = False
EK = {}  # (t,k,mu) -> poly dict
for t in TS:
    ut = inv(t)
    HP = {n: HLP(n, ut) for n in range(0, NMAX + 1)}
    for N in range(1, NMAX + 1):
        for k in range(1, N + 1):
            for mu in parts(N - k):
                pol = Ek_poly(k, mu, t); EK[(t, k, mu)] = pol; ncase += 1
                Lk = {}
                for nu, c in pol.items():
                    sh = nfun(mu) - nfun(nu)  # b_nu coordinate = s^{n(mu)-n(nu)} c
                    v = val_s(c)
                    if v is None: continue
                    if v + sh < 0: ok1 = False; say('THM H(1) FAIL', k, mu, nu)
                    if sh <= 0 and -sh < len(c) and c[-sh]: Lk[nu] = c[-sh]  # value at s=0 of s^{sh} c(s)
                pr = printed_3(mu, k, t)
                if Lk != pr: ok3 = False; say('THM H(3) FAIL', t, k, mu, Lk, pr)
                if printed_3(mu, k, t, reverse=True) != Lk: NC1 = True
                # (2): phi(L_k bbar_mu) == t^{-C(k,2)} e_k phi(bbar_mu), phi(bbar_mu) = t^{-n(mu')} P_{mu'}(x;1/t)
                def phi(D, n, hp):
                    out = Counter()
                    for nu, c in D.items():
                        f = c * inv(pow(t, nfun(conj(nu)), P_)) % P_
                        for m_, a in hp[n][conj(nu)].items(): out[m_] = (out[m_] + f * a) % P_
                    return {m_: v for m_, v in out.items() if v}
                lhs = phi(Lk, N, HP)
                rhs0 = m_coeffs_times_ek(phi({mu: 1}, N - k, HP), k, N - k)
                f = inv(pow(t, k * (k - 1) // 2, P_))
                rhs = {m_: v * f % P_ for m_, v in rhs0.items() if v * f % P_}
                if lhs != rhs: ok2 = False; say('THM H(2) FAIL', k, mu)
                # NC2: phi with P(x;t) instead of P(x;1/t)
                if t == TS[0]:
                    HPw = {n: HLP(n, t) for n in (N, N - k)}
                    l2 = phi(Lk, N, HPw); r2 = m_coeffs_times_ek(phi({mu: 1}, N - k, HPw), k, N - k)
                    if l2 != {m_: v * f % P_ for m_, v in r2.items() if v * f % P_}: NC2 = True
say('NMAX=%d, t in %s: %d (k,mu) cases per t' % (NMAX, TS, ncase // len(TS)))
say('Thm H(1) [b-coords in Q[s,t], i.e. s^{n(nu)-n(mu)} | c]:', ok1)
say('Thm H(3) [printed vertical-strip matrix]:', ok3)
say('Thm H(2) [phi∘L_k = t^{-C(k,2)} e_k·phi, P by Gram-Schmidt]:', ok2)
say('NEG CONTROL NC1 (inv with v>w) detected a difference:', NC1)
say('NEG CONTROL NC2 (phi with P(x;t)) detected a difference:', NC2)
# NC4: perturbed operator (s-scaling on complement) must break (1) or (3)
bad = False
t = TS[0]
for (k, mu) in [(1, (1,)), (2, (1,)), (1, (2, 1)), (2, (2,))]:
    pol = Ek_poly(k, mu, t, perturb='complement'); Lk = {}
    viol = False
    for nu, c in pol.items():
        sh = nfun(mu) - nfun(nu); v = val_s(c)
        if v is not None and v + sh < 0: viol = True
        elif v is not None and sh <= 0 and -sh < len(c) and c[-sh]: Lk[nu] = c[-sh]
    if viol or Lk != printed_3(mu, k, t): bad = True
say('NEG CONTROL NC4 (s-scaling on complement) detected a difference:', bad)

# ---------- Cor dmatrix ----------
def estar_poly(lam, t):
    """c_{lam,mu}(s) as s-polynomials: e*_lam = E_{lam_1} ... E_{lam_l}(1), operators applied right to left."""
    cur = {(): [1]}
    for i in range(len(lam) - 1, -1, -1):
        k = lam[i]; new = {}
        for mu, c in cur.items():
            for nu, d in EK[(t, k, mu)].items():
                new[nu] = padd(new.get(nu, []), pmul(c, d))
        cur = {a: b for a, b in new.items() if any(b)}
    return cur
# exact Kostka-Foulkes K_{nu,kappa}(u) for n <= NMAX: interpolate s = K(u) P(u) in u
def KF_exact(n):
    Ps = parts(n); us = [random.randrange(2, P_) for _ in range(n * n // 2 + 3)]
    data = []
    for u in us:
        hp = HLP(n, u)
        # s_nu = sum_kappa K(u) P_kappa : solve in monomial basis
        M = [[hp[ka].get(mu, 0) for ka in Ps] for mu in Ps]
        B = [[schur_m(nu).get(mu, 0) % P_ for nu in Ps] for mu in Ps]
        X = solve(M, B)  # X[kappa][nu]
        data.append(X)
    K = {}
    for a, ka in enumerate(Ps):
        for b, nu in enumerate(Ps):
            c = interp(us, [D[a][b] for D in data])
            c = [lift(x) for x in c]
            while c and c[-1] == 0: c.pop()
            K[(nu, ka)] = c
    return K
def M01(lam, col):
    @lru_cache(None)
    def rec(i, cs):
        if i == len(lam): return int(all(c == 0 for c in cs))
        return sum(rec(i + 1, tuple(cs[j] - (j in S) for j in range(len(cs))))
                   for S in itertools.combinations(range(len(cs)), lam[i]) if all(cs[j] > 0 for j in S))
    return rec(0, tuple(col))
okA = okB = okC = okD = True; NC3 = False; okKF = True
for n in range(1, NMAX + 1):
    K = KF_exact(n)
    for nu in parts(n):  # sanity: K(0)=delta, K(1)=Kostka, coefficients >= 0, degree n(kappa)-n(nu)
        for ka in parts(n):
            c = K[(nu, ka)]
            if (c[0] if c else 0) != int(nu == ka) or sum(c) != kostka(nu, ka) or any(x < 0 for x in c): okKF = False
    for lam in parts(n):
        # second formula as an exact integer Laurent polynomial in t: t^{-n(lam')} sum_nu K_{nu',lam} t^{n(mu')} K_{nu,mu'}(1/t)
        for mu in parts(n):
            mp = conj(mu); poly = Counter(); polyNC = Counter()
            for nu in parts(n):
                a = kostka(conj(nu), lam)
                if not a: continue
                for j, c in enumerate(K[(nu, mp)]):
                    poly[nfun(mp) - j - nfun(conj(lam))] += a * c
                    polyNC[j - nfun(conj(lam))] += a * c
            poly = {e: c for e, c in poly.items() if c}
            if any(e < 0 or c < 0 for e, c in poly.items()): okC = False; say('N[t] FAIL', lam, mu, poly)
            if sum(poly.values()) != M01(lam, mp): okD = False; say('t=1 FAIL', lam, mu)
            for t in TS:
                ep = estar_poly(lam, t); c = ep.get(mu, [])
                d_ = c[nfun(mu)] if nfun(mu) < len(c) else 0
                if val_s(c) is not None and val_s(c) < nfun(mu): okA = False; say('DS valuation FAIL', lam, mu)
                # first formula: t^{n(mu')-n(lam')} [P_{mu'}(x;1/t)] e_lam   (solve in monomial basis)
                hp = HLP(n, inv(t)); Ps = parts(n)
                M = [[hp[ka].get(m_, 0) for ka in Ps] for m_ in Ps]
                elam = Counter({(): 1}); deg = 0
                for q in lam:
                    elam = Counter(m_coeffs_times_ek(dict(elam), q, deg)); deg += q
                X = solve(M, [[elam.get(m_, 0)] for m_ in Ps])
                f1 = pow(t, nfun(mp), P_) * inv(pow(t, nfun(conj(lam)), P_)) % P_ * X[Ps.index(mp)][0] % P_
                if f1 != d_ % P_: okA = False; say('FIRST FORMULA FAIL', lam, mu, t)
                f2 = sum(c * pow(t, e, P_) for e, c in poly.items()) % P_
                if f2 != d_ % P_: okB = False; say('SECOND FORMULA FAIL', lam, mu, t)
                ncv = sum(c * (pow(t, e, P_) if e >= 0 else inv(pow(t, -e, P_))) for e, c in polyNC.items()) % P_
                if ncv != d_ % P_: NC3 = True
            if lam == (1, 1, 1, 1) and mu == (2, 1, 1): say('remark: d_{(1^4),(2,1,1)} =', poly)
    say('n=%d done' % n)
say('Kostka-Foulkes engine sanity (K(0)=delta, K(1)=Kostka, coeffs>=0):', okKF)
say('Cor dmatrix first formula (pointwise, 2 random t):', okA)
say('Cor dmatrix second formula (cocharge KF, pointwise):', okB)
say('Cor dmatrix d in N[t]:', okC)
say('Cor dmatrix d(1) = #0-1 matrices rows lam cols mu\':', okD)
say('NEG CONTROL NC3 (K in place of cocharge K~) detected a difference:', NC3)
