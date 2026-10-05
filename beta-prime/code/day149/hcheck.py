import sympy as sp, pickle, sys
from sympy import Rational, factorial
N=8
d=pickle.load(open('/home/agent/projects/beta-prime/code/day149/phi%d.pkl'%N,'rb'))
u1,u2,u3=sp.symbols('u1 u2 u3'); u=[u1,u2,u3]
E1,E2,E3=sp.symbols('E1 E2 E3')
Phi=[sp.sympify(sp.srepr!=None) for _ in []]
Phi=[sp.parse_expr(s) if False else sp.sympify(s) for s in d['Phi']]
Phi=[sp.sympify(s) for s in d['Phi']]
# sympify of srepr works
Phi=[sp.expand(sp.sympify(s)) for s in d['Phi']]

# sigma: u -> u-1
sub={u1:u1-1,u2:u2-1,u3:u3-1}
sPhi=[sp.expand(p.subs(sub,simultaneous=True)) for p in Phi]
print("sigma applied")
# Htilde = sPhi/Phi as series in T
H=[]
for n in range(N+1):
    v=sPhi[n]
    for k in range(1,n+1):
        v-= sp.expand(Phi[k]*H[n-k])
    H.append(sp.expand(v))   # Phi[0]=1
    print("H T^%d"%n); sys.stdout.flush()

def to_E(p):
    pol=sp.Poly(p,u1,u2,u3)
    res=sp.symmetrize(pol.as_expr(),[u1,u2,u3],formal=False) if False else None
    from sympy.polys.polyfuncs import symmetrize
    s,rem,_=symmetrize(p,[u1,u2,u3],formal=True)
    assert rem==0, "not symmetric"
    s1,s2,s3=sp.symbols('s1 s2 s3')
    return sp.expand(s.subs({s1:E1,s2:E2,s3:E3}))

HE=[]
for n in range(N+1):
    HE.append(to_E(H[n]))
    print("T^%d : "%n, sp.factor(HE[-1])); sys.stdout.flush()
pickle.dump([sp.srepr(x) for x in HE],open('/home/agent/projects/beta-prime/code/day149/HE%d.pkl'%N,'wb'))
# checks
for n in range(N+1):
    p=sp.Poly(HE[n],E1,E2,E3)
    degE3=max([m[2] for m in p.monoms()]) if HE[n]!=0 else -1
    dens=[sp.Rational(c).q for c in p.coeffs()]
    print("n=%d  deg_E3=%d  (floor n/3 = %d)  integral=%s"%(n,degE3,n//3,all(q==1 for q in dens)))
