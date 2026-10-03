"""Day 219: positivity sweep for e*_lam = e_{l1}*e_{l2}*... (Hikita star, from day216 mats_N5.pkl).
Expand e*_lam in bases e, b=s^{n(mu)}e, Schur, HL P(t), Q'(t), HL P(1/t), Q'(1/t), m, p, forgotten f;
test single-sign (coefficientwise) under substitutions applied to the coefficient polynomials.
Grade: computed."""
import sys, pickle, itertools, time, sympy as sp
from collections import Counter
sys.path.insert(0,'/home/agent/projects/scripts/day214')
from ek_subset_engine import transpose, dominates
from sympy.utilities.iterables import partitions
s,t,u,v=sp.symbols('s t u v')
N=int(sys.argv[1]) if len(sys.argv)>1 else 5
mats=pickle.load(open('/home/agent/projects/scripts/day216/mats_N5.pkl','rb'))
def nn(m): return sum(i*x for i,x in enumerate(m))
def apply(k,vec):
    res={}
    for mu,c in vec.items():
        for nu,d in mats[(k,sum(mu))][mu].items(): res[nu]=res.get(nu,0)+c*d
    return {a:sp.cancel(b) for a,b in res.items() if sp.cancel(b)!=0}
def plist(n): return sorted([tuple(sorted(sum(([k]*v for k,v in p.items()),[]),reverse=True)) for p in partitions(n)])
def m_of(expr,xs):
    P=sp.Poly(sp.expand(expr),*xs); d={}
    for mon,c in P.terms():
        if list(mon)==sorted(mon,reverse=True): d[tuple(a for a in mon if a>0)]=c
    return d
def zee(l):
    r=1
    for k,c in Counter(l).items(): r*=k**c*sp.factorial(c)
    return r
SUBS={'(s,t)':lambda c:c,
      '(s,1/t)':lambda c:c.subs(t,1/t),
      's=1+u':lambda c:c.subs(s,1+u),
      't=1+v':lambda c:c.subs(t,1+v),
      's=1-u':lambda c:c.subs(s,1-u),
      # extras beyond the requested five
      '(1/s,t)':lambda c:c.subs(s,1/s),
      '(1/s,1/t)':lambda c:c.subs({s:1/s,t:1/t},simultaneous=True),
      '(-s,t)':lambda c:c.subs(s,-s),
      '(s,-t)':lambda c:c.subs(t,-t),
      '(-s,-t)':lambda c:c.subs({s:-s,t:-t},simultaneous=True),
      's=1-u,1/t':lambda c:c.subs({s:1-u,t:1/t},simultaneous=True),
      's=1-u,t=1+v':lambda c:c.subs({s:1-u,t:1+v},simultaneous=True),
      's=1+u,t=1+v':lambda c:c.subs({s:1+u,t:1+v},simultaneous=True),
      's=1/(1-u)':lambda c:c.subs(s,1/(1-u))}
def sign_of(c):
    """return +1/-1 if c (rational fn) = monomial-clearable single-sign ratio, 0 if mixed. c!=0"""
    c=sp.cancel(sp.together(c)); nu,de=sp.fraction(c)
    sg=1
    for p in (nu,de):
        cs=sp.Poly(sp.expand(p),s,t,u,v).coeffs()
        if all(x>0 for x in cs): pass
        elif all(x<0 for x in cs): sg=-sg
        else: return 0
    return sg
