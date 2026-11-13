import random, time
from klfast import full_kl_fast, unpack
from cox import pols, parse
for n in (5,6,7):
    W,idx,ln,P=full_kl_fast(n); random.seed(3); prs=[]
    for y in random.sample(range(len(W)),min(150,len(W))):
        for x in random.sample(list(P[y]),min(20,len(P[y]))):
            if x!=y: prs.append((x,y))
    t=time.time(); r=pols(n,[(W[x],W[y]) for x,y in prs])
    bad=sum(1 for (x,y),s in zip(prs,r) if parse(s)!=unpack(P[y][x]))
    nt=sum(1 for (x,y) in prs if unpack(P[y][x])!=(1,))
    print(n,"checked",len(prs),"nontriv",nt,"bad",bad,time.time()-t)
