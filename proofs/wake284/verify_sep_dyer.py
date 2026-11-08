"""Independent checks of the S_7 separator pairs.
Method B: prove283/kl.py brute(7) (left-multiplication KL recursion, separate code).
Method C: prove283/kl.py P_interval = Dyer path formula on the Bruhat interval (dyer.c), 2 reflection orders.
Also prints RSK tableaux and interval statistics."""
import sys,os,time
sys.path.insert(0,'/home/agent/projects/proofs/prove283'); os.chdir('/home/agent/projects/proofs/prove283')
from kl import brute,P_interval,interval_elems
from interval import length
pairs=[("1432765","1634752"),("1432765","3416752"),("1324765","1634752"),("1324765","3416752")]
T=lambda s:tuple(int(c) for c in s)
def rsk(w):
    P=[];Q=[]
    for k,a in enumerate(w,1):
        r=0
        while True:
            if r==len(P): P.append([a]);Q.append([k]);break
            row=P[r]; j=next((j for j,b in enumerate(row) if b>a),None)
            if j is None: row.append(a);Q[r].append(k);break
            row[j],a=a,row[j]; r+=1
    return P,Q
for x,y in pairs:
    E=interval_elems(T(x),T(y)); lx=length(T(x))
    prof=[sum(1 for e in E if length(e)==lx+k) for k in range(length(T(y))-lx+1)]
    print(x,y,'P(x),Q(x)=',rsk(T(x)),' P(y),Q(y)=',rsk(T(y)),' interval rank profile',prof)
    for kind in ('lex','revlex'):
        res,_,_=P_interval(list(T(x)),list(T(y)),kind); p=list(res[T(x)])
        while len(p)>1 and p[-1]==0: p.pop()
        print('   method C dyer',kind,'P =',p)
sys.exit(0)
for x,y in pairs:
    print('   method B',x,y,'P =',P[(T(x),T(y))],'mu =',mu[(T(x),T(y))])
