"""Cross-checks of mu for an instance: other Q's (mu must be Q-independent), inverse pair, revlex reflection order."""
import sys,json,time,random
sys.path.insert(0,'/home/agent/projects/proofs/prove282')
from kl import P_interval
from interval import length, interval
from qsearch import hookwalk, swaps, score, rowsuper, colsuper
from rskmod import rsk
D=json.load(open('/home/agent/projects/proofs/prove282/open26.json')); B=json.load(open('qbest.json'))
k=int(sys.argv[1]); cap=int(sys.argv[2]) if len(sys.argv)>2 else 60000; I=D[k]
def mu_of(x,z,kind='lex'):
    res,N,E=P_interval(x,z,kind); p=res[tuple(x)]; d=length(z)-length(x)
    return (p[(d-1)//2] if len(p)>(d-1)//2 else 0),N,p
def inv(w): return [w.index(i)+1 for i in range(1,len(w)+1)]
x,z=B[k]['x'],B[k]['z']
print('best Q  lex   ',mu_of(x,z)); print('best Q  revlex',mu_of(x,z,'revlex')); print('inverse pair  ',mu_of(inv(x),inv(z)))
# other Q: neighbours of best Q and random hill-climbs, keep those with small intervals
random.seed(7); seen=0; Qs=swaps(B[k]['Q'])
random.shuffle(Qs)
for Q in Qs:
    lz,lx,x2,z2=score(I,Q)
    if (x2,z2)==(x,z): continue
    assert [list(R) for R in rsk(x2)[0]]==I['Px'] and [list(R) for R in rsk(z2)[0]]==I['Pz']
    t,s,done=interval(x2,z2,cap=cap,verbose=False)
    if not done: print('Q',Q,'interval >',cap); continue
    print('other Q',Q,'lx',lx,'lz',lz,'mu,N,P',mu_of(x2,z2),flush=True); seen+=1
    if seen>=3: break
