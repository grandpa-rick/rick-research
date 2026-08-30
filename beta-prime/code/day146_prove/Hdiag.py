"""H = tau(F_P)/F_P at (U,V)=(0,0) i.e. (E1,E2)=(-2,1); tau image (E1,E2)=(1,0), E3 unshifted
(since phi_1 = E2+E1+1 = 0 there).  Check order and compute diagonal h_j = [E3^j T^{3j}] H."""
from core import *
from fractions import Fraction
import math, sys
BMAX=int(sys.argv[1]) if len(sys.argv)>1 else 24
P=build_P(BMAX)
def series(e1,e2):
    return {b:{k:Fraction(v,math.factorial(b)) for k,v in subs_E12(P[b],e1,e2).items()} for b in range(BMAX+1)}
FP  = series(-2,1)
FPt = series(1,0)

def smul(A,B,N):
    R=defaultdict(lambda: defaultdict(Fraction))
    for b1,d1 in A.items():
        if b1>N: continue
        for b2,d2 in B.items():
            if b1+b2>N: continue
            for k1,v1 in d1.items():
                for k2,v2 in d2.items(): R[b1+b2][k1+k2]+=v1*v2
    return {b:{k:v for k,v in d.items() if v} for b,d in R.items()}
def sinv(A,N):
    # A[0]={0:1}
    B={0:{0:Fraction(1)}}
    for n in range(1,N+1):
        acc=defaultdict(Fraction)
        for j in range(1,n+1):
            for k1,v1 in A.get(j,{}).items():
                for k2,v2 in B.get(n-j,{}).items(): acc[k1+k2]-=v1*v2
        B[n]={k:v for k,v in acc.items() if v}
    return B
H=smul(FPt,sinv(FP,BMAX),BMAX)
def v3f(fr):
    if fr==0: return None
    n,d=fr.numerator,fr.denominator; v=0
    while n%3==0: n//=3;v+=1
    while d%3==0: d//=3;v-=1
    return v
print("=== support check: [E3^k T^b] H nonzero only for b>=3k ? ===")
bad=[]
for b in range(BMAX+1):
    for k,v in H.get(b,{}).items():
        if v and b<3*k: bad.append((b,k,v))
print("violations:", bad[:8] if bad else "NONE  -> H has order >= 0")
print()
print("=== h_j = [E3^j T^{3j}] H ===")
hs=[]
for j in range(0, BMAX//3+1):
    v=H.get(3*j,{}).get(j,Fraction(0)); hs.append(v)
    print(f"  h_{j} = {v}   v3={v3f(v)}")

print()
print("=== v3([E3^k T^b] H): rows b, cols k ; '.'=zero ===")
mn=0
for b in range(0,BMAX+1):
    row=[]
    for k in range(0,b//2+1):
        v=H.get(b,{}).get(k,Fraction(0))
        if v==0: row.append('.')
        else:
            x=v3f(v); mn=min(mn,x); row.append(str(x))
    print(f"b={b:3d} "+' '.join(f"{s:>3}" for s in row))
print("min v3 over all coeffs of H:", mn)
