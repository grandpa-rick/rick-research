import sympy as sp, itertools, sys
sys.path.insert(0,'../wake291'); from cap_rank import coeff, basis
x,y,z,u=sp.symbols('x y z u')
E=lambda n: abs(sp.euler(n)) if n%2==0 else 0
# Hankel PD
for n in range(0,7):
    for eps in (0,1):
        H=sp.Matrix(n+1,n+1,lambda a,b:E(2*(eps+a+b)))
        assert H.det()>0
print("Hankel dets >0 n<=6 eps=0,1")
# moment check: int u^{2n} sech(pi u/2)/2 = E_{2n}
for n in range(4):
    val=sp.Integral(u**(2*n)*sp.sech(sp.pi*u/2)/2,(u,-sp.oo,sp.oo)).evalf(20)
    print("moment",n,val,E(2*n))
# specialised lower bound: span of [z^j] e^{-y z^2/2} sech^{(a)}(xz), a=i,i-2,..
for k in range(1,8):
    d=2*k; N=2*k
    ser=sp.series(sp.exp(-y*z**2/2)*sp.sech(u),u,0,N+2).removeO() # placeholder
    rs=[]
    for i in range(d+1):
        j=d-i; vecs=[]
        for a in range(i%2,i+1,2):
            f=sp.diff(sp.sech(u),u,a).subs(u,x*z)
            c=sp.series(sp.exp(-y*z**2/2)*f,z,0,j+1).removeO().coeff(z,j)
            vecs.append(sp.Poly(sp.expand(c),x,y))
        mons=sorted({m for v in vecs for m in v.monoms()})
        M=sp.Matrix(len(vecs),len(mons),lambda r,c: vecs[r].coeff_monomial(x**mons[c][0]*y**mons[c][1]))
        rs.append(M.rank())
    print(k,rs,[min(i//2,(d-i)//2)+1 for i in range(d+1)])
# q-formula equivalence
q=sp.symbols('q')
qi=lambda n,t: sum(t**m for m in range(n))
for k in range(1,15):
    d=2*k
    P=sp.Poly(sp.expand(qi(k//2+1,q**2)*qi(2*((k+1)//2)+1,q)),q).all_coeffs()[::-1]
    assert P==[min(i//2,(d-i)//2)+1 for i in range(d+1)], k
print("q-product formula OK k<=14")
# complement automorphism: [F_{s^c}](F_{u^c}F_{v^c}) = [F_s](F_uF_v)
cmp=lambda w: None if w is None else ''.join('1' if c=='0' else '0' for c in w)
bad=0;tot=0
for L in range(0,6):
  for s in map(''.join,itertools.product('01',repeat=L)):
    d=L+1
    for i in range(d+1):
      for uu in ([None] if i==0 else map(''.join,itertools.product('01',repeat=i-1))):
        for vv in ([None] if i==d else map(''.join,itertools.product('01',repeat=d-i-1))):
          tot+=1; bad+= coeff(uu,vv,s)!=coeff(cmp(uu),cmp(vv),cmp(s))
print("complement",tot,bad)
