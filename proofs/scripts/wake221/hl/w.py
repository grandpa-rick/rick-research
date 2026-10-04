import sympy as sp, itertools
from sympy.utilities.iterables import partitions
t=sp.symbols('t')
def parts(n):
    return [tuple(sorted([k for k,v in p.items() for _ in range(v)],reverse=True)) for p in partitions(n)]
def dom(a,b): # a >= b
    sa=sb=0
    for i in range(max(len(a),len(b))):
        sa+= a[i] if i<len(a) else 0; sb+= b[i] if i<len(b) else 0
        if sa<sb: return False
    return True
def HLP(lam,n):
    x=sp.symbols('x0:%d'%n)
    lam=list(lam)+[0]*(n-len(lam))
    base=sp.Mul(*[x[i]**lam[i] for i in range(n)])*sp.Mul(*[x[i]-t*x[j] for i in range(n) for j in range(i+1,n)])
    num=0
    for w in itertools.permutations(range(n)):
        sgn=sp.combinatorics.Permutation(list(w)).signature()
        num+=sgn*base.subs({x[i]:sp.Symbol('y%d'%w[i]) for i in range(n)},simultaneous=True)
    y=sp.symbols('y0:%d'%n)
    V=sp.Mul(*[y[i]-y[j] for i in range(n) for j in range(i+1,n)])
    q,r=sp.div(sp.Poly(sp.expand(num),*y),sp.Poly(V,*y))
    assert r.is_zero
    from collections import Counter
    v=1
    for m in Counter(lam).values():
        for j in range(1,m+1): v*= sp.cancel((1-t**j)/(1-t))
    return q,y,v
def val(e):
    e=sp.factor(e)
    if e==0: return None
    k=0
    while True:
        e2=sp.cancel(e/(1-t))
        if sp.denom(e2).subs(t,1)==0 or sp.simplify(e.subs(t,1))!=0: break
        e=e2;k+=1
    return k
def kappa(lam,mu):
    # max blocks: partition multisets of parts compatibly
    from functools import lru_cache
    @lru_cache(None)
    def best(L,M):
        if not L and not M: return 0
        if not L or not M: return -10**9
        b=-10**9
        # choose block containing L[0]: subsets
        Ls=list(L); Ms=list(M)
        res=-10**9
        for i in range(0,1<<(len(Ls)-1)):
            sub=[Ls[0]]+[Ls[j+1] for j in range(len(Ls)-1) if i>>j&1]
            rest=[Ls[j+1] for j in range(len(Ls)-1) if not i>>j&1]
            s=sum(sub)
            for k in range(1,1<<len(Ms)):
                msub=[Ms[j] for j in range(len(Ms)) if k>>j&1]
                if sum(msub)!=s: continue
                mrest=[Ms[j] for j in range(len(Ms)) if not k>>j&1]
                a=tuple(sorted(sub,reverse=True)); m=tuple(sorted(msub,reverse=True))
                if dom(m,a):
                    r=best(tuple(sorted(rest,reverse=True)),tuple(sorted(mrest,reverse=True)))
                    res=max(res,1+r)
        return res
    return best(tuple(lam),tuple(mu))
import sys
if __name__!="__main__": sys.argv=[0,"1"]
for n in range(2,int(sys.argv[1])+1):
    P=parts(n); N=len(P)
    W=sp.zeros(N,N)
    for a,lam in enumerate(P):
        q,y,v=HLP(lam,n)
        d=q.as_dict()
        for b,mu in enumerate(P):
            e=tuple(list(mu)+[0]*(n-len(mu)))
            W[a,b]=sp.cancel(d.get(e,0)/v)
    Wi=sp.simplify(W.inv())
    for name,M in (('W',W),('Winv',Wi)):
        ok1=ok2=0;tot=0;bad=[]
        for a,lam in enumerate(P):
            for b,mu in enumerate(P):
                if a==b or M[a,b]==0: continue
                tot+=1; v_=val(M[a,b])
                # row index a=lam, column b=mu
                p1=len(lam)-kappa(lam,mu) if dom(mu,lam) else None
                p2=len(mu)-kappa(mu,lam) if dom(lam,mu) else None
                ok1+= (v_==p1); ok2+=(v_==p2)
                if n==6 and name=='Winv' and lam==(2,2,2) or (lam,mu)==((5,1),(2,2,2)) or (lam,mu)==((2,2,2),(5,1)): bad.append((lam,mu,v_,p1,p2))
        print(n,name,'nonzero offdiag',tot,'match ell(row)-kappa',ok1,'match ell(col)-kappa',ok2,bad)
