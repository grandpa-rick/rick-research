#!/usr/bin/env python3
"""Independent re-derivation of H = tau(F_P)/F_P straight from the DEFINITION
   F_P = T^+(e^{T e_2} V)/V,  T^+ : u^alpha -> prod_i u_i^{(alpha_i)} (rising),
   tau : u_i -> u_i + 1.
   Compared against day149/H16.pkl (built by bigH.py via the day146 Psi-recursion)."""
import sympy as sp, pickle
from sympy.polys.polyfuncs import symmetrize
from fractions import Fraction as Q

NMAX = 9
u1,u2,u3 = sp.symbols('u1 u2 u3'); u=[u1,u2,u3]
E1,E2,E3 = sp.symbols('E1 E2 E3'); s1,s2,s3 = sp.symbols('s1 s2 s3')
V  = sp.expand((u1-u2)*(u1-u3)*(u2-u3))
e2 = u1*u2+u1*u3+u2*u3

def rising(x,k):
    r = sp.Integer(1)
    for j in range(k): r *= (x+j)
    return r

def Tplus(p):
    """umbral rising-factorial map on a polynomial in u1,u2,u3"""
    pol = sp.Poly(sp.expand(p), u1,u2,u3)
    out = sp.Integer(0)
    for mon, c in zip(pol.monoms(), pol.coeffs()):
        t = c
        for i in range(3): t *= rising(u[i], mon[i])
        out += t
    return sp.expand(out)

# P_b = T^+(e2^b V)/V
P = []
cur = V
for b in range(NMAX+1):
    num = Tplus(cur)
    q = sp.simplify(sp.cancel(num/V))
    assert sp.expand(q*V-num)==0, b
    P.append(sp.expand(q))
    cur = sp.expand(cur*e2)

FP  = [sp.Rational(1,sp.factorial(b))*P[b] for b in range(NMAX+1)]
tau = {u1:u1+1, u2:u2+1, u3:u3+1}
FPt = [sp.expand(f.subs(tau, simultaneous=True)) for f in FP]

# H = FPt / FP  as a T-series
H = []
for n in range(NMAX+1):
    v = FPt[n]
    for k in range(1,n+1): v -= sp.expand(FP[k]*H[n-k])
    H.append(sp.expand(v))

def toE(p):
    s,rem,_ = symmetrize(p,[u1,u2,u3],formal=True); assert rem==0
    return sp.expand(s.subs({s1:E1,s2:E2,s3:E3}))

ref = pickle.load(open('/home/agent/projects/beta-prime/code/day149/H16.pkl','rb'))
allok=True
for n in range(NMAX+1):
    e = toE(H[n]); pol = sp.Poly(e,E1,E2,E3)
    mine = {tuple(m):sp.Rational(c) for m,c in zip(pol.monoms(),pol.coeffs())}
    mine = {m:int(c) for m,c in mine.items() if c!=0}
    ok = (mine == ref[n])
    allok &= ok
    print("T^%d : match=%s (#mon %d vs %d)"%(n,ok,len(mine),len(ref[n])))
    if not ok:
        for m in set(mine)|set(ref[n]):
            if mine.get(m,0)!=ref[n].get(m,0): print("    ",m,mine.get(m,0),ref[n].get(m,0))
print("INDEPENDENT CHECK of H16.pkl to T^%d:"%NMAX, "PASS" if allok else "FAIL")
