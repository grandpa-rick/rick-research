# Thm ellcol as printed: Gamma_k (via printed subset formula) == T_k (printed V, K), pointwise exact.
from lv_engine import *
from check_pieri_printed_defs import c
import itertools
def K(i,j,z,w,s,t):
    return prod((t**p*z-s*w)/(t**p*z-t**j*w) for p in range(i))*prod((s*z-t**r*w)/(t**i*z-t**r*w) for r in range(j))
def comps(n,l):
    if l==1: yield (n,); return
    for a in range(n+1):
        for rest in comps(n-a,l-1): yield (a,)+rest
def V(n,I,z,s,t):
    l=len(I); S=sum(I)
    if any(i<0 for i in I): return Fr(0)
    KI=prod(K(I[a],I[b],z[a],z[b],s,t) for a in range(l) for b in range(a+1,l))
    tot=Fr(0)
    for ns in comps(n,l):
        if any(ns[a]<I[a] for a in range(l)): continue
        ex=-sum((ns[a]-I[a])*I[b] for a in range(l) for b in range(l) if a!=b)
        tot+=t**ex*prod(t**(-ns[a]*I[a])*c(ns[a],I[a],s,t)*z[a]**(-ns[a]) for a in range(l))
    return KI*s**((l-1)*(n-S))*tot
def V2explicit(n,i,j,z,w,s,t):   # Cor twocol printed form
    tot=Fr(0)
    for n1 in range(n+1):
        n2=n-n1
        tot+=s**(n-i-j)*t**(-(n1-i)*j-(n2-j)*i-n1*i-n2*j)*c(n1,i,s,t)*c(n2,j,s,t)*z**(-n1)*w**(-n2)
    return K(i,j,z,w,s,t)*tot
def E(xs,z): return prod(1+xx*z for xx in xs)
ok=True; cnt=0
for l in (1,2,3):
  for m in range(0,6 if l<3 else 5):
    for k in range(0,5):
      s,t=rnd(),rnd(); x=rndpt(m); z=[rnd() for _ in range(l)]
      G=Ek(k,lambda y: prod(E(y,zz) for zz in z),x,s,t) if k>0 else prod(E(x,zz) for zz in z)
      T=Fr(0)
      for b in range(k+1):
        for S in range(k-b+1):
          for I in comps(S,l):
            T+=(s**l*t**(-S))**b*V(k-b,I,z,s,t)*esym(x,b)*prod(E(x,t**I[a]*z[a]) for a in range(l))
      cnt+=1
      if G!=T: ok=False; print('FAIL l,m,k',l,m,k)
print('Thm ellcol pointwise (%d cases):'%cnt, ok)
ok2=True
for n in range(6):
  for i in range(4):
    for j in range(4):
      s,t=rnd(),rnd(); z,w=rnd(),rnd()
      if V(n,(i,j),[z,w],s,t)!=V2explicit(n,i,j,z,w,s,t): ok2=False; print('V2 FAIL',n,i,j)
print('Cor twocol explicit V == general V:',ok2)
# Lemma Z
okZ=True
for l in range(1,6):
  for _ in range(3):
    la=[rnd() for _ in range(l)]; mu=[rnd() for _ in range(l)]
    lhs=prod(m_-1 for m_ in mu)-prod(a-1 for a in la)
    rhs=sum((mu[c_]-la[c_])*prod((la[d]-1)*(la[c_]-mu[d])/(la[c_]-la[d]) for d in range(l) if d!=c_) for c_ in range(l))
    if lhs!=rhs: okZ=False
print('Lemma Z l<=5:',okZ)
# Lemma Cj: series check; D_j formula and recursion; K symmetry
from check_pieri_printed_defs import alpha, qp
okC=True
for j in range(5):
  s,t=rnd(),rnd(); xx=Fr(1,1000003)
  # compare coefficients via truncated series in exact arithmetic: build series of RHS
  N=12
  g=[qp(s,t,n)/qp(t,t,n) for n in range(N+1)]
  Gt=[g[n]*t**n for n in range(N+1)]           # G(tx)
  D=alpha(j,s,t)-s*alpha(j-1,s,t)
  # (1 - s t^{-j} x)/(1-x) series
  h=[Fr(1)]+[1-s*t**(-j) for _ in range(N)]
  conv=[sum(Gt[a]*h[n-a] for a in range(n+1)) for n in range(N+1)]
  rhs=[Fr(0)]*(N+1)
  for n in range(N+1-j): rhs[n+j]=D*conv[n]
  lhs=[c(n,j,s,t) for n in range(N+1)]
  if lhs!=rhs: okC=False; print('Cj FAIL',j)
  if j>=1:
    if D!=alpha(j-1,s,t)*t**j*(s-1)/(1-t**j): okC=False; print('Dj FAIL')
    Dm=alpha(j-1,s,t)-s*alpha(j-2,s,t)
    if (1-t**j)*D!=(t*s-t**j)*Dm: okC=False; print('Drec FAIL')
  # (1-x)G(x)=(1-sx)G(tx)
  for n in range(1,N+1):
    if g[n]-g[n-1]!=t**n*g[n]-s*t**(n-1)*g[n-1]: okC=False
print('Lemma Cj:',okC)
okK=True
for i in range(4):
  for j in range(4):
    s,t,z,w=rnd(),rnd(),rnd(),rnd()
    if K(i,j,z,w,s,t)!=K(j,i,w,z,s,t): okK=False
print('K symmetry:',okK)
