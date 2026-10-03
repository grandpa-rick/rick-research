"""Day 219 addendum: c_{lam mu} = s^{n(mu)} (1-s)^{v} R_{lam mu}; test sign of R. Grade: computed."""
import sys,pickle,sympy as sp
sys.path.insert(0,'/home/agent/projects/scripts/day214')
from ek_subset_engine import transpose, dominates
from sympy.utilities.iterables import partitions
s,t,u=sp.symbols('s t u')
mats=pickle.load(open('/home/agent/projects/scripts/day216/mats_N5.pkl','rb'))
nn=lambda m:sum(i*x for i,x in enumerate(m))
def apply(k,vec):
    res={}
    for mu,c in vec.items():
        for nu,d in mats[(k,sum(mu))][mu].items(): res[nu]=res.get(nu,0)+c*d
    return {a:sp.cancel(b) for a,b in res.items() if sp.cancel(b)!=0}
def sg(p):
    cs=sp.Poly(sp.expand(p),s,t,u).coeffs()
    return 1 if all(x>0 for x in cs) else (-1 if all(x<0 for x in cs) else 0)
for n in range(2,6):
    for p in partitions(n):
        lam=tuple(sorted(sum(([k]*v for k,v in p.items()),[]),reverse=True))
        vec={():sp.Integer(1)}
        for k in reversed(lam): vec=apply(k,vec)
        for mu,cc in vec.items():
            if mu==lam: continue
            c=sp.factor(cc)  # = c_{lam mu}/s^{n(mu)}
            v=0
            while sp.cancel(c.subs(s,1))==0: c=sp.cancel(c/(1-s)); v+=1
            R=sp.factor(c); a,b=sg(R),sg(R.subs(s,1-u))
            # predicted v and sign
            print(lam,mu,'v=',v,'ell diff',len(lam)-len(mu),'sign(s,t)=',a,'sign(s=1-u)=',b, '' if a==1 and b==1 else 'R='+str(R))
