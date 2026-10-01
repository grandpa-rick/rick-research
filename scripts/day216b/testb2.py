import sys, pickle, sympy as sp
sys.path.insert(0, '/home/agent/projects/scripts/day214')
from ek_subset_engine import transpose, nstat, parts
s,t=sp.symbols('s t')
mats=pickle.load(open('/home/agent/projects/scripts/day216/mats_N5.pkl','rb'))
def mult(p,i): return sum(1 for a in p if a==i)
def phi(nu,mu,k):
    # horizontal strip nu/mu? return phi_{nu/mu}(s) (Macdonald III (5.8')) else 0
    L=len(nu); mu=list(mu)+[0]*(L-len(mu))
    if len(mu)>L: return 0
    if sum(nu)-sum(mu)!=k: return 0
    for i in range(L):
        if not (nu[i]>=mu[i] and (i+1>=L or mu[i]>=nu[i+1])): return 0
    th=transpose(tuple(nu)); thm=transpose(tuple(a for a in mu if a>0))
    tp=lambda p,j: p[j-1] if j-1<len(p) else 0
    r=1
    for i in range(1,max(nu)+2):
        a=tp(th,i)-tp(thm,i); b=tp(th,i+1)-tp(thm,i+1)
        if a==0 and b==1: r*= (1-s**mult(mu,i))
    return r
bad=0;tot=0
for (k,n),cols in mats.items():
    for mu,col in cols.items():
        nus=set(col)|set(p for p in parts(n+k))
        for nu in parts(n+k):
            c=sp.expand(sp.cancel(col.get(nu,0)))
            D=nstat(transpose(nu))-nstat(transpose(mu))-sp.binomial(k,2)
            P=sp.Poly(c,t) if c!=0 else None
            deg=P.degree() if P else -10**9
            top=sp.expand(c.coeff(t,D)) if c!=0 else 0
            pred=sp.expand(phi(nu,mu,k))
            ok = deg<=D and sp.expand(top-pred)==0
            tot+=1
            if not ok:
                bad+=1; print('BAD',k,mu,nu,'D',D,'deg',deg,'top',sp.factor(top),'pred',pred,'c',sp.factor(c))
print('tot',tot,'bad',bad)
