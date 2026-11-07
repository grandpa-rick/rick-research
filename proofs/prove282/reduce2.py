"""reduce.explore with the Prop K premise tracked: flag 'forced' holds at a node if
 (nested Des(B) < Des(A) with |diff|>=2 for the current (A,B)) or the node came by an R-step from a forced node."""
import sys,json
sys.path.insert(0,'.')
from corner import evac
from reduce import rb, corners, key
def des(T):
    n=sum(map(len,T)); row={v:k for k,R in enumerate(T) for v in R}; return {i for i in range(1,n) if row[i+1]>row[i]}
def nested(a,b):
    A,B=des(a),des(b); return B<=A and len(A-B)>=2
def explore2(Ty,Tz):
    seen=set(); st=[(Ty,Tz,'',nested(Ty,Tz))]
    while st:
        a,b,h,forced=st.pop()
        forced = forced or nested(a,b)
        k=(key(a),key(b),forced)
        if k in seen: continue
        seen.add(k); n=sum(map(len,a))
        for (A,B,tag) in ((a,b,''),(evac(a),evac(b),'e')):
            for c in corners(A):
                ra,TA=rb(A,c); rbb,TB=rb(B,c)
                if ra<rbb and forced: return 'KILL',h+tag+'k%d'%c
                if ra==rbb: st.append((TA,TB,h+tag+'r%d,'%c,forced))
            ra=next(i for i,R in enumerate(A) if n in R); rz=next(i for i,R in enumerate(B) if n in R)
            if ra==rz:
                st.append(([[v for v in R if v!=n] for R in A if R!=[n]],[[v for v in R if v!=n] for R in B if R!=[n]],h+tag+'L,',False))
    return 'OPEN',None
if __name__=='__main__':
    from collections import Counter
    D=json.load(open('pfail.json')); c=Counter()
    for d in D:
        r=explore2(d['Px'],d['Pz']); c[(r[0], None if r[1] is None else r[1].count(','))]+=1
    print(c)
