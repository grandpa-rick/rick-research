# fast bitset version: (d)-pairs; classify stuck / doubly-stuck (all s in D_L(y): sx<x and x<=sy); gap histogram
import sys, collections, time
exec(open('q_cominuscule_scout.py').read().split('def boolean')[0])
def run(t,n,J,verbose=False):
    T=time.time(); C=Cox(cartan(t,n)); J=set(J); lam,els=quotient(C,J)
    L=list(els); N=len(L); ix={m:i for i,m in enumerate(L)}
    wr=[els[m][0] for m in L]; wd=[els[m][1] for m in L]; ln=[els[m][2] for m in L]
    # up-bitsets
    upb=[0]*N; 
    for a in range(N):
        b=0
        for c in range(N):
            if ln[c]>=ln[a] and C.le(wr[a],wr[c]): b|=1<<c
        upb[a]=b
    le=lambda a,b: (upb[a]>>b)&1
    # bad set: z in W^J s.t. zt <= y for some t in J -> for each y, set of z with some zt<=y
    zt=[[C.apply_word(wd[z]+[j],C.rho) for j in J] for z in range(N)]
    lsh=lambda i,a: ix[C.refl(i,L[a])] if L[a][i]!=0 else None  # left mult on W^J (None = stays in coset)
    hist=collections.Counter(); dst=collections.Counter(); nd=0
    for y in range(N):
        badz=0
        for z in range(N):
            if any(C.le(w,wr[y]) for w in zt[z]): badz|=1<<z
        DLy=[i for i in range(n) if wr[y][i]<0]
        for x in range(N):
            if not le(x,y): continue
            iv=upb[x] & ~0
            # interval = {z: x<=z<=y}
            ivs=0
            m=upb[x]
            while m:
                lb=m&-m; z=lb.bit_length()-1; m^=lb
                if le(z,y): ivs|=lb
            if ivs & badz: continue
            nd+=1; g=ln[y]-ln[x]
            stuck=all(wr[x][i]<0 for i in DLy)
            if stuck and g>0:
                hist[g]+=1
                if all(le(x,lsh(i,y)) for i in DLy): dst[g]+=1
    print(t+str(n),'K=',[i for i in range(n) if i not in J],'|W^J|',N,'(d)',nd,'stuck gaps',dict(hist),'doubly-stuck gaps',dict(dst),'%.0fs'%(time.time()-T),flush=True)
if __name__=='__main__':
    for t,n in [('F',4),('B',4),('C',4),('D',5),('A',5),('B',5),('D',6),('E',6)]:
        for k in range(n): run(t,n,[i for i in range(n) if i!=k])
