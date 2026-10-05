"""Day 149: Psi is the Schur -> factorial-Schur map; P_b = sum_mu K_{mu'(2^b)} frs_mu;
tau(frs_mu) = frs_{mu+(1,1,1)}/E3; B = e_2-Pieri operator.  All verified here."""
import sympy as sp, sys
sys.path.insert(0,'/home/agent/projects/beta-prime/code/day146_prove')
from core import build_P
from sympy.polys.polyfuncs import symmetrize
u1,u2,u3=sp.symbols('u1 u2 u3'); U=[u1,u2,u3]
E1,E2,E3,s1,s2,s3=sp.symbols('E1 E2 E3 s1 s2 s3')
V=sp.expand((u1-u2)*(u1-u3)*(u2-u3)); rho=(2,1,0)
def rise(x,n):
    r=sp.Integer(1)
    for j in range(n): r*=(x+j)
    return r
def Tplus(p):
    pol=sp.Poly(sp.expand(p),u1,u2,u3); out=sp.Integer(0)
    for m,c in zip(pol.monoms(),pol.coeffs()):
        t=c
        for i in range(3): t*=rise(U[i],m[i])
        out+=t
    return sp.expand(out)
def Psi(f): return sp.expand(sp.cancel(Tplus(sp.expand(f*V))/V))
def schur(mu): return sp.expand(sp.cancel(sp.expand(sp.Matrix(3,3,lambda i,j: U[i]**(mu[j]+rho[j])).det())/V))
def frs(mu):   return sp.expand(sp.cancel(sp.expand(sp.Matrix(3,3,lambda i,j: rise(U[i],mu[j]+rho[j])).det())/V))
def toE(p):
    ss,rem,_=symmetrize(sp.expand(p),[u1,u2,u3],formal=True); assert rem==0
    return sp.expand(ss.subs({s1:E1,s2:E2,s3:E3}))
def pieri2(d):
    out={}
    for mu,c in d.items():
        for i in range(3):
            for j in range(i+1,3):
                nu=list(mu); nu[i]+=1; nu[j]+=1; nu=tuple(nu)
                if nu[0]>=nu[1]>=nu[2]>=0: out[nu]=out.get(nu,0)+c
    return out
if __name__=="__main__":
    print("Theorem A  Psi(s_mu)=frs_mu:",
          all(sp.expand(Psi(schur(m))-frs(m))==0 for m in [(0,0,0),(1,0,0),(1,1,0),(2,0,0),(1,1,1),(2,1,0),(3,1,0),(2,2,1),(3,2,2)]))
    P=build_P(6); cur={(0,0,0):1}
    for b in range(7):
        lhs=sp.expand(sum(sp.Integer(c)*E1**m[0]*E2**m[1]*E3**m[2] for m,c in P[b].items()))
        rhs=sp.expand(sum(sp.Integer(c)*toE(frs(mu)) for mu,c in cur.items()))
        print("Corollary B  b=%d :"%b, sp.expand(lhs-rhs)==0, dict(sorted(cur.items())))
        cur=pieri2(cur)
    for mu in [(0,0,0),(1,0,0),(2,1,0),(3,1,1),(2,2,2)]:
        a=toE(frs(mu)).subs({E1:E1+3,E2:E2+2*E1+3,E3:E3+E2+E1+1},simultaneous=True)
        print("Theorem C  mu=%s :"%str(mu), sp.expand(sp.expand(a)-sp.cancel(toE(frs(tuple(x+1 for x in mu)))/E3))==0)
