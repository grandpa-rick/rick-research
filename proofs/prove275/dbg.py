src=open('test_b.py').read(); exec(src.split('# 1.')[0]); exec('def decon'+src.split('def decon')[1].split('print')[0])
for N in range(1,4):
  for n in range(2,4):
    for a in range(1,n):
      for C in comps(N,n,range(1,n)):
        s=std(C[0]); D=ides(s)
        sub=[c for c in comps(N,n,[i for i in range(1,n) if i!=a]) if std(c[0])==s]
        pred=Counter()
        for k,D1,D2 in decon(D,N):
            A=Fpoly(D1,k,range(a)); B=Fpoly(D2,N-k,range(a,n))
            for x,cx in A.items():
                for y,cy in B.items(): pred[tuple(sorted(x+y))]+=cx*cy
        got=Counter(wt(w,n) for c in sub for w in c)
        ks=[len({sum(1 for ch in w if ch<=a) for w in c}) for c in sub]
        if got!=pred or any(x!=1 for x in ks): print(N,n,a,s,sorted(D),dict(got),dict(pred),ks);break
