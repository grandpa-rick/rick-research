"""Day 229: closed form of separator J_star(t) and gauge-invariant ratios at n=5 (status: computed).
Gauge: L(lam) -> L(lam) * prod_i f(lam_i) * g(|lam|) * a^{l(lam)}.
Ratio prod L(alpha)^{e_alpha} is invariant iff (i) sum e over each size n = 0, (ii) for each part size k
sum e_alpha m_k(alpha) = 0 (kills f), (iii) sum e_alpha l(alpha) = 0 (kills a; implied by (ii))."""
import sys; sys.path.insert(0,'/home/agent/projects/scripts/day228')
sys.path.insert(0,'/home/agent/projects/scripts/browse_dolega'); sys.path.insert(0,'/home/agent/projects/scripts/day216b')
import sympy as sp
from sep import objs, T   # reruns sep.py's n<=4 table on import
def parts(n,m=None):
    m=m or n
    if n==0: yield (); return
    for k in range(min(n,m),0,-1):
        for r in parts(n-k,k): yield (k,)+r
def check(e):
    sizes={}; ks={}; ell=0
    for a,x in e.items():
        sizes[sum(a)]=sizes.get(sum(a),0)+x; ell+=x*len(a)
        for k in a: ks[k]=ks.get(k,0)+x
    ok=all(v==0 for v in sizes.values()) and all(v==0 for v in ks.values()) and ell==0
    return ok,sizes,ks,ell
def ratio(F,e): return sp.factor(sp.prod([F(a)**x for a,x in e.items()]))
def report(name,e):
    ok,s,k,l=check(e); print(f"\n== {name}: exponents {e}\n   constraints: sizes {s}  part-mults {k}  sum-ell {l}  -> invariant={ok}")
    assert ok
    for o in ['Rick','HTphi','Dol(b)']:
        R=ratio(objs[o],e); print(f"   {o:7s} = {R}   at t=0: {sp.limit(R,T,0)}   at t=1: {sp.limit(R,T,1)}")
report("J (n=4)",{(1,1,1,1):1,(2,2):1,(2,1,1):-2})
# integer kernel at n=5
P=list(parts(5)); M=sp.Matrix([[a.count(k) for a in P] for k in range(1,6)])
ker=M.nullspace(); print("\nn=5 partitions",P,"\nkernel basis:")
for v in ker:
    v=v*sp.ilcm(*[x.q for x in v]); print("  ",{P[i]:int(v[i]) for i in range(len(P)) if v[i]!=0})
report("J5a",{(1,1,1,1,1):1,(2,2,1):1,(2,1,1,1):-2})
report("J5b",{(3,2):1,(2,1,1,1):1,(3,1,1):-1,(2,2,1):-1})
