"""Day 219: edge-regularity check for the e <-> P transition used by Theorems H (via N), H', DS-from-(N).
P_nu = P_nu(x; q=s, T=tau), tau = 1/t (the normalisation of Day 216b/218).
Independent instrument: Gram-Schmidt w.r.t. <p_l,p_m> = delta z_l prod (1-q^li)/(1-T^li), in m-basis,
order = reverse-lex (a linear extension of dominance).  B[nu][mu] = [e_mu] P_nu, A = B^{-1}.
Checks for all nu |- n <= N:
 (R0) every entry of A,B is regular at s=0 (denominator(s=0) != 0 in Q(tau))
 (R1) every entry of A,B is regular at tau=0 (denominator(tau=0) != 0 in Q(s))  [t -> infinity edge, H']
 (U)  support B_{nu mu}!=0 => mu >= nu' ; B_{nu nu'} = 1 ; A_{lam nu}!=0 => nu <= lam' ; A_{lam lam'} = 1
 (HL) B(s=0) = e-expansion of HL P_nu(x;tau) (independent Gram-Schmidt with q=0 inner product)
 (QW) B(tau=0) = e-expansion of q-Whittaker P_nu(x;s,0) (independent Gram-Schmidt with T=0 inner product)
 (NZ) A_{lam mu'}(s=0) != 0 for all mu >= lam  (the d != 0 input for DS); A_{lam mu'}(tau=0) != 0 likewise
"""
import sys, itertools, sympy as sp
from collections import Counter
q,T=sp.symbols('s tau')
FAST='fast' in sys.argv  # specialise: s-edge checks at tau=3/7, tau-edge checks at s=2/5
if FAST: sys.argv.remove('fast')
N=int(sys.argv[1]) if len(sys.argv)>1 else 4
def plist(n):
    out=[]
    def rec(n,mx,cur):
        if n==0: out.append(tuple(cur)); return
        for k in range(min(n,mx),0,-1): rec(n-k,k,cur+[k])
    rec(n,n,[]); return sorted(out)  # increasing lex = linear extension of dominance
def conj(l): return tuple(sum(1 for x in l if x>i) for i in range(l[0])) if l else ()
def dom(a,b):  # a >= b
    sa=sb=0
    for i in range(max(len(a),len(b))):
        sa+=a[i] if i<len(a) else 0; sb+=b[i] if i<len(b) else 0
        if sa<sb: return False
    return True
def z(l):
    r=1
    for k,v in Counter(l).items(): r*=k**v*sp.factorial(v)
    return r
def m_coeffs(expr,xs,parts):
    P=sp.Poly(sp.expand(expr),*xs); d={p:0 for p in parts}
    for mon,c in P.terms():
        if list(mon)==sorted(mon,reverse=True):
            d[tuple(a for a in mon if a>0)]=c
    return [d[p] for p in parts]
