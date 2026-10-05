import sympy as sp, pickle
from sympy.polys.polyfuncs import symmetrize
N=8
d=pickle.load(open('/home/agent/projects/beta-prime/code/day149/phi%d.pkl'%N,'rb'))
u1,u2,u3=sp.symbols('u1 u2 u3'); E1,E2,E3=sp.symbols('E1 E2 E3'); s1,s2,s3=sp.symbols('s1 s2 s3')
Phi=[sp.expand(sp.sympify(s)) for s in d['Phi']]
def toE(p):
    s,rem,_=symmetrize(sp.expand(p),[u1,u2,u3],formal=True); assert rem==0
    return sp.expand(s.subs({s1:E1,s2:E2,s3:E3}))
PhiE=[toE(p) for p in Phi]
# log Phi
L=[sp.Integer(0)]*(N+1)
# log(1+x): use recursion  L' relation: n*L_n = n*Phi_n - sum_{k=1}^{n-1} k L_k Phi_{n-k}
for n in range(1,N+1):
    v=sp.Integer(n)*PhiE[n]
    for k in range(1,n): v-= k*L[k]*PhiE[n-k]
    L[n]=sp.expand(v/n)
print("=== log F_P (E coords) ===")
for n in range(N+1):
    if L[n]==0: print(n,0); continue
    p=sp.Poly(L[n],E1,E2,E3); dE3=max(m[2] for m in p.monoms())
    print("n=%d  deg_E3=%d  bound floor((n+1)/3)=%d  OK=%s"%(n,dE3,(n+1)//3,dE3<=(n+1)//3))
print("=== ell_{-1}(log F_P): coeff of E3^k T^{3k-1} ===")
for k in [1,2]:
    n=3*k-1
    c=sp.Poly(L[n],E3).coeff_monomial(E3**k)
    print("k=%d  n=%d  coeff = %s   E1,E2-free = %s"%(k,n,c,c.free_symbols==set()))
print("=== ell_0(log F_P): coeff of E3^k T^{3k} (for contrast) ===")
for k in [1,2]:
    n=3*k
    c=sp.Poly(L[n],E3).coeff_monomial(E3**k)
    print("k=%d  n=%d  coeff = %s   E1,E2-free = %s"%(k,n,sp.expand(c),c.free_symbols==set()))
# now log H = (tau-1) log Phi_sigma?  we use tilde H = sigma Phi/Phi -> log tildeH = (sigma-1) log Phi
# sigma on E: u->u-1 : E1->E1-3, E2->E2-2E1+3, E3->E3-E2+E1-1
sub={E1:E1-3,E2:E2-2*E1+3,E3:E3-E2+E1-1}
print("=== log tilde H = (sigma-1) log F_P ===")
for n in range(N+1):
    lh=sp.expand(L[n].subs(sub,simultaneous=True)-L[n])
    if lh==0: print("n=%d  0"%n); continue
    p=sp.Poly(lh,E1,E2,E3); dE3=max(m[2] for m in p.monoms())
    print("n=%d  deg_E3=%d  bound floor(n/3)=%d  OK=%s"%(n,dE3,n//3,dE3<=n//3))
