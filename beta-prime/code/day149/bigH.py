import sys, math, pickle
sys.path.insert(0,'/home/agent/projects/beta-prime/code/day146_prove')
from core import *
from verify_master import tau_op
from fractions import Fraction as Q
from collections import defaultdict
BMAX=int(sys.argv[1]) if len(sys.argv)>1 else 16
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
H={}
for n in range(BMAX+1):
    acc={}
    for j in range(n+1): acc=qadd(acc,qmul(FPt[j],INV[n-j]))
    H[n]={m:int(c) for m,c in acc.items()}
    assert all(c.denominator==1 for c in acc.values()), n
print("H integral to T^%d: YES"%BMAX)
for n in range(BMAX+1):
    cs=list(H[n].values())
    negs=[(m,c) for m,c in H[n].items() if c<0]
    top=H[n].get((n,0,0),None)
    print("n=%2d  #mon=%3d  min=%s  #neg=%d  [E1^n]=%s  H_n(0,0,0)=%s"%(n,len(cs),min(cs),len(negs),top,H[n].get((0,0,0),0)))
pickle.dump(H,open('/home/agent/projects/beta-prime/code/day149/H%d.pkl'%BMAX,'wb'))
