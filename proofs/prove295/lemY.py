"""Lemma Y check (word level): for all weights mu!=nu and w in M_nu with Asc(w) subset S(mu), w in Y,
Y = words that miss a letter or violate first-occurrence / last-occurrence increasing order."""
import sys, itertools
from split import asc
def inY(w,n):
    if any(c not in w for c in range(1,n+1)): return True
    first=[w.index(c) for c in range(1,n+1)]; last=[len(w)-1-w[::-1].index(c) for c in range(1,n+1)]
    return not (first==sorted(first) and last==sorted(last))
def run(n,N):
    W=list(itertools.product(range(1,n+1),repeat=N))
    wt=lambda w: tuple(w.count(c) for c in range(1,n+1))
    mus=sorted({wt(w) for w in W}); bad=0; tot=0
    for mu in mus:
        v0=tuple(c for c in range(1,n+1) for _ in range(mu[c-1])); S=asc(v0)
        for w in W:
            if wt(w)!=mu and asc(w)<=S:
                tot+=1
                if not inY(w,n): bad+=1; print('VIOLATION',mu,w)
    print(n,N,'cross S-words',tot,'violations',bad,flush=True)
for a in sys.argv[1:]:
    n,N=map(int,a.split(',')); run(n,N)
