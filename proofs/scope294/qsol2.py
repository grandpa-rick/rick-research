import sys
exec(open('qsolomon.py').read().split("subsets=")[0])
import itertools, sympy as sp
subsets=[frozenset(s) for r in range(n) for s in itertools.combinations(range(n-1),r)]
for tname,t in (("1",F(1)),("1/q",1/q),("-1",F(-1)),("-1/q",-1/q),("q",q),("-q",-q)):
  for name,des in (("R",rdes),):
    for mode in ("sub","sup","eq"):
      cond={"sub":lambda d,I:d<=I,"sup":lambda d,I:d>=I,"eq":lambda d,I:d==I}[mode]
      D=[{w:t**inv(w) for w in W if cond(des(w),I)} for I in subsets]
      M=sp.Matrix([[d.get(w,0) for w in W] for d in D]).T; r0=M.rank(); bad=0
      for a in D:
        for b in D:
          p=mult(a,b); v=sp.Matrix([p.get(w,0) for w in W])
          if M.row_join(v).rank()>r0: bad+=1
      print(n,"q",q,"t",tname,mode,"bad",bad)
