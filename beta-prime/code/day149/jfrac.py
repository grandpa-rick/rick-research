import pickle
from fractions import Fraction as Q
H=pickle.load(open('H16.pkl','rb'))
def ev(A,e): return sum(c*e[0]**m[0]*e[1]**m[1]*e[2]**m[2] for m,c in A.items())
def hankel(seq,r,shift=0):
    M=[[Q(seq[i+j+shift]) for j in range(r)] for i in range(r)]
    # det
    n=r; det=Q(1)
    A=[row[:] for row in M]
    for c in range(n):
        p=None
        for rr in range(c,n):
            if A[rr][c]!=0: p=rr;break
        if p is None: return Q(0)
        if p!=c: A[c],A[p]=A[p],A[c]; det=-det
        det*=A[c][c]
        inv=Q(1)/A[c][c]
        for rr in range(c+1,n):
            f=A[rr][c]*inv
            if f: A[rr]=[a-f*b for a,b in zip(A[rr],A[c])]
    return det
def jfrac(seq,K):
    """return b_i, lambda_i of the J-fraction via Hankel dets"""
    D=[hankel(seq,r,0) for r in range(0,K+2)]
    D1=[hankel(seq,r,1) for r in range(0,K+2)]
    lam=[]; b=[]
    for k in range(K):
        if k==0: b.append(Q(seq[1],seq[0]))
        else:
            if D[k]==0 or D[k+1]==0: break
            b.append(D1[k+1]/D[k+1]-D1[k]/D[k])
        if k>=1:
            if D[k]==0: break
            lam.append(D[k+1]*D[k-1]/D[k]**2)
    return b,lam
for pt in [(0,0,0),(1,0,0),(0,1,0),(2,1,1)]:
    seq=[ev(H[n],pt) for n in range(17)]
    b,lam=jfrac(seq,7)
    print(pt)
    print("   b     =",b)
    print("   lambda=",lam)
