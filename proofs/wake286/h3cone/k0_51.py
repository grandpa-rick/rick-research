import sys; sys.path.insert(0,'/home/agent/projects/proofs/wake279')
import json, numpy as np
from cones import words, dominant
from scipy.spatial import ConvexHull
cells=json.load(open('cells5.json'))
A=[np.array(a,float) for a in cells[0]['A']]; B=[a.T for a in A]
for L in [4,6,8,10]:
    S=[]
    for w in words(3,L):
        P=np.eye(5)
        for s in w: P=B[s]@P
        r=dominant(P)
        if r is None: continue
        S.append(r[0]/r[0].sum())
    S=np.unique(np.round(np.array(S),9),axis=0)
    for _ in range(2):
        S=np.vstack([S]+[ (b@S.T).T for b in B]); S=S[S.sum(1)>1e-12]; S=S/S.sum(1,keepdims=True)
        S=np.unique(np.round(S,9),axis=0)
    h=ConvexHull(S[:,:4]); V=S[h.vertices]
    print('L',L,'perron+images',len(S),'extreme rays',len(V))
V=V/V.max(1,keepdims=True)
print(np.round(V[np.argsort(V[:,4])],4))
