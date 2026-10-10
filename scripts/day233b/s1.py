from util import *
import sys, time
NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 6
t0 = int(rng.integers(2, p))
def cost(lam): return math.prod(math.comb(sum(lam), k) for k in sorted(lam)[:-1])
CAP = 4e4
# ---------------- Thm 2.2 DS ----------------
R = Res("Thm2.2 DS (support=up-set, diag s^n(lam), s-val n(mu), c(1)=0, t=0 leads 1)")
Rneg = Res("Thm2.2 NEG control: claim s-val = n(lam) for mu!=lam (should FAIL often)")
dlead = {}
skipped = []
for n in range(1, NMAX + 1):
    for lam in partitions(n):
        if cost(lam) > CAP: skipped.append(lam); continue
        K = nfun(lam) + 3
        for tt in (t0, 0, 1):
            ctx = Ctx(0, tt, K, maxe=len(lam) + 1)
            d = estar(ctx, lam)
            for mu in partitions(n):
                c = d[mu]
                R.chk(all(x == 0 for x in c[nfun(lam) + 1:]), f"deg_s>n(lam) {lam}{mu}")
                if not dom(mu, lam): R.chk(not any(c), f"support {lam}{mu} t={tt}"); continue
                if mu == lam:
                    R.chk(c[nfun(lam)] == 1 and not any(c[:nfun(lam)]), f"diag {lam}"); continue
                R.chk(sum(c) % p == 0, f"c(1)!=0 {lam}{mu}")
                if tt != 1:
                    R.chk(val(c) == nfun(mu), f"sval {lam}{mu} t={tt} got {val(c)}")
                    Rneg.chk(val(c) == nfun(lam), "neg")
                if tt == 0: R.chk(c[nfun(mu)] == 1, f"t0 lead {lam}{mu}={sym(c[nfun(mu)])}")
                if tt == t0: dlead[(lam, mu)] = c[nfun(mu)]
                if tt == 1: dlead[(lam, mu, 1)] = c[nfun(mu)]
print(R); print(Rneg, "(expected FAIL)"); print("  skipped (cost):", skipped)
# ---------------- Remark 2.3 d-matrix ----------------
R = Res("Rem2.3 d(t)=t^{n(mu')-n(lam')} M(e,P)_{lam,mu'}(1/t); d(1)=#01-matrices")
Rneg = Res("Rem2.3 NEG: drop the t-power prefactor")
ti = inv(t0)
for n in range(1, min(NMAX, 6) + 1):
    N = n; kap = list(partitions(n)); Pn = len(kap) + 2
    xb = rng.integers(1, p, size=(Pn, N)).astype(np.int64)
    Pcols = np.array([P_at(k, xb, ti) for k in kap]).T
    for lam in partitions(n):
        sol = solve_mod(Pcols, eval_e(xb, lam).reshape(-1, 1))
        Mrow = {k: sol[i][0] for i, k in enumerate(kap)}
        for mu in partitions(n):
            if not dom(mu, lam) or (lam, mu) not in dlead: continue
            e = nfun(conj(mu)) - nfun(conj(lam))
            pred = pow(t0, e % (p - 1), p) * Mrow[conj(mu)] % p
            R.chk(pred == dlead[(lam, mu)], f"{lam}{mu}")
            Rneg.chk(Mrow[conj(mu)] == dlead[(lam, mu)], "")
            # 0-1 matrices with row sums lam, column sums mu'
            cs = conj(mu)
            def cnt(rows, cols):
                if not rows: return 1 if all(c == 0 for c in cols) else 0
                tot = 0
                for S in itertools.combinations(range(len(cols)), rows[0]):
                    if all(cols[j] > 0 for j in S):
                        tot += cnt(rows[1:], tuple(c - (j in S) for j, c in enumerate(cols)))
                return tot
            R.chk(cnt(lam, cs) % p == dlead[(lam, mu, 1)], f"d(1) {lam}{mu}")
print(R); print(Rneg, "(expected FAIL)")
