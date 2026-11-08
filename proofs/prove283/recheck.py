"""Independent consistency check of P_{x,z}: classical recursion with s in L(x)∩L(z) (c=1):
P_{x,z} = P_{sx,sz} + q P_{x,sz} - sum_{x<=y<sz, sy<y} mu(y,sz) q^{(l(z)-l(y))/2} P_{x,y},
each ingredient computed by Dyer on a DIFFERENT interval ([sx,sz], [x,sz], [x,y])."""
import sys,json
sys.path.insert(0,'/home/agent/projects/proofs/prove282')
from kl import P_interval
from interval import length
B=json.load(open('qbest.json')); k=int(sys.argv[1]); x,z=B[k]['x'],B[k]['z']
def lmul(s,w): return [s+1 if a==s else s if a==s+1 else a for a in w]
def ldes(s,w): return w.index(s+1)<w.index(s)
def trim(p):
    p=list(p)
    while len(p)>1 and p[-1]==0: p.pop()
    return p
n=len(x); S=[s for s in range(1,n) if ldes(s,x) and ldes(s,z)]; print('L(x)∩L(z)',S)
Pxz=trim(P_interval(x,z)[0][tuple(x)])
for s in S:
    sx,sz=lmul(s,x),lmul(s,z)
    A=trim(P_interval(sx,sz)[0][tuple(sx)])
    from cfg import bru
    if bru(x,sz): R,N,_=P_interval(x,sz); Bp=trim(R[tuple(x)])
    else: R,N,Bp={},0,[0]
    r=[0]*20
    for i,c in enumerate(A): r[i]+=c
    for i,c in enumerate(Bp): r[i+1]+=c
    lz=length(z); used=0
    for y,p in R.items():
        y=list(y)
        if y==sz or not ldes(s,y): continue
        d=length(sz)-length(y)
        if d%2==0: continue
        m=p[(d-1)//2] if len(p)>(d-1)//2 else 0
        if m:
            used+=1; Pxy=trim(P_interval(x,y)[0][tuple(x)]); sh=(lz-length(y))//2
            for i,c in enumerate(Pxy): r[i+sh]-=m*c
    print('s',s,'|[x,sz]|',N,'mu-terms',used,'recursion gives',trim(r),'direct',Pxz,'MATCH' if trim(r)==Pxz else 'MISMATCH',flush=True)
