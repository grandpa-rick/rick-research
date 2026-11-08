import itertools,random
from kl import *
from parab import minrep,maxrep
from parab2 import run
random.seed(23)
for n in (5,6):
    W=list(itertools.permutations(range(1,n+1)))
    tests=bad=nt=0; nontrivdes=0; cache={}
    for _ in range(10 if n==5 else 3500):
        a,b=random.sample(W,2)
        if not leq(a,b): a,b=b,a
        if not leq(a,b): continue
        if b not in cache: cache[b]=kl_interval(tuple(range(1,n+1)),b)
        truth=cache[b][a]
        got,_,_=run(a,b,verbose=False)
        tests+=1; bad+=(got!=truth); nt+=(len(truth)>1)
        nontrivdes+= (len(ldes(b))>0 and len(rdes(b))>0)
    print('n',n,'random pairs',tests,'nontrivial P',nt,'z with nonempty L and R',nontrivdes,'mismatches',bad,flush=True)
