from klo import *
from math import comb, factorial
CS={m:connected_shapes(m) for m in range(1,10)}
nsyt={}
def ns(c):
    if c not in nsyt: nsyt[c]=len(syt(cells_of(c)))
    return nsyt[c]
for n in range(2,10):
    cnt={'conn':0,'dr':0,'hyp':0}; mx=0; ds=[]
    for comps in all_shapes(n,CS):
        if len(comps)==1: cnt['conn']+=1; continue
        rib=[is_ribbon(c) for c in comps]
        if any(rib[j] and rib[j+1] for j in range(len(comps)-1)): cnt['dr']+=1; continue
        cnt['hyp']+=1
        sizes=[len(cells_of(c)) for c in comps]
        d=factorial(n)
        for c,m in zip(comps,sizes): d=d//factorial(m)*ns(c)
        ds.append(d)
    print(n,cnt,'max d hyp',max(ds) if ds else 0,'sum d^2',sum(x*x for x in ds))
