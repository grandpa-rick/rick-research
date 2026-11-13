import numpy as np
from core import *
import bic
R=bic.run(5)
Z,Av,B_,off=R['Z'],R['Av'],R['B_'],R['off']
for a,b in enumerate(B_):
    s=slice(off[a],off[a]+len(b)**2)
    print(a,len(b),'A_a',rank(Av[:,s]),'B_a',rank(Z.T[:,s]))
# pairs
import itertools
for a,c in itertools.combinations(range(len(B_)),2):
    s=np.r_[off[a]:off[a]+len(B_[a])**2, off[c]:off[c]+len(B_[c])**2]
    rA=rank(Av[:,s]); rB=rank(Z.T[:,s])
    if rA!=rB: print('pair',a,c,rA,rB)
