from core import *
from fractions import Fraction as Q
import math,sys
BMAX=int(sys.argv[1]) if len(sys.argv)>1 else 21
P=build_P(BMAX)
def ser(e1,e2):
    return {b:{k:Q(v,math.factorial(b)) for k,v in subs_E12(P[b],e1,e2).items()} for b in range(BMAX+1)}
FP=ser(-2,1); FPt=ser(1,0)
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
H=smul(FPt,sinv(FP,BMAX),BMAX)
def frob(A,N): return {3*b:d for b,d in A.items() if 3*b<=N}
H3=smul(smul(H,H,BMAX),H,BMAX)
D=smul(H3,sinv(frob(H,BMAX),BMAX),BMAX)
def v3(fr):
    if fr==0: return None
    n,d=fr.numerator,fr.denominator; v=0
    while n%3==0: n//=3;v+=1
    while d%3==0: d//=3;v-=1
    return v
print("H(T)^3 / H(T^3):  v3 of each coefficient (need >=1 for b>=1)")
bad=[]
for b in range(0,BMAX+1):
    row=[]
    for k,v in sorted(D.get(b,{}).items()):
        vv=v3(v); row.append(f"{k}:{vv}")
        if b>=1 and vv is not None and vv<1: bad.append((b,k,v))
    print(f" b={b:3d} "+'  '.join(row))
print("VIOLATIONS:", bad[:6] if bad else "NONE -> consistent with Dwork")
