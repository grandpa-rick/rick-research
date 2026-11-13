import sys, numpy as np, itertools
from core import *
import bic
def run(N,R=None):
    R=R or bic.run(N); Z,Av,B_,off,G=R['Z'],R['Av'],R['B_'],R['off'],R['G']
    Pb=[[mat(g)[np.ix_(b,b)] for b in B_] for g in G]
    I=[np.eye(len(b),dtype=np.int64) for b in B_]
    def unvec(v): return [v[off[a]:off[a]+len(b)**2].reshape(len(b),len(b)) for a,b in enumerate(B_)]
    def vec(Ms): return np.concatenate([M.ravel() for M in Ms])%P
    def w0(J,bar):  # block matrices of pi_{w0(J)} (bar: 1-pi), right-action composition = matrix product reversed
        X=[i.copy() for i in I]
        for _ in range(N*(N-1)//2):
            for j in J:
                X=[ (( (Ii-Pj) if bar else Pj) @ Xb)%P for Xb,Pj,Ii in zip(X,Pb[j],I)]
        return X
    res={}; sA=sB=0
    for r in range(N):
        for D in itertools.combinations(range(N-1),r):
            Dc=[j for j in range(N-1) if j not in D]
            X1=w0(D,True); X2=w0(Dc,False)
            x=[(b@a)%P for a,b in zip(X1,X2)]   # x = pibar_{w0 D} then pi_{w0 Dc}  (right action order)
            # xA, xB : right ideal: x then y  -> matrix y@x
            def mul(V): return np.array([vec([(Y@xb)%P for Y,xb in zip(unvec(v),x)]) for v in V])
            dA=rank(mul(Av)); dB=rank(mul(Z.T))
            sA+=dA; sB+=dB
            if dB!=dA or dA: res[tuple(d+1 for d in D)]=(dA,dB)
    print(N,'sumA',sA,'sumB',sB)
    for D,(a,b) in res.items():
        print('  D',D,'dimxA',a,'dimxB',b,'defect',b-a)
    return res
if __name__=='__main__':
    for N in map(int,sys.argv[1:]): run(N)
