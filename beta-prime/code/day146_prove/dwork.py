"""Dwork test.  K(G) := G(T)^3 / G(T^3).  Since tau acts on coefficients only,
K(tau F_P) = tau(K(F_P)).  Dwork: H=tau(F_P)/F_P is in 1+T Z_3[[T]]  iff
tau(K)/K  in  1 + 3T Z_3[[T]],  where K := K(F_P).
Compute K and tau(K)/K at (U,V)=(0,0) [E1=-2,E2=1; shifted (1,0)]."""
from core import *
from fractions import Fraction as Q
import math,sys
BMAX=int(sys.argv[1]) if len(sys.argv)>1 else 24
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
def frob(A,N):  # G(T^3)
    return {3*b:d for b,d in A.items() if 3*b<=N}
def K(A,N):
    A3=smul(smul(A,A,N),A,N)
    return smul(A3, sinv(frob(A,N),N), N)
def v3(fr):
    if fr==0: return None
    n,d=fr.numerator,fr.denominator; v=0
    while n%3==0: n//=3;v+=1
    while d%3==0: d//=3;v-=1
    return v
Ka=K(FP,BMAX); Kb=K(FPt,BMAX)
R=smul(Kb,sinv(Ka,BMAX),BMAX)
print("=== v3 of coefficients of K = F_P(T)^3/F_P(T^3)  (rows b, cols E3-power) ===")
for b in range(0,min(BMAX,16)+1):
    print(f"b={b:3d} "+' '.join(f"{(v3(v) if v else '.'):>3}" for k,v in sorted(Ka.get(b,{}).items())) )
print()
print("=== tau(K)/K : need  in 1 + 3T Z_3[[T]] ===")
ok=True
for b in range(0,BMAX+1):
    for k,v in R.get(b,{}).items():
        need = 0 if b==0 else 1
        if v==0: continue
        if b==0 and k==0 and v==1: continue
        if v3(v) is not None and v3(v) < need:
            ok=False
            if b<12: print(f"   VIOLATION b={b} k={k} v={v} v3={v3(v)}")
print("tau(K)/K in 1+3T Z_3[[T]] :", "YES" if ok else "NO")
print("first few coeffs of tau(K)/K:")
for b in range(0,7):
    print("  b=%d"%b, {k:str(v) for k,v in sorted(R.get(b,{}).items())})
