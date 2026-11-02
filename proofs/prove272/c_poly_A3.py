# Independent polynomial check, SL_4: O(N)=C[x_ab], Delta f(X,Y)=f(XY); Phi via theta-top bidegree; e_j = d/dt f(n exp(tE_{j,j+1})).
import sympy as sp, itertools
m=4
X={(a,b):sp.Symbol(f"x{a}{b}") for a in range(1,m+1) for b in range(a+1,m+1)}
Y={(a,b):sp.Symbol(f"y{a}{b}") for a in range(1,m+1) for b in range(a+1,m+1)}
def mat(V): return sp.Matrix(m,m,lambda i,k: 1 if i==k else (V[(i+1,k+1)] if k>i else 0))
NX,NY=mat(X),mat(Y)
def minor(M,I,J): return M.extract([i-1 for i in I],[j-1 for j in J]).det()
def ej(f,j):
    t=sp.Symbol('t'); E=sp.eye(m); E[j-1,j]=t; P=NX*E
    sub={X[k]:P[k[0]-1,k[1]-1] for k in X}
    return sp.expand(sp.diff(f.subs(sub,simultaneous=True),t).subs(t,0))
def wtX(mon):  # weight in simple-root coords of monomial in x (Q_+)
    w=[0]*(m-1)
    for (a,b),e in mon:
        for r in range(a,b): w[r-1]+=e
    return tuple(w)
def topsplit(f,g):
    D=sp.expand(f.subs({X[k]:(NX*NY)[k[0]-1,k[1]-1] for k in X},simultaneous=True).subs({X[k]:sp.Symbol('z'+str(k)) for k in X}))
    # careful: rebuild: Delta f = f(XY) as poly in X,Y
    return D
cnt=ok=0
for perm in itertools.permutations(range(m)):
    g={i+1:perm[i] for i in range(m)}
    th=lambda w: sum(w[r]*(g[r+1]-g[r+2]) for r in range(m-1))
    for j in range(1,m):
        if g[j]<g[j+1]: continue
        F=[k for k in range(1,m+1) if k not in (j,j+1) and g[j+1]<g[k]<g[j]]
        if not F: continue
        R=[k for k in F if k>j+1]
        if R: k=min(R); L=[r for r in range(j+2,k) if g[r]<g[j+1]]; J=list(range(1,j))+[j+1]+L+[k]
        else: k=max(F); L=[r for r in range(k+1,j) if g[r]<g[j+1]]; J=list(range(1,k))+L+[j+1]
        I=list(range(1,len(J)+1))
        b=sp.expand(minor(NX,I,J)); eb=ej(b,j); e2=ej(eb,j)
        def top(f):
            Df=sp.Poly(sp.expand(minor(NX*NY,I,[c for c in range(1,m+1)][:0]) if False else 0) ,*X.values()) if False else None
            F_=sp.expand(f.subs({X[q]:sp.Symbol('u%d%d'%q) for q in X},simultaneous=True))
            F_=sp.expand(F_.subs({sp.Symbol('u%d%d'%q):(NX*NY)[q[0]-1,q[1]-1] for q in X},simultaneous=True))
            P=sp.Poly(F_,*(list(X.values())+list(Y.values())))
            best=None
            for mon,c in P.terms():
                mx=[(q,e) for q,e in zip(X.keys(),mon[:len(X)]) if e]; w=wtX(mx)
                if best is None or th(w)>th(best): best=w
            return best
        wb=wtX([(q,e) for q,e in zip(X.keys(),sp.Poly(b,*X.values()).monoms()[0]) if e])
        web=wtX([(q,e) for q,e in zip(X.keys(),sp.Poly(eb,*X.values()).monoms()[0]) if e])
        cnt+=1
        good = (e2==0 and eb!=0 and top(b)==wb and top(eb)!=web)
        ok+=good
print("A3 far pairs:",cnt,"polynomial witness OK:",ok)
