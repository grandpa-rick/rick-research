import numpy as np, time
from coxkl import *
def A(n): return [[1 if i==j else (3 if abs(i-j)==1 else 2) for j in range(n)] for i in range(n)]
for name,M in [('A3',A(3)),('I2(5)',[[1,5],[5,1]]),('B3',[[1,4,2],[4,1,3],[2,3,1]]),('D4',[[1,3,2,2],[3,1,3,3],[2,3,1,2],[2,3,2,1]]),('A4',A(4))]:
    t=time.time(); G=coxeter_group(M); P,mu=kl(G); cells,D=left_cells(G,mu)
    ok=True
    for c in cells:
        Am=cell_module(G,mu,D,c); R=rho_all(G,Am)
        for w in range(G['N']):
            for s in range(G['n']):
                if not np.allclose(R[w]@(Am[s]-np.eye(len(c))), R[G['rm'][s,w]]): ok=False
    print(name,G['N'],len(cells),sorted(len(c) for c in cells),'hom',ok,'maxmu',mu.max(),'%.1fs'%(time.time()-t))
