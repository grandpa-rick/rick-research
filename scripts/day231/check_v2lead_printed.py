from lv_engine import *
from check_DS_printed import estar, interp
from check_v2_printed import Phi_formula, psum, br
import itertools
def L(a,b,t): return (1-t**(a+b))*(t**(a*b)-1)/((1-t**a)*(1-t**b))
def key(*ps): return tuple(sorted([p for p in ps if p>0],reverse=True))
def M(k,r,t):
    if k<r: k,r=r,k
    out={}
    def add(kk,v): out[kk]=out.get(kk,0)+v
    if r>0: add(key(k,r),Fr(r))
    for j in range(1,r+1): add(key(k+j,r-j),L(k-r+j,j,t))
    return out
def mul(f,g):
    out={}
    for a,u in f.items():
        for b,v in g.items():
            kk=tuple(sorted(a+b,reverse=True)); out[kk]=out.get(kk,0)+u*v
    return out
def Da(a,f,t):
    out={}
    for mon,c in f.items():
        for i,p in enumerate(mon):
            rest={tuple(mon[:i]+mon[i+1:]):Fr(1)}
            for kk,v in mul(rest,M(a,p,t)).items(): out[kk]=out.get(kk,0)+c*v
    return out
def Xi(a,r,q,t): return (-1)**(r+q)*br(a+r+q,t)/br(a,t)*br(a,t**r)*br(a,t**q)
def lead_formula(a,b,c,x,y,t):
    n=x+y; m=2 if x==y else 1
    g=lambda z: psum(z,b)*psum(z,c)
    U=((-1)**n*Phi_formula(a,g,b+c,x,y,t)-Xi(a,b,c,t))/m
    tot=(-1)**(b+c)*U
    for r in range(1,b):
        if sorted([b-r,a+r+c])==sorted([x,y]): tot+=(-1)**(r+c)*Xi(a,r,c,t)
    for q in range(1,c):
        if sorted([c-q,a+b+q])==sorted([x,y]): tot+=(-1)**(b+q)*Xi(a,b,q,t)
    tot+=Da(a,M(b,c,t),t).get(key(x,y),Fr(0))
    return tot
ok=True
for lam,mu in [((2,2,2),(5,1)),((2,2,2),(3,3)),((3,3,1),(5,2)),((3,2,2),(6,1))]:
    t=Fr(3,5); n=sum(lam)
    hs=[Fr(i+1,i+3)*(-1)**i for i in range(10)]
    D=[e_expand(lambda xx: estar(lam,xx,1+h,t),n,n) for h in hs]
    cc=interp(hs,[d.get(mu,Fr(0)) for d in D])
    for (a,b,c) in set(itertools.permutations(lam)):
        f=lead_formula(a,b,c,mu[0],mu[1],t)
        if f!=cc[2] or cc[0]!=0 or cc[1]!=0: ok=False; print('V2 FAIL',lam,mu,(a,b,c),f,cc[:3])
print('thm:v2 vs engine (4 pairs, all orderings):',ok)
ok2=True
P1=lambda t: 2*t**13+3*t**12+3*t**11+6*t**10+6*t**9+6*t**8+9*t**7+6*t**6+3*t**5+9*t**4+6*t**3+3*t+4
P2=lambda t: (t+1)*(t**2+1)*(2*t**8+t**7+t**6+3*t**4+t**3+t**2-t+2)
for j in range(20):
    t=Fr(j+2,j+7)*(-1)**j
    for (a,b,c) in [(3,3,3)]:
        if lead_formula(a,b,c,7,2,t)!=P1(t): ok2=False; print('ex v2 (333) fail',t)
    for (a,b,c) in set(itertools.permutations((4,4,2))):
        if lead_formula(a,b,c,7,3,t)!=P2(t): ok2=False; print('ex v2 (442) fail',t,(a,b,c))
print('ex:v2 printed polynomials = thm:v2 formula (20 t-points, all orderings):',ok2)
