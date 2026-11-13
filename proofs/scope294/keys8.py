"""Original Q76-T' hypothesis at n=8 enumerated directly (all Q: x_Q<=y_Q Bruhat, const ldiff) vs good (c,P1)."""
import sys, pickle, time
from collections import defaultdict
from itertools import permutations
from q76t_s7 import rsk
from klfast import inv
n=int(sys.argv[1]); t=time.time()
W=list(permutations(range(1,n+1)))
def rankmat(w):
    n=len(w); M=[[0]*(n+1) for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,n+1): M[i][j]=M[i-1][j]+M[i][j-1]-M[i-1][j-1]+(1 if w[i-1]<=j and w[i-1]>j-1 else 0)
    return M
byQ=defaultdict(dict); RM={}; L={}
for w in W:
    a,b=rsk(w); byQ[b][a]=w
for w in W: RM[w]=rankmat(w); L[w]=inv(w)
def le(u,v):
    A=RM[u];B=RM[v]
    return all(A[i][j]>=B[i][j] for i in range(1,n+1) for j in range(1,n+1))
shapes=defaultdict(list)
for Q in byQ: shapes[tuple(map(len,Q))].append(Q)
keys=[]
for sh,Qs in shapes.items():
    Ps=list(byQ[Qs[0]].keys())
    for P1 in Ps:
        for P2 in Ps:
            d=None; ok=True
            for Q in Qs:
                x=byQ[Q][P1]; y=byQ[Q][P2]; dd=L[y]-L[x]
                if d is None: d=dd
                if dd!=d or dd<0 or not le(x,y): ok=False;break
            if ok:
                cs={tuple(byQ[Q][P2][byQ[Q][P1].index(v)] for v in range(1,n+1)) for Q in Qs}
                keys.append((P1,P2,d,len(cs)))
print("n",n,"original keys",len(keys),"keys with nonconstant c:",sum(1 for k in keys if k[3]>1),time.time()-t)
