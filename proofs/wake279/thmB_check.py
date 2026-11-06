"""Theorem B check: for every s,t with m(s,t)>=4, J=S\\{t}: (x,z)=(w_J, s t w_J) is a dominated twin in the left cell of w_J.
Also report dim / commutant dim (irreducibility) of that cell module."""
import sys
from coxkl import *
from bn_family import commutant_dim
exec(open('twin_criterion.py').read().split("for name in")[0].split("from coxkl import *")[1])
for name in sys.argv[1].split(','):
    M=CASES[name]; G=coxeter_group(M); P,mu=kl(G); cells,D=left_cells(G,mu); L=G['length']; lm=G['lm']; N=G['N']; n=G['n']
    for s in range(n):
        for t in range(n):
            if s==t or M[s][t]<4: continue
            J=[r for r in range(n) if r!=t]
            wJ=max((u for u in range(N) if set(G['word'][u])<=set(J)), key=lambda u:L[u])
            c=next(c for c in cells if wJ in c); z=lm[s,lm[t,wJ]]
            ok= z in c and z!=wJ and D[z]<=D[wJ] and all(mu[y,z]>=mu[y,wJ] for y in c if D[y]-D[wJ])
            onlyy=[y for y in range(N) if mu[y,wJ] and (D[y]-D[wJ])]
            print(name,'s=%d t=%d'%(s+1,t+1),'twin',ok,'| y with mu(y,wJ)!=0, L(y) not sub J:',[G['word'][y] for y in onlyy],'== t wJ?',onlyy==[lm[t,wJ]],'| cell dim',len(c),'commutant',commutant_dim(cell_module(G,mu,D,c,conv='C')))
