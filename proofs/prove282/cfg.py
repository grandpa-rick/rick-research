"""Enumerate interior configs (T_y,T_z): same shape, nonempty Des T_z subset int Des T_y. Test Bruhat y<=z in canonical cells."""
import sys, random
from count_int import partitions, syt, des
def rsk_inv(P,Q):
    # inverse RSK: returns one-line w with insertion P, recording Q
    P=[list(r) for r in P]; Q=[list(r) for r in Q]; n=sum(map(len,P)); w=[0]*n
    for k in range(n,0,-1):
        r=next(i for i,R in enumerate(Q) if R and R[-1]==k)
        Q[r].pop(); a=P[r].pop()
        for rr in range(r-1,-1,-1):
            row=P[rr]; j=max(j for j,b in enumerate(row) if b<a)
            row[j],a=a,row[j]
        w[k-1]=a
        P=[R for R in P]; 
    return w
def bru(u,w):
    n=len(u)
    for k in range(1,n):
        a=sorted(u[:k]); b=sorted(w[:k])
        if any(x>y for x,y in zip(a,b)): return False
    return True
def inv(w): return sum(1 for i in range(len(w)) for j in range(i+1,len(w)) if w[i]>w[j])
def configs(n):
    def intr(A): return frozenset(i for i in A if (i-1 in A or i==1) and (i+1 in A or i==n-1))
    out=[]
    for lam in partitions(n):
        T=syt(lam); D=[des(t,n) for t in T]
        for i,a in enumerate(T):
            I=intr(D[i])
            for j,b in enumerate(T):
                if D[j] and D[j]<=I and D[j]!=D[i]: out.append((lam,a,b))
    return out
if __name__=='__main__':
    n=int(sys.argv[1]); C=configs(n); print('n',n,'configs',len(C))
