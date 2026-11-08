import sys,time
from kl import length
from parab2 import run
from run_inst0 import cases
for name in sys.argv[1:]:
    x,z=cases[name]; t0=time.time()
    p,sz,nr=run(x,z)
    d=length(z)-length(x)-1
    print(name,'P',p,'mu',p[d//2] if d%2==0 and len(p)>d//2 else 0,'W^J size',sz,'reps',nr,'time',time.time()-t0,flush=True)
