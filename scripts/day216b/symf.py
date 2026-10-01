"""tiny symmetric-function library in power-sum basis over Q(q,t,s)."""
import sympy as sp, itertools
from functools import lru_cache
from math import factorial
q,t,s=sp.symbols('q t s')
def parts(n, mx=None):
    mx = n if mx is None else mx
    if n == 0: yield (); return
    for p in range(min(n, mx), 0, -1):
        for r in parts(n-p, p): yield (p,)+r
def zee(l):
    from collections import Counter
    r=1
    for i,m in Counter(l).items(): r*=i**m*factorial(m)
    return r
def add(a,b,c=1):
    r=dict(a)
    for k,v in b.items(): r[k]=r.get(k,0)+c*v
    return {k:v for k,v in r.items() if v!=0}
def mul(a,b):
    r={}
    for k1,v1 in a.items():
        for k2,v2 in b.items():
            k=tuple(sorted(k1+k2,reverse=True)); r[k]=r.get(k,0)+v1*v2
    return {k:v for k,v in r.items() if v!=0}
def scal(a,c): return {k:v*c for k,v in a.items()}
@lru_cache(None)
def h(n): return {l: sp.Rational(1,zee(l)) for l in parts(n)} if n>0 else ({():1} if n==0 else {})
@lru_cache(None)
def e(n): return {l: sp.Rational((-1)**(n-len(l)),zee(l)) for l in parts(n)} if n>0 else ({():1} if n==0 else {})
def prod(fs):
    r={():1}
    for f in fs: r=mul(r,f)
    return r
@lru_cache(None)
def schur(lam):
    lam=tuple(lam); L=len(lam)
    if L==0: return {():1}
    M=sp.Matrix(L,L,lambda i,j: sp.Symbol(f'H{lam[i]-i+j}'))
    det=sp.expand(M.det()); r={}
    for term in sp.Add.make_args(det):
        c,fs=term.as_coeff_mul(); f={():c}; zero=False
        for fac in fs:
            b,ex=fac.as_base_exp(); idx=int(str(b)[1:])
            if idx<0: zero=True;break
            for _ in range(int(ex)): f=mul(f,h(idx))
        if not zero: r=add(r,f)
    return r
def inner(a,b): return sp.together(sum(v*b.get(k,0)*zee(k) for k,v in a.items()))
def pleth(a, fn):
    """p_k -> fn(k) p_k (fn gives scalar)"""
    return {l: sp.together(v*sp.prod([fn(i) for i in l])) for l,v in a.items()}
def omega(a): return {l: v*(-1)**(sum(l)-len(l)) for l,v in a.items()}
def to_basis(a, basis):
    """basis: dict name->sf; solve a = sum c_name basis[name]"""
    names=list(basis); n=sum(next(iter(a)) ) if a else 0
    P=sorted(set(k for b in basis.values() for k in b)|set(a))
    M=sp.Matrix([[basis[nm].get(k,0) for nm in names] for k in P]); v=sp.Matrix([a.get(k,0) for k in P])
    sol=M.solve_least_squares(v) if M.shape[0]>M.shape[1] else M.LUsolve(v)
    return {nm: sp.factor(sp.simplify(sol[i])) for i,nm in enumerate(names)}
def dominates(a,b):
    sa=sb=0
    for i in range(max(len(a),len(b))):
        sa+=a[i] if i<len(a) else 0; sb+=b[i] if i<len(b) else 0
        if sa<sb: return False
    return True
def transpose(k): return tuple(sum(1 for p in k if p>i) for i in range(k[0])) if k else ()
@lru_cache(None)
def Htilde(mu):
    n=sum(mu); P=list(parts(n)); cs=sp.symbols(f'c0:{len(P)}')
    H={}
    for c,l in zip(cs,P): H=add(H,scal(schur(l),c))
    eqs=[]
    A=pleth(H, lambda k: 1-q**k); B=pleth(H, lambda k: 1-t**k)
    for l in P:
        if not dominates(l,mu): eqs.append(inner(A,schur(l)))
        if not dominates(l,transpose(mu)): eqs.append(inner(B,schur(l)))
    eqs.append(inner(H,schur((n,)))-1)
    sol=sp.solve([sp.numer(sp.together(x)) for x in eqs],cs,dict=True)[0]
    return {k: sp.factor(sp.together(v.subs(sol))) for k,v in H.items()}
