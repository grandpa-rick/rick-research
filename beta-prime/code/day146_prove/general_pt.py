"""At a base point (E1,E2): build F_P, tau(F_P) (shifted point AND E3 -> E3+phi1),
H = tau F_P / F_P, check integrality + order, diagonal Hcal, and verify
  F^2 - F = tau*Hcal*(2F-3),  with F from log F_P leading diagonal."""
from core import *
from fractions import Fraction as Q
import math,sys
BMAX=int(sys.argv[1]) if len(sys.argv)>1 else 20
E1v=Q(sys.argv[2]) if len(sys.argv)>2 else Q(-2)
E2v=Q(sys.argv[3]) if len(sys.argv)>3 else Q(1)
P=build_P(BMAX)
phi1=E2v+E1v+1
E1s=E1v+3; E2s=E2v+2*E1v+3      # shifted point
def spec(e1,e2):  # -> {b: {E3power: coeff}}
    return {b:{k:Q(v) for k,v in subs_E12(P[b],e1,e2).items()} for b in range(BMAX+1)}
raw=spec(E1v,E2v); raws=spec(E1s,E2s)
def shiftE3(d,c):   # substitute E3 -> E3 + c  in dict {power:coef}
    out=defaultdict(Q)
    for k,v in d.items():
        for i in range(k+1): out[i]+=v*math.comb(k,i)*c**(k-i)
    return {k:v for k,v in out.items() if v}
FP ={b:{k:v/math.factorial(b) for k,v in raw[b].items()} for b in range(BMAX+1)}
FPt={b:{k:v/math.factorial(b) for k,v in shiftE3(raws[b],phi1).items()} for b in range(BMAX+1)}
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
INV=sinv(FP,BMAX); H=smul(FPt,INV,BMAX); LG=slog(FP,BMAX)
def v3(fr):
    if fr==0: return 0
    n,d=fr.numerator,fr.denominator; v=0
    while n%3==0: n//=3;v+=1
    while d%3==0: d//=3;v-=1
    return v
print(f"### base (E1,E2)=({E1v},{E2v})  phi1={phi1}  shifted=({E1s},{E2s})")
badord=[(b,k) for b in H for k,v in H[b].items() if v and b<3*k]
print(" H order>=0 :", "OK" if not badord else f"VIOLATIONS {badord[:5]}")
badint=[(b,k,H[b][k]) for b in H for k,v in H[b].items() if v.denominator!=1]
print(" H integral :", "OK (all integer)" if not badint else f"NON-INTEGER e.g. {badint[:3]}")
bad3=[(b,k) for b in H for k,v in H[b].items() if v3(v)<0]
print(" H 3-integral:", "OK" if not bad3 else f"VIOLATIONS {bad3[:5]}")
# n_k , b_k  and h_j
K=(BMAX+1)//3
n=[Q(0)]+[LG.get(3*k-1,{}).get(k,Q(0)) for k in range(1,K+1)]
bk=[0]+[(3*k-1)*n[k] for k in range(1,K+1)]
h=[H.get(3*j,{}).get(j,Q(0)) for j in range(0,K+1)]
print(" b_k =", [str(x) for x in bk[1:]])
print(" h_j =", [str(x) for x in h])
# check  F^2 - F = tau*Hcal*(2F-3)  up to tau^K
Fc=[Q(0)]+[Q(bk[k]) for k in range(1,K+1)]
def mul(a,b,K):
    r=[Q(0)]*(K+1)
    for i in range(K+1):
        for j in range(K+1-i): r[i+j]+=a[i]*b[j]
    return r
F2=mul(Fc,Fc,K)
lhs=[F2[i]-Fc[i] for i in range(K+1)]
twoFm3=[Q(-3)]+[2*Fc[i] for i in range(1,K+1)]
rhs0=mul(h+[Q(0)]*(K+1-len(h)),twoFm3,K)
rhs=[Q(0)]+rhs0[:K]
print(" identity F^2-F = tau*Hcal*(2F-3):", "HOLDS" if lhs==rhs else f"FAILS lhs={lhs} rhs={rhs}")
