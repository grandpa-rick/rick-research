"""CORRECT Dieudonne-Dwork test, done SYMBOLICALLY in Z[E1,E2,E3]:
    H in 1+T R[[T]]   <==>   H(T)^3 / varsigma(H)(T^3)  in  1+3T R[[T]]
with varsigma applied to the COEFFICIENTS (no tau, no numeric base point --
varsigma moves any numeric base point, which is why the numeric checks in
dwork.py/dwork2.py were testing the wrong thing).
Three lifts compared:  identity (not a lift), naive E_i -> E_i^3, Adams psi^3."""
import sys, math
sys.path.insert(0,'/home/agent/projects/beta-prime/code/day146_prove')
from core import build_P, pmul, padd, pscal, ppow, ONE, E1, E2, E3, const
from verify_master import tau_op
from fractions import Fraction as Q
from collections import defaultdict
BMAX=int(sys.argv[1]) if len(sys.argv)>1 else 12

def qp(A): return {m:Q(c) for m,c in A.items()}
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
FP={b:qs(Q(1,math.factorial(b)),qp(P[b])) for b in range(BMAX+1)}
FPt={b:qs(Q(1,math.factorial(b)),qp(tau_op(P[b]))) for b in range(BMAX+1)}
def sinv(A):
    B={0:{(0,0,0):Q(1)}}
    for n in range(1,BMAX+1):
        acc={}
        for j in range(1,n+1): acc=qadd(acc,qs(Q(-1),qmul(A[j],B[n-j])))
        B[n]=acc
    return B
IN=sinv(FP)
H={n:qadd(*[qmul(FPt[j],IN[n-j]) for j in range(n+1)]) for n in range(BMAX+1)}
bad=[(n,m) for n in H for m,c in H[n].items() if c.denominator!=1]
print("H integral symbolically to T^%d:"%BMAX, "YES" if not bad else bad[:3])

def smul(A,B):
    R={}
    for n in range(BMAX+1):
        R[n]=qadd(*[qmul(A[j],B[n-j]) for j in range(n+1)])
    return R
H3=smul(smul(H,H),H)

# --- three coefficient lifts ---
def lift_id(A): return A
NA1=ppow(E1,3); NA2=ppow(E2,3); NA3=ppow(E3,3)
PS1=padd(ppow(E1,3), pscal(-3,pmul(E1,E2)), pscal(3,E3))
PS2=padd(ppow(E2,3), pscal(-3,pmul(pmul(E1,E2),E3)), pscal(3,ppow(E3,2)))
PS3=ppow(E3,3)
def mk_lift(L1,L2,L3):
    def f(A):
        out={}
        for (a,b,c),co in A.items():
            t=pmul(pmul(ppow(L1,a),ppow(L2,b)),ppow(L3,c))
            out=qadd(out, qs(co, qp(t)))
        return out
    return f
lifts={'identity (NOT a lift)':lift_id,
       'naive E_i -> E_i^3':mk_lift(NA1,NA2,NA3),
       'Adams psi^3':mk_lift(PS1,PS2,PS3)}

for name,L in lifts.items():
    sH={n:({} if n%3 else L(H[n//3])) for n in range(BMAX+1)}
    D=smul(H3, sinv(sH))
    viol=[]
    for n in range(1,BMAX+1):
        for m,c in D[n].items():
            if c.denominator%3==0 or c.numerator%3!=0 or c.denominator!=1:
                viol.append((n,m,str(c)))
    print(f"  lift = {name:24s} -> H^3/varsigma(H)(T^3) in 1+3T Z[E][[T]] ? "
          + ("YES" if not viol else f"NO  first: {viol[:3]}"))
