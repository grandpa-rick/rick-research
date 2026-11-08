"""Brute-force KL via classical recursion on the full group, compare with interval method."""
import itertools, random, sys
from kl import *

def brute(n):
    W=list(itertools.permutations(range(1,n+1)))
    L={w:length(w) for w in W}
    W.sort(key=lambda w:L[w])
    le={}
    for u in W:
        for v in W: le[(u,v)]=leq(u,v)
    P={}
    for w in W:
        lw=L[w]
        if lw==0:
            P[(w,w)]=[1]; continue
        # left descent s: s w < w ; v = s w
        i=ldes(w)[0]; v=lswap(w,i); lv=lw-1
        # C'_s C'_v = C'_w + sum_{z<v, sz<z} mu(z,v) C'_z
        mus=[]
        for zz in W:
            if L[zz]<lv and le[(zz,v)] and i in ldes(zz):
                p=P[(zz,v)]; d=(lv-L[zz]-1)
                if d%2==0 and len(p)>d//2 and p[d//2]!=0: mus.append((zz,p[d//2]))
        for y in W:
            if not le[(y,w)]: continue
            sy=lswap(y,i)
            ly=L[y]
            # P_{y,w} = q^{1-c} P_{sy,v} + q^c P_{y,v} - sum mu q^{(l(w)-l(z))/2} P_{y,z}, c=1 if sy<y
            c=1 if L[sy]<ly else 0
            def g(a,b): return P.get((a,b),[]) if le[(a,b)] else []
            res=padd(pmul([0]*(1-c)+[1],g(sy,v)), pmul([0]*c+[1],g(y,v)))
            for zz,m in mus:
                if le[(y,zz)]:
                    e=(lw-L[zz])//2
                    res=padd(res,pmul([0]*e+[-m],P[(y,zz)]))
            P[(y,w)]=res
    return W,le,P

for n in (4,5):
    W,le,P=brute(n)
    bad=0; cnt=0
    tops=W if n==4 else W
    for z in tops:
        for x in W:
            if le[(x,z)]:
                Q=kl_interval(x,z)
                cnt+=1
                if Q[x]!=P[(x,z)]: bad+=1; print('MISMATCH',x,z,Q[x],P[(x,z)])
                # also all y in interval
                for y,p in Q.items():
                    if p!=P[(y,z)]: bad+=1
        if n==5 and cnt>3000: break
    print('n',n,'interval-method pairs checked',cnt,'mismatches',bad,flush=True)
    if n==4:
        print('P_{1324,3412}',P[((1,3,2,4),(3,4,1,2))],'P_{2143,4231}',P[((2,1,4,3),(4,2,3,1))])
        assert all(P[((1,2,3,4),w)][0]==1 for w in W)
        print('nontrivial S4:',[(x,z,p) for (x,z),p in P.items() if len(p)>1])
