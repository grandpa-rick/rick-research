"""Certificate: beta_C = (1-pi_1)(1-pi_{N-1}) o 1_C  (C = set of weights = #ones).
Check (a) beta_C commutes with S = End_H(V) (exact over Z: S basis via fmpz nullspace, blockwise),
(b) beta_{2} not in A = span(monoid)  (exact rank over Z).  n=2, full tensor space."""
import sys, itertools, numpy as np
from flint import fmpz_mat
def run(N, exact=True):
    W=list(itertools.product([1,2],repeat=N)); idx={w:k for k,w in enumerate(W)}; d=len(W)
    def pmat(i):
        M=np.zeros((d,d),dtype=np.int64)
        for w in W:
            k=idx[w]
            if w[i]<w[i+1]: M[idx[w[:i]+(w[i+1],w[i])+w[i+2:]],k]=1
            else: M[k,k]=1
        return M
    Pm=[pmat(i) for i in range(N-1)]
    I=np.eye(d,dtype=np.int64)
    h=(I-Pm[N-2])@(I-Pm[0])        # right action v.(1-pi_1).(1-pi_{N-1}) ; column convention: later factor on the left
    ones=[w.count(1) for w in W]
    def oneC(C): return np.diag([1 if o in C else 0 for o in ones]).astype(np.int64)
    blocks={}
    for k,o in enumerate(ones): blocks.setdefault(o,[]).append(k)
    # S basis blockwise exact
    Sb=[]
    for s,bs in blocks.items():
        for t,bt in blocks.items():
            ds,dt=len(bs),len(bt); rows=[]
            for Pi in Pm:
                Ps=Pi[np.ix_(bs,bs)]; Pt=Pi[np.ix_(bt,bt)]
                rows.append(np.kron(np.eye(dt,dtype=np.int64),Ps.T)-np.kron(Pt,np.eye(ds,dtype=np.int64)))
            R=np.vstack(rows)
            X,k=fmpz_mat([[int(x) for x in r] for r in R]).nullspace()
            K=np.array([[int(X[r,c]) for c in range(k)] for r in range(ds*dt)],dtype=object)
            for c in range(k):
                phi=np.zeros((d,d),dtype=object); phi[np.ix_(bt,bs)]=K[:,c].reshape(dt,ds); Sb.append(phi)
    print(N,'dim S',len(Sb),flush=True)
    ok_all=True
    for C in [{2},{3},set(range(0,N+1,2)),{1,N-1},{0,2,N}]:
        beta=(h@oneC(C)).astype(object)     # first project to C (commutes with H), then h
        ok=all(not (beta.dot(phi)-phi.dot(beta)).any() for phi in Sb)
        print('  C',sorted(C),'beta in B:',ok); ok_all&=ok
    # A: monoid span (closure)
    gens=[tuple(int(np.nonzero(Pi[:,k])[0][0]) for k in range(d)) for Pi in Pm]
    ident=tuple(range(d)); Mn={ident}; fr=[ident]
    while fr:
        nf=[]
        for f in fr:
            for g in gens:
                hh=tuple(g[f[x]] for x in range(d))
                if hh not in Mn: Mn.add(hh); nf.append(hh)
        fr=nf
    rows=[]
    for f in Mn:
        v=np.zeros(d*d,dtype=np.int64); v[[f[x]*d+x for x in range(d)]]=1; rows.append(v)
    beta=(h@oneC({2})).ravel()
    rA=fmpz_mat([[int(x) for x in r] for r in rows]).rank()
    rAb=fmpz_mat([[int(x) for x in r] for r in rows+[beta]]).rank()
    print('  dim A',rA,' rank(A+beta_{2})',rAb,' beta_{2} notin A:',rAb==rA+1)
    # lower bound: span of h 1_s, s=0..N, modulo A
    extra=[(h@oneC({s})).ravel() for s in range(N+1)]
    rAe=fmpz_mat([[int(x) for x in r] for r in rows+extra]).rank()
    print('  dim(A+span h1_s)-dimA =',rAe-rA)
for N in map(int,sys.argv[1:]): run(N)
