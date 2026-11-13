import numpy as np
from core import *
import bic
from flint import nmod_mat
R=bic.run(5)
Z,Av,B_,off,W=R['Z'],R['Av'],R['B_'],R['off'],R['W']
tot=Z.shape[0]; a=2; s=slice(off[a],off[a]+100)
def only(V):
    mask=np.ones(tot,bool); mask[s]=False
    K=null(V[:,mask].T); return (K.T@V%P)[:,s]
XB=only(Z.T.copy()); XA=only(Av.copy())
def rref(X):
    M=tomat(X); M,r=M.rref(); E=np.array(M.entries(),dtype=np.int64).reshape(X.shape); return E[:r]
RA=rref(XA); RB=rref(XB)
def lift(x): return np.where(x>P//2,x-P,x)
print('A-only rref rows'); 
for r in RA: print(lift(r).reshape(10,10).tolist())
# reduce B rows mod RA
piv=[np.nonzero(r)[0][0] for r in RA]
for r in RB:
    x=r.copy()
    for pr,pc in zip(RA,piv): x=(x-x[pc]*pr)%P
    if x.any(): print('B mod A:',lift(x).reshape(10,10).tolist())
print([W[k] for k in B_[a]])
