import sys, numpy as np
from core import *; import bic, modan
N=int(sys.argv[1]); R=bic.run(N); U=modan.setup(R,N)
Z,Av=R['Z'],R['Av']
def rideal(x,V):  # x.v  : matrix V@X
    X=U['unvec'](x); return np.array([U['vec']([(Y@Xb)%P for Y,Xb in zip(U['unvec'](v),X)]) for v in V])
Ds=[tuple(map(int,s.split(','))) for s in sys.argv[2:]]
for D in Ds:
    x=U['xD'](tuple(d-1 for d in D))
    QA=modan.basis(rideal(x,Av)); QB=modan.basis(rideal(x,Z.T))
    print('D',D,'dim xA',len(QA),'xB',len(QB))
    print('  cf xA',modan.cfactors(QA,U['ract'],N))
    print('  soc xA',modan.socle(QA,U['ract'],N))
    print('  cf xB',modan.cfactors(QB,U['ract'],N))
    print('  soc xB',modan.socle(QB,U['ract'],N))
    print('  soc xB/xA',modan.socle(QB,U['ract'],N,sub=QA))
