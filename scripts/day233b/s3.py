from util import *
import sys
NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 6
s0, t0 = int(rng.integers(2, p)), int(rng.integers(2, p))
def cost(lam): return math.prod(math.comb(sum(lam), k) for k in sorted(lam)[:-1]) if lam else 1
cache = {}
def es(lam, ss, tt, K=1):
    key = (lam, ss, tt, K)
    if key not in cache: cache[key] = estar(Ctx(ss, tt, K, maxe=len(lam) + 1), lam) if lam else {(): [1]+[0]*(K-1)}
    return cache[key]
def C(lam, mu, ss=s0, tt=t0, K=1, i=0):
    if sum(lam) != sum(mu): return 0
    return es(lam, ss, tt, K)[mu][i] if mu in es(lam, ss, tt, K) else 0
# ---------- Thm 5.1 Box Complement ----------
R = Res("Thm5.1 c_{N^l-lam,N^l-mu} = s^{N C(l,2)-(l-1)|lam|} c_{lam,mu}")
Rneg = Res("Thm5.1 NEG: exponent N C(l,2)-l|lam|")
for n in range(1, NMAX + 1):
    for lam in partitions(n):
        for l in (len(lam), len(lam) + 1):
            for N in (lam[0], lam[0] + 1):
                cl = srt(tuple(N - x for x in (lam + (0,) * (l - len(lam))))[::-1])
                if sum(cl) > 8 or sum(cl) == 0 or cost(cl) > 4e4 or cost(lam) > 4e4: continue
                for mu in partitions(n):
                    if len(mu) > l or mu[0] > N: continue
                    cm = srt(tuple(N - x for x in (mu + (0,) * (l - len(mu))))[::-1])
                    e = N * math.comb(l, 2) - (l - 1) * n
                    lhs = C(cl, cm); rhs = pow(s0, e % (p - 1), p) * C(lam, mu) % p
                    R.chk(lhs == rhs, f"{lam}{mu} N={N} l={l}")
                    if C(lam, mu): Rneg.chk(lhs == rhs * inv(pow(s0, n, p)) % p, "")
print(R); print(Rneg, "(expected FAIL)")
# ---------- Cor 5.2 Column Lemma + examples ----------
R = Res("Cor5.2 c_{lam+1^l,mu+1^l} = s^{C(l,2)} c_{lam,mu} (l>=l(lam)); examples")
for n in range(1, NMAX + 1):
    for lam in partitions(n):
        for l in (len(lam), len(lam) + 1):
            L1 = srt(tuple(x + 1 for x in lam + (0,) * (l - len(lam))))
            if sum(L1) > 8 or cost(L1) > 4e4: continue
            for mu in partitions(n):
                if len(mu) > l: continue
                M1 = srt(tuple(x + 1 for x in mu + (0,) * (l - len(mu))))
                R.chk(C(L1, M1) == pow(s0, math.comb(l, 2), p) * C(lam, mu) % p, f"{lam}{mu} l={l}")
ex = (1 + t0 + t0 * t0) * (t0 + 2) % p
for lam, mu in (((1, 1, 1), (3,)), ((2, 2, 2), (3, 3)), ((2, 2, 2), (4, 1, 1))):
    kp = kappa(lam, mu); m = len(lam) - kp
    R.chk(m == 2 and C(lam, mu, 1, t0, m + 1, m) == ex, f"example {lam}{mu} m={m}")
print(R)
# ---------- Thm 5.1 proof: inversion lemma E_{N-k} F = s^{m(N-k)-g} e_N^{m+1} (E_k G)(1/x) ----------
R = Res("Thm5.1 proof inversion lemma (N<=4)")
ctx = Ctx(s0, t0, 1, maxe=3)
for N in (2, 3, 4):
    for k in range(0, N + 1):
        for mpow_ in (0, 1):
            for Gp in [(1,), (2,), (1, 1), (2, 1)]:
                if Gp[0] > N: continue
                g = sum(Gp)
                def Fbase(ctx, xb, m, Gp=Gp, mpow_=mpow_, N=N):
                    X = ctx.coords(xb, m); Xi = sinv(X)
                    v = ctx.const(1, (xb.shape[0],))
                    for _ in range(mpow_): v = smul(v, esym(ctx, X, N))
                    for j in Gp: v = smul(v, esym(ctx, Xi, j))
                    return v
                xb = rng.integers(1, p, size=(4, N)).astype(np.int64); m0 = np.zeros((4, N), dtype=np.int64)
                lhs = evalE(ctx, [N - k], xb, m0, Fbase)[:, 0]
                xi = minv(xb)
                Ek = evalE(ctx, [k], xi, m0, base_eprod(list(Gp)))[:, 0]
                eN = e_scalar(xb, N)
                rhs = pow(s0, (mpow_ * (N - k) - g) % (p - 1), p) * mpow(eN, mpow_ + 1) % p * Ek % p
                R.chk(np.array_equal(lhs, rhs), f"N={N} k={k} m={mpow_} G=e{Gp}")
