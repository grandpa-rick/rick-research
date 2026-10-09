# printed side-claim of thm:blockmult: for kappa=kappa(lam,mu)>=1, every pi with |pi|=kappa and every tuple
# (nu^C) with sqcup nu^C = mu, nu^C >= lam^C has kappa(lam^C,nu^C)=1 for all C. Pure combinatorics, n<=8.
import sys, os, itertools
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'day231'))
from fastmodp import partitions
from check_DS_printed import dom
from check_blocklaw_printed import kappa, setparts
from functools import lru_cache
K = lru_cache(None)(kappa)
def srt(L): return tuple(sorted(L, reverse=True))
N = int(sys.argv[1]); ok = True; cnt = 0
for n in range(2, N + 1):
  for lam in partitions(n):
    for mu in partitions(n):
      if mu == lam or not dom(mu, lam): continue
      k = K(lam, mu)
      for pi in setparts(range(len(lam))):
        if len(pi) != k: continue
        subs = [srt([lam[i] for i in B]) for B in pi]
        def rec(i, rem):
            if i == len(subs): return [[]] if not rem else []
            out = []; seen = set()
            for r in range(1, len(rem) + 1):
                for idx in itertools.combinations(range(len(rem)), r):
                    nu = srt([rem[j] for j in idx])
                    if nu in seen or sum(nu) != sum(subs[i]) or not dom(nu, subs[i]): continue
                    seen.add(nu); left = list(rem)
                    for q in nu: left.remove(q)
                    for tl in rec(i + 1, srt(left)): out.append([nu] + tl)
            return out
        for tup in rec(0, mu):
            cnt += 1
            if any(K(a, b) != 1 for a, b in zip(subs, tup)): ok = False; print('VIOLATION', lam, mu, subs, tup)
print('factor kappa=1 claim, n<=%d: %d (pi,tuple) terms, all kappa(lam^C,nu^C)=1: %s' % (N, cnt, ok))
