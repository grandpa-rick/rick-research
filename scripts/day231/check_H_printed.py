# Thm H (1),(3) and Cor dmatrix, re-implemented from PRINTED statements (longversion §5).
from check_DS_printed import estar, interp, nfun, conj, dom
from lv_engine import *
import itertools
def qbin(N,r,t):
    if r<0 or r>N: return Fr(0)
    return prod(1-t**(N-i) for i in range(r))/prod(1-t**(i+1) for i in range(r))
def mult(kap,v): return sum(1 for p in kap if p==v)
def vstrips(kap,k):
    """rho with kap/rho vertical k-strip, with data r_v"""
    vals=sorted(set(kap))
    for rs in itertools.product(*[range(mult(kap,v)+1) for v in vals]):
        if sum(rs)!=k: continue
        r=dict(zip(vals,rs)); rho=[]
        for v in vals:
            rho+= [v]*(mult(kap,v)-r[v]) + [v-1]*r[v]
        yield tuple(sorted([p for p in rho if p>0],reverse=True)), r
def predicted(mu,k,t):
    rho0=conj(mu); out={}
    n=sum(mu)+k
    for nu in partitions(n):
        kap=conj(nu); tot=Fr(0)
        for rho,r in vstrips(kap,k):
            if rho!=rho0: continue
            inv=sum(r[v]*(mult(kap,w)-r[w]) for v in r for w in r if v<w)
            tot+=t**inv*prod(qbin(mult(kap,v),r[v],t) for v in r)
        if tot!=0: out[nu]=tot
    return out
ok=True; cnt=0
for t in [Fr(-5,11),Fr(3,2)]:
  for n in range(0,5):
    for mu in (partitions(n) if n>0 else [()]):
      for k in range(1,6-n):
        N=n+k; P=18; ss=[Fr(i+2,i+5)*(-1)**i for i in range(P)]+[Fr(7,3)]
        data=[e_expand(lambda x: Ek(k,lambda y: s_**nfun(mu)*prod(esym(y,p) for p in mu),x,s_,t),N,N) for s_ in ss]
        pred=predicted(mu,k,t)
        for nu in partitions(N):
          ys=[d.get(nu,Fr(0)) for d in data]; c=interp(ss[:P],ys[:P])
          if sum(c[j]*ss[P]**j for j in range(P))!=ys[P]: ok=False; print('interp',mu,k,nu)
          e0=nfun(nu)
          if any(c[j]!=0 for j in range(min(e0,P))): ok=False; print('INTEGRALITY FAIL',mu,k,nu,t)
          lim=c[e0] if e0<P else Fr(0)
          if lim!=pred.get(nu,Fr(0)): ok=False; print('MATRIX FAIL',mu,k,nu,t,lim,pred.get(nu))
        cnt+=1
print('Thm H (1),(3): %d (mu,k,t) cases:'%cnt, ok)
# Cor dmatrix first formula: HL P via Macdonald symmetrisation, pointwise
def HLP(lam,x,u):
    m=len(x); lamp=list(lam)+[0]*(m-len(lam))
    tot=Fr(0)
    for w in itertools.permutations(range(m)):
        y=[x[w[i]] for i in range(m)]
        term=prod(y[i]**lamp[i] for i in range(m))*prod((y[i]-u*y[j])/(y[i]-y[j]) for i in range(m) for j in range(i+1,m))
        tot+=term
    # v_lambda(u)
    from collections import Counter
    v=Fr(1)
    for part,mm in Counter(lamp).items():
        v*=prod((1-u**(i+1))/(1-u) for i in range(mm))
    return tot/v
def e_to_P(lam,u,m):
    n=sum(lam); kaps=list(partitions(n)); pts=[];
    while len(pts)<len(kaps)+2: pts.append(rndpt(m))
    M=[[HLP(kap,p,u) for kap in kaps] for p in pts]; b=[prod(esym(p,r) for r in lam) for p in pts]
    return dict(zip(kaps,solve(M,b)))
ok2=True
for t in [Fr(-5,11),Fr(2,3)]:
  for n in range(1,5):
    for lam in partitions(n):
      P=16; ss=[Fr(i+2,i+5)*(-1)**i for i in range(P)]
      data=[e_expand(lambda x: estar(lam,x,s_,t),n,n) for s_ in ss]
      MP=e_to_P(lam,1/t,n)
      for mu in partitions(n):
        c=interp(ss,[d.get(mu,Fr(0)) for d in data]); d_=c[nfun(mu)]
        pred=t**(nfun(conj(mu))-nfun(conj(lam)))*MP.get(conj(mu),Fr(0))
        if d_!=pred: ok2=False; print('DMATRIX FAIL',lam,mu,t,d_,pred)
print('Cor dmatrix first formula n<=4:',ok2)
# N[t] and t=1 count, n<=4
ok3=True
def M01(lam,col):
    # count 0-1 matrices row sums lam, col sums col
    from functools import lru_cache
    cols=tuple(col)
    @lru_cache(None)
    def rec(i,cs):
        if i==len(lam): return 1 if all(c==0 for c in cs) else 0
        tot=0
        for S in itertools.combinations(range(len(cs)),lam[i]):
            if all(cs[j]>0 for j in S):
                tot+=rec(i+1,tuple(cs[j]-(1 if j in S else 0) for j in range(len(cs))))
        return tot
    return rec(0,cols)
for n in range(1,5):
  for lam in partitions(n):
    ts=[Fr(j+2,j+3)*(-1)**j for j in range(9)]
    dvals={}
    for t in ts:
      P=14; ss=[Fr(i+2,i+5)*(-1)**i for i in range(P)]
      data=[e_expand(lambda x: estar(lam,x,s_,t),n,n) for s_ in ss]
      for mu in partitions(n):
        c=interp(ss,[d.get(mu,Fr(0)) for d in data]); dvals.setdefault(mu,[]).append(c[nfun(mu)])
    for mu in partitions(n):
      dt=interp(ts,dvals[mu])
      if any(x.denominator!=1 or x<0 for x in dt): ok3=False; print('N[t] FAIL',lam,mu,dt)
      if sum(dt)!=M01(lam,conj(mu)): ok3=False; print('t=1 FAIL',lam,mu)
print('Cor dmatrix: d in N[t], d(1)=#0-1 matrices, n<=4:',ok3)
