"""Step 1: for each open26 instance, search Q in SYT(lam) minimising l(z) (x=rsk_inv(Px,Q), z=rsk_inv(Pz,Q)).
Random hook-walk samples + superstandard choices + hill-climb via k<->k+1 swaps in Q."""
import sys,json,random
sys.path.insert(0,'/home/agent/projects/proofs/prove282')
from cfg import rsk_inv,bru,inv
from rskmod import rsk
random.seed(283)
def hookwalk(lam):
    n=sum(lam); shape=list(lam); T=[[0]*l for l in lam]
    for k in range(n,0,-1):
        cells=[(i,j) for i in range(len(shape)) for j in range(shape[i])]
        i,j=random.choice(cells)
        while True:
            arm=shape[i]-j-1; leg=sum(1 for r in range(i+1,len(shape)) if shape[r]>j)
            if arm+leg==0: break
            t=random.randrange(arm+leg)
            if t<arm: j=j+1+t
            else: i=i+1+(t-arm)
        T[i][j]=k; shape[i]-=1
    return T
def rowsuper(lam):
    T=[];c=1
    for l in lam: T.append(list(range(c,c+l))); c+=l
    return T
def colsuper(lam):
    T=[[0]*l for l in lam];c=1
    for j in range(lam[0]):
        for i in range(len(lam)):
            if lam[i]>j: T[i][j]=c;c+=1
    return T
def swaps(Q):
    pos={v:(i,j) for i,R in enumerate(Q) for j,v in enumerate(R)}; n=len(pos); out=[]
    for k in range(1,n):
        (a,b),(c,d)=pos[k],pos[k+1]
        if a!=c and b!=d:
            Q2=[R[:] for R in Q]; Q2[a][b]=k+1; Q2[c][d]=k; out.append(Q2)
    return out
def score(I,Q):
    x=rsk_inv(I['Px'],Q); z=rsk_inv(I['Pz'],Q); return inv(z),inv(x),x,z
def search(I,nsamp=300,nclimb=20):
    lam=I['lam']; best=None
    starts=[rowsuper(lam),colsuper(lam)]+[hookwalk(lam) for _ in range(nsamp)]
    scored=sorted(((score(I,Q)[0],Q) for Q in starts),key=lambda t:t[0])
    for s0,Q in scored[:nclimb]:
        cur=s0
        while True:
            nb=[(score(I,Q2)[0],Q2) for Q2 in swaps(Q)]
            m=min(nb,key=lambda t:t[0])
            if m[0]<cur: cur,Q=m
            else: break
        if best is None or cur<best[0]: best=(cur,Q)
    lz,lx,x,z=score(I,best[1])
    return dict(lz=lz,lx=lx,gap=lz-lx,bru=bru(x,z),Q=best[1],x=x,z=z,smin=scored[0][0])
if __name__=='__main__':
    D=json.load(open('/home/agent/projects/proofs/prove282/open26.json')); out=[]
    for k,I in enumerate(D):
        r=search(I); r['idx']=k; r['lam']=I['lam']; out.append(r)
        # sanity: RSK roundtrip
        assert [list(R) for R in rsk(r['z'])[0]]==I['Pz'] and [list(R) for R in rsk(r['x'])[0]]==I['Px']
        print(k,I['lam'],'lz',r['lz'],'lx',r['lx'],'gap',r['gap'],'bru',r['bru'],'(best sample',r['smin'],')',flush=True)
    json.dump(out,open('/home/agent/projects/proofs/prove283/qbest.json','w'))
