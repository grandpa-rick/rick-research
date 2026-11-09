import numpy as np, sympy as sp, json
from scipy.optimize import linprog
cells=json.load(open('cells5.json')); A=[sp.Matrix(a) for a in cells[3]['A']]
t=sp.symbols('t',positive=True)
g=[sp.Matrix(x) for x in [[0,0,-t,0,1],[0,-t,-2*t,1-t,2],[-t,-2*t,1-2*t,2-2*t,1-t],[-2*t,-t,0,1-t,2-2*t]]]
gens=list(sp.eye(5).columnspace())+g
# numeric facet enumeration at t0 to find which images are tight
import itertools
def facets(tv):
    G=np.array([[float(x.subs(t,tv)) for x in v] for v in gens])
    F=[]
    for S in itertools.combinations(range(len(G)),4):
        M=G[list(S)]
        if np.linalg.matrix_rank(M)<4: continue
        n=sp.Matrix(M.tolist()).nullspace()
        f=np.array([float(x) for x in n[0]]); 
        vals=G@f
        if (vals>-1e-9).all(): F.append(tuple(np.round(f/np.abs(f).max(),9)))
        elif (vals<1e-9).all(): F.append(tuple(np.round(-f/np.abs(f).max(),9)))
    return sorted(set(F)),G
for tv in [0.55,0.6]:
    F,G=facets(tv)
    print('t',tv,'facets',len(F))
    for s in range(3):
        for k,gg in enumerate(g):
            im=np.array([float(x.subs(t,tv)) for x in A[s]*gg])
            m=min(np.array(f)@im for f in F)
            if m<0.05: print('  tight/near: (1+s%d)g%d minval'%(s+1,k+1),round(m,5), [f for f in F if abs(np.array(f)@im)<0.06])
