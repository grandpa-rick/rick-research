"""INDEPENDENT replay (fresh code): mu(y,z)=0 for the (5,5,3,3) undecided (ii) instances.
Steps: (1) y,z in the given cell share the position of value v (v=n or 1); (2) delete v -> y',z' (Layer Lemma: P_{y,z}=P_{y',z'});
(3) y',z' have equal recording tableau (same left cell of S_{n-1}); (4) in cell Q*, y''=(P(y'),Q*), z''=(P(z'),Q*) is a mu=0 endpoint."""
import json
def rsk(w):
    P=[];Q=[]
    for t,a in enumerate(w,1):
        r=0
        while True:
            if r==len(P): P.append([a]);Q.append([t]);break
            R=P[r]; j=next((j for j,b in enumerate(R) if b>a),None)
            if j is None: R.append(a);Q[r].append(t);break
            R[j],a=a,R[j]; r+=1
    return P,Q
def unrsk(P,Q):
    P=[r[:] for r in P]; Q=[r[:] for r in Q]; n=sum(map(len,P)); w=[0]*n
    for t in range(n,0,-1):
        r=[i for i,R in enumerate(Q) if R and R[-1]==t][0]; Q[r].pop(); a=P[r].pop()
        for rr in range(r-1,-1,-1):
            R=P[rr]; j=max(j for j,b in enumerate(R) if b<a); R[j],a=a,R[j]
        w[t-1]=a
    return w
def length(w): return sum(w[i]>w[j] for i in range(len(w)) for j in range(i+1,len(w)))
def leq(u,w):  # Bruhat via rank matrices
    n=len(u)
    for i in range(n):
        for j in range(1,n+1):
            if sum(1 for k in range(i+1) if u[k]>=j) > sum(1 for k in range(i+1) if w[k]>=j): return False
    return True
def Lset(w):
    p={a:i for i,a in enumerate(w)}; return {i for i in range(1,len(w)) if p[i+1]<p[i]}
def superstd(lam):
    T=[];k=0
    for m in lam: T.append(list(range(k+1,k+m+1))); k+=m
    return T
import sys
C=json.load(open(sys.argv[1] if len(sys.argv)>1 else 'undec16_ii.json'))
for c in C:
    if c['res'] is None: print(c['lam'],'no certificate'); continue
    tr=c['res'][1]; side,k,_=tr[0][:3]; Qstar=[list(r) for r in tr[1][2]]
    lam=c['lam']; Q0=superstd(lam)
    y=unrsk(c['Py'],Q0); z=unrsk(c['Pz'],Q0); n=len(y)
    assert rsk(y)==(c['Py'],Q0) and rsk(z)==(c['Pz'],Q0)
    pass
    v= n if k==n-1 else 1; assert side=='L' and k in (1,n-1)
    assert y.index(v)==z.index(v), 'layer'
    dl=lambda w:[a-(1 if v==1 else 0) for a in w if a!=v]
    y1,z1=dl(y),dl(z)
    (Py1,Qy1),(Pz1,Qz1)=rsk(y1),rsk(z1)
    assert Qy1==Qz1,'same cell'
    assert length(y)-length(z)==length(y1)-length(z1)
    y2=unrsk(Py1,Qstar); z2=unrsk(Pz1,Qstar)
    g=length(z2)-length(y2)
    inc=not leq(y2,z2) and not leq(z2,y2)
    print(lam,'delete',v,'| cell-check ok | reduced gap',g,'| y2,z2 incomparable:',inc,'| y2<=z2:',leq(y2,z2), '| L(y2)>L(z2):',Lset(y2)>Lset(z2))

# ---- explicit right-star path from realised cell Q(y1) to Q* (simultaneous on y1,z1), fresh code ----
from collections import deque
def Rset(w): return {i for i in range(1,len(w)) if w[i-1]>w[i]}
def rmul(w,i): w=w[:]; w[i-1],w[i]=w[i],w[i-1]; return w
def rstar(w,i):  # star for {s_i,s_{i+1}} on the right; None if w not in D_R
    R=Rset(w); a,b=(i in R),(i+1 in R)
    if a==b: return None
    for j in (i,i+1):
        u=rmul(w,j); Ru=Rset(u)
        if (i in Ru)!=(i+1 in Ru) and ((i in Ru)!=a): return u
    return None
for c in C:
    if c['res'] is None: continue
    tr=c['res'][1]; side,k,_=tr[0][:3]; Qstar=[list(r) for r in tr[1][2]]
    lam=c['lam']; Q0=superstd(lam); y=unrsk(c['Py'],Q0); z=unrsk(c['Pz'],Q0); n=len(y)
    v= n if k==n-1 else 1
    dl=lambda w:[a-(1 if v==1 else 0) for a in w if a!=v]
    y1,z1=dl(y),dl(z); target=unrsk(rsk(y1)[0],Qstar)
    seen={tuple(y1):None}; dq=deque([(y1,z1)]); found=None
    while dq:
        a,b=dq.popleft()
        if a==target: found=(a,b); break
        for i in range(1,len(a)-1):
            a2=rstar(a,i); b2=rstar(b,i)
            if a2 is None or b2 is None: continue
            assert Rset(a)==Rset(b)
            if tuple(a2) not in seen: seen[tuple(a2)]=(tuple(a),i); dq.append((a2,b2))
    a,b=found; path=[]; t=tuple(a)
    while seen[t] is not None: path.append(seen[t][1]); t=seen[t][0]
    assert rsk(a)[0]==rsk(y1)[0] and rsk(b)[0]==rsk(z1)[0] and rsk(a)[1]==Qstar==rsk(b)[1]
    print(lam,'right-star path length',len(path),'reaches Q*; endpoint incomparable:',not leq(a,b) and not leq(b,a))
