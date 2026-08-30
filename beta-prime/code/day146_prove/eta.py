from core import *
from fractions import Fraction
import math,sys
BMAX=int(sys.argv[1]) if len(sys.argv)>1 else 20
P=build_P(BMAX)
def series(e1,e2):
    return {b:{k:Fraction(v,math.factorial(b)) for k,v in subs_E12(P[b],e1,e2).items()} for b in range(BMAX+1)}
FP=series(-2,1); FPt=series(1,0)
# eta from  tau(P_n) = sum_j n!/(n-j)! eta_j P_{n-j}   (eta_j polys in E3)
Praw ={b:subs_E12(P[b],-2,1) for b in range(BMAX+1)}
Ptraw={b:subs_E12(P[b],1,0) for b in range(BMAX+1)}
eta={0:{0:Fraction(1)}}
for n in range(1,BMAX+1):
    acc=defaultdict(Fraction)
    for k,v in Ptraw.get(n,{}).items(): acc[k]+=v
    for j in range(0,n):
        c=Fraction(math.factorial(n),math.factorial(n-j))
        for k1,v1 in eta[j].items():
            for k2,v2 in Praw.get(n-j,{}).items(): acc[k1+k2]-=c*v1*v2
    eta[n]={k:v/math.factorial(n) for k,v in acc.items() if v}
allint=True
for n in range(BMAX+1):
    for k,v in eta[n].items():
        if v.denominator!=1: allint=False
    if n<=10: print(f"eta_{n} =", {k:str(v) for k,v in sorted(eta[n].items())})
print("ALL eta coefficients are INTEGERS:", allint)
