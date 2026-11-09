"""Find the complementary F2-piece(s) of a sub-piece P1 among ALL D8 elements with the same right descent set."""
import pickle, random, sys, time, itertools
from collections import Counter
from d8lib import *
n=8; T=pickle.load(open('targets8.pkl','rb')); key=sys.argv[1]; tgt=T[key]['dist']; dim=T[key]['dim']
random.seed(int(sys.argv[2]))
def dist(P): return Counter(ldes(u) for u in P)
def rand_elt():
    p=list(range(1,n+1)); random.shuffle(p); sg=[random.choice((1,-1)) for _ in range(n)]
    if sg.count(-1)%2: sg[0]*=-1
    return tuple(a*b for a,b in zip(p,sg))
sub=lambda d,t: all(t.get(A,0)>=c for A,c in d.items())
t0=time.time()
while True:
    w=rand_elt()
    if ldes(w) not in tgt: continue
    P1=f2_closure(w,n,cap=3000)
    if P1 and len(P1)==int(sys.argv[3]) and sub(dist(P1),tgt): break
R=rdes(w); d1=dist(P1); miss=Counter({A:c-d1.get(A,0) for A,c in tgt.items() if c-d1.get(A,0)})
print('P1',len(P1),'R',sorted(R),'missing size',sum(miss.values()), f'{time.time()-t0:.1f}s',flush=True)
# all elements u with rdes(u)==R  <=> inverse has ldes == R ; enumerate signed perms
pool=[]
for p in itertools.permutations(range(1,n+1)):
    for sg in itertools.product((1,-1),repeat=n-1):
        s0 = 1 if sg.count(-1)%2==0 else -1
        u=(p[0]*s0,)+tuple(a*b for a,b in zip(p[1:],sg))
        # quick right-descent test
        if rdes(u)==R and ldes(u) in miss: pool.append(u)
print('pool (R fixed, L in missing support)',len(pool), f'{time.time()-t0:.1f}s',flush=True)
done=set(P1); found=[]
for u in pool:
    if u in done: continue
    P=f2_closure(u,n,cap=3000)
    if P is None: continue
    done|=P
    if sub(dist(P),miss): found.append(P)
print('pieces (same R) with dist <= missing:',sorted(len(P) for P in found), f'{time.time()-t0:.1f}s')
# exact cover by subsets (small search)
import itertools as it
ds=[dist(P) for P in found]; sols=[]
for k in range(1,6):
    for idx in it.combinations(range(len(found)),k):
        if sum(len(found[i]) for i in idx)!=sum(miss.values()): continue
        tot=Counter()
        for i in idx: tot+=ds[i]
        if tot==miss: sols.append(idx)
    if sols: break
print('exact covers:',[[len(found[i]) for i in s] for s in sols][:10], 'count',len(sols))
pickle.dump(dict(key=key,P1=P1,P2s=found,R=R),open('glue_%s.pkl'%sys.argv[3],'wb'))
