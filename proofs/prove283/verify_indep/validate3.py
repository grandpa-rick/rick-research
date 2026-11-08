import itertools,random,sys
from kl import *
from parab import *
random.seed(7)
for n in (5,6):
    W=list(itertools.permutations(range(1,n+1)))
    tests=0;bad={'q':0,'-1':0};incons={'q':0,'-1':0};nontriv=0;nontrivJ=0
    allJ=[J for r in range(n) for J in itertools.combinations(range(n-1),r)]
    cache={}
    trials=2500 if n==5 else 2600
    for _ in range(trials):
        J=random.choice(allJ[1:]) if random.random()<0.9 else ()
        a,b=random.sample(W,2)
        if not leq(a,b): a,b=b,a
        if not leq(a,b): continue
        xm,zm=maxrep(a,J),maxrep(b,J)
        if not leq(xm,zm): continue
        if zm not in cache: cache[zm]=kl_interval(minrep(a,J) if False else (1,)*0 or tuple(range(1,n+1)),zm)
        Pz=cache[zm]; truth=Pz[xm]
        tests+=1
        if len(truth)>1: nontriv+=1
        for u in ('q','-1'):
            try:
                PJ,_=Parab(J,u).P(minrep(a,J),minrep(b,J))
                if PJ[minrep(a,J)]!=truth: bad[u]+=1
            except ValueError: incons[u]+=1; bad[u]+=1
        # descent-invariance check (two-sided) within same pair
        for s in ldes(zm):
            if Pz.get(lswap(a,s) if leq(lswap(a,s),zm) else a, None) is None: pass
    print('n',n,'tests',tests,'nontrivial',nontriv,'mismatch',bad,'inconsistent',incons,flush=True)
