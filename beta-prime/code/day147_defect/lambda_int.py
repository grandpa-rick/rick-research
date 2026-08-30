"""Is Lambda = theta(F_P)/F_P = theta log F_P an ORDINARY integral series
(coefficients in Z[E1,E2,E3])?  And X = L F_P / F_P ?   Symbolic test."""
import sys, math
sys.path.insert(0,'/home/agent/projects/beta-prime/code/day146_prove')
from core import build_P
from fractions import Fraction as Q
from collections import defaultdict
BMAX=int(sys.argv[1]) if len(sys.argv)>1 else 14
def qmul(A,B):
    R=defaultdict(Q)
    for m1,c1 in A.items():
        for m2,c2 in B.items(): R[(m1[0]+m2[0],m1[1]+m2[1],m1[2]+m2[2])]+=c1*c2
    return {m:c for m,c in R.items() if c}
def qadd(*Xs):
    R=defaultdict(Q)
    for X in Xs:
        for m,c in X.items(): R[m]+=c
    return {m:c for m,c in R.items() if c}
def qs(k,A): return {m:k*c for m,c in A.items()} if k else {}
P=build_P(BMAX)
FP={b:{m:Q(c,math.factorial(b)) for m,c in P[b].items()} for b in range(BMAX+1)}
TH={b:qs(Q(b),FP[b]) for b in range(BMAX+1)}          # theta F_P
IN={0:{(0,0,0):Q(1)}}
for n in range(1,BMAX+1):
    IN[n]=qadd(*[qs(Q(-1),qmul(FP[j],IN[n-j])) for j in range(1,n+1)])
LAM={n:qadd(*[qmul(TH[j],IN[n-j]) for j in range(n+1)]) for n in range(BMAX+1)}
bad=[(n,m,str(c)) for n in LAM for m,c in LAM[n].items() if c.denominator!=1]
print("Lambda = theta F_P / F_P integral in Z[E1,E2,E3][[T]] to T^%d:"%BMAX,
      "YES" if not bad else f"NO  first {bad[:4]}")
# denominators seen
dens=sorted({c.denominator for n in LAM for c in LAM[n].values()})
print("  denominators observed:", dens[:10])
# order (in rho,T coords): order of E3^k T^b is b-3k ; check ord >= -1
worst=min((n-3*m[2] for n in LAM for m in LAM[n]), default=None)
print("  min order (b-3k) over nonzero coefficients:", worst, " (Prop 1 predicts >= -1)")
