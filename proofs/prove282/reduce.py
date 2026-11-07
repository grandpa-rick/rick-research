"""Exact reductions of mu(T,T') (cell-independent, nested => T<T' in all cells):
 R-layer: corner c with rho_T(c)==rho_T'(c)  -> (T<-c, T'<-c) standardized, shape lam-c.
 L-layer: n in same row of T,T' -> delete n.
 kill: some corner with rho_T(c) < rho_T'(c)  (T must be below).  evac variants via w0 w w0."""
import sys,json
sys.path.insert(0,'.')
from corner import evac
def rb(T,r):
    T=[list(R) for R in T]; a=T[r].pop()
    for rr in range(r-1,-1,-1):
        row=T[rr]; j=max(j for j,b in enumerate(row) if b<a); row[j],a=a,row[j]
    T=[R for R in T if R]
    T=[[v-1 if v>a else v for v in R] for R in T]
    return a,T
def corners(T):
    lam=[len(R) for R in T]; return [r for r in range(len(lam)) if r==len(lam)-1 or lam[r]>lam[r+1]]
def key(T): return tuple(map(tuple,T))
def explore(Ty,Tz,maxn=8):
    seen=set(); st=[(Ty,Tz,'')]; leaves=[]
    while st:
        a,b,h=st.pop()
        k=(key(a),key(b))
        if k in seen: continue
        seen.add(k); n=sum(map(len,a))
        for (A,B,tag) in ((a,b,''),(evac(a),evac(b),'e')):
            for c in corners(A):
                ra,TA=rb(A,c); rbb,TB=rb(B,c)
                if ra<rbb: return 'KILL',h+tag+'k%d'%c,None
                if ra==rbb: st.append((TA,TB,h+tag+'r%d,'%c))
            ra=next(i for i,R in enumerate(A) if n in R); rz=next(i for i,R in enumerate(B) if n in R)
            if ra==rz:
                st.append(([[v for v in R if v!=n] for R in A if R!=[n]],[[v for v in R if v!=n] for R in B if R!=[n]],h+tag+'L,'))
        if n<=maxn: leaves.append((a,b,h))
    return 'OPEN',len(seen),leaves
if __name__=='__main__':
    from rskmod import rsk
    S=json.load(open('../wake282/sieve16.json'))
    for r in S:
        for e in r['elems']:
            if e['kind']=='ii' and e['muyz'] is None:
                Py=[list(R) for R in rsk(e['y'])[0]]
                res=explore(Py,r['Pz'])
                print(r['lam'],res[0],res[1], 'small leaves:',len(res[2]) if res[2] else 0, flush=True)
