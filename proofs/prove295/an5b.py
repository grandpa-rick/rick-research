import numpy as np
from core import *
import bic
R=bic.run(5)
Z,Av,B_,off,W=R['Z'],R['Av'],R['B_'],R['off'],R['W']
tot=Z.shape[0]
def restrict_zero(V,a):
    # subspace of rowspace(V) vanishing outside block a
    mask=np.ones(tot,bool); mask[off[a]:off[a]+len(B_[a])**2]=False
    K=null(V[:,mask].T)   # coefficients c with c^T V[:,mask]=0
    X=(K.T@V)%P
    return X[[i for i in range(X.shape[0])]] if K.shape[1] else np.zeros((0,tot),dtype=np.int64), K.shape[1]
for a in range(len(B_)):
    XB,kB=restrict_zero(Z.T.copy(),a); XA,kA=restrict_zero(Av.copy(),a)
    print(a,'B only-block',rank(XB) if kB else 0,'A only-block',rank(XA) if kA else 0)
