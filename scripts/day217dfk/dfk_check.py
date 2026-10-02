# Check DFK 1704.00154 dictionary: nabla^(N) e_k nabla^(N)^{-1} vs M_{k;1}, N=3, exact rationals.
import itertools, sympy as sp
from sympy import Rational as R
N=3; x=sp.symbols('x1:%d'%(N+1))
q=R(3,7); t=R(-5,2)   # DFK (q,t)
def parts(d,l):
    out=[]
    def rec(rem,mx,cur):
        if rem==0: out.append(tuple(cur+[0]*(l-len(cur)))); return
        if len(cur)==l: return
        for p in range(min(rem,mx),0,-1): rec(rem-p,p,cur+[p])
    rec(d,d,[]); return out
def mono(lam):
    return sp.Add(*[sp.Mul(*[x[i]**e[i] for i in range(N)]) for e in set(itertools.permutations(lam))])
def coords(f,d):
    P=sp.Poly(sp.expand(f),*x); B=parts(d,N)
    return [P.coeff_monomial(sp.Mul(*[x[i]**l[i] for i in range(N)])) for l in B]
def op(k,n,f,tt=t):
    # DFK M_{k;n} : sum_I x_I^n prod_{i in I, j notin I} (t x_i - x_j)/(x_i-x_j) Gamma_I (q-shift)
    s=0
    for I in itertools.combinations(range(N),k):
        c=sp.Mul(*[(tt*x[i]-x[j])/(x[i]-x[j]) for i in I for j in range(N) if j not in I])
        sub={x[i]:q*x[i] for i in I}
        s+=sp.Mul(*[x[i]**n for i in I])*c*f.subs(sub,simultaneous=True)
    return sp.factor(sp.together(s))
def nn(l): return sum(i*li for i,li in enumerate(l))
def nconj(l): return sum(li*(li-1)//2 for li in l)
def macP(d):
    B=parts(d,N); M=[mono(l) for l in B]
    D=sp.Matrix([coords(op(1,0,m),d) for m in M]).T  # columns = images
    Ps={}
    for a,l in enumerate(B):
        ev=sum(q**l[i]*t**(N-1-i) for i in range(N))
        # P_l = m_l + sum_{mu<l} c m_mu ; B ordered reverse-lex so lower = later indices
        idx=list(range(a,len(B)))
        A=(D-ev*sp.eye(len(B)))[:,idx]
        cs=sp.symbols('c0:%d'%len(idx))
        v=sp.Matrix([1]+list(cs[1:]))
        if len(idx)>1:
            sol=sp.solve(list(A*v),cs[1:],dict=True)[0]
            v=v.subs(sol)
        Ps[l]=sp.expand(sum(v[j]*M[idx[j]] for j in range(len(idx))))
    return Ps
P={d:macP(d) for d in range(0,5)}
def nab(f,d,sign=1):
    B=parts(d,N); Ps=[P[d][l] for l in B]
    Mat=sp.Matrix([coords(p,d) for p in Ps]).T
    c=Mat.LUsolve(sp.Matrix(coords(f,d)))
    return sp.expand(sum(c[j]*(t**(-nn(l))*q**nconj(l))**sign*Ps[j] for j,l in enumerate(B)))
e=[1,x[0]+x[1]+x[2],x[0]*x[1]+x[0]*x[2]+x[1]*x[2],x[0]*x[1]*x[2]]
for k in (1,2,3):
  for d in range(0,5-k):
    for l in parts(d,N):
        f=P[d][l]
        for sign in (1,-1):
            lhs=nab(sp.expand(e[k]*nab(f,d,-sign)),d+k,sign)  # nabla^sign e_k nabla^-sign
            rhs=sp.expand(op(k,1,f))
            r=sp.cancel(lhs/rhs) if rhs!=0 else None
            ok = r is not None and r.is_number
            print(k,l,'sign',sign,'ratio',r if ok else 'NOT SCALAR')
