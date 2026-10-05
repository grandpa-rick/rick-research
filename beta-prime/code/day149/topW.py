import pickle
from math import comb
H=pickle.load(open('H16.pkl','rb'))
N=16
# H in the project's sign convention already (bigH used tau_op on P). weighted degree of E1^a E2^b E3^c = a+2b+3c
def toppart(n):
    return {m:c for m,c in H[n].items() if m[0]+2*m[1]+3*m[2]==n}
def toU(A,x,y,z):
    e1=x+y+z; e2=x*y+x*z+y*z; e3=x*y*z
    return sum(c*e1**m[0]*e2**m[1]*e3**m[2] for m,c in A.items())
import sympy as sp
X,Y,Z=sp.symbols('x y z')
print("top part W_n = (weighted-deg-n part of H_n)/(n+1); check Narayana at z=0")
allok=True
for n in range(1,N+1):
    A=toppart(n)
    assert all(c%(n+1)==0 for c in A.values()), (n,A)
    W={m:c//(n+1) for m,c in A.items()}
    p=sp.expand(toU(W,X,Y,0))
    pol=sp.Poly(p,X,Y)
    coeffs=[pol.coeff_monomial(X**(n-k)*Y**k) for k in range(n+1)]
    nar=[sp.Integer(comb(n+1,k)*comb(n+1,k+1)//(n+1)) for k in range(n+1)]
    ok=(coeffs==nar)
    allok&=ok
    print("n=%2d  z=0 coeffs=%s  Narayana=%s  %s"%(n,coeffs[:6],nar[:6],"OK" if ok else "MISMATCH"))
print("ALL Narayana:",allok)
print()
print("W_n(1,1,1):",[ (lambda A: sum(c for c in A.values())//(n+1))(toppart(n)) for n in range(0,N+1)])
print("W_n(1,1,0):",[ (lambda A,n=n: sp.Integer(toU({m:c//(n+1) for m,c in A.items()},1,1,0)))(toppart(n)) for n in range(1,N+1)])
for n in range(1,7):
    A=toppart(n); W={m:c//(n+1) for m,c in A.items()}
    print("W_%d ="%n, sp.expand(sum(sp.Symbol('E1')**m[0]*sp.Symbol('E2')**m[1]*sp.Symbol('E3')**m[2]*c for m,c in W.items())))
