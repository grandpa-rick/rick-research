import sympy as sp, sys
from hl import *
s,t=sp.Rational(3,7),sp.Rational(-5,2)
m=int(sys.argv[1]); xs=sp.symbols(f'x1:{m+1}')
bad=0
for n in range(0,4):
  for mu in parts(n):
    F=sp.prod([e(p,xs) for p in mu])
    for k in range(1,m+1):
        if n+k>m: continue
        lhs=sp.expand(Ek(F,k,xs,s,t))
        ys=sp.symbols(f'y1:{k+1}')
        # F[X+(s-1)Y]: F in variables xs plus "virtual": e_r[X+(s-1)Y] = sum_j e_{r-j}(x) e_j[(s-1)Y]; e_j[(s-1)Y] = e_j[sY - Y]
        # compute via generating fn: E(z)[X+(s-1)Y] = prod(1+x z) prod(1+s y z)/prod(1+y z)
        z=sp.Symbol('z')
        gen=sp.prod([1+xi*z for xi in xs])*sp.prod([(1+s*y*z) for y in ys])*sp.prod([sp.series(1/(1+y*z),z,0,n+1).removeO() for y in ys])
        gen=sp.expand(gen)
        er=lambda r: sp.expand(gen.coeff(z,r))
        G=sp.expand(sp.prod([er(p) for p in mu]))
        # truncate higher z-terms irrelevant since we took coeff
        co=expand_in_P(G,ys,xs,t,n)
        rhs=sp.expand(sum(c*HLP(tuple(a+1 for a in rho)+(1,)*(k-len(rho)),xs,t) for rho,c in co.items() if len(rho)<=k))
        ok=sp.expand(lhs-rhs)==0
        if not ok: bad+=1
        print(n,mu,k,ok,flush=True)
print('bad',bad)
