import sys, random
sys.path.insert(0,'/home/agent/projects/proofs/prove286'); sys.path.insert(0,'/home/agent/projects/proofs/wake285')
from decide import *
from orbit import orbit
from d8lib import from_word
K=sys.argv[1]; s=sys.argv[2]; T=C8[K]; x=from_word(s,8); Bd=Bounder(8)
U=bound(x,Bd,same_R(8,rdes(x)),log=lambda s:None); O=orbit(U)
print(K,'all images have target dist:',all(dict(dist(C))==T['dist'] for C in O.values()))
random.seed(3); ok=0; samp=random.sample(list(O.values()),3)
for C in samp:
    y=min(C); V=bound(y,Bd,same_R(8,rdes(y)),log=lambda s:None); ok+= V==C
print(K,'random images re-bounded == image:',ok,'/3')
