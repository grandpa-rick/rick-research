"""Full KL for S_n (small n) on one-line permutations; mu dict. Computed tool."""
from itertools import permutations
def inv(w): return sum(1 for i in range(len(w)) for j in range(i+1,len(w)) if w[i]>w[j])
def lmul(i,w): return tuple(i+1 if a==i else i if a==i+1 else a for a in w)
def L(w):
    pos={a:k for k,a in enumerate(w)}; return {i for i in range(1,len(w)) if pos[i+1]<pos[i]}
def bruhat_le(u,w):
    for k in range(1,len(u)):
        a=sorted(u[:k]); b=sorted(w[:k])
        if any(x>y for x,y in zip(a,b)): return False
    return True
def full_kl(n):
    W=sorted(permutations(range(1,n+1)),key=inv); ln={w:inv(w) for w in W}
    P={}; mu={}; mut={}
    for w in W:
        if ln[w]==0:
            P[(w,w)]=[1]; continue
        s=min(L(w)); v=lmul(s,w)
        below=[x for x in W if ln[x]<=ln[w] and bruhat_le(x,w)]
        for x in below:
            sx=lmul(s,x); c= s in L(x)
            a=P.get((sx,v),[]); b=P.get((x,v),[])
            col=[0]*(ln[w]+2)
            if not c:
                for k,e in enumerate(a): col[k+1]+=e
                for k,e in enumerate(b): col[k]+=e
            else:
                for k,e in enumerate(a): col[k]+=e
                for k,e in enumerate(b): col[k+1]+=e
            for zz,m in mut.get(v,[]):
                if s in L(zz) and (x,zz) in P:
                    sh=(ln[w]-ln[zz])//2
                    for k,e in enumerate(P.get((x,zz),[])): col[k+sh]-=m*e
            while col and col[-1]==0: col.pop()
            P[(x,w)]=col
            d=ln[w]-ln[x]
            if d%2==1 and len(col)>(d-1)//2 and col[(d-1)//2]: mu[(x,w)]=col[(d-1)//2]; mut.setdefault(w,[]).append((x,col[(d-1)//2]))
    return W,P,mu
def MU(mu,x,y):
    return mu.get((x,y),0) or mu.get((y,x),0)
