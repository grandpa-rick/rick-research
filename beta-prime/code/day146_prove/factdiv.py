"""On the locus phi_1 = E2+E1+1 = 0 we have f=1 and tau fixes E3, so H = F_P at the
shifted point (E1+3, E1+2).  Conjecture H1 there reads:  b! | P_b(E1+3, E1+2, E3).
Test symbolically in E1 (call it c) and E3."""
from core import *
from fractions import Fraction as Q
import math
BMAX=22
P=build_P(BMAX)
# substitute E1 -> c+3, E2 -> c+2 : result is poly in (c, E3) -> dict (i,k)->int
def sub_locus(A):
    out=defaultdict(int)
    for (a,b,k),co in A.items():
        # (c+3)^a * (c+2)^b  -> expand in c
        pa=[1]
        for _ in range(a):
            npa=[0]*(len(pa)+1)
            for i,v in enumerate(pa): npa[i+1]+=v; npa[i]+=3*v
            pa=npa
        pb=[1]
        for _ in range(b):
            npb=[0]*(len(pb)+1)
            for i,v in enumerate(pb): npb[i+1]+=v; npb[i]+=2*v
            pb=npb
        for i,vi in enumerate(pa):
            if not vi: continue
            for j,vj in enumerate(pb):
                if not vj: continue
                out[(i+j,k)]+=co*vi*vj
    return {m:v for m,v in out.items() if v}
print("b :  b! | P_b(c+3,c+2,E3) ?   ; also gcd/b!")
allok=True
for b in range(0,BMAX+1):
    S=sub_locus(P[b]); fb=math.factorial(b)
    ok=all(v%fb==0 for v in S.values())
    g=0
    for v in S.values(): g=math.gcd(g,abs(v))
    allok=allok and ok
    print(f"  b={b:2d}: {'YES' if ok else 'NO '}   gcd(P_b)/b! = {Q(g,fb) if fb else '-'}")
print("ALL:", allok)
