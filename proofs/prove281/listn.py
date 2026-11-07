"""All (*)-violating (lambda,A) at n and all candidate (Px,Pz): Des Px=A, {}!=Des Pz subset int A. Kostka-dominance list + direct SYT enumeration."""
import sys; sys.path.insert(0,'.')
from common import syts
n=int(sys.argv[1])
def parts(n,m=None):
    if m is None: m=n
    if n==0: yield []; return
    for k in range(min(n,m),0,-1):
        for p in parts(n-k,k): yield [k]+p
def comp(cuts):
    c=sorted(cuts); prev=0; out=[]
    for i in c: out.append(i-prev); prev=i
    out.append(n-prev); return sorted(out,reverse=True)
def conj(a): return [sum(1 for x in a if x>=k) for k in range(1,(a[0] if a else 0)+1)]
def dom(b,a):
    sb=sa=0
    for k in range(max(len(a),len(b))):
        sb+= b[k] if k<len(b) else 0; sa+= a[k] if k<len(a) else 0
        if sb>sa: return False
    return True
intr=lambda A:frozenset(i for i in A if all(j in A for j in (i-1,i+1) if 1<=j<=n-1))
viol=[]
for m in range(1,2**(n-1)-1):
    A=frozenset(i for i in range(1,n) if m>>(i-1)&1); I=intr(A)
    if not I: continue
    al=comp(I); be=comp(set(range(1,n))-A)
    for lam in parts(n):
        if dom(be,conj(lam)) and dom(al,lam): viol.append((tuple(lam),A))
print('n',n,'violating (lambda,A):',len(viol))
shapes=sorted(set(l for l,A in viol),reverse=True)
def tab(t,lam): return [[k+1 for k in range(n) if t[k]==r] for r in range(len(lam))]
def des(T):
    row={v:r for r,R in enumerate(T) for v in R}; return frozenset(i for i in range(1,n) if row[i+1]>row[i])
out=[]
for lam in shapes:
    Ts=[tab(t,lam) for t in syts(lam)]; D=[des(T) for T in Ts]
    for l2,A in viol:
        if l2!=lam: continue
        I=intr(A)
        X=[T for T,d in zip(Ts,D) if d==A]; Z=[T for T,d in zip(Ts,D) if d and d<=I]; U=[T for T,d in zip(Ts,D) if d>A]
        print(lam,'A',sorted(A),'int',sorted(I),'#Px',len(X),'#Pz',len(Z),'#Des>A',len(U),flush=True)
        out.append(dict(lam=lam,A=sorted(A),I=sorted(I),X=X,Z=Z,U=U))
import json; json.dump(out,open('viol%d.json'%n,'w'))
