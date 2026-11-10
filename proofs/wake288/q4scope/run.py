import itertools, sys, sympy as sp, numpy as np
from ind import *; from modp import *
def comps_sets(m): return [frozenset(S) for r in range(m) for S in itertools.combinations(range(1,m),r)]
def comp(S,m):
    c=[];prev=0
    for s in sorted(S)+[m]: c.append(s-prev); prev=s
    return tuple(c)
Nmax=int(sys.argv[1]); out=[]
for N in range(2,Nmax+1):
  for a in range(1,N):
    b=N-a
    pass
    for S1 in comps_sets(a):
      for S2 in comps_sets(b):
        D=set(S1)|{s+a for s in S2}
        reps,mats=ind_module([a,b],D); n=len(reps)
        if N<=4: check_rel(mats,N)
        E=endo_modp(mats,n); k=nsum_modp(E,n,1); k2=nsum_modp(E,n,2)
        # Mackey check: for every 0<a'<N, double-coset spans preserved by pi_i, i!=a'
        mack=True
        for ap in range(1,N):
            lab=[sum(1 for v in w[:a] if v<=ap) for w in reps]
            for i,A in mats.items():
                if i==ap: continue
                for r,c in zip(*np.nonzero(np.array(A.tolist(),dtype=np.int64))):
                    if lab[r]!=lab[c]: mack=False
        out.append((N,comp(S1,a),comp(S2,b),n,len(E),k,k2,mack))
        print(N,comp(S1,a),comp(S2,b),'dim',n,'dimEnd',len(E),'#summands',k,k2,'MackeySplitBasis',mack,flush=True)
