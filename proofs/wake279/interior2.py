import sys
from coxkl import *
exec(open('twin_criterion.py').read().split("for name in")[0].split("from coxkl import *")[1])
for name in sys.argv[1].split(','):
    M=CASES[name]; G = coxeter_group(M); P, mu = kl(G); cells, D = left_cells(G, mu); n=G['n']; N=G['N']
    nb=lambda s:[t for t in range(n) if t!=s and M[s][t]==3]
    intr=lambda A: frozenset(s for s in A if all(t in A for t in nb(s)))
    # two-sided cells: union left cells related by inverse
    inv=[None]*N
    for w in range(N):
        # inverse via word reversal
        u=0
        for s in G['word'][w]: u=G['lm'][s,u]
        inv[w]=u
    cid={}
    for i,c in enumerate(cells):
        for w in c: cid[w]=i
    # union-find on cells: c ~ cell of inverses
    par=list(range(len(cells)))
    def f(a):
        while par[a]!=a: a=par[a]
        return a
    for w in range(N):
        a,b=f(cid[w]),f(cid[inv[w]]); par[a]=b
    # need also left cells in same two-sided cell connected via R-cells: x~_R y iff x^-1 ~_L y^-1; two-sided = generated
    tw={}
    for w in range(N): tw.setdefault(f(cid[w]),[]).append(w)
    bad=0; badex=None
    for T in tw.values():
        Ds=set(D[w] for w in T)
        for A in Ds:
            I=intr(A)
            for B in Ds:
                if B and B<=I: bad+=1; badex=(sorted(A),sorted(B))
    print(name,'two-sided (approx) violations',bad,badex, 'num 2-sided',len(tw))
