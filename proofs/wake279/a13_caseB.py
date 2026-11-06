"""For the n=14 (*)-failures, test the Case-B necessary condition of a twin (x=P, z=P'):
for every boundary pair (s,t) of L(x) (s in L(x), t=s+-1 notin L(x)), x'=*x must satisfy mu(x',z)>=1.
By KL (2.3.e): if z<x' then z = t x' (B1); else x' < z in Bruhat (B2). With >=2 boundary pairs B1 is impossible
(lengths), so need l(z) > l(x') and x' <= z Bruhat in EVERY left cell (fixed Q). Search Q violating this."""
import itertools
exec(open('syt_interior.py').read().split('for n in range')[0])
def rsk_inv(P,Q):
    P=[r[:] for r in P]; Q=[r[:] for r in Q]; n=sum(map(len,P)); w=[0]*n
    for k in range(n,0,-1):
        r=next(i for i,row in enumerate(Q) if row and row[-1]==k); Q[r].pop()
        x=P[r].pop()
        for i in range(r-1,-1,-1):
            row=P[i]; j=max(j for j,y in enumerate(row) if y<x); row[j],x=x,row[j]
        w[k-1]=x
        P=[r for r in P]; 
    return w
def rsk(w):
    P=[];Q=[]
    for k,x in enumerate(w,1):
        i=0
        while True:
            if i==len(P): P.append([x]);Q.append([k]);break
            row=P[i]; j=next((j for j,y in enumerate(row) if y>x),None)
            if j is None: row.append(x);Q[i].append(k);break
            row[j],x=x,row[j]; i+=1
    return P,Q
inv=lambda w: sum(1 for i in range(len(w)) for j in range(i+1,len(w)) if w[i]>w[j])
def lmul(i,w): # s_i w : swap values i,i+1
    return [i+1 if a==i else i if a==i+1 else a for a in w]
def L(w):
    pos={a:k for k,a in enumerate(w)}; return {i for i in range(1,len(w)) if pos[i+1]<pos[i]}
def bruhat_le(u,w):
    n=len(u)
    for k in range(1,n):
        a=sorted(u[:k]); b=sorted(w[:k])
        if any(x>y for x,y in zip(a,b)): return False
    return True
n=14
cases={(4,4,3,3):([[1,2,6,10],[3,7,11,14],[4,8,12],[5,9,13]],[[1,2,3,7],[4,5,6,11],[8,9,10],[12,13,14]]),
       (5,3,3,3):([[1,2,6,10,14],[3,7,11],[4,8,12],[5,9,13]],[[1,2,3,7,11],[4,5,6],[8,9,10],[12,13,14]])}
for lam,(PX,PZ) in cases.items():
    Qs=syts(lam); viol=0; first=None; tot=0
    for t in Qs:
        Q=[[k+1 for k in range(n) if t[k]==r] for r in range(len(lam))]
        x=rsk_inv(PX,Q); z=rsk_inv(PZ,Q)
        assert rsk(x)==(PX,Q) and rsk(z)==(PZ,Q)
        Lx=L(x); assert sorted(Lx)==[2,3,4,6,7,8,10,11,12]
        ok=True; why=None
        for s in Lx:
            for tt in (s-1,s+1):
                if 1<=tt<=n-1 and tt not in Lx:
                    c=[y for y in (lmul(s,x),lmul(tt,x)) if len(L(y)&{s,tt})==1]; assert len(c)==1; xp=c[0]
                    if not (inv(z)>inv(xp) and bruhat_le(xp,z)): ok=False; why=(s,tt,inv(x),inv(xp),inv(z)); break
            if not ok: break
        tot+=1
        if not ok:
            viol+=1; first=first or (Q,why)
        if viol>=1 and tot>200: break
    print(lam,'cells tested',tot,'cells refuting twin',viol,'example',first)
