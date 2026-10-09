# thm:blockmult (longversion Thm 7.8) from the PRINTED statement, mod-p engine with m = max mu_1 variables.
# usage: python3 check_blockmult_fast.py N mode   (mode = noncoarse | all)
import sys, os, time, itertools
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'day231'))
from fastmodp_memo import *
from check_DS_printed import dom
from check_blocklaw_printed import kappa, setparts
N = int(sys.argv[1]); mode = sys.argv[2]
T0 = 3 * inv(5) % P          # t = 3/5, same as Day 231
TS = [T0, (P - 2) % P]       # and t = -2
def srt(L): return tuple(sorted(L, reverse=True))
def rhs(lam, mu, kap, t, m, perturb=False):
    l = len(lam); tot = 0; bad = []; nt = 0
    for pi in setparts(range(l)):
        if len(pi) != kap: continue
        subs = [srt([lam[i] for i in B]) for B in pi]
        def rec(i, rem):
            if i == len(subs): return [[]] if not rem else []
            out = []; seen = set(); nC = sum(subs[i])
            for r in range(1, len(rem) + 1):
                for idx in itertools.combinations(range(len(rem)), r):
                    nu = srt([rem[j] for j in idx])
                    if nu in seen or sum(nu) != nC or not dom(nu, subs[i]): continue
                    seen.add(nu); left = list(rem)
                    for q in nu: left.remove(q)
                    for tl in rec(i + 1, srt(left)): out.append([nu] + tl)
            return out
        for tup in rec(0, tuple(mu)):
            p = 1
            for lc, nu in zip(subs, tup):
                f = (1 if nu == lc else 0) if len(lc) == 1 else hexp(lc, t, m)[nu][len(lc) - 1]
                p = p * f % P
            if p == 0: continue
            nt += 1
            for lc, nu in zip(subs, tup):
                if len(lc) > 1 and kappa(lc, nu) != 1: bad.append((lc, nu))
            if perturb and nt == 1: p = p * 8 * inv(7) % P
            tot = (tot + p) % P
    return tot, bad, nt
logf = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'check_blockmult_memo_n%d_%s.log' % (N, mode)), 'w')
def say(*a):
    s = ' '.join(str(x) for x in a); print(s, flush=True); logf.write(s + '\n'); logf.flush()
T = time.time(); pairs = []
for lam in partitions(N):
    for mu in partitions(N):
        if mu == lam or not dom(mu, lam): continue
        k = kappa(lam, mu)
        if k < 2: continue
        if mode == 'noncoarse' and k == len(mu): continue
        pairs.append((lam, mu, k))
pairs.sort(key=lambda q: (len(q[0]), q[1][0]))
say('n=%d mode=%s: %d pairs with kappa>=2, %d non-coarsening; t in {3/5,-2} mod 2^61-1' %
    (N, mode, len(pairs), sum(1 for q in pairs if q[2] < len(q[1]))))
ok = True; done = 0; neg = None; zeros = []; nz_ok = True
for lam, mu, k in pairs:
    t1 = time.time(); m = mu[0]
    for t in TS:
        L = hexp(lam, t, m)[mu][len(lam) - k]
        R, bad, nt = rhs(lam, mu, k, t, m)
        good = L == R and not bad
        ok &= good
        if L == 0:
            zeros.append((lam, mu, 't=3/5' if t == T0 else 't=-2'))
            if t == T0: nz_ok = False
        if not good: say('FAIL', lam, mu, k, t, L, R, bad)
        if neg is None and nt >= 2:
            Rn, _, _ = rhs(lam, mu, k, t, m, perturb=True); neg = Rn != L
            say('  negative control on', lam, mu, '(one of %d terms x 8/7): fails =' % nt, neg)
    done += 1
    say('%s %s kappa=%d %s terms=%d %s [%.1fs, total %.0fs]' % (lam, mu, k, 'COARSE' if k == len(mu) else 'NONCOARSE',
        nt, 'OK' if good else 'FAIL', time.time() - t1, time.time() - T))
say('zero leads (identity holds as 0=0; Thm 6.6 promises nonzero only over Q(t), Open Problem (2)):', zeros)
say('lead nonzero at t=3/5 for every pair:', nz_ok)
say('thm:blockmult n=%d %s: %d/%d pairs at 2 values of t, all OK = %s; negative control = %s; %.0fs' %
    (N, mode, done, len(pairs), ok, neg, time.time() - T))
