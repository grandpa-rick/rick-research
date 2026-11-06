import sys
from coxkl import *
from bn_family import Bmat, commutant_dim
n=int(sys.argv[1])
G=coxeter_group(Bmat(n)); P,mu=kl(G); cells,D=left_cells(G,mu); L=G['length']; N=G['N']
w=lambda u: ''.join(str(s+1) for s in G['word'][u]) or 'e'
# longest elements of parabolics
wJ={}
for u in range(N):
    J=frozenset(G['word'][u])
    if J not in wJ or L[u]>L[wJ[J]]: wJ[J]=u
isWJ={u:J for J,u in wJ.items()}
for c in cells:
    if commutant_dim(cell_module(G,mu,D,c,conv='C'))!=1: continue
    tw=[(z,x) for x in c for z in c if x!=z and D[z]<=D[x] and all(mu[y,z]>=mu[y,x] for y in c if D[y]-D[x])]
    if not tw: continue
    desc=[(w(z),w(x), 'x=w_J J=%s'%sorted(s+1 for s in isWJ[x]) if x in isWJ else 'x not w_J') for z,x in tw]
    print('dim',len(c),'#twins',len(tw),desc[:3])
