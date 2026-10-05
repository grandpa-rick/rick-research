import sympy as sp
x1,x2,x3,T=sp.symbols('x1 x2 x3 T')
X=[x1,x2,x3]
e1=x1+x2+x3; e2=x1*x2+x1*x3+x2*x3; e3=x1*x2*x3
V=(x1-x2)*(x1-x3)*(x2-x3)
def A(k,f):
    return sp.expand(f + T*(e1-X[k])*f + sp.diff(f,X[k]))
# check commutativity on a random poly
import random
f=sp.expand(x1**2*x2+3*x3**3+x1*x2*x3+x2)
print("commute check:", sp.simplify(A(0,A(1,f))-A(1,A(0,f)))==0)
W=A(0,A(1,A(2,V)))
W=sp.expand(W)
g=sp.simplify(sp.cancel(W/V))
g=sp.expand(g)
print("W/V is polynomial:", sp.expand(g*V-W)==0)
print("g =",sp.factor(g))
# express g in E-basis
from sympy.polys.polyfuncs import symmetrize
E1,E2,E3,s1,s2,s3=sp.symbols('E1 E2 E3 s1 s2 s3')
s,rem,_=symmetrize(g,[x1,x2,x3],formal=True)
print("symmetric:",rem==0)
gE=sp.expand(s.subs({s1:E1,s2:E2,s3:E3}))
print("g in E =",sp.collect(gE,T))
for r in range(0,5):
    print("  T^%d :"%r, sp.factor(sp.expand(gE.coeff(T,r))))
