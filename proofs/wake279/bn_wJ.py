"""Cell of w_J, J = S\{s2}, in B_n (s1--s2 has m=4). Print elements as y.w_J, descents, mu-graph, irreducibility, twin (s1 s2 w_J, w_J)."""
import sys
from coxkl import *
from bn_family import Bmat, commutant_dim
import numpy as np
n=int(sys.argv[1])
G=coxeter_group(Bmat(n)); P,mu=kl(G); cells,D=left_cells(G,mu)
L=G['length']; lm=G['lm']; N=G['N']
J=[s for s in range(n) if s!=1]
wJ=max((u for u in range(N) if set(G['word'][u])<=set(J)), key=lambda u:L[u])
c=next(c for c in cells if wJ in c)
# write each element as y.wJ: find y by stripping
def yof(u):
    # u = y wJ with l(u)=l(y)+l(wJ): y word = first l(u)-l(wJ) letters of some reduced word ending in wJ; use right division
    inv={}
    return None
w=lambda u: ''.join(str(s+1) for s in G['word'][u]) or 'e'
A=cell_module(G,mu,D,c,conv='C')
print('B%d cell of w_J: dim'%n,len(c),'commutant',commutant_dim(A))
for u in sorted(c,key=lambda u:L[u]):
    nbrs=[(w(v),int(mu[u,v])) for v in c if mu[u,v]]
    print(' ',w(u),'l=',L[u],'L=',sorted(s+1 for s in D[u]),'nbrs',nbrs)
z=lm[0,lm[1,wJ]]
print('z=s1s2wJ in cell:',z in c, 'twin ok:', D[z]<=D[wJ] and all(mu[y,z]>=mu[y,wJ] for y in c if D[y]-D[wJ]))
