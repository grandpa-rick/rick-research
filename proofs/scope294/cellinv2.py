import sys; sys.path.insert(0,'../prove281')
from klperm import full_kl, bruhat_le
from collections import defaultdict
exec(open('cellinv.py').read().split("for n in range")[0].split("from collections")[1].split("\n",1)[1])
for n in range(4,int(sys.argv[1])+1):
    W,P,mu=full_kl(n); R={w:rsk(w) for w in W}
    grp=defaultdict(set)
    for x in W:
        for y in W:
            if R[x][1]==R[y][1] and bruhat_le(x,y): grp[(R[x][0],R[y][0])].add(tuple(P[(x,y)]))
    bad=[k for k,v in grp.items() if len(v)>1]
    print(n,"comparable keys",len(grp),"P varies with Q:",len(bad), [grp[k] for k in bad[:3]])
