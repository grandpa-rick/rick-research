"""Task 1/2: D(v) = Hcal(v)^3 / Hcal(v^3) over Q; v3 table."""
import json,sys
from fractions import Fraction as Q
fn=sys.argv[1] if len(sys.argv)>1 else "data_36.json"
h=[int(x) for x in json.load(open(fn))["h"]]
N=len(h)-1
def v3(x):
    if x==0: return None
    if isinstance(x,Q):
        n,d=x.numerator,x.denominator; v=0
        while n%3==0: n//=3;v+=1
        while d%3==0: d//=3;v-=1
        return v
    v=0
    while x%3==0: x//=3;v+=1
    return v
def mul(A,B,N):
    R=[Q(0)]*(N+1)
    for i,a in enumerate(A):
        if a==0: continue
        for j,b in enumerate(B):
            if i+j>N: break
            R[i+j]+=a*b
    return R
def inv(A,N):
    assert A[0]==1
    B=[Q(0)]*(N+1); B[0]=Q(1)
    for n in range(1,N+1):
        s=Q(0)
        for j in range(1,n+1): s+=A[j]*B[n-j]
        B[n]=-s
    return B
Hc=[Q(x) for x in h]
H3=mul(mul(Hc,Hc,N),Hc,N)                    # Hcal(v)^3
Hv3=[Q(0)]*(N+1)
for j in range(N+1):
    if 3*j<=N: Hv3[3*j]=Q(h[j])              # Hcal(v^3)
D=mul(H3,inv(Hv3,N),N)
print("N =",N)
print()
print("h_j and v3(h_j):")
for j,x in enumerate(h): print(f"  j={j:2d}  h={x:<22d} v3={v3(x)}")
print()
print("D = Hcal(v)^3/Hcal(v^3) coefficients (should be integers):")
nonint=[n for n in range(N+1) if D[n].denominator!=1]
print("  non-integer coefficients:", nonint if nonint else "NONE")
print()
print(" n |  v3(D_n) | D_n")
fails=[]
for n in range(N+1):
    c=D[n]
    vv=v3(c)
    if n>=1 and c!=0 and vv<1: fails.append(n)
    print(f"{n:2d} | {str(vv):>7} | {c}")
print()
print("D_0 =",D[0])
print("degrees n>=1 with v3 < 1 :", fails if fails else "NONE  -> D in 1+3v Z_3[[v]] PASSES")
print("v3 values for n=1..N:", [v3(D[n]) for n in range(1,N+1)])
