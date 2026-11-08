import time
from kl import *
x=(7,3,2,11,10,6,5,1,15,9,8,4,16,14,13,12)
z=(10,6,2,14,11,7,3,1,15,12,8,4,16,13,9,5)
t0=time.time()
print('l(x)',length(x),'l(z)',length(z),'x<=z',leq(x,z))
print('L(x)',[i+1 for i in ldes(x)],'L(z)',[i+1 for i in ldes(z)])
print('R(x)',[i+1 for i in rdes(x)],'R(z)',[i+1 for i in rdes(z)])
P=kl_interval(x,z,verbose=True,ckpt="ckpt.pkl",tlimit=500)
if P is None: raise SystemExit("partial")
p=P[x]
print('|[x,z]|',len(P))
print('P_{x,z}',p)
d=(length(z)-length(x)-1)
print('mu', p[d//2] if d%2==0 and len(p)>d//2 else 0)
print('Rmemo',len(RMEMO),'time',time.time()-t0)
