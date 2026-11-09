import sympy as sp, json
cells=json.load(open('cells5.json'))
phi=(1+sp.sqrt(5))/2; ip=1/phi
def simp(M): return M.applyfunc(lambda x: sp.nsimplify(sp.radsimp(sp.expand(x))))
for ci in [3,5,7,8,9]:
  A=[sp.Matrix(a) for a in cells[ci]['A']]; B=[a.T for a in A]
  words={'e3':[1,3,2],'e4':[1,3],'r_a':[1,2],'r_b':[2,1],'r_c':[2,1,2,3]}
  vecs={'e3':sp.Matrix([0,0,0,1,0]),'e4':sp.Matrix([0,0,0,0,1]),'r_a':sp.Matrix([0,ip,0,1,0]),
        'r_b':sp.Matrix([0,0,1,0,ip]),'r_c':sp.Matrix([ip,0,0,0,1])}
  ok=True
  for k,w in words.items():
    P=sp.eye(5)
    for s in w: P=B[s-1]*P
    lam=sp.symbols('lam'); cp=sp.factor(P.charpoly(lam).as_expr(),extension=sp.sqrt(5))
    e=vecs[k]; Pe=simp(P*e)
    j=[i for i in range(5) if e[i]!=0][0]; L=sp.radsimp(Pe[j]/e[j])
    iseig=simp(Pe-L*e)==sp.zeros(5,1)
    roots=sp.Poly(P.charpoly(lam).as_expr(),lam).all_roots() if False else sp.solve(P.charpoly(lam).as_expr(),lam)
    others=[r for r in roots if sp.simplify(r-L)!=0]
    dom=all(sp.N(abs(r))<sp.N(L)-1e-9 for r in others)
    mult=sp.Poly(P.charpoly(lam).as_expr(),lam).as_expr().subs(lam,L)
    ns=(P.T-L*sp.eye(5)).applyfunc(sp.radsimp).nullspace(simplify=True)
    y=ns[0]; y=y if sum(sp.N(x) for x in y)>0 else -y
    ynn=all(sp.N(x)>-1e-12 for x in y)
    ok&= iseig and dom and ynn and len(ns)==1
    if ci==3: print(k,'word',w,'lambda',sp.nsimplify(L),'charpoly',cp,'eig',iseig,'strict dominant',dom,'left>=0',ynn,'geom mult',len(ns))
  R=sp.Matrix.hstack(*[vecs[k] for k in ['e3','e4','r_a','r_b','r_c']])
  Ri=R.inv()
  conj=[simp(Ri*b*R) for b in B]
  nonneg=all(sp.N(x)>=-1e-12 and (sp.simplify(x)>=0) for C in conj for x in C)
  M=simp((R.T).inv())
  conjA=[simp(M.inv()*a*M) for a in A]
  nonnegA=all(sp.simplify(x)>=0 for C in conjA for x in C)
  print('cell',cells[ci]['cell'][0],'forced-rays OK',ok,'R^-1 B_s R>=0',nonneg,'M^-1 A_s M>=0',nonnegA)
  if ci==3:
    for s,C in enumerate(conjA): print(' M^-1(1+s%d)M ='%(s+1),C.tolist())
    print('C_max generators (columns of M, in basis c0..c4):')
    for j in range(5): print('  ',list(M[:,j]))
