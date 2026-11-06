"""Re-search star paths using ONLY same-direction simultaneous steps (l(a*)-l(a) == l(b*)-l(b)),
the case of KL79 Thm 4.2 proved in-file (Lemma S). Also control in S_5/S_6 for Lemma S."""
import json,sys
from orbit import *
def path_same(y,z):
    n=len(y); start=(tuple(y),tuple(z)); par={start:None}; dq=deque([start])
    while dq:
        a,b=dq.popleft()
        st,g=status(list(a),list(b))
        if st!='open':
            p=[]; cur=(a,b)
            while par[cur] is not None: cur,i=par[cur]; p.append(i)
            return st,p[::-1],len(par)
        for i in range(1,n-1):
            a2=star(i,list(a))
            if a2 is None: continue
            b2=star(i,list(b))
            if b2 is None: continue
            if inv(a2)-inv(list(a))!=inv(b2)-inv(list(b)): continue
            nx=(tuple(a2),tuple(b2))
            if nx not in par: par[nx]=((a,b),i); dq.append(nx)
    return 'exhausted',None,len(par)
for f in sys.argv[1:]:
    D=json.load(open(f)); z=D['z']; new=[]
    for c in D['certs']:
        a,b=list(c['y']),list(z); mixed=0
        for i in c['path']:
            a2,b2=star(i,a),star(i,b)
            mixed+= (inv(a2)-inv(a))!=(inv(b2)-inv(b)); a,b=a2,b2
        st,p,sz=path_same(c['y'],z)
        print(f,'s',c['s'],'old path mixed steps',mixed,'| same-dir search:',st,'len',None if p is None else len(p),'orbit',sz)
        new.append(dict(c,path_samedir=p,verdict_samedir=st))
    D['certs']=new; json.dump(D,open(f,'w'))
