"""Verify the P-frame master recursion:
 P_{b+1} = phi_{b+1} P_b + 3b E3 tau(P_{b-1}) - b(b-1)(E1+2b+2) E3 tau(P_{b-2})
 with phi_c = E2 + c E1 + c^2,  tau: E1->E1+3, E2->E2+2E1+3, E3->E3+E2+E1+1
Equivalent to  L F_P = E3 T^2 [ -3 + T(E1+6+2 theta) ] tau(F_P).
"""
from core import *

T1 = padd(E1, const(3))
T2 = padd(E2, pscal(2,E1), const(3))
T3 = padd(E3, E2, E1, const(1))

def tau_op(P):
    maxa=max((m[0] for m in P),default=0); maxb=max((m[1] for m in P),default=0); maxc=max((m[2] for m in P),default=0)
    A=[ONE];B=[ONE];C=[ONE]
    for _ in range(maxa): A.append(pmul(A[-1],T1))
    for _ in range(maxb): B.append(pmul(B[-1],T2))
    for _ in range(maxc): C.append(pmul(C[-1],T3))
    out=defaultdict(int)
    for (a,b,c),co in P.items():
        t=pmul(pmul(A[a],B[b]),C[c])
        for m,cc in t.items(): out[m]+=co*cc
    return {m:c for m,c in out.items() if c}

BM=16
P=build_P(BM)
ok=True
for b in range(0,BM):
    c=b+1
    lhs=P[c]
    rhs=pmul(padd(E2,pscal(c,E1),const(c*c)),P[b])
    if b>=1:
        rhs=padd(rhs, pscal(3*b, pmul(E3, tau_op(P[b-1]))))
    if b>=2:
        rhs=padd(rhs, pscal(-b*(b-1), pmul(pmul(padd(E1,const(2*b+2)),E3), tau_op(P[b-2]))))
    d=padd(lhs,pscal(-1,rhs))
    if d: ok=False; print("MISMATCH at b+1=",c, "nterms diff",len(d), list(d.items())[:4])
print("MASTER RECURSION VERIFIED" if ok else "FAILED")
