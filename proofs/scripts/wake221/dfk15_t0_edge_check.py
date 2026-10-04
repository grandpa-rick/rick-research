# Check: prod_alpha E_alpha|_{t=0}^{m_alpha(mu)} 1  ==  s^{n(mu)} P_{mu'}(x; 1/s, 0)
# E_k at t=0 per Day217e def; DFK M_{k,1} = sum_I z_I a_I(z) Gamma_I (Gamma: z_i -> q z_i), q=s.
# P_lam(x;q,t) computed independently: monic, m-triangular eigenfunction of Macdonald D_1 (generic t), then t->0.
import itertools, sys
from sympy import symbols, Poly, cancel, together, expand, simplify, Rational, factor, solve, S as SS
N=int(sys.argv[1]); nmax=int(sys.argv[2])
x=symbols(f'x0:{N}'); s,q,t=symbols('s q t')
def parts(n,m=None):
    if m is None: m=n
    if n==0: yield (); return
    for k in range(min(n,m),0,-1):
        for p in parts(n-k,k): yield (k,)+p
def conj(l): return tuple(sum(1 for a in l if a>j) for j in range(l[0])) if l else ()
def nfun(l): return sum(i*a for i,a in enumerate(l))
def shift(F,A,c): return F.subs({x[i]:c*x[i] for i in A},simultaneous=True)
def Ek_t(k,F,tt,ss):  # Rick's E_k
    tot=0
    for A in itertools.combinations(range(N),k):
        c=1
        for i in A:
            c*=x[i]
            for j in range(N):
                if j not in A: c*=(x[i]-tt*x[j])/(x[i]-x[j])
        tot+=c*shift(F,A,ss)
    return expand(cancel(together(tot)))
def M_k1(k,F,qq):  # DFK (5.15) n=1 literal: (z_I)^1 a_I(z) Gamma_I, a_I=prod_{i in I, j notin I} z_i/(z_i-z_j)
    tot=0
    for I in itertools.combinations(range(N),k):
        c=1
        for i in I:
            c*=x[i]
            for j in range(N):
                if j not in I: c*=x[i]/(x[i]-x[j])
        tot+=c*shift(F,I,qq)
    return expand(cancel(together(tot)))
def mono(l):
    l=tuple(l)+(0,)*(N-len(l))
    return sum({tuple(p):1 for p in itertools.permutations(l)} and [ \
        __import__('sympy').Mul(*[x[i]**p[i] for i in range(N)]) for p in set(itertools.permutations(l))])
def dominated(a,b):  # a <= b
    sa=sb=0
    for i in range(max(len(a),len(b))):
        sa+=a[i] if i<len(a) else 0; sb+=b[i] if i<len(b) else 0
        if sa>sb: return False
    return True
def D1(F):
    tot=0
    for i in range(N):
        c=1
        for j in range(N):
            if j!=i: c*=(t*x[i]-x[j])/(x[i]-x[j])
        tot+=c*shift(F,[i],q)
    return expand(cancel(together(tot)))
def macP(lam):
    n=sum(lam); lower=[m for m in parts(n) if m!=lam and dominated(m,lam) and len(m)<=N]
    cs=symbols(f'c0:{len(lower)}')
    F=mono(lam)+sum(c*mono(m) for c,m in zip(cs,lower))
    lam_=tuple(lam)+(0,)*(N-len(lam)); ev=sum(q**lam_[i]*t**(N-1-i) for i in range(N))
    G=Poly(expand(D1(F)-ev*F),*x)
    if not cs:
        assert all(c==0 for c in G.coeffs()); return expand(F)
    sols=solve(G.coeffs(),cs,dict=True); assert len(sols)==1, sols
    sol=sols[0]
    return expand(F.subs(sol))
ok=True
for n in range(1,nmax+1):
    for mu in parts(n):
        if mu[0]>N-1: continue   # DFK: lambda=mu' must have <= r = N-1 parts
        # operator identity on a test function
        lhs=SS(1); rhs=SS(1)
        for a in mu: lhs=Ek_t(a,lhs,0,s); rhs=M_k1(a,rhs,s)
        same_op = expand(lhs-rhs)==0
        lam=conj(mu)
        P=macP(lam)
        P0=cancel(together(P.subs(t,0).subs(q,1/s)))
        target=expand(cancel(s**nfun(mu)*P0))
        good=expand(lhs-target)==0
        ok&=good and same_op
        print(f'N={N} mu={mu} lam=mu\'={lam}: E|t0 == M_k1(q=s): {same_op};  prod == s^n(mu) P_lam(x;1/s,0): {good}',flush=True)
print('ALL OK' if ok else 'FAIL')
