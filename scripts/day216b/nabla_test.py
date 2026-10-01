import pickle, sys
from symf import *
sys.path.insert(0,'/home/agent/projects/scripts/day214')
from ek_subset_engine import nstat
mats=pickle.load(open('/home/agent/projects/scripts/day216/mats_N5.pkl','rb'))
def apply(k,vec):
    res={}
    for mu,c in vec.items():
        for nu,d in mats[(k,sum(mu))][mu].items(): res[nu]=res.get(nu,0)+c*d
    return res
def estar(lam):  # in b-basis
    v={():sp.Integer(1)}
    for k in reversed(lam): v=apply(k,v)
    return v
def b_to_p(v):
    r={}
    for mu,c in v.items(): r=add(r,scal(prod([e(p) for p in mu]),c*s**nstat(mu)))
    return r
N=int(sys.argv[1]); qv=sp.sympify(sys.argv[2]); tv=sp.sympify(sys.argv[3])
def nabla(f,n):
    P=list(parts(n)); basis={mu:Htilde(mu) for mu in P}
    co=to_basis(f,basis); r={}
    for mu,c in co.items(): r=add(r,scal(basis[mu],c*t**nstat(mu)*q**nstat(transpose(mu))))
    return {k: sp.together(v.subs({q:qv,t:tv},simultaneous=True)) for k,v in r.items()}
phi=lambda f: pleth(f, lambda k: (-1)**(k-1)/(1-t**k))
phiinv=lambda f: pleth(f, lambda k: (-1)**(k-1)*(1-t**k))
for n in range(1,N+1):
    for lam in parts(n):
        lhs=scal(b_to_p(estar(lam)), t**nstat(transpose(lam)))
        f=phi(prod([e(p) for p in lam]))
        # nabla with generic q,t then substitute q->qv,t->tv: but phi uses t; do nabla in symbols then subst
        rhs=phiinv({k:v for k,v in nabla(f,n).items()})
        # phi/phiinv use symbol t; fine if tv==t
        d={k: sp.simplify(lhs.get(k,0)-rhs.get(k,0)) for k in set(lhs)|set(rhs)}
        print(n,lam,all(v==0 for v in d.values()),flush=True)
