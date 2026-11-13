import sys, numpy as np, itertools
import blocksearch as bs
from flint import nmod_mat
P=bs.P
src=open('blocksearch.py').read()
# monkeypatch: re-run internals for one weight and print excess element
def run(n,N,mu):
    import types
    g={}
    code=src.split("if __name__")[0]
    code=code.replace("        out[mu]=r1-r2","        out[mu]=(R1,R2,Mu,W,F)")
    exec(code,g)
    out={}
    res=g['run'](n,N,only=[mu])
    return res
n,N=map(int,sys.argv[1:3]); mu=tuple(map(int,sys.argv[3].split(',')))
code=open('blocksearch.py').read().split("if __name__")[0].replace("        out[mu]=r1-r2","        out[mu]=(R1,R2,Mu,W,F)").replace("    print(n,N,'total single-weight excess',sum(out.values()))","    return out")
g={}; exec(code,g)
R1,R2,Mu,W,F=g['run'](n,N,only=[mu])[mu]
# column keys: reconstruct (y,t) order
keys=[]
for y in Mu:
    col=F[:,y]
    for t in np.unique(col): keys.append((y,t))
def rref(X):
    M=nmod_mat(X.shape[0],X.shape[1],[int(x)%P for x in X.ravel()],P); E,r=M.rref()
    return np.array(E.entries(),dtype=np.int64).reshape(X.shape)[:r]
E2=rref(R2); piv=[int(np.nonzero(e)[0][0]) for e in E2]
E1=rref(R1)
lift=lambda x: x-P if x>P//2 else x
best=None
for r in E1:
    x=r.copy()
    for pr,pc in zip(E2,piv): x=(x-x[pc]*pr)%P
    if x.any():
        nz=np.nonzero(x)[0]
        if best is None or len(nz)<len(np.nonzero(best)[0]): best=x
x=best
print('excess element on weight',mu,': v_src -> sum coeff v_tgt')
from collections import defaultdict
m=defaultdict(list)
for j in np.nonzero(x)[0]:
    y,t=keys[j]; m[W[y]].append((lift(int(x[j])),W[t]))
for s,l in m.items(): print(' ',''.join(map(str,s)),'->',' '.join(f"{c:+d}*{''.join(map(str,t))}" for c,t in l))