print(R)
# ---------- Thm 5.4 plethystic linear coefficient ----------
R = Res("Thm5.4 lin(e_k*G) = (-1)^d [k+d]/[k] G[(s-1)[k]_t]  (G=e_mu, p_mu, d<=5)")
Rneg = Res("Thm5.4 NEG: p_r -> (s-1)^r [k]_{t^r}")
ctx = Ctx(s0, t0, 1)
def pr_img(r, k, wrong=False):
    return ((pow(s0, r, p) - 1) if not wrong else pow(s0 - 1, r, p)) * tq(k, t0, r) % p
def G_eval(Gp_dict, k, wrong=False):
    tot = 0
    for rho, c in Gp_dict.items():
        v = c
        for r in rho: v = v * pr_img(r, k, wrong) % p
        tot = (tot + v) % p
    return tot
for k in range(1, 5):
    for d_ in range(1, 6):
        n = k + d_
        if n > 8: continue
        for mu in partitions(d_):
            for kind in ("e", "p"):
                base = base_eprod(list(mu)) if kind == "e" else base_pprod(list(mu))
                lin = EkF(ctx, k, base, n)[(n,)][0]
                Gp = ebasis_to_p({mu: 1}) if kind == "e" else {mu: 1}
                pref = (-1) ** d_ * tq(n, t0) * inv(tq(k, t0)) % p
                R.chk(lin == pref * G_eval(Gp, k) % p, f"k={k} {kind}{mu}")
                Rneg.chk(lin == pref * G_eval(Gp, k, True) % p, "")
print(R); print(Rneg, "(expected FAIL)")
# ---------- Cor 5.5 Pieri all s ----------
def pi_a(a, j, ss):  # [u^j] prod_{m<a} (1+s u t^m)/(1+u t^m)
    poly = [1] + [0] * j
    for m_ in range(a):
        tm = pow(t0, m_, p)
        # multiply by (1+s tm u)
        poly = [(poly[i] + (ss * tm * poly[i - 1] if i else 0)) % p for i in range(j + 1)]
        # divide by (1+tm u): series sum (-tm u)^i
        out = [0] * (j + 1)
        for i in range(j + 1):
            out[i] = (poly[i] - (tm * out[i - 1] if i else 0)) % p
        poly = out
    return poly[j]
def Cab(a, b, ss):
    if a == 0 or b == 0: return 1
    return (-1) ** b * tq(a + b, t0) * inv(tq(a, t0)) % p * pi_a(a, b, ss) % p
R = Res("Cor5.5 e_k*e_r = sum_y s^y C_{k-y,r-y} e_{k+r-y} e_y (k,r<=5)")
for k in range(1, 6):
    for r in range(1, 6):
        if k + r > 9: continue
        d = EkF(ctx, k, base_eprod([r]), k + r); pred = {}
        for y in range(0, min(k, r) + 1):
            kk = srt((k + r - y, y)); pred[kk] = (pred.get(kk, 0) + pow(s0, y, p) * Cab(k - y, r - y, s0)) % p
        R.chk(all(d[mu][0] == pred.get(mu, 0) for mu in d), f"{k},{r}")
# proof claim: d/ds pi_a(j) at s=1 = (-1)^{j-1} [a]_{t^j}; via finite difference in series: use exact derivative by linearity in s per factor
for a in range(1, 5):
    for j in range(1, 5):
        # pi_a(j) is a polynomial in s of degree <= j; derivative at 1 via interpolation at j+1 points
        xs = list(range(1, j + 3)); ys = [pi_a(a, j, x) for x in xs]
        # Lagrange derivative at s=1
        der = 0
        for i, xi_ in enumerate(xs):
            # derivative of basis l_i at 1
            num_terms = 0
            for q in range(len(xs)):
                if q == i: continue
                prod = 1
                for r_ in range(len(xs)):
                    if r_ in (i, q): continue
                    prod = prod * (1 - xs[r_]) % p
                num_terms = (num_terms + prod) % p
            den = 1
            for r_ in range(len(xs)):
                if r_ != i: den = den * (xi_ - xs[r_]) % p
            der = (der + ys[i] * num_terms * inv(den)) % p
        R.chk(der == (-1) ** (j - 1) * tq(a, t0, j) % p, f"dpi {a},{j}")
print(R)