def run(n):
    xs=sp.symbols('x1:%d'%(n+1)); parts=plist(n); k=len(parts)
    pw=lambda r: sum(x**r for x in xs)
    el=lambda r: sum(sp.prod(c) for c in itertools.combinations(xs,r))
    L=sp.Matrix([m_coeffs(sp.prod([pw(r) for r in l]),xs,parts) for l in parts])   # p = L m
    E=sp.Matrix([m_coeffs(sp.prod([el(r) for r in l]),xs,parts) for l in parts])   # e = E m
    Li=L.inv()
    def gram(qq,TT):
        D=sp.diag(*[z(l)*sp.prod([(1-qq**r)/(1-TT**r) for r in l]) for l in parts])
        return (Li*D*Li.T).applyfunc(sp.cancel)
    def GS(G):
        P=[]  # rows in m-coords
        for i in range(k):
            v=sp.zeros(1,k); v[i]=1
            for Pj in P:
                c=sp.cancel((v*G*Pj.T)[0]/(Pj*G*Pj.T)[0]); v=(v-c*Pj).applyfunc(sp.cancel)
            P.append(v)
        return sp.Matrix.vstack(*P)
    Ei=E.inv()
    if FAST:
        runfast(n,parts,k,GS,gram,Ei); return
    Pm=GS(gram(q,T)); B=(Pm*Ei).applyfunc(sp.cancel); A=B.inv().applyfunc(sp.cancel)
    BHL=(GS(gram(0,T))*Ei).applyfunc(sp.cancel); BQW=(GS(gram(q,0))*Ei).applyfunc(sp.cancel)
    bad=[]; cnt=0
    def reg(x,var):
        de=sp.denom(sp.cancel(x)); return sp.simplify(de.subs(var,0))!=0
    for M,name in ((A,'A'),(B,'B')):
        for i in range(k):
            for j in range(k):
                x=M[i,j]; cnt+=1
                if x==0: continue
                if not reg(x,q): bad.append(('R0',name,parts[i],parts[j],x))
                if not reg(x,T): bad.append(('R1',name,parts[i],parts[j],x))
    idx={p:i for i,p in enumerate(parts)}
    for nu in parts:
        for mu in parts:
            b=B[idx[nu],idx[mu]]; a=A[idx[nu],idx[mu]]
            if b!=0 and not dom(mu,conj(nu)): bad.append(('U-B',nu,mu))
            if a!=0 and not dom(conj(nu),mu): bad.append(('U-A',nu,mu))
            if sp.cancel(b.subs(q,0)-BHL[idx[nu],idx[mu]])!=0: bad.append(('HL',nu,mu))
            if sp.cancel(b.subs(T,0)-BQW[idx[nu],idx[mu]])!=0: bad.append(('QW',nu,mu))
        if B[idx[nu],idx[conj(nu)]]!=1: bad.append(('diagB',nu))
        if A[idx[nu],idx[conj(nu)]]!=1: bad.append(('diagA',nu))
    nz=0
    for lam in parts:
        for mu in parts:
            if dom(mu,lam):
                a=A[idx[lam],idx[conj(mu)]]
                if sp.cancel(a.subs(q,0))==0: bad.append(('NZ0',lam,mu))
                if sp.cancel(a.subs(T,0))==0: bad.append(('NZinf',lam,mu))
                nz+=1
    print('n=',n,'entries',cnt,'NZ pairs',nz,'BAD',len(bad)); [print(' ',b) for b in bad[:10]]
    # negative control: dividing P by its q=0-vanishing quantity (1-q^{a+1}...) is fine; instead use
    # P'_nu = P_nu / s^{n(nu')} (a plausible wrong normalisation) -> must fail R0 when n(nu')>0
    fails=sum(1 for nu in parts for mu in parts if B[idx[nu],idx[mu]]!=0 and
              not reg(B[idx[nu],idx[mu]]/q**sum(i*x for i,x in enumerate(conj(nu))),q))
    print('   negative control (P/s^{n(nu\')}): R0 failures =',fails, '(should be >0 for n>=2)')
def runfast(n,parts,k,GS,gram,Ei):
    idx={p:i for i,p in enumerate(parts)}; bad=[]
    for var,other,val,tag in ((q,T,sp.Rational(3,7),'s=0'),(T,q,sp.Rational(2,5),'tau=0')):
        G=gram(q,T).subs(other,val).applyfunc(sp.cancel)
        B=(GS(G)*Ei).applyfunc(sp.cancel); A=B.inv().applyfunc(sp.cancel)
        Ge=(gram(0,T) if var==q else gram(q,0)).subs(other,val).applyfunc(sp.cancel)
        Bedge=(GS(Ge)*Ei).applyfunc(sp.cancel)
        for M,name in ((A,'A'),(B,'B')):
            for i in range(k):
                for j in range(k):
                    x=M[i,j]
                    if x!=0 and sp.denom(x).subs(var,0)==0: bad.append(('reg',tag,name,parts[i],parts[j]))
        for nu in parts:
            if B[idx[nu],idx[conj(nu)]]!=1 or A[idx[nu],idx[conj(nu)]]!=1: bad.append(('diag',tag,nu))
            for mu in parts:
                b=B[idx[nu],idx[mu]]; a=A[idx[nu],idx[mu]]
                if b!=0 and not dom(mu,conj(nu)): bad.append(('U-B',tag,nu,mu))
                if a!=0 and not dom(conj(nu),mu): bad.append(('U-A',tag,nu,mu))
                if sp.cancel(b.subs(var,0)-Bedge[idx[nu],idx[mu]])!=0: bad.append(('edge-id',tag,nu,mu))
        for lam in parts:
            for mu in parts:
                if dom(mu,lam) and sp.cancel(A[idx[lam],idx[conj(mu)]].subs(var,0))==0: bad.append(('NZ',tag,lam,mu))
        neg=sum(1 for nu in parts for mu in parts if var==q and B[idx[nu],idx[mu]]!=0 and
              sp.denom(sp.cancel(B[idx[nu],idx[mu]]/q**sum(i*x for i,x in enumerate(conj(nu))))).subs(q,0)==0)
        print('n=',n,tag,'(other param =',val,') BAD',len(bad),('neg-control R0 failures=%d'%neg if var==q else '')); sys.stdout.flush()
    [print(' ',b) for b in bad[:10]]
def arms_legs(nu):
    c=conj(nu); return [(nu[i]-j-1,c[j]-i-1) for i in range(len(nu)) for j in range(nu[i])]
for n in (range(1,N+1) if len(sys.argv)<3 else [int(sys.argv[2])]): run(n); sys.stdout.flush()
