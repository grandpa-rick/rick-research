import sympy as sp,sys
sys.argv=[0,'1']
sys.path.insert(0,'/tmp/hl')
from w import HLP, parts
from r import raise_coeffs
t=sp.symbols('t')
for n in range(2,5):
    P=parts(n);N=len(P);W=sp.zeros(N,N)
    for a,lam in enumerate(P):
        q,y,v=HLP(lam,n);d=q.as_dict()
        for b,mu in enumerate(P):
            W[a,b]=sp.cancel(d.get(tuple(list(mu)+[0]*(n-len(mu))),0)/v)
    Wi=W.inv()
    bad=0
    for c,lam in enumerate(P):
        rc=raise_coeffs(lam,n)
        for r_,mu in enumerate(P):
            if sp.simplify(Wi[r_,c]-rc.get(mu,0))!=0: bad+=1
    print(n,'mismatches',bad,flush=True)
