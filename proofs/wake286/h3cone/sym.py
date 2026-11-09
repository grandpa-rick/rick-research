import json, sympy as sp
cells=json.load(open('cells5.json'))
t=sp.symbols('t',positive=True)
c=cells[3]; A=[sp.Matrix(a) for a in c['A']]
E=sp.eye(5)
for (i,j) in [(4,0),(4,2),(3,1)]:
    v=E[:,i]-t*E[:,j]
    print('v=e%d - t e%d'%(i,j))
    orb=[v]; fr=[(v,'v')]
    while fr:
        new=[]
        for u,nm in fr:
            for k,a in enumerate(A):
                w=sp.simplify(a*u)
                print('  (1+s%d)%s ='%(k+1,nm), list(w))
        fr=[]
    # just one level printed; now recursively (numeric t=1/20 earlier gave 3 elems)
