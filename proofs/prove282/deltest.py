"""Full-KL control: (a) Layer Lemma for K=S\\{s_k}, all k; (b) Deletion Prop: same left cell, n in same row of P => mu(y,z)=mu(y\\n,z\\n)."""
import sys; sys.path.insert(0,'../prove281'); sys.path.insert(0,'.')
from klperm import full_kl,L,MU,lmul
from rskmod import rsk
n=int(sys.argv[1]); W,P,mu=full_kl(n)
Wm,Pm,mum=full_kl(n-1)
# (b)
cells={}
for w in W: cells.setdefault(rsk(w)[1],[]).append(w)
tot=bad=nz=0
for C in cells.values():
    for y in C:
        Py=rsk(y)[0]; ry=next(i for i,R in enumerate(Py) if n in R)
        for z in C:
            if z<=y: continue
            Pz=rsk(z)[0]; rz=next(i for i,R in enumerate(Pz) if n in R)
            if ry!=rz: continue
            tot+=1; a=tuple(v for v in y if v!=n); b=tuple(v for v in z if v!=n)
            m1=MU(mu,y,z); m2=MU(mum,a,b); nz+=(m1!=0)
            if m1!=m2: bad+=1
print('n',n,'deletion pairs',tot,'nonzero mu',nz,'mismatch',bad)
# (a) Young layers
def std(s):
    t=sorted(s); r={v:i+1 for i,v in enumerate(t)}; return tuple(r[v] for v in s)
bad2=tot2=0
for k in range(1,n):
    for y in W:
        for z in W:
            if z<=y: continue
            if set(y[:k])!=set(z[:k]): continue
            tot2+=1
            # product: mu = mu(prefix) if suffix equal, mu(suffix) if prefix equal, else 0
            p1,p2=std(y[:k]),std(z[:k]); s1,s2=std(y[k:]),std(z[k:])
            def m(a,b):
                if len(a)<=1: return 0
                if len(a)==n-1: return MU(mum,a,b)
                Wk,Pk,muk=full_kl.cache[len(a)] if hasattr(full_kl,'cache') and len(a) in full_kl.cache else (None,None,None)
                return None
            if p1!=p2 and s1!=s2: pred=0
            else: pred=None
            if pred==0 and MU(mu,y,z)!=0: bad2+=1
print('n',n,'right-layer pairs (k any)',tot2,'both-factors-differ kills violated',bad2)