results={}  # (basis,sub) -> dict(status, first counterexample, signs)
t0=time.time()
for n in range(1,N+1):
    xs=sp.symbols(f'x1:{n+1}'); Ps=plist(n); idx={l:i for i,l in enumerate(Ps)}; L=len(Ps)
    esym=lambda r: sum(sp.prod(c) for c in itertools.combinations(xs,r)) if r<=n else 0
    hsym=lambda r: sum(sp.prod(c) for c in itertools.combinations_with_replacement(xs,r)) if r>=0 else 0
    M=lambda dd: sp.Matrix([[dd[l].get(m,0) for m in Ps] for l in Ps])
    Em=M({l:m_of(sp.prod([esym(r) for r in l]),xs) for l in Ps})
    Hm=M({l:m_of(sp.prod([hsym(r) for r in l]),xs) for l in Ps})
    Pm=M({l:m_of(sp.prod([sum(x**r for x in xs) for r in l]),xs) for l in Ps})
    Sm=M({l:m_of(sp.Matrix(len(l),len(l),lambda i,j:hsym(l[i]-i+j)).det(),xs) for l in Ps})
    Pinv=Pm.inv()
    def hall(f,g,tt):  # f,g row vectors in m-coords; tt=None -> ordinary Hall
        fp=f*Pinv; gp=g*Pinv
        return sum(fp[i]*gp[i]*zee(l)*(1 if tt is None else sp.prod([1/(1-tt**r) for r in l])) for i,l in enumerate(Ps))
    def HLP(tt):
        rows={}
        for lam in Ps:
            f=sp.zeros(1,L); f[idx[lam]]=1
            for mu in Ps:
                if mu==lam: break
                if dominates(lam,mu):
                    c=sp.cancel(hall(sp.Matrix([[1 if k==lam else 0 for k in Ps]]),rows[mu],tt)/hall(rows[mu],rows[mu],tt))
                    f=(f-c*rows[mu]).applyfunc(sp.cancel)
            rows[lam]=f
        return sp.Matrix.vstack(*[rows[l] for l in Ps])
    # ordinary Hall Gram in m-coords: <f,g> = f G g^T ; Q'_mu dual to P_mu  => coeff of Q'_mu in f = <f,P_mu>
    G=(Pinv*sp.diag(*[zee(l) for l in Ps])*Pinv.T)
    bases={}
    # coefficient extractor: given f (m-coords row), return row of coeffs
    for name,Bm in [('e',Em),('schur',Sm),('m',sp.eye(L)),('p',Pm)]:
        Bi=Bm.inv(); bases[name]=(lambda Bi: lambda f:(f*Bi))(Bi)
    bases['forgotten']=None  # handled via omega
    for tname,tt in [('t',t),('1/t',1/t)]:
        HP=HLP(tt); HPi=HP.inv().applyfunc(sp.cancel)
        bases['HL_P('+tname+')']=(lambda HPi: lambda f:(f*HPi))(HPi)
        bases["Q'("+tname+')']=(lambda HP: lambda f:(f*G*HP.T))(HP)
    print(f'n={n} bases built {time.time()-t0:.1f}s',flush=True)
    for lam in Ps:
        vec={():sp.Integer(1)}
        for k in reversed(lam): vec=apply(k,vec)
        c={mu:sp.cancel(cc*s**nn(mu)) for mu,cc in vec.items()}   # e*_lam = sum c_mu e_mu
        cvec=sp.Matrix([[c.get(mu,0) for mu in Ps]])
        fm=(cvec*Em).applyfunc(sp.expand); fwm=(cvec*Hm).applyfunc(sp.expand)  # m-coords of f and omega f
        if n<=4: print('  e*',lam,'=',{mu:sp.factor(x) for mu,x in c.items()},flush=True)
        exps={'e':list(cvec),'b':[sp.cancel(c.get(mu,0)/s**nn(mu)) for mu in Ps]}
        for name,fn in bases.items():
            if name=='forgotten': exps[name]=list(fwm)  # [f_mu] f = [m_mu] omega f
            else: exps[name]=[sp.cancel(x) for x in fn(fm)]
        for name,co in exps.items():
            for sn,sb in SUBS.items():
                R=results.setdefault((name,sn),{'fail':None,'signs':{}})
                for mu,x in zip(Ps,co):
                    if x==0: continue
                    sg=sign_of(sb(x))
                    if sg==0:
                        if R['fail'] is None: R['fail']=(lam,mu,sp.factor(x))
                    else: R['signs'][(lam,mu)]=sg
    print(f'n={n} done {time.time()-t0:.1f}s',flush=True)
# sign formulas
cands={'+1':lambda l,m:0,'n(mu)-n(lam)':lambda l,m:nn(m)-nn(l),"n(mu')-n(lam')":lambda l,m:nn(transpose(m))-nn(transpose(l)),
       'l(mu)-l(lam)':lambda l,m:len(m)-len(l),'|mu|-l(mu)':lambda l,m:sum(m)-len(m),"n(mu)-n(lam')":lambda l,m:nn(m)-nn(transpose(l)),
       "n(mu')-n(lam)":lambda l,m:nn(transpose(m))-nn(l),'l(mu)-l(lam\')':lambda l,m:len(m)-len(transpose(l))}
print('\n=== TABLE (N=%d) ==='%N)
for (name,sn),R in results.items():
    if R['fail'] is None:
        fs=[k for k,f in cands.items() if all(sg==(-1)**f(l,m) for (l,m),sg in R['signs'].items())]
        print(f'PASS  {name:10s} {sn:12s} eps formula: {fs if fs else "none of candidates"}  signs={ {k:v for k,v in R["signs"].items() if v<0} if not fs else ""}')
    else:
        print(f'fail  {name:10s} {sn:12s} first: lam={R["fail"][0]} mu={R["fail"][1]} coeff={R["fail"][2]}')
