# Independent re-implementation of the PRINTED statements of longversion.tex §2-3.
from fractions import Fraction as Fr
import itertools, random
random.seed(231)
def rnd(): return Fr(random.randint(2,997),random.randint(2,997))*random.choice([1,-1])
def rndpt(m):
    while True:
        p=[rnd() for _ in range(m)]
        if len(set(p))==m: return p
def prod(L):
    p=Fr(1)
    for a in L: p*=a
    return p
def esym(xs,r):
    if r<0 or r>len(xs): return Fr(0)
    return sum((prod(c) for c in itertools.combinations(xs,r)),Fr(0))
def Ek(k,F,x,s,t):
    """subset formula as printed: sum_{|A|=k} c_A x_A F(x with x_i->s x_i for i in A)"""
    m=len(x); tot=Fr(0)
    for A in itertools.combinations(range(m),k):
        cA=prod((x[i]-t*x[j])/(x[i]-x[j]) for i in A for j in range(m) if j not in A)
        y=[s*x[i] if i in A else x[i] for i in range(m)]
        tot+=cA*prod(x[i] for i in A)*F(y)
    return tot
def partitions(n,maxp=None):
    if maxp is None: maxp=n
    if n==0: yield (); return
    for p in range(min(n,maxp),0,-1):
        for q in partitions(n-p,p): yield (p,)+q
def solve(M,b):
    n=len(M); A=[row[:]+[bb] for row,bb in zip(M,b)]; cols=len(M[0])
    r=0; piv=[]
    for c in range(cols):
        pr=next((i for i in range(r,n) if A[i][c]!=0),None)
        if pr is None: continue
        A[r],A[pr]=A[pr],A[r]
        inv=1/A[r][c]; A[r]=[a*inv for a in A[r]]
        for i in range(n):
            if i!=r and A[i][c]!=0:
                f=A[i][c]; A[i]=[a-f*bb for a,bb in zip(A[i],A[r])]
        piv.append(c); r+=1
    assert r==cols, "singular"
    for i in range(r,n): assert A[i][-1]==0, "inconsistent fit"
    return [A[i][-1] for i in range(cols)]
def e_expand(G,n,m):
    """G: function of point x (len m) homogeneous deg n; return dict mu->coef over partitions mu of n with mu1<=m"""
    mus=[mu for mu in partitions(n) if mu[0]<=m]
    pts=[];b=[]
    while len(pts)<len(mus)+3:
        p=rndpt(m)
        try: v=G(p)
        except ZeroDivisionError: continue
        pts.append(p); b.append(v)
    M=[[prod(esym(p,r) for r in mu) for mu in mus] for p in pts]
    sol=solve(M,b)
    return dict(zip(mus,sol))
