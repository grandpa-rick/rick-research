import sys; sys.path.insert(0,'/home/agent/projects/proofs/wake279')
import numpy as np
from coxkl import *
H3=[[1,5,2],[5,1,3],[2,3,1]]
G=coxeter_group(H3); P,mu=kl(G); cells,D=left_cells(G,mu)
def wd(w): return ''.join(str(s+1) for s in G['word'][w]) or 'e'
out=[]
for c in sorted(cells,key=lambda c:(len(c),min(G['length'][w] for w in c))):
    if len(c)!=5: continue
    A=cell_module(G,mu,D,c,'C')
    print('cell',[wd(w) for w in c],'D',[sorted(s+1 for s in D[w]) for w in c])
    for s in range(3): print(' 1+s%d'%(s+1)); print(A[s].astype(int))
    out.append(dict(cell=[wd(w) for w in c],D=[sorted(D[w]) for w in c],A=[A[s].astype(int).tolist() for s in range(3)]))
print('max mu',mu.max())
import json; json.dump(out,open('cells5.json','w'))
