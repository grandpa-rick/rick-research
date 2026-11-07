"""(1) monotonicity of reverse-bump letter in corner height; (2) rows of n (and of n in evac) for parity-failing candidate pairs."""
import sys,json
sys.path.insert(0,'.')
from count_int import partitions, syt
from collections import Counter
def rbump(Q,r):
    Q=[list(R) for R in Q]; a=Q[r].pop()
    for rr in range(r-1,-1,-1):
        row=Q[rr]; j=max(j for j,b in enumerate(row) if b<a); row[j],a=a,row[j]
    return a
def corners(lam): return [r for r in range(len(lam)) if r==len(lam)-1 or lam[r]>lam[r+1]]
if __name__=='__main__':
  viol=0;tot=0;eq=0
  for n in range(3,9):
      for lam in partitions(n):
          for Q in syt(lam):
              cs=corners(lam)
              for i in cs:
                  for j in cs:
                      if i<j:
                          tot+=1; a,b=rbump(Q,i),rbump(Q,j)
                          if a<b: viol+=1
                          if a==b: eq+=1
  print('monotone test (higher corner => letter >=): pairs',tot,'violations',viol,'equalities',eq)
def evac(T):
    T=[list(R) for R in T]; n=sum(map(len,T)); out={}
    for k in range(n,0,-1):
        # delete smallest (1 after relabel): do jdt into (0,0)
        r,c=0,0
        while True:
            down=T[r+1][c] if r+1<len(T) and c<len(T[r+1]) else None
            right=T[r][c+1] if c+1<len(T[r]) else None
            if down is None and right is None: break
            if right is None or (down is not None and down<right): T[r][c]=down; r+=1
            else: T[r][c]=right; c+=1
        T[r].pop(); 
        if not T[r]: T.pop()
        out[(r,c)]=k
        T=[[v-1 for v in R] for R in T]
    lam=[len(R) for R in out and []] 
    rows={}
    for (r,c),k in out.items(): rows.setdefault(r,{})[c]=k
    return [[rows[r][c] for c in sorted(rows[r])] for r in sorted(rows)]
def rowof(T,v): return next(i for i,R in enumerate(T) if v in R)
if __name__=='__main__':
  D=json.load(open('pfail.json')); c=Counter()
  for d in D:
      n=d['n']; Px,Pz=d['Px'],d['Pz']
      a=(rowof(Px,n),rowof(Pz,n)); b=(rowof(evac(Px),n),rowof(evac(Pz),n))
      key=('n:'+('z-higher' if a[1]<a[0] else 'same' if a[1]==a[0] else 'z-lower'), 'evac:'+('z-higher' if b[1]<b[0] else 'same' if b[1]==b[0] else 'z-lower'))
      c[key]+=1
  print(c)
