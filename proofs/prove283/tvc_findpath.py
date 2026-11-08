"""PROVE283 twin-verdict-check: BFS a right-star path taking (y,z) in the superstandard cell Q0 to the cell of a
dyer2-computed pair (xd,zd) with the same P-tableaux. Search only; verification is done by verifyn_ext.py."""
import json,sys
from collections import deque
sys.path.insert(0,'/home/agent/projects/proofs/wake282')
n=16
from itertools import combinations
def ldes(w):
    p=[0]*(n+2)
    for k,a in enumerate(w): p[a]=k
    return {i for i in range(1,n) if p[i+1]<p[i]}
def sw(i,w): return [i+1 if a==i else (i if a==i+1 else a) for a in w]
def inverse(w):
    r=[0]*n
    for k,a in enumerate(w): r[a-1]=k+1
    return r
def lstar(i,w):
    A=ldes(w)&{i,i+1}
    if len(A)!=1: return None
    c=[y for y in (sw(i,w),sw(i+1,w)) if len(ldes(y)&{i,i+1})==1 and (ldes(y)&{i,i+1})!=A]
    return c[0]
def rstar(i,w):
    v=lstar(i,inverse(w)); return None if v is None else inverse(v)
def bfs(y,z,target):
    start=tuple(y); prev={start:None}; dq=deque([start])
    while dq:
        a=dq.popleft()
        if list(a)==target: break
        for i in range(1,n-1):
            b=rstar(i,list(a))
            if b is None: continue
            b=tuple(b)
            if b not in prev: prev[b]=(a,i); dq.append(b)
    else: return None,len(prev)
    path=[]; a=tuple(target)
    while prev[a] is not None: a,i=prev[a]; path.append(['R',i])
    return path[::-1],len(prev)
def readperms(f):
    L=open(f).read().split(); m=int(L[0]); v=list(map(int,L[1:]))
    return v[:m],v[m:2*m]
jobs={'inst0':('/home/agent/projects/proofs/prove283/in0b.txt',[1,5,9,11,15,16,4,8,10,14,3,7,13,2,6,12],[4,12,13,14,15,16,8,9,10,11,5,6,7,1,2,3]),
      'inst1':('/home/agent/projects/proofs/prove283/in1b.txt',[1,5,7,11,15,16,4,6,10,14,3,9,13,2,8,12],None)}
