from d8class import *
from collections import defaultdict
import random
n=6; nat=load('D',n); cell=defaultdict(set)
for w,c in nat.items(): cell[c].add(w)
B=Bounder(n); random.seed(1); pools={}
ex=0; tot=0; worst=[]
for c in random.sample(sorted(cell),60):
    x=next(iter(cell[c])); R=rdes(x)
    if R not in pools: pools[R]=[v for v in nat if rdes(v)==R]
    U=bound(x,B,pools[R],log=lambda s:None)
    assert cell[c]<=U
    tot+=1; ex+= U==cell[c]
    if U!=cell[c]: worst.append((len(cell[c]),len(U)))
print(tot,ex,worst)
