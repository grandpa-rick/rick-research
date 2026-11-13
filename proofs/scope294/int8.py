import sys
from itertools import permutations
from collections import Counter
from klfast import inv
n=8
def rm(w):
    M=[[0]*(n+1) for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,n+1): M[i][j]=M[i-1][j]+M[i][j-1]-M[i-1][j-1]+(w[i-1]==j)
    return M
def le(A,B): return all(A[i][j]>=B[i][j] for i in range(1,n+1) for j in range(1,n+1))
W=list(permutations(range(1,n+1)))
for xs,ys in [("21436587","41627385"),("21463587","41672385"),("24681357","46781235")]:
    x=tuple(map(int,xs)); y=tuple(map(int,ys)); X=rm(x); Y=rm(y); lx=inv(x); ly=inv(y)
    I=[w for w in W if lx<=inv(w)<=ly and le(X,rm(w)) and le(rm(w),Y)]
    prof=Counter(inv(w)-lx for w in I)
    print(xs,ys,"size",len(I),"rank profile",sorted(prof.items()),"coatoms-atoms",prof[ly-lx-1]-prof[1])
