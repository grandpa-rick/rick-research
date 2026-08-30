"""F_P = exp(sum Lambda_n T^n/n)  (ghost components Lambda_n).
Dwork defect of F_P itself:  Delta_n := Lambda_n - varsigma(Lambda_{n/3}).
Conjecture H1 should be equivalent to:  Delta_n is tau-invariant mod 3^{v_3(n)}."""
import sys, math
sys.path.insert(0,'/home/agent/projects/beta-prime/code/day146_prove')
from core import build_P, pmul, padd, pscal, ppow, E1, E2, E3
from verify_master import tau_op
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
IN={0:{(0,0,0):Q(1)}}
for n in range(1,BMAX+1):
    IN[n]=qadd(*[qs(Q(-1),qmul(FP[j],IN[n-j])) for j in range(1,n+1)])
LAM={n:{m:int(c) for m,c in qadd(*[qmul(qs(Q(j),FP[j]),IN[n-j]) for j in range(n+1)]).items()}
     for n in range(BMAX+1)}
NAIVE=(ppow(E1,3),ppow(E2,3),ppow(E3,3))
PSI  =(padd(ppow(E1,3),pscal(-3,pmul(E1,E2)),pscal(3,E3)),
       padd(ppow(E2,3),pscal(-3,pmul(pmul(E1,E2),E3)),pscal(3,ppow(E3,2))),
       ppow(E3,3))
def lift(A,L):
    out={}
    for (a,b,c),co in A.items():
        out=padd(out, pscal(co, pmul(pmul(ppow(L[0],a),ppow(L[1],b)),ppow(L[2],c))))
    return out
def red(A,M): return {m:c%M for m,c in A.items() if c%M}
for name,L in [("naive",NAIVE),("psi^3",PSI)]:
    print("lift",name)
    for n in range(1,BMAX+1):
        v=0; nn=n
        while nn%3==0: nn//=3; v+=1
        if v==0: continue
        M=3**v
        D=padd(LAM[n], pscal(-1, lift(LAM[n//3],L)))
        inv = red(padd(tau_op(D), pscal(-1,D)), M)
        print(f"  n={n:3d} 3^v3={M}: Delta_n tau-invariant mod 3^v3? {'YES' if not inv else 'NO '+str(list(inv.items())[:2])}"
              f"   [Delta_n = 0 mod 3^v3? {'yes' if not red(D,M) else 'no'}]")
print()
print("Lambda_n mod 3, n=1..8:")
for n in range(1,min(BMAX,8)+1):
    print(f"  Lambda_{n} mod 3 =", dict(sorted(red(LAM[n],3).items())))
