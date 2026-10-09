# longversion §9 printed: thm:2pt, lem:pair2, lem:shuffle, ex:tworow, thm:v2 (+ex:v2 polynomials), Gamma identity via prop:reduce.
from lv_engine import *
from check_DS_printed import estar, interp
from hl import HLP
import itertools, sympy as sp
def br(n,t): return (1-t**n)/(1-t)
def phi(m,t): return prod(1-t**i for i in range(1,m+1))
def qbinom(n,k,t): return phi(n,t)/(phi(k,t)*phi(n-k,t))
def psum(xs,r): return sum((v**r for v in xs),Fr(0))
def zee(mu):
    from collections import Counter
    from math import factorial
    z=1
    for p_,mm in Counter(mu).items(): z*=p_**mm*factorial(mm)
    return z
def p_expand(G,n,m):
    mus=list(partitions(n)); pts=[];b=[]
    while len(pts)<len(mus)+3:
        pt=rndpt(m)
        try: v=G(pt)
        except ZeroDivisionError: continue
        pts.append(pt); b.append(v)
    M=[[prod(psum(pt,r) for r in mu) for mu in mus] for pt in pts]
    return dict(zip(mus,solve(M,b)))
def Ta(a,g,x,t):
    m=len(x); tot=Fr(0)
    for A in itertools.combinations(range(m),a):
        cA=prod((x[i]-t*x[j])/(x[i]-x[j]) for i in A for j in range(m) if j not in A)
        tot+=cA*prod(x[i] for i in A)*g([x[i] for i in A])
    return tot
def Phi_formula(a,g,d,x,y,t):
    n=a+d; tot=Fr(0)
    for A in range(1,a):
        B=a-A
        w=sp.Symbol('w')
        T=sp.Rational(t.numerator,t.denominator)
        GA=sp.expand(g([T**i for i in range(A)]+[w*T**i for i in range(B)]))
        Gk=lambda k: Fr(str(sp.Poly(GA,w).coeff_monomial(w**k))) if k>=0 else Fr(0)
        inner=Gk(y-B)/((1-t**A)*(1-t**B))
        inner+=sum(((t**(-A*mm)-t**(B*mm))*Gk(y-B-mm) for mm in range(1,y-B+1)),Fr(0))/(1-t**a)
        tot+=t**(-A*B)*inner
    gpi=g([t**i for i in range(a)])
    tot-=gpi/(1-t**a)*sum(t**(-j*y) for j in range(a))
    return (-1)**a*(1-t**x)*(1-t**y)*tot
ok=True; cnt=0
gs=[((lambda z: psum(z,1)),1),((lambda z: psum(z,2)),2),((lambda z: psum(z,1)**2),2),((lambda z: psum(z,2)*psum(z,1)),3),((lambda z: psum(z,3)),3),((lambda z: Fr(1)),0)]
for a in range(1,4):
  for g,d in gs:
    n=a+d
    if n>6: continue
    t=rnd()
    pe=p_expand(lambda xx: Ta(a,g,xx,t),n,n)
    for x in range(1,n):
      y=n-x
      if x<y: continue
      key=tuple(sorted((x,y),reverse=True))
      pairing=zee(key)*pe.get(key,Fr(0))
      cnt+=1
      if pairing!=Phi_formula(a,g,d,x,y,t): ok=False; print('2PT FAIL',a,d,x,y)
      # also y,x order (formula should be symmetric in roles? Phi(x,y) with y the w-exponent)
      if Phi_formula(a,g,d,y,x,t)!=pairing: ok=False; print('2PT order FAIL',a,d,x,y)
print('thm:2pt vs power-sum pairing (%d cases, both orders):'%cnt, ok)
# lem:pair2
ok2=True
for lam in [(2,1),(2,2),(3,1),(2,1,1),(3,2),(4,1)]:
    t=rnd(); s=rnd(); n=sum(lam)
    G=lambda xx: Ek(lam[0],lambda yy: prod(esym(yy,q) for q in lam[1:]),xx,s,t)
    pe=p_expand(G,n,n); ee=e_expand(G,n,n)
    for x in range(1,n):
        y=n-x
        if x<y: continue
        key=(x,y); m_=2 if x==y else 1
        if zee(key)*pe.get(key,Fr(0))!=(-1)**n*(m_*ee.get(key,Fr(0))+ee.get((n,),Fr(0))): ok2=False; print('PAIR FAIL',lam,key)
print('lem:pair2:',ok2)
# lem:shuffle brute force
ok3=True
for A in range(0,4):
  for B in range(0,4):
    t=rnd(); w=rnd()
    tot=Fr(0)
    for pos in itertools.combinations(range(A+B),A):
        word=['V']*(A+B)
        for p_ in pos: word[p_]='U'
        ia=ib=0; seq=[]
        for L in word:
            if L=='U': seq.append(('U',ia)); ia+=1
            else: seq.append(('V',ib)); ib+=1
        f=Fr(1)
        for i in range(len(seq)):
            for j in range(i+1,len(seq)):
                (L1,k1),(L2,k2)=seq[i],seq[j]
                if L1==L2: continue
                if L1=='U': al,be=k1,k2; f*=(w*t**(be-al)-1)/(w*t**(be-al)-t)
                else: be,al=k1,k2; f*=(1-w*t**(be-al))/(1-w*t**(be-al+1))
        tot+=f
    pred=qbinom(A+B,A,t)*t**(-A*B)*(1-w)*(1-t**(B-A)*w)/((1-t**(-A)*w)*(1-t**B*w))
    if tot!=pred: ok3=False; print('SH FAIL',A,B)
    if A>0 and B>0:
        kap=(1-t**A)*(1-t**B)/(1-t**(A+B)); ws=Fr(1,1000)
        ser=1+kap*sum((t**(-A*mm)-t**(B*mm))*ws**mm for mm in range(1,40))
        val=(1-ws)*(1-t**(B-A)*ws)/((1-t**(-A)*ws)*(1-t**B*ws))
        if abs(float(ser-val))>1e-12: ok3=False; print('pf fail',A,B)
print('lem:shuffle (+partial fractions):',ok3)
# ex:tworow: X^lambda_(x,y) for two-row lambda, |lambda|<=6, from p_x p_y in P-basis
ok4=True
for n in range(2,7):
  for l2 in range(1,n//2+1):
    lam=(n-l2,l2)
    for y in range(1,n//2+1):
      x=n-y; t=rnd()
      kaps=list(partitions(n)); pts=[rndpt(n) for _ in range(len(kaps)+2)]
      M=[[HLP(k,pt,t) for k in kaps] for pt in pts]; bb=[psum(pt,x)*psum(pt,y) for pt in pts]
      X=dict(zip(kaps,solve(M,bb))).get(lam,Fr(0))
      mxy=2 if x==y else 1; L2=lam[1]
      if y<L2: pred=(t-1)*t**(L2-1-y)*(1+t**y)
      elif y==L2: pred=mxy-(1-t)*t**(L2-1)
      else: pred=(t-1)*t**(L2-1)
      if X!=pred: ok4=False; print('TWOROW FAIL',lam,(x,y),X,pred)
print('ex:tworow |lambda|<=6:',ok4)
