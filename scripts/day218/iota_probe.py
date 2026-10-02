"""Day 218 probe: iota = Psi o beta (beta: (s,t)->(1/s,1/t) on e-coeffs). Test iota^2=id,
triangularity on curves t=s^a, Lusztig canonical basis. Reuses scripts/day216/mats_N5.pkl
(E_k matrices in b-basis, b_nu = s^{n(nu)} e_nu)."""
import sys, pickle, sympy as sp
sys.path.insert(0,'/home/agent/projects/scripts/day214')
from ek_subset_engine import transpose, parts, dominates
s,t,v=sp.symbols('s t v')
mats=pickle.load(open('/home/agent/projects/scripts/day216/mats_N5.pkl','rb'))
NMAX=int(sys.argv[1]) if len(sys.argv)>1 else 4
def nn(m): return sum(i*x for i,x in enumerate(m))
def apply(k,vec):
    res={}
    for mu,c in vec.items():
        for nu,d in mats[(k,sum(mu))][mu].items(): res[nu]=res.get(nu,0)+c*d
    return {a:sp.cancel(b) for a,b in res.items() if sp.cancel(b)!=0}
def bar(x): return sp.cancel(x.subs({s:1/s,t:1/t},simultaneous=True))
def barv(x): return sp.expand(x.subs(v,1/v))
def Psi_inv_matrix(n):
    P=list(parts(n))
    A=sp.zeros(len(P))
    for j,mu in enumerate(P):
        vec={():sp.Integer(1)}
        for k in reversed(mu): vec=apply(k,vec)
        for nu,c in vec.items():
            i=P.index(nu); A[i,j]=sp.cancel(t**nn(transpose(mu))*c*s**nn(nu))
    return P,A
# Schur <-> e transition (Jacobi-Trudi dual: s_lam = det e_{lam'_i - i + j})
def schur_in_e(lam,P):
    lt=transpose(lam); L=len(lt); E=sp.symbols('E0:%d'%(sum(lam)+1))
    M=sp.Matrix(L,L,lambda i,j: (E[lt[i]-i+j] if lt[i]-i+j>=0 else 0) if lt[i]-i+j<=sum(lam) else 0)
    M=M.subs(E[0],1); d=sp.expand(M.det()); res={}
    for term in sp.Add.make_args(d):
        c,fs=term.as_coeff_mul(); key=[]
        for f in fs:
            b,ex=f.as_base_exp(); key+= [int(str(b)[1:])]*int(ex)
        key=tuple(sorted(key,reverse=True)); res[key]=res.get(key,0)+c
    return res
def out(*a):
    print(*a,flush=True)
def lpoly_ok(x):
    x=sp.expand(x)
    try: sp.Poly(x*v**200,v); return True
    except Exception: return False
RES={}
for n in range(1,NMAX+1):
    if n>=5: out('n=5 inversion...')
    P,A=Psi_inv_matrix(n)
    M=A.inv().applyfunc(sp.cancel)      # matrix of Psi in e-basis
    Mb=M.applyfunc(bar)
    I2=(M*Mb).applyfunc(sp.cancel)
    out(f'==== n={n} partitions {P}')
    out(' iota^2=id (Psi*bar(Psi)=I):', I2==sp.eye(len(P)))
    out(' diag of Psi (e-basis):',[sp.factor(M[i,i]) for i in range(len(P))])
    # support check generic: Psi(e_mu) supported on nu dominating mu?
    sup=all(M[i,j]==0 or dominates(P[i],P[j]) for i in range(len(P)) for j in range(len(P)))
    out(' Psi(e_mu) supported on {nu >= mu} (dominance up-set), generic s,t:',sup)
    RES[n]=(P,M)
pickle.dump(RES,open('/home/agent/projects/scripts/day218/psi_e.pkl','wb'))

