import random, time
from run_pol import pol
random.seed(5)
rw=lambda L:''.join(str(random.randint(1,8)) for _ in range(L))
for i in range(6):
    y=rw(400); x=y[:random.randint(5,60)]   # prefix => x<=y likely
    r,dt=pol('D',8,x,y,timeout=500); print(i,repr(r[:80]),f'{dt:.2f}s',flush=True)
