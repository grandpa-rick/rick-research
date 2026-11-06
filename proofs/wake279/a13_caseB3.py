"""n=14 (*)-failure pair: test F1-necessary conditions for mu(y,z)!=0 for ALL y = s x in the cell with
L(y) not subset L(x) (these have mu(y,x)=1, so a twin needs mu(y,z)>=1), across all left cells Q."""
exec(open('a13_caseB.py').read().split('\nn=14')[0])
import sys
n=14
def mu_possible(y,z):
    ly,lz=inv(y),inv(z)
    if (ly-lz)%2==0: return False,'parity'
    lo,hi=(y,z) if ly<lz else (z,y)
    if not bruhat_le(lo,hi): return False,'incomparable'
    for r in L(hi)-L(lo):
        if lmul(r,hi)!=lo: return False,'F1 r=%d'%r
    return True,''
for lam,(PX,PZ) in {(4,4,3,3):([[1,2,6,10],[3,7,11,14],[4,8,12],[5,9,13]],[[1,2,3,7],[4,5,6,11],[8,9,10],[12,13,14]]),
                    (5,3,3,3):([[1,2,6,10,14],[3,7,11],[4,8,12],[5,9,13]],[[1,2,3,7,11],[4,5,6],[8,9,10],[12,13,14]])}.items():
    kills=0; tot=0; ex=None; ys=set()
    for t in syts(lam):
        Q=[[k+1 for k in range(n) if t[k]==r] for r in range(len(lam))]
        x=rsk_inv(PX,Q); z=rsk_inv(PZ,Q); Lx=L(x); tot+=1
        for s in range(1,n):
            y=lmul(s,x)
            if not (L(y)-Lx): continue
            if rsk(y)[1]!=Q: continue
            ys.add(str(rsk(y)[0]))
            ok,why=mu_possible(y,z)
            if not ok:
                kills+=1; ex=ex or (s,why,Q); break
    print(lam,'cells',tot,'cells where some y=sx kills the twin:',kills,'distinct P(y):',len(ys),'example',ex)
