# Checks of longversion.tex §3 printed statements against the printed subset formula (Thm 2.x).
from lv_engine import *
import sympy as sp
def qp(a,t,n): return prod(1-a*t**i for i in range(n))
def alpha(j,s,t):
    if j<0: return Fr(0)
    return prod((s-t**i)/(1-t**i) for i in range(1,j+1))
def c(n,j,s,t):
    if j<0 or j>n: return Fr(0)
    return qp(s,t,n-j)/qp(t,t,n-j)*(alpha(j,s,t)-s*t**(n-j)*alpha(j-1,s,t))
def Fpoly(n,w,s,t): return sum((c(n,j,s,t)*w**j for j in range(n+1)),Fr(0))
ok=True
# --- Cor pieri-ekr vs engine
for k in range(1,5):
  for r in range(0,6):
    s,t=rnd(),rnd(); m=k+r
    if m==0: continue
    got=e_expand(lambda x: Ek(k,lambda y: esym(y,r),x,s,t),k+r,m)
    pred={}
    for b in range(0,k+1):
        mu=tuple(sorted([q for q in (b,r+k-b) if q>0],reverse=True))
        pred[mu]=pred.get(mu,0)+s**b*Fpoly(k-b,t**(r-b),s,t)
    for mu in set(got)|set(pred):
        if got.get(mu,0)!=pred.get(mu,0): ok=False; print('PIERI FAIL',k,r,mu)
print('Cor pieri-ekr k<=4 r<=5:', ok)
# --- support min(k,r): collected pred has only b<=min
for k in range(1,5):
  for r in range(0,6):
    s,t=rnd(),rnd()
    pred={}
    for b in range(k+1):
        mu=tuple(sorted([q for q in (b,r+k-b) if q>0],reverse=True)); pred[mu]=pred.get(mu,0)+s**b*Fpoly(k-b,t**(r-b),s,t)
    for mu,v in pred.items():
        if v!=0 and len(mu)==2 and mu[1]>min(k,r): ok=False; print('SUPPORT FAIL',k,r,mu)
print('support <= min(k,r):',ok)
# --- t=0 corollary vs engine at t=0
ok0=True
for k in range(1,5):
  for r in range(0,6):
    s=rnd(); t=Fr(0); m=k+r
    got=e_expand(lambda x: Ek(k,lambda y: esym(y,r),x,s,t),k+r,m)
    mu_,M=min(k,r),max(k,r); pred={}
    def add(a,b,v):
        mu=tuple(sorted([q for q in (a,b) if q>0],reverse=True)); pred[mu]=pred.get(mu,0)+v
    for b in range(mu_): add(b,r+k-b,(1-s)*s**b)
    add(mu_,M,s**mu_)
    for mu in set(got)|set(pred):
        if got.get(mu,0)!=pred.get(mu,0): ok0=False; print('T0 FAIL',k,r,mu,got.get(mu),pred.get(mu))
print('Cor t=0:',ok0)
# --- FPSAC C_{a,b} form agreement (remark)
u=sp.symbols('u')
def pi_a(a,j,s,t):
    S,T=sp.Rational(s.numerator,s.denominator),sp.Rational(t.numerator,t.denominator)
    f=sp.prod([(1+S*u*T**mm)/(1+u*T**mm) for mm in range(a)])
    return Fr(str(sp.series(f,u,0,j+1).removeO().coeff(u,j)))
def br(n,t): return (1-t**n)/(1-t)
def Cab(a,b,s,t):
    if a==0 or b==0: return Fr(1)
    return (-1)**b*br(a+b,t)/br(a,t)*pi_a(a,b,s,t)
okC=True
for k in range(1,5):
  for r in range(0,6):
    s,t=rnd(),rnd(); A={};B={}
    for b in range(k+1):
        mu=tuple(sorted([q for q in (b,r+k-b) if q>0],reverse=True)); A[mu]=A.get(mu,0)+s**b*Fpoly(k-b,t**(r-b),s,t)
    for y in range(min(k,r)+1):
        mu=tuple(sorted([q for q in (y,r+k-y) if q>0],reverse=True)); B[mu]=B.get(mu,0)+s**y*Cab(k-y,r-y,s,t)
    for mu in set(A)|set(B):
        if A.get(mu,0)!=B.get(mu,0): okC=False; print('C-form FAIL',k,r,mu)
print('F-form == C-form:',okC)
# --- k=2 explicit F_2 symbolic
S,T,W=sp.symbols('s t w')
def csym(n,j):
    if j<0 or j>n: return 0
    qq=lambda a,nn: sp.prod([1-a*T**i for i in range(nn)])
    al=lambda jj: 0 if jj<0 else sp.prod([(S-T**i)/(1-T**i) for i in range(1,jj+1)])
    return qq(S,n-j)/qq(T,n-j)*(al(j)-S*T**(n-j)*al(j-1))
for n in range(3):
    print('F_%d ='%n, sp.factor(sp.simplify(sum(csym(n,j)*W**j for j in range(n+1)))))
    for j in range(n+1): print('   c(%d,%d)='%(n,j), sp.factor(csym(n,j)))
