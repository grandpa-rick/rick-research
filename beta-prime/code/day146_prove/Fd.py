"""F_P = sum_d T^d Fcal_d(rho),  Fcal_d(rho) = sum_k [E3^k]P_{2k+d}/(2k+d)! rho^k.
Check Fcal_0 = e^{3rho/2} and get Fcal_1/e^{3rho/2} etc."""
from core import *
from fractions import Fraction as Q
import math
BMAX=26
P=build_P(BMAX)
def E3coef(A,k): return {(m[0],m[1]):c for m,c in A.items() if m[2]==k}
def show(d,var='E1,E2'):
    if not d: return "0"
    return ' + '.join((f"{c}" if (a,b)==(0,0) else f"{c}*E1^{a}E2^{b}") for (a,b),c in sorted(d.items()))
for dd in range(0,4):
    print(f"--- Fcal_{dd}: coefficient of rho^k ---")
    for k in range(0,5):
        b=2*k+dd
        if b>BMAX: break
        c=E3coef(P[b],k)
        cc={m:Q(v,math.factorial(b)) for m,v in c.items()}
        print(f"  k={k}: ", ' + '.join(f"({v})*E1^{m[0]}E2^{m[1]}" for m,v in sorted(cc.items())) or "0")
