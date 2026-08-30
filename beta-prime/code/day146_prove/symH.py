"""Is H = tau(F_P)/F_P integral in Z[E1,E2,E3][[T]] (symbolically)?"""
from core import *
from verify_master import tau_op
from fractions import Fraction as Q
import math,sys
BMAX=int(sys.argv[1]) if len(sys.argv)>1 else 14
P=build_P(BMAX)
def qp(A): return {m:Q(c) for m,c in A.items()}
def qmul(A,B):
    R=defaultdict(Q)
    for m1,c1 in A.items():
        for m2,c2 in B.items(): R[(m1[0]+m2[0],m1[1]+m2[1],m1[2]+m2[2])]+=c1*c2
    return {m:c for m,c in R.items() if c}
def qadd(A,B):
    R=defaultdict(Q)
    for X in (A,B):
        for m,c in X.items(): R[m]+=c
    return {m:c for m,c in R.items() if c}
def qs(k,A): return {m:k*c for m,c in A.items()} if k else {}
FP={b:qs(Q(1,math.factorial(b)),qp(P[b])) for b in range(BMAX+1)}
FPt={b:qs(Q(1,math.factorial(b)),qp(tau_op(P[b]))) for b in range(BMAX+1)}
INV={0:{(0,0,0):Q(1)}}
for n in range(1,BMAX+1):
    acc={}
    for j in range(1,n+1): acc=qadd(acc,qs(Q(-1),qmul(FP[j],INV[n-j])))
    INV[n]=acc
eta={}
for n in range(BMAX+1):
    acc={}
    for j in range(n+1): acc=qadd(acc,qmul(FPt[j],INV[n-j]))
    eta[n]=acc
bad=[(n,m,c) for n in eta for m,c in eta[n].items() if c.denominator!=1]
print(f"H symbolic in Z[E1,E2,E3] up to T^{BMAX}:", "INTEGRAL" if not bad else f"NOT: {bad[:4]}")
mx=max((m[2] for n in eta for m in eta[n]),default=0)
for n in range(min(10,BMAX+1)):
    dg=max((m[2] for m in eta[n]),default=-1)
    print(f"  n={n}: deg_E3 = {dg}  (floor(n/3)={n//3}), #terms={len(eta[n])}")
