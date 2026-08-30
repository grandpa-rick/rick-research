"""How much of Conjecture H's evidence is NOT the diagonal (i.e. NOT circular with 3|b_k)?"""
import sys, math
sys.path.insert(0,'/home/agent/projects/beta-prime/code/day146_prove')
from core import build_P, subs_E12
from fractions import Fraction as Q
from collections import defaultdict
BMAX=int(sys.argv[1]) if len(sys.argv)>1 else 30
P=build_P(BMAX)
def ser(e1,e2):
    return {b:{k:Q(v,math.factorial(b)) for k,v in subs_E12(P[b],e1,e2).items()} for b in range(BMAX+1)}
FP,FPt=ser(-2,1),ser(1,0)
def mul(A,B,N):
    R=[defaultdict(Q) for _ in range(N+1)]
    for b1 in range(N+1):
        d1=A.get(b1)
        if not d1: continue
        for b2 in range(N+1-b1):
            d2=B.get(b2)
            if not d2: continue
            t=R[b1+b2]
            for k1,v1 in d1.items():
                for k2,v2 in d2.items(): t[k1+k2]+=v1*v2
    return {b:{k:v for k,v in d.items() if v} for b,d in enumerate(R)}
def inv(A,N):
    B={0:{0:Q(1)}}
    for n in range(1,N+1):
        acc=defaultdict(Q)
        for j in range(1,n+1):
            for k1,v1 in A.get(j,{}).items():
                for k2,v2 in B.get(n-j,{}).items(): acc[k1+k2]-=v1*v2
        B[n]={k:v for k,v in acc.items() if v}
    return B
H=mul(FPt,inv(FP,BMAX),BMAX)
tot=diag=offd=bad=ordbad=0
for b in range(BMAX+1):
    for k,v in H.get(b,{}).items():
        if v==0: continue
        tot+=1
        if b==3*k: diag+=1
        else: offd+=1
        if v.denominator!=1: bad+=1
        if b<3*k: ordbad+=1
print("BMAX=%d"%BMAX)
print("nonzero coefficients of H = tau(F_P)/F_P at (E1,E2)=(-2,1):", tot)
print("  on the l_0 diagonal (b=3k)      :", diag, " <- CIRCULAR with 3|b_k")
print("  OFF the diagonal                :", offd, " <- genuinely independent evidence for (H1)")
print("non-integral coefficients (H1 violations):", bad)
print("order<0 coefficients (H2 violations)     :", ordbad)
