import sys; sys.path.insert(0,'../prove281')
from klperm import full_kl, bruhat_le, inv
from collections import defaultdict
def rsk(w):
    P=[];Q=[]
    for k,a in enumerate(w):
        r=0
        while True:
            if r==len(P): P.append([a]);Q.append([k+1]);break
            row=P[r]; j=next((j for j,b in enumerate(row) if b>a),None)
            if j is None: row.append(a);Q[r].append(k+1);break
            row[j],a=a,row[j]; r+=1
    return tuple(map(tuple,P)),tuple(map(tuple,Q))
for n in range(3,int(sys.argv[1])+1):
    W,P,mu=full_kl(n)
    R={w:rsk(w) for w in W}
    # sanity: number of nontrivial P
    nt=sum(1 for k,v in P.items() if v!=[1])
    grp=defaultdict(set); bru=defaultdict(set)
    for x in W:
        for y in W:
            if R[x][1]!=R[y][1]: continue
            key=(R[x][0],R[y][0])
            le=bruhat_le(x,y)
            bru[key].add(le)
            grp[key].add(tuple(P.get((x,y),[])) if le else None)
    bad=[k for k,v in grp.items() if len(v)>1]
    badb=[k for k,v in bru.items() if len(v)>1]
    print(n,"nontrivP",nt,"keys",len(grp),"Bruhat-noninvariant",len(badb),"P-noninvariant",len(bad))
    for k in bad[:3]: print("  ",k,grp[k])
