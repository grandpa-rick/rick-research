"""KEY TEST.  Facts:  H = tau(F_P)/F_P  and  Lambda = theta log F_P  satisfy
       theta H / H = tau(Lambda) - Lambda        (cocycle identity, exact)
   so   H = exp( sum_{n>=1} ell_n T^n / n ),   ell_n := (tau Lambda - Lambda)_n .
Dwork's lemma (ghost form):  H in 1+T R[[T]]  <==>  ell_n = varsigma(ell_{n/3}) mod 3^{v_3(n)}.
Test:  (0) cocycle identity;  (1) ell_{3m} = ell_m^3 mod 3;  (2) mod 3^{v_3(n)} in general."""
import sys, math
sys.path.insert(0,'/home/agent/projects/beta-prime/code/day146_prove')
from core import build_P, pmul, padd, pscal, ppow, ONE, E1, E2, E3
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
FPt={b:{m:Q(c,math.factorial(b)) for m,c in tau_op(P[b]).items()} for b in range(BMAX+1)}
IN={0:{(0,0,0):Q(1)}}
for n in range(1,BMAX+1):
    IN[n]=qadd(*[qs(Q(-1),qmul(FP[j],IN[n-j])) for j in range(1,n+1)])
LAM={n:qadd(*[qmul(qs(Q(j),FP[j]),IN[n-j]) for j in range(n+1)]) for n in range(BMAX+1)}
H  ={n:qadd(*[qmul(FPt[j],IN[n-j]) for j in range(n+1)]) for n in range(BMAX+1)}
def toZ(A):
    for c in A.values(): assert c.denominator==1, A
    return {m:int(c) for m,c in A.items()}
LAMZ={n:toZ(LAM[n]) for n in LAM}; HZ={n:toZ(H[n]) for n in H}
ell={n: padd(tau_op(LAMZ[n]), pscal(-1,LAMZ[n])) for n in range(BMAX+1)}

# (0) cocycle:  theta H = H * (tau Lambda - Lambda)
ok=True
for n in range(BMAX+1):
    lhs=pscal(n,HZ[n])
    rhs=padd(*[pmul(HZ[j],ell[n-j]) for j in range(n+1)]) if n else {}
    if padd(lhs,pscal(-1,rhs)): ok=False; print("  cocycle FAILS at n=",n)
print("(0) cocycle  theta H = H (tau Lambda - Lambda)  to T^%d:"%BMAX, "HOLDS" if ok else "FAILS")

# Frobenius lifts
NAIVE=(ppow(E1,3),ppow(E2,3),ppow(E3,3))
PSI  =(padd(ppow(E1,3),pscal(-3,pmul(E1,E2)),pscal(3,E3)),
       padd(ppow(E2,3),pscal(-3,pmul(pmul(E1,E2),E3)),pscal(3,ppow(E3,2))),
       ppow(E3,3))
def lift(A,L):
    out={}
    for (a,b,c),co in A.items():
        out=padd(out, pscal(co, pmul(pmul(ppow(L[0],a),ppow(L[1],b)),ppow(L[2],c))))
    return out
def redmod(A,M): return {m:c%M for m,c in A.items() if c%M}

print()
print("(1)/(2) Dwork ghost congruences   ell_n = varsigma(ell_{n/3})  mod 3^{v3(n)}")
for name,L in [("naive E^3",NAIVE),("Adams psi^3",PSI)]:
    print("  lift:",name)
    allok=True
    for n in range(1,BMAX+1):
        v=0; nn=n
        while nn%3==0: nn//=3; v+=1
        M=3**v
        if M==1: continue
        tgt = lift(ell[n//3],L) if n%3==0 else {}
        d = redmod(padd(ell[n],pscal(-1,tgt)),M)
        print(f"    n={n:3d} v3={v} 3^v={M}:  {'OK' if not d else 'FAIL '+str(list(d.items())[:3])}")
        if d: allok=False
    print("   ->", "ALL CONGRUENCES HOLD" if allok else "SOME FAIL")
print()
print("ell_n (first few), as polynomials in E1,E2,E3:")
for n in range(1,min(BMAX,7)+1):
    print(f"  ell_{n} =", dict(sorted(ell[n].items())))
