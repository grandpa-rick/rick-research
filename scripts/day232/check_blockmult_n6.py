# Day 232: thm:blockmult (longversion Thm 7.8) at n=6, PRINTED statement, NON-COARSENING pairs.
# LHS  [(s-1)^m] c_{lam,mu}, m = l(lam)-kappa, from the subset-formula engine (exact Fractions, s-interp).
# RHS  sum_{pi, |pi|=kappa} sum_{(nu^C): sqcup nu^C = mu, nu^C >= lam^C} prod_C [(s-1)^{|C|-1}] c_{lam^C,nu^C}.
# Also checks the printed side-claims: every nonzero factor has kappa(lam^C,nu^C)=1; LHS != 0 (Thm 6.6 equality).
# Negative control: multiply one factor of one term by (1+1/7) -> must FAIL.
import sys, os, time, itertools
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'day231'))
sys.argv = ['x', '1']                       # suppress the n<=N self-test inside check_leads_printed
import io, contextlib
with contextlib.redirect_stdout(io.StringIO()):
    from check_leads_printed import hexp, T0
from lv_engine import partitions, Fr
from check_DS_printed import dom
from check_blocklaw_printed import kappa, setparts

N = 6; t = T0
def srt(L): return tuple(sorted(L, reverse=True))
def coef1(lamC, nu):        # [(s-1)^{|C|-1}] c_{lamC,nu}
    if len(lamC) == 1: return Fr(1) if nu == lamC else Fr(0)
    return hexp(lamC, t)[nu][len(lamC) - 1]
def rhs(lam, mu, kap, perturb=False):
    l = len(lam); tot = Fr(0); bad = []; nterms = 0
    for pi in setparts(range(l)):
        if len(pi) != kap: continue
        subs = [srt([lam[i] for i in B]) for B in pi]
        def rec(i, rem):
            if i == len(subs): return [[]] if not rem else []
            out = []; nC = sum(subs[i]); seen = set()
            for r in range(1, len(rem) + 1):
                for idx in itertools.combinations(range(len(rem)), r):
                    nu = srt([rem[j] for j in idx])
                    if nu in seen or sum(nu) != nC or not dom(nu, subs[i]): continue
                    seen.add(nu); left = list(rem)
                    for q in nu: left.remove(q)
                    for tail in rec(i + 1, srt(left)): out.append([nu] + tail)
            return out
        for tup in rec(0, tuple(mu)):
            fs = [coef1(subs[i], tup[i]) for i in range(kap)]
            p = Fr(1)
            for f in fs: p *= f
            if p == 0: continue
            nterms += 1
            for i in range(kap):
                if len(subs[i]) > 1 and kappa(subs[i], tup[i]) != 1: bad.append((subs[i], tup[i]))
            if perturb and nterms == 1: p *= Fr(8, 7)
            tot += p
    return tot, bad, nterms

log = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'check_blockmult_n6.log'), 'w')
def say(*a):
    s = ' '.join(str(x) for x in a); print(s, flush=True); log.write(s + '\n'); log.flush()
T = time.time()
lams = sorted([l for l in partitions(N)], key=len)
pairs = []
for lam in lams:
    for mu in partitions(N):
        if mu == lam or not dom(mu, lam): continue
        k = kappa(lam, mu)
        if k >= 2 and k < len(mu): pairs.append((lam, mu, k))
say('n=6 t=%s: %d non-coarsening pairs with kappa>=2 (kappa=1 is the trivial one-block case)' % (t, len(pairs)))
ok = True; done = 0; negok = None
for lam, mu, k in pairs:
    t0 = time.time(); m = len(lam) - k
    L = hexp(lam, t)[mu][m]
    R, bad, nt = rhs(lam, mu, k)
    good = (L == R) and not bad and L != 0
    ok &= good; done += 1
    say('%s %s kappa=%d m=%d terms=%d LHS=%s RHS=%s %s%s  [%.0fs, total %.0fs]' % (lam, mu, k, m, nt, L, R,
        'OK' if good else 'FAIL', (' badkappa=' + str(bad)) if bad else '', time.time() - t0, time.time() - T))
    if negok is None and nt >= 1:
        Rn, _, _ = rhs(lam, mu, k, perturb=True)
        negok = (Rn != L); say('  negative control (one term x 8/7) on', lam, mu, ': fails as it should =', negok)
say('thm:blockmult n=6 non-coarsening, kappa>=2: %d/%d pairs, all OK = %s; negative control = %s; %.0fs' % (done, len(pairs), ok, negok, time.time() - T))
