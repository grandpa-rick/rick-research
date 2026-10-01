import pickle, sympy as sp, sys
sys.path.insert(0,'/home/agent/projects/scripts/day214')
from ek_subset_engine import parts, transpose
s,t=sp.symbols('s t')
PSI=pickle.load(open('/home/agent/projects/scripts/day216/psi_N5.pkl','rb'))
# omega on m-basis: build via sympy in n variables: m -> e-basis -> h
from sympy.combinatorics.partitions import IntegerPartition
import itertools
def msym(kap,xs):
    kap=list(kap)+[0]*(len(xs)-len(kap)); return sum(sp.prod([x**a for x,a in zip(xs,p)]) for p in set(itertools.permutations(kap)))
def ekx(r,xs): return sum(sp.prod(c) for c in itertools.combinations(xs,r))
def hkx(r,xs): return sum(sp.prod(c) for c in itertools.combinations_with_replacement(xs,r))
def omega(f,xs,n):
    # express f in e-basis via leading monomials then replace e by h
    P=sp.Poly(sp.expand(f),*xs); out=0
    while not P.is_zero:
        mon,c=max(P.terms(),key=lambda mc:mc[0])
        kap=tuple(a for a in mon if a>0); nu=transpose(kap)
        out+=c.as_expr()*sp.prod([hkx(p,xs) for p in nu])
        P=P-sp.Poly(c*sp.prod([ekx(p,xs) for p in nu]),*xs)
    return sp.expand(out)
N=int(sys.argv[1])
for n in range(1,N+1):
    xs=sp.symbols(f'x1:{n+1}')
    for mu in parts(n):
        f=sum(c*msym(k,xs) for k,c in PSI[mu].items())
        g=sum(c*msym(k,xs) for k,c in PSI[transpose(mu)].items())
        g2=sp.expand(sp.together(g.subs({s:1/t,t:1/s},simultaneous=True)))
        of=omega(sp.together(f)*1,xs,n) if False else None
        fn,fd=sp.fraction(sp.together(f)); of=sp.expand(omega(sp.expand(fn),xs,n))/fd
        # ratio test via leading monomial
        Pf=sp.Poly(sp.expand(sp.numer(sp.together(of))),*xs); Pg=sp.Poly(sp.expand(sp.numer(sp.together(g2))),*xs)
        mon=max(Pf.monoms()); r=sp.cancel(sp.together(of).subs({}) )
        ratio=sp.cancel((Pf.coeff_monomial(mon)/sp.denom(sp.together(of)))/(Pg.coeff_monomial(mon)/sp.denom(sp.together(g2))))
        diff=sp.cancel(sp.together(of - ratio*g2))
        print(n,mu,'ratio',sp.factor(ratio),'ok',diff==0,flush=True)
