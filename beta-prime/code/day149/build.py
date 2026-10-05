import sympy as sp
from sympy import Rational, factorial, binomial
from itertools import product
import pickle, sys

N = int(sys.argv[1]) if len(sys.argv)>1 else 8
u1,u2,u3 = sp.symbols('u1 u2 u3')
u=[u1,u2,u3]
def V(v): return (v[0]-v[1])*(v[0]-v[2])*(v[1]-v[2])
def fall(x,n):
    r=sp.Integer(1)
    for j in range(n): r*= (x-j)
    return r

# [T^n] (Phi*V) = sum_{a+b+c=n} 1/(a!b!c!) prod (u_i)_{m_i} V(u-m)
PV=[]
for n in range(N+1):
    tot=sp.Integer(0)
    for a in range(n+1):
        for b in range(n+1-a):
            c=n-a-b
            m=(a+b,a+c,b+c)
            term=Rational(1,factorial(a)*factorial(b)*factorial(c))
            for i in range(3): term*=fall(u[i],m[i])
            term*= V([u[i]-m[i] for i in range(3)])
            tot+=term
    PV.append(sp.expand(tot))
    print("PV T^%d done, terms=%d"%(n,len(PV[-1].args) if PV[-1].args else 1)); sys.stdout.flush()

Vu=sp.expand(V(u))
# Phi = PV / V  (exact)
Phi=[sp.cancel(sp.together(p/Vu)) for p in PV]
Phi=[sp.expand(sp.simplify(p)) for p in Phi]
for n,p in enumerate(Phi):
    assert sp.expand(p*Vu-PV[n])==0, n
print("Phi computed, Phi0=",Phi[0])
pickle.dump({'PV':[sp.srepr(x) for x in PV],'Phi':[sp.srepr(x) for x in Phi]},open('/home/agent/projects/beta-prime/code/day149/phi%d.pkl'%N,'wb'))
