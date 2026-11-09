import sympy as sp, json
cells=json.load(open('cells5.json')); A=[sp.Matrix(a) for a in cells[3]['A']]
phi=(1+sp.sqrt(5))/2
c=[sp.eye(5)[:,i] for i in range(5)]
N=sp.Matrix.hstack(c[0],c[1],c[2],c[3]-phi*c[1],c[4]-phi*c[0]-c[2]/phi)
Ni=N.inv().applyfunc(sp.radsimp)
for s in range(3): print('N^-1(1+s%d)N='%(s+1),(Ni*A[s]*N).applyfunc(lambda x:sp.nsimplify(sp.radsimp(x))).tolist())
inside=lambda v: all(sp.simplify(x)>=0 for x in (Ni*v).applyfunc(sp.radsimp))
print('c3-c1 in C_max',inside(c[3]-c[1]),'c4-c0',inside(c[4]-c[0]),'c4-c2/phi',inside(c[4]-c[2]/phi))
print('Galois conj invariant?', all(sp.simplify(x)>=0 for s in range(3) for x in (Ni*A[s]*N).applyfunc(lambda x: sp.radsimp(x.subs(sp.sqrt(5),-sp.sqrt(5))))))
