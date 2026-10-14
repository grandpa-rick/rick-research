from q442_check import *
import time
grid=[(1,l,n) for l in (0,1,2) for n in range(1,8)]+[(2,l,n) for l in (0,1) for n in range(1,6)]+[(3,0,n) for n in range(1,4)]
res=defaultdict(lambda:[0,0])
for (k,l,n) in grid:
    w=2*l+2; t0=time.time()
    Gt=G(k,l,n)
    Ainf=chains(k,n,w,E(k),False); A=chains(k,n,w,E(k),True); B=chains(k,n,w,Bcl(k,w),True)
    mindeg=min(kk[-1] for kk in Gt) if Gt else 0
    c0=coeff_t(Gt,0); c1=at_t1(Gt)
    chk={'tdeg>=0':mindeg>=0,'c0=Ainf':c0==Ainf,'c1=A-B':c1==add(A,B,-1),'eq9 det=Ainf':detf(k,n)==Ainf,
         'Thm14(1) n<=w => A=Ainf':(A==Ainf) if n<=w else True,
         'tfree<=>n<w':((max(kk[-1] for kk in Gt)==0)==(n<w))}
    for c,v in chk.items(): res[c][0]+=v; res[c][1]+=1
    bad=[c for c,v in chk.items() if not v]
    print((k,l,n),'w',w,'nmon',len(Ainf),'FAIL' if bad else 'ok',bad,round(time.time()-t0,1),flush=True)
for c,v in res.items(): print(c,f"{v[0]}/{v[1]}")
