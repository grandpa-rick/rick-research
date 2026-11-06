"""B_n: for J = S\{t}, t in {s1,s2} (s1--s2 the m=4 bond), the left cell of w_J: dim, commutant dim, twin (s t w_J, w_J) check."""
import sys
from coxkl import *
from bn_family import Bmat, commutant_dim
n=int(sys.argv[1])
G=coxeter_group(Bmat(n)); P,mu=kl(G); cells,D=left_cells(G,mu)
L=G['length']; lm=G['lm']; N=G['N']
print('B%d cells'%n,len(cells),'dims',sorted(len(c) for c in cells))
for t,s in ((1,0),(0,1)):
    J=[r for r in range(n) if r!=t]
    wJ=max((u for u in range(N) if set(G['word'][u])<=set(J)), key=lambda u:L[u])
    c=next(c for c in cells if wJ in c)
    A=cell_module(G,mu,D,c,conv='C')
    z=lm[s,lm[t,wJ]]
    ok= z in c and D[z]<=D[wJ] and all(mu[y,z]>=mu[y,wJ] for y in c if D[y]-D[wJ])
    print(' t=s%d: cell dim'%(t+1),len(c),'commutant',commutant_dim(A),'twin(s t wJ, wJ):',ok,'a-guess l(wJ)=',L[wJ])
