"""TWISTED Dwork check:  varsigma(E_i)=E_i^3  (naive lift).
K := F_P(T)^3 / varsigma(F_P)(T^3).   Need tau(K)/K in 1+3T Z_3[E3][[T]].
Base point (E1,E2)=(-2,1)  [phi_1=0];  tau-image (1,0).
varsigma of the base point: (-8,1);  varsigma of (1,0): (1,0)."""
import sys, math
sys.path.insert(0,'/home/agent/projects/beta-prime/code/day146_prove')
from core import build_P, subs_E12
from fractions import Fraction as Q
from collections import defaultdict
BMAX=int(sys.argv[1]) if len(sys.argv)>1 else 20
P=build_P(BMAX)
def ser(e1,e2,tw=1):
    return {b:{tw*k:Q(v,math.factorial(b)) for k,v in subs_E12(P[b],e1,e2).items()}
            for b in range(BMAX+1)}
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
def sub3(A,N): return {3*b:d for b,d in A.items() if 3*b<=N}
def v3(fr):
    if fr==0: return None
    n,d=fr.numerator,fr.denominator; v=0
    while n%3==0: n//=3;v+=1
    while d%3==0: d//=3;v-=1
    return v
def Kof(F, Fsig, N):
    F3=smul(smul(F,F,N),F,N)
    return smul(F3, sinv(sub3(Fsig,N),N), N)

# base point
F  = ser(-2,1)          # F_P
Fs = ser(-8,1,tw=3)     # varsigma(F_P):  E1,E2 -> cubes, E3 -> E3^3
# tau-shifted point (1,0)
G  = ser(1,0)
Gs = ser(1,0,tw=3)      # varsigma of (1,0) is (1,0)

Ka=Kof(F,Fs,BMAX); Kb=Kof(G,Gs,BMAX)
R=smul(Kb,sinv(Ka,BMAX),BMAX)
print("=== TWISTED  tau(K)/K : need coefficient v3 >= 1 for all b>=1 ===")
bad=[]
for b in range(1,BMAX+1):
    for k,v in sorted(R.get(b,{}).items()):
        if v and v3(v)<1: bad.append((b,k,v3(v)))
print("VIOLATIONS:", bad[:8] if bad else "NONE")
print("min v3 per b:")
for b in range(0,min(BMAX,15)+1):
    row=R.get(b,{})
    print(f"  b={b:2d}  "+ " ".join(f"{k}:{v3(v)}" for k,v in sorted(row.items()) if v))
