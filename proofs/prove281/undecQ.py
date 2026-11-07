import sys,json; sys.path.insert(0,'.')
from common import *
from collections import Counter
n=15; lam=(5,4,3,3)
Px=[[1, 2, 6, 10, 15], [3, 7, 11, 14], [4, 8, 12], [5, 9, 13]]; Pz=[[1, 2, 3, 7, 15], [4, 5, 6, 11], [8, 9, 10], [12, 13, 14]]; U=[[1, 2, 6, 10, 14], [3, 7, 11, 15], [4, 8, 12], [5, 9, 13]]
C=Counter(); ex=None; T=syts(lam); print('#SYT',len(T))
for t in T:
    Q=[[k+1 for k in range(n) if t[k]==r] for r in range(len(lam))]
    y=rsk_inv(U,Q); z=rsk_inv(Pz,Q)
    c=bruhat_le(y,z); C[c]+=1
    if not c and ex is None: ex=Q; print('incomparable at Q',Q,flush=True)
print(C)
