"""Compute X = L F_P / F_P symbolically in (E1,E2,E3); extract diagonals
   a_k = [E3^k T^{3k-1}] X   and   y_k = [E3^k T^{3k}] X  as polys in E1,E2."""
from core import *
from fractions import Fraction
import math, sys
BMAX=int(sys.argv[1]) if len(sys.argv)>1 else 15
P=build_P(BMAX)
Q=Fraction
def qpoly(P):   # int poly -> Fraction poly
    return {m:Q(c) for m,c in P.items()}
def qmul(A,B):
    R=defaultdict(Q)
    for m1,c1 in A.items():
        for m2,c2 in B.items(): R[(m1[0]+m2[0],m1[1]+m2[1],m1[2]+m2[2])]+=c1*c2
    return {m:c for m,c in R.items() if c}
def qadd(*Ps):
    R=defaultdict(Q)
    for Pp in Ps:
        for m,c in Pp.items(): R[m]+=c
    return {m:c for m,c in R.items() if c}
def qscal(k,Pp): return {m:k*c for m,c in Pp.items()} if k else {}

# F_P = sum P_b T^b / b!   ; LF_P: [T^n] = ((E2+n E1+n^2) P_{n-1} - P_n)/(n-1)!
FP={b:qscal(Q(1,math.factorial(b)),qpoly(P[b])) for b in range(BMAX+1)}
LF={}
for n in range(1,BMAX+1):
    t=qadd(qmul(qadd(E2 and qpoly(E2), qscal(n,qpoly(E1)), qpoly(const(n*n))), qpoly(P[n-1])), qscal(-1,qpoly(P[n])))
    LF[n]=qscal(Q(1,math.factorial(n-1)),t)
LF[0]={}
# invert FP
INV={0:{(0,0,0):Q(1)}}
for n in range(1,BMAX+1):
    acc={}
    for j in range(1,n+1):
        acc=qadd(acc, qscal(-1,qmul(FP[j],INV[n-j])))
    INV[n]=acc
X={}
for n in range(BMAX+1):
    acc={}
    for j in range(n+1):
        if LF.get(j): acc=qadd(acc,qmul(LF[j],INV[n-j]))
    X[n]=acc
def coefE3(Pp,k):
    return {(m[0],m[1]):c for m,c in Pp.items() if m[2]==k}
def show(d):
    if not d: return "0"
    return ' + '.join(f"{c}*E1^{a}E2^{b}" for (a,b),c in sorted(d.items()))
print("=== a_k = [E3^k T^{3k-1}] X ===")
for k in range(1,(BMAX+1)//3+1):
    print(f" k={k}: ", show(coefE3(X[3*k-1],k)))
print()
print("=== y_k = [E3^k T^{3k}] X ===")
for k in range(1,BMAX//3+1):
    print(f" k={k}: ", show(coefE3(X[3*k],k)))
