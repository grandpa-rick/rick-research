import sys
from coxkl import *
import numpy as np
def Bmat(n):
    M=[[1 if i==j else (3 if abs(i-j)==1 else 2) for j in range(n)] for i in range(n)]
    M[0][1]=M[1][0]=4; return M
def commutant_dim(A):
    d=A[0].shape[0]; I=np.eye(d)
    rows=[np.kron(I,a)-np.kron(a.T,I) for a in A]
    K=np.vstack(rows); return d*d-np.linalg.matrix_rank(K)
if __name__=="__main__":
    n=int(sys.argv[1])    
    G=coxeter_group(Bmat(n)); P,mu=kl(G); cells,D=left_cells(G,mu)
    w=lambda u: ''.join(str(s+1) for s in G['word'][u]) or 'e'
    idx={G['word'][u]:u for u in range(G['N'])}
    for c in cells:
        A=cell_module(G,mu,D,c,conv='C'); cd=commutant_dim(A)
        tw=[(w(z),w(x)) for x in c for z in c if x!=z and D[z]<=D[x] and all(mu[y,z]>=mu[y,x] for y in c if D[y]-D[x])]
        if tw and cd==1:
            print('irred d=%d'%len(c),'minlen rep',w(min(c,key=lambda u:G['length'][u])),'twins',tw[:3])
