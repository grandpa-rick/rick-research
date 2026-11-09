import numpy as np, sympy as sp, itertools
t=sp.symbols('t',positive=True)
g=[sp.Matrix(x) for x in [[0,0,-t,0,1],[0,-t,-2*t,1-t,2],[-t,-2*t,1-2*t,2-2*t,1-t],[-2*t,-t,0,1-t,2-2*t]]]
gens=[sp.eye(5)[:,i] for i in range(5)]+g
names=['c0','c1','c2','c3','c4','g1','g2','g3','g4']
tv=sp.Rational(3,5)
for S in itertools.combinations(range(9),4):
    M=sp.Matrix.hstack(*[gens[i] for i in S]).T
    if M.subs(t,tv).rank()<4: continue
    n=M.nullspace()
    if len(n)!=1: continue
    f=n[0]; vals=[ (f.T*v)[0].subs(t,tv) for v in gens]
    if all(x>=0 for x in vals) or all(x<=0 for x in vals):
        if all(x<=0 for x in vals): f=-f
        f=sp.simplify(f/ f[2]) if f[2]!=0 else f
        if f[1]!=0 and f[0]==0 and f[3]==0: print([names[i] for i in S], list(sp.factor(f.T)))
