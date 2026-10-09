# Thm DS / Cor opDS / Lem Ek1 / Lem stable / Peel Lemma / remark d=1+3t, re-implemented from PRINTED statements.
from lv_engine import *
import sys, itertools
def nfun(l): return sum(i*p for i,p in enumerate(l))
def conj(l): return tuple(sum(1 for p in l if p>j) for j in range(l[0])) if l else ()
def dom(a,b): # a >= b (dominance), same size
    sa=sb=0
    for i in range(max(len(a),len(b))):
        sa+=a[i] if i<len(a) else 0; sb+=b[i] if i<len(b) else 0
        if sa<sb: return False
    return True
def estar(lam,x,s,t):
    if not lam: return Fr(1)
    k=lam[0]; rest=lam[1:]
    return Ek(k,lambda y: estar(rest,y,s,t),x,s,t)
def coeffs(lam,s,t,m):
    n=sum(lam); return e_expand(lambda x: estar(lam,x,s,t),n,m)
def interp(xs,ys):
    # Newton -> monomial coefficients
    n=len(xs); coef=[Fr(0)]*n
    for i in range(n):
        num=[Fr(1)]; den=Fr(1)
        for j in range(n):
            if j==i: continue
            num=[ (num[k-1] if k>0 else 0) - xs[j]*(num[k] if k<len(num) else 0) for k in range(len(num)+1)]
            den*=xs[i]-xs[j]
        for k in range(len(num)): coef[k]+=ys[i]*num[k]/den
    return coef
if __name__=="__main__":
    N=int(sys.argv[1]) if len(sys.argv)>1 else 5
    ok=True; report=[]
    for t in [Fr(-5,11),Fr(0)]:
      for n in range(1,N+1):
        m=n
        for lam in partitions(n):
          P=26
          ss=[Fr(i+2,i+5)*(-1)**i for i in range(P)]+[Fr(7,3),Fr(-9,4)]
          data=[coeffs(lam,s_,t,m) for s_ in ss]
          mus=list(partitions(n))
          for mu in mus:
            ys=[d.get(mu,Fr(0)) for d in data]
            c=interp(ss[:P],ys[:P])
            ev=lambda s_: sum(c[k]*s_**k for k in range(P))
            if ev(ss[P])!=ys[P] or ev(ss[P+1])!=ys[P+1]: ok=False; print('interp fail',lam,mu); continue
            nz=[k for k in range(P) if c[k]!=0]
            if not dom(mu,lam):
                if nz: ok=False; print('SUPPORT FAIL',lam,mu,t)
                continue
            if not nz: ok=False; print('ZERO in up-set',lam,mu,t); continue
            if nz[0]!=nfun(mu): ok=False; print('VAL FAIL',lam,mu,t,nz[0],nfun(mu))
            if mu==lam and (nz!=[nfun(lam)] or c[nfun(lam)]!=1): ok=False; print('DIAG FAIL',lam)
            if mu!=lam and sum(c)!=0: ok=False; print('s=1 FAIL',lam,mu)
            if t==0 and c[nfun(mu)]!=1: ok=False; print('t0 lead FAIL',lam,mu)
      print('t=%s: Thm DS printed statement n<=%d:'%(t,N), ok)
    # Cor opDS: e_k * e_mu
    ok2=True
    for n in range(2,N+1):
      for mu in partitions(n-1):
        pass
    for k in range(1,4):
      for mu in [(1,),(2,),(1,1),(2,1),(3,),(2,2)]:
        lamk=tuple(sorted(mu+(k,),reverse=True)); n=sum(lamk)
        if n>6: continue
        s,t=rnd(),rnd()
        got=e_expand(lambda x: Ek(k,lambda y: prod(esym(y,p) for p in mu),x,s,t),n,n)
        for nu,v in got.items():
            if v==0: continue
            if nu==lamk:
                if v!=s**sum(min(p,k) for p in mu): ok2=False; print('opDS lead fail',k,mu)
            elif not (dom(nu,lamk)): ok2=False; print('opDS supp fail',k,mu,nu)
    print('Cor opDS:',ok2)
    # Lem Ek1 and stability
    ok3=True
    for m in range(1,6):
      for k in range(1,m+1):
        s,t=rnd(),rnd(); x=rndpt(m)
        if Ek(k,lambda y: Fr(1),x,s,t)!=esym(x,k): ok3=False
        F=lambda y: esym(y,2)*esym(y,1)+esym(y,3)
        x0=x[:-1]+[Fr(0)]
        # x_m=0 is allowed after cancellation; evaluate limit by small perturbation-free route: compare polynomial identity at x_m=eps->0 via exact e-expansion instead
    print('Lem Ek1:',ok3)
    ok4=True
    for lam in [(2,1),(2,2),(3,1),(2,1,1)]:
      n=sum(lam); s,t=rnd(),rnd()
      a=e_expand(lambda x: estar(lam,x,s,t),n,n); b=e_expand(lambda x: estar(lam,x,s,t),n,n+1)
      if a!=b: ok4=False; print('stability fail',lam)
    print('Lem stable (m=n vs n+1):',ok4)
    # remark d_{1111,211}=1+3t
    ok5=True
    for t in [Fr(2),Fr(-3,7),Fr(5)]:
      P=14; ss=[Fr(i+2,i+5)*(-1)**i for i in range(P)]
      ys=[coeffs((1,1,1,1),s_,t,4).get((2,1,1),Fr(0)) for s_ in ss]
      c=interp(ss,ys)
      if c[nfun((2,1,1))]!=1+3*t: ok5=False; print('d fail',t,c[nfun((2,1,1))])
    print('d_(1111),(211)=1+3t:',ok5)
    # Peel lemma brute force n<=10
    def peel(k,kap):
        l=list(kap); 
        for i in range(k): l[i]-=1
        return tuple(sorted([p for p in l if p>0],reverse=True))
    ok6=True; cnt=0
    for n in range(1,11):
      P=list(partitions(n))
      for rho in P:
        for kap in P:
          if not dom(rho,kap): continue
          for k in range(1,len(rho)+1):
            cnt+=1
            if not dom(peel(k,rho),peel(k,kap)): ok6=False
    print('Peel Lemma n<=10 (%d triples):'%cnt, ok6)
    # q-binomial identity sum_B prod (x_i - t x_j)/(x_i-x_j) = [L choose r]_t
    from math import comb
    ok7=True
    def qbin(L,r,t):
        num=prod(1-t**(L-i) for i in range(r)); den=prod(1-t**(i+1) for i in range(r)); return num/den
    for L in range(1,6):
      for r in range(0,L+1):
        for t in [rnd(),Fr(0)]:
          x=rndpt(L)
          sB=sum((prod((x[i]-t*x[j])/(x[i]-x[j]) for i in B for j in range(L) if j not in B) for B in itertools.combinations(range(L),r)),Fr(0))
          if sB!=qbin(L,r,t): ok7=False
    print('level-set q-binomial identity:',ok7)
    