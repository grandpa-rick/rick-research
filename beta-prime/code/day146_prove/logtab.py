from core import *
from fractions import Fraction
import math, sys

BMAX = int(sys.argv[1]) if len(sys.argv)>1 else 20
P = build_P(BMAX)
# specialise (U,V)=(0,0): E1=-2, E2=1 ; f = 1
# series in T (0..BMAX) with coeffs = dict {E3power: Fraction}
def spec(Pb):
    return {k: Fraction(v) for k,v in subs_E12(Pb,-2,1).items()}

FP = {}
for b in range(BMAX+1):
    d = spec(P[b])
    FP[b] = {k: v/math.factorial(b) for k,v in d.items()}

def smul(A,B,N):
    R = defaultdict(lambda: defaultdict(Fraction))
    for b1,d1 in A.items():
        if b1>N: continue
        for b2,d2 in B.items():
            if b1+b2>N: continue
            for k1,v1 in d1.items():
                for k2,v2 in d2.items():
                    R[b1+b2][k1+k2]+=v1*v2
    return {b:{k:v for k,v in d.items() if v} for b,d in R.items()}

# u = FP - 1
u = {b:dict(d) for b,d in FP.items() if b>=1}
log = defaultdict(lambda: defaultdict(Fraction))
term = {0:{0:Fraction(1)}}
for m in range(1, BMAX+1):
    term = smul(term, u, BMAX)
    if not term: break
    c = Fraction((-1)**(m-1), m)
    for b,d in term.items():
        for k,v in d.items():
            log[b][k]+= c*v
log = {b:{k:v for k,v in d.items() if v} for b,d in log.items()}

def v3f(fr):
    if fr==0: return None
    n,dd = fr.numerator, fr.denominator
    v=0
    while n%3==0: n//=3; v+=1
    while dd%3==0: dd//=3; v-=1
    return v

print("=== v3([E3^k T^b] log FP)  rows b, cols k=0.. ===")
for b in range(0,BMAX+1):
    d = log.get(b,{})
    row=[]
    for k in range(0, b//2+2):
        v = d.get(k)
        row.append('.' if (v is None or v==0 and False) else (str(v3f(v)) if v is not None else '.'))
    print(f"b={b:3d}", ' '.join(f"{x:>3}" for x in row))

print()
print("=== n_k = [E3^k T^{3k-1}] log FP , b_k=(3k-1)n_k ===")
for k in range(1, (BMAX+1)//3+1):
    b=3*k-1
    v = log.get(b,{}).get(k,Fraction(0))
    print(f"k={k}: n_k={v}  b_k={(3*k-1)*v}")
