import sys
from itertools import combinations
def partitions(n,m=None):
    if m is None: m=n
    if n==0: yield (); return
    for k in range(min(n,m),0,-1):
        for p in partitions(n-k,k): yield (k,)+p
def syt(lam):
    n=sum(lam); res=[]
    def rec(T,k):
        if k>n: res.append(tuple(map(tuple,T))); return
        for r in range(len(lam)):
            if len(T[r])<lam[r] and (r==0 or len(T[r-1])>len(T[r])):
                T[r].append(k); rec(T,k+1); T[r].pop()
    rec([[] for _ in lam],1); return res
def des(T,n):
    row={v:k for k,R in enumerate(T) for v in R}; return frozenset(i for i in range(1,n) if row[i+1]>row[i])
if __name__=='__main__':
 for n in range(4,int(sys.argv[1])+1):
     def intr(A): return frozenset(i for i in A if (i-1 in A or i==1) and (i+1 in A or i==n-1))
     tot=0; shapes=[]
     for lam in partitions(n):
         D=[des(T,n) for T in syt(lam)]
         Ds=set(D); 
         c=sum(1 for a in Ds for b in Ds if b and b<=intr(a) and b!=a)
         if c: shapes.append((lam,c)); tot+=c
     print(n,tot,shapes[:8])
