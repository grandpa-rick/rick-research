from test_i_ii import *
# Sym: Q_{B(lambda)} components vs SYT descent compositions (Gessel)
def syt(lam):
    N=sum(lam);out=[]
    def rec(T,k):
        if k>N: out.append([r[:] for r in T]);return
        for r in range(len(lam)):
            if len(T[r])<lam[r] and (r==0 or len(T[r-1])>len(T[r])):
                T[r].append(k);rec(T,k+1);T[r].pop()
    rec([[] for _ in lam],1);return out
def des(T):
    row={v:r for r,R in enumerate(T) for v in R}; N=len(row)
    return frozenset(k for k in range(1,N) if row[k+1]>row[k])
bad=0;cnt=0
for n in (2,3,4):
  for N in range(1,6 if n<=3 else 5):
    for lam in partitions(N,n):
        C=word_crystal_component(hw_word(lam),n); Q=quasify(C)
        got=Counter(iso2comp[(n,canon(Q,c))] for c in comps(Q))
        pred=Counter(comp_of_D(des(T),N) for T in syt(lam)); pred=Counter({a:m for a,m in pred.items() if len(a)<=n})
        cnt+=1; bad+= got!=pred
print("Sym: lambdas",cnt,"Q_B(lambda) decomposition != sum_T F_Des(T):",bad)
# Levi: slice map w -> (w|<=a, w|>a - a) is a quasi-crystal iso onto C_s1 x C_s2 (external product)
bad=0;cnt=0
for n in (3,4):
  for N in range(1,5):
    for a in range(1,n):
      for s in set(std(w) for w in itertools.product(range(1,n+1),repeat=N)):
        els=[w for w in itertools.product(range(1,n+1),repeat=N) if std(w)==s]
        for k in range(N+1):
          sl=[w for w in els if sum(c<=a for c in w)==k]
          if not sl: continue
          cnt+=1
          mp={w:(tuple(c for c in w if c<=a),tuple(c-a for c in w if c>a)) for w in sl}
          img=set(mp.values())
          s1={std(u) for u,v in img};s2={std(v) for u,v in img}
          full={(u,v) for u in itertools.product(range(1,a+1),repeat=k) for v in itertools.product(range(1,n-a+1),repeat=N-k) if std(u) in s1 and std(v) in s2}
          ok= len(img)==len(sl) and len(s1)==1 and len(s2)==1 and img==full
          for w in sl:
            u,v=mp[w]
            for i in range(1,n):
              if i==a: continue
              for op in 'ef':
                r=quasi(w,i,op)
                if i<a: t=quasi(u,i,op); exp=None if t is None else (t,v)
                else: t=quasi(v,i-a,op); exp=None if t is None else (u,t)
                if (None if r is None else mp.get(r,'OUT'))!=exp: ok=False
          bad+= not ok
print("Levi slices",cnt,"slice -> C_s1 x C_s2 not an iso:",bad)
