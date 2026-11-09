import sys, pickle
sys.path.insert(0,'/home/agent/projects/proofs/wake285')
from targets import *   # chdir to prove285
from itertools import combinations
n=8; G=D(n)
deg=[r[G.classes.index(((1,)*n,(),0))] for r in G.table]
subsets=[frozenset(J) for k in range(n+1) for J in combinations(range(1,n+1),k)]
out={}
for v in sorted(Con(n)):
    g=dist(n,v,subsets)
    out[label(n,v)]=dict(dim=sum(a*b for a,b in zip(v,deg)), dist={frozenset(MAP[s] for s in A):c for A,c in g.items()})
pickle.dump(out,open('/home/agent/projects/proofs/prove286/cons8.pkl','wb'))
print(len(out), sum(1 for k in out), sorted(set(d['dim'] for d in out.values()))[:50])
