"""Interval-intrinsic KL via Dyer path formula (dyer.c) + brute-force S_n KL for validation."""
import sys,subprocess,itertools,random,json
from interval import covers_down, rankmat, geq_x, length
def interval_elems(x,z):
    Rx=rankmat(x); level={tuple(z)}; allv=set(level)
    while level:
        nxt=set(v for w in level for v in covers_down(w) if geq_x(v,Rx)); allv|=nxt; level=nxt
    return allv
def refl_order(n,kind='lex'):
    T=[(i,j) for i in range(n) for j in range(i+1,n)]
    if kind=='lex': return {t:k for k,t in enumerate(T)}
    if kind=='revlex': return {t:k for k,t in enumerate(sorted(T,key=lambda t:(-t[1],-t[0])))}
    if kind=='colex': return {t:k for k,t in enumerate(sorted(T,key=lambda t:(t[1],-t[0])))}
    if kind=='bad': random.seed(5); random.shuffle(T); return {t:k for k,t in enumerate(T)}
def P_interval(x,z,kind='lex',exe='./dyer'):
    E=sorted(interval_elems(x,z),key=lambda w:(length(w),w)); idx={w:i for i,w in enumerate(E)}
    n=len(x); ro=refl_order(n,kind); edges=[]
    for a in E:
        for i in range(n):
            for j in range(i+1,n):
                if a[i]<a[j]:
                    b=list(a); b[i],b[j]=b[j],b[i]; b=tuple(b)
                    if b in idx: edges.append((idx[a],idx[b],ro[(i,j)]))
    edges.sort(key=lambda e:(e[1],e[2]))
    inp=f"{len(E)} {len(edges)} {idx[tuple(z)]}\n"+" ".join(str(length(w)) for w in E)+"\n"+"\n".join(f"{a} {b} {l}" for a,b,l in edges)+"\n"
    out=subprocess.run([exe],input=inp,capture_output=True,text=True,check=True).stdout
    res={}
    for line in out.split('\n'):
        if line.strip():
            t=list(map(int,line.split())); res[E[t[0]]]=t[1:]
    return res,len(E),len(edges)
# ---------- brute force ----------
def brute(n):
    W=sorted(itertools.permutations(range(1,n+1)),key=length); Lw={w:length(w) for w in W}
    def leq(u,w):
        for k in range(1,n):
            a=sorted(u[:k]); b=sorted(w[:k])
            if any(p>q for p,q in zip(a,b)): return False
        return True
    def lmul(i,w): return tuple(i+1 if a==i else i if a==i+1 else a for a in w)  # s_i w
    def ldes(i,w): return w.index(i+1)<w.index(i)
    P={}; mu={}
    def padd(a,b,sh=0,c=1):
        r=list(a)+[0]*max(0,len(b)+sh-len(a))
        for k,v in enumerate(b): r[k+sh]+=c*v
        return r
    below={w:[u for u in W if Lw[u]<=Lw[w] and leq(u,w)] for w in W}
    for w in W:
        if Lw[w]==0: P[(w,w)]=[1]; continue
        s=next(i for i in range(1,n) if ldes(i,w)); v=lmul(s,w)
        for u in below[w]:
            if u==w: P[(u,w)]=[1]; continue
            su=lmul(s,u); c=1 if ldes(s,u) else 0
            r=[0]
            if (su,v) in P: r=padd(r,P[(su,v)],1-c)
            if (u,v) in P: r=padd(r,P[(u,v)],c)
            for y in below[v]:
                if y!=v and ldes(s,y) and (u,y) in P:
                    m=mu.get((y,v),0)
                    if m: r=padd(r,P[(u,y)],(Lw[w]-Lw[y])//2,-m)
            while len(r)>1 and r[-1]==0: r.pop()
            P[(u,w)]=r
            d=Lw[w]-Lw[u]
            if d%2==1: mu[(u,w)]=r[(d-1)//2] if len(r)>(d-1)//2 else 0
    return W,P,mu
if __name__=='__main__':
    for n in (4,5,6):
        W,P,mu=brute(n)
        inv=lambda w:tuple(sorted(range(1,n+1),key=lambda i:w[i-1]))
        bad=sum(1 for (u,w),p in P.items() if P[(inv(u),inv(w))]!=p); print('S',n,'pairs',len(P),'inverse-invariance failures',bad,'nontrivial mu',sum(1 for (u,w),m in mu.items() if m and length(w)-length(u)>1),'max mu',max(mu.values()))
        random.seed(n); tops=random.sample(W,min(len(W),30 if n<6 else 25))+[tuple(range(n,0,-1))]
        for kind in ('lex','revlex','colex','bad'):
            fails=0;checked=0
            for z in tops:
                x=tuple(range(1,n+1)) if random.random()<0.5 else random.choice([u for u in W if (u,z) in P])
                res,N,Ecount=P_interval(list(x),list(z),kind)
                for u,p in res.items():
                    q=P[(u,z)]; pp=list(p)
                    while len(pp)>1 and pp[-1]==0: pp.pop()
                    checked+=1
                    if pp!=q: fails+=1
            print('  dyer',kind,'checked',checked,'fails',fails,flush=True)
