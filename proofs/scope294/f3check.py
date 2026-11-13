"""F3: Q(kappa_i w) depends only on (Q(w),i); LemmaA: const ldiff alone => const c. (computed)"""
import sys
from collections import defaultdict
from itertools import permutations
from q76t_s7 import rsk
from klfast import inv
n=int(sys.argv[1])
W=list(permutations(range(1,n+1))); R={w:rsk(w) for w in W}
def kappa(w,i):  # window positions i,i+1,i+2 (1-based)
    a,b,c=w[i-1],w[i],w[i+1]; w=list(w)
    if (a>b)==(b>c): return None
    if min(a,b)<c<max(a,b): w[i-1],w[i]=w[i],w[i-1]     # xzy<->zxy
    elif min(b,c)<a<max(b,c): w[i],w[i+1]=w[i+1],w[i]   # yxz<->yzx
    else: raise Exception
    return tuple(w)
D={}; bad=0
for w in W:
    for i in range(1,n-1):
        v=kappa(w,i)
        if v is None: continue
        assert R[v][0]==R[w][0]
        k=(R[w][1],i)
        if k in D and D[k]!=R[v][1]: bad+=1
        D[k]=R[v][1]
print("n",n,"F3 violations",bad)
if n<=7:
    byQ=defaultdict(dict)
    for w in W: byQ[R[w][1]][R[w][0]]=w
    sh=defaultdict(list)
    for Q in byQ: sh[tuple(map(len,Q))].append(Q)
    cnt=0;badA=0
    for s,Qs in sh.items():
        Ps=list(byQ[Qs[0]])
        for P1 in Ps:
            for P2 in Ps:
                ds={inv(byQ[Q][P2])-inv(byQ[Q][P1]) for Q in Qs}
                if len(ds)==1:
                    cnt+=1
                    cs={tuple(byQ[Q][P2][byQ[Q][P1].index(v)] for v in range(1,n+1)) for Q in Qs}
                    badA+= len(cs)>1
    print("  const-ldiff keys",cnt,"with nonconstant c",badA)
