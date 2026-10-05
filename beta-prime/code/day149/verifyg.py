import sympy as sp
from sympy import Rational as R, factorial
u1,u2,u3,T=sp.symbols('u1 u2 u3 T')
U=[u1,u2,u3]
N=7
def V(v): return (v[0]-v[1])*(v[0]-v[2])*(v[1]-v[2])
def fall(x,n):
    r=sp.Integer(1)
    for j in range(n): r*=(x-j)
    return r
def Tmap(poly):
    """umbral T: monomial u^alpha -> prod (u_i)_{alpha_i}"""
    p=sp.Poly(sp.expand(poly),u1,u2,u3)
    out=sp.Integer(0)
    for mono,c in zip(p.monoms(),p.coeffs()):
        term=c
        for i in range(3): term*=fall(U[i],mono[i])
        out+=term
    return sp.expand(out)
e1=u1+u2+u3; e2=u1*u2+u1*u3+u2*u3; e3=u1*u2*u3
Vu=sp.expand(V(U))
g=1+2*(e1+3)*T+(e1**2+4*e1+e2)*T**2+(e1*e2-e3)*T**3
# LHS: Phi(u+1)*V(u)   ; RHS: T-map of  g*e^{T e2}*V , order by order in T
# build e^{T e2} V  up to T^N
EV=[sp.expand(e2**b*Vu/factorial(b)) for b in range(N+1)]
gs=[sp.expand(g.coeff(T,r)) for r in range(4)]
lhs=[]; rhs=[]
for n in range(N+1):
    # RHS_n = sum_r Tmap(g_r * e2^{n-r} V /(n-r)!)
    acc=sp.Integer(0)
    for r in range(min(3,n)+1):
        acc+=Tmap(sp.expand(gs[r]*EV[n-r]))
    rhs.append(sp.expand(acc))
    # LHS_n = [T^n]Phi(u+1) * V(u) = Tmap(e2^n V/n!) with u->u+1 , then *V(u)/V(u+1)=1
    l=Tmap(EV[n]).subs({u1:u1+1,u2:u2+1,u3:u3+1},simultaneous=True)
    lhs.append(sp.expand(l))
ok=all(sp.expand(lhs[n]-rhs[n])==0 for n in range(N+1))
print("identity  Phi(u+1)V(u) = Tmap(g e^{Te2} V)  verified to T^%d :"%N, ok)
for n in range(N+1):
    print("  n=%d  diff=%s"%(n,sp.expand(lhs[n]-rhs[n])))
