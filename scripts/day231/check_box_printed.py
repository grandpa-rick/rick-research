# longversion §8 printed: thm:box, cor:column, lem:inversion (pointwise), thm:lin, cor:pieri, F_n(t^m) identity.
from lv_engine import *
from check_DS_printed import estar, interp, dom
from check_pieri_printed_defs import c as cnj, alpha, qp
import itertools, sympy as sp
def Fpoly(n,w,s,t): return sum((cnj(n,j,s,t)*w**j for j in range(n+1)),Fr(0))
def br(n,t): return (1-t**n)/(1-t)
def pi(a,j,s,t):
    # [u^j] prod_{m<a} (1+s u t^m)/(1+u t^m) via series
    coef=[Fr(1)]+[Fr(0)]*j
    for m in range(a):
        # multiply by (1+s u t^m) * sum_i (-u t^m)^i
        num=[Fr(1),s*t**m]
        new=[Fr(0)]*(j+1)
        for i in range(j+1):
            for d in range(2):
                if i+d<=j: new[i+d]+=coef[i]*num[d]
        coef=new
        inv=[(-t**m)**i for i in range(j+1)]
        new=[sum(coef[i-q]*inv[q] for q in range(i+1)) for i in range(j+1)]
        coef=new
    return coef[j]
def coeffs_stable(lam,s,t):
    lam=tuple(p for p in lam if p>0); n=sum(lam)
    if n==0: return {():Fr(1)}
    return e_expand(lambda x: estar(lam,x,s,t),n,n)
ok=True; cnt=0
for (lam,N) in [((2,1),2),((2,1),3),((2,2,1),2),((2,1,1),2),((3,1),3),((1,1,1),1),((1,1,1),2),((2,1,0),2),((3,2,0),3),((1,1),2)]:
    l=len(lam); s,t=rnd(),rnd()
    A=coeffs_stable(lam,s,t)
    comp=tuple(sorted([N-p for p in lam],reverse=True))
    B=coeffs_stable(comp,s,t)
    sig=N*l*(l-1)//2-(l-1)*sum(lam)
    for mu,v in A.items():
        if mu and mu[0]>N: continue
        if len(mu)>l: continue
        mup=list(mu)+[0]*(l-len(mu)); cm=tuple(sorted([N-p for p in mup],reverse=True)); cm=tuple(p for p in cm if p>0)
        cnt+=1
        if B.get(cm,Fr(0))!=s**sig*v: ok=False; print('BOX FAIL',lam,N,mu)
    # reverse direction: all support of B accounted
    for nu,v in B.items():
        if v==0: continue
        nup=list(nu)+[0]*(l-len(nu))
        if len(nu)>l: ok=False; print('box len fail')
print('thm:box (%d coefficient pairs):'%cnt, ok)
ok2=True
for lam in [(1,1),(2,1),(1,1,1),(2,1,0),(2,2,1),(1,0)]:
    l=len(lam); s,t=rnd(),rnd()
    A=coeffs_stable(lam,s,t); B=coeffs_stable(tuple(p+1 for p in lam),s,t)
    for mu,v in A.items():
        mup=list(mu)+[0]*(l-len(mu))
        if len(mup)>l: continue
        if B.get(tuple(p+1 for p in mup),Fr(0))!=s**(l*(l-1)//2)*v: ok2=False; print('COL FAIL',lam,mu)
print('cor:column:',ok2)
# lem:inversion pointwise, N=3
ok3=True
for k in range(0,4):
  for (G,g) in [(lambda y: esym(y,1),1),(lambda y: esym(y,2)*esym(y,1),3),(lambda y: Fr(1),0)]:
    for m in range(0,3):
      N=3; s,t=rnd(),rnd(); x=rndpt(N)
      F=lambda y,G=G,m=m: prod(y)**m*G([1/v for v in y])
      lhs=Ek(N-k,F,x,s,t) if N-k>0 else F(x)
      EkG=(lambda y: Ek(k,G,y,s,t)) if k>0 else G
      rhs=s**(m*(N-k)-g)*prod(x)**(m+1)*EkG([1/v for v in x])
      if lhs!=rhs: ok3=False; print('INV FAIL',k,g,m)
print('lem:inversion:',ok3)
# thm:lin
ok4=True
for k in range(1,4):
  for J in [(1,),(2,),(1,1),(3,),(2,1)]:
    s,t=rnd(),rnd(); d=sum(J); n=k+d
    co=e_expand(lambda x: Ek(k,lambda y: prod(esym(y,j) for j in J),x,s,t),n,n)
    pred=(-1)**d*br(n,t)/br(k,t)*prod(pi(k,j,s,t) for j in J)
    if co.get((n,),Fr(0))!=pred: ok4=False; print('LIN FAIL',k,J)
    # also check ring-map description p_r -> (s^r-1)[k]_{t^r} for e_j via Newton: e_2 = (p1^2-p2)/2
    P=lambda r: (s**r-1)*br(k,t**r)
    if pi(k,2,s,t)!=(P(1)**2-P(2))/2: ok4=False; print('ringmap fail')
print('thm:lin:',ok4)
# cor:pieri C-form vs engine (k,r<=4) and F_n(t^m) identity n<=m
def Cab(a,b,s,t):
    if a==0 or b==0: return Fr(1)
    return (-1)**b*br(a+b,t)/br(a,t)*pi(a,b,s,t)
ok5=True
for k in range(1,5):
  for r in range(0,5):
    s,t=rnd(),rnd(); n=k+r
    co=e_expand(lambda x: Ek(k,lambda y: esym(y,r),x,s,t),n,n)
    pred={}
    for y in range(min(k,r)+1):
        mu=tuple(sorted([q for q in (k+r-y,y) if q>0],reverse=True)); pred[mu]=pred.get(mu,0)+s**y*Cab(k-y,r-y,s,t)
    for mu in set(co)|set(pred):
        if co.get(mu,0)!=pred.get(mu,0): ok5=False; print('CPIERI FAIL',k,r,mu)
okF=True
for n_ in range(1,5):
  for m_ in range(n_,7):
    s,t=rnd(),rnd()
    if Fpoly(n_,t**m_,s,t)!=(-1)**m_*br(n_+m_,t)/br(n_,t)*pi(n_,m_,s,t): okF=False; print('Fnm fail',n_,m_)
okFlow=True
for n_ in range(2,5):
  for m_ in range(1,n_):
    s,t=rnd(),rnd()
    if Fpoly(n_,t**m_,s,t)!=(-1)**m_*br(n_+m_,t)/br(n_,t)*pi(n_,m_,s,t): okFlow=False
print('cor:pieri C-form:',ok5,' F_n(t^m) identity 1<=n<=m:',okF,' (m<n, not claimed):',okFlow)
