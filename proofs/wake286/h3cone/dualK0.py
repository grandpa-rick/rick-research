import sys; sys.path.insert(0,'/home/agent/projects/proofs/wake279')
import json, numpy as np, itertools
from cones import testA
from scipy.spatial import ConvexHull
cells=json.load(open('cells5.json'))
for ci in [3,0]:
    A=[np.array(a,float) for a in cells[ci]['A']]
    reached,npf,S=testA(A,L=8)
    S=np.array(S); 
    # extreme rays: project to sum=1 slice
    P=S/S.sum(1,keepdims=True)
    rk=np.linalg.matrix_rank(P-P[0])
    print('cell',ci,'perron',npf,'forced vecs',len(S),'affine rank of slice',rk,'reached',reached)
    if rk==4:
        Q=P[:, :4]
        h=ConvexHull(Q); ext=sorted(set(h.vertices))
        for i in ext: print('   ext', np.round(S[i]/S[i].max(),6))
