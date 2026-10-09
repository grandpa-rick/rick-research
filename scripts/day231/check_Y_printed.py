# Printed conventions of longversion §2.2: T_i, pi, Y_i; check t^{-C(k,2)} e_k(Y) F == E_k F (Thm subset), m=3,4.
import sympy as sp, itertools
from math import comb
s,t=sp.Rational(3,7),sp.Rational(-5,4)
def run(m):
    x=sp.symbols('x1:%d'%(m+1))
    def sw(f,i): return f.subs({x[i-1]:x[i],x[i]:x[i-1]},simultaneous=True)
    def T(i,f): return sp.cancel(t*sw(f,i)+(t-1)*x[i]/(x[i-1]-x[i])*(sw(f,i)-f))
    def Tinv(i,f): return sp.cancel((T(i,f)-(t-1)*f)/t)
    def pi(f):
        sub={x[j]:x[j+1] for j in range(m-1)}; sub[x[m-1]]=s*x[0]
        return sp.cancel(x[0]*f.subs(sub,simultaneous=True))
    def Y(i,f):
        for j in range(i,m): f=Tinv(j,f)          # T_{m-1}^{-1}...T_i^{-1}: rightmost (T_i^{-1}) acts first
        f=pi(f)
        for j in range(1,i): f=T(j,f)            # T_{i-1}...T_1: T_1 acts first
        return sp.cancel(t**(m-i)*f)
    def ekY(k,f):
        tot=0
        for B in itertools.combinations(range(1,m+1),k):
            g=f
            for b in reversed(B): g=Y(b,g)          # Y_{b_k} acts first
            tot+=g
        return sp.expand(sp.cancel(tot))
    def Ek(k,F):
        tot=0
        for A in itertools.combinations(range(m),k):
            cA=sp.prod([(x[i]-t*x[j])/(x[i]-x[j]) for i in A for j in range(m) if j not in A])
            tot+=cA*sp.prod([x[i] for i in A])*F.subs({x[i]:s*x[i] for i in A},simultaneous=True)
        return sp.expand(sp.cancel(tot))
    e=lambda r: sp.Integer(sum(sp.prod(c) for c in itertools.combinations(x,r))) if r==0 else sum(sp.prod(c) for c in itertools.combinations(x,r))
    ok=True
    for k in range(1,m+1):
        for F in [sp.Integer(1),e(1),e(2),e(1)**2,e(1)*e(2)]:
            lhs=sp.expand(t**(-comb(k,2))*ekY(k,F)); rhs=Ek(k,F)
            if sp.expand(lhs-rhs)!=0: ok=False; print('FAIL m',m,'k',k,F)
    print('m=%d subset formula from printed Y:'%m, ok)
    # Hikita Thm 3.12 check: e1*e_r
    for r in range(1,m):
        lhs=Ek(1,e(r)); rhs=sp.expand((1-s)*(1-t**(r+1))/(1-t)*e(r+1)+s*e(1)*e(r))
        print('  e1*e%d Hikita rule:'%r, sp.expand(lhs-rhs)==0)
run(3); run(4)
