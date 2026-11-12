from eng import A_rw,B_rw
def w(*parts):  # padded word -> s
    P=''.join(parts); assert P[0]=='r' and P[-1]=='u'; return P[1:-1]
def vec(*terms):
    d={}
    for c,P in terms:
        k=w(P); d[k]=d.get(k,0)+c
    return {k:v for k,v in d.items() if v}
ok=0
for a in range(1,12):
  for b in range(1,12):
    L=a+b-2
    if L>=3: # (i) hook P=r^a u^b, a,b>=2
      s=w('r'*a,'u'*b)
      if a>=2 and b>=2:
        X=[(1,'r'*(a-1)+'u'*(b-1))]+([(1,'r'*(a-2)+'u'*b)] if a>=3 else [])
        Y=[(1,'r'*(a-1)+'u'*(b-1))]+([(1,'r'*a+'u'*(b-2))] if b>=3 else [])
        assert A_rw(s)==vec(*X,*[(-c,P) for c,P in Y]) and B_rw(s)==vec(*Y),(a,b); ok+=1
    if a+b>=3: # (ii) P = r u^b r^a u
      s=w('r','u'*b,'r'*a,'u')
      W1='r'+'u'*b+'r'*(a-2)+'u'; W2='r'+'u'*(b-2)+'r'*a+'u'; W3='r'+'u'*(b-1)+'r'*(a-1)+'u'
      assert A_rw(s)==vec(*([(1,W1)] if a>=2 else []),*([(-1,W2)] if b>=2 else [])),(a,b)
      assert B_rw(s)==vec((1,W3),*([(1,W2)] if b>=2 else [])); ok+=1
  # (iii) P= r u r^a u u
  s=w('r','u','r'*a,'uu'); X1='ru'+'r'*(a-1)+'u'; X2='ru'+'r'*(a-2)+'uu'
  assert A_rw(s)==(vec((1,X2)) if a>=2 else vec((-1,X1)))
  assert B_rw(s)==vec((1,'r'*(a+1)+'u'),(1,'r'*a+'uu'),(1,X1)); ok+=1
  # (iv) P = r r u^b r u  (b plays role)
  b=a; s=w('rr','u'*b,'ru'); V1='r'+'u'*(b-1)+'ru'; V2='rr'+'u'*(b-2)+'ru'
  assert A_rw(s)==(vec((-1,V2)) if b>=2 else vec((1,V1)))
  assert B_rw(s)==vec((1,'rr'+'u'*b),(1,'r'+'u'*(b+1)),*([(1,V2),(1,V1)] if b>=2 else [])); ok+=1
print('family formulas ok',ok)
