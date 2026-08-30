"""G_d := [T^d] ( e^{-3rho/2} F_P )  in (rho,T) coords.  Claim: G_d is a POLYNOMIAL in
rho with  deg_rho + deg_E <= 2d   (deg E1 = 1, deg E2 = 2)."""
from core import *
from fractions import Fraction as Q
import math
BMAX=34
P=build_P(BMAX)
KMAX=8
ok=True
for d in range(0,6):
    # Fcal_d[k] = [E3^k]P_{2k+d}/(2k+d)!   as poly in (E1,E2)
    F={}
    for k in range(0,KMAX+1):
        b=2*k+d
        if b>BMAX: break
        F[k]={(m[0],m[1]):Q(c,math.factorial(b)) for m,c in P[b].items() if m[2]==k}
    K=max(F)
    # G = e^{-3rho/2} * F : G[k] = sum_j (-3/2)^j/j! * F[k-j]
    G={}
    for k in range(K+1):
        acc=defaultdict(Q)
        for j in range(k+1):
            c=Q((-3)**j,2**j*math.factorial(j))
            for m,v in F[k-j].items(): acc[m]+=c*v
        G[k]={m:v for m,v in acc.items() if v}
    hi=max([k for k in G if G[k]],default=-1)
    bad=[(k,m) for k in G for m in G[k] if k+m[0]+2*m[1]>2*d]
    print(f"d={d}: deg_rho(G_d)={hi} (bound 2d={2*d});  weighted-degree violations: {bad if bad else 'NONE'}")
    if hi>2*d or bad: ok=False
print("graded claim deg_rho + deg_E <= 2d :", "HOLDS d<=5" if ok else "FAILS")
