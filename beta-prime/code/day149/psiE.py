import sympy as sp, pickle
from sympy.polys.polyfuncs import symmetrize
N=8
d=pickle.load(open('/home/agent/projects/beta-prime/code/day149/phi%d.pkl'%N,'rb'))
u1,u2,u3=sp.symbols('u1 u2 u3'); E1,E2,E3=sp.symbols('E1 E2 E3'); s1,s2,s3=sp.symbols('s1 s2 s3')
Phi=[sp.expand(sp.sympify(s)) for s in d['Phi']]
PsiE=[]
for n in range(N+1):
    p=sp.expand(Phi[n]*sp.factorial(n))
    s,rem,_=symmetrize(p,[u1,u2,u3],formal=True); assert rem==0
    e=sp.expand(s.subs({s1:E1,s2:E2,s3:E3}))
    PsiE.append(e)
    pol=sp.Poly(e,E1,E2,E3)
    print("Psi_%d integer coeffs: %s"%(n,all(sp.Rational(c).q==1 for c in pol.coeffs())))
pickle.dump([sp.srepr(x) for x in PsiE],open('/home/agent/projects/beta-prime/code/day149/PsiE%d.pkl'%N,'wb'))
print(PsiE[1]); print(PsiE[2])
