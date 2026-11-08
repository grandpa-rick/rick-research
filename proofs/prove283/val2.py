"""Validate dyer2 (coset mode, all double-max u) against brute-force KL in S_5, S_6."""
import random,subprocess
from kl import brute
for n in (5,6):
    W,P,mu=brute(n); random.seed(100+n); fails=chk=0
    for z in random.sample(W,80):
        xs=[u for u in W if (u,z) in P]; x=random.choice(xs)
        inp=f"{n}\n{' '.join(map(str,x))}\n{' '.join(map(str,z))}\n"
        out=subprocess.run(['./dyer2','coset','dump'],input=inp,capture_output=True,text=True).stdout
        for line in out.split('\n'):
            if line.startswith('U'):
                a,b=line[1:].split(':'); u=tuple(map(int,a.split())); p=list(map(int,b.split()))
                while len(p)>1 and p[-1]==0: p.pop()
                chk+=1; fails+=(p!=P[(u,tuple(z))])
    print('S',n,'checked',chk,'fails',fails)
