"""Type A check of (*): no two distinct SYT P,P' of the same shape with {} != Des(P') subset int Des(P).
int D = {i in D : i-1 and i+1 (those in [1,n-1]) both in D}."""
import sys
def partitions(n,m=None):
    if m is None: m=n
    if n==0: yield (); return
    for k in range(min(n,m),0,-1):
        for p in partitions(n-k,k): yield (k,)+p
def syts(lam):
    n=sum(lam); rows=[0]*len(lam); res=[]
    def rec(k,pos):
        if k>n: res.append(tuple(pos)); return
        for r in range(len(lam)):
            if rows[r]<lam[r] and (r==0 or rows[r-1]>rows[r]):
                rows[r]+=1; rec(k+1,pos+[r]); rows[r]-=1
    rec(1,[]); return res
for n in range(2,int(sys.argv[1])+1):
    bad=0
    for lam in partitions(n):
        Ds={}
        for T in syts(lam):
            D=frozenset(i for i in range(1,n) if T[i]>T[i-1])  # i+1 strictly lower row
            Ds[D]=Ds.get(D,0)+1
        for A,ca in Ds.items():
            I=frozenset(i for i in A if all(j in A for j in (i-1,i+1) if 1<=j<=n-1))
            for B,cb in Ds.items():
                if B and B<=I and (A!=B or ca>1): bad+=1; print('VIOLATION',lam,sorted(A),sorted(B))
    print(n,'violations',bad)
