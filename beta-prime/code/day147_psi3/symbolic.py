"""Fully symbolic (E1,E2,E3 all free) Dwork check with varsigma = {WHICH}, order varsigma o tau."""
import sys, math
sys.path.insert(0,'/home/agent/projects/beta-prime/code/day146_prove')
from fractions import Fraction as Q
from collections import defaultdict
from core import build_P

N=int(sys.argv[1]) if len(sys.argv)>1 else 10
def mul(A,B):
    R=defaultdict(Q)
    for m1,c1 in A.items():
        for m2,c2 in B.items(): R[(m1[0]+m2[0],m1[1]+m2[1],m1[2]+m2[2])]+=c1*c2
    return {m:c for m,c in R.items() if c}
def add(*Xs):
    R=defaultdict(Q)
    for X in Xs:
        for m,c in X.items(): R[m]+=c
    return {m:c for m,c in R.items() if c}
def sc(k,A): return {m:k*c for m,c in A.items()} if k else {}
ONE={(0,0,0):Q(1)}
def MON(i,j,k,c=1): return {(i,j,k):Q(c)}
def subst(P,f1,f2,f3):
    ma=max((m[0] for m in P),default=0); mb=max((m[1] for m in P),default=0); mc=max((m[2] for m in P),default=0)
    A=[ONE];B=[ONE];C=[ONE]
    for _ in range(ma): A.append(mul(A[-1],f1))
    for _ in range(mb): B.append(mul(B[-1],f2))
    for _ in range(mc): C.append(mul(C[-1],f3))
    out={}
    for (i,j,k),co in P.items(): out=add(out, sc(Q(co), mul(mul(A[i],B[j]),C[k])))
    return out
# tau images
T1=add(MON(1,0,0),MON(0,0,0,3)); T2=add(MON(0,1,0),sc(Q(2),MON(1,0,0)),MON(0,0,0,3))
T3=add(MON(0,0,1),MON(0,1,0),MON(1,0,0),MON(0,0,0,1))
# psi^3 images
import os
WHICH=os.environ.get('LIFT','psi')
if WHICH=='psi':
    S1=add(MON(3,0,0),sc(Q(-3),MON(1,1,0)),sc(Q(3),MON(0,0,1)))
    S2=add(MON(0,3,0),sc(Q(-3),MON(1,1,1)),sc(Q(3),MON(0,0,2)))
    S3=MON(0,0,3)
elif WHICH=='naive':
    S1=MON(3,0,0); S2=MON(0,3,0); S3=MON(0,0,3)
else:
    S1=MON(1,0,0); S2=MON(0,1,0); S3=MON(0,0,3)   # E3only
# (psi^3 o tau)(E_i) = psi^3 applied AFTER tau : substitute E->psi^3 images into tau(E_i)
ST=[subst({m:Q(c) for m,c in X.items()},S1,S2,S3) for X in (T1,T2,T3)]
P=build_P(N)
def ser(imgs,M):
    return {n: sc(Q(1,math.factorial(n)), subst(P[n],*imgs)) for n in range(M+1)}
ID=[MON(1,0,0),MON(0,1,0),MON(0,0,1)]
F  =ser(ID,N); Ft=ser([T1,T2,T3],N)
Fs =ser([S1,S2,S3],N//3); Fts=ser(ST,N//3)
def Smul(A,B,M):
    R={}
    for n1,p in A.items():
        if n1>M: continue
        for n2,q in B.items():
            if n1+n2>M: continue
            R[n1+n2]=add(R.get(n1+n2,{}),mul(p,q))
    return {n:p for n,p in R.items() if p}
def Sinv(A,M):
    B={0:ONE}
    for n in range(1,M+1):
        acc={}
        for j in range(1,n+1):
            if j in A and (n-j) in B: acc=add(acc, mul(A[j],B[n-j]))
        B[n]=sc(Q(-1),acc)
    return {n:p for n,p in B.items() if p}
def Tc(A,M): return {3*n:p for n,p in A.items() if 3*n<=M}
K =Smul(Smul(Smul(F,F,N),F,N),   Sinv(Tc(Fs,N),N),N)
Kt=Smul(Smul(Smul(Ft,Ft,N),Ft,N),Sinv(Tc(Fts,N),N),N)
D =Smul(Kt,Sinv(K,N),N)
def v3(fr):
    n,d=fr.numerator,fr.denominator; v=0
    while n%3==0: n//=3;v+=1
    while d%3==0: d//=3;v-=1
    return v
ok=True
print(f"FULLY SYMBOLIC in Z[E1,E2,E3], varsigma = {WHICH}, order = varsigma o tau, N={N}")
print(" D[0] == 1 :", D.get(0)==ONE)
for n in range(1,N+1):
    vs=[v3(c) for c in D.get(n,{}).values()]
    mn=min(vs) if vs else None
    if mn is not None and mn<1: ok=False
    print(f"   T^{n:2d}: #monomials={len(D.get(n,{})):6d}  min v3 = {mn}")
print("==> criterion (symbolic):", "PASS" if ok else "FAIL")

import pickle
pickle.dump({n:{m:(c.numerator,c.denominator) for m,c in d.items()} for n,d in D.items()},
            open(f"D_{WHICH}.pkl","wb"))
