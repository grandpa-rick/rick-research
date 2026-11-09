import sys, json, re, glob, pickle
sys.path.insert(0,'/home/agent/projects/proofs/prove286'); sys.path.insert(0,'/home/agent/projects/proofs/wake285')
from decide import *
from d8lib import from_word
K=sys.argv[1]; seed=sys.argv[2]; T=C8[K]
x=from_word(seed,8); Bd=Bounder(8); U=bound(x,Bd,same_R(8,rdes(x)),log=lambda s:None)
assert len(U)==T['dim'] and dict(dist(U))==T['dist']
M=MU(); out=open(f'log_orb_{abs(hash(seed))%10**8}.txt','w')
res=kill_pairs(U,M,lambda s:None)
for r in res: out.write(json.dumps(r)+'\n')
print(K, seed, len(U), Counter(r['verdict'] for r in res)); M.cox.close()
