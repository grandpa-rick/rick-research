import itertools, random
from kl import *
from validate import brute
# 1. Bruhat leq vs transitive closure of reflection-covers (independent of tableau criterion), S5
for n in (4,5):
    W=list(itertools.permutations(range(1,n+1)))
    below={}
    for w in sorted(W,key=length):
        s={w}
        for c in lower_covers(w): s|=below[c]
        below[w]=s
    bad=sum(1 for u in W for v in W if leq(u,v)!=(u in below[v]))
    print('n',n,'leq vs cover-closure mismatches',bad,flush=True)
# 2. S5 all pairs, S6 random
for n,samp in ((5,None),(6,400)):
    W,le,P=brute(n)
    pairs=[(x,z) for z in W for x in W if le[(x,z)]]
    print('n',n,'comparable pairs',len(pairs),flush=True)
    random.seed(1)
    if samp: 
        # bias to long intervals
        pairs=random.sample(pairs,samp)+[(W[0],W[-1])]
    bad=0; nontriv=0
    for x,z in pairs:
        Q=kl_interval(x,z)
        if Q[x]!=P[(x,z)]: bad+=1
        if len(P[(x,z)])>1: nontriv+=1
    print('n',n,'checked',len(pairs),'nontrivial',nontriv,'mismatches',bad,flush=True)
