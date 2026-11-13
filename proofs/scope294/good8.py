import sys, pickle, time
from collections import defaultdict, Counter
from itertools import permutations
from q76t_s7 import rsk
from klfast import inv
n=int(sys.argv[1]); t=time.time()
W=list(permutations(range(1,n+1))); idx={w:k for k,w in enumerate(W)}
Rp=[];Rq=[]; Pid={}; Qid={}
for w in W:
    a,b=rsk(w); Rp.append(Pid.setdefault(a,len(Pid))); Rq.append(Qid.setdefault(b,len(Qid)))
L=[inv(w) for w in W]
byP=defaultdict(list)
for k in range(len(W)): byP[Rp[k]].append(k)
good={}
for P1,K in byP.items():
    for ci,c in enumerate(W):
        lc=L[ci]; P2=None; ok=True
        for x in K:
            X=W[x]; y=idx[tuple(c[v-1] for v in X)]
            if Rq[y]!=Rq[x] or L[y]!=L[x]+lc: ok=False;break
            if P2 is None: P2=Rp[y]
            elif Rp[y]!=P2: ok=False;break
        if ok: good[(ci,P1)]=P2
print("n",n,"good",len(good),"by l(c)",sorted(Counter(L[c] for c,_ in good).items()),time.time()-t)
Pinv={v:k for k,v in Pid.items()}
pickle.dump((good,{k:Pinv[k] for k in byP},),open(f'good{n}.pkl','wb'))
