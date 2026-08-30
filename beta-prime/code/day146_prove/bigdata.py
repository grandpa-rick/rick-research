from core import *
from fractions import Fraction as Q
import math,sys,json
BMAX=36
P=build_P(BMAX)
raw ={b:{k:Q(v) for k,v in subs_E12(P[b],-2,1).items()} for b in range(BMAX+1)}
raws={b:{k:Q(v) for k,v in subs_E12(P[b],1,0).items()} for b in range(BMAX+1)}
FP ={b:{k:v/math.factorial(b) for k,v in raw[b].items()} for b in range(BMAX+1)}
FPt={b:{k:v/math.factorial(b) for k,v in raws[b].items()} for b in range(BMAX+1)}
def smul(A,B,N):
    R=defaultdict(lambda: defaultdict(Q))
    for b1,d1 in A.items():
        if b1>N: continue
        for b2,d2 in B.items():
            if b1+b2>N: continue
            for k1,v1 in d1.items():
                for k2,v2 in d2.items(): R[b1+b2][k1+k2]+=v1*v2
    return {b:{k:v for k,v in d.items() if v} for b,d in R.items()}
def sinv(A,N):
    B={0:{0:Q(1)}}
    for n in range(1,N+1):
        acc=defaultdict(Q)
        for j in range(1,n+1):
            for k1,v1 in A.get(j,{}).items():
                for k2,v2 in B.get(n-j,{}).items(): acc[k1+k2]-=v1*v2
        B[n]={k:v for k,v in acc.items() if v}
    return B
def slog(A,N):
    u={b:d for b,d in A.items() if b>=1}
    out=defaultdict(lambda: defaultdict(Q)); term={0:{0:Q(1)}}
    for m in range(1,N+1):
        term=smul(term,u,N)
        if not term: break
        c=Q((-1)**(m-1),m)
        for b,d in term.items():
            for k,v in d.items(): out[b][k]+=c*v
    return {b:{k:v for k,v in d.items() if v} for b,d in out.items()}
H=smul(FPt,sinv(FP,BMAX),BMAX); LG=slog(FP,BMAX)
K=(BMAX+1)//3
bk=[str((3*k-1)*LG.get(3*k-1,{}).get(k,Q(0))) for k in range(1,K+1)]
hj=[str(H.get(3*j,{}).get(j,Q(0))) for j in range(0,K+1)]
badint=[(b,k) for b in H for k,v in H[b].items() if v.denominator!=1]
badord=[(b,k) for b in H for k,v in H[b].items() if v and b<3*k]
print("BMAX",BMAX)
print("b_k:", bk)
print("h_j:", hj)
print("H integral up to T^%d:"%BMAX, "YES" if not badint else badint[:5])
print("H order>=0:", "YES" if not badord else badord[:5])
json.dump({"b":bk,"h":hj},open("data.json","w"))
