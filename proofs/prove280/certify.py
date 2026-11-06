"""Produce explicit star-path certificates; check no step has pair in same <s_i,s_i+1> left coset."""
from orbit import *
import json
def path_search(y,z):
    n=len(y); start=(tuple(y),tuple(z)); par={start:None}; dq=deque([start])
    while dq:
        a,b=dq.popleft()
        st,g=status(list(a),list(b))
        if st!='open':
            p=[]; cur=(a,b)
            while par[cur] is not None: cur,i=par[cur]; p.append(i)
            return st,p[::-1],(a,b)
        for i in range(1,n-1):
            a2=star(i,list(a)); 
            if a2 is None: continue
            b2=star(i,list(b))
            if b2 is None: continue
            nx=(tuple(a2),tuple(b2))
            if nx not in par: par[nx]=((a,b),i); dq.append(nx)
def same_coset(i,a,b):
    # b = u a with u in <s_i,s_{i+1}>  <=> a,b agree outside positions of values i,i+1,i+2 and those sets equal
    S={i,i+1,i+2}
    return all((p in S)==(q in S) and (p==q or p in S) for p,q in zip(a,b))
import sys
which=sys.argv[1] if len(sys.argv)>1 else '1'
X,Z={'1':(PX,PZ),'2':(PX2,PZ2),'3':([[1,4,8,12],[2,5,9,13],[3,6,10,14],[7,11]],[[1,3,4,5],[2,7,8,9],[6,11,12,13],[10,14]]),'4':([[1,4,8,12],[2,5,9,13],[3,6,10,14],[7],[11]],[[1,3,4,5],[2,7,8,9],[6,11,12,13],[10],[14]])}[which]
Q=[[1,2,3,4],[5,6,7,14],[8,9,10],[11,12,13]] if which=='1' else json.loads(sys.argv[2])
x=rsk_inv(X,Q); z=rsk_inv(Z,Q); assert rsk(x)==(X,Q) and rsk(z)==(Z,Q)
out=[]
for s,y in star_images(x):
    st,p,end=path_search(y,z)
    a,b=list(y),list(z); coset=False
    for i in p:
        if same_coset(i,a,b): coset=True
        a,b=star(i,a),star(i,b)
    assert (tuple(a),tuple(b))==end
    print('s=%d'%s,'x\'=',y,'verdict',st,'path',p,'len',len(p),'same-coset step?',coset,'end lengths',inv(a),inv(b))
    out.append(dict(s=s,y=y,z=z,verdict=st,path=p))
json.dump(dict(Q=Q,x=x,z=z,certs=out),open('certs_%s.json'%which,'w'))