def curve_analysis(a, n, P, M, label, basis='e'):
    # s=v^2, t=v^(2a)
    sub={s:v**2, t:v**(2*a)}
    Mc=M.applyfunc(lambda x: sp.cancel(x.subs(sub,simultaneous=True)))
    m=len(P)
    if basis=='schur':
        # change of basis: S[e-index, schur-index]
        S=sp.zeros(m)
        for j,lam in enumerate(P):
            for k,c in schur_in_e(lam,P).items(): S[P.index(k),j]=c
        # iota(s_lam) = Psi(s_lam) since s_lam has integer coeffs in e-basis
        Mc=(S.inv()*Mc*S).applyfunc(sp.cancel)
    # normalization: d_mu^2 = diag ; d_mu = monomial sqrt
    d=[]
    for i in range(m):
        x=sp.factor(Mc[i,i]); ex,c=sp.Poly(x*v**200,v).terms()[0]; ex=ex[0]-200
        assert len(sp.Poly(x*v**200,v).terms())==1 and c==1 and ex%2==0, x
        d.append(v**(ex//2))
    # iota(tilde b_mu) = bar(d_mu) * sum_nu M[nu,mu] b_nu = sum_nu bar(d_mu) M[nu,mu]/d_nu tilde b_nu
    R=sp.zeros(m)
    for i in range(m):
        for j in range(m):
            R[i,j]=sp.factor(sp.cancel(d[j].subs(v,1/v)*Mc[i,j]/d[i]))
    out(f'--- {label} n={n} basis={basis}: diag of Psi =',[sp.factor(Mc[i,i]) for i in range(m)],' normalizer d =',d)
    unit=all(sp.simplify(R[i,i]-1)==0 for i in range(m))
    dom=all(R[i,j]==0 or dominates(P[i],P[j]) for i in range(m) for j in range(m))
    domdown=all(R[i,j]==0 or dominates(P[j],P[i]) for i in range(m) for j in range(m))
    out(f'   support in dominance DOWN-set={domdown}')
    # triangular wrt some linear ext? test lex order (P is reverse-lex decreasing)
    up_lex=all(R[i,j]==0 or i<=j for i in range(m) for j in range(m))
    lo_lex=all(R[i,j]==0 or i>=j for i in range(m) for j in range(m))
    laur=all(lpoly_ok(R[i,j]) for i in range(m) for j in range(m))
    out(f'   unit diag={unit}; support in dominance up-set={dom}; lex-triangular(up/low)={up_lex}/{lo_lex}; Laurent in v={laur}')
    for j in range(m):
        out('   iota(~',P[j],') =',{P[i]:R[i,j] for i in range(m) if R[i,j]!=0})
    return R,unit,dom,laur

def lusztig(P,R,neg=True):
    """C_mu = ~mu + sum_{lam>mu} p_{lam,mu} ~lam, p in v^{-1}Z[v^{-1}] (neg) or vZ[v] (not neg).
    R[i,j]: iota(~P[j]) = sum_i R[i,j] ~P[i]. 'Above' = rows i with R support; use order of index:
    we process lam in an order compatible with support."""
    m=len(P)
    # P is in decreasing lex; up-set of mu has smaller indices. Process lam = indices j-1,...,0
    C={}
    for j in range(m):
        p={j:sp.Integer(1)}
        for i in range(j-1,-1,-1):
            rhs=sp.expand(sum(barv(p[k])*R[i,k] for k in p if k!=i))  # p_i - bar p_i = rhs
            # need rhs anti-invariant
            anti=sp.expand(rhs+barv(rhs))==0
            if not anti: return None,('not anti-invariant',P[i],P[j],rhs)
            pol=sp.Poly(sp.expand(rhs*v**100),v)
            val=0
            for (e,),c in pol.terms():
                e-=100
                if (neg and e<0) or ((not neg) and e>0): val+=c*v**e
            if val!=0: p[i]=val
        C[P[j]]={P[i]:p[i] for i in p}
    return C,None

def check_iota_inv(P,R,C):
    m=len(P); idx={mu:i for i,mu in enumerate(P)}
    for mu,cm in C.items():
        img={}
        for lam,c in cm.items():
            k=idx[lam]
            for i in range(m):
                if R[i,k]!=0: img[P[i]]=sp.expand(img.get(P[i],0)+barv(c)*R[i,k])
        if any(sp.expand(img.get(l,0)-cm.get(l,0))!=0 for l in set(img)|set(cm)): return False
    return True

if __name__=='__main__':
    curves=[(1,'t=s'),(2,'t=s^2'),(-1,'t=1/s'),(-2,'t=s^-2'),(0,'t=1')]
    for a,label in curves:
        for n in range(2,NMAX+1):
            P,M=RES[n]
            for basis in ['e','schur']:
                R,unit,dom,laur=curve_analysis(a,n,P,M,label,basis)
                PP,RR=P,R
                if not dom:   # lower-triangular: reverse the order so 'above' = smaller index
                    m=len(P); PP=P[::-1]; RR=sp.Matrix(m,m,lambda i,j:R[m-1-i,m-1-j])
                for neg in [True,False]:
                    C,err=lusztig(PP,RR,neg)
                    tag='v^-1 Z[v^-1]' if neg else 'v Z[v]'
                    if C is None: out(f'   Lusztig ({tag}) FAILED:',err); continue
                    out(f'   Lusztig canonical basis ({tag}), iota-invariant check:',check_iota_inv(PP,RR,C))
                    for mu in P:
                        out('     C',mu,'=',{l:sp.factor(c) for l,c in C[mu].items()})

# ---------------- Part 2: sign/positivity analysis + star structure constants in C basis -------------
def signinfo(C,P):
    """per-coefficient sign: +1,-1, or 0 (mixed); then test for a sign twist eps making all >=0."""
    mixed=[]; sg={}
    for mu,cm in C.items():
        for lam,c in cm.items():
            if lam==mu: continue
            cs=[co for co in sp.Poly(sp.expand(c*v**100),v).coeffs()]
            if all(x>0 for x in cs): sg[(lam,mu)]=1
            elif all(x<0 for x in cs): sg[(lam,mu)]=-1
            else: mixed.append((lam,mu,sp.expand(c)))
    # 2-colouring
    eps={}; ok=True
    adj={}
    for (a,b),x in sg.items(): adj.setdefault(a,[]).append((b,x)); adj.setdefault(b,[]).append((a,x))
    for st in P:
        if st in eps: continue
        eps[st]=1; stack=[st]
        while stack:
            a=stack.pop()
            for b,x in adj.get(a,[]):
                want=eps[a]*x
                if b in eps:
                    if eps[b]!=want: ok=False
                else: eps[b]=want; stack.append(b)
    return mixed, ok

def star_constants(a,NN,neg):
    """C-basis (e-based canonical basis on t=s^a) structure constants of E_k: C_mu -> sum c C_nu."""
    sub={s:v**2,t:v**(2*a)}
    Cb={}
    for n in range(1,NN+1):
        P,M=RES[n]
        R,_,_,_=curve_analysis(a,n,P,M,f'(a={a}) aux','e') if False else (None,0,0,0)
    return Cb

if __name__=='__main__' and len(sys.argv)>2:
    a=int(sys.argv[2]); NN=NMAX
    sub={s:v**2,t:v**(2*a)}
    import io, contextlib
    CB={}; DD={}
    for n in range(1,NN+1):
        P,M=RES[n]
        with contextlib.redirect_stdout(io.StringIO()):
            R,_,_,_=curve_analysis(a,n,P,M,'aux','e')
        Mc=M.applyfunc(lambda x: sp.cancel(x.subs(sub,simultaneous=True)))
        d=[]
        for i in range(len(P)):
            ex,c=sp.Poly(Mc[i,i]*v**200,v).terms()[0]; d.append(v**((ex[0]-200)//2))
        for neg in [True,False]:
            C,err=lusztig(P,R,neg)
            if n>=2:
                mixed,ok=signinfo(C,P)
                out(f'[a={a} n={n} {"v^-1" if neg else "v"}] mixed-sign coefficients:',mixed,' | consistent sign twist exists:',ok)
            # C in e-basis: C_mu = sum p ~lam = sum p d_lam e_lam ; b_lam = s^{n(lam)} e_lam
            CB[(n,neg)]=(P,{mu:{lam:sp.expand(c*d[P.index(lam)]) for lam,c in C[mu].items()} for mu in P})
    # E_k action on e-basis at curve: E_k(e_lam) = E_k(s^{-n(lam)} b_lam)
    def Ek_e(k,vec):
        res={}
        for lam,c in vec.items():
            m=sum(lam)
            src=mats[(k,m)][lam] if m>0 else {(k,) if False else ():None}
            if m==0:
                # E_k(1)=e_k
                res[(k,)]=res.get((k,),0)+c; continue
            for nu,dd in mats[(k,m)][lam].items():
                res[nu]=res.get(nu,0)+c*sp.cancel((dd*s**(-sum(i*x for i,x in enumerate(lam)))*s**(sum(i*x for i,x in enumerate(nu)))).subs(sub,simultaneous=True))
        return res
    # wait: mats gives E_k(b_lam)=sum dd b_nu ; b_nu = s^{n(nu)} e_nu, so E_k(e_lam)= s^{-n(lam)} sum dd s^{n(nu)} e_nu  (as coded)
    for neg in [True,False]:
        out(f'==== star structure constants, a={a}, basis C ({"v^-1" if neg else "v"}):  E_k C_mu = e_k * C_mu expanded in C')
        for n in range(1,NN):
            Pn,Cn=CB[(n,neg)]
            for k in range(1,NN-n+1):
                Pm,Cm=CB[(n+k,neg)]
                # e_k itself vs C_(k): e_k = ~(k) * d^-1
                Mmat=sp.Matrix([[Cm[mu].get(lam,0) for mu in Pm] for lam in Pm])  # cols: C_mu in e-basis
                for mu in Pn:
                    img=Ek_e(k,Cn[mu]); vec=sp.Matrix([sp.cancel(img.get(lam,0)) for lam in Pm])
                    sol=Mmat.LUsolve(vec).applyfunc(lambda x: sp.factor(sp.cancel(x)))
                    out(f'  e_{k} * C{mu} =',{Pm[i]:sol[i] for i in range(len(Pm)) if sol[i]!=0})
