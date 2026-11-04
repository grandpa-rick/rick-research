src=open('test_b.py').read(); exec(src.split('# 1.')[0])
ok=True;c=0
for N in range(1,6):
  for n in range(2,5):
    for a in range(1,n):
      full=comps(N,n,range(1,n)); sub=comps(N,n,[i for i in range(1,n) if i!=a])
      for C in full:
        s=std(C[0]); S=[x for x in sub if std(x[0])==s]
        kset={sum(1 for ch in w if ch<=a) for w in C}
        if len(S)!=len(kset): ok=False
        c+=1
print('Levi slices connected (one subcomponent per k):',c,ok)
