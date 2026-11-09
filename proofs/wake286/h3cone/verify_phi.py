import sympy as sp, itertools, json
cells=json.load(open('cells5.json')); A=[sp.Matrix(a) for a in cells[3]['A']]
tp=(sp.sqrt(5)-1)/2   # 1/phi
def cone_facets(gens):
    F=[]
    for S in itertools.combinations(range(len(gens)),4):
        M=sp.Matrix.hstack(*[gens[i] for i in S]).T
        n=M.nullspace()
        if len(n)!=1: continue
        f=n[0]; vals=[sp.nsimplify(sp.simplify((f.T*v)[0])) for v in gens]
        num=[float(x) for x in vals]
        if all(x>-1e-12 for x in num): pass
        elif all(x<1e-12 for x in num): f=-f; vals=[-x for x in vals]
        else: continue
        assert all(sp.simplify(x)>=0 for x in vals)
        k=[i for i,x in enumerate(vals) if sp.simplify(x)==0]
        F.append((tuple(sp.simplify(x) for x in f), tuple(k)))
    out={}
    for f,k in F: out[k]=f
    return list(out.values())
def check(gens,label):
    F=cone_facets(gens)
    inv=all(sp.simplify((sp.Matrix(f).T*(a*g))[0])>=0 for f in F for a in A for g in gens)
    # pointed: f = sum of facet normals strictly positive on all gens
    fs=sum((sp.Matrix(f) for f in F),sp.zeros(5,1))
    pt=all(sp.simplify((fs.T*g)[0])>0 for g in gens)
    ext=[i for i in range(len(gens)) if sum(1 for f in F if sp.simplify((sp.Matrix(f).T*gens[i])[0])==0)>=4 and
         sp.Matrix.hstack(*[sp.Matrix(f) for f in F if sp.simplify((sp.Matrix(f).T*gens[i])[0])==0]).rank()==4]
    print(label,'facets',len(F),'invariant',inv,'pointed',pt,'extreme gens',ext)
    return F
E=[sp.eye(5)[:,i] for i in range(5)]
t=tp
g=[sp.Matrix(x) for x in [[0,0,-t,0,1],[0,-t,-2*t,1-t,2],[-t,-2*t,1-2*t,2-2*t,1-t],[-2*t,-t,0,1-t,2-2*t]]]
F=check(E+g,'K_phi (t=1/phi)')
for f in F: print('   facet',[sp.nsimplify(x) for x in f])
T=[E[0],E[1],E[2],E[3]-E[1],E[4]-E[0]]
check(E+T[3:],'K_T')
check(E+T[3:]+g,'K_T + K_phi')
t2=sp.Rational(1,2)
g2=[sp.Matrix(x) for x in [[0,0,-t2,0,1],[0,-t2,-2*t2,1-t2,2],[-t2,-2*t2,1-2*t2,2-2*t2,1-t2],[-2*t2,-t2,0,1-t2,2-2*t2]]]
check(E+g2,'K_{1/2}')
