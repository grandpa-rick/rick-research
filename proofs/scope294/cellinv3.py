import sys; sys.path.insert(0,'../prove281')
from klperm import full_kl, bruhat_le
from collections import defaultdict
exec(open('cellinv.py').read().split("for n in range")[0].split("from collections")[1].split("\n",1)[1])
def le(a,b):
    a=list(a)+[0]*(len(b)-len(a)); b=list(b)+[0]*(len(a)-len(b)); return all(x<=y for x,y in zip(a,b))
for n in (5,6):
    W,P,mu=full_kl(n); R={w:rsk(w) for w in W}
    grp=defaultdict(dict); allQ=defaultdict(set)
    for x in W:
        for y in W:
            if R[x][1]==R[y][1]:
                key=(R[x][0],R[y][0]); allQ[key].add(R[x][1])
                if bruhat_le(x,y): grp[key][R[x][1]]=tuple(P[(x,y)])
    nontot=0; varying=0; fullcomp=0; maxfirstrow=0
    for k,d in grp.items():
        vals=set(d.values())
        if len(vals)<2: continue
        varying+=1
        if len(d)==len(allQ[k]): fullcomp+=1
        vs=list(vals)
        if any(not(le(a,b) or le(b,a)) for a in vs for b in vs): nontot+=1
    print(n,"varying keys",varying,"of which comparable for all Q",fullcomp,"non-totally-ordered",nontot)
    full=[k for k,d in grp.items() if len(d)==len(allQ[k])]
    nontriv=[k for k in full if any(v!=(1,) for v in grp[k].values())]
    multiQ=[k for k in nontriv if len(allQ[k])>1]
    print("   all-Q-comparable keys",len(full),"with P!=1",len(nontriv),"and >1 Q",len(multiQ), "polys",sorted(set(v for k in multiQ for v in grp[k].values())))
