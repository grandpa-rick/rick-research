import pickle, sys, time
from collections import defaultdict, Counter
from itertools import permutations
from q76t_s7 import rsk
from klfast import inv
from cox import pols, parse
n=int(sys.argv[1]); t=time.time()
good,Ptab=pickle.load(open(f'good{n}.pkl','rb'))
W=list(permutations(range(1,n+1)))
byP=defaultdict(list)
for w in W: byP[rsk(w)[0]].append(w)
pairs=[];own=[]
for (ci,P1),P2 in good.items():
    c=W[ci]
    if inv(c)<3: continue
    for X in byP[Ptab[P1]]:
        Y=tuple(c[v-1] for v in X); pairs.append((X,Y)); own.append((ci,P1))
print("pairs",len(pairs))
res=[parse(s) for s in pols(n,pairs)]
vals=defaultdict(set)
for k,r in zip(own,res): vals[k].add(r)
nontriv=[k for k in vals if vals[k]!={(1,)}]
viol=[k for k in vals if len(vals[k])>1]
print("n",n,"keys l(c)>=3:",len(vals),"nontrivial",len(nontriv),"VIOLATIONS",len(viol))
print("poly dist",Counter(tuple(sorted(v)) for v in vals.values()))
print("by l(c):",Counter((inv(W[k[0]]),tuple(sorted(vals[k]))) for k in vals))
for k in viol[:10]: print("VIOL c=",W[k[0]],Ptab[k[1]],vals[k])
pickle.dump((vals,),open(f'sep{n}.pkl','wb'))
print(time.time()-t)
