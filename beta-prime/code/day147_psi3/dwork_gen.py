"""Day 147: Dwork defect  D := tau(K)/K,  K := F_P(T)^3 / varsigma(F_P)(T^3),
for several Frobenius lifts varsigma.  General framework.

All substitutions are computed SYMBOLICALLY in Z[E1,E2,E3] (sympy) and only then
specialised at E1=a, E2=b, E3=x (x kept as a polynomial variable).  So the lift is
ALWAYS applied before specialisation.

tau  = day146's actual tau (verify_master.py) : E1->E1+3, E2->E2+2E1+3, E3->E3+E1+E2+1
       (= the substitution u_i -> u_i + 1 on the three roots)
"""
import sys, math, itertools
sys.path.insert(0,'/home/agent/projects/beta-prime/code/day146_prove')
from fractions import Fraction as Q
import sympy as sp
from core import build_P

E1,E2,E3 = sp.symbols('E1 E2 E3'); Ev=[E1,E2,E3]
x = sp.Symbol('x')

TAU   = {E1:E1+3, E2:E2+2*E1+3, E3:E3+E1+E2+1}
PSI   = [E1**3-3*E1*E2+3*E3, E2**3-3*E1*E2*E3+3*E3**2, E3**3]
NAIVE = [E1**3, E2**3, E3**3]
E3ONLY= [E1, E2, E3**3]                     # day146's fibrewise lift (E1,E2 = Z_3 constants)
IDENT = [E1, E2, E3]                        # no lift at all (dwork.py)

def comp(outer, inner):
    """(outer o inner)(E_i): apply `inner` first then `outer`.
       inner, outer given as lists [img(E1),img(E2),img(E3)]."""
    m = {E1:outer[0], E2:outer[1], E3:outer[2]}
    return [sp.expand(inner[i].subs(m, simultaneous=True)) for i in range(3)]

TAUL = [TAU[E1],TAU[E2],TAU[E3]]

# ---------- univariate poly over Q as list of Fraction ----------
def trim(p):
    while p and p[-1]==0: p.pop()
    return p
def pmul(p,q):
    if not p or not q: return []
    r=[Q(0)]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        if a==0: continue
        for j,b in enumerate(q):
            if b: r[i+j]+=a*b
    return trim(r)
def padd(p,q):
    n=max(len(p),len(q)); r=[Q(0)]*n
    for i,a in enumerate(p): r[i]+=a
    for i,b in enumerate(q): r[i]+=b
    return trim(r)
def pscal(c,p): return trim([c*a for a in p]) if c else []

def to_ux(expr,a,b):
    """specialise E1=a,E2=b,E3=x ; return coefficient list in x"""
    e = sp.Poly(sp.expand(sp.sympify(expr).subs({E1:sp.Integer(a),E2:sp.Integer(b),E3:x}, simultaneous=True)), x)
    cs = e.all_coeffs()[::-1]
    return trim([Q(int(c)) for c in cs])

def subst(P, f1, f2, f3):
    ma=max((m[0] for m in P),default=0); mb=max((m[1] for m in P),default=0); mc=max((m[2] for m in P),default=0)
    A=[[Q(1)]]; B=[[Q(1)]]; C=[[Q(1)]]
    for _ in range(ma): A.append(pmul(A[-1],f1))
    for _ in range(mb): B.append(pmul(B[-1],f2))
    for _ in range(mc): C.append(pmul(C[-1],f3))
    acc={}
    for (i,j,k),co in P.items():
        t=pmul(pmul(A[i],B[j]),C[k])
        for d,v in enumerate(t):
            if v: acc[d]=acc.get(d,Q(0))+co*v
    if not acc: return []
    out=[Q(0)]*(max(acc)+1)
    for d,v in acc.items(): out[d]=v
    return trim(out)

def Smul(F,G,N):
    R={}
    for n1,p in F.items():
        if n1>N or not p: continue
        for n2,q in G.items():
            if n1+n2>N or not q: continue
            R[n1+n2]=padd(R.get(n1+n2,[]), pmul(p,q))
    return {n:p for n,p in R.items() if p}
def Sinv(F,N):
    assert F.get(0)==[Q(1)], F.get(0)
    B={0:[Q(1)]}
    for n in range(1,N+1):
        acc=[]
        for j in range(1,n+1):
            if j in F and (n-j) in B: acc=padd(acc, pmul(F[j],B[n-j]))
        B[n]=pscal(Q(-1),acc)
    return {n:p for n,p in B.items() if p}
def Tcube(F,N): return {3*n:p for n,p in F.items() if 3*n<=N}
def v3(fr):
    if fr==0: return None
    n,d=fr.numerator,fr.denominator; v=0
    while n%3==0: n//=3; v+=1
    while d%3==0: d//=3; v-=1
    return v

_Pcache={}
def getP(N):
    if N not in _Pcache: _Pcache[N]=build_P(N)
    return _Pcache[N]

def series(P,N,imgs,a,b,upto=None):
    f=[to_ux(i,a,b) for i in imgs]
    M = N if upto is None else upto
    S={n: pscal(Q(1,math.factorial(n)), subst(P[n],*f)) for n in range(M+1)}
    return {n:p for n,p in S.items() if p}

def compute(a,b,N,lift,order='tau_after'):
    """order='tau_after'  -> tau(K) uses (tau o varsigma)   [ = genuine tau(K) ]
       order='tau_before' -> tau(K) uses (varsigma o tau)   [ = K(tau F_P) ]"""
    P=getP(N)
    F  = series(P,N,IDENT,a,b)
    Ft = series(P,N,TAUL,a,b)
    Fs = series(P,N,lift,a,b,upto=N//3)
    if order=='tau_after': g = comp(TAUL, lift)     # tau o varsigma
    else:                  g = comp(lift, TAUL)     # varsigma o tau
    Fts= series(P,N,g,a,b,upto=N//3)
    K  = Smul(Smul(Smul(F,F,N),F,N),   Sinv(Tcube(Fs ,N),N), N)
    Kt = Smul(Smul(Smul(Ft,Ft,N),Ft,N),Sinv(Tcube(Fts,N),N), N)
    D  = Smul(Kt, Sinv(K,N), N)
    return K,D

def report(a,b,N,lift,lname,order='tau_after',show=True):
    K,D=compute(a,b,N,lift,order)
    ok=True; first=None; minv={}
    for n in range(N+1):
        p=D.get(n,[])
        if n==0:
            if p!=[Q(1)]: ok=False; first=first or 0
            continue
        vs=[(v3(c) if c else None) for c in p]
        nz=[v for v in vs if v is not None]
        minv[n]=min(nz) if nz else None
        if minv[n] is not None and minv[n]<1:
            ok=False
            if first is None: first=n
    if show:
        print(f"\n##### (E1,E2)=({a},{b}) phi1={a+b+1}  lift={lname}  order={order}  N={N}")
        print("  v3 tau(K)/K coefficients (row=T-deg, col=E3-deg, '.'=0):")
        for n in range(N+1):
            p=D.get(n,[])
            vs=[(v3(c) if c else None) for c in p]
            flag = "  <== VIOLATION" if (n>=1 and any(v is not None and v<1 for v in vs)) else ""
            print(f"   n={n:3d} "+' '.join(f"{(v if v is not None else '.'):>3}" for v in vs)+flag)
        print(f"  ==> PASS={ok}  first failing T-degree={first}  "
              f"min v3 (n>=1) = {min([v for v in minv.values() if v is not None],default=None)}")
    return ok, first, minv, K, D
