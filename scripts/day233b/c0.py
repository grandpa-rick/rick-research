from eng import *
import time
# C0a: sum_A c_A X_A = e_k (E_k(1)=e_k), N<=7, at s generic, t generic
ctx = Ctx(rng.integers(2,p), rng.integers(2,p), 3)
ok=True
for N in range(1,8):
    for k in range(0,N+1):
        d = to_ebasis(ctx, k, N, lambda xb,m: evalE(ctx,[k],xb,m,base_one)) if k else None
        if k and any(any(v) for mu,v in d.items() if mu!=(k,)) or (k and d[(k,)]!=[1,0,0]): ok=False; print("E_k(1)!=e_k",N,k,d)
print("C0a E_k(1)=e_k N<=7:", ok)
# C0b: commutativity: full subset recursion in all orders, no e_last shortcut, n<=6
def estar_full(ctx, seq, n):
    return to_ebasis(ctx, n, n, lambda xb,m: evalE(ctx, list(seq), xb, m, base_one))
ok=True; cnt=0
for n in range(2,7):
    for lam in partitions(n):
        perms=set(itertools.permutations(lam))
        ref=None
        for q in perms:
            d=estar_full(ctx,q,n); cnt+=1
            if ref is None: ref=d
            elif d!=ref: ok=False; print("noncomm",lam,q)
        if estar(ctx,lam)!=ref: ok=False; print("shortcut mismatch",lam)
print("C0b commutativity + shortcut, n<=6:", ok, cnt)
# C0c Hikita Pieri e1*er=(1-s)[r+1]e_{r+1}+s e1 er at random s,t (K=1)
s0,t0=int(rng.integers(2,p)),int(rng.integers(2,p)); c1=Ctx(s0,t0,1); ok=True
for r in range(1,7):
    d=estar(c1,(r,1)); br=sum(pow(t0,i,p) for i in range(r+1))%p
    exp={(r+1,):(1-s0)*br%p, (r,1) if r>1 else (1,1):s0%p}
    for mu,v in d.items():
        if v[0]!=exp.get(mu,0)%p: ok=False; print("pieri",r,mu)
print("C0c Hikita e1*er:", ok)
# negative control: wrong t in c_A should break Pieri
c2=Ctx(s0,t0+1,1); d=estar(c2,(2,1)); br=(1+t0+t0*t0)%p
print("C0c neg control fires:", d[(3,)][0]!=(1-s0)*br%p)
