# longversion §6 printed statements: prop:M, thm:blocklaw, thm:coarse (history formula), thm:W, lem:linT, lem:linP.
from lv_engine import *
from check_DS_printed import estar, interp, nfun, conj, dom
from hl import HLP
import itertools
def br(n,t): return (1-t**n)/(1-t)
def hcoeffs(fun,P=16):
    """fun(s)->value; return coefficients in h=s-1 (polynomial, deg<P)"""
    hs=[Fr(i+1,i+3)*(-1)**i for i in range(P)]+[Fr(5,7)]
    ys=[fun(1+h) for h in hs]; c=interp(hs[:P],ys[:P])
    assert sum(c[j]*hs[P]**j for j in range(P))==ys[P]
    return c
def setparts(S):
    S=list(S)
    if not S: yield []; return
    f=S[0]
    for rest in setparts(S[1:]):
        for i in range(len(rest)):
            yield rest[:i]+[[f]+rest[i]]+rest[i+1:]
        yield [[f]]+rest
def kappa(lam,mu):
    best=-10**9
    for pl in setparts(range(len(lam))):
        # need to split mu into same number of blocks with matching sums and dominance
        sums=[sum(lam[i] for i in B) for B in pl]
        for pm in setparts(range(len(mu))):
            if len(pm)!=len(pl): continue
            ms=[sum(mu[i] for i in B) for B in pm]
            for perm in itertools.permutations(range(len(pm))):
                okk=True
                for a,B in enumerate(pl):
                    C=pm[perm[a]]
                    if sums[a]!=ms[perm[a]]: okk=False;break
                    l1=tuple(sorted([lam[i] for i in B],reverse=True)); m1=tuple(sorted([mu[i] for i in C],reverse=True))
                    if not dom(m1,l1): okk=False;break
                if okk: best=max(best,len(pl)); break
    return best
def L(a,b,t): return (1-t**(a+b))*(t**(a*b)-1)/((1-t**a)*(1-t**b))
if __name__=="__main__":
    ok=True
    # prop:M
    for k in range(1,5):
      for r in range(0,k+1):
        t=rnd(); n=k+r
        pts_coef={}
        got={}
        mus=list(partitions(n))
        data=[]
        hs=None
        c=None
        # e-coefficients as functions of s
        def ecoef(s_): return e_expand(lambda x: Ek(k,lambda y: esym(y,r),x,s_,t),n,n)
        hsP=[Fr(i+1,i+3)*(-1)**i for i in range(10)]
        D=[ecoef(1+h) for h in hsP]
        for mu in mus:
            cc=interp(hsP,[d.get(mu,Fr(0)) for d in D]); got[mu]=cc[1]
        pred={}
        def add(a,b,v):
            key=tuple(sorted([q for q in (a,b) if q>0],reverse=True)); pred[key]=pred.get(key,0)+v
        add(k,r,r)
        for j in range(1,r+1): add(k+j,r-j,L(k-r+j,j,t))
        for mu in set(got)|set(pred):
            if got.get(mu,0)!=pred.get(mu,0): ok=False; print('M FAIL',k,r,mu,got.get(mu),pred.get(mu))
    print('prop:M k<=4:',ok)
    # thm:blocklaw, n<=5, t generic and t=0
    ok2=True; cnt=0
    for t in [Fr(3,5),Fr(0)]:
      for n in range(2,6):
        for lam in partitions(n):
          cs={}
          hsP=[Fr(i+1,i+3)*(-1)**i for i in range(14)]
          D=[e_expand(lambda x: estar(lam,x,1+h,t),n,n) for h in hsP]
          for mu in partitions(n):
            cc=interp(hsP,[d.get(mu,Fr(0)) for d in D])
            if mu==lam: continue
            kap=kappa(lam,mu); l=len(lam)
            nz=[j for j,v in enumerate(cc) if v!=0]
            if kap<0:
                if nz: ok2=False; print('support',lam,mu)
                continue
            cnt+=1
            if not nz or nz[0]!=l-kap: ok2=False; print('VAL FAIL',lam,mu,t,nz[:1],l-kap)
            elif t==0:
                lead=cc[l-kap]
                if lead.denominator!=1 or lead*(-1)**(l-kap)<1: ok2=False; print('t0 lead FAIL',lam,mu,lead)
    print('thm:blocklaw val=l-kappa (%d pairs, t=3/5 and 0), t=0 lead sign:'%cnt, ok2)
    # thm:W from printed definition (iterated commutator) vs closed form
    def Ep_apply(k,p,F,t):
        """returns function x-> E_k^{(p)}F(x) via h-interpolation pointwise"""
        def g(x):
            P=k*0+p+8
            hsP=[Fr(i+1,i+3)*(-1)**i for i in range(P)]
            ys=[Ek(k,F,x,1+h,t) for h in hsP]
            return interp(hsP,ys)[p]
        return g
    ok3=True; cntW=0
    for k in range(1,4):
      for J in [(1,),(2,),(1,1),(3,),(2,1),(1,1,1),(2,2)]:
        p=len(J); d=sum(J); n=k+d
        if n>6: continue
        t=rnd()
        def comm(x):
            tot=Fr(0)
            for T in itertools.product([0,1],repeat=p):
                Tin=[J[i] for i in range(p) if T[i]]; Tout=[J[i] for i in range(p) if not T[i]]
                sign=(-1)**len(Tout)
                F=lambda y,Tin=Tin: prod(esym(y,j) for j in Tin)
                tot+=sign*prod(esym(x,j) for j in Tout)*Ep_apply(k,p,F,t)(x)
            return tot
        co=e_expand(comm,n,n)
        W=co.get((n,),Fr(0))
        pred=(-1)**p*br(n,t)/br(k,t)*prod(br(k,t**j) for j in J)
        cntW+=1
        if W!=pred: ok3=False; print('W FAIL',k,J,W,pred)
    print('thm:W from printed commutator definition (%d cases):'%cntW, ok3)
    # lem:linT
    ok4=True
    for k in range(1,4):
      for f in [lambda y: Fr(1), lambda y: sum(y), lambda y: sum(v**2 for v in y), lambda y: sum(y)*sum(v**2 for v in y), lambda y: prod(y)*sum(y)]:
        t=rnd()
        # degree of f: probe
        for d in range(0,5):
            pt=[Fr(2)]*k
            if f([v*3 for v in pt])==f(pt)*3**d: break
        n=k+d
        T=lambda x: sum((prod((x[i]-t*x[j])/(x[i]-x[j]) for i in A for j in range(len(x)) if j not in A)*prod(x[i] for i in A)*f([x[i] for i in A]) for A in itertools.combinations(range(len(x)),k)),Fr(0))
        co=e_expand(T,n,n)
        pred=(-1)**d*br(n,t)/br(k,t)*f([t**i for i in range(k)])
        if co.get((n,),Fr(0))!=pred: ok4=False; print('linT FAIL',k,d)
    print('lem:linT:',ok4)
    # lem:linP
    ok5=True
    for lam in [(2,1),(3,1),(2,2),(3,2),(2,1,1),(3,2,1),(2,2,1)]:
        t=rnd(); n=sum(lam); k=len(lam)
        co=e_expand(lambda x: HLP(lam,x,t),n,n)
        rho=[p-1 for p in lam]
        pred=(-1)**(n-k)*br(n,t)/br(k,t)*HLP(tuple(q for q in rho if q>0),[t**i for i in range(k)],t)
        if co.get((n,),Fr(0))!=pred: ok5=False; print('linP FAIL',lam)
    print('lem:linP:',ok5)
    